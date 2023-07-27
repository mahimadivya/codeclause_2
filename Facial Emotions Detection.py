#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install deepface


# In[2]:


#import the required modules
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace


# In[3]:


# read image
img = cv2.imread('img.jpeg')

# call imshow() using plt object
plt.imshow(img[:, :, : : -1])

# display that image
plt.show()


# In[4]:


# storing the result
result = DeepFace.analyze(img,actions = ['emotion'])
# print result
print(result)


# In[6]:


# import the required modules
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

# read image
img = cv2.imread('img.jpeg')

# call imshow() using plt object
plt.imshow(img[:,:,::-1])

# display that image
plt.show()

# storing the result
result = DeepFace.analyze(img,actions=['emotion'])

# print result
print(result)


# In[ ]:




