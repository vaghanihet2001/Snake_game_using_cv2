import cv2
import numpy as np

class Snake():
    def __init__(self,width,height,unit) -> None:
        self.length = 0
        self.body = []
        self.score = 0
        self.unit = unit
        self.min_x_cord = unit
        self.min_y_cord = unit
        self.max_x_cord = width-(unit*2)
        self.max_y_cord = height-(unit*2)
        self.pos = None
        self.is_alive = True
        self.direction = 1 # left = 1 , top = 2 , right = 3 , bottom = 4
        
        
    def spown(self,image):
        x = np.random.randint(0,self.max_x_cord)
        y = np.random.randint(0,self.max_y_cord)
        image = cv2.rectangle(image.copy(),(x,y),(x+self.unit,y+self.unit),(0,255,0),2)
        self.body.append([x,y])
        self.pos = [x,y]
        self.length += 1
        return image 
    
    def update(self,image,move):
        cp = self.body[-1]
        if move == 1 : # left
            np = [cp[0]-self.unit,cp[1]]
        elif move == 2: # top
            np = [cp[0],cp[1]-self.unit]
        elif move == 3: # right
            np = [cp[0]+self.unit,cp[1]]
        elif move == 4: # bottom
            np = [cp[0],cp[1]+self.unit]
            
        if np in self.body:
            self.is_alive = False
        
        if np[0] >= self.min_x_cord and np[1] >= self.min_y_cord and np[0] <= self.max_x_cord and np[1] <= self.max_y_cord:
            self.body.append(np)
            self.pos = [self.body[-1][0]//self.unit ,self.body[-1][1]//self.unit]
        
        if len(self.body) != self.length:
            # print("snake",len(self.body),self.body)
            self.body.pop(0) 
            
        for index, i in enumerate(self.body):
            if index == len(self.body)-1:
                color = (255,0,0)
            else:
                color = (0,255,0)
            image = cv2.rectangle(image,(i[0],i[1]),(i[0]+self.unit,i[1]+self.unit),color,2)
        
        return image ,self.is_alive
        
    