import streamlit as st
from pytube import YouTube 

def first(iterable, default=None):
  for item in iterable:
    return item
  return default

with st.sidebar:
    # get youtube url
    url = st.text_input("YouTube URL")
    quality_options = []
    if url:
        yt = YouTube(url)
        # get the audio from the video
        audio_list = yt.streams.filter(only_audio=True)
        for i in audio_list:
            # put aviable quality options into a list
            quality_options.append(i.abr)
        print(quality_options)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        if url:
            st.image(yt.thumbnail_url, width=128)
    with col2:
        if url:
            option = st.selectbox(
                "Choose the audio quality you are looking for",
                (quality_options)
                )
            st.write("you selected: ", option)
            stream = first(x for x in audio_list if x.abr == option)
            print(type(stream))
            audio = yt.streams.get_by_itag(stream.itag)
            btn = st.download_button(
                label='Download audio file',
                data=audio.download(),
                mime=stream.mime_type
            )