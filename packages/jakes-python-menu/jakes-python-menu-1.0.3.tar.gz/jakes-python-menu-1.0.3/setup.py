from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

setup(
    name="jakes-python-menu",
    version="1.0.3",
    description="A Python menu library",
    long_description=open("README.txt").read() + '\n\n' + open("CHANGELOG.txt").read(),
    url='',
    author="Jake2k4",
    author_email="jakelandrum2004@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords='menu',
    packages=find_packages(),
    install_requires=[""]
)