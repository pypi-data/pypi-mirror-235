from setuptools import setup, find_packages

requirements = [
    "logging",
]

_version = "0.0.5"

with open(__file__.rstrip("setup.py") + "desc.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="python-logging-tools",
    version=_version,
    author="Daniil10295",
    author_email="chernyak.daniil.2010@gmail.com",
    url="https://www.youtube.com/channel/UCWNjclaL2HQ5gDVayqhNEfw",
    description="logging package",
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    entry_points={"console_scripts": ["MGS-Daniil = python_logging_tools.main:main"]},
)
