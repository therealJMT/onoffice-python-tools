"""
Setup configuration for the OnOffice SDK.
"""

from setuptools import setup, find_packages

# Read version from version.py
with open('src/onoffice_sdk/version.py', 'r') as f:
    exec(f.read())

# Read README for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='onoffice-sdk',
    version=__version__,  # noqa: F821
    description='Python SDK for the OnOffice API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='therealJMT',
    author_email='mm@mentor-sw.de',
    license='MIT',
    url='https://github.com/therealJMT/onoffice-python-tools',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests>=2.31.0',
        'python-dotenv>=1.0.0',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
