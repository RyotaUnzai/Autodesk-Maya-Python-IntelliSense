from typing import (
    NewType,
    Any
)


boolean = NewType("boolean", bool)
uint = NewType("uint", int)
linear = NewType("linear", int)
angle = NewType("angle", int)
time = NewType("time", int)
floatrange = NewType("floatrange", float)
timerange = NewType("timerange", str)
name = NewType("name", str)
string = NewType("string", str)
script = NewType("script", str)


def vectorize(browserView: boolean, byFrame: float, camera: string, combineFillsEdges: boolean, currentFrame: boolean, curveTolerance: float, customExtension: string, detailLevel: int, edgeColor: tuple[int, int, int], edgeDetail: boolean, edgeStyle: string, edgeWeight: float, endFrame: float, filenameFormat: string, fillStyle: string, flashVersion: int, frameRate: int, height: int, hiddenEdges: boolean, highlightLevel: int, highlights: boolean, imageFormat: string, layer: name, minEdgeAngle: float, outlinesAtIntersections: boolean, outputFileName: string, pixelAspectRatio: float, reflectionDepth: int, reflections: boolean, renderLayers: boolean, renderOptimization: string, renderView: boolean, secondaryCurveFitting: boolean, shadows: boolean, showBackFaces: boolean, startFrame: float, svgAnimation: string, svgCompression: boolean, width: int) -> None:
    """Synopsis:
---
---
 vectorize([browserView=boolean], [byFrame=float], [camera=string], [combineFillsEdges=boolean], [currentFrame=boolean], [curveTolerance=float], [customExtension=string], [detailLevel=int], [edgeColor=[int, int, int]], [edgeDetail=boolean], [edgeStyle=string], [edgeWeight=float], [endFrame=float], [filenameFormat=string], [fillStyle=string], [flashVersion=int], [frameRate=int], [height=int], [hiddenEdges=boolean], [highlightLevel=int], [highlights=boolean], [imageFormat=string], [layer=name], [minEdgeAngle=float], [outlinesAtIntersections=boolean], [outputFileName=string], [pixelAspectRatio=float], [reflectionDepth=int], [reflections=boolean], [renderLayers=boolean], [renderOptimization=string], [renderView=boolean], [secondaryCurveFitting=boolean], [shadows=boolean], [showBackFaces=boolean], [startFrame=float], [svgAnimation=string], [svgCompression=boolean], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

vectorize is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Create a poly sphere.
cmds.polySphere()

Now vector render the current frame. The output will be a 320x240
swf vector file using the single color fill option, and have
"untitled.swf" as its name.
cmds.vectorize(imageFormat='swf', w=320, h=240, fs='SingleColor',
               c='persp', cf=True, ff='name.ext', of='untitled')

---


Flags:
---


---
browserView(bv): boolean
    properties: create
    Specifies whether to preview the render in the browser.  This option is
swf only.

---
byFrame(bf): float
    properties: create
    Specifies the frame increment.

---
camera(c): string
    properties: create
    Specifies the camera to render.

---
combineFillsEdges(cfe): boolean
    properties: create
    Specifies whether fills and edges should be combined as a single object
in Flash. This option is swf only.

---
currentFrame(cf): boolean
    properties: create
    Specifies whether to render the current frame only.

---
curveTolerance(ct): float
    properties: create
    Specifies the curve tolerance.  Valid values are in the range: 0.0 to
15.0.  The curve tolerance determines how aggressively the renderer tries
to fit a series of connected, consecutive line segments to a curve.
A value of 0.0 causes all line segments to be drawn without curve
fitting.  A value of 15.0 causes aggressive curve fitting.

---
customExtension(ce): string
    properties: create
    Specifies a custom extension to use for the filename. Any non-empty
string is valid.

---
detailLevel(dl): int
    properties: create
    Specifies the detail level.  Valid values are:  0 to 50.  The smaller the
value, the more polygons may be combined to produce smaller files.  A
higher value results in a more accurate render, but also larger files
and longer render times.

---
edgeColor(ec): [int, int, int]
    properties: create
    Specifies the red, green, and blue components of the edge color.  Valid
values are: 0 to 255 for each color component.

---
edgeDetail(ed): boolean
    properties: create
    Specifies whether edge detail should be rendered; ie. edges that
have an angle between the face normals of any two adjacent polygons
sharing an edge that is greater than the minimum edge angle (specified by
the -mea flag).

---
edgeStyle(es): string
    properties: create
    Specifies the edge style.  Valid values are:  "Outline", "EntireMesh",
"None".

---
edgeWeight(ew): float
    properties: create
    Specifies the edge weight to be used for all edges in points.  There are
72 points per inch.  A value of 0.0 specifies hairline edge weight.

---
endFrame(ef): float
    properties: create
    Specifies the end frame.

---
filenameFormat(ff): string
    properties: create
    Specifies the file name format.  Valid values are:  "name", "name.ext",
"name.#.ext", "name.ext.#", "name.#", "name#.ext", "name_#.ext".

---
fillStyle(fs): string
    properties: create
    Specifies the fill style.  Valid values are:  "SingleColor", "TwoColor",
"FourColor", "FullColor", "AverageColor", "AreaGradient",
"MeshGradient", "None".  AreaGradient and MeshGradient are not available
for the eps and ai image formats.

---
flashVersion(fv): int
    properties: create
    Specifies the Flash version of the swf output.  Valid values are:  3, 4,
5.  This option is swf only.

---
frameRate(fr): int
    properties: create
    Specifies the frame rate.  This option is for svg and swf only.

---
height(h): int
    properties: create
    Specifies the height of the output image in pixels.

---
hiddenEdges(he): boolean
    properties: create
    Specifies whether hidden edges should be rendered; ie. edges that have
are not visible from the camera.

---
highlightLevel(hl): int
    properties: create
    Specifies the highlight level.  Valid values are:  1 to 8.  The value
specifies how many concentric rings will be used to render an object's
highlight.  This option is for the SingleColor, AverageColor, and
AreaGradient fill styles only.

---
highlights(hi): boolean
    properties: create
    Specifies whether highlights should be rendered.  This option has no
effect for ai, eps, and svg.  This option is for the SingleColor,
AverageColor, and AreaGradient fill styles only.

---
imageFormat(imageFormat): string
    properties: create
    Specifies the image format to render. Valid values for the Windows and
Mac platforms are: "swf", "eps", "ai", "svg", "jpg", "iff", "sgi", "tga",
"tif", "bmp". Additional valid values for the Windows platform are:
"als", "cin", "gif", "yuv", "rla", "si".  Additional valid values for the
Mac platform are: "pntg", "ps", "png", "pict", "qtif", "qt".

---
layer(l): name
    properties: create
    Render the specified render layer.
        Only this render layer will be rendered,
        regardless of the renderable attribute value of the render layer.
        The layer name will be appended to the output image file name.
        The specified render layer becomes the current render layer before rendering,
        and remains as current render layer after the rendering.

---
minEdgeAngle(mea): float
    properties: create
    Specifies the minimum edge angle in degrees.  Valid values are: 0.0 to
90.0.  This angle is the minimum angle between adjacent polygon face
normals that is used to determine if the edge is rendered when the -ed
flag is specified.

---
outlinesAtIntersections(oai): boolean
    properties: create
    Specifies if edges should be drawn when two polygons intersect. By default
this flag is enabled.

---
outputFileName(of): string
    properties: create
    Specifies the output file name.

---
pixelAspectRatio(par): float
    properties: create
    Specifes the pixel aspect ratio.

---
reflectionDepth(rd): int
    properties: create
    Specifies the reflection depth.  Valid values are:  1 to 4.  The value
specifies how many levels of reflection will be applied.  This option has
no effect for ai, eps, and svg.

---
reflections(rf): boolean
    properties: create
    Specifies whether reflections should be rendered.  This option has no
effect for ai, eps, and svg.

---
renderLayers(rl): boolean
    properties: create
    Specifies whether render layers should be rendered into separate files.

---
renderOptimization(ro): string
    properties: create
    Specifies the render optimization. Valid values are:  "Safe", "Good",
"Aggressive".
"Safe"  will  remove redundant geometry.
"Good" removes redundant geometry as well as sub-pixel
geometry that would not be visible without zooming
into the high detail area.
"Agressive" removes all of the geometry that "Good" removes
but will also remove geometry at slightly above the
single pixel level making it possible to visibly detect
the removed geometry without zooming in on the affected region.

---
renderView(rv): boolean
    properties: create
    Specifies whether to display the rendered image to the render view.  This
option is not applicable when batch rendering.

---
secondaryCurveFitting(scf): boolean
    properties: create
    Specifies whether to do secondary curve fitting.

---
shadows(sh): boolean
    properties: create
    Specifies whether shadows should be rendered.  This option has no
effect for ai, eps, and svg.

---
showBackFaces(sb): boolean
    properties: create
    Specifies whether back faces will should be rendered; ie. faces whose
normals are pointed away from the camera.

---
startFrame(sf): float
    properties: create
    Specifies the start frame.

---
svgAnimation(sa): string
    properties: create
    Specifies the SVG animation type.  Valid values are:  "Native",
"HTMLScript".  This option is SVG only.

---
svgCompression(sc): boolean
    properties: create
    Specifies whether the SVG output should be compressed.  This option is
svg only.

---
width(w): int
    properties: create
    Specifies the width of the output image in pixels.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/vectorize.html 
    """


