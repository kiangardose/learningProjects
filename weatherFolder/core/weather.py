import tkinter as tk
from tkinter import PhotoImage, Label, Button
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("My Weather App")
root.configure(bg="white")
root.geometry("900x500+300+200")
root.resizable(False, False)

Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("Poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040")
myimage_icon.place(x=400, y=34)

Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

Frame_image = PhotoImage(file="box.png")
frame_image = Label(image=Frame_image)
frame_image.pack(padx=5, pady=5, side=BOTTOM)

label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("Arial", 70, 'bold'), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("Arial", 15, 'bold'))
c.place(x=400, y=500)

w = Label(text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
