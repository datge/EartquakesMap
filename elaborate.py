from eartquakes import *
import cv2
from numpy import interp



def elaborate(csv_url):
    zoom = 1

    ##call the function download in eartquakes module 
    # api='https://api.mapbox.com/styles/v1/mapbox/dark-v9/static/0,0,{}/1024x1024?access_token=pk.eyJ1IjoiZGF0Z2UiLCJhIjoiY2pwaGFzbHhxMHMybDNqbGd3bGYzZm01dyJ9.aSkY8EVTTfdmPzs3PQDzcw'.format(zoom)
    # mappa = download(api)
    ##if the map is already download we don't download it another time

    img = cv2.imread('map_raw.png',1)
    maxmag = math.sqrt(math.pow(10,10))
    csv_content = get_csv(csv_url)
    #call the function get_csv to get the csv file from usgs up to what we chose on the menù

    
    for row in csv_content:
        if row[4] != '':
            temp_mag = math.pow(10,float(row[4]))
            temp_mag =  math.sqrt(temp_mag )
            temp_mag = interp(temp_mag ,[0,maxmag],[0,60])
            #for differentiate magnitude from for example(1.2 and 1.9) we make calculation and then we map these values
            #to 0/60 like that we won't have similar circle because we can't write circle with a float number as diameter
            convertito = Converti(float(row[2]),float(row[1]),zoom)
            #convert latitude and longituted in x,y axis for draw circles on map
            disegna(convertito.mercX(),convertito.mercY(),temp_mag,img)
            #draw circle
    
    cv2.imshow('World Eartquakes Map',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #show map and wait the pressure of a kay for close all the windows elaborated by cv2


