# Research Plan

Steps to undertake:

- Evaluating finetuned models
- Data collection
- Finetuning models

### Evaluating finetuned models

- Can probably be done on Colab or any platform really (needs ~10-12 GB VRAM)
- Probably want to think of good prompts that show some specific characteristic, save interesting seeds, and query multiple models for them

- Tentatively: Setting up a GDrive to store outputs per model-checkpoint or per experiment

- Probably will spend most of our time here - I think this is the hardest part, figuring out how to find interesting conclusions about models

### Dataset collection

- Need to collect 512x512 images, along with labels
- In theory a dataset as small as 30 images might work, but worth noting waifu diffusion used 50k images.
  - Would be cool to test all along the 30 images to 50k spectrum and report results.
- Need to also label the images, ie: give them meaningful prompts
  - Would be cool to see what poorer/better prompts does
- Probably want to store the datasets on R2, but they're likely small enough on the lower end (~100s of MB) that egress costs don't matter much.

### Finetuning models

- Needs ~30-35GB VRAM, can only really be done on an A6000/A100

  - Currently looks like vast.ai is the best bet.
  - Runpod.io and lambdalabs.com have supply, but only sometimes.

- Need to figure out checkpointing, and storing outputs:

  - Probably want to store a model checkpoint after every epoch or few epochs, both to gracefully handle host death and to do comparisons over # of epochs
  - R2 is probably the best bet for storage as it's cheap and has low storage costs
  - In theory it looks like we can store this on HuggingFace too - and there'll be an easy way to use it with the diffusers package - we probably want to do this when we're releasing this or such.

- The TouhouAI Discord seems to be leading open finetuning efforts, join them here: https://discord.gg/touhouai
- Their finetuning code can be found here: https://github.com/harubaru/waifu-diffusion/blob/main/configs/stable-diffusion/v1-finetune.yaml

- In theory, since finetuning ~= training, the HF Diffusers library might just be able to do it for us and make it much smoother.
