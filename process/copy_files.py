import os
import shutil


def copy_matched_audios(ref_dir, dir_a, dir_b):
    """
    根据 ref_dir 中的文件名，将 dir_a 中同名的文件复制到 dir_b。

    :param ref_dir: 包含目标音频名的参考目录
    :param dir_a: 源音频所在的目录 (A)
    :param dir_b: 要复制到的目标目录 (B)
    """

    # 1. 检查参考目录和源目录是否存在
    if not os.path.exists(ref_dir):
        print(f"❌ 错误: 参考目录不存在 -> {ref_dir}")
        return
    if not os.path.exists(dir_a):
        print(f"❌ 错误: 源目录A不存在 -> {dir_a}")
        return

    # 2. 如果目标目录B不存在，则自动创建
    os.makedirs(dir_b, exist_ok=True)

    # 3. 获取参考目录中的所有目标文件名
    # 常见音频后缀，可根据你的实际情况增删
    valid_extensions = ('.wav', '.mp3', '.flac', '.m4a', '.ogg')

    target_filenames = []
    for f in os.listdir(ref_dir):
        # 确保是文件，且后缀在我们的列表中（忽略大小写），同时也排除了 .DS_Store 等隐藏文件
        if os.path.isfile(os.path.join(ref_dir, f)) and f.lower().endswith(valid_extensions):
            target_filenames.append(f)

    total_targets = len(target_filenames)
    print(f"🔍 在参考目录中找到了 {total_targets} 个目标音频文件。")

    if total_targets == 0:
        print("⚠ 没有找到任何音频文件，程序结束。")
        return

    # 4. 开始在 A 目录中查找并复制到 B 目录
    success_count = 0
    missing_files = []

    print(f"🚀 开始从 目录A 复制到 目录B...")

    for filename in target_filenames:
        source_path = os.path.join(dir_a, filename)
        dest_path = os.path.join(dir_b, filename)

        # 检查文件在目录 A 中是否存在
        if os.path.exists(source_path):
            try:
                # copy2 会保留文件的元数据 (修改时间、权限等)
                shutil.copy2(source_path, dest_path)
                success_count += 1
            except Exception as e:
                print(f"❌ 复制 {filename} 时出错: {e}")
        else:
            missing_files.append(filename)

    # 5. 打印最终统计结果
    print("-" * 40)
    print("📊 复制任务完成统计：")
    print(f"✅ 成功复制: {success_count} / {total_targets} 个文件")

    if missing_files:
        missing_count = len(missing_files)
        print(f"⚠ 目录A中缺失: {missing_count} 个文件")
        print("缺失的文件列表 (前10个):")
        for f in missing_files[:10]:
            print(f"  - {f}")
        if missing_count > 10:
            print(f"  ... 以及其他 {missing_count - 10} 个文件。")


if __name__ == "__main__":
    # ================= 配置路径 =================
    # 请将下面三个路径替换为你服务器上的实际绝对路径

    # 里面装着你想要收集名字的音频的目录
    REFERENCE_DIR = "/Users/housiyuan/project/music/MuseAdapt.github.io/audio/ours/transfer"

    # 目录 A (源文件库，拥有大量音频)
    DIR_A = "/Users/housiyuan/Downloads/cqt_melody_key_text/self_rec"

    # 目录 B (你想把提取出来的音频放到的目标位置)
    DIR_B = "/Users/housiyuan/project/music/MuseAdapt.github.io/audio/ours/self_rec"
    # ============================================

    copy_matched_audios(REFERENCE_DIR, DIR_A, DIR_B)