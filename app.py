import streamlit as st
from pytube import YouTube 

with st.sidebar:
    # get youtube url
    url = st.text_input("YouTube URL")
    quality_options = []
    if url:
        yt = YouTube(url)
        audio_list = yt.streams.filter(only_audio=True)
        for audio in audio_list:
            quality_options.append(audio.abr)
        print(quality_options)

with st.container():
    col1, col2 = st.columns(2)
    

    with col1:
        st.image(yt.thumbnail_url, width=128)
    with col2:
        option = st.selectbox(
            "Choose the audio quality you are looking for",
            (quality_options)
            )
        st.write("you selected: ", option)
