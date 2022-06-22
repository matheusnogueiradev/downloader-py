from tkinter import *
#from pytube  import YouTube
import youtube_dl
import os  
from tkinter import filedialog

class Downloader:

    def __init__(self):

        self.window = Tk()
        self.window.title('Youtube Downloader')
        self.window.resizable(0, 0)
        self.window.geometry('1280x720+300+200')

        self.img_logo  = PhotoImage(file='youtube.png')
        self.img_audio = PhotoImage(file='audio.png')
        self.img_video = PhotoImage(file='video.png')
        self.img_audio_video = PhotoImage(file='audio-video.png')
        
        self.audio = False
        self.video = False
        
        self.frame = Frame(self.window, bg='#3b3b3b', pady=30)
        self.frame.pack(fill='x')

        self.label_logo = Label(self.frame, image=self.img_logo, bg='#3b3b3b')
        self.label_logo.pack()

        self.frame2 = Frame(self.window, pady=10)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text='  Insert link: ', font='arial 12 bold')
        self.label_insert.pack(side='left')

        self.link = Entry(self.frame2,font='arial 20', width=50)
        self.link.pack(side='left')

        self.play = Button(self.frame2, bg='red', text='  >  ', bd=0, fg='white',
                           width=4, heigh=2, command=lambda: self.download(self.link.get())).pack()
        self.ab = lambda: self.download(self.link.get())
        print(self.ab)

        self.frame3 = Frame(self.window)
        self.frame3.pack()
        
        self.radio1 = Radiobutton(self.frame3, image=self.img_audio, value=0, command=self.Audio).pack(side='left')
        self.radio2 = Radiobutton(self.frame3, image=self.img_video, value=1, command=self.Video).pack(side='left')
        self.radio3 = Radiobutton(self.frame3, image=self.img_audio_video, value=2, command=self.All).pack(side='left')

      
        self.window.mainloop()

    def Audio(self):
        self.audio = True
        self.video = False
      
    def Video(self):
        self.audio = False
        self.video = True
    

    def All(self):
        self.audio = False
        self.video = False
        
    def download(self, link):
#       
        os.system("youtube-dl " + str(link)) # Faz download do video.
        self.complete()
     

    def msn(self):
        window = Toplevel()
        window.title('E R R O')
        window.resizable(0,0)
        window.geometry('300x200')

        text = Label(window, text='O Link não é válido', font='arial 20 bold',pady=30)
        text.pack()

        button_exit = Button(window, text='OK', bg='lightblue',command=window.destroy)
        button_exit.pack()

        
    def complete(self):
        window = Toplevel()
        window.title('Efetuado')
        window.resizable(0,0)
        window.geometry('300x200')
 

        text = Label(window, text='Download Efetuado', payy=30)
        text.pach()

        button_exit = Button(window, text='OK', command=window.destroy)
        button_exit.pack()
          
Downloader()        
