from setuptools import setup, find_packages


setup(
    name="salaryandtaxcalculator",
    version='1.0.1',
    author="Pamela Haxhici",
    author_email="<pamelahaxhici@gmail.com>",
    description='A package that calculates tax based on salary',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=[ 'salaryandtaxcalculator', 'SDA', 'salary', 'calculator', 'tax'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)