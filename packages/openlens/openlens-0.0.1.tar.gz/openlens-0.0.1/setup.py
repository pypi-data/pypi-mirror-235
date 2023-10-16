import pathlib
import setuptools

file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

with open(file / 'requirements.txt') as f:
    required_packages = f.read().splitlines()

setuptools.setup(
    name="openlens",
    version="0.0.1",
    author="Nuhman Pk",
    author_email="nuhmanpk7@gmail.com",
    long_description=README,
    long_description_content_type="text/markdown",
    description="A user-friendly open-source OCR framework for effortless model training and text extraction",
    license="MIT",
    url="https://github.com/nuhmanpk/openlens",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=setuptools.find_packages(include=['openlens']),
    install_requires=required_packages,

    python_requires=">=3.6",

)
