from tkinter import *
from tkinter import filedialog
import pytube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="blue")

#main functions
def vdownload(): #video download
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first() 
        video.download(Folder_Name)
        notif.config(fg ="green",text="Download complete! :)")
    except Exception as e:
        print(e)
        notif.config(fg ="red",text="The URL could not be downloaded :(")

def adownload(): #audio download
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.filter(only_audio=True).first()
        video.download(Folder_Name)
        notif.config(fg ="green",text="Download complete! :)")
    except Exception as e:
        print(e)
        notif.config(fg ="red",text="The URL could not be downloaded :(")

#main screen 
master = Tk()
master.title("YouTubeMP4")
master.iconbitmap("C:/Users/Will Zheng/Documents/GitHub/EE551Final/exe/mp4icon.ico")
master.geometry("325x305") #set window
master.columnconfigure(0,weight=1) #set all content in center.

#header and entry  
Label(master, text="YouTube MP4 Converter", fg="red", font=("Calibri", 15,"bold")).grid(pady=1)
Label(master,text="Please enter the URL link below: ",font=("Calibri",12)).grid(pady=1)

#entry and vars
url = StringVar()
ytdEntry = Entry(master, width=50,textvariable=url)
ytdEntry.grid(pady=1)

#Asking save file label
saveLabel = Label(master,text="Save the MP4 File",font=("Calibri",13,"bold"))
saveLabel.grid(pady=1)

#btn of save file
saveEntry = Button(master,width=12,bg="red",fg="white",text="Choose Path",font=("Calibri",12),command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(master,fg="red",font=("Calibri",11,"bold"))
locationError.grid()

#button
videodownload = Button(master,width=16,text="Video Download",fg="red", font=("Calibri",12),command=vdownload)
videodownload.grid(pady=5)
audiodownload = Button(master,width=16,text="Audio Download",fg="red", font=("Calibri",12),command=adownload)
audiodownload.grid()

#message
notif = Label(master, font=("Calibri",12,"bold"))
notif.grid()

#developer Label
developerlabel = Label(master,text="[ William Zheng ]",font=("Calibri",11,"bold"))
developerlabel.grid()

#runner
master.mainloop()