def view2dToolCtx(alternateContext: boolean, boxzoom: boolean, dolly: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, toolName: string, track: boolean) -> string:
    """Synopsis:
---
---
 view2dToolCtx([alternateContext=boolean], [boxzoom=boolean], [dolly=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [toolName=string], [track=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

view2dToolCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a new view2dTool context, set it to do dolly in the Hypergraph window, then switch to this tool
cmds.view2dToolCtx('view2dToolCtx1', dolly=True)
cmds.setToolTo('view2dToolCtx1')

---
Return:
---


    string: The context name

Flags:
---


---
alternateContext(ac): boolean
    properties: create, query
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

---
boxzoom(bz): boolean
    properties: create, query
    Perform Box Zoom

---
dolly(do): boolean
    properties: create, query
    Dollies the view

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
history(ch): boolean
    properties: create
    If this is a tool command, turn the construction history on
for the tool in question.

---
image1(i1): string
    properties: create, query, edit
    First of three possible icons representing the tool
associated with the context.

---
image2(i2): string
    properties: create, query, edit
    Second of three possible icons representing the tool
associated with the context.

---
image3(i3): string
    properties: create, query, edit
    Third of three possible icons representing the tool
associated with the context.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
toolName(tn): string
    properties: create, query
    Name of the specific tool to which this command refers.

---
track(tr): boolean
    properties: create, query
    Tracks the view

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/view2dToolCtx.html 
    """


