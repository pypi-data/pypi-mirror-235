# -*- coding: utf-8 -*-
"""Contains helpers for calculating font sizes."""

from math import sqrt
from typing import Union

import pdfrw

from ..middleware.constants import GLOBAL_FONT_SIZE
from . import constants, template


def text_field_font_size(element: pdfrw.PdfDict) -> Union[float, int]:
    """
    Calculates the font size it should be drawn with
    given a text field element.
    """

    if template.is_text_multiline(element):
        return GLOBAL_FONT_SIZE

    height = abs(
        float(element[constants.ANNOTATION_RECTANGLE_KEY][1])
        - float(element[constants.ANNOTATION_RECTANGLE_KEY][3])
    )

    return height * 2 / 3


def checkbox_radio_font_size(element: pdfrw.PdfDict) -> Union[float, int]:
    """
    Calculates the font size it should be drawn with
    given a checkbox/radio button element.
    """

    area = abs(
        float(element[constants.ANNOTATION_RECTANGLE_KEY][0])
        - float(element[constants.ANNOTATION_RECTANGLE_KEY][2])
    ) * abs(
        float(element[constants.ANNOTATION_RECTANGLE_KEY][1])
        - float(element[constants.ANNOTATION_RECTANGLE_KEY][3])
    )

    return sqrt(area) * 72 / 96
