import cv2
import matplotlib.pyplot as plt
import numpy as np


input_image_file=cv2.imread('./test.jpeg')
input_image_file.shape

def expand2darray(arr):
    rowadded=[]
    for row in range(1,arr.shape[0]):
        temp=(arr[row-1]+arr[row])/2
        rowadded.append(arr[row-1].tolist())
        rowadded.append(temp.tolist())
    
    rowadded.append(arr[arr.shape[0]-1].tolist())
    rowadded=np.array(rowadded)
    arr=rowadded
    columnadded=[]
    for column in range(1,arr.shape[1]):
        
        temp=(arr[:,column-1]+arr[:,column])/2
        columnadded.append(arr[:,column-1].tolist())
        columnadded.append(temp.tolist())
    
    columnadded.append(arr[:,arr.shape[1]-1].tolist())
    columnadded=np.array(columnadded)
    columnadded=columnadded.transpose()
    return columnadded
    
r,g,b=cv2.split(input_image_file)
r,g,b=r/255,g/255,b/255
r_new=expand2darray(r)
g_new=expand2darray(g)
b_new=expand2darray(b)
r_new,g_new,b_new=r_new*255,g_new*255,b_new*255
new_img=(cv2.merge((r_new,g_new,b_new)))
cv2.imwrite("hd_output.jpeg",new_img)