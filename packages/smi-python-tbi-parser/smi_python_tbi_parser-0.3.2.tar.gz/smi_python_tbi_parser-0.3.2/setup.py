from setuptools import setup, find_packages

from smi_python_tbi_parser.project import VERSION, NAME

setup(
    name=NAME,
    version=VERSION,
    description='setmy.info Python TBI parser library.',
    long_description='setmy.info Python TBI parser library.',
    author='Imre Tabur',
    author_email='info@setmy.info',
    license='MIT',
    url='https://github.com/setmy-info/python-tbi-parser',
    packages=find_packages(),
    install_requires=[
        "smi-python-commons==0.3.3"
    ],
)
