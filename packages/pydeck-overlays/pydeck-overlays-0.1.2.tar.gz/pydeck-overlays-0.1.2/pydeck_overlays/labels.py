import orjson
import webcolors as wc
import geopandas as gpd
import numpy as np
from matplotlib.colors import rgb2hex, hex2color
from pydeck.bindings.layer import Layer
from pydeck.types.base import PydeckType
from pydeck.bindings.json_tools import JSONMixin, IGNORE_KEYS, lower_camel_case_keys

import pydeck


pydeck.settings.custom_libraries = pydeck.settings.custom_libraries + [
    {
        "libraryName": "DeckOverlayLayers",
        "resourceUri": "https://assets.oceanum.io/packages/deck-gl-overlays/bundle.umd.cjs",
    }
]


def parse_color(color):
    if isinstance(color, str):
        if color.startswith("#"):
            color = wc.hex_to_rgb(color)
        else:
            color = wc.name_to_rgb(color)
    return color


class LabelLayerException(Exception):
    pass


class LabelLayer(Layer):
    """pydeck layer with label overlays"""

    def __init__(
        self,
        data,
        id=None,
        get_label="label",
        get_color=None,
        get_background_color=[100, 100, 100, 200],
        get_border_color=[50, 50, 50, 200],
        get_border_width=1,
        get_line_width=1,
        get_icon_url=None,
        font_size=14,
        font_family="'Arial'",
        font_weight=500,
        padding=2,
        opacity=1.0,
        max_labels=20,
        line_width=1,
        offscreen_labels=None,
        **kwargs
    ):
        """Configures a deck.gl layer for rendering data labels on a map.

        Args:
            data : geopandas.GeoDataFrame
                Data for labels with geometry column defining the label location
            id : str, default None
                Unique name for layer
            get_label : str, default 'label'
                Column name for label text
            get_color : str or array, default None
                Column name for label color or RGBA(0-255)  array for constant color
            get_background_color : str or array, default [100, 100, 100, 200]
                Column name for label background color or RGBA(0-255) array for constant color
            get_border_color : str or array, default [50, 50, 50, 200]
                Column name for label border color or RGBA(0-255) array for constant color
            get_border_width : int or str, default 1
                Column name for label border width or constant width
            get_line_width : int or str, default 1
                Column name for label line width or constant width
            get_icon_url : str, default None
                Column name for label icon url or constant icon URL
            font_size : int, default 14
                Font size in pixels
            font_family : str, default 'Arial'
                Font family
            font_weight : int, default 500
                Font weight
            padding : int, default 2
                Padding in pixels
            max_labels : int, default 20
                Maximum number of labels to render on screen for any view
            line_width : int, default 1
                Line width for label anchor line
            offscreen_labels : str, default None
                Where to placelabels that are offscreen. One of None, 'left', 'right'



        Raises:
            LabelLayerException
                missing or invalid arguments
        """

        if not isinstance(data, gpd.GeoDataFrame) and not data is None:
            raise LabelLayerException("data must be a GeoDataFrame")

        if isinstance(get_color, str):
            data["_r"], data["_g"], data["_b"] = zip(*data[get_color].map(parse_color))
            colorfn = ["_r", "_g", "_b", 255]
        elif isinstance(get_color, list):
            colorfn = get_color
        else:
            colorfn = [0, 0, 0, 255]

        super().__init__(
            "LabelLayer",
            data,
            id,
            get_label=get_label,
            get_color=colorfn,
            get_background_color=get_background_color,
            background=get_background_color is not None,
            get_border_color=get_border_color,
            get_border_width=get_border_width,
            get_line_width=get_line_width,
            get_icon_url=get_icon_url,
            font_size=font_size,
            font_family=font_family,
            font_weight=font_weight,
            padding=padding,
            max_labels=max_labels,
            line_width=line_width,
            offscreen_labels=offscreen_labels,
            **kwargs
        )
