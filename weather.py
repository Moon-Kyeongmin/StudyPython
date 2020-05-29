from urllib.request import urlopen
from tkinter import *

def get_weather(city):
    page=urlopen("https://www.weather.go.kr/weather/observation/currentweather.jsp")
    text=page.read().decode("euckr")
    text=text[text.find(">"+city+"</a>"):]
    for i in range(5):
        text=text[text.find("<td>")+1:]
    start=3
    end=text.find("</td>")
    tempV.set("온도 : "+text[start:end])
    print(text[start:end])

def refresh(*args):
    get_weather(cities.get())

root=Tk()
root.title("현재온도")
root.geometry("640x400+320+60")
Label(root,text="도시 : ").pack(side="left")
city_list=["서울","부산","대구","제주"]

cities=StringVar()
cities.set(city_list[0])
cities.trace("w",refresh)
OptionMenu(root,cities,*city_list).pack(side="right")
tempV=StringVar()
tempV.set("온도 : ")
Label(root,textvariable=tempV).pack(pady=40,side="top")

Button(root,text="refresh",command=refresh).pack(pady=40,side="bottom")

root.mainloop()