def viewCamera(move: name, sideView: boolean, topView: boolean) -> None:
    """Synopsis:
---
---
 viewCamera(
[camera]
    , [move=name], [sideView=boolean], [topView=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewCamera is undoable, NOT queryable, and NOT editable.
The default behaviour: If no other flags are specified, the camera
in the active panel is moved and the -t is presumed. If there is a
camera selected, it is used as the target camera.




Example:
---
import maya.cmds as cmds

cmds.viewCamera( 'cameraShape2', m='cameraShape1' )

Move current view camera to top of camera1
cmds.viewCamera( 'camera1' )

---


Flags:
---


---
move(m): name
    properties: create
    Specifies which camera needs to move.

---
sideView(s): boolean
    properties: create
    Position camera to look at the side of the target camera.

---
topView(t): boolean
    properties: create
    Position camera to look at the top of the target camera
(default).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewCamera.html 
    """


def viewClipPlane(autoClipPlane: boolean, farClipPlane: linear, nearClipPlane: linear, surfacesOnly: boolean) -> None:
    """Synopsis:
---
---
 viewClipPlane(
[camera]
    , [autoClipPlane=boolean], [farClipPlane=linear], [nearClipPlane=linear], [surfacesOnly=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewClipPlane is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.viewClipPlane( 'perspShape', acp=True )

cmds.viewClipPlane( acp=True )

cmds.viewClipPlane( acp=True, ncp=3.0 )

cmds.viewClipPlane( ncp='3.0cm' )

cmds.viewClipPlane( 'perspShape', q=True, ncp=True )

---


Flags:
---


---
autoClipPlane(acp): boolean
    properties: create, query
    Compute the clip planes such that all object's in the camera's
viewing frustum will be visible.

---
farClipPlane(fcp): linear
    properties: create, query
    Set or query the far clip plane.

---
nearClipPlane(ncp): linear
    properties: create, query
    Set or query the near clip plane.

---
surfacesOnly(so): boolean
    properties: create
    This flag is to be used in conjunction with the auto clip
plane flag. Only the bounding boxes of surfaces will be used
to compute the camera's clipping planes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewClipPlane.html 
    """


def viewFit(allObjects: boolean, animate: boolean, center: boolean, fitClipPlanes: boolean, fitFactor: float, namespace: string, noChildren: boolean) -> None:
    """Synopsis:
---
---
 viewFit(
[camera...]
    , [allObjects=boolean], [animate=boolean], [center=boolean], [fitClipPlanes=boolean], [fitFactor=float], [namespace=string], [noChildren=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewFit is undoable, NOT queryable, and NOT editable.
Additionally, a list of objects can be passed as arguments.
If a camera is specified it must be the first argument. Objects
passed as arguments to the command will be used instead of the
selected objects.




Example:
---
import maya.cmds as cmds

Position the active camera to view the active objects
cmds.viewFit()

Position cameraShape-1 to view all objects
cmds.viewFit( 'cameraShape1', all=True )

Fill 50 percent of the active view with active objects
cmds.viewFit( f=0.5 )

cmds.viewFit( all=True )

---


Flags:
---


---
allObjects(all): boolean
    properties: create
    Specifies that all objects are to be fit regardless of the
active list.

---
animate(an): boolean
    properties: create
    Specifies that the transition between camera positions
should be animated.

---
center(c): boolean
    properties: create
    Specifies that the camera moves to the center of the
selected object, but does not move the camera closer.

---
fitClipPlanes(fcp) 2024: boolean
    properties: create
    Fit orthographic clipping planes in order to contain selection bounding box in the view frustum

---
fitFactor(f): float
    properties: create
    Specifies how much of the view should be filled with the
"fitted" items.

---
namespace(ns): string
    properties: create
    Specifies a namespace that should be excluded. All objects
in the specified namespace will be excluded from the fit
process.

---
noChildren(noc): boolean
    properties: create
    Specifies that the children of fitted objects should be ignored when determining
the fit.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewFit.html 
    """


def viewHeadOn() -> None:
    """Synopsis:
---
---
 viewHeadOn(
[camera]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewHeadOn is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a new camera
cam = cmds.camera()
camera = cam[0]

Create a polygonal cone, rotate it, make it live
object = cmds.polyCone( ax=(0, 1, 0) )
cmds.rotate( 15, 30, 45 )
cmds.makeLive( object[0] )

cmds.viewHeadOn( camera )

cmds.makeLive( none=True )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewHeadOn.html 
    """


def viewLookAt(position: tuple[linear, linear, linear]) -> None:
    """Synopsis:
---
---
 viewLookAt(
[camera]
    , [position=[linear, linear, linear]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewLookAt is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a new camera
cam = cmds.camera()
camera = cam[0]

cmds.viewLookAt( camera, pos=(0.0, 1.0, 0.0) )

---


Flags:
---


---
position(pos): [linear, linear, linear]
    properties: create
    Position in world space to make the camera look at.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewLookAt.html 
    """


