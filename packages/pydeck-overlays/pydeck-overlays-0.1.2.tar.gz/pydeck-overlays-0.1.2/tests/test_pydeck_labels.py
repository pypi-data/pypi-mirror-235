#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pydeck_overlays` package."""
import os
import tempfile
import pytest
import pydeck as pdk
import geopandas as gpd


from pydeck_overlays import LabelLayer


HERE = os.path.dirname(__file__)


@pytest.fixture
def data():
    data = gpd.read_file(os.path.join(HERE, "data", "label_test.json"))
    return data


@pytest.fixture
def view(data):
    view = pdk.ViewState(
        longitude=float(data.longitude.mean()),
        latitude=float(data.latitude.mean()),
        zoom=3,
        min_zoom=2,
        max_zoom=10,
        pitch=0,
        bearing=0,
    )
    return view


def handle_event(event):
    print(event)


def test_label_simple(data, view):
    layer = LabelLayer(data, id="test", get_border_color=[255, 255, 255, 255])
    assert isinstance(layer, pdk.Layer)
    r = pdk.Deck(
        layer,
        initial_view_state=view,
    )

    fname = tempfile.mktemp(suffix=".html")
    r.to_html(fname, True)


def test_label_event(data, view):
    layer = LabelLayer(
        data, id="test", get_border_color=[255, 255, 255, 255], pickable=True
    )
    assert isinstance(layer, pdk.Layer)
    r = pdk.Deck(
        layer,
        initial_view_state=view,
        on_click=handle_event,
    )

    fname = tempfile.mktemp(suffix=".html")
    r.to_html(fname, True)


def test_label_icon(data, view):
    layer = LabelLayer(
        data,
        font_size=48,
        id="test_icon",
        get_icon_url="https://img.icons8.com/color/48/000000/airplane-take-off.png",
        get_border_color=[255, 255, 255, 255],
    )
    assert isinstance(layer, pdk.Layer)
    r = pdk.Deck(
        layer,
        initial_view_state=view,
    )

    fname = tempfile.mktemp(suffix=".html")
    r.to_html(fname, True)


def test_label_colors(data, view):
    layer = LabelLayer(
        data,
        id="test_icon",
        get_color="color",
        get_background_color=[0, 0, 0, 200],
        padding=10,
    )
    assert isinstance(layer, pdk.Layer)
    r = pdk.Deck(
        layer,
        initial_view_state=view,
    )

    fname = tempfile.mktemp(suffix=".html")
    r.to_html(fname, True)
