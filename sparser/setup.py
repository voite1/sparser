from setuptools import setup

setup (
    # Project name
    name="sparser",
    
    # Project version
    version="0.1",
    
    # Project author
    author="Aleksey Kramer",
    
    # Project description
    description='news web scraper',
    
    # Project URL
    url='https://github.com/voite1/sparser',
    
    # Required prerequisites 
    install_requires = [
        'joblib', 
        'beautifulsoup4'
        ],
    
    # Project classifiers
    classifiers=[
        'Programming Language :: Python :: 3.6',
        ],
    )

