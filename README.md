## Sample Instructions for package development

### Create and upload package
1. Create an account at pypi.python.org
2. Edit 'setup.py' file to describe package
3. Use `python setup.py check` to validate file
4. Use `python setup.py register` to publish package info (will prompt for un/pw)
5. Use `python setup.py sdist upload` to create a download file, and push to Pypi

> Register command is used to create the initial package, as well as send updates. By default the Pypi page will only show the latest package info, however this can be amended within the web interface.

### Testing install
pip install -e git+https://user@gitrepo.com/user/package.git#egg=package

### Project layout
```
MANIFEST.in # Describe non-Python files to include in distribution
README.md # Just good practice!
setup.py # Defines package info
package_name/
  __init__.py
  file.py
```

### Sample setup.py
```python
from setuptools import setup, find_packages
import os
import django_mock as app


CLASSIFIERS = [
    "Framework :: Django",  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
]

setup(
    author="Ashley Wilson",
    author_email="ash@jp74.com",
    name="django_mock",
    version=app.__version__,
    description="My test package",
    # Long desc will display on the PyPi page
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url="https://github.com/JP74/django-mock",
    download_url="https://github.com/JP74/django-mock/archive/master.zip",
    license="BSD",
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.6',
    ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=True,
    test_suite='run tests.main',
)

