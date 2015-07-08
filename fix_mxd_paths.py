__author__ = 'George Kipp'
# Script: fix mxd paths
# Author: George Kipp
# For: Missouri LEAF
# Created Date: March 28th, 2015
# Last Modified Date: May 28th, 2015
# Description: This script fixes the path of an mxd when using geodatabases on removable media.
#   This script is meant to run in the interactive window only!

import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")
mxd.findAndReplaceWorkspacePaths("old", "new")
mxd.save()
