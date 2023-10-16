from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'automlex',
    version = '0.0.1',
    description ='Say hello!',
    py_modules = ["main"],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/nityanandmathur/AutoML",
    author="Nityanand mathur",
    author_email="nityanandmathur@gmail.com",

    install_requires = [
        "numpy >= 1.13.3",
    ],

    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    },
)