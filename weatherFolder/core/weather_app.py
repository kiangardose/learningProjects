# weather_app.py

import tkinter as tk
from tkinter import PhotoImage, Label, Button
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def main():
    root = tk.Tk()
    root.title("My Weather App")
    root.configure(bg="white")
    root.geometry("900x500+300+200")
    root.resizable(False, False)

    def getWeather():
        try:
            city = textfield.get()

            geolocator = Nominatim(user_agent="weather_app_by_kian")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=236ff8f9ec85b41a383ca1e12532442d"
            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            t.config(text=f"{temp}°")
            c.config(text=f"{condition} | FEELS LIKE {temp}°")
            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)
        except Exception:
            messagebox.showerror("Weather App", "Invalid Entry!")

    # UI Layout
    Search_image = PhotoImage(file="search.png")
    myimage = Label(image=Search_image)
    myimage.place(x=20, y=20)

    textfield = tk.Entry(root, justify="center", width=17, font=("Poppins", 25, "bold"),
                         bg="#404040", border=0, fg="white")
    textfield.place(x=50, y=40)
    textfield.focus()

    Search_icon = PhotoImage(file="search_icon.png")
    myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
    myimage_icon.place(x=400, y=34)

    Logo_image = PhotoImage(file="logo.png")
    logo = Label(image=Logo_image)
    logo.place(x=150, y=100)

    Frame_image = PhotoImage(file="box.png")
    frame_image = Label(image=Frame_image)
    frame_image.pack(padx=5, pady=5, side=tk.BOTTOM)

    name = Label(root, font=("Arial", 15, 'bold'))
    name.place(x=30, y=100)
    clock = Label(root, font=("Helvetica", 20))
    clock.place(x=30, y=130)

    # Weather Info Labels
    Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=120, y=400)
    Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=250, y=400)
    Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=430, y=400)
    Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=650, y=400)

    t = Label(root, font=("Arial", 70, 'bold'), fg="#ee666d", bg="white")
    t.place(x=400, y=150)
    c = Label(root, font=("Arial", 15, 'bold'), bg="white", fg="black")
    c.place(x=400, y=250)

    w = tk.Label(root, text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
    w.place(x=120, y=430)

    h = tk.Label(root, text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
    h.place(x=280, y=430)

    d = tk.Label(root, text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
    d.place(x=450, y=430)

    p = tk.Label(root, text="...", font=("Arial", 20, 'bold'), bg="#1ab5ef")
    p.place(x=670, y=430)

    root.mainloop()

if __name__ == "__main__":
    main()
