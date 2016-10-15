Django Link
===========
**Modeled link objects which include linking to objects, views and static urls.**

.. figure:: https://travis-ci.org/praekelt/django-link.svg?branch=develop
   :align: center
   :alt: Travis

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-link`` to your Python path.

#. Add ``link`` to your ``INSTALLED_APPS`` setting.

#. Add ``url(r'^link/', include("link.urls", namespace="link"))`` to your ``url patterns`` (only required if you intend on using the list/detail views)

Note: ``django-link`` relies on ``"django.contrib.contenttypes"`` framework so
this will need to be included in your ``INSTALLED_APPS`` setting.

Usage
-----

``django-link`` provides a model to add links to your projects. It provides a ``get_absolute_url``
method on the model which provides the url to either of these url types:

#. Standard url string.

#. Link to an ``object`` provided by the contenttype framework.

#. Link to a pre-existing view with configurable view params.

To use include the link object in the context of your view and include the following code:
``{{ link.get_absolute_url  }}``

Or use the inclusion tag which has been provided:
``{% render_link object %}``

To exclude certain apps from the view name choice field add the namespace in your settings:
``LINK = {"excluded-viewname-choices": ["admin"]}``
