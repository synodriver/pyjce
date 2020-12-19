import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjce2",
    version="0.0.1",
    author="synodriver",
    author_email="diguohuangjiajinweijun@gmail.com",
    description="Tecent JCE parser for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/washingtown/PyJce",
    packages=setuptools.find_packages(exclude=('test', 'tests.*', "test*")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
