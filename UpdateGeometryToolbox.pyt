import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "UpdateGeometryToolbox"
        self.alias = "upgeo"

        # List of tool classes associated with this toolbox
        self.tools = [UpdateGeometryTool]


class UpdateGeometryTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "UpdateGeometryTool"
        self.description = "Update Geometry"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Feature Class",
            name = "in_features",
            datatype="DEFeatureClass",
            parameterType = "Required",
            direction = "Input"
        )

        param1 = arcpy.Parameter(
            displayName="Joint Feature Class",
            name = "joint_features",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Input"
        )

        param2 = arcpy.Parameter(
            displayName="Joint ID Field",
            name = "joint_id_field",
            datatype = "Field",
            parameterType = "Required",
            direction = "Input"
        )

        param2.parameterDependencies=[param1.name]

        return [param0,param1,param2]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        inFeatureClass = parameters[0].valueAsText
        jointFeatureClass = parameters[1].valueAsText
        jointField = parameters[2].valueAsText

        in_fields = ("OID@","SHAPE@")
        joint_fields = (jointField,"SHAPE@")
        count = 0
        with arcpy.da.UpdateCursor(inFeatureClass, in_fields) as inCursor:
            for row in inCursor:
                whereClause = (u'{} = '+ str(row[0])).format(arcpy.AddFieldDelimiters(jointFeatureClass, jointField))
                with arcpy.da.SearchCursor(jointFeatureClass,joint_fields,whereClause) as jointCursor:
                    jointRow = jointCursor.next()
                    if jointRow is not None:
                        if not row[1].equals(jointRow[1]) :
                            row[1]=jointRow[1]
                            inCursor.updateRow(row)
                            count+=1
        arcpy.AddMessage("Has Updated {} features.".format(count))
        return
