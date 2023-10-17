# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pali3']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'horovod', 'torch', 'torchvision', 'zetascale']

setup_kwargs = {
    'name': 'pali3',
    'version': '0.0.3',
    'description': 'pali3 - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Pali3\n![pali](pali.png)\n\n"Figure 1: Overview of the PaLI-3 (5B) model: images are encoded into visual tokens individually\nby the contrastively pretrained 2B SigLIP vision model. Along with a query, these visual tokens\nare passed to an 3B encoder-decoder UL2 Transformer which produces the desired answer."\n\n\nVit trained with siglip loss -> embeddings -> ul2 -> text tokens\n\ntext -> tokenizer -> embeddings -> ul2 -> text tokens\n\n\n\n## Installation\n\n`pip install pali3`\n\n\n## Usage:\n\n\n## Architecture\n\nHere is the ASCII representation of the model architecture and the stages of training:\n\n```\nModel Architecture:\n\nImage Input\n    |\n    V\nContrastive Vision Encoder (ViT-G/14)\n    |\n    V\nTransformer Encoder\n    |\n    V\nTransformer Decoder\n    |\n    V\nText Output\n\nStages of Training:\n\nStage 0: Unimodal pretraining\n    |\n    V\nStage 1: Multimodal training\n    |\n    V\nStage 2: Resolution increase\n    |\n    V\nTask specialization (transfer)\n\n```\n\nThe model architecture consists of a contrastive vision encoder (ViT-G/14) that encodes the image into tokens. These tokens are passed to a transformer encoder and then to a transformer decoder that generates a text output.\n\nThe training procedure consists of multiple stages:\n\n-   Stage 0: Unimodal pretraining. The image encoder is pretrained contrastively on image-text pairs from the web, following the SigLIP training protocol. The text encoder-decoder is a 3B UL2 model trained following the mixture of denoisers procedure.\n\n-   Stage 1: Multimodal training. The image encoder is combined with the text encoder-decoder and trained on a multimodal task and data mixture, keeping the image encoder frozen and using its native resolution.\n\n-   Stage 2: Resolution increase. The resolution of the model is increased by fine-tuning the whole model with a short curriculum of increasing resolutions.\n\n-   Task specialization (transfer). Finally, for each individual task, the model is fine-tuned with frozen ViT image encoder on the task\'s training data.\n\nPlease note that this is a high-level representation and the actual implementation might involve more details and complexities.\n\n# License\nMIT\n\n# Todo\n\n- [ ] Implement sig_lip vit model with training recipe\n- [ ] Implement the text tokenizer, maybe use token monster \n- [ ] Implement the UL2 Transformer Encoder and Decoder\n- [ ] Implement training scripts for the full pali3 model\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/pali3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
