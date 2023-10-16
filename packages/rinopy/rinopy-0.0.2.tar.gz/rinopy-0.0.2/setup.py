from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2'
DESCRIPTION = 'Personal utility packages'
# LONG_DESCRIPTION = 'Personal utility packages for personal quick data science and machine learning things.'

# Setting up
setup(
    name="rinopy",
    version=VERSION,
    author="Gregorino Al Josan",
    author_email="<rino.grego@gmail.com>",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=['scikit-learn'],
    keywords=['python', 'machine learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        # "Operating System :: Unix",
        # "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)