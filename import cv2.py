import cv2
import os
import time
import uuid
Img_path = '/Users/alf/Documents/DataCollectingTry/Images/CollectedImages'
labels= ['stop','forward','back']
num_imgs = 25
for label in labels:
  os.mkdir ('/Users/alf/Documents/DataCollectingTry/Images/CollectedImages//'+label)
  cap = cv2.VideoCapture(0)
  print('collecting images for {}'.format(label))
  time.sleep(4)
  for imgnum in range(num_imgs):
    ret, frame = cap.read()
    imagename = os.path.join(Img_path,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
    cv2.imwrite(imagename,frame)
    cv2.imshow('frame',frame)
    time.sleep(2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  cap.release()