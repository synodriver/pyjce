import re
import sys
import os

from setuptools import setup, find_packages


def get_version() -> str:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "pyjce", "__init__.py")
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    result = re.findall(r"(?<=__version__ = \")\S+(?=\")", data)
    return result[0]


def get_dis():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


def main():
    if sys.version_info < (3, 8):
        raise Exception("Too old to install,please update your python version to 3.8 or latest")
    packages = find_packages(exclude=('test', 'tests.*', "test*"))
    version: str = get_version()
    dis = get_dis()
    setup(
        name="pyjce2",
        version=version,
        url="https://github.com/synodriver/pyjce",
        packages=packages,
        keywords=["jce", "tars"],
        description="Tencent JCE parser for Python,implement with pydantic",
        long_description_content_type="text/markdown",
        long_description=dis,
        author="synodriver",
        author_email="diguohuangjiajinweijun@gmail.com",
        maintainer="synodriver",
        python_requires=">=3.8",
        install_requires=["pydantic"],
        license='MIT',
        classifiers=[
            "Operating System :: OS Independent",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
        include_package_data=True,
    )


if __name__ == "__main__":
    main()
