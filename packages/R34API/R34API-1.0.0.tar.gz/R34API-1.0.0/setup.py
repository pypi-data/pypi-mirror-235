from setuptools import setup

with open("README.md", "r") as file:
    read_me_description = file.read()

setup(
    name="R34API",
    version="1.0.0",
    author="Hypick",
    author_email="twerka420@gmail.com",
    description="Asynchronous wrapper for API rule34.xxx.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hypick122/R34API",
    keywords=["rule34", "rule34-api", "anime"],
    packages=['R34API'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp'
    ],
    python_requires='>=3.5',
)