# This script reads a GPS track in CSV format and
#  writes geometries from the list of coordinate pairs
import csv
import arcpy
 
# Set up input and output variables for the script
gpsTrack = open("C:\\data\\Geog485\\gps_track.txt", "r")
polylineFC = "C:\\data\\Geog485\\tracklines.shp"
spatialRef = arcpy.Describe(polylineFC).spatialReference
 
# Set up CSV reader and process the header
csvReader = csv.reader(gpsTrack)
header = csvReader.next()
latIndex = header.index("lat")
lonIndex = header.index("long")
 
# Create an empty array object
vertexArray = arcpy.Array()
 
# Loop through the lines in the file and get each coordinate
for row in csvReader:
    lat = row[latIndex]
    lon = row[lonIndex]
 
    # Make a point from the coordinate and add it to the array
    vertex = arcpy.Point(lon,lat)
    vertexArray.add(vertex)
 
# Write the array to the feature class as a polyline feature
with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
    polyline = arcpy.Polyline(vertexArray, spatialRef)
    cursor.insertRow((polyline,))   