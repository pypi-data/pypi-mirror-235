from setuptools import setup, find_packages

setup(
    name='PermutiveAPI',
    version='1.12',
    packages=find_packages(),
    install_requires=[
        "aiofiles"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
