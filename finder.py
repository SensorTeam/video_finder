from detect_bright_spots import *
from circle_filter import *
from diagnostic_tool import *
import os

# Returns image with eyes circled
def extract_data_from(image):
	# Increase contrast
	# clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(16,16))
	# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# contrast = clahe.apply(gray)
	# contrast = cv2.cvtColor(contrast, cv2.COLOR_GRAY2BGR)

	cnts, thresh = detect_bright_spots(image)
	# show_thresh(thresh)
	contours = circle_filter(cnts)
	circled = circle_contours(contours,image)
	# show_contours(contours, image)

	return circled
	

# returns image with contours circled
def circle_contours(cnts, image):
	# loop over the contours
	for (i, c) in enumerate(cnts):
		# draw the bright spot on the image
		(x, y, w, h) = cv2.boundingRect(c)
		((cX, cY), radius) = cv2.minEnclosingCircle(c)
		cv2.circle(image, (int(cX), int(cY)), int(radius)+4,
			(0, 0, 255), 2)

	# show the output image
	image = cv2.resize(image, (954, 634))
	return image


# # Run main on one image
# path = "mice.jpg"
# image = cv2.imread(path)
# image = extract_data_from(image)
# cv2.imshow(path, image)
# cv2.waitKey(0)
