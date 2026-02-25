import os
import json
import re
from transformers import AutoTokenizer

# ================= 配置区域 =================
# 1. 存放 wav 文件的本地目录
WAV_DIR = "/Users/housiyuan/project/music/MuseAdapt.github.io/audio/ours/transfer"
# 2. 包含大字典的 JSON 文件路径
JSON_PATH = "/Users/housiyuan/project/music/MuseAdapt.github.io/resources/test_share_song.json"
# 3. 输出的 Markdown 文件路径
OUTPUT_MD_PATH = "resources/generated_cards.md"
# 4. T5 最大 Token 长度
MAX_TOKENS = 128
# ============================================

# 预加载 T5 Tokenizer 以便精准计算长度
print("正在加载 T5 Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("t5-base")

# HTML 卡片模板（使用占位符，避免 f-string 和 CSS 大括号冲突）
CARD_TEMPLATE = """<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example [EXAMPLE_NUM]: Piano ➔ Acoustic Guitar</h4>
  <p><b>Song Name:</b> <i>[SONG_NAME]</i></p>
  <p><b>Text Prompt:</b> <i>[TEXT_PROMPT]</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/[FILE_NAME].wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>
"""

def truncate_text_by_sentence(text, max_tokens=128):
    """
    按整句截断文本，确保总 token 数不超过 max_tokens，且保留的是完整的句子。
    """
    # 按照英文的句号、叹号、问号分隔，并保留标点符号
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    
    valid_text = ""
    for sentence in sentences:
        if not sentence:
            continue
        
        # 尝试将当前句子加进去
        test_text = (valid_text + " " + sentence).strip()
        
        # 使用 T5 Tokenizer 计算长度 (T5 默认包含 </s> 结束符)
        tokens = tokenizer.encode(test_text)
        
        if len(tokens) <= max_tokens:
            valid_text = test_text
        else:
            # 如果加上这句超标了，就丢弃这句并停止，保证剩下的是完整句
            break
            
    return valid_text

def main():
    # 1. 读取 JSON 数据
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        meta_data = json.load(f)

    # 2. 获取目录下的所有 wav 文件
    if not os.path.exists(WAV_DIR):
        print(f"❌ 目录 {WAV_DIR} 不存在！")
        return

    wav_files = [f for f in os.listdir(WAV_DIR) if f.endswith('.wav')]
    wav_files.sort() # 排序，让 Example 编号更稳定
    
    generated_html = ""
    example_num = 1

    print(f"🔍 找到 {len(wav_files)} 个音频文件，开始生成代码...")

    # 3. 遍历文件并生成卡片
    for wav_file in wav_files:
        # 去掉 .wav 后缀作为字典的 key
        file_name = os.path.splitext(wav_file)[0]
        
        if file_name not in meta_data:
            print(f"⚠️ 警告: JSON 中找不到 {file_name} 的元数据，跳过该项。")
            continue
            
        # 提取信息
        song_info = meta_data[file_name]
        song_name = song_info.get("song_id", "Unknown Song")
        raw_text = song_info.get("text", "")
        
        # 核心逻辑：进行 T5 完整句子级别的截断
        truncated_text = truncate_text_by_sentence(raw_text, MAX_TOKENS)
        
        # 替换模板内容
        card_html = CARD_TEMPLATE.replace("[EXAMPLE_NUM]", str(example_num))
        card_html = card_html.replace("[SONG_NAME]", song_name)
        card_html = card_html.replace("[TEXT_PROMPT]", truncated_text)
        # 注意 URL 里的空格，这里直接把你的文件名填入
        card_html = card_html.replace("[FILE_NAME]", file_name)
        
        generated_html += card_html + "\n\n"
        example_num += 1

    # 4. 写入输出文件
    with open(OUTPUT_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(generated_html)
        
    print(f"✅ 生成完毕！成功生成 {example_num - 1} 个卡片，已保存至 {OUTPUT_MD_PATH}。")

if __name__ == "__main__":
    main()