from setuptools import setup, find_packages

setup(
    name="semantichar",
    version="0.1",
    install_requires=[
        #"torch==1.13.0",
        #"numpy==1.20.1",
        "scikit-learn",
        "timm==0.6.7",
        "ftfy",
        "regex",
        "einops",
        "iopath",
        "wandb",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
