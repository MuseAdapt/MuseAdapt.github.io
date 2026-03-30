Thank you for the careful reading and valuable comments. We are glad that the reviewer finds the motivation reasonable and recognizes the potential value of the dataset.

[Regarding the definition of MAMA]
We agree that the task definition of Melody-Aware Music Adaptation is not explicit enough in the current draft.

MAMA is not a frame-level reconstruction task. It is a constrained adaptation task that aims to preserve the perceptual melodic skeleton of the source while satisfying the target style. Here, "melodic skeleton" refers to the perceptual identity of the melody, such as the global contour, the order of salient melodic events, and phrase-level recognizability. Local details can change, including articulation, ornamentation, expressive timing, and instrument-specific realization. In this sense, our task is closer to content-preserving style transfer or voice conversion than to strict self-reconstruction. Directly reconstructing the source audio is therefore not the desired solution, because it may preserve melody while failing the adaptation objective when the target style conflicts with the source texture.

This is why we separate the self-reconstruction task and the music adaptation task. The key question is whether a model can preserve the source melodic skeleton under a conflicting target style condition, instead of simply copying the source morphology. Our concern with the self-reconstruction paradigm is that it often rewards source-style leakage. A model can obtain high melody similarity simply by reproducing the source audio, even when the generated result does not follow the requested target style well. For this reason, our goal is not to maximize melody similarity alone, but to evaluate melody preservation jointly with target-style compliance. We will revise the manuscript accordingly and also fix the broken “Sec. ??” reference.

[Regarding the dataset samples]
The “Source Audio (Melodic Skeleton)” and “Reference Audio (Target Texture)” examples on our demo page are drawn from the test split of our dataset. The current demo covers both Chinese and English music, and help illustrate the audio conditions in the dataset.

[Regarding the evaluation metrics]
We agree that FAD and KL should not be interpreted as direct measures of subjective fidelity or musical realism. A more precise interpretation is that these metrics measure distributional proximity under the chosen embedding spaces. Therefore, our current results should not be read as a definitive claim of superior perceptual quality. What they support more directly is that our method remains more stable in the proposed adaptation setting, especially compared with the clear drop of the baselines from self-reconstruction to adaptation.

[Regarding the inference setting]
Our model is built on the Stable Audio Open + ControlNet architecture, following Stable Audio Control [1]. We therefore used the inference setting reported in that work, namely 250 sampling steps and CFG scale 7.

For the baselines built on the same framework, including MuseControlLite, we also used CFG scale 7. This is consistent with the guidance scale used in its original paper [2]. MuseControlLite uses 50 sampling steps in its paper [2], which is much smaller than the setting used by our model. To reduce the effect of using fewer sampling steps, we also evaluated it with 250 steps. In our manual inspection on multiple generated samples, we did not observe a quality drop, and in some cases the results were slightly better. Our goal was not to claim that 250 and 7 are the individually optimal settings for every model, but to avoid giving our method an advantage simply because of a larger sampling budget.

[1] Hou et al., Editing music with melody and text: Using controlnet for diffusion transformer
[2] Tsai et al., Musecontrollite: Multifunctional music generation with lightweight conditioners

[Regarding the experiment]
We agree that the current experimental section is not yet comprehensive enough for a strong claim about overall perceptual superiority. The main point supported by the current results is narrower. Our experiments show that the proposed adaptation setting reveals a clear weakness of self-reconstruction-based methods: when the source melody and the target style are in conflict, these models tend to leak the source texture and perform much worse on true music adaptation than on self-reconstruction. This gap is consistently reflected in our quantitative results, and we have also updated Part 2 of the demo page with additional examples to make this difference more visible. In those examples, some self-reconstruction baselines can sound reasonable in the self-reconstruction setting, but degrade clearly in the actual music adaptation setting, while our model remains more stable. We will make this point more precise in the revised paper and include more comprehensive experiments to strengthen the empirical support.

Thank you again for the constructive feedback.