def viewManip(bottomLeft: boolean, bottomRight: boolean, compassAngle: float, dragSnap: boolean, drawCompass: boolean, fitToView: boolean, frontParameters: string, goDefault: boolean, goHome: boolean, homeParameters: string, levelCamera: boolean, minOpacity: float, namespace: string, postCommand: string, preCommand: string, preserveSceneUp: boolean, resetFront: boolean, resetHome: boolean, restoreCenter: boolean, selectionLockParameters: string, setFront: boolean, setHome: boolean, size: string, toggleSelectionLock: boolean, topLeft: boolean, topRight: boolean, visible: boolean, zoomToFitScene: boolean) -> None:
    """Synopsis:
---
---
 viewManip([bottomLeft=boolean], [bottomRight=boolean], [compassAngle=float], [dragSnap=boolean], [drawCompass=boolean], [fitToView=boolean], [frontParameters=string], [goDefault=boolean], [goHome=boolean], [homeParameters=string], [levelCamera=boolean], [minOpacity=float], [namespace=string], [postCommand=string], [preCommand=string], [preserveSceneUp=boolean], [resetFront=boolean], [resetHome=boolean], [restoreCenter=boolean], [selectionLockParameters=string], [setFront=boolean], [setHome=boolean], [size=string], [toggleSelectionLock=boolean], [topLeft=boolean], [topRight=boolean], [visible=boolean], [zoomToFitScene=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewManip is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

---
Position the view cube in the top left of the screen and set it to fully opaque
cmds.viewManip(topLeft=True, minOpacity=1)

---


Flags:
---


---
bottomLeft(bl): boolean
    properties: create, query
    Positions the cube in the bottom left of the screen.

---
bottomRight(br): boolean
    properties: create, query
    Positions the cube in the bottom right of the screen.

---
compassAngle(ca): float
    properties: create, query
    Angle (in degrees) to rotate the compass.

---
dragSnap(ds): boolean
    properties: create, query
    Enable snapping of orbit direction to view cube part directions during drag operation.

---
drawCompass(dc): boolean
    properties: create, query
    Show compass below the view cube.

---
fitToView(ftv): boolean
    properties: create
    Fits the scene bounding box to the active view.

---
frontParameters(fp): string
    properties: create, query
    Parameter string for the front position

---
goDefault(gd): boolean
    properties: create, query
    Go to the default position

---
goHome(gh): boolean
    properties: create, query
    Go to the home position

---
homeParameters(hp): string
    properties: create, query
    Parameter string for the home position

---
levelCamera(lc): boolean
    properties: create
    Flattens the camera view rotation relative to the ground plane.

---
minOpacity(mo): float
    properties: create, query
    Opacity level (in range [0,1]) on view cube when the cursor is away from it (it is fully opaque when the cursor is in the view cube area).

---
namespace(ns): string
    properties: create, query
    Namespace to use for the object

---
postCommand(p): string
    properties: create, query
    Command to run after moving

---
preCommand(pr): string
    properties: create, query
    Command to run before moving

---
preserveSceneUp(psu): boolean
    properties: create, query
    Specify whether the scene "up" direction should be preserved

---
resetFront(rf): boolean
    properties: create, query
    Reset the front position

---
resetHome(rh): boolean
    properties: create, query
    Reset the home position

---
restoreCenter(rc): boolean
    properties: create
    Repositions the pivot point for orbiting/tumbling the scene to the center
of the scene's bounding box.

---
selectionLockParameters(slp): string
    properties: create, query
    String containing the selection lock parameters

---
setFront(sf): boolean
    properties: create
    Set the front view to the current one

---
setHome(sh): boolean
    properties: create
    Set the home view to the current one

---
size(s): string
    properties: create, query
    Set or query the size of the View Cube, which can be one of "tiny",
"small", "normal", "large" or "auto". When set to "auto" the View Cube
will be automatically set to the size most appropriate for the view.

---
toggleSelectionLock(tsl): boolean
    properties: create
    Toggle the selection lock

---
topLeft(tl): boolean
    properties: create, query
    Positions the cube in the top left of the screen.

---
topRight(tr): boolean
    properties: create, query
    Positions the cube in the top right of the screen.

---
visible(v): boolean
    properties: create, query
    Shows/hides the view manip.

---
zoomToFitScene(zf): boolean
    properties: create, query
    Zoom the camera during animated transitions to fit the scene object in the viewport.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewManip.html 
    """


def viewPlace(animate: boolean, eyePoint: tuple[linear, linear, linear], fieldOfView: angle, lookAt: tuple[linear, linear, linear], ortho: boolean, perspective: boolean, upDirection: tuple[linear, linear, linear], viewDirection: tuple[linear, linear, linear]) -> None:
    """Synopsis:
---
---
 viewPlace(
[camera]
    , [animate=boolean], [eyePoint=[linear, linear, linear]], [fieldOfView=angle], [lookAt=[linear, linear, linear]], [ortho=boolean], [perspective=boolean], [upDirection=[linear, linear, linear]], [viewDirection=[linear, linear, linear]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewPlace is undoable, NOT queryable, and NOT editable.

If the camera is not specified on the command line, the command
will check to see if there is a camera on the active list. 

The user should be aware that some positions will be
unattainable. For example, using a new camera located at the
origin and specifying a lookAt of [0 0 -5] and an up of [1 1
1]. In these cases, the camera will always aim at the lookAt, and
the new up direction will be determined by transforming the
specified up into camera space and then projecting this vector
onto a plane defined by the camera's up and right vectors. Using
the example above, the new up vector will be [1 1 0]. 




Example:
---
import maya.cmds as cmds

Create a new camera
cam = cmds.camera();
camShape = cam[1];

cmds.viewPlace( camShape, p=True, fov=20 )

cmds.viewPlace( camShape, eye=(0, 0, 20) )

cmds.viewPlace( camShape, la=(0, 0, 0) )

---


Flags:
---


---
animate(an): boolean
    properties: create
    If set to true then animate the camera transition from current
position to the final one.

---
eyePoint(eye): [linear, linear, linear]
    properties: create
    The new eye point in world coordinates.

---
fieldOfView(fov): angle
    properties: create
    The new field of view (in degrees, for perspective cameras,
and in world distance for ortho cameras)

---
lookAt(la): [linear, linear, linear]
    properties: create
    The new look-at point in world coordinates.

---
ortho(o): boolean
    properties: create
    Sets the camera to be orthgraphic.

---
perspective(p): boolean
    properties: create
    Sets the camera to be perspective.

---
upDirection(up): [linear, linear, linear]
    properties: create
    The new up direction vector.

---
viewDirection(vd): [linear, linear, linear]
    properties: create
    The new view direction vector.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewPlace.html 
    """


