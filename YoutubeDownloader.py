from tkinter import * 
from tkinter import filedialog, messagebox
import pathlib
from pytube import YouTube


def browse():
    download = filedialog.askdirectory()
    path.set(download)
def downloader():
    video = link.get()
    downFolder = path.get()
    
    getVideo = YouTube(video)

    videoStream = getVideo.streams.first()

    videoStream.download(downFolder)

    messagebox.showinfo("Successfully","Downloaded and saved in\n"+downFolder)
def Widgets():
    link_lab = Label(root, text="Youtube link :",bg="#E8D579",width=20)
    link_lab.grid(row=1, column=0,pady=5,padx=5)

    linkText = Entry(root,width=55,textvariable=link)
    linkText.grid(row=1, column=1,pady=5,padx=5,columnspan=2)

    saveLab = Label(root,text="Destination :",bg="#E8D579", width=20)
    saveLab.grid(row=2, column=0,pady=5,padx=5)

    saveText = Entry(root,width=55,textvariable=path)
    saveText.grid(row=2, column=1,pady=5,padx=5,columnspan=2)

    browseButton = Button(root,text="Browse",command=browse,width=10,bg="#05E8E0")
    browseButton.grid(row=2, column=2,pady=1,padx=1)

    downloadButton = Button(root,text="Download", command=downloader,width =20,bg="#05E8E0")
    downloadButton.grid(row=3, column=1,pady=3,padx=3)


root = Tk()
root.geometry("500x110")
root.resizable(0,0)
root.title("Youtube Downloader v2")
root.config(background="#000000")

link = StringVar()
path = StringVar()

Widgets()
root.mainloop()
