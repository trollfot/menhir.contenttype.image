# -*- coding: utf-8 -*-

import grok
from zope.lifecycleevent import IObjectCopiedEvent
from menhir.contenttype.image import IImage
from dolmen.thumbnailer import IImageMiniaturizer


@grok.subscribe(IImage, IObjectCopiedEvent)
def copyImage(target, event):
    original = event.original
    target = event.object
    fdst = target.image = original.image.data
    thumbnailer = IImageMiniaturizer(target)
    thumbnailer.generate_thumbnails()
