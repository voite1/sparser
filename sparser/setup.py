from setuptools import setup

setup (
    name="sparser",
    version="0.1",
    author="Aleksey Kramer",
    description='news web scraper',
    url='https://github.com/voite1/sparser',
    
    install_requires = [
        'joblib', 
        'beautifulsoup4'
        ],
       
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
    )

