from setuptools import setup, find_packages

packages = ['latent_diffusion', 'latent_diffusion.scripts', 'latent_diffusion.ldm'] + ['latent_diffusion.ldm.'+p for p in find_packages('ldm')]

setup(
    name='latent-diffusion',
    version='0.0.1',
    description='',
    packages=packages,
    package_dir={p: p.replace('.', '/').replace('latent_diffusion', '.') for p in packages},
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
