# -*- coding: utf-8 -*-
from PIL import Image
from plone.namedfile.scaling import ImageScaling
from StringIO import StringIO
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse
from zope.traversing.interfaces import ITraversable

import logging


# from .. import messageFactory as _
logger = logging.getLogger("Plone")


@implementer(ITraversable, IPublishTraverse)
class GrayscaleImageScalingView(ImageScaling):

    def create(self,
               fieldname,
               direction='thumbnail',
               height=None,
               width=None,
               **parameters):
        parent = super(GrayscaleImageScalingView, self)
        img, format, dimension = parent.create(fieldname, direction,
                                               height,
                                               width,
                                               **parameters)

        if 'quality' not in parameters:
            quality = self.getQuality()
            if quality:
                parameters['quality'] = quality

        bw_img = Image.open(StringIO(img.data)).convert('L')
        result = StringIO()
        bw_img.save(result, format, quality=quality, optimize=True,
                    progressive=True)
        result = result.getvalue()

        value = img.__class__(result, contentType=img.contentType,
                              filename=img.filename)
        value.filename = img.filename
        return value, format, dimension
