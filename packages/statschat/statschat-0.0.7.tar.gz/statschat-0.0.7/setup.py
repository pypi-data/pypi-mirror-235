# coding=utf-8
import re

import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    version_file = os.path.join(current_dir, 'statschat', 'version.py')
    with open(version_file, 'r') as f:
        content = f.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
        if version_match:
            return version_match.group(1)
        else:
            raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="statschat",  # 用自己的名替换其中的YOUR_USERNAME_
    version=get_version(),  # 包版本号，便于维护版本,保证每次发布都是版本都是唯一的
    author="YueLi",  # 作者，可以写自己的姓名
    author_email="yueli961201@gmail.com",  # 作者联系方式，可写自己的邮箱地址
    description="A statschat llm package",  # 包的简述
    long_description=long_description,  # 包的详细介绍，读取README.md
    long_description_content_type="text/markdown",
    url="https://github.com/",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    entry_points={
    },
    install_requires=[  # 项目依赖
        'typing_extensions',
        'openpyxl',
        'et-xmlfile',
        'openai',
        'pydantic',
        'numpy',
        'matplotlib',
        'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',  # 对python的最低版本要求
)
