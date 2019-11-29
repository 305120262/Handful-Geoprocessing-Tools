# coding=utf-8
import arcpy
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet("Sheet1")
arcpy.env.workspace=r"C:\Temp\Connection to 192.168.1.80 oracle.sde"
fds  = arcpy.ListDatasets("*","Feature")
r=0
sheet.write(r,0,"FeatureDataset")
sheet.write(r,1,"FeatureClass")
sheet.write(r,2,"CoordinateSystem")
for fd  in fds:
    fcs = arcpy.ListFeatureClasses(feature_dataset=fd)
    desc = arcpy.Describe(fd)
    fdName = desc.name
    srCode = desc.spatialReference.PCSCode
    r = r+1
    sheet.write(r,0,fdName)
    sheet.write(r,2,srCode)
    for fc in fcs:
        r = r+1
        fc_desc = arcpy.Describe(fc)
        sheet.write(r,1,fc_desc.name)
        sheet.write(r,2,fc_desc.spatialReference.PCSCode)
r=r+1
sheet.write(r,0,"Standalone FeatureClasss")
sfcs = arcpy.ListFeatureClasses()
for sfc in sfcs:
    r = r+1
    sfc_desc = arcpy.Describe(sfc)
    sheet.write(r,1,sfc_desc.name)
    sheet.write(r,2,sfc_desc.spatialReference.PCSCode)
book.save(r"C:\Temp\datadic.xls")
print(u"完成")
