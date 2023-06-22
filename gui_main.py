from tkinter import *
import datetime
from PIL import Image,ImageTk
import cv2
import cvzone


Frame=['Filters/star.png','Filters/sunglass.png','Filters/exp2.png','Filters/exp4.png','Filters/exp7.png','Filters/exp0.png']
x=0

def prev():
    global x
    global spectacle_frame
    if x!=0:
        x-=1
    if x==0:
        x=0
    spectacle_frame = cv2.imread(Frame[x], cv2.IMREAD_UNCHANGED)

def nxt():
    global x
    global spectacle_frame
    if x!=len(Frame)-1:
        x+=1
    if x==len(Frame):
        x=len(Frame)-1
    spectacle_frame = cv2.imread(Frame[x], cv2.IMREAD_UNCHANGED)

def snapshot():
    image=Image.fromarray(final_image)
    file_name='IMG-' + str(datetime.datetime.now().today()).replace(":"," ") + ".jpg"
    image.save(file_name)



def main_function():
    global final_image
    try:
        _, frame = video.read()
        #new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(frame)
    

        #for rectangle frame around the faces
        for (x,y,w,h) in faces:
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0))
            spectacle_frame_resize=cv2.resize(spectacle_frame,(w,h))
            final_image=cvzone.overlayPNG(frame,spectacle_frame_resize,[x,y])


        frame = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)


    
        # Update the video_placeholder
        image = ImageTk.PhotoImage(image=Image.fromarray(frame))
        video_placeholder.configure(image=image)
        video_placeholder.image = image
        video_placeholder.after(1, main_function)
    
    except:
        pass



if __name__=='__main__':
    
    #screen
    screen=Tk()
    screen.geometry('700x540')
    screen.resizable(0,0)
    screen.title('Frame_Test')
    screen.configure(bg='black')
    
    #buttons
    #previous button
    prev_btn=Button(screen,text ='Previous',bg='black',fg='white',command = lambda:prev())
    prev_btn.pack(side=LEFT,padx=3,anchor=S)
    
    #next button
    nxt_btn=Button(screen,text ='Next',bg='black',fg='white',command = lambda:nxt())
    nxt_btn.pack(side=RIGHT,padx=3,anchor=S)
    
    #snapshot button
    snap_btn=Button(screen,text ='Snapshot',bg='black',fg='white',command = lambda:snapshot())
    snap_btn.pack(side=BOTTOM, expand = True,anchor=S)
    
    #video placeholder
    video=cv2.VideoCapture(0)
    
    img=video.read()[1]
    new_img=ImageTk.PhotoImage(Image.fromarray(img))

    #placing the video 
    video_placeholder=Label(screen,image=new_img)
    video_placeholder.pack()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    spectacle_frame=cv2.imread(Frame[x],cv2.IMREAD_UNCHANGED)

    #main function
    main_function()
    
    #to hold the screen for infinite time
    screen.mainloop()