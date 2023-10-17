from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="name_gen_tool",
    version="0.1.1",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],  
    author="Bellamy",
    author_email="bellamyy.blakee100@gmail.com",
    description="A package to generate user names based on styles.",
    keywords="username generator, instagram username generator, social media name generator",
    url="https://github.com/bellamy-blakee/username-generator-tool",
)
