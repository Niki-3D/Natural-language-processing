from setuptools import setup, find_packages

setup(
    name='',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'fuzzywuzzy',
        'python-Levenshtein',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            '',
        ],
    },
    author='',
    author_email='',
    description='A tool to analyze donation data with potential typos and similar entries.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
