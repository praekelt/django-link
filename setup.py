from setuptools import setup, find_packages

description_files = ["README.rst", "AUTHORS.rst", "CHANGELOG.rst"]

setup(
    name="django-link",
    description="Modeled link objects which include linking to objects, views and static urls.",
    long_description="".join([open(f, "r").read() for f in description_files]),
    version="2.0.0",
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/django-link",
    packages=find_packages(),
    dependency_links=[],
    install_requires=[
        "django",
        "djangorestframework-extras>=0.3"
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
    include_package_data=True
)
