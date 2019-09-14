# Import the neccessary modules for converting a folder filled with feature classes to a different projection
# which is identified by the user specifying a template feature class. Also set environment to allow overwriting existing files.

import arcpy
import os
arcpy.env.overwriteOutput = True

try:
    # Prompt the script user to input the paths to a target folder containing input feature classes,
    # and a template feature class which will specify the spatial reference to project to.
    # Also set an output folder path.
    
    targetFolder = arcpy.GetParameterAsText(0)
    templateFeatureClass = arcpy.GetParameterAsText(1)
    outputFolder = targetFolder + '/Projected/'
    
    # Set the workspace environment to the target folder set by user
    
    arcpy.env.workspace = targetFolder
    
    # Create a list of the feature classes in environment

    featureClassList = arcpy.ListFeatureClasses()

    # Create a spatial reference object of the template feature class specified by user

    templateSpatialReference = arcpy.Describe(templateFeatureClass).spatialReference

    # Create a list to hold the feature classes that have been successfully projected into the template spatial reference

    projectedList = []

    # I noticed that later in my code, my arcpy.project command did not automatically create a new folder for the output
    # despite using a path that includes this. Therefore, in my search for a solution, I found this statement using os.makedirs to create
    # the folder I will later put my projected shapefiles in. I found this solution by user Pixdigit on Stackoverflow: https://stackoverflow.com/questions/1274405/how-to-create-new-folder

    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # Set up a for loop to iterate through the feature classes contained in the target folder
    
    for featureClass in featureClassList:
        # Create a string which trims the .shp ending from the feature classes which will lated be renamed if they
        # are projected to a new spatial reference

        rootName = featureClass.replace('.shp','')

        # Create a spatial reference object for every feature class in the target folder

        featureClassSpatialReference = arcpy.Describe(featureClass).spatialReference

        # Set up an if statement which checks if the spatial reference object has the same name property as the
        # template spatial reference object
        
        if featureClassSpatialReference.name != templateSpatialReference.name:

            # Create a string which will be used to place the new projected feature class in the output path folder
            # and also add _projected.shp to the end of the feature class name

            projectedFeatureClass = outputFolder + rootName + '_projected.shp'

            # Use the project tool to convert the feature class into the template spatial reference

            arcpy.Project_management(featureClass, projectedFeatureClass, templateSpatialReference)

            # Append the feature class to the list of feature classes that have been projected

            projectedList.append(featureClass)

    # Create a string which will join the feature classes in the list of projected feature classes together seperated by a comma and space

    projectedString = 'Projected:   ' + ', '.join(projectedList)

    # Report message containing the feature classes projected

    arcpy.AddMessage(projectedString)

except:
    # Report an error message
    arcpy.AddError('There was an error in the geoprocessing')

    # Report any error messages that the Project tool may have generated
    arcpy.AddMessage(arcpy.GetMessages())

