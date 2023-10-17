"""setup for instasave"""

from setuptools import setup

setup(
    name="ddinsta",
    version="0.1",
    packages=["ddinsta"],
    author="Yasin Zingiev (Rocket)",
    author_email="m@zingiev.ru",
    description="Module for downloading photos and videos from Instagram",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zingiev/ddinsta",
    license="MIT",
    install_requires=("requests",),
)