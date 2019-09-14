##                                              ##
##              GEOG 485 Project 3              ##
##                 Script Tool                  ##

# Import necessary modules and allow overwrites

import arcpy
from arcpy.da import *
from arcpy import env
env.overwriteOutput = True

# Prompt for the workspace

env.workspace = arcpy.GetParameterAsText(0)

# Prompt for the point and country shapefiles

pointShapefile = arcpy.GetParameterAsText(1)
countryShapefile = arcpy.GetParameterAsText(2)

# Prompt for a comma-separated list of amenities and the country of interest
# State the required string format for correct splitting e.g. "A comma separated list with spaces after commas
# and underscores for spaces between words"

amenitiesString = arcpy.GetParameterAsText(3)
amenities = amenitiesString.split(', ')

country = arcpy.GetParameterAsText(4)
countryQuery = '"NAME" = ' + "'" + country + "'"

# Loop through the amenities specified in the list

for amenity in amenities:

    # Construct a string for later queries
    amenityQuery = '"amenity" = ' + "'" + amenity + "'"

    try:

        # Create feature layer of amenities and countries and select amenities within specified country
        arcpy.MakeFeatureLayer_management(pointShapefile, 'AmenityLayer', amenityQuery)
        arcpy.MakeFeatureLayer_management(countryShapefile, 'CountryLayer', countryQuery)
        arcpy.SelectLayerByLocation_management('AmenityLayer', "CONTAINED_BY", 'CountryLayer')

        # Create a naming convention for outputs
        amenityShapefile = amenity + '_' + country + '_shapefile.shp'

        # Save selection as a new feature class
        arcpy.CopyFeatures_management('AmenityLayer', amenityShapefile)

        # Delete created feature layers
        arcpy.Delete_management('AmenityLayer')
        arcpy.Delete_management('CountryLayer')
        

        try:

            # Add the source field
            arcpy.AddField_management(amenityShapefile, 'source', 'TEXT', '', '', 13)

            # Use cursor to iterate through rows and populate the source field with desired text
            with UpdateCursor(amenityShapefile, ('source',)) as cursor:
                for row in cursor:
                    row[0] = 'OpenStreetMap'
                    cursor.updateRow(row)
                del cursor


# Add error handling exceptions for problems arising from creating shapefiles and updating fields
        except:
            arcpy.AddError('There was an error creating and updating the source field within amenity shapefile')
            arcpy.AddMessage(arcpy.GetMessages())

    except:
        arcpy.AddError('There was an error creating the amenity shapefiles')
        arcpy.AddMessage(arcpy.GetMessages())
