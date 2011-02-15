django-oauth-access
===================

An app that supports connecting to oAuth sites.

Installation
------------

### Requirements:

* Python *2.4+* (Python 3.x is *not* supported yet)
* Django *1.2+*

### Steps:

Add the app to your python path from github:

	git clone https://github.com/shelfworthy/django-oauth-access.git

Using pip:

	pip install -e git+https://github.com/shelfworthy/django-oauth-access.git#egg=django_oauth_access-0.1.dev10-py2.6-dev

Usage
-----

Add oauth_access to your INSTALLED_APPS:

	INSTALLED_APPS = [
	    # ...
	    "oauth_access",
	]

Add your service keys to your settings file:

	CONNECTION_SETTINGS = {
	    "twitter": {
	        # to obtain these visit http://dev.twitter.com/apps/new
	        "keys": {
	            "KEY": "<your key here>",
	            "SECRET": "<your secret here>",
	        }
	    },
	    "facebook": {
	        "keys": {
	            # to obtain these visit http://developers.facebook.com/setup/
	            "KEY": "<your key here>",
	            "SECRET": "<your secret here>",
	        },
	    }
	}

Hook up oauth_access to your URLconf:

	urlpatterns = patterns("",
	    # ...
	    url(r"^oauth/", include("oauth_access.urls"))
	)