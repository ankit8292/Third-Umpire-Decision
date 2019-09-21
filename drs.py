import tkinter
import cv2  #open source computer vision and machine learning software library which contains many algorithem to detect or recognize the faces or images.
import PIL.Image, PIL.ImageTk #for jpg image
from functools import partial #for hiding arguments in function
import threading
import time
import imutils # To resize the image in equal pixels


stream = cv2.VideoCapture("clip1.mp4")
flag = True
def play(speed):
    global flag
    print(f"Umpire clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    tream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    #Stream -  official Python client for Stream, a web service for building scalable newsfeeds and activity streams
   
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="red", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "ot.jpg"
    else:
        decisionImg = "not_out1.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)






def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
    

# Width and height of our main screen
SET_WIDTH= 650
SET_HEIGHT= 400




# Tkinter gui starts here
window= tkinter.Tk()
window.title("Third Umpire Decision")
cv_img = cv2.cvtColor(cv2.imread("wc1.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor=tkinter.NW, image=photo)
canvas.pack()


# Buttons to control playback
btn= tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn= tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -1.5))
btn.pack()

btn= tkinter.Button(window, text=" Next (slow) >>", width=50,command=partial(play, 1.6))
btn.pack()

btn= tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn= tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn= tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()

#The Pack geometry manager packs widgets in rows or columns.

window.mainloop() #root GUI
