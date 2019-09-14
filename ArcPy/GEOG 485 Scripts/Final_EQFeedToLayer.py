##                                                                       ##
##                        GEOG 485 Final Project                         ##
##                                                                       ##
##  This script downloads earthquake data from USGS feeds in KML and in  ##
##  GeoJSON format. The script converts the GeoJSON into a geodatabase   ##
##    if the user has the Data Interoperability extension. If not the    ##
##     GeoJSON is converted to a shapefile using an online converter.    ##
##    Earthquake data in KML format is converted using and arcpy tool    ##
##  which creates a file geodatabase containing a feature class within   ##
##                          a feature dataset.                           ##
##                                                                       ##
##                          Author: Tyler Fritz                          ##


# Import the necessary modules

import zipfile
import arcpy
import urllib, urllib2
import os
import datetime
arcpy.env.overwiteOutput = True

# Designate the urls of the earthquake data feeds. The KML feed contains all
# earthquakes in the last month greater than 2.5+ magnitude. The GeoJSON feed
# contains all the earthquakes in the last month greater than 4.5+ magnitude.

kmlUrl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month_age.kml'
geojsonUrl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson'

# Designate the target folder for script output. Create it if it does not already exist.

targetFolder = 'C:/EQData'

if not os.path.exists(targetFolder):
    os.makedirs(targetFolder)

# Create a string with date information to label output datasets.

date = datetime.datetime.now()
dateString = '_' + date.strftime('%b') + '_' + date.strftime('%d') + '_' + date.strftime('%Y')

# Attempt to download data over HTTP. Create new files with the open command with
# path and date information previously designated. Write the downloaded data to each
# file handle. Close the file handles after.

try:
    kmlData = urllib2.urlopen(kmlUrl).read()
    geojsonData = urllib2.urlopen(geojsonUrl).read()
    kmlPath = targetFolder + '/2.5_month' + dateString + '.kml'
    geojsonPath = targetFolder + '/4.5_month' + dateString + '.geojson'
    kmlHand = open(kmlPath, 'w')
    geojsonHand = open(geojsonPath, 'w')
    kmlHand.write(kmlData)
    geojsonHand.write(geojsonData)
    kmlHand.close()
    geojsonHand.close()

except:
    print('Error retrieving earthquake data')

# Check if the user has the Data Interoperability extension for ArcGIS

if arcpy.CheckExtension('DataInteroperability') == 'Available':

    # Try using the QuickImport tool to create the output geodatabase.

    try:
        gdbPath = targetFolder + '/4.5_month' + dateString + '.gdb'
        arcpy.CheckOutExtension('DataInteroperability')
        arcpy.QuickImport_interop(geojsonPath, gdbPath)
        arcpy.CheckInExtension('DataInteroperability')

    except:
        print(arcpy.GetMessages())

    # Also try using the KMLToLayer tool to create output datasets.

    try:
        arcpy.KMLToLayer_conversion(kmlPath, targetFolder)

    except:
        print(arcpy.GetMessages())

# If the user does not have the required extension, then attempt use the online GeoJSON
# converter.

else:

    try:
        # Define the url and the desired output name,
        url = 'http://ogre.adc4gis.com/convertJson/'
        outputName = '4.5_month' + dateString
        # Encode the parameters and attempt to download the data with a POST request
        params = urllib.urlencode({'jsonUrl' : geojsonUrl, 'outputName' : outputName})
        data = urllib2.urlopen(url, params).read()
        # Designate where the file should be written.
        zipPath = targetFolder + '/4.5_month' + dateString + '.zip'
        # Create a file handle to write to, write the data, and close the handle
        zipHand = open(zipPath, 'wb')
        zipHand.write(data)
        zipHand.close()
        # Create a zipfile object and extract the files to a desired folder
        zip = zipfile.ZipFile(zipPath, 'r')
        unzipPath = targetFolder + '/4.5_month' + dateString
        zip.extractall(unzipPath)
        # Rename all the zipped shapefile components so that they have descriptive names.
        # Some work is done as all files come with the same name but different extensions.
        for file in os.listdir(unzipPath):
            nameWoExt = os.path.splitext(file)[0]
            ext = os.path.splitext(file)[1]
            newNameWoExt = outputName
            newName = newNameWoExt + ext
            os.rename(os.path.join(unzipPath, file), os.path.join(unzipPath, newName))

    except:
        print('Problem retrieving shapefiles from webpage GeoJSON converter')

# Also try using the KMLToLayer tool to create output datasets.

    try:
        arcpy.KMLToLayer_conversion(kmlPath, targetFolder)

    except:
        print(arcpy.GetMessage())

