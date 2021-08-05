from setuptools import setup

with open("README.rst", "r") as fin:
    long_description = fin.read()

setup(
    name='am-rocker',
    version='0.1.0',
    packages=['am_rocker'],
    package_data={'am_rocker': ['templates/*.em']},
    author='Andres Montano',
    author_email='andres.montano@tecnalia.com',
    description='Extra plugins for rocker',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/anfemosa/am-rocker",
    license='Apache 2.0',
    install_requires=[
        'rocker',
    ],
    entry_points={
        'rocker.extensions': [
            'am_devenv = am_rocker.devenv:Devenv',
        ]
    }
)
