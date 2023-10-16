import os
import streamlit as st
import streamlit.components.v1 as components

from st_screen_stats import IS_RELEASE

if not IS_RELEASE:
    _st_screen_data = components.declare_component(

        "st_screen_data",

        url="http://localhost:3001",
    )
else:
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_screen_data = components.declare_component("st_window_query_size", path=build_dir)


class WindowQuerySize:

    def __init__(self) -> None:
        pass

    def mediaQuery(self, mediaMatchQ=None, default=None, key=None):

        if mediaMatchQ == None or type(mediaMatchQ) != str:
            return

        value = _st_screen_data(windowType="mediaQuery", mediaMatchQ=mediaMatchQ, key=key, default=default)

        return value
