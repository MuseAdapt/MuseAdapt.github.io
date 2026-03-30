# Response to Reviewer 1FnY
Thank you for the careful reading and for the constructive comments. We are glad that the reviewer recognizes the value of the dataset, the motivation of the task, and the overall design of MuseAdapt.

### [Regarding the dataset and its release]
We thank the reviewer for pointing out that the current dataset description is not detailed enough. We will expand this part in the revised manuscript and include more statistics on the corpus composition and quality.

Our real-audio dataset contains 2,662 songs and 20,425 audio tracks, from which we extract 274,462 melody-aligned segments. Among them, 1,625 are Chinese songs, with 11,706 audio tracks and 155,201 aligned segments. The remaining 1,037 are English songs, with 8,719 audio tracks and 119,461 aligned segments. The instrument coverage includes piano, strings such as cello and violin, guitars such as fingerstyle guitar and electric guitar, flute, saxophone, harp, Chinese traditional instruments such as erhu, pipa, and guzheng, as well as orchestral arrangements. We will add these statistics to the revised paper to make the dataset description more complete.

| Split | Songs | Audio tracks | Aligned melody segments |
|---|---:|---:|---:|
| Chinese songs | 1,625 | 11,706 | 155,201 |
| English songs | 1,037 | 8,719 | 119,461 |
| Total | 2,662 | 20,425 | 274,462 |

As a corpus-level quality signal, we also evaluated the dataset with PAM [1] and music aesthetics metrics [2], including Content Enjoyment, Content Usefulness, Production Complexity, and Production Quality. The results are shown below. CE, CU, and PQ are all relatively high, which suggests that the collected audio is generally of good perceptual and production quality. PC is lower mainly because many of the manually collected recordings contain a clear lead instrument, so the audio components are less dense and less layered. In our case, this is not necessarily a drawback, since such recordings are better suited for a task that requires a clear melodic foreground. We will include this analysis in the revised manuscript. **MAMA-20k will be publicly released upon acceptance.**

| Metric | PAM | CE | CU | PC | PQ |
|---|---|---|---|---|---|
| Value  | 0.8902 | 7.6297 | 7.8808 | 4.8294 | 7.7877 |

[1] Deshmukh et al., Pam: Prompting audio-language models for audio quality assessment
[2] Tjandra et al., Meta audiobox aesthetics: Unified automatic quality assessment for speech, music, and sound

### [Regarding the experimental evidence]
We agree that the current experiments are not yet comprehensive enough, especially in terms of ablation studies and subjective evaluation. Our current evidence supports a narrower point. The main result we want to highlight is that the proposed adaptation setting reveals a clear weakness of self-reconstruction-based methods: when the source melody and the target style are in conflict, these models tend to leak the source texture and perform much worse on true music adaptation than on self-reconstruction. This gap is consistently reflected in our quantitative results, and we have also updated the demo page with more examples to make this difference more visible. In those examples, some self-reconstruction baselines can sound reasonable in the self-reconstruction setting, but degrade clearly in the actual adaptation setting, while our model remains more stable. We agree that ablations and listening tests would make the claims stronger, and we will include more comprehensive experiments in the final version.

### [Regarding the CMS metric]  
We agree that this is a valid concern. Since CMS is computed using our contrastive melody encoder, it may favor our method to some extent because the evaluation space is related to the representation used in training. We will make this limitation explicit in the revised paper.

At the same time, CMS is not used in isolation. We also report MAS, and the two metrics show a consistent trend across models. This means that our conclusion does not rely on CMS alone. To further examine the behavior of CMS, we also measured the CMS between real paired audio segments and their input audio in the MAMA-20k test set, which gives a score of 0.6509. For comparison, the CMS between randomly sampled pairs is only 0.0792. This range covers the scores of all evaluated models and provides additional evidence that CMS is able to reflect meaningful melody-level similarity to a certain extent.

We agree that human evaluation is still important here. In the final version, we will add human listening tests to further examine the validity of CMS and its consistency with human perception of melody similarity.

### [Regarding the Gemini-generated captions]
The Gemini-generated captions are based on the input audio. Their purpose is to provide text descriptions of the audio in terms of instrumentation, mood, and genre. To improve quality, we compared several available captioning options and found Gemini-2.5-Pro to produce the most reliable results for this purpose. In addition, we also performed manual spot checking on sampled examples to verify the caption quality. We will clarify this process in the revised paper.

### [Regarding the demopage]
The missing baseline samples on the demo page were mainly caused by the large number of audio files on the page, which could make loading unstable and give the impression that some samples were missing. We have now updated the demo page, improved the loading logic, and added more examples for comparison. More details can be found at: https://museadapt.github.io/

### [Regarding the training details]
Thank you for pointing this out. During the full generative training stage, the melody encoder is frozen after pretraining. The frozen part is the main DiT backbone, while the trainable parts are the ControlNet, the parallel melody adapter, and the related projection layers. We agree that this should be stated more clearly in the paper, and we will revise the description to avoid confusion.

### [Regarding presentation]
We also agree that the current presentation can be improved. In particular, adding a system overview figure and improving the overall structure would make the method easier to follow. We will improve both the figures and the organization in the final version. We will also fix the incorrect “Sec. ??” reference.