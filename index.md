<div style="text-align: center"> 

<h1> MuseAdapt: Melody-Aware Music Adaptation <br> via Structure-Texture Disentanglement </h1>

Anonymous Authors

<p>
Supporting webpage for ICML 2026<br>
</p>

</div>

# Abstract

Melody-conditioned music generation is a cornerstone of controllable synthesis. However, existing self-reconstruction paradigms, which condition models on melodic features extracted from the target audio, often fail to separate semantic melody from acoustic texture. This entanglement encourages models to replicate the source audio rather than perform genuine melodic adaptation. To bridge this gap, we define melody-aware music adaptation (MAMA), a task focused on generating stylistically diverse music that preserves melodic identity without enforcing frame-level reconstruction. We introduce MAMA-20k, the first large-scale dataset for this task, featuring weakly paired segments with shared melodic skeletons but distinct acoustic realizations. Leveraging this data, we propose MuseAdapt, a diffusion-based framework that achieves disentangled melodic control via a contrastive encoder. Experiments demonstrate that MuseAdapt significantly outperforms self-reconstruction baselines in cross-instrument and real-world scenarios, highlighting the necessity of disentangled supervision for robust music synthesis.

**Open Source**: We will open-source our model, code, dataset metadata, and the data processing pipeline upon paper acceptance.
<br>

<p align="center">
<img src="method.png">
</p>

# 🎧 Audio Samples

As discussed in our paper, existing melody-conditioned models trained via the **self-reconstruction paradigm** often suffer from **texture leakage**. Because these models learn to reconstruct the target audio using control signals extracted from the exact same audio, they struggle to separate semantic melody from acoustic texture. Consequently, they tend to overfit to the control conditions and ignore text prompts during real-world inference.

