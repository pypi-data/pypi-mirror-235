import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twettletwattletwattle",
    version="0.0.1",
    author="zazzzSec",
    author_email="ian@zazzz.io",
    description="twettletwattletwattle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://twettletwattletwattle.com",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "twettletwattletwattle/src"},
    packages=setuptools.find_packages(where="twettletwattletwattle/src"),
    python_requires=">=3.6",
)