from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.0.1"
DESCRIPTION = "A simple method to interactively preempt a running script to run a debugger"
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="preemptive_debugger",
    version=VERSION,
    author="Tyler Lum",
    author_email="tylergwlum@gmail.com",
    url="https://github.com/tylerlum/preemptive_debugger",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "debugger", "preemptive", "interactive"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)
