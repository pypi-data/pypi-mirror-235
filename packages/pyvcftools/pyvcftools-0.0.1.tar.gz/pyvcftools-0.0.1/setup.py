#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = [line.strip() for line in requirements_file]

test_requirements = [ ]

setup(
    author="Vivian Leung",
    author_email='leung.vivian.w@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="VTools for manipulating vcfs doing genomics work",
    entry_points={
        'console_scripts': [
            'pyvcftools=pyvcftools.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyvcftools',
    name='pyvcftools',
    packages=find_packages(include=['pyvcftools', 'pyvcftools.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/vivianleung/pyvcftools',
    version='0.1.0',
    zip_safe=False,
)
