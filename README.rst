django-datatrans
================

By Jef Geskens, Koen Vossen; City Live nv and Robin Allen

FEATURES
--------

* Translate Django models without changing anything to existing applications and their underlying database.
* Uses a registration approach.
* All translations are stored in one extra lookup table. Existing database tables remain untouched.
* Recovery and cleanup of obsolete translations.
* Translation admin interface included (uses CSS from django admin).
* Transparent model API (in 99% of all cases, nothing has to be changed to original code).
* Infinite caching for all strings (based on id and hash)

HOW TO USE
----------

1. Add it to INSTALLED_APPS
2. Syncdb
3. Register models (example for FlatPage model):

    from datatrans.utils import register

    class FlatPageTranslation(object):
        fields = ('title', 'content')

    register(FlatPage, FlatPageTranslation)

4. Include the datatrans.urls in your urlconf somewhere, and point your browser to it!
5. Translate away!

Note: you can also search through your objects using translated query strings with the
`datatrans_filter` on your manager. For example:

    FlatPageTranslation.objects.datatrans_filter(title__icontains='zoek dit', language='nl')

will return a QuerySet containing those objects whose dutch title contains the
string 'zoek dit'. Note that this filter API is not identical to Django's, read the docstring
for more info.
