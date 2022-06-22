import cv2
import matplotlib.pyplot as plt
# matplotlib inline
def imShow(path):
  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)
  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  
  plt.axis("off")
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  plt.show()


darknet_no_gpu detector test /Users/Castro/Desktop/Yolo2/darknet/data/obj.data /Users/Castro/Desktop/Yolo2/darknet/my_tiny.cfg yolov4.weights /Users/Castro/Desktop/Yolo2/imgTeste/img2.png
imShow('predictions.jpg')
