#Simple python youtube downloader.
#Using: python subprocess, pytube

from pytube import YouTube
import subprocess
import os
from threading import Thread
import tkinter as tk
from tkinter import ttk

class Downloader:
      
      def __init__(self, path, url):
          if url != None:
             self.path = path
             self.youtube = YouTube(url)
          else:
              pass

      def get_format(self):
          video_format = self.youtube.streams.first()

      def download(self):
          try:
              stream = self.youtube.streams.first()
              stream.download(self.path)

          except Exception as e:
              print("Error trying to download.", e)
      


class Progress_Bar(ttk.Frame):

      def __init__(self, window):
          self.window = window
          super().__init__(self.window)

          self.window.title("Downloading...")
          self.bar = ttk.Progressbar(self)
          self.bar.place(x=50, y=60, width=250)

          self.place(width=350, height=200)
          self.window.geometry("350x180")

      def download_status(self, count):
          self.bar.step(count)
          '''if count == 0:
             # Establecer el máximo valor para la barra de progreso.
             self.bar.configure(maximum=total_data)
          else:
             # Aumentar el progreso.
             self.bar.step(data_size)'''


if __name__ == "__main__":
     bar_window = tk.Tk()
     progress = Progress_Bar(bar_window )
     progress.mainloop() 
