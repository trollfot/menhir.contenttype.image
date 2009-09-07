# -*- coding: utf-8 -*-

import grok
import shutil

from ZODB.blob import Blob
from zope.lifecycleevent import IObjectCopiedEvent
from dolmen.imaging import IImageMiniaturizer
from menhir.contenttype.image import IImage


@grok.subscribe(IImage, IObjectCopiedEvent)
def copyImage(target, event):
    original = event.original
    target = event.object
    target.image._blob = Blob()

    fsrc = original.image._blob.open('r')
    fdst = target.image._blob.open('w')
    shutil.copyfileobj(fsrc, fdst)
    fdst.close()
    fsrc.close()

    thumbnailer = IImageMiniaturizer(target)
    thumbnailer.generate_thumbnails()
