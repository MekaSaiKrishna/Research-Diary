
from abaqus import *
from abaqusConstants import *



session.viewports['Viewport: 1'].makeCurrent()



from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='OGMod_Cooling_8elem.odb')

#: Model: C:/ABAQUS+UMAT/Week101 [092624]/ResidualStress/OGMod_Cooling_8elem.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          9
#: Number of Steps:              1

viewport = session.viewports['Viewport: 1']

# Set the size of the viewport window to a square (e.g., 400x400 pixels)
viewport.setValues(width=400, height=400)

# Optionally, center the model in the square viewport
viewport.view.fitView()


session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
    title=OFF, state=OFF, annotations=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    compass=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legend=OFF)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FREE)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, DEFORMED, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.superimposeOptions.setValues(
    visibleEdges=FREE)
session.viewports['Viewport: 1'].odbDisplay.superimposeOptions.setValues(
    renderStyle=HIDDEN)
session.viewports['Viewport: 1'].odbDisplay.superimposeOptions.setValues(
    edgeLineStyle=DASHED, edgeLineThickness=MEDIUM)
session.viewports['Viewport: 1'].odbDisplay.superimposeOptions.setValues(
    edgeLineThickness=THIN)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    edgeColorWireHide='#FF0000')
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    edgeColorWireHide='#00FF00', fillColor='#0099FF')
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    fillColor='#FFEFDB')
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    fillColor='#EEC591')
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=5)



session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')



session.viewports['Viewport: 1'].odbDisplay.superimposeOptions.setValues(
    translucencyFactor=0)

session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    curveRefinementLevel=EXTRA_FINE)

session.printOptions.setValues(reduceColors=False)



# Loop to save images of all frames
x=0
while x < 101:
    session.viewports[session.currentViewportName].odbDisplay.setFrame(
        step='Step-1', frame=x)
    session.printToFile(
        fileName='C:/ABAQUS+UMAT/Week101 [092624]/ResidualStress/tiffImages/image'+str(x), 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    x = x+1

