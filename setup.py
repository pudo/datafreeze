import sys
from setuptools import setup, find_packages


py26_dependency = []
if sys.version_info[:2] <= (2, 6):
    py26_dependency = ["argparse >= 1.1", "ordereddict >= 1.1"]

with open('README.rst', 'r') as fh:
    readme_rst = fh.read()

setup(
    name='datafreeze',
    version='0.1.0',
    description="Export data from a SQL database to a set of file formats.",
    long_description=readme_rst,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='sql sqlalchemy etl loading utility',
    author='Friedrich Lindenberg, Gregor Aisch, Stefan Wehrmeyer',
    author_email='friedrich@pudo.org',
    url='http://github.com/pudo/datafreeze',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'dataset >= 1.0.0',
        "PyYAML >= 3.10",
        "six >= 1.7.3"
    ] + py26_dependency,
    tests_require=[],
    test_suite='test',
    entry_points={
        'console_scripts': [
            'datafreeze = datafreeze.app:main',
        ]
    }
)
