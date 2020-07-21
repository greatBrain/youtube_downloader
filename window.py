import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from downloader import Downloader
from threading import Thread

class Main_Window:
      def __init__(self):
          self.window = tk.Tk()
          self.path = ''

          #Store the tkinter Text Box object, that recibes the video url
          self.url_obj = StringVar() 

      def set_main_window(self):          
          self.window.configure(background='black')
          self.window.title('Youtube Simple Downloader')
          #self.icon = PhotoImage(file='src/you.ico')
          #self.window.tk.call('wm', 'iconphoto', self.window._w, self.icon)
          self.window.geometry("510x300")
          self.window.resizable(False,False) 

          url_label = tk.Label(self.window,text="Enter here the video URL:")
          url_label.configure(background='black', fg="white")
          url_label.config(font=("mini_pixel-7", 12))
          url_label.place(x=10, y=65)          

          self.set_url_box() 
          self.set_download_button()          

          return self.window

      def set_url_box(self):

          url_box = tk.Text(self.window, 
              height=1.4, 
              width=60, bd=1,              
              background = 'black',
              highlightbackground = 'red',
              highlightcolor = 'green'
          )
          url_box.config(font=("sans", 10), fg="yellow")    
          url_box.place(x=10, y=100)        
          self.url_obj = url_box

      def get_url(self):
          url = str(self.url_obj.get(1.0, tk.END+"-1c"))
          return url     
      
      def save_file(self):
          self.path = filedialog.askdirectory()          
          return self.path

      def set_download_button(self):
          button = tk.Button(self.window, text="Download", font=("caladea", 13), background="red", command=self.download)
          button.configure(fg="white", activebackground = "green", relief = FLAT)          
          button.place(x=189, y=175)          
          return button
     
      def download(self):        
          Downloader(self.save_file(), self.get_url()).download()

      def set_pogress_bar(self):          
          self.bar = ttk.Progressbar(self.window)
          self.bar.place(x=10, y=275, width=250)
          self.bar.place(width=487, height=20)

          return self.bar             

      def start_loop(self):
          self.set_main_window().mainloop()