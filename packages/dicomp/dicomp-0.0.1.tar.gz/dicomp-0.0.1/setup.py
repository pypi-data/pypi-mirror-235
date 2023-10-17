from setuptools import setup, find_packages

setup(
    name='dicomp',
    version='0.0.1',
    description='This is a project developed by Serem for development purposes',
    author='serem',
    author_email='gangh9230@gmail.com',
    url='https://github.com/hayul0629/wdex',
    install_requires=[
        "novus==0.2.3",
        "nextcord",
    ],
    packages=find_packages(exclude=[]),
    python_requires=">=3.9",
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
