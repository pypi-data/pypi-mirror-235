from setuptools import setup, find_packages

from smi_python_runner.project import NAME, VERSION

setup(
    name=NAME,
    version=VERSION,
    description='setmy.info Python runner library.',
    long_description='setmy.info Python runner library.',
    author='Imre Tabur',
    author_email='info@setmy.info',
    license='MIT',
    url='https://github.com/setmy-info/python-runner',
    packages=find_packages(),
    install_requires=[
        "smi-python-commons==0.3.3"
    ],
)
