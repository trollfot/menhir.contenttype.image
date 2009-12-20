# -*- coding: utf-8 -*-

import grokcore.view as grok
import dolmen.app.layout as layout

from megrok import resource
from menhir.contenttype.image import IImage, popup
from zope.size import byteDisplay
from zope.traversing.browser.absoluteurl import absoluteURL


class ImageView(layout.Index):
    """Default view for an image.
    """
    grok.context(IImage)
    resource.include(popup)
    
    def update(self):
        url = absoluteURL(self.context, self.request)
        self.size = byteDisplay(self.context.image.getSize())
        self.thumbnail = "%s/++thumbnail++image.preview" % url
        self.popup_url = "%s/++thumbnail++image.large" % url
        self.download_url = "%s/++download++image" % url
