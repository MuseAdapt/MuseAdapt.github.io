<div style="text-align: center"> 

<h1> MuseAdapt: Melody-Aware Music Adaptation <br> via Structure-Texture Disentanglement </h1>

Anonymous Authors

<p>
Supporting webpage for ICML 2026<br>
</p>

</div>


<div style="text-align: justify"> 

# Abstract

Melody-conditioned music generation is a cornerstone of controllable synthesis. However, existing self-reconstruction paradigms, which condition models on melodic features extracted from the target audio, often fail to separate semantic melody from acoustic texture. 
This entanglement encourages models to replicate the source audio rather than perform genuine melodic adaptation. 
To bridge this gap, we define melody-aware music adaptation (MAMA), a task focused on generating stylistically diverse music that preserves melodic identity without enforcing frame-level reconstruction. 
We introduce MAMA-20k, the first large-scale dataset for this task, featuring weakly paired segments with shared melodic skeletons but distinct acoustic realizations. 
Leveraging this data, we propose MuseAdapt, a diffusion-based framework that achieves disentangled melodic control via a contrastive encoder. 
Experiments demonstrate that MuseAdapt significantly outperforms self-reconstruction baselines in cross-instrument and real-world scenarios, highlighting the necessity of disentangled supervision for robust music synthesis.
</div>

<br>

<p align="center">
<img src="method.png">
</p>

# 🎧 Audio Samples

As discussed in our paper, existing melody-conditioned models trained via the **self-reconstruction paradigm** often suffer from **texture leakage**. Because these models learn to reconstruct the target audio using control signals extracted from the exact same audio, they struggle to separate semantic melody from acoustic texture. Consequently, they tend to overfit to the control conditions and ignore text prompts during real-world inference.

