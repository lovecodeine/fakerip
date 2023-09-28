from setuptools import setup, find_packages


setup(
    name='fakerip',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests-html'],
    author='purplevoid',
    author_email='suckmynuts@yarak.com',
    description='I dont want to pay for their shitty api',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HaRaMC0de/fakerip',
)
