from setuptools import setup, find_packages

setup(
    name='pypapago',
    version='0.1.1',
    url='https://github.com/Beomi/pypapago',
    license='MIT',
    author='Junbum Lee',
    author_email='jun@beomi.net',
    description='[Unofficial] Python wrapper for Papago translation service',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests<3'],
)
