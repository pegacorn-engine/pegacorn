import setuptools

from pegacorn import __version__

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pegacorn",
    version=__version__,
    author="0xonk",
    author_email="0xonkfd@gmail.com",
    description="pegacorn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pegacorn-engine/pegacorn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.10",
    install_requires=[
        "androguard==3.4.0a1",
        "click",
    ],
)
