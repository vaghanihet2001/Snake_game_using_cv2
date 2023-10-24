from classes.prey import Prey
from classes.snake import Snake
import numpy as np
import cv2

class GameManager():
    
    def __init__(self,width,height,border = 5) -> None:
        self.border = border
        self.width = width
        self.height = height
        self.ground = np.zeros((self.height,self.width,3))
        self.move = 1
        self.speed = 10
        
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
            if snake.pos == prey.pos:
                snake.length += 1
                image = prey.spown(image)
            else:
                image = prey.update(image)
            print(snake.pos ,prey.pos)
            image = snake.update(image,self.move)
            cv2.imshow("Snake Game",image)
            if cv2.waitKey() == ord('a'):
                self.move = 1
            elif cv2.waitKey() == ord('w'):
                self.move = 2
            elif cv2.waitKey() == ord('d'): 
                self.move = 3
            elif cv2.waitKey() == ord('s'): 
                self.move = 4
            elif cv2.waitKey() == ord("q"):
                break
        image = cv2.putText(image,"Quiting Game?",(image.shape[0]//2-(self.border*13),image.shape[1]//2-(self.border*13)),1,2,(255,255,255),2)
        cv2.imshow("Snake Game",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
                
            
        
        