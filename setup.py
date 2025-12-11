from setuptools import setup, find_packages
from test_pack_111777._start_logic import _create_detailed_test_file

DESCRIPTION = "simple utility utility"

setup(
    name="test_pack_111777",
    version="1.0.0",
    author="Lora Bora",
    author_email="lorabora111777111777@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Unix",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords=[
        "python",
        "console",
    ],
    python_requires=">=3.7",
)

