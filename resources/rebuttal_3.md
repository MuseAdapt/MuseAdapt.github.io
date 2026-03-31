### [Regarding the task definition]

We agree the task definition needs to be more explicit. Please refer to our response to Reviewer Nj6v for a detailed clarification of how we define the "melodic skeleton" and why MAMA is a constrained adaptation task rather than a frame-level reconstruction task.

We also agree that representing musical texture with text alone is limited. However, one of the key observations behind our paper is that finer musical texture conditions in prior work are often extracted from the target audio itself and then used for conditional generation through self-reconstruction. While this gives stronger control, it also makes feature leakage much more likely, which leads to poor behavior in real adaptation settings. In contrast, text does not leak target-side acoustic details, which is why we use it as the texture condition in the current setting. Another practical reason is that text is easier to use than complex texture representations. At the same time, we do not claim that text is a complete representation of musical texture. We agree that incorporating richer texture conditions into MAMA is important, and we see this as a meaningful direction for future work.

### [Regarding the system description and training procedure]

We agree that the paper is difficult to follow in some parts and will improve the clarity of the overall pipeline, training procedure and the dataset construction in the revised manuscript. 

The contrastive module is used to pretrain the melody encoder on weakly paired data. The weighted supervised contrastive loss in Eq. (6) pulls together samples that share the same melody and pushes apart samples with different melodies, especially hard negatives with similar instrumentation but different melodic content. After pretraining, the encoder is frozen and used as the melody encoder of the DiT-based generative model.

The model uses two audio features: the global melody embedding $Z_{mel}$ extracted by the contrastive encoder, and the sparse Top-k CQT feature, which provides local structural guidance and follows prior work [1]. Regarding Eq. (8), our original intention was to write the standard v-objective diffusion loss, so we omitted the condition term $c$. We agree that this can be misleading, because the conditional information is indeed part of the model input. A clearer form should be:

$$
\mathcal{L} = \mathbb{E}_{t, \mathbf{x}_0, \epsilon}
\left[
\left\| f_\theta(\alpha_t \mathbf{x}_0 + \sigma_t \epsilon, t, c) - \mathbf{v}_t \right\|_2^2
\right]
$$

### [Regarding the demos and generation quality]

In our demo, the source and target share the same melody by design, because the goal is not to modify the melody itself, but to test whether the model can preserve the melodic skeleton while adapting the texture or style. In our music adaptation setting the model only takes information from the source audio and does not extract any condition from the target audio. This is the main difference from previous self-reconstruction-based setups.

Regarding generation quality, we agree that the current audio quality still has room for improvement. The current model is able to preserve a recognizable melody while carrying out texture or style adaptation, which is exactly the part that previous self-reconstruction-based methods struggle with in realistic settings. We have updated Part 2 of the demo page with more examples showing that these baselines are difficult to transfer to the real adaptation setting. We also agree that the difficulty of the task itself, together with a small portion of lower-quality samples in the dataset, is one factor that affects the current generation quality.

### [Regarding related work]

Thank you for pointing out these relevant references. Lin et al. and Lan et al. are already discussed in our related work, and we agree that BOSSA should also be included. At the same time, we would like to clarify that these works are related but not direct baselines for our setting.

**MusiConGen** focuses on rhythm and chord controlled text-to-music generation. Its own paper states that it is designed for backing track generation, where the music often does not contain the primary melody and mainly serves as accompaniment. In contrast, our task assumes a source audio with a clear melodic foreground and asks whether the model can preserve the source melodic skeleton while adapting to a target style. For this reason, MusiConGen and our method do not address the same problem setting.

**Coco-Mulla** is closer in spirit, since it also introduces piano roll or MIDI based control. In this sense, piano roll or MIDI can indeed be viewed as a melody representation that is more disentangled from texture than raw audio features. However, its conditioning pipeline relies on symbolic and pseudo-labeled controls obtained through automatic transcription. In our preliminary attempts, the Omnizart tool used in Coco-Mulla worked reasonably on single-instrument audio, but was much less reliable on the complex accompanied audio in MAMA-20k. A direct comparison would therefore require an extra front-end transcription pipeline and would introduce substantial upstream error before generation begins. That said, we fully agree that Coco-Mulla is closely related to our work, and we will discuss it more clearly in the revision and consider it in future comparisons.

We also agree that **BOSSA** is highly relevant, but it still differs from our task in two important ways. First, BOSSA is an audio-to-symbolic piano arrangement system. It takes an audio reference and a lead sheet as input, generates symbolic piano arrangement tokens with a symbolic music language model, and then renders them to audio using a soundfont. Our task, in contrast, is raw-audio generation. Because of this difference in output space, the resulting audio quality is not directly comparable in a fair way. Second, BOSSA is centered on piano arrangement, while our task studies raw-audio melody-aware adaptation across multiple instrumental textures. For these reasons, we think BOSSA is better viewed as an important related work rather than a direct apples-to-apples baseline. We will add it to the revised related work and make these distinctions more explicit.