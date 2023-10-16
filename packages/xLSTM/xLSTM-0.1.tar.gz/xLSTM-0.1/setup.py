from setuptools import setup, find_packages


def requirements():
    with open("requirements.txt", "r") as f:
        return f.read().splitlines()

def readme():
    with open("README.md", "r") as f:
        return f.read()

setup(
    name='xLSTM',
    version='0.1',
    author='Patrick Haller',
    description='Lets hope for a GPT-free future.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages("src"),
    license="Apache 2.0",
    python_requires=">=3.8.0",
    install_requires=requirements(),
)
