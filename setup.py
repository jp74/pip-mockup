from setuptools import setup, find_packages
import os
import django_mock as app


CLASSIFIERS = [
    "Framework :: Django",  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
]

setup(
    author="Ashley Wilson",
    author_email="ash@jp74.com",
    name="django-mock",
    version=app.__version__,
    description="My test package",
    # Long desc will display on the PyPi page
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url="www.package-website.com",
    download_url="https://gitrepo.com/user/package/downloads/tar_file.tar.gz",
    license="BSD",
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.6',
    ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False,
    test_suite='run tests.main',
)