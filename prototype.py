from tkinter import *
import pytube

#functions
def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        #video = youtube.streams.first() 
        video = youtube.streams.filter(only_audio=True).first()
        video.download("C:/Users/Will Zheng/Desktop/MyMusic")
        notif.config(fg ="green",text="Download complete! :)")
    except Exception as e:
        print(e)
        notif.config(fg ="red",text="Video URL could not be downloaded :(")

#main screen 
master = Tk()
master.title("YouTube Video Downloader")

#label 
Label(master, text="Youtube Video Converter", fg="red", font=("Calibri", 15)).grid(sticky=N,padx=100,row=0)
Label(master,text="Please enter the URL link to your video below: ", font=("Calibri",12)).grid(sticky=N,pady=15,row=1)
notif = Label(master, font=("Calibri",12))
notif.grid(sticky=N,pady=1,row=4)

#vars
url = StringVar()

#entry
Entry(master, width=50,textvariable=url).grid(sticky=N,row=2)

#button
Button(master,width=20,text="MP4 Download", font=("Calibri",12),command=download).grid(sticky=N,pady=15,row=3)

master.mainloop()