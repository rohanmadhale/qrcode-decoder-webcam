from __future__ import print_function
import cv2
import streamlit as st


import pyzbar.pyzbar as pyzbar
import numpy as np
# import cv2
import time
# from PIL import Image

# st.title("Webcam Live Feed")
st.title("QR code decoder using WebCam")

run = st.radio("Click here to : ", ('Stop Camera', 'Start Camera'))
if run == 'Start Camera':
    stat = True
elif run == 'Stop Camera':
    stat = False
# run = st.checkbox('Run')


FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)


def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    return decodedObjects


def yet_another_decoder(string):
    return str(string).replace('b', '').replace("'", "")  # decodedObject.data


apple = ''


while stat:

    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

    decodedObjects = decode(frame)

    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        if decodedObject.data != apple:
            st.write('Data : ', yet_another_decoder(decodedObject.data), '\n')

            apple = decodedObject.data


else:

    # st.write(my_items)
    st.write('Stopped')