def viewSet(animate: boolean, back: boolean, bottom: boolean, fit: boolean, fitFactor: float, front: boolean, home: boolean, keepRenderSettings: boolean, leftSide: boolean, namespace: string, nextView: boolean, persp: boolean, previousView: boolean, rightSide: boolean, side: boolean, top: boolean, viewNegativeX: boolean, viewNegativeY: boolean, viewNegativeZ: boolean, viewX: boolean, viewY: boolean, viewZ: boolean) -> None:
    """Synopsis:
---
---
 viewSet(
[camera]
    , [animate=boolean], [back=boolean], [bottom=boolean], [fit=boolean], [fitFactor=float], [front=boolean], [home=boolean], [keepRenderSettings=boolean], [leftSide=boolean], [namespace=string], [nextView=boolean], [persp=boolean], [previousView=boolean], [rightSide=boolean], [side=boolean], [top=boolean], [viewNegativeX=boolean], [viewNegativeY=boolean], [viewNegativeZ=boolean], [viewX=boolean], [viewY=boolean], [viewZ=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

viewSet is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a new camera
cam = cmds.camera();
camShape = cam[1];

Set cameraShape1 to the persp position
cmds.viewSet( camShape, p=True )

Set the camera in the active view to the top position
cmds.viewSet( t=True )

---


Flags:
---


---
animate(an): boolean
    properties: create
    Specifies that the transition between camera positions
should be animated.

---
back(b): boolean
    properties: create
    Moves the camera to the back position.

---
bottom(bo): boolean
    properties: create
    Moves the camera to the bottom position.

---
fit(fit): boolean
    properties: create, query
    Apply a viewFit after positioning camera to persp, top, side,
or front.

---
fitFactor(ff): float
    properties: create
    Specifies how much of the view should be filled with the "fitted" items

---
front(f): boolean
    properties: create
    Moves the camera to the front position.

---
home(h): boolean
    properties: create
    Executes the camera's home attribute command. Before the
string is executed, all occurances of "%camera" will be
replaced by the camera's name. Use the camera command to set a
camera's home command.

---
keepRenderSettings(krs): boolean
    properties: create, query
    Retain the 'renderable' flag vaue on the view. Especially important if it switches from
perspective to orthographic and then back again.

---
leftSide(ls): boolean
    properties: create
    Moves the camera to the left side position.

---
namespace(ns): string
    properties: create
    Specifies a namespace that should be excluded. All objects
in the specified namespace will be excluded from the fit
process.

---
nextView(nv): boolean
    properties: create, query
    Moves the camera to the next position.

---
persp(p): boolean
    properties: create
    Moves the camera to the persp position.

---
previousView(pv): boolean
    properties: create, query
    Moves the camera to the previous position.

---
rightSide(rs): boolean
    properties: create
    Moves the camera to the right side position.

---
side(s): boolean
    properties: create
    Moves the camera to the (right) side position (deprecated).

---
top(t): boolean
    properties: create
    Moves the camera to the top position.

---
viewNegativeX(vnx): boolean
    properties: create
    Moves the camera to view along negative X axis.

---
viewNegativeY(vny): boolean
    properties: create
    Moves the camera to view along negative Y axis.

---
viewNegativeZ(vnz): boolean
    properties: create
    Moves the camera to view along negative Z axis.

---
viewX(vx): boolean
    properties: create
    Moves the camera to view along X axis.

---
viewY(vy): boolean
    properties: create
    Moves the camera to view along Y axis.

---
viewZ(vz): boolean
    properties: create
    Moves the camera to view along Z axis.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/viewSet.html 
    """


