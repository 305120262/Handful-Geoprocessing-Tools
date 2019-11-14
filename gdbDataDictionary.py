import arcpy
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet("Sheet1")
arcpy.env.workspace="C:\Temp\Connection to 192.168.1.80 oracle.sde"
fds  = arcpy.ListDatasets("*","feature")
r=0
sheet.write(r,0,"FeatureDataset")
sheet.write(r,1,"FeatureClass")
for fd  in fds:
    fcs = arcpy.ListFeatureClasses(feature_dataset=fd)
    fdName = arcpy.Describe(fd).name
    r = r+1
    sheet.write(r,0,fdName)
    for fc in fcs:
        r = r+1
        sheet.write(r,1,arcpy.Describe(fc).name)
r=r+1
sheet.write(r,0,"Standalone FeatureClasss")
sfcs = arcpy.ListFeatureClasses()
for sfc in sfcs:
    r = r+1
    fcName = arcpy.Describe(sfc).name
    sheet.write(r,1,fcName)
book.save("C:\Temp\datadic.xls")