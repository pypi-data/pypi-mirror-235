from setuptools import setup, find_packages

setup(
    name="guess_num_package",
    version="1",
    description="This package contains Python files that you can run and test",
    author="Connor Johnson",
    packages=find_packages(include=["src*", "tests*"]),
    install_requires=[
        "python>=3.7.0, <3.8",
        "importlib-metadata>=4.0",
        "sphinx>=1.0.0, <7",
        "sphinx-copybutton>=0.4",
    ],
)
