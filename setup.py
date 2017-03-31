# coding: utf-8
from setuptools import setup, find_packages
import os

# not so bad: http://joebergantine.com/blog/2015/jul/17/releasing-package-pypi/
version = __import__('djangocms_baseplugins').__version__


setup(
    name="djangocms-baseplugins",
    version=version,
    url='http://github.com/benzkji/djangocms-baseplugins',
    license='BSD',
    platforms=['OS Independent'],
    description="djangocms_baseplugins",
    long_description='a common base for consistent django-cms plugin development. includes default plugins.',
    author=u'Ben Stähli',
    author_email='bnzk@bnzk.ch',
    packages=find_packages(),
    install_requires=(
        # 'Django>=1.3,<1.5',  # no need to limit while in development
        'django>=1.8',
        'django-cms>=3.3',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='runtests.main',
    tests_require=(
        'argparse',  # needed on python 2.6
    ),
)
