from setuptools import setup, find_packages

setup(
    name='wappalyzer-python',
    version='0.1.2',
    url='https://github.com/gatufo/wappalyzer-python',
    description='Python wrapper for Wappalyzer (utility that uncovers the technologies used on websites)',
    author='Javier Casas',
    author_email='gatufo@gmail.com',
    packages=find_packages(),
    package_data={'': ['data/*.*', 'data/icons/*.*']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords=['wappalyzer', 'scraping', 'crawling', 'site'],
    install_requires=[
        'requests',
        'PyV8',
        'lxml',
    ],
)


