from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2", "pandas>=1.0.3", "nltk>=3.4.5"]

setup(
    name="tfidf",
    version="0.0.1",
    author="Ali Balouchi",
    author_email="alibalouchi.74@gmail.com",
    description="A package to extract word's tf_idf",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/alibalouchi/tfidf/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
