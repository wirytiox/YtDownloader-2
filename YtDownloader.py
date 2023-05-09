from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter import filedialog
import os
import youtube_dl
from asyncio.log import logger
import logging
def debugMode():
    CheckboxNotCriying=checkbox_var.get()
    
    if CheckboxNotCriying==True:
        logging.basicConfig(filename='test.log',level=logging.DEBUG)
        logging.debug('debugging is enabled')
    else:
        print('debugger is not enabled and you cant see this')
        print(CheckboxNotCriying)
directorio=desktop = os.path.expanduser("~/Desktop")
def browseFiles():
    global directorio
    directorio = filedialog.askdirectory()
def downloadmp3():
    try:
        url = txt1.get()
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': directorio+"\\"+'%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'extractaudio': True,
            'audioformat': 'mp3',
            'noplaylist': True,
            'nocheckcertificate': True,
            'quiet': False,
            'no_warnings': False,
            'default_search': 'auto'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except :
        logger.exception('you fucked up')
def downloadmp4():
    try:
        url = txt1.get()
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': directorio+"\\"+'%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'prefer_ffmpeg': True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        logger.exception('Error occurred while downloading video.')
window = Tk()                                                           #ClassDefinition
window.title("Yotube Downloader")                                       #Titulo
#window.iconbitmap("icon.ico")                                          #icon broken i dont know how to make it work
checkbox_var = IntVar()                                                 #int var, odio esto
checkbox = ttk.Checkbutton(window,
                text='Debug Mode',
                command=debugMode,
                variable=checkbox_var,
                onvalue=True,
                offvalue=False).grid(column=0, row=3)
lbl = Label (window, text="Youtube Downloader")                         #Label Decorativa
lbl.grid(column=0, row=0)                                               #Label Decorativa
btnmp3 = Button (window, text="Descargar Mp3",command=downloadmp3)     #Descargarmp3   boton
btnmp3.grid(column=2, row=0)                                            #Descargarmp3   boton
btnmp4 = Button(window, text="Descargar Mp4", command=downloadmp4)     #descargarMP4   boton
btnmp4.grid(column=2, row=1)                                            #descargarMP4   boton
txt1 = Entry(window,width=40)                                           #link
txt1.grid(column=0, row=2)                                              #link
txt1.get()                                                              #link
btn = Button(window, text="Donde descargar", command=browseFiles)       #FileExplorer boton
btn.grid(column=2, row=2)                                               #FileExplorer boton
window.mainloop()
# notes
# pyinstaller --onefile -w -F --icon="icon.ico" --add-binary "icon.ico;." "SimplePyDownloader.py"
# pyinstaller --onefile -w -F "SimplePyDownloader.py"