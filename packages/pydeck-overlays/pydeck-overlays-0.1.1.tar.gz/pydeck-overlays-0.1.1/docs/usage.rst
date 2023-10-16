=====
Usage
=====

To use pydeck-overlays in a project::

    import tempfile
    import pydeck as pdk
    import geopandas as gpd
    import pydeck_overlays
    from pydeck_overlays import LabelLayer

    #This is some sample data included with the library
    data = gpd.read_file(os.path.join(HERE, "data", "label_test.json"))

    view = pdk.ViewState(
        longitude=float(data.longitude.mean()),
        latitude=float(data.latitude.mean()),
        zoom=3,
        min_zoom=2,
        max_zoom=10,
        pitch=0,
        bearing=0,
    )

    layer = LabelLayer(data, id="my-layer", get_border_color=[255, 255, 255, 255])
    assert isinstance(layer, pdk.Layer)
    r = pdk.Deck(
        layer,
        initial_view_state=view,
    )

    fname = tempfile.mktemp(suffix=".html")
    r.to_html(fname, True)
    


The ``data`` argument is always a geopandas GeoDataFrame.

