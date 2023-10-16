from setuptools import setup, find_packages

setup(
    name='CookieXplorer',
    version='0.1.0',
    description='A Python package to handle cookie acceptance using XPath in web scraping automation.',
    author='Aman Ojha',
    author_email='amanojha258@gmail.com',
    url='https://github.com/amanojha258/Web-Scraping-Cookie-Handler.git',
    packages=find_packages(),
    install_requires=[
        'pyppeteer',
        'asyncio',
    ],
)