def visor(addFolder: boolean, addNodes: string, allowPanningInX: boolean, allowPanningInY: boolean, allowZooming: boolean, command: string, deleteFolder: string, editFolder: string, folderList: string, menu: string, name: string, nodeType: string, openDirectories: boolean, openFolder: boolean, parent: string, path: string, popupMenuScript: string, rebuild: boolean, refreshAllSwatches: boolean, refreshSelectedSwatches: boolean, refreshSwatch: string, reset: boolean, restrictPanAndZoom: boolean, saveSwatches: boolean, scrollBar: string, scrollPercent: float, selectedGadgets: string, showDividers: boolean, showFiles: boolean, showFolders: boolean, showNodes: boolean, stateString: boolean, style: string, transform: string, type: string) -> string:
    """Synopsis:
---
---
 visor([addFolder=boolean], [addNodes=string], [allowPanningInX=boolean], [allowPanningInY=boolean], [allowZooming=boolean], [command=string], [deleteFolder=string], [editFolder=string], [folderList=string], [menu=string], [name=string], [nodeType=string], [openDirectories=boolean], [openFolder=boolean], [parent=string], [path=string], [popupMenuScript=string], [rebuild=boolean], [refreshAllSwatches=boolean], [refreshSelectedSwatches=boolean], [refreshSwatch=string], [reset=boolean], [restrictPanAndZoom=boolean], [saveSwatches=boolean], [scrollBar=string], [scrollPercent=float], [selectedGadgets=string], [showDividers=boolean], [showFiles=boolean], [showFolders=boolean], [showNodes=boolean], [stateString=boolean], [style=string], [transform=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

visor is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

The visor command is not one which would commonly be used by the user.
For examples of its use, refer to visorPanel.mel and addVisorFolders.mel.

---
Return:
---


    string: Command result

Flags:
---


---
addFolder(add): boolean
    properties: create, query
    Add a new folder to the current visual browser

---
addNodes(adn): string
    properties: create, query
    Add dependency graph nodes by name to a user defined custom folder.  The
argument is a string encolsed in quotes with 1 one more node names
seperated by blanks

---
allowPanningInX(apx): boolean
    properties: create, query
    Specifies whether or not the user should be able to pan the contents of the
visor horizontally. Default is true.

---
allowPanningInY(apy): boolean
    properties: create, query
    Specifies whether or not the user should be able to pan the contents of the
visor vertically. Default is true.

---
allowZooming(az): boolean
    properties: create, query
    Specifies whether or not the user should be able to zoom the contents of the
visor. Default is true.

---
command(cmd): string
    properties: create, query
    Mel command which will return a list of nodes to add to a folder

---
deleteFolder(deleteFolder): string
    properties: create, query
    Delete the specified folder and all of its children

---
editFolder(edf): string
    properties: create, query
    Edit the name and MEL command for an existing folder

---
folderList(fl): string
    properties: query
    Return a string array of the folders in the visor.

---
menu(mn): string
    properties: create, query
    Set the name of the script to run to get a popup menu

---
name(n): string
    properties: create, query
    Name of the new folder

---
nodeType(ntp): string
    properties: create, query
    A node type used by folders of type nodeTypeInDAG

---
openDirectories(opd): boolean
    properties: create, query
    When adding a new folder indicate if it sub directories will be show.
The default is to not show sub directories.

---
openFolder(opf): boolean
    properties: create, query
    When adding a new folder indicate if it will be open or closed by default.
The default is closed.

---
parent(p): string
    properties: create, query
    Parent folder of this folder

---
path(pth): string
    properties: create, query
    Path to a file system directory to be displayed in the folder

---
popupMenuScript(pms): string
    properties: create, query
    Specifies the script to be called when the right mouse button is pressed in
the visor. The name of the editor in which the right mouse button was pressed
will be appended to the script at the time the script is called.

---
rebuild(re): boolean
    properties: create, query
    Rebuild the visor after interactively adding a folder

---
refreshAllSwatches(ras): boolean
    properties: create, query
    Refresh the swatches of all files currently displayed in this visor.

---
refreshSelectedSwatches(rss): boolean
    properties: create, query
    Refresh the swatches of all files currently selected in any visor.

---
refreshSwatch(rs): string
    properties: create, query
    Refresh the swatch of the file with the specified path.

---
reset(rst): boolean
    properties: create, query
    Clear all previously loaded folder descriptions in preperation for
building a new visual browser

---
restrictPanAndZoom(rpz): boolean
    properties: create, query
    Specifies whether the panning and zooming of the visor should be
restricted to keep the contents in the top left corner of the
visor when they are smaller than the visible area within the visor.
Default is true.

---
saveSwatches(ss): boolean
    properties: create, query
    Save swatches to disk for currently displayed image files.

---
scrollBar(sb): string
    properties: create, query
    Set the name of the scroll bar associated with visor

---
scrollPercent(sp): float
    properties: create, query
    Set the percentage value for the scroll bar.  Typically called from a
a scroll bars callback.

---
selectedGadgets(sg): string
    properties: query
    Return a string array of the currently selected gadgets (files, folders, nodes)
in the visor.

---
showDividers(sd): boolean
    properties: create, query
    Specifies whether or not the visor should show dividers. The default is true.
If -showDividers is set to false, dividers will be drawn as folders instead.

---
showFiles(sfi): boolean
    properties: create, query
    Specifies whether or not the visor should show files. The default is true.

---
showFolders(sfo): boolean
    properties: create, query
    Specifies whether or not the visor should show folders. The default is true.

---
showNodes(sn): boolean
    properties: create, query
    Specifies whether or not the visor should show nodes. The default is true.

---
stateString(sts): boolean
    properties: create, query
    Return the MEL command string to save the folder setup in visor

---
style(stl): string
    properties: create, query
    Set display style for the browser.  Options are:
    outliner
         A single column with an outliner style icon and a text label
    singleColumn
         A single column with an image style icon and a text label
    multiColumn
         A multiple column grid of swatches with the text label below the swatch

---
transform(trn): string
    properties: create, query
    Name of a transform node used by folders of type nodeTypeInDAG

---
type(typ): string
    properties: create, query
    Type of the new folder.  Options are: 

command 
         A mel command that will return a list of depend nodes that will
         be displayed in the folder
connectedNodes 
         The nodes connected to the specified node name will be displayed
         in the folder
defaultNodes 
         A mel command that will generate default node types.  These nodes
         will not be part of the scene and are used for drag and drop
         creation of new nodes that are in the scene.  The mel command
         use with this type is usually "listNodetypes".
directory 
        A directory name in the file system
directoryCommand 
        A mel command that will return a directory name in the file system
folder 
        An empty folder(the default value).  Empty folders can be used
        as user defined folders by dropping dependency graph nodes in to them
nodeTypeInDAG 
                List all nodes of a given type under a specified transforms in the
                DAG.  For example list all the shaders for a character by specifying
        the top transform of the character
shelfItems 
        A directory containing mel files to use as shelf items

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/visor.html 
    """


