# Define a function which checks if a rhino is in the dictionary and
# if not, creates an array as a value to the rhino name as the key while adding
# a point object to the array. If the rhino is in the dictionary, the array
# is updated with a point object with the given lat and lon arguments.

def updateDict(rhino, dictionary, lat, lon):
    if rhino not in dictionary:
        dictionary[rhino] = arcpy.Array()
        vertex = arcpy.Point(lat, lon)
        dictionary[rhino].add(vertex)
    else:
        vertex = arcpy.Point(lat, lon)
        dictionary[rhino].add(vertex)

# Import necessary modules

import arcpy
import csv
arcpy.env.overwriteOutput = True

# Attempt to open the CSV file with rhino path points

try:
    fileHandle = open(r'C:\TmpWrkDirGIS\GEOG485\Lesson4\RhinoObservations.csv', 'r')
except:
    print('Input CSV file could not be opened')

# Create neccessary variables for updating the feature class

csvReader = csv.reader(fileHandle)
header = csvReader.next()
latIndex = header.index('X')
lonIndex = header.index('Y')
rhinoIndex = header.index('Rhino')

# Create a dictionary to contain rhino arrays

rhinoDict = {}

# Attempt to create the polyline feature class and add a NAME field

try:
    spatialRef = arcpy.SpatialReference('WGS 1984')
    rhinoFC = arcpy.CreateFeatureclass_management(r'C:\TmpWrkDirGIS\GEOG485\Lesson4', 'rhinopaths.shp', 'POLYLINE', '', '', '', spatialRef)
    arcpy.AddField_management(rhinoFC, 'NAME', 'TEXT', '', '', 20)
except:
    print('Error in creating polyline feature class')

# Attempt to update the dictionary by iterating through the rows in the CSV

try:
    for row in csvReader:
        updateDict(row[rhinoIndex], rhinoDict, row[latIndex], row[lonIndex])

    # Once the dictionary is updated, insert the arrays into the polyline feature class
    # using the key for the NAME field and the value as a polyline object

    try:
        with arcpy.da.InsertCursor(rhinoFC, ('SHAPE@', 'NAME')) as cursor:
            for rhino in rhinoDict:
                polyline = arcpy.Polyline(rhinoDict[rhino], spatialRef)
                cursor.insertRow((polyline, rhino))
            del cursor
    except:
        print('Error inserting tracking points into feature class')
except:
    print('Error creating rhino point arrays')