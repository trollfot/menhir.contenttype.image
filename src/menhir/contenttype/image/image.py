# -*- coding: utf-8 -*-

import megrok.resourcelibrary
import dolmen.content as content
import dolmen.app.security.content as security

from dolmen.file import ImageField
from dolmen.blob import BlobProperty
from menhir.library.jquery import SlimBox

from zope.schema import Text
from zope.i18nmessageid import MessageFactory
from zope.dublincore.property import DCProperty

_ = MessageFactory('dolmen')


class ImagePopup(megrok.resourcelibrary.ResourceLibrary):
    megrok.resourcelibrary.depend(SlimBox)
    megrok.resourcelibrary.directory('resources')
    megrok.resourcelibrary.include('popup.js')


class IImage(content.IBaseContent):
    """Defines a simple object that contains an image.
    """ 
    image = ImageField(
        title = _(u"Image"),
        required = True
        )


class Image(content.Content):
    """A simple image storing its data in a blob.
    """
    content.name(_(u"Image"))
    content.schema(IImage)
    content.icon("image.png")
    content.require(security.CanAddContent)
    
    image = BlobProperty(IImage['image'])
  
