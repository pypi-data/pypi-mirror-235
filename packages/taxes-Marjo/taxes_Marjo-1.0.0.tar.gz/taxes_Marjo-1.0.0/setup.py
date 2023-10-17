from setuptools import setup, find_packages


setup(
    name="taxes_Marjo",
    version='1.0.0',
    author="Marjol Mata",
    author_email="<marjolmata29@gmail.com>",
    description='A package that generate taxes based on the salary',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=[ 'Taxes', 'tax'],

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)