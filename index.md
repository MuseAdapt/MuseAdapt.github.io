<div style="text-align: center"> 

<h1> MuseAdapt: Melody-Aware Music Adaptation via Structure-Texture Disentanglement </h1>

Anonymous Authors

<p>
Supporting webpage for ICML 2026<br>
</p>

</div>


<div style="text-align: justify"> 

<h2>Abstract</h2>

Melody-conditioned music generation is a cornerstone of controllable synthesis. However, existing self-reconstruction paradigms, which condition models on melodic features extracted from the target audio, often fail to separate semantic melody from acoustic texture. 
This entanglement encourages models to replicate the source audio rather than perform genuine melodic adaptation. 
To bridge this gap, we define melody-aware music adaptation (MAMA), a task focused on generating stylistically diverse music that preserves melodic identity without enforcing frame-level reconstruction. 
We introduce MAMA-20k, the first large-scale dataset for this task, featuring weakly paired segments with shared melodic skeletons but distinct acoustic realizations. 
Leveraging this data, we propose MuseAdapt, a diffusion-based framework that achieves disentangled melodic control via a contrastive encoder. 
Experiments demonstrate that MuseAdapt significantly outperforms self-reconstruction baselines in cross-instrument and real-world scenarios, highlighting the necessity of disentangled supervision for robust music synthesis.

</div>
<p align="center">
<img src="method.png">
</p>

## 🎧 Audio Samples

As discussed in our paper, existing models trained via self-reconstruction often fail to separate semantic melody from acoustic texture, leading to overfitting. To demonstrate the superiority of **MuseAdapt**, we evaluate the models under two distinct scenarios: **Music Adaptation (Transfer)** and **Self-Reconstruction**.

The baseline models include: *MusicGen-Stereo-Melody, MusicGen-Stereo-Melody-Large, MuseControlLite, SongEcho-base, and SongEcho-large*. All generated samples are approximately 47 seconds long.

---

### Part 1: Music Adaptation Task (Cross-Instrument & Style Transfer)
In this challenging real-world scenario, models are tasked with generating a target audio segment with a distinct instrumentation/style while preserving the perceptual melodic identity of the source audio. **Our model (MuseAdapt) successfully disentangles the melody and follows the text prompt, whereas baselines often simply replicate the source texture.**

<br>

<div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6;">
  <h4>🎵 Example 1: Piano ➔ Acoustic Guitar</h4>
  <p><b>Song Name:</b> <i>Boom Clap</i></p>
  <p><b>Text Prompt:</b> <i>This piece features a blend of rock and classical instrumentation, led by a virtuosic electric violin with a bright, cutting timbre that soars over the ensemble. The foundation is provided by thick, distorted electric guitars, a deep and driving bass guitar, and a powerful rock drum kit, all while atmospheric synthesizer pads add a subtle, ethereal layer in the background. The music aligns with the symphonic or neoclassical metal genre, blending the fast tempo, driving rock beat, and powerful chord progressions of metal with the complex melodic structures and technical virtuosity of classical music. </i></p>
  
  <table style="width: 100%; text-align: center; margin-bottom: 15px;">
    <tr>
      <th style="width: 50%;">Source Audio (Melodic Skeleton)</th>
      <th style="width: 50%;">Reference Audio (Target Texture)</th>
    </tr>
    <tr>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/src/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 260px;"></audio></td>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/dst/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 260px;"></audio></td>
    </tr>
  </table>

  <table style="width: 100%; text-align: center;">
    <tr>
      <th style="width: 33.3%; color: #d9534f;">MuseAdapt (Ours) ✨</th>
      <th style="width: 33.3%;">MusicGen-Melody</th>
      <th style="width: 33.3%;">MusicGen-Melody-Large</th>
    </tr>
    <tr>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/ours/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 200px;"></audio></td>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 200px;"></audio></td>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musicgen_melody_large/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 200px;"></audio></td>
    </tr>
    <tr>
      <th>MuseControlLite</th>
      <th>SongEcho-Base</th>
      <th>SongEcho-Large</th>
    </tr>
    <tr>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/musecontrollite/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 200px;"></audio></td>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_base/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 200px;"></audio></td>
      <td><audio src="https://huggingface.co/datasets/MuseAdapt/MuseAdapt_Demo/resolve/main/songecho_large/transfer/Boom Clap_4IT6QLUrNts_HKgtPYhkcWo_0.wav" controls style="width: 90%; min-width: 200px;"></audio></td>
    </tr>
  </table>
</div>


## References 

<a id="note1" href="#note1ref">[1]</a> I. Manco, B. Weck, S. Doh, M. Won, Y. Zhang, D. Bogdanov, Y. Wu, K. Chen, P. Tovstogan, E. Benetos, E. Quinton, G. Fazekas, and J. Nam, “The Song Describer dataset: A corpus of audio captions for music-and-language evaluation,” in Proc. NeurIPS, New Orleans, 2023.

<a id="note2" href="#note2ref">[2]</a> J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Defossez, “Simple and controllable music generation,” in Proc. NeurIPS, New Orleans, 2023.
