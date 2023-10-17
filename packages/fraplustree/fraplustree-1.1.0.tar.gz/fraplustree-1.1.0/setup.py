from setuptools import setup, find_packages


setup(
    name="fraplustree",
    version='1.1.0',
    author="Guido Xhindoli",
    author_email="<mail@gmail.com>",
    description='A package draws tree and fractals',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "PythonTurtle==0.3.2"
    ],
    keywords=[ 'fraplustree', 'SDA', 'fra', 'tree'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)