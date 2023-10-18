import streamlit as st
from st_img_card import my_component

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`


col1, col2, col3 = st.columns(3)

with col1:
    num_clicks = my_component("http://localhost:8000/image/3b194819-6a3a-4a39-8032-061a7bf74df7_1696328802496_1",
                                "Some Header",
                                "This is some common message I wanted to write here to make the the text long enough",
                                "key1"
                            )
    text_contents = '''This is some text'''
    st.download_button('Download', text_contents, key="key12")

with col2:
    num_clicks = my_component("http://localhost:8000/image/3b194819-6a3a-4a39-8032-061a7bf74df7_1696328802496_2",
                                "Some Header",
                                "This is some common message I wanted to write here to make the the text long enough",
                                "key2"
                            )
    text_contents = '''This is some text'''
    st.download_button('Download', text_contents, key="key22")


with col3:
    num_clicks = my_component("http://localhost:8000/image/3b194819-6a3a-4a39-8032-061a7bf74df7_1696328802496_3",
                                "Some Header",
                                "This is some common message I wanted to write here to make the the text long enough",
                                "key3"
                            )
    text_contents = '''This is some text'''
    st.download_button('Download', text_contents, key="key32")
