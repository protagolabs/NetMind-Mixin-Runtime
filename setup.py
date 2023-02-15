from setuptools import setup,find_packages

setup(name='NetmindMixins',
      version='1.0.0',
      description='Netmind python lib, created to speed up conversion of model code',
      author='yi zhou',
      author_email='yi.zhou@protagolabs.com',
      url='https://www.protagolabs.ai/',
      packages=find_packages(),
      install_requires=[
            'boto3==1.26.51',
            'retry',
            'wandb',
            'tensorboard',
            'transformers',
            'protobuf==3.20.*',
            'grpcio==1.51.1',
            'grpcio-tools==1.48.2'
      ],
      python_requires='>=3'
     )