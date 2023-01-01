from setuptools import setup, find_packages

packages = ['latent_diffusion', 'latent_diffusion.scripts', 'latent_diffusion.ldm'] + ['latent_diffusion.ldm.'+p for p in find_packages('ldm')]

setup(
    name='latent-diffusion',
    version='0.0.1',
    description='',
    packages=packages,
    package_dir={p: p.replace('.', '/').replace('latent_diffusion', '.') for p in packages},
    python_requires=">=3.8",
    install_requires=[
        'torch',
        'opencv-python',
        'albumentations',
        'Pillow',
        'numpy',
        'torchvision',
        'omegaconf',
        'taming-transformers @ git+https://github.com/CompVis/taming-transformers.git@master#egg=taming-transformers',
        'tqdm',
        'pytorch-lightning',
        'einops',
        'natsort',
        'clip @ git+https://github.com/openai/CLIP.git@main#egg=clip',
        'kornia',
        'scipy',
        'scann'
    ],
)
