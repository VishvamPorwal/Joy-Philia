from flask import Flask, render_template, request, redirect
import weather
import hello
import html
import location
import nearby

app = Flask(__name__)

cant_go_out = ["Thunderstorm", "Drizzle", "Rain", "Snow", "Fog", "Ash","Smoke", "Haze", "Dust", "Sand", "Tornado", "Squall"]
can_go_out = ["Clear", "Clouds", "Mist"]

loc = location.get_location()
greet = hello.get_greet(loc)
greet = html.unescape(greet["hello"])
Weather = weather.get_weather(loc) 
Nearby = nearby.get_nearby(loc)

@app.route("/")
def index():
    return render_template("index.html", greet = greet, weather = Weather["desc"], main = Weather["ac"], cant_go_out = cant_go_out, can_go_out = can_go_out)


@app.route("/outside")
def outside():
    return render_template("outside.html", Nearby = Nearby)


@app.route("/inside")
def inside():
    return render_template("inside.html")


@app.route("/music")
def music():
    return render_template("music.html")


@app.route("/cook")
def cook():
    return render_template("cook.html")


@app.route("/book")
def book():
    return render_template("book.html")
