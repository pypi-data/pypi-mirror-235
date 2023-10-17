from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Singly LinkedList operations package'
# LONG_DESCRIPTION = 'A pacakage consists of most used operations perform on Singly LinkedList Example: 1. Insertion [ head , tail , In  Between ] 2. Deletion [ head , tail , In Between ] 3. Finding Length of linkedlist 4. Reversing a linkedlist 5. Searching node in linkedlist 6. Finding Middle node of Linkedlist 7. Finding Occurence of Node in given LinkedList 8. Finding Intersection of Two LinkedList'

# Setting up
setup(
    name="Rayuga35_LinkedList",
    version=VERSION,
    author="Shubham Vishwakarma",
    author_email="vishwakarmashubham.2503@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.txt').read()+'\n\n'+open('CHANGELOG.txt').read(),
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'tutorial', 'LinkedList', 'Operations', 'Shubham','Data Structure','Insertion','Reverse','Deletion','Occurence','Length','Intersection'],
    classifiers=[
        "Development Status :: 5 - Production/Stable" ,
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]
)