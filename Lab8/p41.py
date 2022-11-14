#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import folium

NYC = folium.Map(location = [40.75, -74.125], zoom_start = 10)
folium.marker(location=[40.7812, -73.9665], popup = "Central Park").addto(NYC)
NYC.save(outfile="nyc_Central_Park.html")
