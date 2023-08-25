from setuptools import setup,find_packages

setup(name='NetmindMixins_py310',
      version='1.0.0',
      description='Netmind python lib, created to speed up conversion of model code',
      author='yi zhou',
      author_email='yi.zhou@protagolabs.com',
      url='https://www.protagolabs.ai/',
      packages=find_packages(),
      package_data={"NetmindMixins": ["*.so"], "NetmindMixins.proto": ["*.so"]},
      install_requires=[
            'boto3==1.26.51',
            'retry',
            'wandb',
            'tensorboard',
            'matplotlib',
            'datasets',
            'pydantic',
            'transformers',
            'protobuf==3.20.*',
            'grpcio==1.51.1',
            'grpcio-tools==1.48.2',
            'cryptography'
      ],
      python_requires='>=3'
     )
