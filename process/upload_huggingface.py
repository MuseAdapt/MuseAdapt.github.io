from huggingface_hub import HfApi

# 1. 初始化 API
api = HfApi()

# 2. 配置你的路径和仓库信息 (请替换为你的真实信息)
LOCAL_AUDIO_DIR = "/Users/housiyuan/project/music/MuseAdapt.github.io/audio" 
REPO_ID = "MuseAdapt/MuseAdapt_Demo"

print(f"🚀 开始将 {LOCAL_AUDIO_DIR} 整个目录上传至 Hugging Face: {REPO_ID}...")

# 3. 执行文件夹批量上传
api.upload_folder(
    folder_path=LOCAL_AUDIO_DIR,
    repo_id=REPO_ID,
    repo_type="dataset",       # 明确指定是数据集仓库
    path_in_repo=".",          # 上传到 HF 仓库的根目录
    ignore_patterns=[".DS_Store", "*.git*", "__pycache__"] # 自动忽略系统垃圾文件
)

print("✅ 所有音频上传完成！目录结构已完美保留！")