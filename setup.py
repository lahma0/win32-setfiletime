import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("win32_setfiletime.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

with open("README.md", "rb") as file:
    readme = file.read().decode("utf-8")

setup(
    name="win32_setfiletime",
    version=version,
    py_modules=["win32_setfiletime"],
    description="A small Python utility to set file creation/modified/accessed time on Windows",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="lahma0",
    author_email="lahma69@gmail.com",
    url="https://github.com/lahma0/win32-setfiletime",
    download_url="https://github.com/lahma0/win32-setfiletime/archive/{}.tar.gz".format(version),
    keywords=[
        "win32", "windows", "filesystem", "filetime", "timestamp", "modified", "created", "accessed"
    ],
    license="MIT license",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Filesystems",
        "Intended Audience :: Developers",
        "Environment :: Win32 (MS Windows)",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    extras_require={"dev": [
        "black>=19.3b0 ; python_version>='3.6'",
        "pytest>=4.6.2",
    ]},
    python_requires=">=3.5",
)
