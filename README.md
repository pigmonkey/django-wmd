Django WMD
==========

Django WMD is a reusable [Django](http://www.djangoproject.com) application for a [Markdown](http://daringfireball.net/projects/markdown/) WMD editor. It consists of a widget, to be used on a `textarea` field, that will provide a JavaScript-based [What You See Is What You Mean](https://secure.wikimedia.org/wikipedia/en/wiki/WYSIWYM) editor to assist in writing the Markdown markup language. A live preview is provided courtesy of Showdown.

WMD
---

Django WMD uses [ChiperSoft's WMD](https://github.com/ChiperSoft/wmd), which is a fork of [Open Library's WMD](https://github.com/openlibrary/wmd), which is a fork of [Stackoverflow's WMD](https://github.com/derobins/wmd/), which was reverse-engineered from the original WMD by John Fraser (who was abducted by aliens sometime in 2008). It's sort of an orgy of forking.

The included JavaScript is ChiperSoft's combined and minified version of WMD and Showdown.

Installation
------------

1.  Put the `wmd` directory somewhere inside your Python path (like in your Django project folder).
2.  Add `wmd` to your `settings.INSTALLED_APPS`.

Usage
-----

To add the WMD widget to a field in the Django admin, first create a `ModelForm`. Your application's `forms.py` is probably a good place to put it. In this example, I'll assign the widget to the `body` field of `myapp.models.Post`.

    from django import forms
    from myapp.models import Post
    from wmd.widgets import WMDWidget

    class PostForm(forms.ModelForm):
        body = forms.CharField(widget=WMDWidget)
        class Meta:
            model = Post

Then tell Django to use the `ModelForm` on the admin site.

    ...
    from myapp.forms import PostForm
    
    class PostAdmin(admin.ModelAdmin):
        form = PostForm
        ...
    admin.site.register(Post, PostAdmin)

### Options

The widget currently takes one option: `large`. If set to true, this will make the widgetized textarea larger than usual. This is much nicer for writing lengthy content, such as blog posts.

An example:

    class PostForm(forms.ModelForm):
        body = forms.CharField(widget=WMDWidget(large=True)
        ...
