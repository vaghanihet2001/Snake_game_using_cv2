from classes.prey import Prey
from classes.snake import Snake
import numpy as np
import cv2

class GameManager():
    
    def __init__(self,width,height,border = 5) -> None:
        self.border = border
        self.width = width
        self.height = height
        self.time = 0
        self.ground = np.zeros((self.height,self.width,3))
        self.score = 0
        self.move = 1
        self.speed = 100
        
    def draw_boder(self):
        # upper border
        self.ground[:self.border,:,:] = np.ones((self.border,self.width,3))*255
        # left border
        self.ground[:,:self.border,:] = np.ones((self.height,self.border,3))*255
        # bottom border
        self.ground[-(self.border):,:,:] = np.ones((self.border,self.width,3))*255
        # right border
        self.ground[:,-(self.border):,:] = np.ones((self.height,self.border,3))*255
        
    def start(self):
    
        snake = Snake(self.width,self.height,self.border)
        prey = Prey(self.width, self.height,self.border)
        image = snake.spown(self.ground)
        image = prey.spown(self.ground)
       
        while True:
            image = self.ground.copy()
            image = cv2.putText(image,"Time : "+str(self.time),(50,50),1,1,(255,255,255))
            image = cv2.putText(image,"Score : "+str(self.score),(50,100),1,1,(255,255,255))
            self.time+=1
            if snake.pos == prey.pos:
                snake.length += 1
                image = prey.spown(image)
                self.point_score()
            else:
                image = prey.update(image)
            # print(snake.pos ,prey.pos)
            image , status  = snake.update(image,self.move)
            cv2.imshow("Snake Game",image)
            if not status:
                break
            key = cv2.waitKeyEx(self.speed)
            if key == ord('a') or key == 2424832:
                self.move = 1
            elif key == ord('w') or key == 2490368:
                self.move = 2
            elif key == ord('d') or key == 2555904: 
                self.move = 3
            elif key == ord('s') or key == 2621440: 
                self.move = 4
            elif key == 27: # Esc
                break
        if not status:
            text = "Game Over"
        else:
            text = "Quiting Game?"
        fontScale = 2
        fontFace = cv2.FONT_HERSHEY_PLAIN

        ((fw,fh), baseline) = cv2.getTextSize(text, fontFace=fontFace, fontScale=fontScale, thickness=1) # empty string is good enough
        # factor = (fh-1) / fontScale
        w,h = image.shape[1],image.shape[0]
        org = ((w-fw)//2, (h+fh)//2)
        image = cv2.putText(image,text,org,fontFace,fontScale,(255,255,255),1)
        cv2.imshow("Snake Game",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
                
            
        
    def point_score(self):
        self.score += 1
        self.speed -= 5 # less speed value == more speed
        