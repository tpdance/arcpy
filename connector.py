__author__ = 'Owner'
import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"F:\PrivateLands\CB4YC"
output_space = arcpy.env.workspace
output_name = "connected.shp"

destination = r"F:\PrivateLands\CB4YC\county_point.shp"
origin = r"F:\PrivateLands\CB4YC\all_fy_editUTM.shp"

spatial_ref = arcpy.Describe(destination).spatialReference

dest_dict = {}

srCursor_dest = arcpy.da.SearchCursor(destination, ["COUNTYNAME", "SHAPE@X", "SHAPE@Y"])
for row in srCursor_dest:
    dest_dict[row[0]] = [row[1], row[2]]
del srCursor_dest

polylineFC = arcpy.CreateFeatureclass_management(output_space, output_name, "POLYLINE", "", "", "", spatial_ref)
arcpy.AddField_management(polylineFC, "LEN_MI", "FLOAT")


with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
    vertex_array = arcpy.Array()
    srCursor_origin = arcpy.da.SearchCursor(origin, ["TIMBER", "SHAPE@X", "SHAPE@Y"])
    for rows in srCursor_origin:
        if rows[0] in dest_dict:
            x1 = rows[1]
            y1 = rows[2]
            vertex1 = arcpy.Point(x1,y1)
            vertex_array.add(vertex1)
            x2 = dest_dict[rows[0]][0]
            y2 = dest_dict[rows[0]][1]
            vertex2 = arcpy.Point(x2, y2)
            vertex_array.add(vertex2)
            new_line = arcpy.Polyline(vertex_array)
            cursor.insertRow((new_line,))
            vertex_array.removeAll()


del srCursor_origin
