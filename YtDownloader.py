from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import os
import yt_dlp

def browseFiles():
    global directorio
    directorio = filedialog.askdirectory()

def downloadmp3():
    try:
        url = txt1.get()
        output_path = os.path.join(directorio, '%(title)s.%(ext)s')
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f'Error occurred while downloading MP3: {str(e)}')

def downloadmp4():
    try:
        url = txt1.get()
        output_path = os.path.join(directorio, '%(title)s.%(ext)s')
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': output_path,
            'merge_output_format': 'mp4',
            'prefer_ffmpeg': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f'Error occurred while downloading MP4: {str(e)}')

window = Tk()
window.title("YouTube Downloader")

directorio = os.path.expanduser("~/Desktop")

lbl = Label(window, text="YouTube Downloader")
lbl.grid(column=0, row=0)

btnmp3 = Button(window, text="Download MP3", command=downloadmp3)
btnmp3.grid(column=2, row=0)

btnmp4 = Button(window, text="Download MP4", command=downloadmp4)
btnmp4.grid(column=2, row=1)

txt1 = Entry(window, width=40)
txt1.grid(column=0, row=2)

btn = Button(window, text="Select Download Directory", command=browseFiles)
btn.grid(column=2, row=2)

window.mainloop()

# notes
# pyinstaller --onefile -w -F --icon="icon.ico" --add-binary "icon.ico;." "YtDownloader.py"
# pyinstaller --onefile -w -F "YtDownloader.py"