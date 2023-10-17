# coding=utf-8

from setuptools import setup, find_packages

setup(
    name="volcengine-avatar-live",
    version="1.0.0",
    description=("SDK for Volcengine Avatar Live"),
    long_description=open("README.rst").read(),
    author="Tingshuo Chen",
    author_email="chentingshuo@bytedance.com",
    license="Apache Software License (Apache 2.0)",
    packages=find_packages(),
    platforms=["all"],
    requires=["requests", "websockets"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
