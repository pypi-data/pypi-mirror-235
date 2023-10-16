# setup.py
from setuptools import setup, find_packages

setup(
    name='corlace-sdk',
    version='0.1.0',
    description='A description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your-email@example.com',
    url='https://github.com/your-username/corlace-sdk',  # replace with the URL of your project's repository
    packages=find_packages(),
    install_requires=[
        "urllib3",
        "Flask",
        "setuptools",
        "Werkzeug",
        "PyYAML"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # change license as needed
    ],
    python_requires='>=3.6',
)
