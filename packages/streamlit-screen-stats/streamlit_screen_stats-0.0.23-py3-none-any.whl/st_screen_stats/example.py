import streamlit as st
# from __init__ import my_component
# from __init__ import SizeRange #ScreenData, StreamlitNativeWidgetScreen
from st_screen_stats import ScreenData, StreamlitNativeWidgetScreen # ScreenData, StreamlitNativeWidgetScreen

st.set_page_config(layout="wide")

# size_r = SizeRange()
# val_ = size_r.mediaQuery(mediaMatchQ="(max-width: 700px)")
# st.write(val_)

# st.subheader("Component with constant args")

screenD = ScreenData()
screen_d = screenD.st_screen_data_window_top()

st.write(screen_d)


st.subheader("native widget method")
screenDN = StreamlitNativeWidgetScreen()
screenDN.st_screen_data_window_top()
stats_ = screenDN.get_window_screen_stats(key="get_item")
st.write(stats_)

# screenRange = SizeRange()
# val_ = screenRange.WidthRange(lowerRange=400, upperRange=500)
# st.write(val_)

# upperScreenWidth = 1000

js_el = f'''
            <script>

                let testD = window.matchMedia("(max-width: 700px)")
            
                function test (e) {{
                
                    let val_ = window.matchMedia("(max-width: 700px)").matches
                    console.log(val_)
                
               
                }}
                
                
                testD.addEventListener("change", test)
                //window.removeEventListener("resize", test)
                
            </script>

        '''
# st.components.v1.html(js_el)

# # my_component()


