import predict
import cv2
import os
import shutil
import pygame as pg

pg.init()
yellow = (255, 255, 0)

screen = pg.display.set_mode((640, 280))
pg.display.set_caption("webcam sign language tester")
# pick a font you have and set its size
myfont = pg.font.SysFont("Comic Sans MS", 30)

i=0
answer = ""
camera = cv2.VideoCapture(0)
try:
    os.mkdir('.snaps')
except:
    pass   
try: 
    while True:
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
        return_value, image = camera.read()
        cv2.imshow("cam",image)
        cv2.waitKey(1)
        i = i+1
        if(i%30 == 0):
            cv2.imwrite('./.snaps/opencv'+str(i)+'.jpg', image)   
            try:
                prediction = predict.predict('./.snaps/opencv'+str(i)+'.jpg')
            except:
                pass
            answer = answer + prediction
            label = myfont.render(answer, 1, yellow)
            screen.blit(label, (100, 100))
            # show the whole thing
            pg.display.flip()
            os.remove('.snaps/opencv'+str(i)+'.jpg')
except KeyboardInterrupt:
    pass
try:        
    shutil.rmtree('.snaps')
except:
    pass
cv2.destroyAllWindows()
del(camera)
pg.quit()