from setuptools import find_packages, setup

with open("README.md", "r") as cd:
    long_description = cd.read()

setup(
    name='dhasher',
    packages=find_packages(include=['dhasher']),
    version='0.1.0',
    description='A python library for password hashing and verification existing password hashes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Geoffrey Israel',
    author_email="israelgeoffrey13@gmail.com",
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