def volumeAxis(alongAxis: float, aroundAxis: float, attenuation: float, awayFromAxis: float, awayFromCenter: float, detailTurbulence: float, directionX: float, directionY: float, directionZ: float, directionalSpeed: float, invertAttenuation: boolean, magnitude: float, maxDistance: linear, name: string, perVertex: boolean, position: tuple[linear, linear, linear], torusSectionRadius: linear, turbulence: float, turbulenceFrequencyX: float, turbulenceFrequencyY: float, turbulenceFrequencyZ: float, turbulenceOffsetX: float, turbulenceOffsetY: float, turbulenceOffsetZ: float, turbulenceSpeed: float, volumeExclusion: boolean, volumeOffset: tuple[linear, linear, linear], volumeShape: string, volumeSweep: angle) -> string:
    """Synopsis:
---
---
 volumeAxis(
selectionList
    , [alongAxis=float], [aroundAxis=float], [attenuation=float], [awayFromAxis=float], [awayFromCenter=float], [detailTurbulence=float], [directionX=float], [directionY=float], [directionZ=float], [directionalSpeed=float], [invertAttenuation=boolean], [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear], [turbulence=float], [turbulenceFrequencyX=float], [turbulenceFrequencyY=float], [turbulenceFrequencyZ=float], [turbulenceOffsetX=float], [turbulenceOffsetY=float], [turbulenceOffsetZ=float], [turbulenceSpeed=float], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

volumeAxis is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
A volume axis field can push particles in four directions, defined with
respect to a volume: along the axis, away from the axis or center,
around the axis, and in a user-specified direction.  These are analogous
to the emission speed controls of volume emitters. The volume axis field
also contains a wind turbulence model (different from the
turbulence field) that simulates an evolving flow of liquid or
gas. The turbulence has a build in animation that is driven
by a connection to a time node.

The transform is the associated dependency node.
Use connectDynamic to cause the field to affect a dynamic object.

If fields are created, this command returns the names of each
of the fields. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If object names are provided or the active selection list is non-empty,
the command creates a field for every object in the list and calls
addDynamic to add it to the object. If the
list is empty, the command defaults to -pos 0 0 0.

Setting the -pos flag with objects named on the command line is an error.




Example:
---
import maya.cmds as cmds

cmds.volumeAxis( pos=(0, 0, 0), afc=1.0, afx=2.0, arx=3.0, alx=4.0, drs=6.0 )

Creates a volume axis field with the following attribute values:
awayFromCenter = 1.0, awayFromAxis = 2.0, aroundAxis = 3.0, alongAxis = 4.0,
directionalSpeed = 6.0.

---
Return:
---


    string: Command result

Flags:
---


---
alongAxis(alx): float
    properties: query, edit
    Initial velocity multiplier in the direction along
the central axis of the volume.  See the diagrams in
the documentation.

---
aroundAxis(arx): float
    properties: query, edit
    Initial velocity multiplier in the direction around
the central axis of the volume.  See the diagrams
in the documentation.

---
attenuation(att): float
    properties: query, edit
    Attentuation rate of field

---
awayFromAxis(afx): float
    properties: query, edit
    Initial velocity multiplier in the direction away
from the central axis of the volume.  See the diagrams
in the documentation.  Used only with the cylinder, cone,
and torus volumes.

---
awayFromCenter(afc): float
    properties: query, edit
    Initial velocity multiplier in the direction away from
the center point of a cube or sphere volume. Used only with
the cube and sphere volumes.

---
detailTurbulence(dtr): float
    properties: query, edit
    The relative intensity of a second higher frequency turbulence.
This can be used to create fine features in large scale flows.
Both the speed and the frequency on this second turbulence are
higher than the primary turbulence. When the detailTurbulence
is non-zero the simulation may run a bit slower, due to the
computation of a second turbulence.

---
directionX(dx): float
    properties: query, edit
    x-component of force direction.  Used with directional speed.

---
directionY(dy): float
    properties: query, edit
    y-component of force direction.  Used with directional speed.

---
directionZ(dz): float
    properties: query, edit
    z-component of force direction.  Used with directional speed.

---
directionalSpeed(drs): float
    properties: query, edit
    Adds a component of speed in the
direction specified by the directionX, Y, and Z attributes.

---
invertAttenuation(ia): boolean
    properties: query, edit
    If this attribute is FALSE, the default, then the
attenuation makes the field's effect decrease as the
affected point is further from the volume's axis and
closer to its edge.  If the is set to TRUE, then the
effect of the field increases in this case, making the
full effect of the field felt at the volume's edge.

---
magnitude(m): float
    properties: query, edit
    Strength of field.

---
maxDistance(mxd): linear
    properties: query, edit
    Maximum distance at which field is exerted.
-1 indicates that the field has no maximum distance.

---
name(n): string
    properties: query, edit
    name of field

---
perVertex(pv): boolean
    properties: query, edit
    Per-vertex application. If this flag is set true, then each
individual point (CV, particle, vertex,etc.) of the chosen object
exerts an identical copy of the force field. If this flag is set to
false, then the froce is exerted only from the geometric center of
the set of points.

---
position(pos): [linear, linear, linear]
    properties: query, edit, multiuse
    Position in space (x,y,z) where you want to place a gravity field.
The gravity then emanates from this position in space rather
than from an object. Note that you can both use -pos
(creating a field at a position) and also provide object names.

---
torusSectionRadius(tsr): linear
    properties: query, edit
    Section radius for a torus volume.  Applies only to torus.
Similar to the section radius in the torus modelling primitive.

---
turbulence(trb): float
    properties: query, edit
    Adds a force simulating a turbulent
wind that evolves over time.

---
turbulenceFrequencyX(tfx): float
    properties: query, edit
    The repeats of the turbulence function in X.

---
turbulenceFrequencyY(tfy): float
    properties: query, edit
    The repeats of the turbulence function in Y.

---
turbulenceFrequencyZ(tfz): float
    properties: query, edit
    The repeats of the turbulence function in Z.

---
turbulenceOffsetX(tox): float
    properties: query, edit
    The translation of the turbulence function in X.

---
turbulenceOffsetY(toy): float
    properties: query, edit
    The translation of the turbulence function in Y.

---
turbulenceOffsetZ(toz): float
    properties: query, edit
    The translation of the turbulence function in Z.

---
turbulenceSpeed(trs): float
    properties: query, edit
    The rate of change of the turbulence over time.
The turbulence loops seamlessly every 1.0/turbulenceSpeed seconds.
To animate this rate attach a new time node to the time input
on the volumeAxisNode then animate the time value on the time node.

---
volumeExclusion(vex): boolean
    properties: query, edit
    Volume exclusion of the field.  If true, points outside the
volume (defined by the volume shape attribute) are affected,  If false,
points inside the volume are affected.  Has no effect if volumeShape
is set to "none."

---
volumeOffset(vof): [linear, linear, linear]
    properties: query, edit
    Volume offset of the field.  Volume offset translates
the field's volume by the specified amount from the actual
field location. This is in the field's local space.

---
volumeShape(vsh): string
    properties: query, edit
    Volume shape of the field.  Sets/edits/queries the
field's volume shape attribute.  If set to any value other
than "none", determines a 3-D volume within which the field has effect.
Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

---
volumeSweep(vsw): angle
    properties: query, edit
    Volume sweep of the field.  Applies only to sphere, cone,
cylinder, and torus.  Similar effect to the sweep attribute
in modelling.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/volumeAxis.html 
    """


