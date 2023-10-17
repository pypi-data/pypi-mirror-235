# coding=utf-8

from setuptools import setup, find_packages

setup(
    name="volcengine-avatar-live",
    version="1.0.1",
    description=("SDK for Volcengine Avatar Live"),
    long_description=open("README.rst").read(),
    author="Tingshuo Chen",
    author_email="chentingshuo@bytedance.com",
    license="Apache 2.0",
    packages=find_packages(),
    platforms=["all"],
    install_requires=[
        "requests>=2.27.1",
        "websockets>=11.0.3",
        'importlib-metadata; python_version >= "3.8"',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
