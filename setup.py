from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="smartvenv",
    version="0.0.1",
    author="Roshan Lamichhane",
    author_email="roshanlamichhanenepali@gmail.com",
    description="A smarter virtual environment and dependency management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roshanlam/smartvenv",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'smartvenv=smartvenv.smartvenv:main',
        ],
    },
    install_requires=[
        "pip-tools",
    ],
)

