from setuptools import setup, find_packages

setup(
    name='aicos_model_zoo',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
    'pandas',
    'torch',
    'torchinfo',
    'scikit-learn',
    'mlflow',
    ]
,
)
