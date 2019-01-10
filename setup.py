from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), 'rt') as f:
    long_description = f.read()

with open(path.join(here, 'version.txt'), 'rt') as f:
    version = f.read()

with open(path.join(here, 'requirements', 'developer.txt')) as f:
    developer_requirements = f.readlines()

with open(path.join(here, 'requirements', 'test.txt')) as f:
    test_requirements = f.readlines()

with open(path.join(here, 'requirements', 'install.txt')) as f:
    install_requirements = f.readlines()

setup(
    name='calyx',

    version=version,

    description='Calyx: Bundle-Adjustment via Factor Graphs in Python',

    long_description=long_description,

    long_description_content_type='text/x-rst',

    url='https://github.com/BrendanDrew/calyx',

    author='Brendan Drew',

    author_email='brendan.drew.github@gmail.com',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],

    packages=find_packages(include=['calyx']),

    entry_points={
        'console_scripts': [
            'simulate_calibration_input=calyx.apps.simulate_calibration_input:main',
        ]
    },

    keywords='calibration photogrammetry python',

    install_requires=install_requirements,

    extras_require={
        'dev': developer_requirements,
        'test': test_requirements,
    },

    package_data={},
)
