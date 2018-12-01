from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', title = "Home page")

@app.route('/galeria')
def galeria():
    listaOwiec = [
    "https://www.gettyimages.ie/gi-resources/images/Homepage/Hero/UK/CMS_Creative_164657191_Kingfisher.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz_4Bmf2jZilGHQSP0Pjj6LG1DfgCp4IDdqDEroZKidZAItstA",
    "https://wallpaperbrowse.com/media/images/3848765-wallpaper-images-download.jpg",
    "https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/09/12/11/naturo-monkey-selfie.jpg?w968h681",
    "https://demo.phpgang.com/crop-images/demo_files/pool.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOtWyngXgu-4Y70Uo7JdwVPB_lQiEVC_1PnBXuqE1YtG2mwteK",
    "http://webresizer.com/images2/bird1_after.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLb5mOUtzV0ObqBVuAURSvPAsC27148aFdKGc6e6Z_Z78vmMWf",
    "https://tinypng.com/images/social/website.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2ktlwSh8RQGskNFUfNSyfHZYLe-Duiu8BgQMb3JEw9uLV7KpbmA"
    ]
    return render_template('galeria.html',listaOwiec = listaOwiec)

@app.route('/user/<name>')
def getUser(name):
    return render_template('user.html', name=name)