# This script uses the Spatial Analyst Contour tool to create 25 meter contour intervals
# for the foxlake DEM
 
import arcpy
arcpy.env.overwriteOutput = True
from arcpy.sa import *

# Specify path to foxlake input/output raster and set contour variables

inRaster = "C:/TmpWrkDirGIS/GEOG485/Lesson1/foxlake"
contourInterval = 25
baseContour = 0
outContour = "C:/TmpWrkDirGIS/GEOG485/Lesson1/foxlake_25m_contour"

# Run the contour tool using previously set variables with try/except error handling.

try:
    arcpy.CheckOutExtension("Spatial")
    Contour(inRaster, outContour, contourInterval, baseContour)
    arcpy.CheckInExtension("Spatial")
    print "Success!"

except:
    print "Error in producing contour map."



