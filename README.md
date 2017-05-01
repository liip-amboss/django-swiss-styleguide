Swiss Style
===========

This app is a simple extension for the federal swiss style guide.

It assumes that you have [the swiss styleguide](https://github.com/swiss/styleguide/ install e) 
installed (via npm). You should also have i18n activated. Probably 
the urls.py needs an update for this:


```
    url(r'^i18n/', include('django.conf.urls.i18n')),
```


It provides a basic template (swiss_base.html) with changeble blocks.

It also provides the tag {% swiss_field %} which is an extended version of
the bootstrap_field but with the styling ready for the swiss styleguide.

Work in Progress



TODO
----

* Make blocks out of everything
* Document the blocks
* Document the fact that there must be a 'home' 
