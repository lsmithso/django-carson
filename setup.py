from setuptools import setup, find_packages
import carson

setup(
    name             = "django-carson",
    version          = carson.__version__,
    packages         = find_packages(exclude=["example_project"]),
    url              = "https://github.com/edavis/django-carson",
    author           = "Eric Davis",
    author_email     = "ed@npri.org",
    description      = "Store tweets posted by a set of users along with tweets containing certain hashtags and/or keywords",
    long_description = open('README.rst').read(),
    install_requires = [
        "pytz==2011h",
        "oauth2==1.5.170",
        "httplib2==0.7.1",
        "django-extensions==0.6",
    ],
    classifiers      = [
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
    ],
)
