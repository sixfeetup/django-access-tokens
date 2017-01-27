"""
A Django app for for generating secure scoped access tokens.

Developed by Mohawk.

<http://www.mohawkhq.com/>


Contributors
------------

- Dave Hall <http://blog.etianen.com/>
"""
import pkg_resources

__version__ = pkg_resources.get_distribution("django-access-tokens").version
