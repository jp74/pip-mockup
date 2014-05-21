from setuptools import setup, find_packages
import os
import pip_mockup as app


CLASSIFIERS = [
    "Framework :: Django",
]

setup(
    author="JP74",
    author_email="mockup@sample.com",
    name="pip_mockup",
    version=app.__version__,
    description="My test package",
    # Long desc will display on the PyPi page
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url="https://github.com/jp74/pip_mockup",
    download_url="https://github.com/jp74/pip_mockup/archive/master.zip",
    license="BSD",
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.6',
    ],
    tests_require=[
        'pytest>=2.1'
    ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=True,
)
