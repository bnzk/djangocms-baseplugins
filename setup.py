# coding: utf-8
import os

from setuptools import find_packages, setup

# not so bad: http://joebergantine.com/blog/2015/jul/17/releasing-package-pypi/
version = __import__("djangocms_baseplugins").__version__


def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="djangocms-baseplugins",
    version=version,
    url="https://github.com/bnzk/djangocms-baseplugins",
    license="BSD",
    platforms=["OS Independent"],
    description="djangocms_baseplugins",
    long_description=read("PYPI.rst"),
    author="Ben Stähli",
    author_email="bnzk@bnzk.ch",
    packages=find_packages(),
    install_requires=(
        "django>=1.8",
        "django-cms>=3.3",
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
