# Response to Reviewer Nj6v
Thank you for the careful reading and for the valuable comments. We are glad that the reviewer finds the motivation reasonable and also recognizes the potential value of the dataset.

## [Regarding the definition of MAMA]
We agree that the task definition of Melody-Aware Music Adaptation is not stated explicitly enough in the current draft.

Melody-Aware Music Adaptation is not a frame-level reconstruction task. It is a constrained adaptation task that aims to preserve the perceptual melodic skeleton of the source while satisfying the target style. Here, "melodic skeleton" refers to the perceptual identity of the melody, such as the global contour, the order of salient melodic events, and phrase-level recognizability. At the same time, local details can change, including articulation, ornamentation, expressive timing, and instrument-specific realization. In this sense, our task is closer to content-preserving style transfer or voice conversion than to strict self-reconstruction. A direct reconstruction of the source audio is therefore not the desired solution in our setting: it may preserve melody, but it can fail the adaptation objective when the target style conflicts with the source texture.

This is also why we separate the self-reconstruction task and the music adaptation task. The key point we want to study is whether a model can still preserve the source melodic skeleton under a conflicting target style condition, instead of simply copying the source morphology. Our concern with the self-reconstruction paradigm is exactly that it often rewards source-style leakage. A model can obtain high melody similarity simply by reproducing the source audio, even when the generated result does not follow the requested target style well. For this reason, our goal is not to maximize melody similarity alone, but to evaluate melody preservation jointly with target-style compliance. We will add this content to the revised manuscript to make the definition of the task clearer. We will also fix the broken “Sec. ??” reference.

## [Regarding the dataset samples]
Regarding the dataset samples, the reviewer asked for more evidence of dataset quality. We would like to clarify that the “Source Audio (Melodic Skeleton)” and “Reference Audio (Target Texture)” examples shown on our demo page are drawn from the test split of our dataset. The several dozen examples currently on the demo page cover both Chinese and English music, and provide a representative view of the audio conditions in the dataset.

## [Regarding the evaluation metrics]
We also agree with the reviewer that FAD and KL should not be interpreted as direct measures of subjective fidelity or musical realism. Our wording in the current draft is too strong on this point. A more precise interpretation is that these metrics measure distributional proximity under the chosen embedding spaces. Therefore, our current results should not be read as a definitive claim of superior perceptual quality. What they support more directly is that our method remains more stable in the proposed adaptation setting, especially when compared with the clear drop of the baselines from self-reconstruction to adaptation.

## [Regarding the inference setting]
Regarding the inference setting, our model is built on the Stable Audio Open + ControlNet architecture, following the design in stable-audio-control[1]. We therefore used the inference setting reported in that work, namely 250 sampling steps and CFG scale 7.

For the baselines built on the same framework, including MuseControlLite and SongEcho, we also used CFG scale 7. This choice is consistent with the guidance scale used in their original papers[2]. For sampling steps, MuseControlLite uses 50 steps in its paper[2], which is much smaller than the setting used by our model. To reduce the effect of using fewer sampling steps, we also evaluated it with 250 steps. In our manual inspection on multiple generated samples, we did not observe a quality drop, and in some cases the results were slightly better. Our goal here was not to claim that 250 and 7 are the individually optimal settings for every model, but to avoid giving our method an advantage simply because of a larger sampling budget.

[1] Hou S, Liu S, Yuan R, et al. Editing music with melody and text: Using controlnet for diffusion transformer

[2] Tsai F D, Wu S L, Lee W, et al. Musecontrollite: Multifunctional music generation with lightweight conditioners

## [Regarding the experiment]
We agree that the current experimental section is not yet comprehensive enough, especially for making a strong claim about overall perceptual superiority. At the same time, we would like to clarify that the main point supported by the current results is more specific. Our experiments show that the proposed adaptation setting reveals a clear weakness of self-reconstruction-based methods: when the source melody and the target style are in conflict, these models tend to leak the source texture and perform much worse on true music adaptation than on self-reconstruction. This gap is consistently reflected in our quantitative results, and we have also updated Part 2 of the demo page with additional examples to make this difference more visible. In those examples, some self-reconstruction baselines can sound reasonable in the self-reconstruction setting, but degrade clearly in the actual music adaptation setting, while our model remains more stable. We will revise the paper to make this point more precise in wording, and we will also include more comprehensive experiments to make the empirical evidence more convincing.

Thank you again for the constructive feedback. We believe these comments are helpful, and we will use them to clarify the task definition and better explain what the current experiments do and do not show.


# Response to Reviewer 1FnY
Thank you for the careful reading and for the valuable comments. We are glad that the reviewer finds the motivation reasonable and also recognizes the potential value of the dataset.

## [Regarding the definition of MAMA]
We agree that the task definition of Melody-Aware Music Adaptation is not stated explicitly enough in the current draft.