To demonstrate the superiority of **MuseAdapt** in decoupling structure from texture, we present our audio samples in two distinct parts. The baseline models include: [MusicGen-Stereo-Melody](https://huggingface.co/facebook/musicgen-stereo-melody)<a href="#note1" id="note1ref">[1]</a>, [MusicGen-Stereo-Melody-Large](https://huggingface.co/facebook/musicgen-stereo-melody-large)<a href="#note1" id="note1ref">[1]</a>, [MuseControlLite](https://huggingface.co/fundwotsai2001/Text-to-Music_control_family)<a href="#note2" id="note2ref">[2]</a>, [SongEcho-base](https://huggingface.co/fundwotsai2001/Text-to-Music_control_family)<a href="#note3" id="note3ref">[3]</a>, and [SongEcho-large](https://huggingface.co/fundwotsai2001/Text-to-Music_control_family)<a href="#note3" id="note3ref">[3]</a>. All generated samples are approximately **47 seconds** long.

---

## Part 1: Music Adaptation Task
In this challenging real-world scenario, models are tasked with generating a stylistically distinct audio segment based on a text prompt, while preserving the perceptual melodic identity of the source audio. **Our model (MuseAdapt) successfully disentangles the melody and follows the text prompt, whereas baselines often simply replicate the source texture.**


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 1: Flute ➔ Violin</h4>
  <p><b>Song Name:</b> <i>Boom Clap</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a blend of rock and classical instrumentation, led by a virtuosic electric violin with a bright, cutting timbre that soars over the ensemble. The foundation is provided by thick, distorted electric guitars, a deep and driving bass guitar, and a powerful rock drum kit, all while atmospheric synthesizer pads add a subtle, ethereal layer in the background.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 2: Flute ➔ Piano</h4>
  <p><b>Song Name:</b> <i>Darkside</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a solo acoustic piano, exhibiting a rich and versatile sound. In its softer sections, the piano's timbre is warm and resonant, with a bell-like quality in the higher register, while in more powerful moments, it becomes bright, full-bodied, and percussive. The music belongs to the Romantic or Neo-Romantic genre, styled as an expressive character piece with a fluid structure, lyrical melodies, and complex, chromatic harmonies.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Darkside_SLNi2WEZ4GY_Dgdsj2gSra4_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 3: Flute ➔ Saxophone</h4>
  <p><b>Song Name:</b> <i>Darkside</i></p>
  <p><b>Text Prompt:</b> <i>The piece features a saxophone as the lead instrument, accompanied by a synthesized plucked instrument in the introduction, lush synth pads for harmony, a deep synth bass, and a crisp electronic drum kit. The saxophone's timbre is warm, reedy, and highly expressive, shifting from a gentle, breathy tone in softer passages to a bright and powerful sound during more intense moments.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Darkside_aBbPeYzkXvU_0uCaxb2Y24I_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 4: Violin ➔ Harp</h4>
  <p><b>Song Name:</b> <i>Darkside</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a solo harp, whose timbre is consistently bright and resonant, producing a clear, bell-like quality in its higher register and a warm, full-bodied tone in its lower notes. Stylistically, the music aligns with a contemplative genre such as New Age or solo instrumental, characterized by a slow, flowing tempo and a consonant, tonal harmony that creates a peaceful atmosphere.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Darkside_yxhhDNIv3P4_cB2l0OnjG6M_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 5: Flute ➔ Violin</h4>
  <p><b>Song Name:</b> <i>Don't Wanna Know</i></p>
  <p><b>Text Prompt:</b> <i>The piece prominently features a solo violin with a bright, expressive, and often poignant timbre, which navigates both lyrical melodies and virtuosic passages. This is accompanied by a warm, smooth-sounding string ensemble or synthesizer pad that provides a lush harmonic foundation, and a gentle plucked string instrument that establishes a rhythmic pulse.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Don't Wanna Know_GAwqvLMAHVY_RtZwhMzr5DY_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 6: Violin ➔ Alto Saxophone</h4>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 7: Flute ➔ Full String Orchestra</h4>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 8: Saxphone ➔ Violin</h4>
  <p><b>Song Name:</b> <i>Intentions</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a blend of acoustic and electronic elements, led by an expressive solo violin with a warm, rich timbre that employs liberal vibrato for emotional depth. It is accompanied by a synthesized lo-fi hip-hop beat, characterized by a soft, thudding kick drum, a crisp snare, and light, sizzly hi-hats, all underpinned by a deep, smooth sub-bass and ethereal, airy synth pads that provide a continuous harmonic layer.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Intentions_2qofYO_o-14_6ZbEkPmEFO4_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 9: Saxphone ➔ Electric Guitar</h4>
  <p><b>Song Name:</b> <i>Intentions</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a heavily overdriven electric guitar, a clean and deep bass guitar, a crisp-sounding drum machine, and a simple synthesizer that appears only in the introduction. The timbre of the electric guitar is raw, gritty, and powerful, dominating the mix with its distorted texture, while the bass provides a smooth, rounded low-end foundation.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Intentions_2qofYO_o-14_cMs3Dsn9yZU_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 10: Saxphone ➔ Electric Guitar</h4>
  <p><b>Song Name:</b> <i>Intentions</i></p>
  <p><b>Text Prompt:</b> <i>This piece features an electric guitar, a bass guitar, and an electronic drum kit, with the electric guitar taking the lead melodic role through expressive techniques like string bends, slides, and vibrato. The timbre of the electric guitar is warm and slightly gritty with a gentle overdrive, while the electronic percussion has a crisp, ticking hi-hat and a soft, thudding kick drum, and the bass guitar provides a deep, rounded, foundational tone.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Intentions_2qofYO_o-14_wWKnsE039xw_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 11: Piano ➔ Guitar</h4>
  <p><b>Song Name:</b> <i>Intentions</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features an electric guitar, whose timbre is clean, warm, and slightly mellow, enhanced by a subtle reverb that creates a spacious and airy quality. The genre is best described as instrumental indie or lo-fi, characterized by a cyclical chord progression, a slow and steady tempo, and a melodic, improvisational style that builds in complexity through layering.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Intentions_TxIP8CvsrUU_sS9-zYTpl_s_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 12: Piano and Flute ➔ Acoustic Guitar and Saxophone</h4>
  <p><b>Song Name:</b> <i>Kiss Me</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a duet between an acoustic guitar and a saxophone. The acoustic guitar provides a rhythmic and harmonic foundation, characterized by a bright, clear, and resonant timbre from its consistently strummed chords. A saxophone, likely an alto, plays the lead melody with a smooth, reedy, and soulful timbre that is both expressive and lyrical.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Kiss Me_57-CfYJlzK0_LPaD-UtBWXI_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 13: Flute ➔ Violin</h4>
  <p><b>Song Name:</b> <i>Liar</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a small ensemble dominated by a solo violin, accompanied by a harpsichord-like keyboard and a cello providing the bass foundation. The violin exhibits a bright, agile timbre, performing intricate and virtuosic melodic lines, while the keyboard's sound is distinctly plucked and metallic, creating a crisp harmonic texture.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Liar_aDNT-1w-KYw_v3zaAMHauGg_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 14: Brass Instruments ➔ Violin</h4>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 15: Flute ➔ Electric Guitar</h4>
  <p><b>Song Name:</b> <i>Like I'm Gonna Lose You</i></p>
  <p><b>Text Prompt:</b> <i>This piece is an instrumental blues-rock or hard rock track driven by a core ensemble of electric guitars, bass, and drums. The lead electric guitar is the primary focus, characterized by a heavily distorted and saturated timbre that is both gritty and searing, employing expressive techniques like string bends and vibrato.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Like I'm Gonna Lose You_31-7mgkSx0Q_K7jMUB6OvPY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 16: Guitar ➔ Alto Saxophone</h4>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 17: Flute ➔ Guitar</h4>
  <p><b>Song Name:</b> <i>Like I'm Gonna Lose You_GCwGFSleIo4</i></p>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 18: Electric guitar ➔ Violin</h4>
  <p><b>Song Name:</b> <i>Like I'm Gonna Lose You</i></p>
  <p><b>Text Prompt:</b> <i>This instrumental piece primarily features a violin and an acoustic guitar. The violin, acting as the lead melodic voice, showcases notable features such as extensive vibrato, smooth legato phrasing in lyrical sections, and crisp, rapid articulation in more virtuosic passages. The acoustic guitar provides a steady rhythmic and harmonic foundation with a blend of arpeggiated and strummed chords.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Like I'm Gonna Lose You_K7jMUB6OvPY_ueabJWy2kSA_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 19: Violin ➔ Flute</h4>
  <p><b>Song Name:</b> <i>Little Do You Know</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a flute, a piano, and an acoustic guitar. The flute, with its airy, bright, and smooth timbre, carries the primary melody with expressive articulation. The piano provides a mellow and resonant harmonic foundation with a soft touch, while the acoustic guitar adds a crisp, plucked texture that enriches the rhythmic and harmonic layers.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Little Do You Know_Oaaus4O3X5M_hMtkDYaC9RE_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 20: Flute ➔ Piano</h4>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 21: Flute ➔ Harp</h4>
  <p><b>Song Name:</b> <i>Little Do You Know</i></p>
  <p><b>Text Prompt:</b> <i>This solo instrumental piece features a harp, which produces a sound characterized by its clear, plucked articulation and warm, resonant sustain. The timbre of the harp is bright, gentle, and ethereal, with each note possessing a distinct, bell-like attack followed by a smooth, lingering decay that creates a rich, layered texture.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Little Do You Know_hMtkDYaC9RE_Yg4od-uKkFI_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 22: Flute and String Orchestra ➔ Piano</h4>
  <p><b>Song Name:</b> <i>Mull Of Kintyre</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a piano and a string orchestra, with the piano exhibiting a warm, resonant timbre and the strings providing a lush, smooth, and cohesive texture. The music aligns with the neo-classical or cinematic genre, characterized by its slow, contemplative tempo, tonal harmony, and a structure that progresses from an intimate solo piano introduction to a grander, more expansive orchestral section.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Mull Of Kintyre_0Bct9Wd6OGo_0OnlxhZghWQ.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 23: Electronic Guitar ➔ Violin</h4>
  <p><b>Song Name:</b> <i>New Rules</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a vibrant interplay between a reedy, expressive saxophone and a crisp, virtuosic violin, both playing with agile articulation, set against a modern rhythm section of an electronic drum machine and a deep, funky synthesizer bass.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/New Rules_J8yl-QMPdqw_r5ZGEvMZZoQ_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 24: Saxphone ➔ Electronic Guitar</h4>
  <p><b>Song Name:</b> <i>New Rules</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a distorted electric guitar, a synthesized bass, and a drum machine. The electric guitar serves as the lead instrument, playing complex melodic solos and rhythmic riffs with a fuzzy, aggressive, and bright timbre achieved through heavy distortion. Providing the low-end foundation, the synth bass has a round, deep, and smooth electronic timbre that lays down a simple, pulsing pattern.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/New Rules_yuDFwigunzY_zSKVx14l-rQ_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 25: Piano ➔ Violin</h4>
  <p><b>Song Name:</b> <i>party favor</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a violin and a piano, where the violin carries the primary melody with a smooth, legato articulation, and the piano provides both harmonic and rhythmic accompaniment. The violin possesses a warm, resonant timbre that becomes bright and clear in its higher registers, while the piano offers a contrasting percussive and crisp sound quality.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/party favor_UtUTLHf08UQ_zVIX6YG_BGw_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 26: Piano ➔ Flute ➔ Piano</h4>
  <p><b>Song Name:</b> <i>party favor</i></p>
  <p><b>Text Prompt:</b> <i>This piece is an instrumental work for solo piano, which has a clear, bright, and resonant timbre, with delicate, bell-like high notes and a warm, full-bodied lower register. The genre is modern classical or neo-classical, characterized by its lyrical melodicism, accessible tonal harmony, and a structured form that unfolds at a moderate tempo.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/party favor_pDeIopcyP8g_UtUTLHf08UQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 27: Violin ➔ Acoustic Guitar</h4>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 28: Flute ➔ Soprano Saxophone</h4>
  <p><b>Song Name:</b> <i>因为爱情</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a lead soprano saxophone, whose bright, warm, and slightly reedy timbre is used to deliver smooth, legato melodies, accompanied by an acoustic guitar that provides a resonant and woody harmonic foundation through arpeggiated chords. A mellow bass guitar and subtle percussion are introduced later to add depth.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/因为爱情_MJJUgVuBCIc_vZWlcF4Aqac_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 29: Saxphone ➔ Piano</h4>
  <p><b>Song Name:</b> <i>因为爱情</i></p>
  <p><b>Text Prompt:</b> <i>This piece is a solo piano performance characterized by its rich and resonant timbre; the instrument produces a warm, full-bodied sound in the lower registers and a clear, bright tone in the higher melodic lines. The genre is reminiscent of romantic or contemporary classical music, possibly a film score, featuring lush harmonies and a flowing, lyrical structure with a moderate tempo that employs expressive rubato.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/因为爱情_u31qN0VDM_k_jsDAEXYgklg_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 30: Violin ➔ Acoustic Guitar</h4>
  <p><b>Song Name:</b> <i>我愿意</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a single instrument, which is a synthesized acoustic guitar, played in a clean, fingerpicked style with distinct, individual notes. The timbre of the instrument is bright and clear, with a gentle attack and moderate sustain, creating a smooth and rounded sound quality. The music aligns with the genre of a gentle instrumental ballad or folk piece, characterized by its slow tempo, simple diatonic harmony, and a clear, lyrical melody.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/我愿意_6s_q8LkyOQc_h5lrsN79yCc_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 31: Saxphone ➔ Piano</h4>
  <p><b>Song Name:</b> <i>我的好兄弟</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a solo piano, which presents both the melody and harmony with a clean and distinct articulation. The piano's timbre is clear and resonant, characterized by a bright, bell-like quality in the higher melodic lines and a warm, full-bodied tone in the supporting chords.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/我的好兄弟_CC3ik6EpROk_7TicCoD2sGs_6.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 32: Saxphone ➔ Violin</h4>
  <p><b>Song Name:</b> <i>斑马斑马</i></p>
  <p><b>Text Prompt:</b> <i>This piece features an acoustic guitar, a male vocalist, and a solo string instrument, likely a violin or viola. The acoustic guitar is fingerpicked, creating a gentle and intricate harmonic foundation. The string instrument is played with significant expression, featuring smooth, connected notes and a rich vibrato.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/斑马斑马_uuGG4Q0iy-s_3Hyj1I2fO_w_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 33: Saxphone ➔ Erhu (a Chinese two-stringed fiddle)</h4>
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


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 34: Saxphone ➔ Piano</h4>
  <p><b>Song Name:</b> <i>斑马斑马</i></p>
  <p><b>Text Prompt:</b> <i>This piece of music features a solo acoustic piano, which possesses a warm, mellow, and resonant timbre; the sound is rich and full-bodied in the lower register while remaining bright and clear in the higher passages, with articulation that is predominantly smooth and legato. The genre is best described as modern classical or Neo-Romantic, reminiscent of a nocturne or a slow character piece, defined by its lyrical melody, rich tonal harmony, and a slow, flowing tempo.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/斑马斑马_uuGG4Q0iy-s_czu_8VAvP4U_3.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 35: Saxphone ➔ String Instrument</h4>
  <p><b>Song Name:</b> <i>斑马斑马</i></p>
  <p><b>Text Prompt:</b> <i>The music primarily features a classical nylon-string guitar, a solo string instrument (resembling a cello or viola), and a string ensemble. The guitar has a warm and mellow timbre, while the solo string is characterized by its rich, resonant, and mournful tone, often employing a smooth, legato articulation with expressive vibrato. The accompanying string ensemble provides a lush, cohesive, and atmospheric background.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/斑马斑马_uuGG4Q0iy-s_u1wVezN0c10_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 36: Erhu (a Chinese two-stringed fiddle) ➔ Piano</h4>
  <p><b>Song Name:</b> <i>枫</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece exclusively features a solo piano, played with a resonant and clear sound that utilizes legato articulation for melodies and both arpeggiated and block chords for harmonic support. The piano's timbre is rich and warm, shifting from a mellow, gentle quality in quiet passages to a brighter, more brilliant and percussive character during moments of high intensity.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/枫_lmi54fAwzRc_mwUbFi4rRIs_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 37: Flute ➔ Acoustic Guitar</h4>
  <p><b>Song Name:</b> <i>清明雨上</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a solo acoustic guitar, characterized by the clean and articulate sound of fingerpicked steel strings that simultaneously provide melody, harmony, and a bass line. The instrument's timbre is bright and resonant, with a warm, metallic clarity that is enhanced by a subtle reverb, creating an intimate yet spacious soundscape.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/清明雨上_5X2V327iAL0_E8IEn95y4Pw.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 38: Flute ➔ Saxphone</h4>
  <p><b>Song Name:</b> <i>清明雨上</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features a prominent alto saxophone, a piano providing harmonic support, a deep electric bass, and a drum kit. The saxophone's playing is smooth and articulate, creating a fluid melodic line. The timbre of the alto saxophone is warm, reedy, and expressive with a breathy quality, while the piano has a bright yet mellow acoustic tone.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/清明雨上_5X2V327iAL0_kQH8pqyd0HY_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 39: Violin ➔ Flute</h4>
  <p><b>Song Name:</b> <i>童话</i></p>
  <p><b>Text Prompt:</b> <i>This piece of contemporary instrumental music features a piano, a flute, and a string section. The piano opens the piece with a clear and resonant sound, playing arpeggiated chords that establish the harmonic foundation. The flute enters with the main melody, exhibiting a soft, airy, and breathy timbre that feels intimate and gentle. The string section provides a lush, warm, and smooth background, with a rich collective timbre that swells to create a full, cinematic texture.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/童话_HueBMrUEH6g_KHdGaIg2bcU_4.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 40: Flute ➔ Piano</h4>
  <p><b>Song Name:</b> <i>美酒加咖啡</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a solo acoustic piano, where the instrument is played with a clear, articulate touch, producing a lyrical melody over a supportive accompaniment of chords and flowing arpeggios. The timbre of the piano is bright and resonant in the higher melodic lines, contrasting with a warm and full-bodied quality in the lower harmonic foundation.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/美酒加咖啡_S1V3jO0GkQQ_IrYEuM05wqQ_0.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 41: Flute ➔ Saxphone</h4>
  <p><b>Song Name:</b> <i>美酒加咖啡</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a blend of acoustic and electronic instruments, with a saxophone serving as the lead melodic voice, characterized by its smooth articulation and prominent vibrato. It is supported by a piano providing harmonic accompaniment, a warm, foundational bass guitar, a clean-sounding drum kit, and a subtle synthesizer pad that adds atmospheric texture.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/美酒加咖啡_S1V3jO0GkQQ_eN60qGQ0mP0_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 42: Violin ➔ Piano</h4>
  <p><b>Song Name:</b> <i>至少还有你</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece is a solo piano composition. The instrument is played with clean and precise articulation, ensuring that both the melodic lines in the right hand and the arpeggiated accompaniment in the left are clearly distinguishable. The piano's timbre is bright and clear in its upper register, creating a singing quality for the melody, while the lower register provides a warm and resonant harmonic foundation.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/至少还有你_9PHGtxWF2rI_o7KSBgxBvFY_2.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 43: Piano ➔ Alto Saxophone</h4>
  <p><b>Song Name:</b> <i>被遗忘的时光</i></p>
  <p><b>Text Prompt:</b> <i>This musical piece features an alto saxophone with a warm, smooth, and expressive timbre as the primary melodic instrument, accompanied by a piano with a clear and resonant sound, a fingerpicked acoustic guitar providing a crisp rhythmic texture, and a lush string section that adds a rich, velvety depth.</i></p>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; margin-bottom: 20px;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Source Audio (Melodic Skeleton)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">Reference Audio (Target Texture)</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; color: #d9534f; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseAdapt (Ours) ✨</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MusicGen-Melody-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">MuseControlLite</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Base</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 10px;">
      <div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 8px;">SongEcho-Large</div>
      <audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/被遗忘的时光_64VPcw2MAEE_BsKOSZJeU_c_1.wav" controls style="width: 100%; outline: none;"></audio>
    </div>
  </div>
</div>


## References 

<a id="note1" href="#note1ref">[1]</a> Copet, J., Kreuk, F., Gat, I., Remez, T., Kant, D., Synnaeve, G., Adi, Y., and Defossez, A. Simple and controllable music generation. In Proc. NeurIPS, New Orleans, 2023.

<a id="note2" href="#note2ref">[1]</a> Tsai, F.-D., Wu, S.-L., Lee, W., Yang, S.-P., Chen, B.-R., Cheng, H.-C., and Yang, Y.-H. Musecontrollite: Multifunctional music generation with lightweight conditioners. In Proc. ICML, Vancouver, 2025.

<a id="note3" href="#note3ref">[1]</a> Li, S., Li, Y., Wang, Z., Zhang, Y., Wu, F., Deussen, O., Lee, T.-Y., and Dong, W. Songecho: Towards cover
song generation via instance-adaptive element-wise linear modulation. In Proc. ICLR, Rio de Janeiro, 2026.
