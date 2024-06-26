# Python program to take 
# screenshots 
import numpy as np 
import cv2 
import pyautogui 
from datetime import datetime
  
def click_screenshot(tag):
    # take screenshot using pyautogui 
    image = pyautogui.screenshot() 
       
    # since the pyautogui takes as a  
    # PIL(pillow) and in RGB we need to  
    # convert it to numpy array and BGR  
    # so we can write it to the disk 
    image = cv2.cvtColor(np.array(image), 
                         cv2.COLOR_RGB2BGR) 
       
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    print("Current Time =", current_time)
    if tag == 'multi_face':
        folder = 'multi_face'
        cv2.imwrite(f'multi_face/{tag}{current_time}.png', image)
        cv2.imwrite(str(folder)+str(tag)+str(current_time)+".png", image)
    # writing it to the disk using opencv 
    else:
        cv2.imwrite("generated-report/"+str(tag)+str(current_time)+".png", image) 
