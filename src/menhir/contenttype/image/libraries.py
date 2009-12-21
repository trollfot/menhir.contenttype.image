#!/usr/bin/python
# -*- coding: utf-8 -*-

from megrok import resource
from menhir.library.jquery import slimbox


class ImagePopup(resource.Library):
    resource.path('resources')
    resource.name("image.popup")

popup = resource.ResourceInclusion(
    ImagePopup, "popup.js", depends=[slimbox])
