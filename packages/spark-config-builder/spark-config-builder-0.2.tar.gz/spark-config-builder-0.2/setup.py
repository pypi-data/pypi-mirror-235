from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

DESCRIPTION = 'Build an Apache Spark configuration easily using a config file.'

# Setting up
setup(
    name="spark-config-builder",
    version='0.02',
    author="kassett",
    author_email="samuel.chai.development@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=requirements,
    keywords=['pyspark'],
)