# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pali3']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch']

setup_kwargs = {
    'name': 'pali3',
    'version': '0.0.1',
    'description': 'pali3 - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Pali3\n![pali](pali.png)\n\n"Figure 1: Overview of the PaLI-3 (5B) model: images are encoded into visual tokens individually\nby the contrastively pretrained 2B SigLIP vision model. Along with a query, these visual tokens\nare passed to an 3B encoder-decoder UL2 Transformer which produces the desired answer."\n\n\n\n## Installation\n\n`pip install pali3`\n\n\n## Usage:\n\n\n\n# License\nMIT\n\n# Todo\n\n- [ ] Implement sig_lip vit model with training recipe\n- [ ] Implement the text tokenizer, maybe use token monster \n- [ ] Implement the UL2 Transformer Encoder and Decoder\n- [ ] Implement training scripts\n- [ ] ',
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
