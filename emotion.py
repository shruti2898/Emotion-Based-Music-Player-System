import cv2
import speech_recognition as sr
import os
import random
import vlc
import pyttsx3
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
er=load_model(r'C:\Users\your user name\Desktop\EmoPlayer\_mini_XCEPTION.106-0.65.xml')
fd=cv2.CascadeClassifier(r'C:\Users\your user name\Desktop\EmoPlayer\haarcascade_frontalface_default.xml')
em=['angry','disgust','scared','happy','sad','surprise','neutral']
v=cv2.VideoCapture(0)
files1 =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\happy')
index1 = random.randrange(0, len(files1))
a=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\happy'+'\\'+files1[index1])
files2 =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\angry')
index2 = random.randrange(0, len(files2))
b=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\angry'+'\\'+files2[index2])
files3 =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\sad')
index3 = random.randrange(0, len(files3))
c=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\sad'+'\\'+files3[index3])
files =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\neutral')
index = random.randrange(0, len(files))
d=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\neutral'+'\\'+files[index])
def txt_to_speech(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
print("=====================================================================WELCOME===========================================================================================")
txt_to_speech("Welcome, welcome and welcome. This is about listening to various songs according to your mood. Enjoy")
print("Press c to Capture: ")
txt_to_speech("Please press c to capture the image.........")
txt_to_speech("Ready to capture the image..")
while(1):
    r,i=v.read()
    cv2.imshow('image',i)
    k=cv2.waitKey(5)
    if(k==ord('c')):
        j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        f=fd.detectMultiScale(j,1.3,5)
        a.stop()
        b.stop()
        c.stop()
        d.stop()
    
        if(len(f)==1):
            for(x,y,w,h) in f:
                g=j[y:y+h,x:x+w]
                g=cv2.resize(g,(48,48))
                g=g.astype('float')/255.0
                g=img_to_array(g)
                g=np.expand_dims(g,axis=0)
                p=er.predict(g)[0]
    
                ind=np.argmax(p)
                print("Your Facial Expression is: ",em[ind])
                if(em[ind]=="happy"):
                    files1 =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\happy')
                    index1 = random.randrange(0, len(files1))
                    a=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\happy'+'\\'+files1[index1])
                    print("Playing song for you: ", files1[index1])
                    print("If you want to stop press n Key.....")
                    txt_to_speech("Press n if you want to stop the song")
                    a.play()
                    
                    
                if(em[ind]=='angry'):
                    files2 =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\angry')
                    index2 = random.randrange(0, len(files2))
                    b=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\angry'+'\\'+files2[index2])
                    print("Playing song for you: ", files2[index2])
                    print("If you want to stop press n Key.....")
                    txt_to_speech("Press n if you want to stop the song")
                    b.play()
                    
                if(em[ind]=="sad"):
                    files3 =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\sad')
                    index3 = random.randrange(0, len(files3))
                    c=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\sad'+'\\'+files3[index3])
                    print("Playing song for you: ", files3[index3])
                    print("If you want to stop press n Key.....")
                    txt_to_speech("Press n if you want to stop the song")
                    c.play()
                   
                if(em[ind]=="neutral"):
                    files =os.listdir(r'C:\Users\your user name\Desktop\EmoPlayer\neutral')
                    index = random.randrange(0, len(files))
                    d=vlc.MediaPlayer(r'C:\Users\your user name\Desktop\EmoPlayer\neutral'+'\\'+files[index])
                    print("Playing song for you: ", files[index])
                    print("If you want to stop press n Key.....")
                    txt_to_speech("Press n if you want to stop the song")
                    d.play()
                   
                
    if(k==ord('q')):
        a.stop()
        b.stop()
        c.stop()
        d.stop()
        cv2.destroyAllWindows()
        print("Hope you like it.... Thank you ")
        txt_to_speech("Hope you like it. Thank You")
        break
    if(k==ord('n')):
        a.stop()
        b.stop()
        c.stop()
        d.stop()
        print("Stopped")
        txt_to_speech("Stopped the song")
        print("Press c for another song or press q to quit: ")
        txt_to_speech("Press c for another song or press q to quit")
