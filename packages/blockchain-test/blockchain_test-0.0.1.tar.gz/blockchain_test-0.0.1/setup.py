from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="blockchain_test",
    version="0.0.1",
    author="ictest",
    author_email="quattroporte54@gmail.com",
    description="blockchain test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IgorTest19/blockchain",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
            'requests',
            'bitcoinlib'
    ],
)
