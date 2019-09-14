# This script reads a GPS track in CSV format and
#  writes geometries from the list of coordinate pairs
#  Handles multiple polylines
 
# Function to add a polyline
def addPolyline(cursor, array, sr):
    polyline = arcpy.Polyline(array, sr)
    cursor.insertRow((polyline,))
    array.removeAll()
 
# Main script body
import csv
import arcpy
 
# Set up input and output variables for the script
gpsTrack = open("C:\\data\\Geog485\\gps_track_multiple.txt", "r")
polylineFC = "C:\\data\\Geog485\\tracklines_sept25.shp"
spatialRef = arcpy.Describe(polylineFC).spatialReference
 
# Set up CSV reader and process the header
csvReader = csv.reader(gpsTrack)
header = csvReader.next()
latIndex = header.index("lat")
lonIndex = header.index("long")
newIndex = header.index("new_seg")
 
# Write the array to the feature class as a polyline feature
with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
 
    # Create an empty array object
    vertexArray = arcpy.Array()
 
    # Loop through the lines in the file and get each coordinate
    for row in csvReader:
         
        isNew = row[newIndex].upper()
 
        # If about to start a new line, add the completed line to the
        #  feature class
        if isNew == "TRUE":
            if vertexArray.count > 0:
                addPolyline(cursor, vertexArray, spatialRef)
 
        # Get the lat/lon values of the current GPS reading
        lat = row[latIndex]
        lon = row[lonIndex]
 
        # Make a point from the coordinate and add it to the array
        vertex = arcpy.Point(lon,lat)
        vertexArray.add(vertex)
 
    # Add the final polyline to the shapefile
    addPolyline(cursor, vertexArray, spatialRef)