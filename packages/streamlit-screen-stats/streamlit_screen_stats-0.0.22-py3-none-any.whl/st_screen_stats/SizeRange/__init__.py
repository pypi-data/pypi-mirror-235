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
    _st_screen_data = components.declare_component("st_screen_data", path=build_dir)


class SizeRange:

    def __init__(self) -> None:
        pass

    def WidthUpperRange(self, upperRange:int=None, key=None, default=None):

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_data(windowType="windowSingleRange", rangeType="upper", heightWidth="width", upperRange=upperRange, key=key, default=default)

        return value
    
    def WidthLowerRange(self, lowerRange:int=None, key=None, default=None):

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_data(windowType="windowSingleRange", rangeType="lower", heightWidth="width", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def HeightUpperRange(self, upperRange:int=None, key=None, default=None):

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_data(windowType="windowSingleRange", rangeType="upper", heightWidth="height", upperRange=upperRange, key=key, default=default)

        return value
    
    def HeightLowerRange(self, lowerRange:int=None, key=None, default=None):

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_data(windowType="windowSingleRange", rangeType="lower", heightWidth="height", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def WidthUpperRangeTop(self, upperRange:int=None, key=None, default=None):

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_data(windowType="windowTopSingleRange", rangeType="upper", heightWidth="width", upperRange=upperRange, key=key, default=default)

        return value
    
    def WidthLowerRangeTop(self, lowerRange:int=None, key=None, default=None):

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_data(windowType="windowTopSingleRange", rangeType="lower", heightWidth="width", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def HeightUpperRangeTop(self, upperRange:int=None, key=None, default=None):

        if upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_data(windowType="windowTopSingleRange", rangeType="upper", heightWidth="height", upperRange=upperRange, key=key, default=default)

        return value
    
    def HeightLowerRangeTop(self, lowerRange:int=None, key=None, default=None):

        if lowerRange == None or type(lowerRange) != int:
            return

        value = _st_screen_data(windowType="windowTopSingleRange", rangeType="lower", heightWidth="height", lowerRange=lowerRange, key=key, default=default)

        return value
    
    def WidthRange(self, lowerRange:int=None, upperRange:int=None, key=None, default=None):

        if lowerRange == None or type(lowerRange) != int or upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_data(windowType="windowUpperLowerJoint", heightWidth="width", lowerRange=lowerRange, upperRange=upperRange, key=key, default=default)

        return value
    
    def HeightRange(self, lowerRange:int=None, upperRange:int=None, key=None, default=None):

        if lowerRange == None or type(lowerRange) != int or upperRange == None or type(upperRange) != int:
            return

        value = _st_screen_data(windowType="windowUpperLowerJoint", heightWidth="height", lowerRange=lowerRange, upperRange=upperRange, key=key, default=default)

        return value
    
    

