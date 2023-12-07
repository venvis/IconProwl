from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'IconProwl : An unofficial API for scraping images off IconFinder.com for web development.'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="IconProwl",
    version="1.1.1",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vishal",
    author_email="vishalvenkat2604@gmail.com",
    license='MIT',
    packages=find_packages(),
      install_requires=[
        'pillow',
        'requests',
        'beautifulsoup4',
        'lxml',
        
    ],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
   
)