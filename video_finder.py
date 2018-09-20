# run with python video_finder.py

import cv2
import numpy as np 
from finder import *
from pyimagesearch.centroidtracker import CentroidTracker

# Path to source and output video
# path = 'RCNX0024.AVI'
path = 'mice2.avi'
output = 'output3.AVI'

# Load video
cap = cv2.VideoCapture(path)

ct = CentroidTracker()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')		# MJPG for mac os, check for Windows
out = cv2.VideoWriter(output, fourcc, 20.0, (1024,576))

# Check if video opened successfully
if (not cap.isOpened()): 
	print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()		# ret is True is frame successfully read
	if ret == True:

		# Process
		circled, rects = extract_data_from(frame)
		objects = ct.update(rects)

		# loop over the tracked objects
		for (objectID, centroid) in objects.items():
			# draw both the ID of the object and the centroid of the
			# object on the output frame
			text = "ID {}".format(objectID)
			cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

		# show the output frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		out.write(frame)

		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

		# # Display the resulting frame
		# cv2.imshow(path,circled)
		# # Save resulting frame
		# out.write(frame)

		# # Press Q on keyboard to exit
		# if cv2.waitKey(20) & 0xFF == ord('q'):
		# 	break

	# Break the loop
	else: 
		break

# Release the video capture object and videowriter object
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()