from tkinter import * 
import tkinter as tk
from tkinter import ttk,filedialog
import requests
import os


class Downloader:
    def __init__(self):
        self.saveto=""
        self.window=tk.Tk()
        self.window.title("NDM")
        self.window.geometry("720x480")
        self.url_label=tk.Label(text="------Enter the URL------",font=("Comic Sans MS",12),justify='center')
        self.url_label.pack()
        self.url_entry=tk.Entry(width=100,justify='center')
        self.url_entry.pack(pady=20)
        self.browse_button=tk.Button(text="Browse",command= self.browseFile,borderwidth=4,relief=tk.GROOVE)
        self.browse_button.pack(padx=10,pady=10)
        self.downloadButton=tk.Button(text="Download",command=self.Download,borderwidth=4,relief=tk.GROOVE)
        self.downloadButton.pack()
        self.progressBar=ttk.Progressbar(self.window, orient="horizontal", maximum=100,length=300, mode="determinate")
        
        self.progressBar.pack()
        self.window.mainloop()

    def browseFile(self):
        saveto=filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1].split("?")[0])
        self.saveto=saveto
    
    def Download(self):
        urls=self.url_entry.get()
        response=requests.get(urls,stream=True)
        total_size_in_byte=1000
        if(response.headers.get("content-length")):
            total_size_in_byte=int(response.headers.get("content-length"))
        blockSize=10000
        self.progressBar["value"]=0
        filename=self.url_entry.get().split("/")[-1].split("?")[0]
        if(self.saveto==""):
            self.saveto=filename
        print(self.saveto)
        with open (self.saveto,"wb") as f:
            for data in response.iter_content(blockSize):
                self.progressBar["value"]+=(100*blockSize)/total_size_in_byte
                #print(self.progressBar["value"])
                f.write(data)

Downloader()
