import streamlit as st
import cv2
import numpy as np
from PIL import Image

protoFile = "models/pose/coco/pose_deploy_linevec.prototxt"
weightsFile = "models/pose/coco/pose_iter_440000.caffemodel"
nPoints = 18

POSE_PAIRS = [[1, 2], [1, 5], [2, 3], [3, 4], [5, 6], [6, 7], [1, 8], [8, 9], [9, 10], 
              [1, 11], [11, 12], [12, 13], [0, 14], [0, 15], [14, 16], [15, 17]]

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

def estimate_pose(image):
    frameWidth = image.shape[1]
    frameHeight = image.shape[0]
    inpBlob = cv2.dnn.blobFromImage(image, 1.0 / 255, (368, 368), (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()
    
    H = output.shape[2]
    W = output.shape[3]
    points = []
    for i in range(nPoints):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H

        if prob > 0.1:
            points.append((int(x), int(y)))
        else:
            points.append(None)

    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:
            cv2.line(image, points[partA], points[partB], (0, 255, 255), 2)
            cv2.circle(image, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(image, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

    return image

st.title("Human Pose Estimation Web App")
st.write("**Created by Ansh Kumar Tripathi under the AICTE internship**")

st.write("""
This web app performs human pose estimation on an uploaded image using OpenCV and the OpenPose model. 
It highlights keypoints and connections on the detected human poses.
""")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Estimating pose...")
    output_image = estimate_pose(image)
    st.image(output_image, caption='Output Image with Pose Estimation.', use_column_width=True)
