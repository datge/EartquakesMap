import urllib.request
import csv
import io
import math
import cv2

def get_csv(url_usgs):
        response = urllib.request.urlopen(url_usgs)
        csvfile = csv.reader(io.StringIO(response.read().decode('utf-8')), delimiter=',')
        next(csvfile, None)
        return csvfile

#web marcator , convert latitute longituted in x,y axis       
class Converti:
    def __init__(self,lon,lat,zoom):
        self.lon = lon
        self.lat =  lat
        self.zoom = zoom

    def mercX(self):
        self.lon =  math.radians(self.lon)
        a = (256/math.pi)*math.pow(2,self.zoom)
        b = self.lon + math.pi
        return a * b

    def mercY(self):
        self.lat =  math.radians(self.lat)
        a = (256/math.pi)*math.pow(2,self.zoom)
        b = math.tan(math.pi/4 + self.lat/2)
        c = (math.pi)-(math.log(b))
        return a * c
#draw circle on the mapp but convert the value that we get in float to int
def disegna(x,y,mag,img):
    cv2.circle(img,(int(x),int(y)),int(mag),(0,0,255),-1)
#open the api and write the content of the png file in a file that we will call map_raw.png
def download(api):
    url_image = api
    image = urllib.request.urlopen(url_image).read()
    with open('map_raw.png', 'wb') as output:
        _ = output.write(image)
