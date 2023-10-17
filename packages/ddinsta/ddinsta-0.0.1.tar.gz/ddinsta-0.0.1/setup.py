"""setup for ddinsta"""

from setuptools import setup

setup(
    name="ddinsta",
    version="0.0.1",
    packages=["ddinsta"],
    license="MIT",
    author="Yasin Zingiev (Rocket)",
    author_email="m@zingiev.ru",
    description="Module for downloading photos and videos from Instagram",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=("requests",),
)