def volumeBind(influence: string, name: string) -> list[string]:
    """Synopsis:
---
---
 volumeBind(
objects
    , [influence=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

volumeBind is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.volumeBind();

---
Return:
---


    list[string]: List of queried influences

Flags:
---


---
influence(inf): string
    properties: query, edit
    Edit or Query the list of influences connected to the skin cluster.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/volumeBind.html 
    """


def vortex(attenuation: float, axisX: float, axisY: float, axisZ: float, magnitude: float, maxDistance: linear, name: string, perVertex: boolean, position: tuple[linear, linear, linear], torusSectionRadius: linear, volumeExclusion: boolean, volumeOffset: tuple[linear, linear, linear], volumeShape: string, volumeSweep: angle) -> string:
    """Synopsis:
---
---
 vortex(
selectionList
    , [attenuation=float], [axisX=float], [axisY=float], [axisZ=float], [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

vortex is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
A vortex field pulls objects in a circular direction, like a whirlpool
or tornado.   Objects affected by the vortex field tend to rotate around
the axis specified by -ax, -ay, and -az.

The transform is the associated dependency node.
Use connectDynamic to cause the field to affect a dynamic object.

If fields are created, this command returns the names of each
of the fields. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If object names are provided or the active selection list is non-empty,
the command creates a field for every object in the list and calls
addDynamic to add it to the object. If the
list is empty, the command defaults to -pos 0 0 0.

Setting the -pos flag with objects named on the command line is an error.




Example:
---
import maya.cmds as cmds

cmds.vortex( ax=0, ay=1.0, az=0.5 )
Creates a vortex field with axis (0,1,0.5) for every active
selection. If there is no active
selection, it creates this field at world position (0,0,0).

---
Return:
---


    string: Command result

Flags:
---


---
attenuation(att): float
    properties: query, edit
    Attentuation rate of field

---
axisX(ax): float
    properties: query, edit
    X-component of vortex axis

---
axisY(ay): float
    properties: query, edit
    Y-component of vortex axis

---
axisZ(az): float
    properties: query, edit
    Z-component of vortex axis

---
magnitude(m): float
    properties: query, edit
    Strength of field.

---
maxDistance(mxd): linear
    properties: query, edit
    Maximum distance at which field is exerted.
-1 indicates that the field has no maximum distance.

---
name(n): string
    properties: query, edit
    name of field

---
perVertex(pv): boolean
    properties: query, edit
    Per-vertex application. If this flag is set true, then each
individual point (CV, particle, vertex,etc.) of the chosen object
exerts an identical copy of the force field. If this flag is set to
false, then the froce is exerted only from the geometric center of
the set of points.

---
position(pos): [linear, linear, linear]
    properties: query, edit, multiuse
    Position in space (x,y,z) where you want to place a gravity field.
The gravity then emanates from this position in space rather
than from an object. Note that you can both use -pos
(creating a field at a position) and also provide object names.

---
torusSectionRadius(tsr): linear
    properties: query, edit
    Section radius for a torus volume.  Applies only to torus.
Similar to the section radius in the torus modelling primitive.

---
volumeExclusion(vex): boolean
    properties: query, edit
    Volume exclusion of the field.  If true, points outside the
volume (defined by the volume shape attribute) are affected,  If false,
points inside the volume are affected.  Has no effect if volumeShape
is set to "none."

---
volumeOffset(vof): [linear, linear, linear]
    properties: query, edit
    Volume offset of the field.  Volume offset translates
the field's volume by the specified amount from the actual
field location. This is in the field's local space.

---
volumeShape(vsh): string
    properties: query, edit
    Volume shape of the field.  Sets/edits/queries the
field's volume shape attribute.  If set to any value other
than "none", determines a 3-D volume within which the field has effect.
Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."

---
volumeSweep(vsw): angle
    properties: query, edit
    Volume sweep of the field.  Applies only to sphere, cone,
cylinder, and torus.  Similar effect to the sweep attribute
in modelling.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/vortex.html 
    """