To demonstrate the superiority of **MuseAdapt** in decoupling structure from texture, we present our audio samples in two distinct parts. The baseline models include: [MusicGen-Stereo-Melody](https://huggingface.co/facebook/musicgen-stereo-melody)<a href="#note1" id="note1ref">[1]</a>, [MusicGen-Stereo-Melody-Large](https://huggingface.co/facebook/musicgen-stereo-melody-large)<a href="#note1" id="note1ref">[1]</a>, [MuseControlLite](https://huggingface.co/fundwotsai2001/Text-to-Music_control_family)<a href="#note2" id="note2ref">[2]</a>, [SongEcho-base](https://huggingface.co/fundwotsai2001/Text-to-Music_control_family)<a href="#note3" id="note3ref">[3]</a>, and [SongEcho-large](https://huggingface.co/fundwotsai2001/Text-to-Music_control_family)<a href="#note3" id="note3ref">[3]</a>. All generated samples are approximately **47 seconds** long.

All examples below are drawn from the **MAMA-20k test set**. In particular, the “Source Audio (Melodic Skeleton)” and “Reference Audio (Target Texture)” are themselves test-set excerpts, giving a direct sense of the dataset’s audio quality and the quality of its weak melodic alignment.

<div style="background-color: #f8f9fa; padding: 14px 16px; border-radius: 10px; margin: 20px 0 24px; border: 1px solid #dee2e6;">
  <div style="font-weight: bold; color: #444; margin-bottom: 10px; font-size: 1.05em;">Quick Navigation</div>
  <div style="display: flex; flex-wrap: wrap; gap: 10px; text-align: center;">
    <a href="#part1" style="flex: 1; min-width: 220px; text-decoration: none; color: inherit; background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 14px; display: block;">
      <div style="font-weight: bold; margin-bottom: 4px;">Part 1: Music Adaptation Task</div>
      <div style="font-size: 0.9em; color: #666;">Real-world melody-aware adaptation examples</div>
    </a>
    <a href="#part2" style="flex: 1; min-width: 220px; text-decoration: none; color: inherit; background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 14px; display: block;">
      <div style="font-weight: bold; margin-bottom: 4px;">Part 2: The Generalization Gap</div>
      <div style="font-size: 0.9em; color: #666;">Self-reconstruction vs. adaptation comparison</div>
    </a>
  </div>
</div>

---

<div id="part1"></div>

## Part 1: Music Adaptation Task
In this challenging real-world scenario, models are tasked with generating a stylistically distinct audio segment based on a text prompt, while preserving the perceptual melodic identity of the source audio. **Our model (MuseAdapt) successfully disentangles the melody and follows the text prompt, whereas baselines often simply replicate the source texture.**

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 1: Violin ➔ Alto Saxophone</h4>
  <p><b>Song Name:</b> <i>Don't Wanna Know</i></p>
  <p><b>Text Prompt:</b> <i>This instrumental piece features a vibrant ensemble consisting of an alto saxophone, an electric keyboard, an electric bass, and a drum kit. The saxophone's bright, reedy timbre leads with expressive, soaring melodies, contrasted by the warm, rounded, and percussive tone of the electric keyboard providing rhythmic and harmonic accompaniment.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Don't Wanna Know_rn6t841tzL8_iENs7cGB42Q_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 2: Flute ➔ Full String Orchestra</h4>
  <p><b>Song Name:</b> <i>Drag Me Down</i></p>
  <p><b>Text Prompt:</b> <i>The music features a full string orchestra, including violins, violas, cellos, and double basses, which employ techniques ranging from crisp pizzicato to smooth, connected legato phrases. The timbre of the violins is bright and soaring, carrying the primary melodies, while the lower strings provide a rich, warm, and resonant foundation.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 3: Brass Instruments ➔ Violin</h4>
  <p><b>Song Name:</b> <i>Liar</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features two distinct sections. The primary section is led by a virtuosic violin, which possesses a bright, sharp, and resonant timbre, delivering rapid and ornate melodic phrases. It is accompanied by a simple, digital-sounding synthesizer and a driving electronic drum machine. This initial part is a high-energy fusion of folk music, possibly of Eastern European or Middle Eastern influence, and modern electronic dance music, characterized by its fast, celebratory tempo and repetitive, dance-oriented structure.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Liar_lNQZwPKL-n4_XXiuyH3CGtk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 4: Guitar ➔ Alto Saxophone</h4>
  <p><b>Song Name:</b> <i>Like I'm Gonna Lose You</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a lead alto saxophone, an acoustic guitar, a bass guitar, and a subtle drum machine. The saxophone's performance is marked by its expressive, fluid articulation and prominent vibrato, while the acoustic guitar provides a crisp, rhythmic accompaniment.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Like I'm Gonna Lose You_GB-AKi7_EYo_8n0bYPTM2f4_5.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 5: Flute ➔ Guitar</h4>
  <p><b>Song Name:</b> <i>Like I'm Gonna Lose You</i></p>
  <p><b>Text Prompt:</b> <i>This instrumental piece features a core ensemble of an acoustic guitar, an electric guitar, a bass guitar, and a drum kit. The acoustic guitar provides a rhythmic and harmonic foundation with a bright, metallic, and resonant timbre, while the lead electric guitar, characterized by a warm, rounded, and slightly gritty timbre, executes soulful melodic lines using smooth bends and sustained notes.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 6: Flute ➔ Piano</h4>
  <p><b>Song Name:</b> <i>Little Do You Know</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece is performed on a solo piano, which articulates both the melody and harmonic accompaniment with a smooth, connected touch. The piano's timbre is consistently warm and mellow; its higher register produces clear, bell-like tones, while the lower notes provide a soft, resonant foundation, resulting in a gentle and non-percussive sound quality.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 7: Violin ➔ Acoustic Guitar</h4>
  <p><b>Song Name:</b> <i>party favor</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a solo steel-string acoustic guitar, whose timbre is warm and resonant with a bright, clear attack from the fingerpicking technique; occasional subtle string slides add an organic texture. The genre is best described as an acoustic fingerstyle instrumental, in the style of Folk music, characterized by a slow, contemplative tempo and a structure built on arpeggiated diatonic chord progressions.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/party favor_zVIX6YG_BGw_ICknngfS1N8_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 8: Saxphone ➔ Erhu (a Chinese two-stringed fiddle)</h4>
  <p><b>Song Name:</b> <i>斑马斑马</i></p>
  <p><b>Text Prompt:</b> <i>This piece is a poignant instrumental work featuring an acoustic guitar, an erhu (a Chinese two-stringed fiddle), and a cello. The acoustic guitar provides a clean, arpeggiated harmonic foundation with a bright, resonant timbre.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/斑马斑马_uuGG4Q0iy-s_GBFAfAkx2Zg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>

<details id="part1-folded" style="margin-bottom: 28px;">
  <summary style="list-style: none; cursor: pointer; background-color: #f8f9fa; padding: 14px 16px; border-radius: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #444;">
    More Part 1 Examples
    <span style="font-weight: normal; color: #666; margin-left: 8px;">(Click to expand the remaining examples)</span>
  </summary>
  <div style="margin-top: 16px;">

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 9: Violin ➔ Harp</h4>
    <p><b>Song Name:</b> <i>Darkside</i></p>
    <p><b>Text Prompt:</b> <i>This piece features a solo harp, whose timbre is consistently bright and resonant, producing a clear, bell-like quality in its higher register and a warm, full-bodied tone in its lower notes. Stylistically, the music aligns with a contemplative genre such as New Age or solo instrumental, characterized by a slow, flowing tempo and a consonant, tonal harmony that creates a peaceful atmosphere.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 10: Saxphone ➔ Violin</h4>
    <p><b>Song Name:</b> <i>Intentions</i></p>
    <p><b>Text Prompt:</b> <i>This piece features a blend of acoustic and electronic elements, led by an expressive solo violin with a warm, rich timbre that employs liberal vibrato for emotional depth. It is accompanied by a synthesized lo-fi hip-hop beat, characterized by a soft, thudding kick drum, a crisp snare, and light, sizzly hi-hats, all underpinned by a deep, smooth sub-bass and ethereal, airy synth pads that provide a continuous harmonic layer.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 11: Piano ➔ Guitar</h4>
    <p><b>Song Name:</b> <i>Intentions</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features an electric guitar, whose timbre is clean, warm, and slightly mellow, enhanced by a subtle reverb that creates a spacious and airy quality. The genre is best described as instrumental indie or lo-fi, characterized by a cyclical chord progression, a slow and steady tempo, and a melodic, improvisational style that builds in complexity through layering.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 12: Piano and Flute ➔ Acoustic Guitar and Saxophone</h4>
    <p><b>Song Name:</b> <i>Kiss Me</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a duet between an acoustic guitar and a saxophone. The acoustic guitar provides a rhythmic and harmonic foundation, characterized by a bright, clear, and resonant timbre from its consistently strummed chords. A saxophone, likely an alto, plays the lead melody with a smooth, reedy, and soulful timbre that is both expressive and lyrical.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 13: Flute ➔ Violin</h4>
    <p><b>Song Name:</b> <i>Liar</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a small ensemble dominated by a solo violin, accompanied by a harpsichord-like keyboard and a cello providing the bass foundation. The violin exhibits a bright, agile timbre, performing intricate and virtuosic melodic lines, while the keyboard's sound is distinctly plucked and metallic, creating a crisp harmonic texture.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 14: Flute ➔ Electric Guitar</h4>
    <p><b>Song Name:</b> <i>Like I'm Gonna Lose You</i></p>
    <p><b>Text Prompt:</b> <i>This piece is an instrumental blues-rock or hard rock track driven by a core ensemble of electric guitars, bass, and drums. The lead electric guitar is the primary focus, characterized by a heavily distorted and saturated timbre that is both gritty and searing, employing expressive techniques like string bends and vibrato.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 15: Electric guitar ➔ Violin and Acoustic Guitar</h4>
    <p><b>Song Name:</b> <i>Like I'm Gonna Lose You</i></p>
    <p><b>Text Prompt:</b> <i>This instrumental piece primarily features a violin and an acoustic guitar. The violin, acting as the lead melodic voice, showcases notable features such as extensive vibrato, smooth legato phrasing in lyrical sections, and crisp, rapid articulation in more virtuosic passages. The acoustic guitar provides a steady rhythmic and harmonic foundation with a blend of arpeggiated and strummed chords.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 16: Electronic Guitar ➔ Violin</h4>
    <p><b>Song Name:</b> <i>New Rules</i></p>
    <p><b>Text Prompt:</b> <i>This piece features a vibrant interplay between a reedy, expressive saxophone and a crisp, virtuosic violin, both playing with agile articulation, set against a modern rhythm section of an electronic drum machine and a deep, funky synthesizer bass.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 17: Piano ➔ Violin</h4>
    <p><b>Song Name:</b> <i>party favor</i></p>
    <p><b>Text Prompt:</b> <i>This piece features a violin and a piano, where the violin carries the primary melody with a smooth, legato articulation, and the piano provides both harmonic and rhythmic accompaniment. The violin possesses a warm, resonant timbre that becomes bright and clear in its higher registers, while the piano offers a contrasting percussive and crisp sound quality.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 18: Flute ➔ Piano</h4>
    <p><b>Song Name:</b> <i>party favor</i></p>
    <p><b>Text Prompt:</b> <i>This piece is an instrumental work for solo piano, which has a clear, bright, and resonant timbre, with delicate, bell-like high notes and a warm, full-bodied lower register. The genre is modern classical or neo-classical, characterized by its lyrical melodicism, accessible tonal harmony, and a structured form that unfolds at a moderate tempo.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 19: Flute ➔ Soprano Saxophone</h4>
    <p><b>Song Name:</b> <i>因为爱情</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a lead soprano saxophone, whose bright, warm, and slightly reedy timbre is used to deliver smooth, legato melodies, accompanied by an acoustic guitar that provides a resonant and woody harmonic foundation through arpeggiated chords. A mellow bass guitar and subtle percussion are introduced later to add depth.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 20: Violin ➔ Acoustic Guitar</h4>
    <p><b>Song Name:</b> <i>我愿意</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a single instrument, which is a synthesized acoustic guitar, played in a clean, fingerpicked style with distinct, individual notes. The timbre of the instrument is bright and clear, with a gentle attack and moderate sustain, creating a smooth and rounded sound quality. The music aligns with the genre of a gentle instrumental ballad or folk piece, characterized by its slow tempo, simple diatonic harmony, and a clear, lyrical melody.</i></p>   
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 21: Saxphone ➔ Piano</h4>
    <p><b>Song Name:</b> <i>我的好兄弟</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a solo piano, which presents both the melody and harmony with a clean and distinct articulation. The piano's timbre is clear and resonant, characterized by a bright, bell-like quality in the higher melodic lines and a warm, full-bodied tone in the supporting chords.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 22: Saxphone ➔ Piano</h4>
    <p><b>Song Name:</b> <i>斑马斑马</i></p>
    <p><b>Text Prompt:</b> <i>This piece of music features a solo acoustic piano, which possesses a warm, mellow, and resonant timbre; the sound is rich and full-bodied in the lower register while remaining bright and clear in the higher passages, with articulation that is predominantly smooth and legato. The genre is best described as modern classical or Neo-Romantic, reminiscent of a nocturne or a slow character piece, defined by its lyrical melody, rich tonal harmony, and a slow, flowing tempo.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 23: Saxphone ➔ String Instrument</h4>
    <p><b>Song Name:</b> <i>斑马斑马</i></p>
    <p><b>Text Prompt:</b> <i>The music primarily features a classical nylon-string guitar, a solo string instrument (resembling a cello or viola), and a string ensemble. The guitar has a warm and mellow timbre, while the solo string is characterized by its rich, resonant, and mournful tone, often employing a smooth, legato articulation with expressive vibrato. The accompanying string ensemble provides a lush, cohesive, and atmospheric background.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 24: Erhu (a Chinese two-stringed fiddle) ➔ Piano</h4>
    <p><b>Song Name:</b> <i>枫</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece exclusively features a solo piano, played with a resonant and clear sound that utilizes legato articulation for melodies and both arpeggiated and block chords for harmonic support. The piano's timbre is rich and warm, shifting from a mellow, gentle quality in quiet passages to a brighter, more brilliant and percussive character during moments of high intensity.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 25: Violin ➔ Flute</h4>
    <p><b>Song Name:</b> <i>童话</i></p>
    <p><b>Text Prompt:</b> <i>This piece of contemporary instrumental music features a piano, a flute, and a string section. The piano opens the piece with a clear and resonant sound, playing arpeggiated chords that establish the harmonic foundation. The flute enters with the main melody, exhibiting a soft, airy, and breathy timbre that feels intimate and gentle. The string section provides a lush, warm, and smooth background, with a rich collective timbre that swells to create a full, cinematic texture.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 26: Violin ➔ Piano</h4>
    <p><b>Song Name:</b> <i>至少还有你</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece is a solo piano composition. The instrument is played with clean and precise articulation, ensuring that both the melodic lines in the right hand and the arpeggiated accompaniment in the left are clearly distinguishable. The piano's timbre is bright and clear in its upper register, creating a singing quality for the melody, while the lower register provides a warm and resonant harmonic foundation.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🎵 Example 27: Piano ➔ Alto Saxophone</h4>
    <p><b>Song Name:</b> <i>被遗忘的时光</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features an alto saxophone with a warm, smooth, and expressive timbre as the primary melodic instrument, accompanied by a piano with a clear and resonant sound, a fingerpicked acoustic guitar providing a crisp rhythmic texture, and a lush string section that adds a rich, velvety depth.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
  </div>

  </div>
</details>

---

<br>

<div id="part2"></div>

## Part 2: The Generalization Gap (Self-Reconstruction vs. Adaptation)

**Why do baselines fail in Part 1?** This section reveals the root cause by comparing each model's performance across two settings: **Self-Reconstruction** (where the melody condition is extracted from the target itself) and **Music Adaptation** (where the melody condition comes from a different source).

In the self-reconstruction task, baselines sound excellent because they are operating within their biased training paradigm. However, when shifting to the adaptation task, their ability to follow text descriptions drops drastically (as evidenced by the sharp decline in CLAP scores in our paper). By comparing the two tasks side-by-side for each model below, you can hear this **"Generalization Gap"** clearly in the baselines, whereas **MuseAdapt maintains highly consistent quality and text-adherence across both scenarios.**

<div id="part2-visible">

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🔄 Example 1: Violin ➔ Harp</h4>
  <p><b>Song Name:</b> <i>Darkside</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a solo harp, whose timbre is consistently bright and resonant, producing a clear, bell-like quality in its higher register and a warm, full-bodied tone in its lower notes. Stylistically, the music aligns with a contemplative genre such as New Age or solo instrumental, characterized by a slow, flowing tempo and a consonant, tonal harmony that creates a peaceful atmosphere.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
    <div></div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Target Audio</b>
      </div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Source Audio</b>
      </div>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>

  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🔄 Example 2: Flute ➔ Full String Orchestra</h4>
  <p><b>Song Name:</b> <i>Drag Me Down</i></p>
  <p><b>Text Prompt:</b> <i>The music features a full string orchestra, including violins, violas, cellos, and double basses, which employ techniques ranging from crisp pizzicato to smooth, connected legato phrases. The timbre of the violins is bright and soaring, carrying the primary melodies, while the lower strings provide a rich, warm, and resonant foundation.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
    <div></div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Target Audio</b>
      </div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Source Audio</b>
      </div>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Drag Me Down_E--mt0BjxOo_S49hNSDDgWo.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>

  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🔄 Example 3: Piano ➔ Guitar</h4>
  <p><b>Song Name:</b> <i>Intentions</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features an electric guitar, whose timbre is clean, warm, and slightly mellow, enhanced by a subtle reverb that creates a spacious and airy quality. The genre is best described as instrumental indie or lo-fi, characterized by a cyclical chord progression, a slow and steady tempo, and a melodic, improvisational style that builds in complexity through layering.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
    <div></div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Target Audio</b>
      </div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Source Audio</b>
      </div>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>

  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🔄 Example 4: Flute ➔ Guitar</h4>
  <p><b>Song Name:</b> <i>Like I'm Gonna Lose You</i></p>
  <p><b>Text Prompt:</b> <i>This instrumental piece features a core ensemble of an acoustic guitar, an electric guitar, a bass guitar, and a drum kit. The acoustic guitar provides a rhythmic and harmonic foundation with a bright, metallic, and resonant timbre, while the lead electric guitar, characterized by a warm, rounded, and slightly gritty timbre, executes soulful melodic lines using smooth bends and sustained notes.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
    <div></div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Target Audio</b>
      </div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Source Audio</b>
      </div>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Like I'm Gonna Lose You_GCwGFSleIo4_GB-AKi7_EYo_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>

  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🔄 Example 5: Violin ➔ Flute</h4>
  <p><b>Song Name:</b> <i>Little Do You Know</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a flute, a piano, and an acoustic guitar. The flute, with its airy, bright, and smooth timbre, carries the primary melody with expressive articulation. The piano provides a mellow and resonant harmonic foundation with a soft touch, while the acoustic guitar adds a crisp, plucked texture that enriches the rhythmic and harmonic layers.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
    <div></div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Target Audio</b>
      </div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Source Audio</b>
      </div>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>

  </div>
</div>

<div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🔄 Example 6: Flute ➔ Piano</h4>
  <p><b>Song Name:</b> <i>Little Do You Know</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece is performed on a solo piano, which articulates both the melody and harmonic accompaniment with a smooth, connected touch. The piano's timbre is consistently warm and mellow; its higher register produces clear, bell-like tones, while the lower notes provide a soft, resonant foundation, resulting in a gentle and non-percussive sound quality.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
      <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
    <div></div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Target Audio</b>
      </div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
      <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
      <div style="font-size: 0.85em; color: #666;">
        Melody Condition is extracted from the <b>Source Audio</b>
      </div>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
      <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Little Do You Know_QB-JGUBRyzQ_bOIRLEpdiRk_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
    </div>

  </div>
</div>


</div>

<details id="part2-folded" style="margin-bottom: 28px;">
  <summary style="list-style: none; cursor: pointer; background-color: #f8f9fa; padding: 14px 16px; border-radius: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #444;">
    More  Part 2 Examples
    <span style="font-weight: normal; color: #666; margin-left: 8px;">(Click to expand the remaining examples)</span>
  </summary>
  <div style="margin-top: 16px;">

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 7: Flute ➔ Piano</h4>
    <p><b>Song Name:</b> <i>party favor</i></p>
    <p><b>Text Prompt:</b> <i>This piece is an instrumental work for solo piano, which has a clear, bright, and resonant timbre, with delicate, bell-like high notes and a warm, full-bodied lower register. The genre is modern classical or neo-classical, characterized by its lyrical melodicism, accessible tonal harmony, and a structured form that unfolds at a moderate tempo.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 8: Piano ➔ Violin</h4>
    <p><b>Song Name:</b> <i>party favor</i></p>
    <p><b>Text Prompt:</b> <i>This piece features a violin and a piano, where the violin carries the primary melody with a smooth, legato articulation, and the piano provides both harmonic and rhythmic accompaniment. The violin possesses a warm, resonant timbre that becomes bright and clear in its higher registers, while the piano offers a contrasting percussive and crisp sound quality.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 9: Saxphone ➔ Piano</h4>
    <p><b>Song Name:</b> <i>斑马斑马</i></p>
    <p><b>Text Prompt:</b> <i>This piece of music features a solo acoustic piano, which possesses a warm, mellow, and resonant timbre; the sound is rich and full-bodied in the lower register while remaining bright and clear in the higher passages, with articulation that is predominantly smooth and legato.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 10: Piano ➔ Alto Saxophone</h4>
    <p><b>Song Name:</b> <i>被遗忘的时光</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features an alto saxophone with a warm, smooth, and expressive timbre as the primary melodic instrument, accompanied by a piano with a clear and resonant sound, a fingerpicked acoustic guitar providing a crisp rhythmic texture, and a lush string section that adds a rich, velvety depth.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 11: Erhu (a Chinese two-stringed fiddle) ➔ Piano</h4>
    <p><b>Song Name:</b> <i>枫</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece exclusively features a solo piano, played with a resonant and clear sound that utilizes legato articulation for melodies and both arpeggiated and block chords for harmonic support. The piano's timbre is rich and warm, shifting from a mellow, gentle quality in quiet passages to a brighter, more brilliant and percussive character during moments of high intensity.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 12: Flute ➔ Saxphone</h4>
    <p><b>Song Name:</b> <i>清明雨上</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a prominent alto saxophone, a piano providing harmonic support, a deep electric bass, and a drum kit. The saxophone's playing is smooth and articulate, creating a fluid melodic line. The timbre of the alto saxophone is warm, reedy, and expressive with a breathy quality, while the piano has a bright yet mellow acoustic tone.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>
  
  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 13: Saxphone ➔ Piano</h4>
    <p><b>Song Name:</b> <i>我的好兄弟</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a solo piano, which presents both the melody and harmony with a clean and distinct articulation. The piano's timbre is clear and resonant, characterized by a bright, bell-like quality in the higher melodic lines and a warm, full-bodied tone in the supporting chords.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>

  <div class="audio-example" style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
    <h4>🔄 Example 14: Violin ➔ Acoustic Guitar</h4>
    <p><b>Song Name:</b> <i>我愿意</i></p>
    <p><b>Text Prompt:</b> <i>This musical piece features a single instrument, which is a synthesized acoustic guitar, played in a clean, fingerpicked style with distinct, individual notes. The timbre of the instrument is bright and clear, with a gentle attack and moderate sustain, creating a smooth and rounded sound quality.</i></p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
        <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Target Audio</div>
        <audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 15px;">
      <div></div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 1: Self-Reconstruction</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Target Audio</b>
        </div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 12px 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
        <div style="font-weight: bold; color: #444; margin-bottom: 5px; font-size: 1.05em;">Task 2: Music Adaptation</div>
        <div style="font-size: 0.85em; color: #666;">
          Melody Condition is extracted from the <b>Source Audio</b>
        </div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px;">
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; color: #d9534f; border-right: 1px solid #eee; padding-right: 10px;">MuseAdapt (Ours) ✨</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/self_rec/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MuseControlLite</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/self_rec/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Base</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/self_rec/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">SongEcho-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/self_rec/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/self_rec/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
      <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px; display: grid; grid-template-columns: 180px 1fr 1fr; gap: 15px; align-items: center; text-align: center;">
        <div style="font-weight: bold; border-right: 1px solid #eee; padding-right: 10px;">MusicGen-Melody-Large</div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/self_rec/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
        <div><audio data-src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" preload="none" controls style="width: 100%; outline: none;"></audio></div>
      </div>
    </div>
  </div>

  </div>
</details>


# References 

<a id="note1" href="#note1ref">[1]</a> Copet, J., Kreuk, F., Gat, I., Remez, T., Kant, D., Synnaeve, G., Adi, Y., and Defossez, A. Simple and controllable music generation. In Proc. NeurIPS, New Orleans, 2023.

<a id="note2" href="#note2ref">[2]</a> Tsai, F.-D., Wu, S.-L., Lee, W., Yang, S.-P., Chen, B.-R., Cheng, H.-C., and Yang, Y.-H. Musecontrollite: Multifunctional music generation with lightweight conditioners. In Proc. ICML, Vancouver, 2025.

<a id="note3" href="#note3ref">[3]</a> Li, S., Li, Y., Wang, Z., Zhang, Y., Wu, F., Deussen, O., Lee, T.-Y., and Dong, W. Songecho: Towards cover
song generation via instance-adaptive element-wise linear modulation. In Proc. ICLR, Rio de Janeiro, 2026.

<script>
  const TIMINGS = {
    part2VisibleDelayMs: 5000,              // part2默认可见区域延迟加载
    foldedWarmupStartMs: 3500,              // 折叠区域在没有操作3.5s后开始预热
    foldedWarmupIdleIntervalMs: 500,        // 折叠区域正常预热间隔0.5s
    foldedWarmupPlayingIntervalMs: 1000,    // 折叠区域在有音频播放时的预热间隔1.0s
    detailsQueueIntervalMs: 500,
    part2ObserverRootMargin: "500px 0px"
  };
  const BUFFER_THRESHOLDS = {
    resumeWarmupSec: 15,
    pauseWarmupSec: 8
  };

  const connection =
    navigator.connection || navigator.mozConnection || navigator.webkitConnection || {};
  const part2Visible = document.getElementById("part2-visible");
  const part1Folded = document.getElementById("part1-folded");
  const part2Folded = document.getElementById("part2-folded");
  const part2Link = document.querySelector('a[href="#part2"]');

  let part2VisibleLoaded = false;
  let foldedWarmupStarted = false;
  let foldedWarmupQueue = [];
  let foldedWarmupTimer = null;
  let allowWarmupWhilePlaying = false;

  function whenIdle(callback, timeout = 1200) {
    if ("requestIdleCallback" in window) {
      requestIdleCallback(callback, { timeout });
    } else {
      setTimeout(callback, timeout);
    }
  }

  function hasWarmableConnection() {
    if (connection.saveData) return false;
    const effectiveType = connection.effectiveType || "";
    return !/^(slow-2g|2g)$/.test(effectiveType);
  }

  function getActivePlayingAudio() {
    return [...document.querySelectorAll("audio")].find(
      audio => !audio.paused && !audio.ended && audio.currentTime > 0
    ) || [...document.querySelectorAll("audio")].find(
      audio => !audio.paused && !audio.ended
    ) || null;
  }

  function getBufferedAhead(audio) {
    if (!audio || !audio.buffered || audio.buffered.length === 0) return 0;

    const currentTime = audio.currentTime;
    for (let i = 0; i < audio.buffered.length; i += 1) {
      const start = audio.buffered.start(i);
      const end = audio.buffered.end(i);

      if (currentTime >= start && currentTime <= end) {
        return Math.max(0, end - currentTime);
      }

      if (start > currentTime) {
        return Math.max(0, end - start);
      }
    }

    return 0;
  }

  function getWarmupState() {
    const activeAudio = getActivePlayingAudio();

    if (!activeAudio) {
      allowWarmupWhilePlaying = false;
      return {
        canWarm: true,
        intervalMs: TIMINGS.foldedWarmupIdleIntervalMs
      };
    }

    const bufferedAhead = getBufferedAhead(activeAudio);
    if (!allowWarmupWhilePlaying && bufferedAhead >= BUFFER_THRESHOLDS.resumeWarmupSec) {
      allowWarmupWhilePlaying = true;
    }
    if (allowWarmupWhilePlaying && bufferedAhead < BUFFER_THRESHOLDS.pauseWarmupSec) {
      allowWarmupWhilePlaying = false;
    }

    return {
      canWarm: allowWarmupWhilePlaying,
      intervalMs: TIMINGS.foldedWarmupPlayingIntervalMs
    };
  }

  function getExampleCards(container) {
    return container ? [...container.querySelectorAll(".audio-example")] : [];
  }

  function loadAudio(audio, preload = "none") {
    if (!audio || audio.getAttribute("src") || !audio.dataset.src) return;

    audio.preload = preload;
    audio.setAttribute("src", audio.dataset.src);
    audio.load();
  }

  function loadExample(example, preload = "none") {
    if (!example) return;

    example.querySelectorAll("audio[data-src]").forEach(audio => {
      loadAudio(audio, preload);
    });
  }

  function ensurePart2VisibleLoaded(preload = "none") {
    if (part2VisibleLoaded || !part2Visible) return;

    part2VisibleLoaded = true;
    getExampleCards(part2Visible).forEach(example => {
      loadExample(example, preload);
    });
  }

  function prioritizeAudio(audio) {
    if (!audio || !audio.matches("audio[data-src]")) return;

    loadAudio(audio, "auto");

    const example = audio.closest(".audio-example");
    if (example) {
      whenIdle(() => loadExample(example, "none"), 200);
    }
  }

  function scheduleFoldedWarmupTick(delay = TIMINGS.foldedWarmupIdleIntervalMs) {
    if (foldedWarmupTimer || !foldedWarmupQueue.length) return;

    foldedWarmupTimer = setTimeout(() => {
      foldedWarmupTimer = null;
      processFoldedWarmupQueue();
    }, delay);
  }

  function nudgeFoldedWarmup(delay = 0) {
    if (foldedWarmupTimer) {
      clearTimeout(foldedWarmupTimer);
      foldedWarmupTimer = null;
    }

    scheduleFoldedWarmupTick(delay);
  }

  function processFoldedWarmupQueue() {
    if (!foldedWarmupStarted || !foldedWarmupQueue.length) return;

    if (!hasWarmableConnection()) return;

    if (document.hidden) {
      scheduleFoldedWarmupTick(TIMINGS.foldedWarmupIdleIntervalMs);
      return;
    }

    const warmupState = getWarmupState();
    if (!warmupState.canWarm) {
      scheduleFoldedWarmupTick(warmupState.intervalMs);
      return;
    }

    const nextExample = foldedWarmupQueue.shift();
    loadExample(nextExample, "none");
    scheduleFoldedWarmupTick(warmupState.intervalMs);
  }

  function startFoldedWarmup() {
    if (foldedWarmupStarted || !hasWarmableConnection()) return;

    foldedWarmupStarted = true;
    foldedWarmupQueue = [
      ...getExampleCards(part1Folded),
      ...getExampleCards(part2Folded)
    ];
    scheduleFoldedWarmupTick();
  }

  if (location.hash === "#part2") {
    ensurePart2VisibleLoaded();
  }

  part2Link?.addEventListener("click", () => {
    ensurePart2VisibleLoaded();
  });

  window.addEventListener("hashchange", () => {
    if (location.hash === "#part2") {
      ensurePart2VisibleLoaded();
    }
  });

  if ("IntersectionObserver" in window && part2Visible) {
    const part2Observer = new IntersectionObserver(
      entries => {
        if (entries.some(entry => entry.isIntersecting)) {
          ensurePart2VisibleLoaded();
          part2Observer.disconnect();
        }
      },
      { rootMargin: TIMINGS.part2ObserverRootMargin }
    );

    part2Observer.observe(part2Visible);
  }

  ["pointerdown", "touchstart", "focusin"].forEach(eventName => {
    document.addEventListener(
      eventName,
      event => {
        const audio = event.target.closest?.("audio[data-src]");
        if (audio) {
          prioritizeAudio(audio);
        }
      },
      true
    );
  });

  document.querySelectorAll("details").forEach(details => {
    details.addEventListener("toggle", () => {
      if (!details.open) return;

      const examples = getExampleCards(details);
      examples.slice(0, 2).forEach(example => {
        loadExample(example, "none");
      });

      whenIdle(() => {
        examples.slice(2).forEach((example, index) => {
          setTimeout(() => loadExample(example, "none"), index * TIMINGS.detailsQueueIntervalMs);
        });
      }, 600);
    });
  });

  document.addEventListener("visibilitychange", () => {
    if (!document.hidden && foldedWarmupStarted) {
      nudgeFoldedWarmup(0);
    }
  });

  ["play", "playing", "pause", "progress", "waiting", "stalled", "ended"].forEach(
    eventName => {
      document.addEventListener(
        eventName,
        () => {
          if (foldedWarmupStarted) {
            nudgeFoldedWarmup(0);
          }
        },
        true
      );
    }
  );

  window.addEventListener("load", () => {
    if (!part2VisibleLoaded) {
      setTimeout(() => {
        whenIdle(() => ensurePart2VisibleLoaded(), 800);
      }, TIMINGS.part2VisibleDelayMs);
    }

    setTimeout(() => {
      whenIdle(() => {
        ensurePart2VisibleLoaded();
        startFoldedWarmup();
      }, 1500);
    }, TIMINGS.foldedWarmupStartMs);
  });
</script>
