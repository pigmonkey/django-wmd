from setuptools import setup, find_packages

setup(
    name = 'Django WMD',
    version = '0.1',
    description = 'A resuable Django app for a Markdown WMD editor widget.',
    long_description = open('README.md').read(),
    license = 'MIT',
    url = 'https://github.com/pigmonkey/django-wmd',
    author = 'Pig Monkey',
    author_email = 'pm@pig-monkey.com',

    packages = find_packages(),
    zip_safe=False,
)
