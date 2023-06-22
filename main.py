import cv2
import cvzone

Frame=['Filters/star.png','Filters/sunglass.png','Filters/exp2.png','Filters/exp4.png','Filters/exp7.png','Filters/exp0.png']

def face_detection():
    global final_image,x
    try:
        while 1:
            x=int(input("enter frame number: ")) - 1
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            video=cv2.VideoCapture(0)
        
            #spectacle frame
            spectacle_frame=cv2.imread(Frame[x],cv2.IMREAD_UNCHANGED)

            while True:
                a,video_capture=video.read() 
                gray_img = cv2.cvtColor(video_capture, cv2.COLOR_BGR2GRAY)
                faces=face_cascade.detectMultiScale(gray_img)

                #for rectangle frame around the faces
                for (x,y,w,h) in faces:
                    #cv2.rectangle(video_capture,(x,y),(x+w,y+h),(0,0,0))
                    spectacle_frame_resize=cv2.resize(spectacle_frame,(w,h))
                    final_image=cvzone.overlayPNG(video_capture,spectacle_frame_resize,[x,y])
        
                #displaying the video
                cv2.imshow("FRAME_TEST",final_image)

                #for holding the screen
                k = cv2.waitKey(10)
            
                #for exiting the screen
                if k==ord('e'):
                    break

                if k==ord('x'):
                    exit()
        
            video.release()
            cv2.destroyAllWindows()
    
    except:
        pass

for _ in range(len(Frame)):
    print(_+1,':',Frame[_].split('/')[-1])
face_detection()
