from setuptools import setup, find_packages

setup(
    name="contentful_rich_text_to_markdown_converter",
    version="0.1",
    description="A Python wrapper for converting Contentful rich text to Markdown",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rioredwards/python-wrapper-for-contentful-rich-text-to-markdown-converter",
    author="Rio Edwards",
    author_email="rioredwards@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            # any command-line utilities you want to provide
        ],
    },
)
