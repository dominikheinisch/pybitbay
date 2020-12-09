from setuptools import setup, find_packages

setup(
    name="pybitbay",
    version="0.0.1",
    description="python api for bitbay cryptocurrency exchange",
    author="dominik heinisch",
    author_email="dominikheinisch2@gmail.com",
    url="https://github.com/dominikheinisch/pybitbay",
    license='Apache 2.0',
    packages=find_packages("pybitbay"),
    install_requires=["pandas", "requests"],
    python_requires=">=3.6",
)
