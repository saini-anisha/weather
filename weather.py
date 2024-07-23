from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercise")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    #api
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=695caa864fe5e98cd1faf421d1ac70b7"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))



        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("weather app","Invalid Entry!!")
Search_image=PhotoImage(file="Copy of search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)
textfield=tk.Entry(root,justify="center",width=17,font=("bold",20,"italic"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
Search_icon=PhotoImage(file="Copy of search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)
#logo
logo_image=PhotoImage(file="Copy of logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)
#bottom box
frame_image=PhotoImage(file="Copy of box.png")
frame=Label(image=frame_image)
frame.pack(padx=5,pady=5,side=BOTTOM)
#time
name=Label(root,font=("arial",15,'bold'))
name.place(x=30,y=100)
clock=Label(root,font=("helvetica",15))
clock.place(x=30,y=130)



            
label1=Label(root,text="Wind",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)
label2=Label(root,text="Humidity",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)
label3=Label(root,text="Description",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)
label4=Label(root,text="Pressure",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)


t=Label(font=("arial",15,'bold'),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)
w=Label(text="...",font=("arial",15,'bold'),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="..",font=("arial",15,'bold'),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",15,'bold'),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",15,'bold'),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()
