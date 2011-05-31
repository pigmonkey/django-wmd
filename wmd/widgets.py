from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class WMDWidget(forms.Textarea):
    def __init__(self, large=False, *args, **kwargs):
        if large:
            attrs = kwargs.setdefault('attrs', {
                'class': 'extraLargeTextField wmd-panel',
            })
        else:
            attrs = kwargs.setdefault('attrs', {
                'class': 'vLargeTextField wmd-panel',
            })
        super(WMDWidget, self).__init__(*args, **kwargs)

    @property
    def media(self):
        return forms.Media(
            css = {'screen': ('wmd/wmd.css',)},
            js = ('wmd/wmd.js',)
        )

    def render(self, name, value, attrs=None):
        rendered = mark_safe(u'<div id="wmd-button-bar" class="wmd-panel"></div>')
        rendered += super(WMDWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''
            <div id="wmd-preview">
                <div id="wmd-preview-label">Preview:</div>
                <div id='wmd-preview-area' class="wmd-panel"></div>
            </div>
            <script type="text/javascript">
                setup_wmd({
                    input: "%s",
                    button_bar: "wmd-button-bar",
                    preview: "wmd-preview-area",
                    helpLink: "http://daringfireball.net/projects/markdown/syntax"
            });
            </script>
            ''' % (attrs['id']))
