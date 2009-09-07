# -*- coding: utf-8 -*-

import grokcore.view as grok
import dolmen.app.layout as layout
from zope.size import byteDisplay
from zope.traversing.browser.absoluteurl import absoluteURL
from menhir.contenttype.image import IImage, ImagePopup


class ImageView(layout.Index):
    """Default view for an image.
    """
    grok.context(IImage)
    
    def update(self):
        ImagePopup.need()
        url = absoluteURL(self.context, self.request)
        self.size = byteDisplay(self.context.image.getSize())
        self.thumbnail = "%s/++thumbnail++image.preview" % url
        self.popup_url = "%s/++thumbnail++image.large" % url
        self.download_url = "%s/++download++image" % url
