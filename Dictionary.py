#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading


# In[54]:


class SignLanguageDictionary():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sign Language Dictionary")
        
        self.root.geometry("800x600+420+60")
        # Create the main frame
        main_frame = tk.Frame(self.root, bg="#FBF0C8")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Create a canvas to hold the video rows
        canvas = tk.Canvas(main_frame, bg="#FBF0C8")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold the video rows
        video_frame = tk.Frame(canvas, bg="#FBF0C8")
        canvas.create_window((0, 0), window=video_frame, anchor="nw")

        # Define the list of videos and letter names
        videos = [
            "Handtalk Letters MP4/A.mp4", "Handtalk Letters MP4/B.mp4", "Handtalk Letters MP4/C.mp4",
            "Handtalk Letters MP4/D.mp4", "Handtalk Letters MP4/E.mp4", "Handtalk Letters MP4/F.mp4",
            "Handtalk Letters MP4/G.mp4", "Handtalk Letters MP4/H.mp4", "Handtalk Letters MP4/I.mp4",
            "Handtalk Letters MP4/J.mp4", "Handtalk Letters MP4/K.mp4", "Handtalk Letters MP4/L.mp4",
            "Handtalk Letters MP4/M.mp4", "Handtalk Letters MP4/N.mp4", "Handtalk Letters MP4/O.mp4", 
            "Handtalk Letters MP4/P.mp4", "Handtalk Letters MP4/Q.mp4", "Handtalk Letters MP4/R.mp4",
            "Handtalk Letters MP4/S.mp4", "Handtalk Letters MP4/T.mp4", "Handtalk Letters MP4/U.mp4",
            "Handtalk Letters MP4/V.mp4", "Handtalk Letters MP4/W.mp4", "Handtalk Letters MP4/X.mp4",
            "Handtalk Letters MP4/Y.mp4", "Handtalk Letters MP4/Z.mp4"
        ]
        letter_names = [
            "A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X",
            "Y", "Z"
        ]

        # Create video rows
        for i in range(0, len(videos), 3):
            video_row_frame = tk.Frame(video_frame, bg="#FBF0C8")
            video_row_frame.pack(side=tk.TOP, padx=10, pady=10)

            # Iterate over videos in the row
            for j in range(i, i + 3):
                if j >= len(videos):
                    break

                video_path = videos[j]
                letter_name = letter_names[j]

                # Create a video player frame
                video_player_frame = tk.Frame(video_row_frame)
                video_player_frame.pack(side=tk.LEFT, padx=10)

                # Create a label for video thumbnail
                video_label = tk.Label(video_player_frame, bg="white")
                video_label.pack()

                # Load video using OpenCV
                cap = cv2.VideoCapture(video_path)

                # Read the first frame
                ret, frame = cap.read()

                # Convert frame from BGR to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize frame
                frame_resized = cv2.resize(frame_rgb, (200, 200))

                # Convert frame to ImageTk format
                img = Image.fromarray(frame_resized)
                img_tk = ImageTk.PhotoImage(image=img)

                # Set the image to the video label
                video_label.img_tk = img_tk  # Store reference to the image
                video_label.configure(image=img_tk)

                # Create a label for letter name
                letter_label = tk.Label(video_player_frame, text=letter_name)
                letter_label.pack()
                # Create a play button
                play_button = tk.Button(video_player_frame, text="Play", command=lambda path=video_path, label=video_label: self.play_video(path, label))
                play_button.pack()



                # Release OpenCV video capture
                cap.release()

    def play_video(self, video_path, video_label):
        def play():
            cap = cv2.VideoCapture(video_path)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_resized = cv2.resize(frame_rgb, (200, 200))
                img = Image.fromarray(frame_resized)
                img_tk = ImageTk.PhotoImage(image=img)
                video_label.config(image=img_tk)
                video_label.img_tk = img_tk  # Update the image reference
                video_label.update_idletasks()
            cap.release()

        # Start a new thread to play the video
        threading.Thread(target=play).start()









