import numpy as np
import cv2

class Prey():
    def __init__(self,width,height,unit) -> None:
        self.unit = unit
        self.min_x_cord = unit
        self.min_y_cord = unit
        self.max_x_cord = width - (unit*2)
        self.max_y_cord = height - (unit*2)
        self.pos = None
        self.current_pos = None
        
    def spown(self,image):
        x = np.random.randint(self.min_x_cord,self.max_x_cord)
        y = np.random.randint(self.min_y_cord,self.max_y_cord)
        image = cv2.circle(image.copy(),(x,y),self.unit//2,(0,0,255),self.unit//2)
        self.pos = [x//self.unit,y//self.unit]
        self.current_pos = [x,y]
        self.is_alive = True
        return image  
    
    def update(self,image):
        x , y = self.current_pos
        image = cv2.circle(image,(x,y),self.unit//2,(0,0,255),self.unit//2)
        return image  