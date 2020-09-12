import cv2
import numpy as np
import os


img = np.zeros((3,3), dtype=np.int8)
print(img.shape)


image = cv2.imread("MyPic.png")
cv2.imwrite("MyPic.jpg", image)


flowerImage = cv2.imread("MyPic.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("window01",flowerImage)
cv2.waitKey(1000)
cv2.destroyWindow("window01")


randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite("randomImageGRAY.jpg", grayImage)

bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite("randomImageBGR.jpg", bgrImage)


img = cv2.imread("MyPic.png")
img.itemset((150, 120, 0), 255)
print(img.item(150, 120, 0))

img = cv2.imread("MyPic.png")
img[:, :, 1] = 0
cv2.imshow("window02",img)
cv2.waitKey(1000)
cv2.destroyWindow("window02")

img = cv2.imread("MyPic.png")
my_roi = img[0:100, 0:100]
print(img.shape)
img[190:290, 190:290] = my_roi
cv2.imshow("Window03", img)
cv2.waitKey(1000)
cv2.destroyWindow("Window03")


videoCapture = cv2.VideoCapture("MyInputVid.avi")
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter("MyOutputVid.avi",
                              cv2.VideoWriter_fourcc("I", '4', '2', '0'),
                              fps,
                              size)
success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()


videoCapture = cv2.VideoCapture("MyInputVid.avi")
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter("MyOutputVid2.avi",
                              cv2.VideoWriter_fourcc("I", "4", "2", "0"),
                              fps,
                              size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()


cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter =  cv2.VideoWriter("CameraOutput.avi",
                               cv2.VideoWriter_fourcc("I", "4", "2", "0"),
                               fps,
                               size)

numOfFrames = 30 * fps - 1

success, frame = cameraCapture.read()

while success and numOfFrames > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numOfFrames -= 1


clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow("MyVideoWindow")
cv2.setMouseCallback("MyVideoWindow", onMouse)

print("Showing Camera Feed. click window or press any key to stop.")
success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow("MyVideoWindow",frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow("MyVideoWindow")
cameraCapture.release()