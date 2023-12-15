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


def sampleImage(flagfastSample: boolean, flagresolution: tuple[int, name]) -> None:
    """Synopsis:
---
---
 sampleImage([fastSample=boolean], [resolution=[int, name]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sampleImage is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

From now on, render sample images at high quality.
---

cmds.sampleImage( f=False )

Render the sample image associated with lambert1 at a resolution of
128 pixels by 128 pixels.
---

cmds.sampleImage( r=(128, 'lambert1') )

---


Flags:
---


---
fastSample(f): boolean
    properties: create
    If fast but rough rendering for sampleImage is to be used

---
resolution(r): [int, name]
    properties: create
    The first argument to this flag specifies a resolution in pixels.
The second argument specifies a dependency node. The effect of this
flag is that further sample image renderings for the specified node
will be made at the specified resolution.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sampleImage.html 
    """


def saveAllShelves() -> boolean:
    """Synopsis:
---
---
 saveAllShelves(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveAllShelves is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

import maya.mel
gShelfTopLevel = maya.mel.eval('$tmpVar=$gShelfTopLevel')
cmds.saveAllShelves( gShelfTopLevel )

---
Return:
---


    boolean: True if successful, otherwise issues an error message and returns false.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveAllShelves.html 
    """


def saveFluid(flagcurrentTime: int, flagendTime: int, flagstartTime: int) -> None:
    """Synopsis:
---
---
 saveFluid([currentTime=int], [endTime=int], [startTime=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveFluid is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

save the current state to the initial conditions cache
cmds.saveFluid()

---


Flags:
---


---
currentTime(ct): int
    properties: create, query, edit
    cache state of fluid at current time

---
endTime(et): int
    properties: create, query, edit
    end Time for cacheing

---
startTime(st): int
    properties: create, query, edit
    start Time for cacheing

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveFluid.html 
    """


def saveImage(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcurrentView: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagimage: string, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagobjectThumbnail: string, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagsceneFile: string, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 saveImage(
[imageName]
[imageName]
    , [annotation=string], [backgroundColor=[float, float, float]], [currentView=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [objectThumbnail=string], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [sceneFile=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveImage is undoable, queryable, and editable.
This command creates a static image control for non-xpm files used to
display a thumbnail image of the scene file.




Example:
---
import maya.cmds as cmds

   Note that for this example to work you must substitute
   "image" below with the full path name to a valid image.
---

window = cmds.window()
cmds.paneLayout()
cmds.image( image='image' )
cmds.showWindow( window )

window = cmds.window('window')
cmds.paneLayout()
cmds.saveImage( currentView=True )
cmds.showWindow( window )

When rendering shaded images, in lieu of using the saveImage command, execute the following
script to take a snapshot of the current scene view and save it as an endSnapshot.jpg file
to the images directory of your project directory.
This workaround can be used for both the default viewport and Viewport 2.0.

import maya.cmds as cmds
Set up workspace for images in current project
ws = cmds.workspace(q = True, fullName = True)
wsp = ws + "/" + "images"
cmds.sysFile(wsp, makeDir=True)

Prepare unique image name for snapshot
imageSnapshot = wsp + "/" + "endSnapshot.jpg"

Take a snapshot of the viewport and save to file
cmds.refresh(cv=True, fe = "jpg", fn = imageSnapshot)

---
Return:
---


    string: The name of the image created.
    string: The name of the saveImage control created.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
currentView(cv): boolean
    properties: edit
    Generate the image from the current view.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
image(i): string
    properties: create, query, edit
    Sets the image given the file name.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
objectThumbnail(ot): string
    properties: edit
    Use an image of the named object, if possible.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
sceneFile(sf): string
    properties: edit
    The name of the file that the icon is to be associated with.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveImage.html 
    """


def saveInitialState(flagattribute: string, flagsaveall: boolean) -> string:
    """Synopsis:
---
---
 saveInitialState(
selectionList
    , [attribute=string], [saveall=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveInitialState is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.saveInitialState( 'particle1' )
Saves current state as initial state for particle1.

cmds.saveInitialState( all=True )
Saves current state as initial state for all dynamics objects.

---
Return:
---


    string: Command result

Flags:
---


---
attribute(atr): string
    properties: create, multiuse
    Save the initial state of the specified attribute only.
This is a multi-use flag.

---
saveall(all): boolean
    properties: create
    Save the initial state for all dynamics objects in the scene.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveInitialState.html 
    """


def saveMenu() -> string:
    """Synopsis:
---
---
 saveMenu(
string string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveMenu is undoable, NOT queryable, and NOT editable.
Note that this command is used solely by the Marking Menu Editor
and is not intended to be used for general purposes.

Note that this command doesn't work well with controls that have
mixed mel and python command callbacks.  Also, because it saves the menu
state to a mel file, it does not work with callbacks that are python
callable objects.

The first argument is the name of the manu to save, the second one is
the name of the file.




Example:
---
import maya.cmds as cmds

Create a window with two frames.
---

win = cmds.window(title='saveMenu Example')
cmds.columnLayout()
frame1 = cmds.frameLayout( h=90, l='Original Menu (LMB)' )
cmds.text( l='(click here)' )
cmds.setParent( '..' )
frame2 = cmds.frameLayout( h=90, l='Copy of Original (LMB)' )
cmds.text( l='(click here)' )
cmds.setParent( '..' )

Create a menu.
---

menu1 = cmds.popupMenu( parent=frame1, b=1, mm=True )

cmds.menuItem( rp='N', l='Up' )
cmds.menuItem( rp='S', l='Down' )
cmds.menuItem( rp='E', l='Right' )
cmds.menuItem( rp='W', l='Left' )
cmds.menuItem( label='Warm', sm=True )
cmds.menuItem( l='Red' )
cmds.menuItem( l='Orange' )
cmds.menuItem( l='Yellow' )
cmds.setParent( '..', m=True )
cmds.menuItem( label='Cold', sm=True )
cmds.menuItem( l='Green' )
cmds.menuItem( l='Blue' )
cmds.menuItem( l='Indigo' )
cmds.menuItem( l='Violet' )
cmds.setParent( '..', m=True )
cmds.setParent( '..', m=True )

Save the menu to a file.
---

result = cmds.saveMenu(menu1, 'menu_example')

Use the file to rebuild another instance of the menu.
---

menu1 = cmds.popupMenu( parent=frame2, b=1, mm=True )
maya.mel.eval( 'source \"' + cmds.internalVar(userMarkingMenuDir=True) + 'menu_example.mel\"' )

Finish up.
print ("The menu was saved in [" + cmds.internalVar(userMarkingMenuDir=True) + result + "]\n" )
cmds.showWindow( win )

---
Return:
---


    string: The name of the saved file.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveMenu.html 
    """


def savePrefObjects() -> boolean:
    """Synopsis:
---
---
 savePrefObjects()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

savePrefObjects is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.savePrefObjects()

---
Return:
---


    boolean: True if successful.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/savePrefObjects.html 
    """


def savePrefs(flagcolors: boolean, flagfile: string, flaggeneral: boolean, flaghotkeys: boolean, flagmenuSets: boolean, flagplugins: boolean, flaguiLayout: boolean) -> None:
    """Synopsis:
---
---
 savePrefs([colors=boolean], [file=string], [general=boolean], [hotkeys=boolean], [menuSets=boolean], [plugins=boolean], [uiLayout=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

savePrefs is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

only save the hotkeys
cmds.savePrefs( hotkeys=True )

save everything
cmds.savePrefs()

only save ui layout prefs
cmds.savePrefs( uiLayout=True )

---


Flags:
---


---
colors(c): boolean
    properties: create
    Save the color prefs to disk

---
file(f): string
    properties: create
    Save a specific preference file. Used to save preferences that
are using optionVar -prefFile to save items to a different file.

---
general(g): boolean
    properties: create
    Save the general prefs to disk (optionVars)

---
hotkeys(hk): boolean
    properties: create
    Save the hotkeys to disk

---
menuSets(ms): boolean
    properties: create
    Save the menuSet preferences to disk

---
plugins(pl): boolean
    properties: create
    Save the plug-in prefs to disk

---
uiLayout(ui): boolean
    properties: create
    Save each window's size and position to disk

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/savePrefs.html 
    """


def saveShelf() -> boolean:
    """Synopsis:
---
---
 saveShelf(
string string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveShelf is undoable, NOT queryable, and NOT editable.
Note that this command doesn't work well with controls that have
mixed mel and python command callbacks.  Also, because it saves the
state to a mel file, it does not work with callbacks that are python
callable objects.




Example:
---
import maya.cmds as cmds

   Create a window with a shelf in it.
---

window = cmds.window()
tabs = cmds.tabLayout()
shelf = cmds.shelfLayout()
cmds.shelfButton( '\"Hello\\n\"")', image1='commandButton.png', command='("print' )
cmds.tabLayout( tabs, edit=True, tabLabel=(str(shelf),'Example Shelf')  )
cmds.showWindow( window )

   At this point the example would be made more interesting if you
   put some additional items on this shelf.

   Now save the shelf in the temp directory.
---

tempDir = cmds.internalVar( userTmpDir=True )
cmds.saveShelf( shelf, (tempDir + 'ExampleShelf') );

---
Return:
---


    boolean: True if successful.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveShelf.html 
    """


def saveToolSettings() -> None:
    """Synopsis:
---
---
 saveToolSettings()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveToolSettings is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.saveToolSettings()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveToolSettings.html 
    """


def saveViewportSettings() -> None:
    """Synopsis:
---
---
 saveViewportSettings()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

saveViewportSettings is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.saveViewportSettings()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/saveViewportSettings.html 
    """


def scale(flagabsolute: boolean, flagcenterPivot: boolean, flagcomponentSpace: boolean, flagconstrainAlongNormal: boolean, flagdeletePriorHistory: boolean, flagdistanceOnly: boolean, flaglocalSpace: boolean, flagobjectCenterPivot: boolean, flagobjectSpace: boolean, flagorientAxes: tuple[angle, angle, angle], flagpivot: tuple[linear, linear, linear], flagpreserveChildPosition: boolean, flagpreserveGeometryPosition: boolean, flagpreserveUV: boolean, flagreflection: boolean, flagreflectionAboutBBox: boolean, flagreflectionAboutOrigin: boolean, flagreflectionAboutX: boolean, flagreflectionAboutY: boolean, flagreflectionAboutZ: boolean, flagreflectionTolerance: float, flagrelative: boolean, flagscaleX: boolean, flagscaleXY: boolean, flagscaleXYZ: boolean, flagscaleXZ: boolean, flagscaleY: boolean, flagscaleYZ: boolean, flagscaleZ: boolean, flagsymNegative: boolean, flagworldSpace: boolean, flagxformConstraint: string) -> None:
    """Synopsis:
---
---
 scale(
float float float [objects]
    , [absolute=boolean], [centerPivot=boolean], [componentSpace=boolean], [constrainAlongNormal=boolean], [deletePriorHistory=boolean], [distanceOnly=boolean], [localSpace=boolean], [objectCenterPivot=boolean], [objectSpace=boolean], [orientAxes=[angle, angle, angle]], [pivot=[linear, linear, linear]], [preserveChildPosition=boolean], [preserveGeometryPosition=boolean], [preserveUV=boolean], [reflection=boolean], [reflectionAboutBBox=boolean], [reflectionAboutOrigin=boolean], [reflectionAboutX=boolean], [reflectionAboutY=boolean], [reflectionAboutZ=boolean], [reflectionTolerance=float], [relative=boolean], [scaleX=boolean], [scaleXY=boolean], [scaleXYZ=boolean], [scaleXZ=boolean], [scaleY=boolean], [scaleYZ=boolean], [scaleZ=boolean], [symNegative=boolean], [worldSpace=boolean], [xformConstraint=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scale is undoable, NOT queryable, and NOT editable.
The default behaviour, when no objects or flags are passed,
is to do a relative scale on each currently selected object
object using each object's existing scale pivot point.




Example:
---
import maya.cmds as cmds

cmds.scale( 1, 1, 1 )
cmds.scale( 3, 3, 3, 'curve1', pivot=(1, 0, 0), absolute=True )

---


Flags:
---


---
absolute(a): boolean
    properties: create
    Perform an absolute operation.

---
centerPivot(cp): boolean
    properties: create
    Let the pivot be the center of the bounding box of all objects

---
componentSpace(cs): boolean
    properties: create
    Move in local component space

---
constrainAlongNormal(xn): boolean
    properties: create
    When true, transform constraints are applied along the vertex normal first
and only use the closest point when no intersection is found along the normal.

---
deletePriorHistory(dph): boolean
    properties: create
    If true then delete the history prior to the current operation.

---
distanceOnly(dso): boolean
    properties: create
    Scale only the distance between the objects.

---
localSpace(ls): boolean
    properties: create
    Use local space for scaling

---
objectCenterPivot(ocp): boolean
    properties: create
    Let the pivot be the center of the bounding box of each object

---
objectSpace(os): boolean
    properties: create
    Use object space for scaling

---
orientAxes(oa): [angle, angle, angle]
    properties: create
    Use the angles for the orient axes.

---
pivot(p): [linear, linear, linear]
    properties: create
    Define the pivot point for the transformation

---
preserveChildPosition(pcp): boolean
    properties: create
    When true, transforming an object will apply an opposite transform to its
child transform to keep them at the same world-space position.
Default is false.

---
preserveGeometryPosition(pgp): boolean
    properties: create
    When true, transforming an object will apply an opposite transform to its
geometry points to keep them at the same world-space position.
Default is false.

---
preserveUV(puv): boolean
    properties: create
    When true, UV values on scaled components are projected along the axis of
scaling in 3d space. For small edits, this will freeze the world space texture
mapping on the object.
When false, the UV values will not change for a selected vertices.
Default is false.

---
reflection(rfl): boolean
    properties: create
    To move the corresponding symmetric components also.

---
reflectionAboutBBox(rab): boolean
    properties: create
    Sets the position of the reflection axis  at the geometry bounding box

---
reflectionAboutOrigin(rao): boolean
    properties: create
    Sets the position of the reflection axis  at the origin

---
reflectionAboutX(rax): boolean
    properties: create
    Specifies the X=0 as reflection plane

---
reflectionAboutY(ray): boolean
    properties: create
    Specifies the Y=0 as reflection plane

---
reflectionAboutZ(raz): boolean
    properties: create
    Specifies the Z=0 as reflection plane

---
reflectionTolerance(rft): float
    properties: create
    Specifies the tolerance to findout the corresponding reflected components

---
relative(r): boolean
    properties: create
    Perform a operation relative to the object's current position

---
scaleX(x): boolean
    properties: create
    Scale in X direction

---
scaleXY(xy): boolean
    properties: create
    Scale in X and Y direction

---
scaleXYZ(xyz): boolean
    properties: create
    Scale in all directions (default)

---
scaleXZ(xz): boolean
    properties: create
    Scale in X and Z direction

---
scaleY(y): boolean
    properties: create
    Scale in Y direction

---
scaleYZ(yz): boolean
    properties: create
    Scale in Y and Z direction

---
scaleZ(z): boolean
    properties: create
    Scale in Z direction

---
symNegative(smn): boolean
    properties: create
    When set the component transformation is flipped so it is relative to the
negative side of the symmetry plane. The default (no flag) is to transform
components relative to the positive side of the symmetry plane.

---
worldSpace(ws): boolean
    properties: create
    Use world space for scaling

---
xformConstraint(xc): string
    properties: create
    Apply a transform constraint to moving components.

none - no constraint
surface - constrain components to the surface
edge - constrain components to surface edges
live - constraint components to the live surface

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scale.html 
    """


def scaleComponents(flagpivot: tuple[linear, linear, linear], flagrotation: tuple[angle, angle, angle]) -> None:
    """Synopsis:
---
---
 scaleComponents(
float float float [objects]
    , [pivot=[linear, linear, linear]], [rotation=[angle, angle, angle]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scaleComponents is undoable, NOT queryable, and NOT editable.
This allows selected components to be scaled in any arbitrary
space, not just object or world space as the regular scale
allows.

Scale values are always relative, not absolute.




Example:
---
import maya.cmds as cmds

cmds.scaleComponents( 2, 2, 2, pivot=(0, 10, 0), rotation=(30, 40, 50) )

---


Flags:
---


---
pivot(p): [linear, linear, linear]
    properties: create
    The pivot position in world space (default is origin)

---
rotation(ro): [angle, angle, angle]
    properties: create
    The rotational offset for the scaling (default is none)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scaleComponents.html 
    """


def scaleConstraint(flaglayer: string, flagmaintainOffset: boolean, flagname: string, flagoffset: tuple[float, float, float], flagremove: boolean, flagscaleCompensate: boolean, flagskip: string, flagtargetList: boolean, flagweight: float, flagweightAliasList: boolean) -> list[string]:
    """Synopsis:
---
---
 scaleConstraint(
[target...] [object]
    , [layer=string], [maintainOffset=boolean], [name=string], [offset=[float, float, float]], [remove=boolean], [scaleCompensate=boolean], [skip=string], [targetList=boolean], [weight=float], [weightAliasList=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scaleConstraint is undoable, queryable, and editable.
A scaleConstraint takes as input one or more "target" DAG
transform nodes to which to scale the single "constraint
object" DAG transform node.  The scaleConstraint scales the
constrained object at the weighted geometric mean of the
world space target scale factors.




Example:
---
import maya.cmds as cmds

Scale cube1 at the scale of cone1.
cmds.scaleConstraint( 'cone1', 'cube1' )

Uses the average of the scale of cone1 and surf2.
cmds.scaleConstraint( 'cone1', 'surf2', 'cube2', w=.1 )

Sets the weight for cone1's effect on cube2 to 10.
cmds.scaleConstraint( 'cone1', 'cube2', e=True, w=10.0 )

Removes surf2 from cube2's scaleConstraint
cmds.scaleConstraint( 'surf2', 'cube2', e=True, rm=True )

Adds surf3 to cube2's scaleConstraint with the default weight
cmds.scaleConstraint( 'surf3', 'cube2' )

Constrain the x and z scale of sph2 to sph1
cmds.scaleConstraint( 'sph1', 'sph2', skip="y" )

---
Return:
---


    list[string]: Name of the created constraint node

Flags:
---


---
layer(l): string
    properties: create, edit
    Specify the name of the animation layer where the constraint should be added.

---
maintainOffset(mo): boolean
    properties: create
    The offset necessary to preserve the constrained
object's initial scale will be calculated and used as the
offset.

---
name(n): string
    properties: create, query, edit
    Sets the name of the constraint node to the specified
name.  Default name is constrainedObjectName_constraintType

---
offset(o): [float, float, float]
    properties: create, query, edit
    Sets or queries the value of the offset. Default is 1,1,1.

---
remove(rm): boolean
    properties: edit
    removes the listed target(s) from the constraint.

---
scaleCompensate(sc): boolean
    properties: create, edit
    Used only when constraining a joint. It specify if a scaleCompensate will be applied on constrained joint.
If true it will connect Tjoint.aCompensateForParentScale to scaleContraint.aConstraintScaleCompensate.

---
skip(sk): string
    properties: create, edit, multiuse
    Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.

---
targetList(tl): boolean
    properties: query
    Return the list of target objects.

---
weight(w): float
    properties: create, query, edit
    Sets the weight value for the specified target(s).
If not given at creation time, the default value of 1.0 is used.

---
weightAliasList(wal): boolean
    properties: query
    Returns the names of the attributes that control the weight
of the target objects. Aliases are returned in the same order
as the targets are returned by the targetList flag

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scaleConstraint.html 
    """


def scaleKey(flaganimation: string, flagattribute: string, flagautoSnap: boolean, flagcontrolPoints: boolean, flagfloat: floatrange, flagfloatPivot: float, flagfloatScale: float, flaghierarchy: string, flagincludeUpperBound: boolean, flagindex: uint, flagnewEndFloat: float, flagnewEndTime: time, flagnewStartFloat: float, flagnewStartTime: time, flagscaleSpecifiedKeys: boolean, flagshape: boolean, flagtime: timerange, flagtimePivot: time, flagtimeScale: float, flagvaluePivot: float, flagvalueScale: float) -> int:
    """Synopsis:
---
---
 scaleKey(
objects
    , [animation=string], [attribute=string], [autoSnap=boolean], [controlPoints=boolean], [float=floatrange], [floatPivot=float], [floatScale=float], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [newEndFloat=float], [newEndTime=time], [newStartFloat=float], [newStartTime=time], [scaleSpecifiedKeys=boolean], [shape=boolean], [time=timerange], [timePivot=time], [timeScale=float], [valuePivot=float], [valueScale=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scaleKey is undoable, NOT queryable, and NOT editable.
The animation curves comprising a keyset depend on the value
of the "-animation" flag:


keysOrObjects:

Any active keys, when no target objects or -attribute
flags appear on the command line, or

All animation curves connected to all keyframable
attributes of objects specified as the command line's
targetList, when there are no active keys.




keys:
Only act on active keys or tangents.
If there are no active keys or tangents, don't do anything.



objects:
Only act on specified objects.  If there are no objects specified, don't
do anything.



Note that the "-animation" flag can be used to override
the curves uniquely identified by the multi-use
"-attribute" flag, which takes an argument of the form
attributeName, such as "translateX".

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given individually or as part of a list or range (see Examples).

This command takes keyframes at (or within) the specified times (or time ranges)
and scales them.  If no times are specified, the scale is applied to active keyframes
or (if no keys are active) all keys of active objects.

This command has two sets of flags for scaling in time/x-axis. One set of flags is
for time-based animation curves, and the other set of flags is for float-based (unitless) animation curves.
Most animation curves in Maya are time-based. Unitless animation curves are less common.
Use the set of flags that corresponds to the type of animation curves being scaled.

To scale all selected animation curves regardless of their type, use both sets of flags.




Example:
---
import maya.cmds as cmds

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given as a range or list of ranges.

time=('10pal','10pal') means the key at frame 10 (PAL format).
time=[('1.0sec','1.0sec'),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
time=(10,None) means all keys from time 10 (in the current time unit) onwards.
time=(10,) means the same as (10,10)
time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
time=(None,None) is a short form to specify all keys.
index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.

Scale keyframes from frame 10 to 20 of nurbsSphere1's translateX
to fill frames 10 to 30.
---

cmds.scaleKey( 'nurbsSphere1', time=(10,20), newStartTime=10, newEndTime=30, attribute='tx' )

Scale all the animation of the active objects
(range 0-30) to fill range 0 to 60.
---

cmds.scaleKey( time=(0,30), timeScale=2, timePivot=0 )

---
Return:
---


    int: Number of curves on which scale was performed

Flags:
---


---
animation(an): string
    properties: create
    Where this command should get the animation to act
on.  Valid values are "objects," "keys," and
"keysOrObjects" Default: "keysOrObjects."  (See
Description for details.)

---
attribute(at): string
    properties: create, multiuse
    List of attributes to select
      In query mode, this flag needs a value.

---
autoSnap(asp): boolean
    properties: create
    Auto snap scaled keys if True.
Default value depend on scaleKeyAutoSnap option

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
float(f): floatrange
    properties: create, multiuse
    value uniquely representing a non-time-based
key (or key range) on a time-based animCurve.  Valid
floatRange include single values (-f 10) or a
string with a lower and upper bound, separated by a
colon (-f "10:20")
      In query mode, this flag needs a value.

---
floatPivot(fp): float
    properties: create
    Scale pivot along the x-axis for float-based (unitless) animCurves

---
floatScale(fs): float
    properties: create
    Amount to scale along the x-axis for float-based (unitless) animation curves
animCurves

---
hierarchy(hi): string
    properties: create
    Hierarchy expansion options.  Valid values are "above,"
"below," "both," and "none." (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
includeUpperBound(iub): boolean
    properties: create
    When the -t/time or -f/float flags represent a range
of keys, this flag determines whether the keys at the
upper bound of the range are included in the keyset.
Default value: true.  This flag is only valid when
the argument to the -t/time flag is a time range with
a lower and upper bound.  (When used with the "pasteKey"
command, this flag refers only to the time range of the
target curve that is replaced, when using options such
as "replace," "fitReplace," or "scaleReplace."  This
flag has no effect on the curve pasted from the clipboard.)

---
index(index): uint
    properties: create, multiuse
    index of a key on an animCurve
      In query mode, this flag needs a value.

---
newEndFloat(nef): float
    properties: create
    The end of the float range to which the float-based (unitless) animation curves should be scaled.

---
newEndTime(net): time
    properties: create
    The end of the time range to which the time-based animation curves should be scaled.

---
newStartFloat(nsf): float
    properties: create
    The start of the float range to which the float-based (unitless) animation curves should be scaled.

---
newStartTime(nst): time
    properties: create
    The start of the time range to which the time-based animation curves should be scaled.

---
scaleSpecifiedKeys(ssk): boolean
    properties: create
    Determines if only the specified keys are affected by the scale.
If false, other keys may be adjusted with the scale. The
default is true.

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

---
timePivot(tp): time
    properties: create
    Scale pivot along the time-axis for time-based animation curves

---
timeScale(ts): float
    properties: create
    Amount to scale along the time-axis for time-based animation curves

---
valuePivot(vp): float
    properties: create
    Scale pivot along the value-axis

---
valueScale(vs): float
    properties: create
    Amount of scale along the value-axis

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scaleKey.html 
    """


def scaleKeyCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagscaleSpecifiedKeys: boolean, flagtype: string) -> boolean | string:
    """Synopsis:
---
---
 scaleKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [scaleSpecifiedKeys=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scaleKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a manipulator style scale key context for the graph editor
---

cmds.scaleKeyCtx( 'scaleKeyContext', type='rect' )

---
Return:
---


    string: Scale type, if the type flag was queried
    boolean: Whether specified keys should be scaled, if the scaleSpecifiedKeys flag was queried

Flags:
---


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
scaleSpecifiedKeys(ssk): boolean
    properties: query, edit
    Determines if only the specified keys should be scaled. If false,
the non-selected keys will be adjusted during the scale. The default
is true.

---
type(typ): string
    properties: query, edit
    rect | manip
Specifies the type of scale manipulator to use
(Note: "rect" is a manipulator style context, and "manip"
is a gestural style context)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scaleKeyCtx.html 
    """


def sceneEditor(flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaghighlightConnection: string, flaglockMainConnection: boolean, flagmainListConnection: string, flagonlyParents: boolean, flagpanel: string, flagparent: string, flagrefreshReferences: boolean, flagselectCommand: script, flagselectItem: int, flagselectReference: string, flagselectionConnection: string, flagshortName: boolean, flagstateString: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagunresolvedName: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string, flagwithoutCopyNumber: boolean) -> string:
    """Synopsis:
---
---
 sceneEditor([control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightConnection=string], [lockMainConnection=boolean], [mainListConnection=string], [onlyParents=boolean], [panel=string], [parent=string], [refreshReferences=boolean], [selectCommand=script], [selectItem=int], [selectReference=string], [selectionConnection=string], [shortName=boolean], [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean], [unresolvedName=boolean], [updateMainConnection=boolean], [useTemplate=string], [withoutCopyNumber=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sceneEditor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.paneLayout()
cmds.sceneEditor()
cmds.showWindow(window)

---
Return:
---


    string: Name of editor.

Flags:
---


---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
filter(f): string
    properties: create, query, edit
    Specifies the name of an itemFilter object to be used with this editor.
This filters the information coming onto the main list
of the editor.

---
forceMainConnection(fmc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will only
display items contained in the selectionConnection object. This is
a variant of the -mainListConnection flag in that it will force a
change even when the connection is locked. This flag is used to
reduce the overhead when using the -unlockMainConnection
, -mainListConnection, -lockMainConnection flags in immediate
succession.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
onlyParents(op): boolean
    properties: query
    When used with the 'selectItem' or 'selectReference' queries it
indicates that, if both a parent and a child file or reference
are selected, only the parent will be returned.

---
panel(pnl): string
    properties: create, query
    Specifies the panel for this editor. By default if
an editor is created in the create callback of a scripted panel it
will belong to that panel. If an editor does not belong to a panel
it will be deleted when the window that it is in is deleted.

---
parent(p): string
    properties: create, query, edit
    Specifies the parent layout for this editor. This flag will only
have an effect if the editor is currently un-parented.

---
refreshReferences(rr): boolean
    properties: edit
    Force refresh of references

---
selectCommand(sc): script
    properties: create, query, edit
    A script to be executed when an item is selected.

---
selectItem(si): int
    properties: query, edit
    Query or change the currently selected item. When queried, the
currently selected file name will be return.

---
selectReference(sr): string
    properties: query
    Query the currently selected reference. Returns the name of the
currently selected reference node.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
shortName(shn): boolean
    properties: query
    When used with the 'selectItem' query it indicates that the file name
returned will be the short name (i.e. just a file name without
any directory paths). If this flag is not present, the full name
and directory path will be returned.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
unParent(up): boolean
    properties: create, edit
    Specifies that the editor should be removed from its layout.
This cannot be used in query mode.

---
unlockMainConnection(ulk): boolean
    properties: create, edit
    Unlocks the mainConnection, effectively restoring the original
mainConnection (if it is still available), and dynamic updates.

---
unresolvedName(un): boolean
    properties: query
    When used with the 'selectItem' query it indicates that the file name
returned will be unresolved (i.e. it will be the path originally
specified when the file was loaded into Maya; this path may
contain environment variables and may not exist on disk). If this
flag is not present, the resolved name will    be returned.

---
updateMainConnection(upd): boolean
    properties: create, edit
    Causes a locked mainConnection to be updated from the orginal
mainConnection, but preserves the lock state.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
withoutCopyNumber(wcn): boolean
    properties: query
    When used with the 'selectItem' query it indicates that the file name
returned will not have a copy number appended to the end. If this
flag is not present, the file name returned may have a copy number
appended to the end.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sceneEditor.html 
    """


def sceneLint(flagissueType: string, flagverbose: boolean) -> list[string] | string:
    """Synopsis:
---
---
 sceneLint([issueType=string], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sceneLint is NOT undoable, queryable, and NOT editable.
The sceneLint command is used to analyze the currently loaded scene
to find potential areas for improvement in performance, memory use, or reduction
of clutter.


In the query mode it will report back the list of available checks it can do.
Each check will have an associated short-form which can be passed to the command
to run specific checks.


In create mode the returned string is a JSON format list of issues and mitigations
that suggest a way to solve the problem it describes.


Mitigation can be automatically performed by extracting the mitigation code and arguments
then running the Python code exec(code, {}, {'OBJECTS' : objects})



Example:
---
import maya.cmds as cmds

Query the list of available issue types
cmds.sceneLint( query=True )
Return: ['FOO', 'BAR', 'BAZ'] ---


Find all scene issues
cmds.sceneLint()
Return: '{ "sceneLint" : ... }' ---


Get more information on the "FOO" issue type
cmds.sceneLint( issueTye=['FOO','BAR'], query=True )
Return: ['FOO', 'FOO_DESCRIPTION', 'BAR', 'BAR_DESCRIPTION'] ---


Run only the "FOO" issue check
cmds.sceneLint( issueTye='FOO' )
Return: '{ "sceneLint" : ... }' ---


---
Return:
---


    string: JSON formatted results showing the issues that could potentially cause problems in the scene.
    list[string]: When querying issueType shows the description, and benefit values for the named scene issue.
    list[string]: When querying returns the list of all issueTypes by name.

Flags:
---


---
issueType(i): string
    properties: create, query, multiuse
    Specify a set of issue types to be checked. If omitted then all known issue types are checked.
In query mode returns a description of what a particular issue type is checking.
                        In query mode, this flag can accept a value.

---
verbose(v): boolean
    properties: create, query
    If set then include both name and description when querying the list of available issue types.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sceneLint.html 
    """


def sceneUIReplacement(flagclear: boolean, flagdeleteRemaining: boolean, flaggetNextFilter: tuple[string, string], flaggetNextPanel: tuple[string, string], flaggetNextScriptedPanel: tuple[string, string], flagupdate: string) -> string:
    """Synopsis:
---
---
 sceneUIReplacement([clear=boolean], [deleteRemaining=boolean], [getNextFilter=[string, string]], [getNextPanel=[string, string]], [getNextScriptedPanel=[string, string]], [update=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sceneUIReplacement is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

import maya.mel as mm
gMainPane = mm.eval( 'global string $gMainPane; $temp = $gMainPane;' )
cmds.sceneUIReplacement( update=gMainPane )

Try to find the modelPanel named Top View
cmds.sceneUIReplacement( getNextPanel=('modelPanel','Top View') )
Result: modelPanel1 ---

cmds.modelPanel( 'modelPanel1', q=True, label=True )
Result: Top View ---


Try to find Front View
cmds.sceneUIReplacement( getNextPanel=('modelPanel', 'Front View') )
Result: modelPanel3 ---

cmds.modelPanel( 'modelPanel3', q=True, label=True )
Result: Front View ---


Is there another Front View?  (No: all we find is a model panel called Persp View)
cmds.sceneUIReplacement( getNextPanel=('modelPanel', 'Front View') )
Result: modelPanel4
cmds.modelPanel( 'modelPanel4', q=True, label=True )
Result: Persp View

---
Return:
---


    string: When used with getNextScriptedPanel, getNextPanel, or getNextFilter

Flags:
---


---
clear(cl): boolean
    properties: create
    Frees any resources allocated by the command.

---
deleteRemaining(dr): boolean
    properties: create
    Delete any UI that is scene dependent and has not been referenced by
this command since the last update.

---
getNextFilter(gf): [string, string]
    properties: create
    Returns the next filter of the specified type with the specified name.

---
getNextPanel(gp): [string, string]
    properties: create
    Returns the next panel of the specified type, preferably with the
specified label.

---
getNextScriptedPanel(gsp): [string, string]
    properties: create
    Returns the next scripted panel of the specified scripted panel type,
preferably with the specified label.

---
update(u): string
    properties: create
    Updates the state of the command to reflect the current state
of the application.  The string argument is the name of the
main window pane layout holding the panels.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sceneUIReplacement.html 
    """


def scmh(flagabsolute: boolean, flagignore: uint, flagquiet: boolean, flagrelative: boolean) -> None:
    """Synopsis:
---
---
 scmh(
float [float...]
    , [absolute=boolean], [ignore=uint], [quiet=boolean], [relative=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scmh is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a new move manip context, set the active handle to X axis handle, then swith to it
cmds.manipMoveContext('manipMoveContext1', ah=0)
cmds.setToolTo('manipMoveContext1')

Set the active handle value to 10.(Translate the pSphere1 by (10, 0, 0))
cmds.scmh(10, r=True)

---


Flags:
---


---
absolute(a): boolean
    properties: create
    The values are absolute

---
ignore(i): uint
    properties: create, multiuse
    This is a multiuse flag which specifies that the index-th (1-based)
entry is to be ignored

---
quiet(q): boolean
    properties: create
    This flag suppresses all error messages

---
relative(r): boolean
    properties: create
    The values are relative

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scmh.html 
    """


def scriptCtx(flagallComponents: boolean, flagallObjects: boolean, flaganimBreakdown: boolean, flaganimCurve: boolean, flaganimInTangent: boolean, flaganimKeyframe: boolean, flaganimOutTangent: boolean, flagbaseClassName: string, flagcamera: boolean, flagcluster: boolean, flagcollisionModel: boolean, flagcontrolVertex: boolean, flagcumulativeLists: boolean, flagcurve: boolean, flagcurveKnot: boolean, flagcurveOnSurface: boolean, flagcurveParameterPoint: boolean, flagdimension: boolean, flagdynamicConstraint: boolean, flagedge: boolean, flageditPoint: boolean, flagemitter: boolean, flagenableRootSelection: boolean, flagescToQuit: boolean, flagexists: boolean, flagexitUponCompletion: boolean, flagexpandSelectionList: boolean, flagfacet: boolean, flagfield: boolean, flagfinalCommandScript: script, flagfluid: boolean, flagfollicle: boolean, flagforceAddSelect: boolean, flaghairSystem: boolean, flaghandle: boolean, flaghistory: boolean, flaghull: boolean, flagignoreInvalidItems: boolean, flagikEndEffector: boolean, flagikHandle: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagimagePlane: boolean, flagimplicitGeometry: boolean, flagisoparm: boolean, flagjoint: boolean, flagjointPivot: boolean, flaglastAutoComplete: boolean, flaglattice: boolean, flaglatticePoint: boolean, flaglight: boolean, flaglocalRotationAxis: boolean, flaglocator: boolean, flaglocatorUV: boolean, flaglocatorXYZ: boolean, flagnCloth: boolean, flagnParticle: boolean, flagnParticleShape: boolean, flagnRigid: boolean, flagname: string, flagnonlinear: boolean, flagnurbsCurve: boolean, flagnurbsSurface: boolean, flagobjectComponent: boolean, flagorientationLocator: boolean, flagparticle: boolean, flagparticleShape: boolean, flagplane: boolean, flagpolymesh: boolean, flagpolymeshEdge: boolean, flagpolymeshFace: boolean, flagpolymeshFreeEdge: boolean, flagpolymeshUV: boolean, flagpolymeshVertex: boolean, flagpolymeshVtxFace: boolean, flagrigidBody: boolean, flagrigidConstraint: boolean, flagrotatePivot: boolean, flagscalePivot: boolean, flagsculpt: boolean, flagselectHandle: boolean, flagsetAllowExcessCount: boolean, flagsetAutoComplete: boolean, flagsetAutoToggleSelection: boolean, flagsetDoneSelectionPrompt: string, flagsetNoSelectionHeadsUp: string, flagsetNoSelectionPrompt: string, flagsetSelectionCount: int, flagsetSelectionHeadsUp: string, flagsetSelectionPrompt: string, flagshowManipulators: boolean, flagspring: boolean, flagspringComponent: boolean, flagstroke: boolean, flagsubdiv: boolean, flagsubdivMeshEdge: boolean, flagsubdivMeshFace: boolean, flagsubdivMeshPoint: boolean, flagsubdivMeshUV: boolean, flagsurfaceEdge: boolean, flagsurfaceFace: boolean, flagsurfaceKnot: boolean, flagsurfaceParameterPoint: boolean, flagsurfaceRange: boolean, flagsurfaceUV: boolean, flagtexture: boolean, flagtitle: string, flagtoolCursorType: string, flagtoolFinish: script, flagtoolStart: script, flagtotalSelectionSets: int, flagvertex: boolean) -> string:
    """Synopsis:
---
---
 scriptCtx(
string
    , [allComponents=boolean], [allObjects=boolean], [animBreakdown=boolean], [animCurve=boolean], [animInTangent=boolean], [animKeyframe=boolean], [animOutTangent=boolean], [baseClassName=string], [camera=boolean], [cluster=boolean], [collisionModel=boolean], [controlVertex=boolean], [cumulativeLists=boolean], [curve=boolean], [curveKnot=boolean], [curveOnSurface=boolean], [curveParameterPoint=boolean], [dimension=boolean], [dynamicConstraint=boolean], [edge=boolean], [editPoint=boolean], [emitter=boolean], [enableRootSelection=boolean], [escToQuit=boolean], [exists=boolean], [exitUponCompletion=boolean], [expandSelectionList=boolean], [facet=boolean], [field=boolean], [finalCommandScript=script], [fluid=boolean], [follicle=boolean], [forceAddSelect=boolean], [hairSystem=boolean], [handle=boolean], [history=boolean], [hull=boolean], [ignoreInvalidItems=boolean], [ikEndEffector=boolean], [ikHandle=boolean], [image1=string], [image2=string], [image3=string], [imagePlane=boolean], [implicitGeometry=boolean], [isoparm=boolean], [joint=boolean], [jointPivot=boolean], [lastAutoComplete=boolean], [lattice=boolean], [latticePoint=boolean], [light=boolean], [localRotationAxis=boolean], [locator=boolean], [locatorUV=boolean], [locatorXYZ=boolean], [nCloth=boolean], [nParticle=boolean], [nParticleShape=boolean], [nRigid=boolean], [name=string], [nonlinear=boolean], [nurbsCurve=boolean], [nurbsSurface=boolean], [objectComponent=boolean], [orientationLocator=boolean], [particle=boolean], [particleShape=boolean], [plane=boolean], [polymesh=boolean], [polymeshEdge=boolean], [polymeshFace=boolean], [polymeshFreeEdge=boolean], [polymeshUV=boolean], [polymeshVertex=boolean], [polymeshVtxFace=boolean], [rigidBody=boolean], [rigidConstraint=boolean], [rotatePivot=boolean], [scalePivot=boolean], [sculpt=boolean], [selectHandle=boolean], [setAllowExcessCount=boolean], [setAutoComplete=boolean], [setAutoToggleSelection=boolean], [setDoneSelectionPrompt=string], [setNoSelectionHeadsUp=string], [setNoSelectionPrompt=string], [setSelectionCount=int], [setSelectionHeadsUp=string], [setSelectionPrompt=string], [showManipulators=boolean], [spring=boolean], [springComponent=boolean], [stroke=boolean], [subdiv=boolean], [subdivMeshEdge=boolean], [subdivMeshFace=boolean], [subdivMeshPoint=boolean], [subdivMeshUV=boolean], [surfaceEdge=boolean], [surfaceFace=boolean], [surfaceKnot=boolean], [surfaceParameterPoint=boolean], [surfaceRange=boolean], [surfaceUV=boolean], [texture=boolean], [title=string], [toolCursorType=string], [toolFinish=script], [toolStart=script], [totalSelectionSets=int], [vertex=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scriptCtx is undoable, queryable, and editable.
The command is processed prior to being executed.  The keyword
"$Selection#" where # is a number 1 or greater specifies
a selection set.  The context can specify several selection sets
which are substituted in place of the $Selection# keyword in the form
of a Mel string array.  Items that are specific per set need to
be specified in each set, if they are going to be specified for any of
the sets.  See examples below.

In addition, in order to specify the type of selection you need
to be making, any of the selection type flags from "selectType" command
can be used here.




Example:
---
import maya.cmds as cmds

Simple example of "attach curve" tool created using scriptCtx. This tool
prompts the user to select two curves to attach. As soon as two curves
are selected, the attach is performed. It uses the selection type
flag 'curveParameterPoint' from "selectType" command to specify the
selection mask for this tool.

cmds.scriptCtx( title='Attach Curve', totalSelectionSets=1, fcs="select -r $Selection1; performAttachCrv 0 \"\"", cumulativeLists=True, expandSelectionList=True, setNoSelectionPrompt='Select two curves close to the attachment points', setSelectionPrompt='Select a second curve close to the attachment point', setDoneSelectionPrompt='Never used because setAutoComplete is set', setAutoToggleSelection=True, setSelectionCount=2, setAutoComplete=True, curveParameterPoint=True )

And a more complex example of fillet blend tool (two sets of any number
of "surface curves").  Notice how the selection lists are passed as
arguments to the callback function, performBlendGiven.

cmds.scriptCtx( i1='birail3Gen.xpm', title='"Birail 3+ Tool', toolCursorType='edit', totalSelectionSets=2, cumulativeLists=True, expandSelectionList=True, fcs='select -r $Selection2; performBirail 0 3 \"birailThreePlusProfileContext\" ', setAutoToggleSelection=[True,True], setAutoComplete=[False, False], setSelectionCount=[0,2], nurbsCurve=[True,True], isoparm=[True,True], curveOnSurface=[True,True], surfaceEdge=[True,True], polymeshEdge=[True,True], setNoSelectionPrompt=['Select any number of profiles','Select two rails'], setSelectionPrompt=['Select additional profiles or hit ENTER', 'Select the second rail'], setDoneSelectionPrompt=['Profiles selected. Hit ENTER to start rail selection.', 'Rails selected. Hit ENTER to compute birail. '] )

Here's Birail 3+ where you select any number of curves, then 2 rails:

cmds.scriptCtx( i1='birail3Gen.xpm', title='"Birail 3+ Tool', toolCursorType='edit', totalSelectionSets=2, cumulativeLists=True, expandSelectionList=True, fcs='select -r $Selection2; performBirail 0 3 \"birailThreePlusProfileContext\" ', setAutoToggleSelection=[True,True], setAutoComplete=[False, False], setSelectionCount=[0,2], nurbsCurve=[True,True], isoparm=[True,True], curveOnSurface=[True,True], surfaceEdge=[True,True], polymeshEdge=[True,True], setNoSelectionPrompt=['Select any number of profiles','Select two rails'], setSelectionPrompt=['Select additional profiles or hit ENTER', 'Select the second rail'], setDoneSelectionPrompt=['Profiles selected. Hit ENTER to start rail selection.', 'Rails selected. Hit ENTER to compute birail. '] )

userBirailContextCallback has "true" as the first argument, which suggests
that $Selection2 contains all of $Selection1 items (as -cumulativeLists
true is specified in the tool creation.)

---
Return:
---


    string: Context name

Flags:
---


---
allComponents(alc): boolean
    properties: create, query, multiuse
    Set all component selection masks on/off

---
allObjects(alo): boolean
    properties: create, query, multiuse
    Set all object selection masks on/off

---
animBreakdown(abd): boolean
    properties: create, query, multiuse
    Set animation breakdown selection mask on/off.

---
animCurve(ac): boolean
    properties: create, query, multiuse
    Set animation curve selection mask on/off.

---
animInTangent(ait): boolean
    properties: create, query, multiuse
    Set animation in-tangent selection mask on/off.

---
animKeyframe(ak): boolean
    properties: create, query, multiuse
    Set animation keyframe selection mask on/off.

---
animOutTangent(aot): boolean
    properties: create, query, multiuse
    Set animation out-tangent selection mask on/off.

---
baseClassName(bcn): string
    properties: create, query, edit
    This string will be used to produce MEL function names for
the property sheets for the tool.  For example, if
"myScriptTool" was given, the functions "myScriptToolValues"
and "myScriptToolProperties" will be used for the
property sheets.  The default is "scriptTool".

---
camera(ca): boolean
    properties: create, query, multiuse
    Set camera selection mask on/off. (object flag)

---
cluster(cl): boolean
    properties: create, query, multiuse
    Set cluster selection mask on/off. (object flag)

---
collisionModel(clm): boolean
    properties: create, query, multiuse
    Set collision model selection mask on/off. (object flag)

---
controlVertex(cv): boolean
    properties: create, query, multiuse
    Set control vertex selection mask on/off. (component flag)

---
cumulativeLists(cls): boolean
    properties: create, query, edit
    If set, the selection lists will be cumulative.  For example,
the second list will contain all the items from the first list,
the third all the items from the second list etc.  Make sure
your script specified above takes that into account.  Relevant
if there is more than one selection set.

---
curve(c): boolean
    properties: create, query, multiuse
    Set curve selection mask on/off. (object flag)

---
curveKnot(ck): boolean
    properties: create, query, multiuse
    Set curve knot selection mask on/off. (component flag)

---
curveOnSurface(cos): boolean
    properties: create, query, multiuse
    Set curve-on-surface selection mask on/off. (object flag)

---
curveParameterPoint(cpp): boolean
    properties: create, query, multiuse
    Set curve parameter point selection mask on/off. (component flag)

---
dimension(dim): boolean
    properties: create, query, multiuse
    Set dimension shape selection mask on/off. (object flag)

---
dynamicConstraint(dc): boolean
    properties: create, query, multiuse
    Set dynamicConstraint selection mask on/off. (object flag)

---
edge(eg): boolean
    properties: create, query, multiuse
    Set mesh edge selection mask on/off. (component flag)

---
editPoint(ep): boolean
    properties: create, query, multiuse
    Set edit-point selection mask on/off. (component flag)

---
emitter(em): boolean
    properties: create, query, multiuse
    Set emitter selection mask on/off. (object flag)

---
enableRootSelection(ers): boolean
    properties: create, query, edit
    If set, the items to be selected are at their root transform
level. Default is false.

---
escToQuit(esc): boolean
    properties: create, query, edit
    If set to true, exit the tool when press "Esc". Default is false.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
exitUponCompletion(euc): boolean
    properties: create, query, edit
    If set, completing the last selection set will exit the
tool.  Default is true.

---
expandSelectionList(esl): boolean
    properties: create, query, edit
    If set, the selection lists will expand to have a single
component in each item.  You probably want this as a default, otherwise
two isoparms on the same surface will show up as 1 item.

To ensure that components on the same object are returned in the order in
which they are selected, use the selectPref -trackSelectionOrder on
command in your -toolStart script to enable ordered
selection, then restore it to its original value in your
-toolFinish script.

---
facet(fc): boolean
    properties: create, query, multiuse
    Set mesh face selection mask on/off. (component flag)

---
field(fi): boolean
    properties: create, query, multiuse
    Set field selection mask on/off. (object flag)

---
finalCommandScript(fcs): script
    properties: create, query, edit
    Supply the script that will be run when the user presses the
enter key and the context is completed.  Depending on the
number of selection sets you have, the script can make use
of variables string $Selection1[], $Selection2[], ...

---
fluid(fl): boolean
    properties: create, query, multiuse
    Set fluid selection mask on/off. (object flag)

---
follicle(fo): boolean
    properties: create, query, multiuse
    Set follicle selection mask on/off. (object flag)

---
forceAddSelect(fas): boolean
    properties: create, query, edit
    If set to true, together with -setAutoToggleSelection (see
below) on the first selection set, causes the first selection after
the computation of the previous result to be "shift" selection,
unless a modifier key is pressed.  Default is false.
Flags for each selection set.  These flags are multi-use.

---
hairSystem(hs): boolean
    properties: create, query, multiuse
    Set hairSystem selection mask on/off. (object flag)

---
handle(ha): boolean
    properties: create, query, multiuse
    Set object handle selection mask on/off. (object flag)

---
history(ch): boolean
    properties: create
    If this is a tool command, turn the construction history on
for the tool in question.

---
hull(hl): boolean
    properties: create, query, multiuse
    Set hull selection mask on/off. (component flag)

---
ignoreInvalidItems(iii): boolean
    properties: create, query, edit
    If you have multiple selection sets, the state of the
selection set is recorded at the time you "complete it".  You could
then delete some of the items in that list and end up with
invalid items in one or more of your selection sets.  If this
flag is set, those items will be detected and ignored.  You will
never know it happened.  Its as if they were never selected in
the first place, except that your selection set now does not
have as many items as it may need.  If this flag is not set,
you will get a warning and your final command callback script
will likely not execute because of an error condition.

---
ikEndEffector(iee): boolean
    properties: create, query, multiuse
    Set ik end effector selection mask on/off. (object flag)

---
ikHandle(ikh): boolean
    properties: create, query, multiuse
    Set ik handle selection mask on/off. (object flag)

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
imagePlane(ip): boolean
    properties: create, query, multiuse
    Set image plane selection mask on/off. (component flag)

---
implicitGeometry(ig): boolean
    properties: create, query, multiuse
    Set implicit geometry selection mask on/off. (object flag)

---
isoparm(iso): boolean
    properties: create, query, multiuse
    Set surface iso-parm selection mask on/off. (component flag)

---
joint(j): boolean
    properties: create, query, multiuse
    Set ik handle selection mask on/off. (object flag)

---
jointPivot(jp): boolean
    properties: create, query, multiuse
    Set joint pivot selection mask on/off. (component flag)

---
lastAutoComplete(lac): boolean
    properties: create, query, edit
    True if auto complete is set for the last selection set,
false otherwise.  Mostly used for query, but if present in conjuction
with -sac/setAutoComplete flag, -sac flag takes precedence.

---
lattice(la): boolean
    properties: create, query, multiuse
    Set lattice selection mask on/off. (object flag)

---
latticePoint(lp): boolean
    properties: create, query, multiuse
    Set lattice point selection mask on/off. (component flag)

---
light(lt): boolean
    properties: create, query, multiuse
    Set light selection mask on/off. (object flag)

---
localRotationAxis(ra): boolean
    properties: create, query, multiuse
    Set local rotation axis selection mask on/off. (component flag)

---
locator(lc): boolean
    properties: create, query, multiuse
    Set locator (all types) selection mask on/off. (object flag)

---
locatorUV(luv): boolean
    properties: create, query, multiuse
    Set uv locator selection mask on/off. (object flag)

---
locatorXYZ(xyz): boolean
    properties: create, query, multiuse
    Set xyz locator selection mask on/off. (object flag)

---
nCloth(ncl): boolean
    properties: create, query, multiuse
    Set nCloth selection mask on/off. (object flag)

---
nParticle(npr): boolean
    properties: create, query, multiuse
    Set nParticle point selection mask on/off. (component flag)

---
nParticleShape(nps): boolean
    properties: create, query, multiuse
    Set nParticle shape selection mask on/off. (object flag)

---
nRigid(nr): boolean
    properties: create, query, multiuse
    Set nRigid selection mask on/off. (object flag)

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
nonlinear(nl): boolean
    properties: create, query, multiuse
    Set nonlinear selection mask on/off. (object flag)

---
nurbsCurve(nc): boolean
    properties: create, query, multiuse
    Set nurbs-curve selection mask on/off. (object flag)

---
nurbsSurface(ns): boolean
    properties: create, query, multiuse
    Set nurbs-surface selection mask on/off. (object flag)

---
objectComponent(ocm): boolean
    properties: create, query
    Component flags apply to object mode.

---
orientationLocator(ol): boolean
    properties: create, query, multiuse
    Set orientation locator selection mask on/off. (object flag)

---
particle(pr): boolean
    properties: create, query, multiuse
    Set particle point selection mask on/off. (component flag)

---
particleShape(ps): boolean
    properties: create, query, multiuse
    Set particle shape selection mask on/off. (object flag)

---
plane(pl): boolean
    properties: create, query, multiuse
    Set sketch plane selection mask on/off. (object flag)

---
polymesh(p): boolean
    properties: create, query, multiuse
    Set poly-mesh selection mask on/off. (object flag)

---
polymeshEdge(pe): boolean
    properties: create, query, multiuse
    Set poly-mesh edge selection mask on/off. (component flag)

---
polymeshFace(pf): boolean
    properties: create, query, multiuse
    Set poly-mesh face selection mask on/off. (component flag)

---
polymeshFreeEdge(pfe): boolean
    properties: create, query, multiuse
    Set poly-mesh free-edge selection mask on/off. (component flag)

---
polymeshUV(puv): boolean
    properties: create, query, multiuse
    Set poly-mesh UV point selection mask on/off. (component flag)

---
polymeshVertex(pv): boolean
    properties: create, query, multiuse
    Set poly-mesh vertex selection mask on/off. (component flag)

---
polymeshVtxFace(pvf): boolean
    properties: create, query, multiuse
    Set poly-mesh vertexFace selection mask on/off. (component flag)

---
rigidBody(rb): boolean
    properties: create, query, multiuse
    Set rigid body selection mask on/off. (object flag)

---
rigidConstraint(rc): boolean
    properties: create, query, multiuse
    Set rigid constraint selection mask on/off. (object flag)

---
rotatePivot(rp): boolean
    properties: create, query, multiuse
    Set rotate pivot selection mask on/off. (component flag)

---
scalePivot(sp): boolean
    properties: create, query, multiuse
    Set scale pivot selection mask on/off. (component flag)

---
sculpt(sc): boolean
    properties: create, query, multiuse
    Set sculpt selection mask on/off. (object flag)

---
selectHandle(sh): boolean
    properties: create, query, multiuse
    Set select handle selection mask on/off. (component flag)

---
setAllowExcessCount(sae): boolean
    properties: create, edit, multiuse
    If set, the number if items is to be interpreted as the minimum.

---
setAutoComplete(sac): boolean
    properties: create, edit, multiuse
    If set to true, as soon as the specified number of items is
selected the tool will start the next selection set or run the command.

---
setAutoToggleSelection(sat): boolean
    properties: create, edit, multiuse
    If set to true, it is as if "shift" key is pressed when there
are no modifiers pressed.  That means that you get the "toggle select"
behaviour by default.  This only applies to the 3D view, and the
selection done in the hypergraph, outliner or elsewhere is still
a subject to the usual rules.

---
setDoneSelectionPrompt(dsp): string
    properties: create, edit, multiuse
    If setAutoComplete is not set (see below) this string will be
shown as soon as the tool has enough items for a particular selection
set.  If this is not set, but is needed, the same string as set with
-setSelectionPrompt flag will be used.

---
setNoSelectionHeadsUp(snh): string
    properties: create, edit, multiuse
    Supply a string that will be shown as a heads up prompt when
there is nothing selected.  This must be set separately for each
selection set.

---
setNoSelectionPrompt(snp): string
    properties: create, edit, multiuse
    Supply a string that will be shown as help when there is
nothing selected.  This must be set separately for each
selection set.

---
setSelectionCount(ssc): int
    properties: create, edit, multiuse
    The number of items in this selection set.  0 means as many as
you need until completion.

---
setSelectionHeadsUp(ssh): string
    properties: create, edit, multiuse
    Supply a string that will be shown as a heads up prompt when
there is something selected.  This must be set separately for each
selection set.

---
setSelectionPrompt(ssp): string
    properties: create, edit, multiuse
    Supply a string that will be shown as help when there is
something selected.  This must be set separately for each
selection set.

---
showManipulators(sm): boolean
    properties: create, query, edit
    If set, the manipulators will be shown for any active objects.
Basically, it is as if you are in the Show Manipulator tool.

---
spring(spr): boolean
    properties: create, query, multiuse
    Set spring shape selection mask on/off. (object flag)

---
springComponent(spc): boolean
    properties: create, query, multiuse
    Set individual spring selection mask on/off. (component flag)

---
stroke(str): boolean
    properties: create, query, multiuse
    Set the Paint Effects stroke selection mask on/off. (object flag)

---
subdiv(sd): boolean
    properties: create, query, multiuse
    Set subdivision surfaces selection mask on/off. (object flag)

---
subdivMeshEdge(sme): boolean
    properties: create, query, multiuse
    Set subdivision surfaces mesh edge selection mask on/off. (component flag)

---
subdivMeshFace(smf): boolean
    properties: create, query, multiuse
    Set subdivision surfaces mesh face selection mask on/off. (component flag)

---
subdivMeshPoint(smp): boolean
    properties: create, query, multiuse
    Set subdivision surfaces mesh point selection mask on/off. (component flag)

---
subdivMeshUV(smu): boolean
    properties: create, query, multiuse
    Set subdivision surfaces mesh UV map selection mask on/off. (component flag)

---
surfaceEdge(se): boolean
    properties: create, query, multiuse
    Set surface edge selection mask on/off. (component flag)

---
surfaceFace(sf): boolean
    properties: create, query, multiuse
    Set surface face selection mask on/off. (component flag)

---
surfaceKnot(sk): boolean
    properties: create, query, multiuse
    Set surface knot selection mask on/off. (component flag)

---
surfaceParameterPoint(spp): boolean
    properties: create, query, multiuse
    Set surface parameter point selection mask on/off. (component flag)

---
surfaceRange(sr): boolean
    properties: create, query, multiuse
    Set surface range selection mask on/off. (component flag)

---
surfaceUV(suv): boolean
    properties: create, query, multiuse
    Set surface uv selection mask on/off. (component flag)

---
texture(tx): boolean
    properties: create, query, multiuse
    Set texture selection mask on/off. (object flag)

---
title(t): string
    properties: create, query, edit
    Supply a string that will be used as a precursor to all the
messages; i.e., the "name" of the tool.

---
toolCursorType(tct): string
    properties: create, query, edit
    Supply the string identifier to set the tool cursor type
when inside of tool. The following are the valid ids:
"create", "dolly", "edit", "pencil", "track", "trackHorizontal",
"trackVertical", "transformation", "tumble", "zoom", "zoomIn",
"zoomOut", "flyThrough", "dot", "fleur",
"leftArrow", "question", "doubleHorizArrow", "doubleVertArrow",
"sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess",
"input", "output", "leftCycle", "rightCycle", "rightExpand",
"knife".

---
toolFinish(tf): script
    properties: create, query, edit
    Supply the script that will be run when the user exits
the script.

---
toolStart(ts): script
    properties: create, query, edit
    Supply the script that will be run when the user first
enters the script

---
totalSelectionSets(tss): int
    properties: create, query, edit
    Total number of selection sets.

---
vertex(v): boolean
    properties: create, query, multiuse
    Set mesh vertex selection mask on/off. (component flag)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scriptCtx.html 
    """


def scriptEditorInfo(flagclearHistory: boolean, flagclearHistoryFile: boolean, flaghistoryFilename: string, flaginput: string, flagsuppressErrors: boolean, flagsuppressInfo: boolean, flagsuppressResults: boolean, flagsuppressStackWindow: boolean, flagsuppressWarnings: boolean, flagwriteHistory: boolean) -> string:
    """Synopsis:
---
---
 scriptEditorInfo([clearHistory=boolean], [clearHistoryFile=boolean], [historyFilename=string], [input=string], [suppressErrors=boolean], [suppressInfo=boolean], [suppressResults=boolean], [suppressStackWindow=boolean], [suppressWarnings=boolean], [writeHistory=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scriptEditorInfo is undoable, queryable, and editable.Note: Due to recent changes, certain flags will no longer work
on the Script Editor Window.  All flags will continue to work with the
CommandWindow (old Script Editor).
Note: This command cannot be used to create a new script
editor window.




Example:
---
import maya.cmds as cmds

Set the text of the input area of the Script Editor.
cmds.scriptEditorInfo(input='// select -all; delete;')
Clear the input area of the Script Editor.
cmds.scriptEditorInfo(input="")

Begin recording the Script Editor history to a file called
tempHistoryLog.txt in your maya directory.
cmds.scriptEditorInfo( historyFilename='tempHistoryLog.txt', writeHistory=True )

Stop recording the Script Editor history
cmds.scriptEditorInfo(writeHistory=False )

On Windows the following line would print something like "C:/maya/tempHistoryLog.txt"
On Linux it would be "~/maya/tempHistoryLog.txt"
cmds.scriptEditorInfo(query=True, historyFilename=True)

Suppress all warning and info messages
cmds.scriptEditorInfo(suppressWarnings=True)
cmds.scriptEditorInfo(suppressInfo=True)

---
Return:
---


    string: The name of the Command Window window is returned.

Flags:
---


---
clearHistory(ch): boolean
    properties: edit
    Clears the read-only text in the upper field of the Command Window.

---
clearHistoryFile(chf): boolean
    properties: edit
    Clear the file defined by the -hf/historyFilename flag, but only
if -wh/writeHistory is true. Use this flag to start a new history file,
since the default behaviour of the Command Window is to append to
the existing file.

---
historyFilename(hfn): string
    properties: query, edit
    Sets or returns the name of the file that the Command Window will
use to echo all of its history to. If this is an empty string when
the -wh/writeHistory flag is set to true, then it will automatically be
set to the default file.

---
input(i): string
    properties: edit
    Sets the text in the lower field of the Command Window.
Set this value to an empty string to clear the field.

Note: this flag only affects the Command Window and not the new script editor.
To find out how to manipulate the new script editor please refer to the documentation
on the cmdScrollFieldExecuter and cmdScrollFieldReporter.

---
suppressErrors(se): boolean
    properties: query, edit
    When true, Command Window and Script Editor will not display error messages.

---
suppressInfo(si): boolean
    properties: query, edit
    When true, Command Window and Script Editor will not display info messages
generated by Maya.

---
suppressResults(sr): boolean
    properties: query, edit
    When true, Command Window and Script Editor will not display command results.

---
suppressStackWindow(ssw): boolean
    properties: query, edit
    When true and when the stackTrace mechanism is on, this
flag will suppress the display of the stack window. If stack
trace is enabled then results will be returned to the output
window instead of a separate stack window.

---
suppressWarnings(sw): boolean
    properties: query, edit
    When true, Command Window and Script Editor will not display warning messages.

---
writeHistory(wh): boolean
    properties: query, edit
    When true, Command Window will echo all of its
history to the file defined by the -hf/historyFilename flag. This
flag effectively turns file writing on/off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scriptEditorInfo.html 
    """


def scriptJob(flagallChildren: boolean, flagattributeAdded: tuple[string, script], flagattributeChange: tuple[string, script], flagattributeDeleted: tuple[string, script], flagcompressUndo: boolean, flagconditionChange: tuple[string, script], flagconditionFalse: tuple[string, script], flagconditionTrue: tuple[string, script], flagconnectionChange: tuple[string, script], flagdisregardIndex: boolean, flagevent: tuple[string, script], flagexists: int, flagforce: boolean, flagidleEvent: script, flagkill: int, flagkillAll: boolean, flagkillWithScene: boolean, flaglistConditions: boolean, flaglistEvents: boolean, flaglistJobs: boolean, flagnodeDeleted: tuple[string, script], flagnodeNameChanged: tuple[string, script], flagoptionVarChanged: tuple[string, script], flagparent: string, flagpermanent: boolean, flagprotected: boolean, flagreplacePrevious: boolean, flagrunOnce: boolean, flagtimeChange: script, flaguiDeleted: tuple[string, script]) -> boolean | int | list[string]:
    """Synopsis:
---
---
 scriptJob([allChildren=boolean], [attributeAdded=[string, script]], [attributeChange=[string, script]], [attributeDeleted=[string, script]], [compressUndo=boolean], [conditionChange=[string, script]], [conditionFalse=[string, script]], [conditionTrue=[string, script]], [connectionChange=[string, script]], [disregardIndex=boolean], [event=[string, script]], [exists=int], [force=boolean], [idleEvent=script], [kill=int], [killAll=boolean], [killWithScene=boolean], [listConditions=boolean], [listEvents=boolean], [listJobs=boolean], [nodeDeleted=[string, script]], [nodeNameChanged=[string, script]], [optionVarChanged=[string, script]], [parent=string], [permanent=boolean], [protected=boolean], [replacePrevious=boolean], [runOnce=boolean], [timeChange=script], [uiDeleted=[string, script]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scriptJob is undoable, NOT queryable, and NOT editable.
Script jobs are tied to the event loop in the interactive application.
They are run during idle events.  This means that script jobs do not
exist in the batch application.  The scriptJob command does nothing
in batch mode.

This triggering happens very frequently so for speed considerations
no events are forwarded during playback.  This means that you cannot
use scriptJob -tc tcCallback; to alter animation behaviour.
Use an expression instead, or the rendering callbacks "preRenderMel"
and "postRenderMel".

When setting up jobs for conditions, it is invalid to setup jobs for
the true state, false state, and state change at the same time.  The
behaviour is undefined.  The user can only setup jobs for the true
and/or false state, or only for the state change, but not three at
the same time. i.e. if you do: 


// Set up a job that runs for the life of the application.
// This job cannot be deleted with the "kill" command no matter what.
scriptJob -e "SelectionChanged" "print \"Annoying Message!\\n\"" -permanent;

// set up a job for the true state
scriptJob -ct "playingBack" playBackCallback;

// set up a job for the false state
scriptJob -cf "playingBack" playBackCallback;

then you should NOT do
scriptJob -cc "playingBack" playBackCallback;
otherwise it will lead to undefined behaviour.


This command can also be used to list available conditions
and events, and to kill running jobs.




Example:
---
import maya.cmds as cmds

create a job that deletes things when they are seleted
jobNum = cmds.scriptJob( ct= ["SomethingSelected","cmds.delete()"], protected=True)

Now display the job
jobs = cmds.scriptJob( listJobs=True )

Now kill it (need to use -force flag since it's protected)
cmds.scriptJob( kill=jobNum, force=True)

create a sphere, but print a warning the next time it
is raised over 10 units high
def warn():
        height = cmds.getAttr( 'mySphere.ty' )
        if height > 10.0:
                print 'Sphere is too high!'
cmds.sphere( n='mySphere' )

cmds.scriptJob( runOnce=True, attributeChange=['mySphere.ty', warn] )

create a job to detect a new attribute named "tag"
---

def detectNewTagAttr():
        print "New tag attribute was added"

cmds.scriptJob( runOnce=True, attributeAdded=['mySphere.tag',detectNewTagAttr] )
cmds.addAttr( 'mySphere', ln='tag', sn='tg', dt='string')

list all the existing conditions and print them
nicely
conds2 = cmds.scriptJob( listConditions=True )
for cond in sorted(conds2):
        print cond

---
Return:
---


    int: Thejob number, which can be used to kill the job. The job
number will be a value greater than or equal to zero
    list[string]: A string list when thelistflag is used
    boolean: For theexistsflag.

Flags:
---


---
allChildren(alc): boolean
    properties: create
    This flag can only be used in conjunction with
the -ac/attributeChange flag.  If it is specified, and the job
is attached to a compound attribute, then the
job will run due to changes to the specified attribute
as well as changes to its children.

---
attributeAdded(aa): [string, script]
    properties: create
    Run the script when the named attribute is added.
The string must identify both the dependency node and the
particular attribute.  If the dependency node is deleted,
this job is killed (even if the deletion is undoable).

---
attributeChange(ac): [string, script]
    properties: create
    Run the script when the named attribute changes value.
The string must identify both the dependency node and the
particular attribute.  If the dependency node is deleted,
this job is killed (even if the deletion is undoable).

---
attributeDeleted(ad): [string, script]
    properties: create
    Run the script when the named attribute is deleted.
The string must identify both the dependency node and the
particular attribute.  If the dependency node is deleted,
this job is killed (even if the deletion is undoable).

---
compressUndo(cu): boolean
    properties: create
    If this is set to true, and the scriptJob is undoable, then
its action will be bundled with the last user action for undo
purposes.  For example; if the scriptJob was triggered by a selection
change, then pressing undo will undo both the scriptJob and the
selection change at the same time.

---
conditionChange(cc): [string, script]
    properties: create
    Run the script when the named condition changes state.
The string must be the name of a pre-defined, or a
user-defined boolean condition.  To get a list of what
conditions exist, use the -listConditions flag.

---
conditionFalse(cf): [string, script]
    properties: create
    Run the script when the named condition becomes false.
The string must be the name of a pre-defined, or a
user-defined boolean condition.  To get a list of what
conditions exist, use the -listConditions flag.

---
conditionTrue(ct): [string, script]
    properties: create
    Run the script when the named condition becomes true.
The string must be the name of a pre-defined, or a
user-defined boolean condition.  To get a list of what
conditions exist, use the -listConditions flag.

---
connectionChange(con): [string, script]
    properties: create
    Run the script when the named attribute changes its
connectivity.  The string must identify both the dependency
node and the particular attribute.  If the dependency node
is deleted, this job is killed (even if the deletion is undoable).

---
disregardIndex(dri): boolean
    properties: create
    This flag can only be used in conjunction with
the -ac/attributeChange flag.  If it is specified, and the job
is attached to a multi (indexed) attribute, then the
job will run no matter which attribute in the multi changes.

---
event(e): [string, script]
    properties: create
    Run the script when the named event occurs.  This string
must be the name of a pre-defined maya event.  To get a list
of what events exist, use the -listEvents flag.

---
exists(ex): int
    properties: create
    Returns true if a scriptJob with the specified "job
number" exists, and false otherwise. The "job number"
should be a value that was returned on creation of a new
scriptJob.

---
force(f): boolean
    properties: create
    This flag can only be used with -kill, -killAll,
or -replacePrevious. It enables the deletion of protected jobs.

---
idleEvent(ie): script
    properties: create
    Run the script every time maya is idle.  WARNING,
as long as an idle event is is registered, the application
will keep calling it and will use up all available CPU time.
Use idleEvents with caution.

---
kill(k): int
    properties: create, multiuse
    Kills the job with the specified job number. Permanent jobs
cannot be killed, however, and protected jobs can only be killed
if the -force flag is used in the command.

---
killAll(ka): boolean
    properties: create
    Kills all jobs. Permanent jobs will not be deleted, and
protected jobs will only be deleted if the -force flag is used.

---
killWithScene(kws): boolean
    properties: create
    Attaches the job to the current scene, and when the scene is
emptied. The current scene is emptied by opening a new or
existing scene.

---
listConditions(lc): boolean
    properties: create
    This causes the command to return a string array containing
the names of all existing conditions.  Below is the descriptions
for all the existing conditions:
Events Based on Available Maya Features
These events are true when the given feature is available.

Event Name
 Maya Feature
AnimationExists
 Animation 
AnimationUIExists
User Interface for Animation
BaseMayaExists
 Any Basic Maya 
BaseUIExists
 Any Interactive Maya
DatabaseUIExists

DeformersExists
 Deformer Functions 
DeformersUIExists
User Interface for Deformers
DevicesExists
Device Support
DimensionsExists
Dimensioning
DynamicsExists
 Dynamics 
DynamicsUIExists
User Interface for Dynamics
ExplorerExists
 Explorer 
ImageUIExists
User Interface for Imaging
KinematicsExists
 Kinematics 
KinematicsUIExists
User Interface for Kinematics
ManipsExists
Manipulators
ModelExists
 Basic Modeling Tools
ModelUIExists
User Interface for Basic Modeling
NurbsExists
 Nurbs Modeling Tools
NurbsUIExists
User Interface for Nurbs Modeling
PolyCoreExists
Basic Polygonal Support
PolygonsExists
 Polygonal Modeling 
PolygonsUIExists
User Interface for Polygonal Modeling
PolyTextureExists
 Polygonal Texturing 
RenderingExists
 Built-in Rendering 
RenderingUIExists
User Interface for Rendering


Other Events
 autoKeyframeState:
true when Maya has autoKeyframing enabled
busy:
true when Maya is busy.
deleteAllCondition:
true when in the middle of a delete-all operation
flushingScene:
true while the scene is being flushed out
GoButtonEnabled:
true when the Go button in the panel context is enabled. 
hotkeyListChange:
true when the list of hotkey definitions has changed
playingBack:
true when Maya is playing back animation keyframes.
playbackIconsCondition:
instance of the playingBack condition used on the
time slider
readingFile:
true when Maya is reading a file.
RedoAvailable:
true when there are commands available for redo. 
SomethingSelected:
true when some object(s) is selected.
UndoAvailable:
true when there are commands available for undo.

---
listEvents(le): boolean
    properties: create
    This causes the command to return a string array containing
the names of all existing events.  Below is the descriptions
for all the existing events:

angularToleranceChanged:
when the tolerance on angular units is changed.
This tolerance can be changed by:
 using the MEL command, "tolerance" with the "-angular" flag
 changing the pref under Options->GeneralPreferences->
Modeling tab->Tangential Tolerance

angularUnitChanged:
when the user changes the angular unit.
axisAtOriginChanged:
when the axis changes at the origin.
  axisInViewChanged:
when the axis changes at a particular view.
ColorIndexChanged:
when the color index values change.
constructionHistoryChanged: 
when construction history is turned on or off.
currentContainerChanged: 
when the user set or unset the current container.
currentSoundNodeChanged:
whenever the sound displayed in the time slider changes
due to:
 the sound being removed (or no longer displayed)
[RMB in the time slider]
a new sound being displayed [RMB in the time slider]
sound display being toggled [animation options]
sound display mode being changed [animation options]

DagObjectCreated:
when a new DAG object is created.
deleteAll:
when a file new occurs
DisplayColorChanged:
when the display color changes.
displayLayerChange:
when a layer has been created or destroyed.
displayLayerManagerChange:
when the display layer manager has changed.
DisplayRGBColorChanged:
when the RGB display color changes.
glFrameTrigger:
for internal use only.
ChannelBoxLabelSelected:
when Channel Box label(first column) selection changes.
gridDisplayChanged:
for internal use only.
idle: 
when Maya is idle and there are no high priority idle tasks
idleHigh: 
when Maya is idle.  This is called before low priority idle
tasks.  You should almost always use "idle" instead.
lightLinkingChanged:
when any change occurs which modifies light linking
relationships.
lightLinkingChangedNonSG:
when any change occurs which modifies light linking
relationships, except when the change is a change of shading
assignment.
linearToleranceChanged:
 when the linear tolerance has been changed.  This tolerance
can be changed by:
 using the MEL command, "tolerance" with the  "-linear" flag
 changing the pref under Options->GeneralPreferences->
Modeling tab->Positional Tolerance

linearUnitChanged: 
when the user changes the linear unit through the Options menu.
MenuModeChanged: 
when the user changes the menu set for the menu bar in the main Maya window
(for example, from "Modeling" to "Animation").
RecentCommandChanged: 
for internal use only.
NewSceneOpened:
when a new scene has been opened.
PostSceneRead:
after a scene has been read. Specifically after a file open, import or all child
references have been read.
nurbsToPolygonsPrefsChanged:
 when any of the nurbs-to-polygons prefs have changed.  These
prefs can be changed by:
 using the Mel command, "nurbsToPolygonsPref"
 changing the prefs under Polygons->Nurbs To
Polygons->Option Box

playbackRangeChanged:
when the playback keyframe range changes.
playbackRangeSliderChanged:
when the animation start/end range (i.e. the leftmost
or rightmost entry cells in the time slider range, the inner
ones adjust the playback range) change
preferredRendererChanged:
when the preferred renderer changes.
quitApplication:
when the user has chosen to quit, either through the quit MEL
command, or through the Exit menu item.
Redo:
when user has selected redo from the menu and there was something
to redo.  This callback can be used for updating UI or local
storage.  Do not change the state of the scene or DG during this
callback.
renderLayerChange:
when creation or deletion of a render layer node has occured.
renderLayerManagerChange:
when the current render layer has changed.
RebuildUIValues:
for internal use only.
SceneOpened:
when a scene has been opened.
SceneSaved:
when a scene has been saved.
SelectionChanged: 
when a new selection is made.
UFESelectionChanged: 
when a new UFE selection is made.
SelectModeChanged: 
when the selection mode changes.
SelectPreferenceChanged: 
for internal use only.
SelectPriorityChanged:
when the selection priority changes.
SelectTypeChanged: 
when the selection type changes.
setEditorChanged:
obsolete.  No longer used.
SetModified:
when the set command is used to modify a set
SequencerActiveShotChanged: 
when the active sequencer shot is changed.
snapModeChanged:
when the snap mode changes. E.g. changes to grid snapping. 
timeChanged:
when the time changes.
timeUnitChanged: 
when the user changes the time unit.
ToolChanged: 
when the user changes the tool/context.
PostToolChanged: 
after the user changes the tool/context.
NameChanged: 
when the user changes the name of an object with the rename command.
Undo:
when user has selected undo from the menu and there was
something to undo.  This callback can be used for updating UI or local
storage.  Do not change the state of the scene or DG during this
callback.
modelEditorChanged: 
when the user changes the options of a model editor.
colorMgtEnabledChanged: 
when the global per-scene color management enabled flag changes.
colorMgtConfigFileEnableChanged: 
when the global per-scene color management OCIO configuration enabled
flag changes.
colorMgtPrefsViewTransformChanged: 
when the global per-scene color management view transform preferences
transform changes.
colorMgtWorkingSpaceChanged: 
when the global per-scene color management working space changes.
colorMgtConfigFilePathChanged: 
when the global per-scene color management OCIO configuration file path
changes.
colorMgtConfigChanged: 
when the color management mode changes from native to OCIO, or when
a different OCIO configuration is loaded.
colorMgtPrefsReloaded: 
when all the global per-scene color management settings are reloaded.
colorMgtUserPrefsChanged: 
when any user-level color management preference has changed.
colorMgtOutputChanged: 
when the color management transform, or its enabled state, has changed.
colorMgtOCIORulesChanged: 
when the type of rules in OCIO mode has changed.
colorMgtRefreshed: 
when the color management is refreshed to trap environment variable changes.
metadataVisualStatusChanged: 
for internal use only.
shapeEditorTreeviewSelectionChanged: 
when a new selection in shape editor's treeview is made .
RenderViewCameraChanged: 
when the Render View's current camera is changed.
tabletModeChanged: 
Windows only: if your device is a Tablet PC, then the convertible mode has
changed.  You can use command about -tabletMode to query if your device
is currently running in tablet or laptop (keyboard attached) mode.

---
listJobs(lj): boolean
    properties: create
    This causes the command to return a string array containing
a description of all existing jobs, along with their job
numbers.  These numbers can be used to kill the jobs later.

---
nodeDeleted(nd): [string, script]
    properties: create
    Run the script when the named node is deleted

---
nodeNameChanged(nnc): [string, script]
    properties: create
    Run the script when the name of the named node changes

---
optionVarChanged(ovc): [string, script]
    properties: create
    Run the script when the named optionVar changes value.
If the optioNVar is deleted, this job is killed (even if the deletion is undoable).

---
parent(p): string
    properties: create
    Attaches this job to a piece of maya UI.  When the UI is
destroyed, the job will be killed along with it.

---
permanent(per): boolean
    properties: create
    Makes the job un-killable. Permanent jobs exist for the life
of the application, or for the life of their parent object.
The -killWithScene flag does apply to permanent jobs.

---
protected(pro): boolean
    properties: create
    Makes the job harder to kill. Protected jobs must be killed
or replaced intentionally by using the -force flag.
The -killWithScene flag does apply to protected jobs.

---
replacePrevious(rp): boolean
    properties: create
    This flag can only be used with the -parent flag.  Before
the new scriptJob is created, any existing scriptJobs that have
the same parent are first deleted.

---
runOnce(ro): boolean
    properties: create
    If this is set to true, the script will only be run a single
time.  If false (the default) the script will run every time
the triggering condition/event occurs.  If the -uid or -nd flags
are used, runOnce is turned on automatically.

---
timeChange(tc): script
    properties: create
    Run the script whenever the current time changes. The
script will not be executed if the time is changed by clicking on
the time slider, whereas scripts triggered by the "timeChanged"
condition will be executed.

---
uiDeleted(uid): [string, script]
    properties: create
    Run the script when the named piece of UI is deleted.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scriptJob.html 
    """


def scriptNode(flagafterScript: string, flagbeforeScript: string, flagexecuteAfter: boolean, flagexecuteBefore: boolean, flagignoreReferenceEdits: boolean, flagname: string, flagscriptType: int, flagsourceType: string) -> None:
    """Synopsis:
---
---
 scriptNode(
[attributeList]
    , [afterScript=string], [beforeScript=string], [executeAfter=boolean], [executeBefore=boolean], [ignoreReferenceEdits=boolean], [name=string], [scriptType=int], [sourceType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scriptNode is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a scriptNode named script that creates a sphere when a file
   containing this node is loaded.
---

nodeName = cmds.scriptNode( st=2, bs='cmds.sphere()', n='script', stp='python')

   Test the before script.
---

cmds.scriptNode( nodeName, executeBefore=True )

   Add a script to create a cone when the script node is deleted.
---

cmds.scriptNode( nodeName, e=True, as='cmds.cone()', stp='python' )

   Test the after script
---

cmds.scriptNode( nodeName, executeAfter=True )

---


Flags:
---


---
afterScript(afterScript): string
    properties: create, query, edit
    The script executed when the script node is deleted. 
C: The default is an empty string. 
Q: When queried, this flag returns a string.

---
beforeScript(bs): string
    properties: create, query, edit
    The script executed during file load. 
C: The default is an empty string. 
Q: When queried, this flag returns a string.

---
executeAfter(ea): boolean
    properties: create
    Execute the script stored in the .after attribute of the
scriptNode. This script is normally executed when the script node
is deleted.

---
executeBefore(eb): boolean
    properties: create
    Execute the script stored in the .before attribute of the
scriptNode. This script is normally executed when the file
is loaded.

---
ignoreReferenceEdits(ire): boolean
    properties: create
    Sets whether changes made to referenced nodes during the execution of the
script should be recorded as reference edits. This flag must be set when
the scriptNode is created. If this flag is not set, changes to referenced
nodes will be recorded as edits by default.

---
name(n): string
    properties: create
    When creating a new scriptNode, this flag specifies the name
of the node. If a non-unique name is used, the name will be
modified to ensure uniqueness.

---
scriptType(st): int
    properties: create, query, edit
    Specifies when the script is executed. The following
values may be used:


0 Execute on demand.


1 Execute on file load or on node deletion.


2 Execute on file load or on node deletion
when not in batch mode. 


3 Internal


4 Execute on software render


5 Execute on software frame render


6 Execute on scene configuration


7 Execute on time changed


C: The default value is 0. 
Q: When queried, this flag returns an int.

---
sourceType(stp): string
    properties: create, query, edit
    Sets the language type for both the attached scripts.
Valid values are "mel" (enabled by default), and "python".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scriptNode.html 
    """


def scriptTable(flagafterCellChangedCmd: script, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcellBackgroundColorCommand: script, flagcellChangedCmd: script, flagcellForegroundColorCommand: script, flagcellIndex: tuple[int, int], flagcellValue: string, flagclearRow: int, flagclearTable: boolean, flagcolumnFilter: tuple[int, string], flagcolumnWidth: tuple[int, int], flagcolumns: int, flagdefineTemplate: string, flagdeleteRow: int, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexcludingHeaders: boolean, flagexists: boolean, flagfullPathName: boolean, flaggetCellCmd: script, flagheight: int, flaghighlightColor: tuple[float, float, float], flaginsertRow: int, flagisObscured: boolean, flaglabel: tuple[int, string], flagmanage: boolean, flagmultiEditEnabled: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrowHeight: int, flagrows: int, flagrowsRemovedCmd: script, flagrowsToBeRemovedCmd: script, flagselectedCells: list[int], flagselectedColumns: list[int], flagselectedRow: boolean, flagselectedRows: list[int], flagselectionBehavior: int, flagselectionChangedCmd: script, flagselectionMode: int, flagsortEnabled: boolean, flagstatusBarMessage: string, flagunderPointerColumn: boolean, flagunderPointerRow: boolean, flaguseDoubleClickEdit: boolean, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 scriptTable(
[name]
    , [afterCellChangedCmd=script], [annotation=string], [backgroundColor=[float, float, float]], [cellBackgroundColorCommand=script], [cellChangedCmd=script], [cellForegroundColorCommand=script], [cellIndex=[int, int]], [cellValue=string], [clearRow=int], [clearTable=boolean], [columnFilter=[int, string]], [columnWidth=[int, int]], [columns=int], [defineTemplate=string], [deleteRow=int], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [excludingHeaders=boolean], [exists=boolean], [fullPathName=boolean], [getCellCmd=script], [height=int], [highlightColor=[float, float, float]], [insertRow=int], [isObscured=boolean], [label=[int, string]], [manage=boolean], [multiEditEnabled=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowHeight=int], [rows=int], [rowsRemovedCmd=script], [rowsToBeRemovedCmd=script], [selectedCells=int[]], [selectedColumns=int[]], [selectedRow=boolean], [selectedRows=int[]], [selectionBehavior=int], [selectionChangedCmd=script], [selectionMode=int], [sortEnabled=boolean], [statusBarMessage=string], [underPointerColumn=boolean], [underPointerRow=boolean], [useDoubleClickEdit=boolean], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scriptTable is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

def edit_cell(row, column, value):
    return 1

window = cmds.window(widthHeight=(400, 300))
form = cmds.formLayout()
table = cmds.scriptTable(rows=4, columns=2, label=[(1,"Column 1"), (2,"Column 2")], cellChangedCmd=edit_cell)

addButton = cmds.button(label="Add Row",command="cmds.scriptTable(table, edit=True,insertRow=1)")
deleteButton = cmds.button(label="Delete Row",command="cmds.scriptTable(table, edit=True,deleteRow=1)")

cmds.formLayout(form, edit=True, attachForm=[(table, 'top', 0), (table, 'left', 0), (table, 'right', 0), (addButton, 'left', 0), (addButton, 'bottom', 0), (deleteButton, 'bottom', 0), (deleteButton, 'right', 0)], attachControl=(table, 'bottom', 0, addButton), attachNone=[(addButton, 'top'),(deleteButton, 'top')],  attachPosition=[(addButton, 'right', 0, 50), (deleteButton, 'left', 0, 50)] )

cmds.showWindow( window )

Set and query cells
cmds.scriptTable(table, cellIndex=(1,1), edit=True, cellValue="MyValue")
print cmds.scriptTable(table, cellIndex=(1,1), query=True, cellValue=True)

Select and query rows, columns and cells
cmds.scriptTable(table, edit=True, selectedRows=[1, 3])
print cmds.scriptTable(table, query=True, selectedRows=True)
cmds.scriptTable(table, edit=True, selectedColumns=[1])
print cmds.scriptTable(table, query=True, selectedColumns=True)
cmds.scriptTable(table, edit=True, selectedCells=[1,2,2,1,3,2,4,1])
print cmds.scriptTable(table, query=True, selectedCells=True)

Set a filter for the first column
cmds.scriptTable(table, edit=True, columnFilter=(1,"MyValue"))
Set a filter for all columns
cmds.scriptTable(table, edit=True, columnFilter=(0,"MyValue"))

---
Return:
---


    string: The full path name to the created script table control.

Flags:
---


---
afterCellChangedCmd(acc): script
    properties: create, edit
    Sets the script to call after the value of a cell has been
changed. The procedure is called with
2 integer arguments specifying the row and column for
which the value was changed. The 3rd argument is the string
which was entered into that cell. The procedure does not need to
return any value.
The row and column numbers passed in are 1-based
(i.e. (1,1) is the upper left cell). The procedure should be
of the form:

global proc procedureName(int $row, int $column, string $value)

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
cellBackgroundColorCommand(cbc): script
    properties: create, edit
    Sets the script to call when it requires
the background color of a cell.
The procedure is called with
2 integer arguments specifying the row and column for
which the value is required. The procedure should return
an array of ints which is the RGB color value for the cell.
The row and column numbers passed in are 1-based
(i.e. (1,1) is the upper left cell).
The procedure should be of the form:

global proc int[] procedureName(int $row, int $column) {
return {255,0,0}; // return Red as cell background color
}

---
cellChangedCmd(ccc): script
    properties: create, edit
    Sets the script to call when somebody has
changed the value of a cell. The procedure is called with
2 integer arguments specifying the row and column for
which the value was changed. The 3rd argument is the string
which was entered into that cell. The procedure should return
an integer value which indicates whether that value should be
accepted (return 1 if yes, and 0 if no).
The row and column numbers passed in are 1-based
(i.e. (1,1) is the upper left cell). The procedure should be
of the form:

global proc int procedureName(int $row, int $column, string $value)

---
cellForegroundColorCommand(cfc): script
    properties: create, edit
    Sets the script to call when it requires
the foreground color of a cell.
The procedure is called with
2 integer arguments specifying the row and column for
which the value is required. The procedure should return
an array of ints which is the RGB color value for the cell.
The row and column numbers passed in are 1-based
(i.e. (1,1) is the upper left cell).
The procedure should be of the form:

global proc int[] procedureName(int $row, int $column) {
return {0,0,0}; // return Black as Text color
}

---
cellIndex(ci): [int, int]
    properties: query, edit
    used with cellValue , to give the index of row and column
This flag and its argument must be passed to the command before the
-q flag (see examples).
      In query mode, this flag needs a value.

---
cellValue(cv): string
    properties: query, edit
    query and set the cell value on the table by the index of row and column referred in
flag -cellIndex.
In edit mode, if flag -multiEditEnabled is True and any cell is selected,
the flag -cellIndex is not used and the selected cells will be changed.

---
clearRow(cr): int
    properties: edit
    Clear the contents for all the cells on the specified
row. Any procedure specified by the -gcc flag will be
called to populate the cleared cells
The row number is 1-based (i.e. the first row is 1 not 0).

---
clearTable(ct): boolean
    properties: edit
    Clears the contents of all the cells in the table.
Any procedure specified by the -gcc flag will be
called to populate the cleared cells

---
columnFilter(cf): [int, string]
    properties: create, edit
    Filter the specified column with the string value provided.
Set filter to columns 0 will apply the filter to all columns.
The filter is case insensitive and support wildcards.
Wildcard Matching: Wildcard matching is much simpler than full regexps and has only four features:
c	Any character represents itself apart from those mentioned below. Thus c matches the character c.
?	Matches any single character. It is the same as . in full regexps.
*	Matches zero or more of any characters. It is the same as .* in full regexps.
[...]	Sets of characters can be represented in square brackets, similar to full regexps.
Within the character class, backslash has no special meaning.
(i.e. you can search for "MyValue" with "y*u" or "??Val??" or "[MyThe]Value" or any letters in "MyValue"
The column number is 1-based (i.e. the first row is 1 not 0).

---
columnWidth(cw): [int, int]
    properties: create, edit, multiuse
    Set the width of the specified column
The column number is 1-based (ie. the first column is 1 not 0).

---
columns(c): int
    properties: create, query, edit
    Set the number of columns in the table

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deleteRow(dr): int
    properties: edit
    Delete the specified row
The row number is 1-based (i.e. the first row is 1 not 0).

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
editable(ed): boolean
    properties: create, query, edit
    The edit state of the table.
By default, this flag is set to true, and the table can be edited.
If false, then the table is 'read only' and cannot be typed into.

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
excludingHeaders(eh): boolean
    properties: query
    when querying the count for the rows or the columns , the number returned will not include the headers

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
getCellCmd(gcc): script
    properties: create, edit
    Sets the script to call when it requires
the contents of a cell. The procedure is called with
2 integer arguments specifying the row and column for
which the value is required. The procedure should return
a string which is the value for the cell.
The row and column numbers passed in are 1-based
(ie. (1,1) is the upper left cell). The procedure should be
of the form:

global proc string procedureName(int $row, int $column)

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
insertRow(ir): int
    properties: edit
    Insert an empty row before the specified row. Any
procedure specified by the -gcc flag will be called to
populate the new new cells.
The row number is 1-based (i.e. the first row is 1 not 0).

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
label(l): [int, string]
    properties: create, edit, multiuse
    Set the label of the specified column.
The column number is 1-based (ie. the first column is 1 not 0).

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
multiEditEnabled(mee): boolean
    properties: create, query, edit
    True: scriptTable support multi-editing function

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
rowHeight(rh): int
    properties: create, query, edit
    Sets the height for each row in the scriptTable

---
rows(r): int
    properties: create, query, edit
    Set the number of rows in the table

---
rowsRemovedCmd(rrc): script
    properties: create, edit
    Sets the script to call after rows are removed by pressing 'delete' or
'backspace' key. The procedure is called with one argument
specifying that selected rows have been removed.
The rows passed in are 1-based. The procedure should be
of the form:

global proc procedureName(int $rows[])

---
rowsToBeRemovedCmd(rtc): script
    properties: create, edit
    Sets the script to call when 'delete' or 'backspace' key is
pressed. The procedure is called with one argument
specifying the selected rows to be removed. The procedure
should return an integer value which indicates whether the
selected rows should be removed (return 1 if yes, and 0 if no).
The rows passed in are 1-based. The procedure should be
of the form:

global proc int procedureName(int $rows[])

---
selectedCells(sc): int[]
    properties: query, edit
    Select the cells or return  the cells currently selected.
This returns a list of indices, the first of each pair is the row, the second is the column, repeated for each cell selected
The returned cell numbers are 1-based (ie. the first row is 1 not 0, the first column is 1 not 0).

---
selectedColumns(scs): int[]
    properties: query, edit
    select the columns or return the columns currently selected.
This returns a list of indices of each column completely selected
The returned column numbers are 1-based

---
selectedRow(sr): boolean
    properties: query
    The current row selected.
The returned row number is 1-based (ie. the first row is 1 not 0).

---
selectedRows(srs): int[]
    properties: query, edit
    In edit mode, select the rows given as argument.
In query mode, return a list of indices of completely selected rows.
The row numbers are 1-based

---
selectionBehavior(sb): int
    properties: create, query, edit
    Set the selection behavior, valid values are from 0 to 2 (inclusive)
0 - Selecting single items.
1 - Selecting only rows.
2 - Selecting only columns.

---
selectionChangedCmd(scc): script
    properties: create, edit
    Sets the script to call when a complete selection
operation triggered by the user has occurred successfully.
The script does not pass any parameters and does not need to
return any value (i.e. It is simply a notification mechanism).

---
selectionMode(sm): int
    properties: create, query, edit
    Set the selection Mode, valid values are from 0 to 4 (inclusive)
0 - Items cannot be selected.
1 - When the user selects an item, any already-selected item becomes unselected, and the user cannot unselect the selected item by clicking on it.
2 - When the user selects an item in the usual way, the selection status of that item is toggled and the other items are left alone. Multiple items can be toggled by dragging the mouse over them.
3 - When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. If the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. Multiple items can be selected by dragging the mouse over them.
4 - When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item.

---
sortEnabled(se): boolean
    properties: create, query, edit
    enable scriptTable sorted by column
default value is false and the whole row will be sorted

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
underPointerColumn(upc): boolean
    properties: query
    The column under the pointer.
The returned column number is 1-based (i.e. the first column is 1 not 0).

---
underPointerRow(upr): boolean
    properties: query
    The row under the pointer.
The returned row number is 1-based (i.e. the first row is 1 not 0).

---
useDoubleClickEdit(udc): boolean
    properties: create, query, edit
    this controls the cell edit mode
False: Click in the cell to select (in Row selection, the last cell of the row is edited, in Column selection, the last cell of the column is edited)(default) 
True:  Clicked in cell is edited when double-clicked only

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scriptTable.html 
    """


def scriptedPanel(flagcontrol: boolean, flagcopy: string, flagcreateString: boolean, flagdefineTemplate: string, flagdocTag: string, flageditString: boolean, flagexists: boolean, flaginit: boolean, flagisUnique: boolean, flaglabel: string, flagmenuBarRepeatLast: boolean, flagmenuBarVisible: boolean, flagneedsInit: boolean, flagparent: string, flagpopupMenuProcedure: script, flagreplacePanel: string, flagtearOff: boolean, flagtearOffCopy: string, flagtearOffRestore: boolean, flagtype: string, flagunParent: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 scriptedPanel(
[panelName]
    , [control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [type=string], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scriptedPanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

// NOTE: The scriptedPanelType command does not support python
// 		 callbacks; these callbacks must be MEL.


global proc sampleCreateCallback(string $panelName) {
//
//  Description:
//      Create any editors unparented here and do
//      any other initialization required.
//
//      In this example we will only declare a global array to
//        maintain some state information.
//
    global float $gSampleState[5];

}


global proc sampleInitCallback(string $panelName) {
//
//  Description:
//      Re-initialize the panel on file -new or file -open.
//
//      In this example we will only re-init the global array.
//
    global float $gSampleState[];

       $gSampleState[0] = 20.2;
       $gSampleState[1] = 50.5;
       $gSampleState[2] = 34.7;
       $gSampleState[3] = 2.0;
       $gSampleState[4] = 1.0;

}

global proc sampleAddCallback(string $panelName) {
//
//  Description:  Create UI and parent any editors.
//
    global float $gSampleState[];

    columnLayout -adj true topCol;
    separator -style "none" -h 10;
        frameLayout -l "Sliders" -mw 10;
            columnLayout -adj true sampleCol;
                separator -style "none" -h 10;

                floatSliderGrp -l "Property A" -f true
                    -v $gSampleState[0]
                    fsg1;
                floatSliderGrp -l "Property B" -f true
                    -v $gSampleState[1]
                    fsg2;
                floatSliderGrp -l "Property C" -f true
                    -v $gSampleState[2]
                    fsg3;
                separator -style "none" -h 10;
            setParent ..;
        setParent ..;

        separator -style "none" -h 10;
        frameLayout -l "Radio Buttons" -mw 10;
            columnLayout sampleCol2;
                separator -style "none" -h 10;
                radioButtonGrp -nrb 3
                    -l "Big Options"
                    -la3 "Option 1" "Option 2" "Option 3"
                    -select $gSampleState[3]
                    rbg;
                radioButtonGrp -nrb 3
                    -l "Little Options"
                    -la3 "Option 4" "Option 5" "Option 6"
                    -select $gSampleState[4]
                    rbg2;
                separator -style "none" -h 10;

}

global proc sampleRemoveCallback(string $panelName) {
//
//  Description:
//        Unparent any editors and save state if required.
//
        global float $gSampleState[];
       //  Scope the control names to this panel.
       //
       string $control = `scriptedPanel -q -control $panelName`;
       setParent $control;

       $gSampleState[0] = `floatSliderGrp -q -v fsg1`;
       $gSampleState[1] = `floatSliderGrp -q -v fsg2`;
       $gSampleState[2] = `floatSliderGrp -q -v fsg3`;
       $gSampleState[3] = `radioButtonGrp -q -sl rbg`;
       $gSampleState[4] = `radioButtonGrp -q -sl rbg2`;
}

global proc sampleDeleteCallback(string $panelName) {
//
//  Description:
//        Delete any editors and do any other cleanup required.

}

global proc string sampleSaveStateCallback(string $panelName) {
//
//  Description:
//        Return a string that will restore the current state
//        when it is executed.

        global float $gSampleState[];
       $indent = "\n\t\t\t";

       return ($indent+"$gSampleState[0]="+$gSampleState[0]+";" +
               $indent+"$gSampleState[1]="+$gSampleState[1]+";" +
               $indent+"$gSampleState[2]="+$gSampleState[2]+";" +
               $indent+"$gSampleState[3]="+$gSampleState[3]+";" +
               $indent+"$gSampleState[4]="+$gSampleState[4]+";" +
               $indent+"setSamplePanelState $panelName;\n" );
}

global proc setSamplePanelState( string $whichPanel ) {
//
//  Description:
//        This is a convenience proc to set the panel state from the
//        global array

        global float $gSampleState[];

       //  Scope the control names to this panel.
       //
       string $control = `scriptedPanel -q -control $whichPanel`;
       if ("" != $control) {
              setParent $control;

              floatSliderGrp -e -v $gSampleState[0] fsg1;
              floatSliderGrp -e -v $gSampleState[1] fsg2;
              floatSliderGrp -e -v $gSampleState[2] fsg3;
              if (0 != $gSampleState[3]) {
               radioButtonGrp -e -sl $gSampleState[3] rbg;
              };
           if (0 != $gSampleState[4]) {
               radioButtonGrp -e -sl $gSampleState[4] rbg2;
           }
       }
}

Below is the python code to create and use scriptedPanelType and scriptedPanel using the MEL
callbacks defined above.

Use unique flag as we don't want two panels sharing the same global data.
cmds.scriptedPanelType( 'sampleScriptedPanelType', ccb='sampleCreateCallback', icb='sampleInitCallback', acb='sampleAddCallback', rcb='sampleRemoveCallback', dcb='sampleDeleteCallback', scb='sampleSaveStateCallback', unique=True )

 This script will create an unparented scripted panel, place it
 in one window, remove it, and place it in another window then
 return it to the first window.
---

---

 Create unparented scripted panel
---

cmds.scriptedPanel( 'sampleScriptedPanel', unParent=True, type='sampleScriptedPanelType', label='Sample' )

   Create a couple of windows and parent the scripted panel to the first.
---

cmds.window( 'sampleWin' )
cmds.frameLayout( 'frm', lv=False, bv=False )
cmds.scriptedPanel( 'sampleScriptedPanel', e=True, parent='sampleWin|frm' )
cmds.showWindow()

cmds.window( 'sampleWin2', w=cmds.window('sampleWin', q=True, w=True), h=cmds.window('sampleWin', q=True, h=True) )
cmds.frameLayout( 'frm', lv=False, bv=False )
cmds.showWindow()

   Reparent the scripted panel to the second window.
---

cmds.scriptedPanel( 'sampleScriptedPanel', e=True, unParent=True )
cmds.scriptedPanel( 'sampleScriptedPanel', e=True, parent='sampleWin2|frm' )

   Reparent the scripted panel back to the first window.
---

cmds.scriptedPanel( 'sampleScriptedPanel', e=True, unParent=True )
cmds.scriptedPanel( 'sampleScriptedPanel', e=True, parent='sampleWin|frm' )

   Close both windows
---

cmds.window( 'sampleWin', e=True, visible=False )
cmds.window( 'sampleWin2', e=True, visible=False )

   The scripted panel should appear in the Panel menu.  Select
   Panels->Panel->Sample and the panel should appear in the main window.
---


---
Return:
---


    string: The name of the scripted panel.

Flags:
---


---
control(ctl): boolean
    properties: query
    Returns the top level control for this panel.
Usually used for getting a parent to attach popup menus.
CAUTION: panels may not have controls at times.  This
flag can return "" if no control is present.

---
copy(cp): string
    properties: edit
    Makes this panel a copy of the specified panel.  Both
panels must be of the same type.

---
createString(cs): boolean
    properties: edit
    Command string used to create a panel

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the Maya panel.

---
editString(es): boolean
    properties: edit
    Command string used to edit a panel

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
init(init): boolean
    properties: create, edit
    Initializes the panel's default state.  This is usually done
automatically on file -new and file -open.

---
isUnique(iu): boolean
    properties: query
    Returns true if only one instance of this panel type is allowed.

---
label(l): string
    properties: query, edit
    Specifies the user readable label for the panel.

---
menuBarRepeatLast(mrl): boolean
    properties: create, query, edit
    Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.

---
menuBarVisible(mbv): boolean
    properties: create, query, edit
    Controls whether the menu bar for the panel is displayed.

---
needsInit(ni): boolean
    properties: query, edit
    (Internal) On Edit will mark the panel as requiring initialization.
Query will return whether the panel is marked for initialization.  Used
during file -new and file -open.

---
parent(p): string
    properties: create
    Specifies the parent layout for this panel.

---
popupMenuProcedure(pmp): script
    properties: query, edit
    Specifies the procedure called for building the panel's popup menu(s).
The default value is "buildPanelPopupMenu".  The procedure should take
one string argument which is the panel's name.

---
replacePanel(rp): string
    properties: edit
    Will replace the specified panel with this panel.  If the
target panel is within the same layout it will perform a swap.

---
tearOff(to): boolean
    properties: query, edit
    Will tear off this panel into a separate window with a paneLayout
as the parent of the panel. When queried this flag will return if the
panel has been torn off into its own window.

---
tearOffCopy(toc): string
    properties: create
    Will create this panel as a torn of copy of the specified source panel.

---
tearOffRestore(tor): boolean
    properties: create, edit
    Restores panel if it is torn off and focus is given to it.
If docked, becomes the active panel in the docked window.
This should be the default flag that is added to all panels
instead of -to/-tearOff flag which should only be used to tear off the panel.

---
type(typ): string
    properties: create, query
    This flag specifies the type of scripted panel to create.

---
unParent(up): boolean
    properties: edit
    Specifies that the panel should be removed from its layout.
This (obviously) cannot be used with query.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scriptedPanel.html 
    """


def scriptedPanelType(flagaddCallback: string, flagcopyStateCallback: string, flagcreateCallback: string, flagcustomView: boolean, flagdefineTemplate: string, flagdeleteCallback: string, flagexists: boolean, flaghotkeyCtxClient: string, flaginitCallback: string, flaglabel: string, flagobsolete: boolean, flagremoveCallback: string, flagretainOnFileOpen: boolean, flagsaveStateCallback: string, flagunique: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 scriptedPanelType(
[string]
    , [addCallback=string], [copyStateCallback=string], [createCallback=string], [customView=boolean], [defineTemplate=string], [deleteCallback=string], [exists=boolean], [hotkeyCtxClient=string], [initCallback=string], [label=string], [obsolete=boolean], [removeCallback=string], [retainOnFileOpen=boolean], [saveStateCallback=string], [unique=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scriptedPanelType is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

// NOTE: The scriptedPanelType command does not support python
// 		 callbacks; these callbacks must be MEL.


global proc sampleCreateCallback(string $panelName) {
//
//  Description:
//      Create any editors unparented here and do
//      any other initialization required.
//
//      In this example we will only declare a global array to
//        maintain some state information.
//
    global float $gSampleState[5];

}


global proc sampleInitCallback(string $panelName) {
//
//  Description:
//      Re-initialize the panel on file -new or file -open.
//
//      In this example we will only re-init the global array.
//
    global float $gSampleState[];

       $gSampleState[0] = 20.2;
       $gSampleState[1] = 50.5;
       $gSampleState[2] = 34.7;
       $gSampleState[3] = 2.0;
       $gSampleState[4] = 1.0;

}

global proc sampleAddCallback(string $panelName) {
//
//  Description:  Create UI and parent any editors.
//
    global float $gSampleState[];

    columnLayout -adj true topCol;
    separator -style "none" -h 10;
        frameLayout -l "Sliders" -mw 10;
            columnLayout -adj true sampleCol;
                separator -style "none" -h 10;

                floatSliderGrp -l "Property A" -f true
                    -v $gSampleState[0]
                    fsg1;
                floatSliderGrp -l "Property B" -f true
                    -v $gSampleState[1]
                    fsg2;
                floatSliderGrp -l "Property C" -f true
                    -v $gSampleState[2]
                    fsg3;
                separator -style "none" -h 10;
            setParent ..;
        setParent ..;

        separator -style "none" -h 10;
        frameLayout -l "Radio Buttons" -mw 10;
            columnLayout sampleCol2;
                separator -style "none" -h 10;
                radioButtonGrp -nrb 3
                    -l "Big Options"
                    -la3 "Option 1" "Option 2" "Option 3"
                    -select $gSampleState[3]
                    rbg;
                radioButtonGrp -nrb 3
                    -l "Little Options"
                    -la3 "Option 4" "Option 5" "Option 6"
                    -select $gSampleState[4]
                    rbg2;
                separator -style "none" -h 10;

}

global proc sampleRemoveCallback(string $panelName) {
//
//  Description:
//        Unparent any editors and save state if required.
//
        global float $gSampleState[];
       //  Scope the control names to this panel.
       //
       string $control = `scriptedPanel -q -control $panelName`;
       setParent $control;

       $gSampleState[0] = `floatSliderGrp -q -v fsg1`;
       $gSampleState[1] = `floatSliderGrp -q -v fsg2`;
       $gSampleState[2] = `floatSliderGrp -q -v fsg3`;
       $gSampleState[3] = `radioButtonGrp -q -sl rbg`;
       $gSampleState[4] = `radioButtonGrp -q -sl rbg2`;
}

global proc sampleDeleteCallback(string $panelName) {
//
//  Description:
//        Delete any editors and do any other cleanup required.

}

global proc string sampleSaveStateCallback(string $panelName) {
//
//  Description:
//        Return a string that will restore the current state
//        when it is executed.

        global float $gSampleState[];
       $indent = "\n\t\t\t";

       return ($indent+"$gSampleState[0]="+$gSampleState[0]+";" +
               $indent+"$gSampleState[1]="+$gSampleState[1]+";" +
               $indent+"$gSampleState[2]="+$gSampleState[2]+";" +
               $indent+"$gSampleState[3]="+$gSampleState[3]+";" +
               $indent+"$gSampleState[4]="+$gSampleState[4]+";" +
               $indent+"setSamplePanelState $panelName;\n" );
}

global proc setSamplePanelState( string $whichPanel ) {
//
//  Description:
//        This is a convenience proc to set the panel state from the
//        global array

        global float $gSampleState[];

       //  Scope the control names to this panel.
       //
       string $control = `scriptedPanel -q -control $whichPanel`;
       if ("" != $control) {
              setParent $control;

              floatSliderGrp -e -v $gSampleState[0] fsg1;
              floatSliderGrp -e -v $gSampleState[1] fsg2;
              floatSliderGrp -e -v $gSampleState[2] fsg3;
              if (0 != $gSampleState[3]) {
               radioButtonGrp -e -sl $gSampleState[3] rbg;
              };
           if (0 != $gSampleState[4]) {
               radioButtonGrp -e -sl $gSampleState[4] rbg2;
           }
       }
}

Below is the python code to create and use scriptedPanelType and scriptedPanel using the MEL
callbacks defined above.

Use unique flag as we don't want two panels sharing the same global data.
cmds.scriptedPanelType( 'sampleScriptedPanelType', ccb='sampleCreateCallback', icb='sampleInitCallback', acb='sampleAddCallback', rcb='sampleRemoveCallback', dcb='sampleDeleteCallback', scb='sampleSaveStateCallback', unique=True )

 This script will create an unparented scripted panel, place it
 in one window, remove it, and place it in another window then
 return it to the first window.
---

---

 Create unparented scripted panel
---

cmds.scriptedPanel( 'sampleScriptedPanel', unParent=True, type='sampleScriptedPanelType', label='Sample' )

   Create a couple of windows and parent the scripted panel to the first.
---

cmds.window( 'sampleWin' )
cmds.frameLayout( 'frm', lv=False, bv=False )
cmds.scriptedPanel( 'sampleScriptedPanel', e=True, parent='sampleWin|frm' )
cmds.showWindow()

cmds.window( 'sampleWin2', w=cmds.window('sampleWin', q=True, w=True), h=cmds.window('sampleWin', q=True, h=True) )
cmds.frameLayout( 'frm', lv=False, bv=False )
cmds.showWindow()

   Reparent the scripted panel to the second window.
---

cmds.scriptedPanel( 'sampleScriptedPanel', e=True, unParent=True )
cmds.scriptedPanel( 'sampleScriptedPanel', e=True, parent='sampleWin2|frm' )

   Reparent the scripted panel back to the first window.
---

cmds.scriptedPanel( 'sampleScriptedPanel', e=True, unParent=True )
cmds.scriptedPanel( 'sampleScriptedPanel', e=True, parent='sampleWin|frm' )

   Close both windows
---

cmds.window( 'sampleWin', e=True, visible=False )
cmds.window( 'sampleWin2', e=True, visible=False )

   The scripted panel should appear in the Panel menu.  Select
   Panels->Panel->Sample and the panel should appear in the main window.
---


---
Return:
---


    string: The name of the scripted panel type.

Flags:
---


---
addCallback(acb): string
    properties: create, query, edit
    This flag specifies the callback procedure for adding the panel
to a particular control layout.  The parent layout is guaranteed to be
the current default layout when the proc is called.  If its name is
required then it can be queried with 'setParent -q'.  Any editors should
be parented here.
global proc procName (string $panelName) { .... }

---
copyStateCallback(ocb): string
    properties: create, query, edit
    This flag specifies the callback procedure for copying the state of
the panel when a tear-off copy of the panel is made.  The callback proc has the form:
global proc procName (string $panelName, string $newPanelName) { .... }
This procedure will be executed immediately after the addCallback
procedure has finished executing. At that point, the copied panel will be
fully created and accessible to facilitate copying of panel settings.
Note: the addCallback procedure is called after the createCallback
procedure has been called.

---
createCallback(ccb): string
    properties: create, query, edit
    This flag specifies the callback procedure for initially creating
the panel object.  No UI should be created here.  Any editors owned
by the panel should be created here unparented.
The callback proc has the form:
global proc procName (string $panelName) { .... }

---
customView(cv): boolean
    properties: create, query, edit
    This flag specifies if this view is a custom 3d view for
MPx3dModelView types. This flag should only be used for
MPx3dModelView types.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deleteCallback(dcb): string
    properties: create, query, edit
    This flag specifies the callback procedure for final deletion of
the panel.  The callback proc has the form:
global proc procName (string $panelName) { .... }

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
hotkeyCtxClient(hkc): string
    properties: create, query, edit
    This flag is used to specify the name of the hotkey context client for this panel type.
By default, it is the same as the panel type.

---
initCallback(icb): string
    properties: create, query, edit
    This flag specifies the callback procedure for the initialize
callback.  This will be called on file -new and file -open to give the
panel an opportunity to re-initialize to a starting state, if required.
The panel may be parented or unparented at this time.
The callback proc has the form:
global proc procName (string $panelName) { .... }

---
label(l): string
    properties: create, query, edit
    Label for the panel

---
obsolete(o): boolean
    properties: create, query, edit
    This flag specifies that this type is no longer used in Maya.

---
removeCallback(rcb): string
    properties: create, query, edit
    This flag specifies the callback procedure for removing the panel
from its current control layout.  Any editors should be unparented here.
The callback proc has the form:
global proc procName (string $panelName) { .... }

---
retainOnFileOpen(rfo): boolean
    properties: create, query, edit
    This flag specifies if panels of this type should be retained after
restoring panel cofiguration during file open. Default value is false.

---
saveStateCallback(scb): string
    properties: create, query, edit
    This flag specifies the callback procedure for saving the state of
the panel.  The callback proc has the form:
global proc string procName (string $panelName) { .... }
Note that the proc returns a string.  This string will be executed after
the createCallback has been called to facilitate restoring the panel
state.

---
unique(u): boolean
    properties: create, query, edit
    This flag specifies if only one instance of this type of panel can exist
at a given time.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scriptedPanelType.html 
    """


def scrollField(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagclear: boolean, flagcommand: string, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagenterCommand: script, flagexists: boolean, flagfont: string, flagfontPointSize: int, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaginsertText: string, flaginsertionPosition: int, flagisObscured: boolean, flagkeyPressCommand: script, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfLines: int, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagselection: boolean, flagstatusBarMessage: string, flagtext: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int, flagwordWrap: boolean) -> string:
    """Synopsis:
---
---
 scrollField(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [clear=boolean], [command=string], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean], [font=string], [fontPointSize=int], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [insertText=string], [insertionPosition=int], [isObscured=boolean], [keyPressCommand=script], [manage=boolean], [noBackground=boolean], [numberOfLines=int], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [selection=boolean], [statusBarMessage=string], [text=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int], [wordWrap=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scrollField is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.paneLayout( configuration='horizontal4' )
cmds.scrollField( editable=False, wordWrap=True, text='Non editable with word wrap' )
cmds.scrollField( editable=False, wordWrap=False, text='Non editable with no word wrap' )
cmds.scrollField( editable=True, wordWrap=True, text='Editable with word wrap' )
cmds.scrollField( editable=True, wordWrap=False, text='Editable with no word wrap' )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
changeCommand(cc): script
    properties: create, edit
    Command executed when the value changes. This command
is executed whenever the field loses focus.

---
clear(cl): boolean
    properties: create, edit
    Removes all text in the field.

---
command(c): string
    properties: create, edit
    Obsolete - use "enterCommand" instead

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
editable(ed): boolean
    properties: create, query, edit
    The edit state of the field.  By default, this flag is
set to true and the field value may be changed by typing into it.
If false then the field is 'read only' and can not be typed into.
The text in the field can always be changed with the -tx/text flag
regardless of the state of the -ed/editable flag.

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
enterCommand(ec): script
    properties: create, edit
    Command executed when the enter key is pressed.
This applies to the enter key on the numeric keypad only.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
font(fn): string
    properties: create, query, edit
    The font for the text.  Valid values are
"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
"smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".

---
fontPointSize(fns): int
    properties: create, query, edit
    The font point size for the text.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
insertText(it): string
    properties: create, edit
    Insert text into the field at the current insertion
position (specified by the -ip/insertionPosition flag).

---
insertionPosition(ip): int
    properties: create, query, edit
    The insertion position for inserted text.  This is a
1 based value where position 1 specifies the beginning of the
field.  Position 0 may be used to specify the end of the field.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
keyPressCommand(kpc): script
    properties: create, edit
    Command executed when any key is pressed.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfLines(nl): int
    properties: query
    Number of lines in the scroll field.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
selection(sl): boolean
    properties: query
    The selected text in the field.  An empty string is returned
if there is no selected text.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
text(tx): string
    properties: create, query, edit
    The field text.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
wordWrap(ww): boolean
    properties: create
    Specify true to break lines at spaces, tabs, or newlines.  Text
will continue on the following line.  A value of false will not
break text between words, in which case text may disappear beyond
the edge of the field.  This flag must be set at create time.
Lines do not word wrap by default.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scrollField.html 
    """


def scrollLayout(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagborderVisible: boolean, flagchildArray: boolean, flagchildResizable: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontalScrollBarThickness: int, flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagminChildWidth: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagpanEnabled: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagresizeCommand: script, flagscrollAreaHeight: boolean, flagscrollAreaValue: boolean, flagscrollAreaWidth: boolean, flagscrollByPixel: tuple[string, int], flagscrollPage: string, flagstatusBarMessage: string, flaguseTemplate: string, flagverticalScrollBarAlwaysVisible: boolean, flagverticalScrollBarThickness: int, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 scrollLayout(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [borderVisible=boolean], [childArray=boolean], [childResizable=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [horizontalScrollBarThickness=int], [isObscured=boolean], [manage=boolean], [margins=int], [minChildWidth=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [panEnabled=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [resizeCommand=script], [scrollAreaHeight=boolean], [scrollAreaValue=boolean], [scrollAreaWidth=boolean], [scrollByPixel=[string, int]], [scrollPage=string], [statusBarMessage=string], [useTemplate=string], [verticalScrollBarAlwaysVisible=boolean], [verticalScrollBarThickness=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

scrollLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window( widthHeight=(350, 150) )
scrollLayout = cmds.scrollLayout(
        horizontalScrollBarThickness=16,
        verticalScrollBarThickness=16)
cmds.rowColumnLayout( numberOfColumns=3 )

for index in range(10):
        cmds.text()
        cmds.intField()
        cmds.intSlider()

cmds.showWindow()

value = cmds.scrollLayout(scrollLayout, query=True, scrollAreaValue=True)
top = value[0]
left = value[1]

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
borderVisible(bv): boolean
    properties: create, query, edit
    Visibility of the border.

---
childArray(ca): boolean
    properties: query
    Returns a string array of the names of the layout's
immediate children.

---
childResizable(cr): boolean
    properties: create, query
    Set to true if you want the child of the control layout to be
as wide as the scroll area.  You may also indicate a minimum
width for the child using the -mcw/minChildWidth flag.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
generalSpacing(gsp) 2024: int
    properties: edit
    Sets the spacing for this layout.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
horizontalScrollBarThickness(hst): int
    properties: create, edit
    Thickness of the horizontal scroll bar.  Specify an
integer value of pixels greater than or equal to 0. Other
than setting the value to 0 to hide the scrollbar, this
flag has no effect on Windows systems.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
margins(mar) 2024: int
    properties: edit
    Sets the content margins for this layout.

---
minChildWidth(mcw): int
    properties: create, query
    A positive non-zero integer value indicating the
minimum width the scroll layout's child.  This flag only has
meaning when the -cr/childResizable flag is set to true.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfChildren(nch): boolean
    properties: query
    Returns in an int the number of immediate children of the layout.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
panEnabled(pe): boolean
    properties: query, edit
    Set to true if you want to pan the scroll layout using ALT + MMB.
On OSX, in one button and two button mode, you could use
command+alt+LMB to pan it. The pan effect is disabled by default.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
resizeCommand(rc): script
    properties: create, edit
    The command invoked when the scroll layout is resized.

---
scrollAreaHeight(sah): boolean
    properties: query
    Return the height of the scroll area (in pixels).

---
scrollAreaValue(sav): boolean
    properties: query
    Return the vertical and horizontal values of the scroll
area (in pixels).

---
scrollAreaWidth(saw): boolean
    properties: query
    Return the width of the scroll area (in pixels).

---
scrollByPixel(sbp): [string, int]
    properties: edit
    Scroll the client area in the direction of the string.
The int specifies the number of pixels.

---
scrollPage(sp): string
    properties: edit
    Scroll the client area in the direction of the string.
Valid values are "up", "down", "left" or "right".

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
verticalScrollBarAlwaysVisible(vsb): boolean
    properties: create
    Set to true if you want to always have the vertical scroll bar visible.

---
verticalScrollBarThickness(vst): int
    properties: create, edit
    Thickness of the vertical scroll bar.  Specify an
integer value of pixels greater than or equal to 0.
This flag has no effect on Windows systems.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/scrollLayout.html 
    """


def sculpt(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagdropoffDistance: linear, flagdropoffType: string, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flaggroupWithLocator: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flaginsideMode: string, flagmaxDisplacement: linear, flagmode: string, flagname: string, flagobjectCentered: boolean, flagparallel: boolean, flagprune: boolean, flagremove: boolean, flagsculptTool: string, flagselectedComponents: boolean, flagsplit: boolean, flaguseComponentTags: boolean) -> list[string]:
    """Synopsis:
---
---
 sculpt(
selectionList
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [deformerTools=boolean], [dropoffDistance=linear], [dropoffType=string], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [groupWithLocator=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [insideMode=string], [maxDisplacement=linear], [mode=string], [name=string], [objectCentered=boolean], [parallel=boolean], [prune=boolean], [remove=boolean], [sculptTool=string], [selectedComponents=boolean], [split=boolean], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sculpt is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.polyPlane(w=24,h=24,sx=20,sy=20)

Deforms whatever is currently on the selection list
cmds.sculpt()

Increase the effect of the deformation
cmds.sculpt( 'sculpt1', edit=True, maxDisplacement=3.0 )

Try another faster deformation mode
cmds.sculpt( 'sculpt1', edit=True, mode='flip', insideMode='ring' )

---
Return:
---


    list[string]: Sculpt algorithm node name, sculpt sphere name, and sculpt stretch origin name

Flags:
---


---
after(af): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node after the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
afterReference(ar): boolean
    properties: create, edit
    The -afterReference flag is used to specify deformer ordering in a hybrid way that
choses between -before and -after automatically. If the geometry being
deformed is referenced then the -after mode is used when adding the new deformer,
otherwise the -before mode is used. The net effect when using -afterReference to build
deformer chains is that internal shape nodes in the deformer chain will only
appear at reference file boundaries, leading to lightweight deformer networks that
may be more amicable to reference swapping.

---
before(bf): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node before the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
components(cmp): boolean
    properties: query
    Returns the components used by the deformer

---
deformerTools(dt): boolean
    properties: query
    Returns the name of the deformer tool objects (if any)
as string string ...

---
dropoffDistance(dds): linear
    properties: create, query, edit
    Specifies the distance from the surface of the sculpt
object at which the sculpt object produces no deformation
effect. Default is 1.0. When queried, this flag returns a float.

---
dropoffType(drt): string
    properties: create, query, edit
    Specifies how the deformation effect drops off from
maximum effect at the surface of the sculpt object to no effect
at dropoff distance limit. Valid values are: linear | none.
Default is linear. When queried, this flag returns a string.

---
exclusive(ex): string
    properties: create, query
    Puts the deformation set in a deform partition.

---
frontOfChain(foc): boolean
    properties: create, edit
    This command is used to specify that the new deformer
node should be placed ahead (upstream) of existing deformer
and skin nodes in the shape's history (but not ahead of
existing tweak nodes). The input to the
deformer will be the upstream shape rather than the visible
downstream shape, so the behavior of this flag is the most
intuitive if the downstream deformers are in their reset
(hasNoEffect) position when the new deformer is added.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
geometry(g): string
    properties: query, edit, multiuse
    The specified object will be added to the list of
objects being deformed by this deformer object, unless
the -rm flag is also specified. When queried, this flag
returns string string string ...

---
geometryIndices(gi): boolean
    properties: query
    Complements the -geometry flag in query mode. Returns
the multi index of each geometry.

---
groupWithLocator(gwl): boolean
    properties: create
    Groups the sculptor and its locator together under
a single transform. Default is off.

---
ignoreSelected(ignoreSelected): boolean
    properties: create
    Tells the command to not deform objects on the
current selection list

---
includeHiddenSelections(ihs): boolean
    properties: create
    Apply the deformer to any visible and hidden objects in the selection list.
Default is false.

---
insideMode(im): string
    properties: create, query, edit
    Specifies how the deformation algorithm deals with
points that are inside the sculpting primitve. The choices are:
ring | even. The default is even. When queried, this flag
returns a string. Ring mode will tend to produce a contour like
ring of points around the sculpt object as it passes through an
object while even mode will try to spread the points out as
evenly as possible across the surface of the sculpt object.

---
maxDisplacement(mxd): linear
    properties: create, query, edit
    Defines the maximum amount the sculpt object may move
a point on an object which it is deforming. Default is 1.0. When
queried, this flag returns a float.

---
mode(m): string
    properties: create, query, edit
    Specifies which deformation algorithm the sculpt
object should use. The choices are: flip | project | stretch.
The default is stretch. When queried, this flag returns a string.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
objectCentered(oc): boolean
    properties: create
    Places the sculpt and locator in the center of the
bounding box of the selected object(s) or
components. Default is off which centers the
sculptor and locator at the origin.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
prune(pr): boolean
    properties: edit
    Removes any points not being deformed by the deformer in
its current configuration from the deformer set.

---
remove(rm): boolean
    properties: edit, multiuse
    Specifies that objects listed after the -g flag should
be removed from this deformer.

---
sculptTool(st): string
    properties: create
    Use the specified NURBS object as the sculpt tool instead
of the default implicit sphere.

---
selectedComponents(cms): boolean
    properties: query
    Returns the components used by the deformer that are currently selected.
This intersects the current selection with the components affected by the deformer.

---
split(sp): boolean
    properties: create, edit
    Branches off a new chain in the dependency graph instead
of inserting/appending the deformer into/onto an
existing chain.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sculpt.html 
    """


def sculptKeyCtx(flagactiveMode: int, flagaffectsTime: boolean, flagaffectsTimeAll: string, flagbrushScaling: int, flageditingRadius: boolean, flageditingStrength: boolean, flagexists: boolean, flagfalloffCurve: string, flagfalloffCurveAll: string, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagminRadius: float, flagminStrength: float, flagminStrengthAll: string, flagmode: int, flagmodeMinStrength: tuple[int, float], flagmodeStrength: tuple[int, float], flagname: string, flagradius: float, flagreset: boolean, flagstrength: float, flagstrengthAll: string) -> string:
    """Synopsis:
---
---
 sculptKeyCtx(
contextName
    , [activeMode=int], [affectsTime=boolean], [affectsTimeAll=string], [brushScaling=int], [editingRadius=boolean], [editingStrength=boolean], [exists=boolean], [falloffCurve=string], [falloffCurveAll=string], [history=boolean], [image1=string], [image2=string], [image3=string], [minRadius=float], [minStrength=float], [minStrengthAll=string], [mode=int], [modeMinStrength=[int, float]], [modeStrength=[int, float]], [name=string], [radius=float], [reset=boolean], [strength=float], [strengthAll=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sculptKeyCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a sculpt key context in grab mode.
cmds.sculptKeyCtx('sculptKeyContext', mode=0)

Switch to smooth mode and set the sculpt radius to 50.
cmds.sculptKeyCtx('sculptKeyContext', edit=True, mode=1, radius=50)

Set the strength for the grab and smooth modes to 50.
cmds.sculptKeyCtx('sculptKeyContext', edit=True, modeStrength=((0,50),(1,50)))

Set the strength for all modes to 80.
cmds.sculptKeyCtx('sculptKeyContext', edit=True, strengthAll=(80, 80, 80))

// Activate affects time option
cmds.sculptKeyCtx('sculptKeyContext', edit=True, affectsTime=1)

---
Return:
---


    string: Context name

Flags:
---


---
activeMode(am): int
    properties: query
    Used to query the current active sculpt mode. This can differ from the base
mode if the user is holding down the shift hotkey to temporarily switch to
smooth mode.

---
affectsTime(at): boolean
    properties: create, query, edit
    Specifies whether or not the sculpt tools affect the time as well as the value of the keys.

---
affectsTimeAll(ata): string
    properties: create, query, edit
    Specifies whether or not the sculpt tools affect the time as well as the value of the keys
for all modes.

---
brushScaling(brs): int
    properties: create, query, edit
    Specifies how the sculpt brush scales relative to the Graph Editor.
1 = no scaling,
2 = scaling based on time,
3 = scaling based on value

---
editingRadius(er): boolean
    properties: create, edit
    Enables or disables interactive radius scaling.

---
editingStrength(es): boolean
    properties: create, edit
    Enables or disables interactive strength scaling.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
falloffCurve(fc): string
    properties: create, query, edit
    Specifies the falloff curve of the sculpting effect.

---
falloffCurveAll(fca): string
    properties: create, query, edit
    Internal flag used to save/restore falloff curves for all modes.

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
minRadius(mr): float
    properties: create, query, edit
    Specifies the minumum radius the sculpt brush will take due to stylus pressure.
Cannot be more than the base brush radius.

---
minStrength(ms): float
    properties: create, query, edit
    Specifies the minumum strength of sculpting due to stylus pressure.
Cannot be more than the base strength.

---
minStrengthAll(msa): string
    properties: create, query, edit
    Internal flag used to save/restore min strength for all modes.

---
mode(m): int
    properties: create, query, edit
    Specifies the base sculpt mode.
0 = grab,
1 = smooth
2 = smear

---
modeMinStrength(mms): [int, float]
    properties: create, edit, multiuse
    Specifies the min strength for the specified mode.

---
modeStrength(mst): [int, float]
    properties: create, edit, multiuse
    Specifies the strength for the specified mode.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
radius(r): float
    properties: create, query, edit
    Specifies the radius of the sculpt brush.

---
reset(rs): boolean
    properties: query, edit
    Internal flag used to reset current tool mode settings.

---
strength(s): float
    properties: create, query, edit
    Specifies the strength of the sculpting effect for the current mode.
Each mode can have a different strength.

---
strengthAll(sa): string
    properties: create, query, edit
    Internal flag used to save/restore strength for all modes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sculptKeyCtx.html 
    """


def sculptMeshCacheChangeCloneSource(flagblendShape: string, flagtarget: string) -> None:
    """Synopsis:
---
---
 sculptMeshCacheChangeCloneSource([blendShape=string], [target=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.sculptMeshCacheChangeCloneSource( bs='blendShape1', t='pSphere4' )

---


Flags:
---


---
blendShape(bs): string
    properties: create, query, edit
    Set which blend shape should be used as the source when using the clone tool. When queried,
returns the current blend shape name as a string.

---
target(t): string
    properties: create, query, edit
    Set which blend shape should be used as the target when using the clone tool. When queried,
returns the current blend shape target name as a string.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sculptMeshCacheChangeCloneSource.html 
    """


def sculptMeshCacheCtx(flagadjustSize: boolean, flagadjustStrength: boolean, flagaffectAllLayers: boolean, flagbrushDirection: int, flagbrushSize: float, flagbrushStrength: float, flagbuildUpRate: float, flagcloneHideSource: boolean, flagcloneMethod: int, flagcloneShapeSource: string, flagcloneTargetSource: string, flagconstrainToSurface: boolean, flagdirection: int, flagdisplayFrozen: boolean, flagdisplayMask: boolean, flagdisplayWireframe: boolean, flagfalloffType: int, flagflood: float, flagfloodFreeze: float, flagframe: boolean, flagfreezeSelection: boolean, flaggrabFollowPath: boolean, flaggrabSilhouette: boolean, flaggrabTwist: boolean, flaginverted: boolean, flaglastMode: string, flaglockShellBorder: boolean, flagmakeStroke: tuple[uint, uint, uint, float, float], flagminSize: float, flagminStrength: float, flagmirror: int, flagmode: string, flagorientToSurface: boolean, flagrecordStroke: boolean, flagsculptFalloffCurve: string, flagsize: float, flagstampDistance: float, flagstampFile: string, flagstampFlipX: boolean, flagstampFlipY: boolean, flagstampOrientToStroke: boolean, flagstampPlacement: int, flagstampRandomization: boolean, flagstampRandomizationSeed: int, flagstampRandomizeFlipX: boolean, flagstampRandomizeFlipY: boolean, flagstampRandomizePosX: float, flagstampRandomizePosY: float, flagstampRandomizeRotation: float, flagstampRandomizeScale: float, flagstampRandomizeStrength: float, flagstampRotation: float, flagsteadyStrokeDistance: float, flagstrength: float, flagupdatePlane: boolean, flaguseGlobalSize: boolean, flaguseScreenSpace: boolean, flaguseStampDistance: boolean, flaguseStampImage: boolean, flaguseSteadyStroke: boolean, flagwholeStroke: boolean, flagwireframeAlpha: float, flagwireframeColor: tuple[float, float, float]) -> None:
    """Synopsis:
---
---
 sculptMeshCacheCtx([adjustSize=boolean], [adjustStrength=boolean], [affectAllLayers=boolean], [brushDirection=int], [brushSize=float], [brushStrength=float], [buildUpRate=float], [cloneHideSource=boolean], [cloneMethod=int], [cloneShapeSource=string], [cloneTargetSource=string], [constrainToSurface=boolean], [direction=int], [displayFrozen=boolean], [displayMask=boolean], [displayWireframe=boolean], [falloffType=int], [flood=float], [floodFreeze=float], [frame=boolean], [freezeSelection=boolean], [grabFollowPath=boolean], [grabSilhouette=boolean], [grabTwist=boolean], [inverted=boolean], [lastMode=string], [lockShellBorder=boolean], [makeStroke=[uint, uint, uint, float, float]], [minSize=float], [minStrength=float], [mirror=int], [mode=string], [orientToSurface=boolean], [recordStroke=boolean], [sculptFalloffCurve=string], [size=float], [stampDistance=float], [stampFile=string], [stampFlipX=boolean], [stampFlipY=boolean], [stampOrientToStroke=boolean], [stampPlacement=int], [stampRandomization=boolean], [stampRandomizationSeed=int], [stampRandomizeFlipX=boolean], [stampRandomizeFlipY=boolean], [stampRandomizePosX=float], [stampRandomizePosY=float], [stampRandomizeRotation=float], [stampRandomizeScale=float], [stampRandomizeStrength=float], [stampRotation=float], [steadyStrokeDistance=float], [strength=float], [updatePlane=boolean], [useGlobalSize=boolean], [useScreenSpace=boolean], [useStampDistance=boolean], [useStampImage=boolean], [useSteadyStroke=boolean], [wholeStroke=boolean], [wireframeAlpha=float], [wireframeColor=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sculptMeshCacheCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a new sculpting context, then switch to it
cmds.sculptMeshCacheCtx('sculptMeshCacheContext')
cmds.setToolTo('sculptMeshCacheContext')

Set sculptMeshCacheContext's brush size to 10.0
cmds.sculptMeshCacheCtx('sculptMeshCacheContext', edit=True, sz=10.0)

---


Flags:
---


---
adjustSize(asz): boolean
    properties: edit
    If true, puts the tool into the mode where dragging the mouse will edit the brush size.
If false, puts the tool back into the previous sculpt mode.

---
adjustStrength(ast): boolean
    properties: edit
    If true, puts the tool into the mode where dragging the mouse will edit the brush strength.
If false, puts the tool back into the previous sculpt mode.

---
affectAllLayers(aal): boolean
    properties: create, query, edit
    If true, the brush affects all layers at once.

---
brushDirection(bd): int
    properties: query, edit
    Specifies the direction of the named brush.

---
brushSize(bsz): float
    properties: query, edit
    Specifies the world-space size of the named brush.

---
brushStrength(bst): float
    properties: query, edit
    Specifies the world-space strength of the named brush.

---
buildUpRate(bur): float
    properties: query, edit
    Specifies the brush strength increasing along the stroke.

---
cloneHideSource(chs): boolean
    properties: create, query, edit
    True if the cloned source should be hidden.

---
cloneMethod(cm): int
    properties: create, query, edit
    Controls how the source delta vectors should change the target. 0=copy 1=add

---
cloneShapeSource(css): string
    properties: create, query, edit
    Name of the shape source to clone.

---
cloneTargetSource(cas): string
    properties: create, query, edit
    Name of the target source of the clone.

---
constrainToSurface(cts): boolean
    properties: create, query, edit
    If true, the modification keeps the surface curvature.

---
direction(d): int
    properties: query, edit
    Specifies the direction in which the vertices are moved.

---
displayFrozen(df): boolean
    properties: create, query, edit
    If false, turns off the display of frozen area on the object.

---
displayMask(dm): boolean
    properties: create, query, edit
    If false, turns off the display of masked area on the object.

---
displayWireframe(dw): boolean
    properties: create, query, edit
    If false, turns off the wireframe display of the object.

---
falloffType(ft): int
    properties: query, edit
    Specifies how the brush determines which vertices to affect.

---
flood(fl): float
    properties: create, edit
    Sets the brush effect for each vertex to the given value.

---
floodFreeze(ff): float
    properties: create, edit
    Sets the freeze value for each vertex to the given value.

---
frame(frm): boolean
    properties: create, edit
    Frames on the sculpted area.

---
freezeSelection(fsl): boolean
    properties: create, edit
    Freezes selected components.

---
grabFollowPath(gfp): boolean
    properties: create, query, edit
    If true, the grab brush effect follows mouse movement.

---
grabSilhouette(gs): boolean
    properties: create, query, edit
    If true, the grab brush uses paint-through mode.

---
grabTwist(gtw): boolean
    properties: create, query, edit
    If true, the grab brush twists the vertices.

---
inverted(inv): boolean
    properties: create, query, edit
    If true, inverts the effect of the brush.

---
lastMode(lm): string
    properties: query, edit
    Specifies the type of the last active sculpting brush.

---
lockShellBorder(lsb): boolean
    properties: create, query, edit
    Lock the shell borders so that they won't be moved by a UV texture brush.

---
makeStroke(mt): [uint, uint, uint, float, float]
    properties: edit, multiuse
    Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke.
The first argument is the mesh index.
The second argument is the side index. use 0 for the original side, and 1 for the mirrored side
The third argument is the face index within the specified mesh.
The fourth and fifth arguments are the face coordinates within the specified face.

---
minSize(msz): float
    properties: query, edit
    Specifies the minimum size percentage of the current brush.

---
minStrength(mst): float
    properties: query, edit
    Specifies the minimum strength percentage of the current brush.

---
mirror(mr): int
    properties: query, edit
    Specifies the mirror mode of the brush.

---
mode(m): string
    properties: query, edit
    Specifies the type of sculpting effect the brush will perform.

---
orientToSurface(ots): boolean
    properties: create, query, edit
    If true, aligns the brush display to the surface of the mesh.

---
recordStroke(rcs): boolean
    properties: query, edit
    Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.

---
sculptFalloffCurve(sfc): string
    properties: query, edit
    Specifies the falloff curve of sculpting effect the brush will perform.

---
size(sz): float
    properties: query, edit
    Specifies the world-space size of the current brush.

---
stampDistance(s): float
    properties: query, edit
    Specifies the stamping distance of the brush.

---
stampFile(stp): string
    properties: query, edit
    Specifies an image file to use as stamp.

---
stampFlipX(sfx): boolean
    properties: create, query, edit
    Specifies if the brush stamp is flipped on the X axis.

---
stampFlipY(sfy): boolean
    properties: create, query, edit
    Specifies if the brush stamp is flipped on the Y axis.

---
stampOrientToStroke(sos): boolean
    properties: create, query, edit
    Specifies if the brush stamp is aligned to the stroke direction.

---
stampPlacement(sp): int
    properties: query, edit
    Specifies the placement mode of the stamp image.

---
stampRandomization(srd): boolean
    properties: create, query, edit
    Specifies if the brush stamp is randomized.

---
stampRandomizationSeed(sre): int
    properties: edit
    Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.

---
stampRandomizeFlipX(srx): boolean
    properties: create, query, edit
    Specifies if the brush stamp flipping is randomized on the X axis.

---
stampRandomizeFlipY(sry): boolean
    properties: create, query, edit
    Specifies if the brush stamp flipping is randomized on the Y axis.

---
stampRandomizePosX(spx): float
    properties: query, edit
    Specifies the stamp X position value is randomized.

---
stampRandomizePosY(spy): float
    properties: query, edit
    Specifies the stamp Y position value is randomized.

---
stampRandomizeRotation(srr): float
    properties: query, edit
    Specifies the stamp rotation value is randomized.

---
stampRandomizeScale(src): float
    properties: query, edit
    Specifies the stamp scale value is randomized.

---
stampRandomizeStrength(srs): float
    properties: query, edit
    Specifies the stamp strength value is randomized.

---
stampRotation(sr): float
    properties: query, edit
    Specifies the rotation value of the stamp image.

---
steadyStrokeDistance(ssd): float
    properties: query, edit
    Specifies the distance for the steady stroke.

---
strength(st): float
    properties: query, edit
    Specifies the world-space strength of the current brush.

---
updatePlane(upl): boolean
    properties: create, query, edit
    Recalculates the underlying tool plane for each stamp in a stroke.

---
useGlobalSize(ugs): boolean
    properties: create, query, edit
    If true, all the brushes have a shared size property; otherwise size is local.

---
useScreenSpace(ssp): boolean
    properties: create, query, edit
    If true, the brush size is in screen space pixels.

---
useStampDistance(usd): boolean
    properties: create, query, edit
    Force the stamps to be spread out along the stroke, rather than building up continually.

---
useStampImage(usi): boolean
    properties: create, query, edit
    Specifies if the brush uses a stamp image.

---
useSteadyStroke(uss): boolean
    properties: create, query, edit
    Turns using steady stroke on/off.

---
wholeStroke(wst): boolean
    properties: create, query, edit
    Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.

---
wireframeAlpha(wa): float
    properties: create, query, edit
    Sets the alpha value of the wireframe for the object that is being sculpted.

---
wireframeColor(wc): [float, float, float]
    properties: create, query, edit
    Sets the color of the wireframe for the object that is being sculpted.
Values should be 0-1 RGB.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sculptMeshCacheCtx.html 
    """


def sculptTarget(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flaginbetweenWeight: float, flagincludeHiddenSelections: boolean, flagname: string, flagparallel: boolean, flagprune: boolean, flagregenerate: boolean, flagremove: boolean, flagselectedComponents: boolean, flagsnapshot: int, flagsplit: boolean, flagtarget: int, flaguseComponentTags: boolean) -> None:
    """Synopsis:
---
---
 sculptTarget(
int
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [deformerTools=boolean], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [inbetweenWeight=float], [includeHiddenSelections=boolean], [name=string], [parallel=boolean], [prune=boolean], [regenerate=boolean], [remove=boolean], [selectedComponents=boolean], [snapshot=int], [split=boolean], [target=int], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sculptTarget is undoable, NOT queryable, and editable.



Example:
---
import maya.cmds as cmds

To set the current editable target to target 3
cmds.sculptTarget( 'blendShape1', e=True, t=3 )

To set the current editable target to none
cmds.sculptTarget( 'blendShape1', e=True, t=-1 )

---


Flags:
---


---
after(af): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node after the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
afterReference(ar): boolean
    properties: create, edit
    The -afterReference flag is used to specify deformer ordering in a hybrid way that
choses between -before and -after automatically. If the geometry being
deformed is referenced then the -after mode is used when adding the new deformer,
otherwise the -before mode is used. The net effect when using -afterReference to build
deformer chains is that internal shape nodes in the deformer chain will only
appear at reference file boundaries, leading to lightweight deformer networks that
may be more amicable to reference swapping.

---
before(bf): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node before the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
components(cmp): boolean
    properties: 
    Returns the components used by the deformer

---
deformerTools(dt): boolean
    properties: 
    Returns the name of the deformer tool objects (if any)
as string string ...

---
exclusive(ex): string
    properties: create
    Puts the deformation set in a deform partition.

---
frontOfChain(foc): boolean
    properties: create, edit
    This command is used to specify that the new deformer
node should be placed ahead (upstream) of existing deformer
and skin nodes in the shape's history (but not ahead of
existing tweak nodes). The input to the
deformer will be the upstream shape rather than the visible
downstream shape, so the behavior of this flag is the most
intuitive if the downstream deformers are in their reset
(hasNoEffect) position when the new deformer is added.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
geometry(g): string
    properties: edit, multiuse
    The specified object will be added to the list of
objects being deformed by this deformer object, unless
the -rm flag is also specified. When queried, this flag
returns string string string ...

---
geometryIndices(gi): boolean
    properties: 
    Complements the -geometry flag in query mode. Returns
the multi index of each geometry.

---
ignoreSelected(ignoreSelected): boolean
    properties: create
    Tells the command to not deform objects on the
current selection list

---
inbetweenWeight(ibw): float
    properties: edit
    Specifies the in between target weight of the blend shape node that will be
made editable by the sculpting and transform tools.

---
includeHiddenSelections(ihs): boolean
    properties: create
    Apply the deformer to any visible and hidden objects in the selection list.
Default is false.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
prune(pr): boolean
    properties: edit
    Removes any points not being deformed by the deformer in
its current configuration from the deformer set.

---
regenerate(r): boolean
    properties: edit
    When this flag is specified a new shape is created for the specified
blend shape target, if the shape does not already exist.
The name of the new shape is returned.

---
remove(rm): boolean
    properties: edit, multiuse
    Specifies that objects listed after the -g flag should
be removed from this deformer.

---
selectedComponents(cms): boolean
    properties: 
    Returns the components used by the deformer that are currently selected.
This intersects the current selection with the components affected by the deformer.

---
snapshot(s): int
    properties: edit
    This flag should only be used internally to add in-between target.
When this flag is specified a snapshot of the shape will be
taken for the specified in-between target when it does not
exist yet.
This flag specifies the base shape index and must be used with the
-target and -inbetweenWeight flags, which specify the in-between
target.

---
split(sp): boolean
    properties: create, edit
    Branches off a new chain in the dependency graph instead
of inserting/appending the deformer into/onto an
existing chain.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
target(t): int
    properties: edit
    Specifies the target index of the blend shape node that will be
made editable by the sculpting and transform tools.

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sculptTarget.html 
    """


def selLoadSettings(flagactiveProxy: string, flagdeferReference: boolean, flagfileName: string, flagnumSettings: uint, flagproxyManager: string, flagproxySetFiles: string, flagproxySetTags: string, flagproxyTag: string, flagreferenceNode: string, flagshortName: boolean, flagunresolvedName: boolean) -> string:
    """Synopsis:
---
---
 selLoadSettings([activeProxy=string], [deferReference=boolean], [fileName=string], [numSettings=uint], [proxyManager=string], [proxySetFiles=string], [proxySetTags=string], [proxyTag=string], [referenceNode=string], [shortName=boolean], [unresolvedName=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selLoadSettings is NOT undoable, queryable, and editable.
        a
       / \
      b   c
         / \
        d   e

a
|
b [-]
|
c [-]



Example:
---
import maya.cmds as cmds

Given the scene:
---

---

       a [+]
      /     \
     b [-]   c [+]
            /     \
           d [-]   e [+]
---

With the IDs:
   a = 0
   b = 1
   c = 2
   d = 3
   e = 4

set c, d, and e to the unloaded state
cmds.selLoadSettings( '2', '3', '4', e=True, deferReference=1 )

this will also set c, d, and e to the unloaded state
cmds.selLoadSettings( '2', e=True, deferReference=1 )

set b to the loaded state
cmds.selLoadSettings( '1', e=True, deferReference=0 )

set b and d to the loaded state
cmds.selLoadSettings( '1', '3', e=True, deferReference=0 )

---
Return:
---


    string: For query execution.

Flags:
---


---
activeProxy(ap): string
    properties: create, query, edit
    Change or query the active proxy of a proxy set. In query mode, returns the
proxyTag of the active proxy; in edit mode, finds the proxy in the proxySet
with the given tag and makes it the active proxy.

---
deferReference(dr): boolean
    properties: create, query, edit
    Change or query the load state of a reference.

---
fileName(fn): string
    properties: create, query
    Return the file name reference file(s) associated with the indicated load setting(s).

---
numSettings(ns): uint
    properties: create, query
    Return the number of settings in the group of implicit load settings. This is
equivalent to number of references in the scene plus 1.

---
proxyManager(pm): string
    properties: create, query
    Return the name(s) of the proxy manager(s) associated with the indicated load setting(s).

---
proxySetFiles(psf): string
    properties: create, query
    Return the name(s) of the proxy(ies) available in the proxy set associated with the indicated load setting(s).

---
proxySetTags(pst): string
    properties: create, query
    Return the name(s) of the proxy tag(s) available in the proxy set associated with the indicated load setting(s).

---
proxyTag(pt): string
    properties: create, query
    Return the name(s) of the proxy tag(s) associated with the indicated load setting(s).

---
referenceNode(rfn): string
    properties: create, query
    Return the name(s) of the reference node(s) associated with the indicated load setting(s).

---
shortName(shn): boolean
    properties: create, query
    Formats the return value of the 'fileName' query flag to only return the short
name(s) of the reference file(s).

---
unresolvedName(un): boolean
    properties: create, query
    Formats the return value of the 'fileName' query flag to return the unresolved
name(s) of the reference file(s). The unresolved file name is the file name
used when the reference was created, whether or not that file actually exists
on disk. When Maya encounters a file name which does not exist on disk it
attempts to resolve the name by looking for the file in a number of other
locations. By default the 'fileName' flag will return this resolved value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selLoadSettings.html 
    """


def select(flagadd: boolean, flagaddFirst: boolean, flagall: boolean, flagallDagObjects: boolean, flagallDependencyNodes: boolean, flagclear: boolean, flagcontainerCentric: boolean, flagdeselect: boolean, flaghierarchy: boolean, flagnoExpand: boolean, flagreplace: boolean, flagsymmetry: boolean, flagsymmetrySide: int, flagtoggle: boolean, flagvisible: boolean) -> None:
    """Synopsis:
---
---
 select(
[objects...]
    , [add=boolean], [addFirst=boolean], [all=boolean], [allDagObjects=boolean], [allDependencyNodes=boolean], [clear=boolean], [containerCentric=boolean], [deselect=boolean], [hierarchy=boolean], [noExpand=boolean], [replace=boolean], [symmetry=boolean], [symmetrySide=int], [toggle=boolean], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

select is undoable, NOT queryable, and NOT editable.
When selecting a set as in "select set1", the behaviour is for all
the members of the set to become selected instead of the set itself.
If you want to select a set, the "-ne/noExpand" flag must be used.

With the advent of namespaces, selection by name may be
confusing.  To clarify, without a qualified namespace, name
lookup is limited to objects in the root namespace ":". There
are really two parts of a name: the namespace and the name
itself which is unique within the namespace. If you want to
select objects in a specific namespace, you need to include
the namespace separator ":".

For example, 'select -r "foo*"' is trying to look for an
object with the "foo" prefix in the root namespace. It is not
trying to look for all objects in the namespace with the "foo"
prefix. If you want to select all objects in a namespace
(foo), use 'select "foo:*"'.

Note: When the application starts up, there are several dependency nodes
created by the system which must exist. These objects are not deletable
but are selectable.  All objects (dag and dependency nodes) in the scene
can be obtained using the "ls" command without any arguments. When using
the "-all", "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only
the deletable objects are selected.  The non deletable object can still
be selected by explicitly specifying their name as in "select time1;".




Example:
---
import maya.cmds as cmds

create some objects and add them to a set
cmds.sphere( n='sphere1' )
cmds.sphere( n='sphere2' )
cmds.sets( 'sphere1', 'sphere2', n='set1' )

select all dag objects and all dependency nodes
cmds.select( all=True )

clear the active list
cmds.select( clear=True )

select sphere2 only if it is visible
cmds.select( 'sphere2', visible=True )

select a couple of objects regardless of visibilty
cmds.select( 'sphere1', r=True )
cmds.select( 'sphere2', add=True )

remove one of the spheres from the active list (using toggle)
cmds.select( 'sphere1', tgl=True )

remove the other sphere from the active list
cmds.select( 'sphere2', d=True )

the following selects all the members of set1
cmds.select( 'set1' )

this selects set1 itself
cmds.select( 'set1', ne=True )


Some examples selecting with namespaces:

create a namespace and an object in the namespace
cmds.namespace( add='foo' )
cmds.namespace( set='foo' )
cmds.sphere( n='bar' )

'select bar' will not select "bar" unless bar is in the
root namespace. You need to qualify the name with the
namespace (shown below).
cmds.select( 'foo:bar' )

select all the objects in a namespace
cmds.select( 'foo:*' )

---


Flags:
---


---
add(add): boolean
    properties: create
    Indicates that the specified items should be
added to the active list without removing existing
items from the active list.

---
addFirst(af): boolean
    properties: create
    Indicates that the specified items should be
added to the front of the active list without
removing existing items from the active list.

---
all(all): boolean
    properties: create
    Indicates that all deletable root level dag objects
and all deletable non-dag dependency nodes should be
selected.

---
allDagObjects(ado): boolean
    properties: create
    Indicates that all deletable root level dag objects
should be selected.

---
allDependencyNodes(adn): boolean
    properties: create
    Indicates that all deletable dependency nodes
including all deletable dag objects should be selected.

---
clear(cl): boolean
    properties: create
    Clears the active list.  This is more efficient than
"select -d;".  Also "select -d;" will not remove sets
from the active list unless the "-ne" flag is also
specified.

---
containerCentric(cc): boolean
    properties: create
    Specifies that the same selection rules as apply to selection in the main
viewport will also be applied to the select command. In particular, if
the specified objects are members of a black-boxed container and are not
published as nodes, Maya will not select them. Instead, their first parent
valid for selection will be selected.

---
deselect(d): boolean
    properties: create
    Indicates that the specified items should
be removed from the active list if they are on the
active list.

---
hierarchy(hi): boolean
    properties: create
    Indicates that all children, grandchildren, ...
of the specified dag objects should also be selected.

---
noExpand(ne): boolean
    properties: create
    Indicates that any set which is among the specified
items should not be expanded to its list of members.
This allows sets to be selected as opposed to
the members of sets which is the default behaviour.

---
replace(r): boolean
    properties: create
    Indicates that the specified items should
replace the existing items on the active list.

---
symmetry(sym): boolean
    properties: create
    Specifies that components should be selected symmetrically using the
current symmetricModelling command settings. If symmetric modeling
is not enabled then this flag has no effect.

---
symmetrySide(sys): int
    properties: create
    Indicates that components involved in the current symmetry
object should be selected, according to the supplied parameter.
Valid values for the parameter are:
-1 : Select components in the unsymmetrical region.
0 : Select components on the symmetry seam.
1 : Select components on side 1.
2 : Select components on side 2.
If symmetric modeling is not enabled then this flag has no effect.
Note: currently only works for topological symmetry.

---
toggle(tgl): boolean
    properties: create
    Indicates that those items on the given list which
are on the active list should be removed from the active
list and those items on the given list which are not on
the active list should be added to the active list.

---
visible(vis): boolean
    properties: create
    Indicates that of the specified items only those
that are visible should be affected.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/select.html 
    """


def selectContext(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 selectContext(
string
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a new select context, then switch to it
cmds.selectContext('selectContext1')
cmds.setToolTo('selectContext1')

---
Return:
---


    string: Name of the context created

Flags:
---


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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectContext.html 
    """


def selectKey(flagaddTo: boolean, flaganimation: string, flagattribute: string, flagclear: boolean, flagcontrolPoints: boolean, flagfloat: floatrange, flaghierarchy: string, flaginTangent: boolean, flagincludeUpperBound: boolean, flagindex: uint, flagkeyframe: boolean, flagoutTangent: boolean, flagremove: boolean, flagreplace: boolean, flagshape: boolean, flagtime: timerange, flagtoggle: boolean, flagunsnappedKeys: float) -> int:
    """Synopsis:
---
---
 selectKey(
[targetList]
    , [addTo=boolean], [animation=string], [attribute=string], [clear=boolean], [controlPoints=boolean], [float=floatrange], [hierarchy=string], [inTangent=boolean], [includeUpperBound=boolean], [index=uint], [keyframe=boolean], [outTangent=boolean], [remove=boolean], [replace=boolean], [shape=boolean], [time=timerange], [toggle=boolean], [unsnappedKeys=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectKey is undoable, NOT queryable, and NOT editable.
The animation curves comprising a keyset depend on the value
of the "-animation" flag:


keysOrObjects:

Any active keys, when no target objects or -attribute
flags appear on the command line, or

All animation curves connected to all keyframable
attributes of objects specified as the command line's
targetList, when there are no active keys.




keys:
Only act on active keys or tangents.
If there are no active keys or tangents, don't do anything.



objects:
Only act on specified objects.  If there are no objects specified, don't
do anything.



Note that the "-animation" flag can be used to override
the curves uniquely identified by the multi-use
"-attribute" flag, which takes an argument of the form
attributeName, such as "translateX".

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given individually or as part of a list or range (see Examples).

This command places keyframes and/or keyframe tangents
on the active list.




Example:
---
import maya.cmds as cmds

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given as a range or list of ranges.

time=('10pal','10pal') means the key at frame 10 (PAL format).
time=[('1.0sec','1.0sec'),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
time=(10,None) means all keys from time 10 (in the current time unit) onwards.
time=(10,) means the same as (10,10)
time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
time=(None,None) is a short form to specify all keys.
index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.

Select all translateX keyframes on nurbsSphere1 in the range 10 to 20.
---

cmds.selectKey( 'nurbsSphere1', time=(10,20), attribute='translateX' )

select all the animation of the active objects, range 0-30
---

cmds.selectKey( time=(0,30) )

---
Return:
---


    int: The number of curves on which keys were
selected (or deselcted).

Flags:
---


---
addTo(add): boolean
    properties: create
    Add to the current selection of keyframes/tangents

---
animation(an): string
    properties: create
    Where this command should get the animation to act
on.  Valid values are "objects," "keys," and
"keysOrObjects" Default: "keysOrObjects."  (See
Description for details.)

---
attribute(at): string
    properties: create, multiuse
    List of attributes to select
      In query mode, this flag needs a value.

---
clear(cl): boolean
    properties: create
    Remove all keyframes and tangents from the active list.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
float(f): floatrange
    properties: create, multiuse
    value uniquely representing a non-time-based
key (or key range) on a time-based animCurve.  Valid
floatRange include single values (-f 10) or a
string with a lower and upper bound, separated by a
colon (-f "10:20")
      In query mode, this flag needs a value.

---
hierarchy(hi): string
    properties: create
    Hierarchy expansion options.  Valid values are "above,"
"below," "both," and "none." (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
inTangent(it): boolean
    properties: create
    Select in-tangents of keyframes in the specified time range

---
includeUpperBound(iub): boolean
    properties: create
    When the -t/time or -f/float flags represent a range
of keys, this flag determines whether the keys at the
upper bound of the range are included in the keyset.
Default value: true.  This flag is only valid when
the argument to the -t/time flag is a time range with
a lower and upper bound.  (When used with the "pasteKey"
command, this flag refers only to the time range of the
target curve that is replaced, when using options such
as "replace," "fitReplace," or "scaleReplace."  This
flag has no effect on the curve pasted from the clipboard.)

---
index(index): uint
    properties: create, multiuse
    index of a key on an animCurve
      In query mode, this flag needs a value.

---
keyframe(k): boolean
    properties: create
    select only keyframes (cannot be combined with -in/-out)

---
outTangent(ot): boolean
    properties: create
    Select out-tangents of keyframes in the specified time range

---
remove(rm): boolean
    properties: create
    Remove from the current selection of keyframes/tangents

---
replace(r): boolean
    properties: create
    Replace the current selection of keyframes/tangents

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

---
toggle(tgl): boolean
    properties: create
    Toggle the picked state of the specified keyset

---
unsnappedKeys(uk): float
    properties: create
    Select only keys that have times that are not a multiple of
the specified numeric value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectKey.html 
    """


def selectKeyCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> None:
    """Synopsis:
---
---
 selectKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a select key context for the graph editor
---

cmds.selectKeyCtx( 'selectKeyContext' )

---


Flags:
---


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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectKeyCtx.html 
    """


def selectKeyframeRegionCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> None:
    """Synopsis:
---
---
 selectKeyframeRegionCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectKeyframeRegionCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a select key context for the dope sheet editor
---

cmds.selectKeyframeRegionCtx( 'selectKeyframeRegionContext' )

---


Flags:
---


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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectKeyframeRegionCtx.html 
    """


def selectMode(flagcomponent: boolean, flaghierarchical: boolean, flagleaf: boolean, flagobject: boolean, flagpreset: boolean, flagroot: boolean, flagtemplate: boolean) -> boolean:
    """Synopsis:
---
---
 selectMode([component=boolean], [hierarchical=boolean], [leaf=boolean], [object=boolean], [preset=boolean], [root=boolean], [template=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectMode is undoable, queryable, and NOT editable.selectMode



Example:
---
import maya.cmds as cmds

cmds.selectMode( object=True )
cmds.selectMode( q=True, component=True )

---
Return:
---


    boolean: if a query operation

Flags:
---


---
component(co): boolean
    properties: create, query
    Set component selection on. Component selection mode allows
filtered selection based on the component selection mask.
The component selection mask is the set of selection masks
related to objects that indicate which components are
selectable.

---
hierarchical(h): boolean
    properties: create, query
    Set hierarchical selection on. There are
three types of hierarchical selection: root, leaf and
template.  Hierarchical mode is set if root, leaf or
template mode is set. Setting to hierarchical mode
will set the mode to whichever of root, leaf, or
template was last on.

---
leaf(l): boolean
    properties: create, query
    Set leaf selection mode on.  This mode allows the leaf
level objects to be selected.  It is similar to object
selection mode but ignores the object selection mask.

---
object(o): boolean
    properties: create, query
    Set object selection on. Object selection mode allows
filtered selection based on the object selection mask.
The object selection mask is the set of selection masks
related to objects that indicate which objects are
selectable.  The masks are controlled by the "selectType"
command.  Object selection mode selects the leaf level
objects.

---
preset(p): boolean
    properties: create, query
    Allow selection of anything with the mask set,
independent of it being an object or a component.

---
root(r): boolean
    properties: create, query
    Set root selection mode on.  This mode allows
the root of a hierarchy to be selected by selecting
any of its descendents.  It ignores the object selection
mask.

---
template(t): boolean
    properties: create, query
    Set template selection mode on.  This mode allows
selection of templated objects.  It selects the templated
object closest to the root of the hierarchy.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectMode.html 
    """


def selectPref(flagaffectsActive: boolean, flagallowHiliteSelection: boolean, flagautoSelectContainer: boolean, flagautoSelectOutlinerSetMembers: boolean, flagautoUseDepth: boolean, flagclickBoxSize: uint, flagclickDrag: boolean, flagcontainerCentricSelection: boolean, flagdisableComponentPopups: boolean, flagexpandPopupList: boolean, flagignoreSelectionPriority: boolean, flagmanipClickBoxSize: uint, flagpaintSelect: boolean, flagpaintSelectWithDepth: boolean, flagpopupMenuSelection: boolean, flagpreSelectBackfacing: boolean, flagpreSelectClosest: boolean, flagpreSelectDeadSpace: uint, flagpreSelectHilite: boolean, flagpreSelectHiliteSize: float, flagpreSelectTweakDeadSpace: uint, flagselectTypeChangeAffectsActive: boolean, flagselectionChildHighlightMode: int, flagsingleBoxSelection: boolean, flagstraightLineDistance: boolean, flagtrackSelectionOrder: boolean, flaguseDepth: boolean, flagxformNoSelect: boolean) -> boolean:
    """Synopsis:
---
---
 selectPref([affectsActive=boolean], [allowHiliteSelection=boolean], [autoSelectContainer=boolean], [autoSelectOutlinerSetMembers=boolean], [autoUseDepth=boolean], [clickBoxSize=uint], [clickDrag=boolean], [containerCentricSelection=boolean], [disableComponentPopups=boolean], [expandPopupList=boolean], [ignoreSelectionPriority=boolean], [manipClickBoxSize=uint], [paintSelect=boolean], [paintSelectWithDepth=boolean], [popupMenuSelection=boolean], [preSelectBackfacing=boolean], [preSelectClosest=boolean], [preSelectDeadSpace=uint], [preSelectHilite=boolean], [preSelectHiliteSize=float], [preSelectTweakDeadSpace=uint], [selectTypeChangeAffectsActive=boolean], [selectionChildHighlightMode=int], [singleBoxSelection=boolean], [straightLineDistance=boolean], [trackSelectionOrder=boolean], [useDepth=boolean], [xformNoSelect=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectPref is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.selectPref(popupMenuSelection=True,disableComponentPopups=True)

---
Return:
---


    boolean: in the query mode.

Flags:
---


---
affectsActive(aa): boolean
    properties: create, query
    Set affects-active toggle which when on
causes the active list to be affected when
changing between object and component
selection mode.

---
allowHiliteSelection(ahs): boolean
    properties: create, query
    When in component selection mode, allow selection of
objects for editing.  If an object is selected for
editing, it appears in the hilite color and its
selectable components are automatically displayed.

---
autoSelectContainer(asc): boolean
    properties: query
    When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.

---
autoSelectOutlinerSetMembers(asm): boolean
    properties: query
    When enabled selecting a set in the Outliner will automatically select the set members instead.

---
autoUseDepth(aud): boolean
    properties: query
    When enabled, useDepth and paintSelectWithDepth will be automatically enabled
in shaded display mode and disabled in wireframe display mode.

---
clickBoxSize(cbs): uint
    properties: create, query
    When click selecting, this value defines the size of
square picking region surrounding the cursor. The size of
the square is twice the specified value. That is, the
value defines the amount of space on all four sides of the
cursor position. The size must be positive.

---
clickDrag(cld): boolean
    properties: create, query
    Set click/drag selection interaction on/off

---
containerCentricSelection(ccs): boolean
    properties: query
    When enabled, selecting any DAG node in a container in the viewport will select the container's
root transform if there is one.  If there is no root transform then the highest
DAG node in the container will be selected.  There is no effect when selecting
nodes which are not in a container.

---
disableComponentPopups(dcp): boolean
    properties: create, query
    A separate preference to allow users to disable popup
menus when selecting components.  This pref is only meaningful
if the popupMenuSelection pref is enabled.

---
expandPopupList(epl): boolean
    properties: create, query
    When in popup selection mode, if this is set then
all selection items that contain multiple objects or
components will be be expanded such that each object or
component will be a single new selection item.

---
ignoreSelectionPriority(isp): boolean
    properties: create, query
    If this is set, selection priority will be ignored
when performing selection.

---
manipClickBoxSize(mcb): uint
    properties: create, query
    When selecting a manipulator, this value defines the size of
square picking region surrounding the cursor. The size of
the square is twice the specified value. That is, the
value defines the amount of space on all four sides of the
cursor position. The size must be positive.

---
paintSelect(ps): boolean
    properties: query
    When enabled, the select tool will use drag selection instead of marquee selection.

---
paintSelectWithDepth(psd): boolean
    properties: query
    When enabled, paint selection will not select components that are behind the surface
in the current camera view.

---
popupMenuSelection(pms): boolean
    properties: create, query
    If this is set, a popup menu will be displayed
and used to determine the object to select. The menu
lists the current user box (marquee) of selected
candidate objects.

---
preSelectBackfacing(psb): boolean
    properties: query
    When enabled preselection will highlight backfacing components whose normals face away from the camera.

---
preSelectClosest(psc): boolean
    properties: query
    When enabled and the cursor is over a surface, preselection highlighting will try
to preselect the closest component to the cursor regardless of distance.

---
preSelectDeadSpace(pds): uint
    properties: query
    This value defines the size of the region around the cursor used for preselection highlighting
when the cursor is outside the surface.

---
preSelectHilite(psh): boolean
    properties: query
    When enabled, the closest component under the cursor will be highlighted to indicate that
clicking will select that component.

---
preSelectHiliteSize(phs): float
    properties: query
    This value defines the size of the region around the cursor used for preselection highlighting.
Within this region the closest component to the cursor will be highlighted.

---
preSelectTweakDeadSpace(pdt): uint
    properties: query
    This value defines the size of the region around the cursor used for preselection highlighting
when the cursor is outside the surface in tweak mode.

---
selectTypeChangeAffectsActive(stc): boolean
    properties: query
    If true then the active list will be updated according to the new selection preferences.

---
selectionChildHighlightMode(sch): int
    properties: create, query
    Controls the highlighting of the children of a selected object. Valid modes are:

0: Always highlight children
1: Never highlight children
2: Use per-object "Selection Child Highlight" setting.

Default mode is (0): Always highlight children.

For (2), each DAG object has an individual "Selection Child Highlight" boolean flag.
By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred
to the selected object's "Selection Child Highlight" flag.

---
singleBoxSelection(sbs): boolean
    properties: create, query
    Set single box selection on/off.
This flag indicates whether just single object
will be selected when the user box (marquee) selects
several objects if flag set to true.  Otherwise, all
those objects inside the box will be selected.

---
straightLineDistance(sld): boolean
    properties: query
    If true then use straight line distances for selection proximity.

---
trackSelectionOrder(tso): boolean
    properties: query
    When enabled, the order of selected objects and components will be tracked.  The 'ls' command will be able
to return the active list in the order of selection which will allow scripts to be written that depend
on the order.

---
useDepth(ud): boolean
    properties: query
    When enabled, marquee selection will not select components that are behind the surface
in the current camera view.

---
xformNoSelect(xns): boolean
    properties: create, query
    Disable selection in xform tools

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectPref.html 
    """


def selectPriority(flagallComponents: uint, flagallObjects: uint, flaganimBreakdown: uint, flaganimCurve: uint, flaganimInTangent: uint, flaganimKeyframe: uint, flaganimOutTangent: uint, flagbyName: tuple[string, boolean], flagcamera: uint, flagcluster: uint, flagcollisionModel: uint, flagcontrolVertex: uint, flagcurve: uint, flagcurveKnot: uint, flagcurveOnSurface: uint, flagcurveParameterPoint: uint, flagdimension: uint, flagdynamicConstraint: uint, flagedge: uint, flageditPoint: uint, flagemitter: uint, flagfacet: uint, flagfield: uint, flagfluid: uint, flagfollicle: uint, flaghairSystem: uint, flaghandle: uint, flaghull: uint, flagikEndEffector: uint, flagikHandle: uint, flagimagePlane: uint, flagimplicitGeometry: uint, flagisoparm: uint, flagjoint: uint, flagjointPivot: uint, flaglattice: uint, flaglatticePoint: uint, flaglight: uint, flaglocalRotationAxis: uint, flaglocator: uint, flaglocatorUV: uint, flaglocatorXYZ: uint, flagmeshUVShell: uint, flagmotionTrailPoint: uint, flagmotionTrailTangent: uint, flagnCloth: uint, flagnParticle: uint, flagnParticleShape: uint, flagnRigid: uint, flagnonlinear: uint, flagnurbsCurve: uint, flagnurbsSurface: uint, flagorientationLocator: uint, flagparticle: uint, flagparticleShape: uint, flagplane: uint, flagpolymesh: uint, flagpolymeshEdge: uint, flagpolymeshFace: uint, flagpolymeshFreeEdge: uint, flagpolymeshUV: uint, flagpolymeshVertex: uint, flagpolymeshVtxFace: uint, flagqueryByName: string, flagrigidBody: uint, flagrigidConstraint: uint, flagrotatePivot: uint, flagscalePivot: uint, flagsculpt: uint, flagselectHandle: uint, flagspring: uint, flagspringComponent: uint, flagstroke: uint, flagsubdiv: uint, flagsubdivMeshEdge: uint, flagsubdivMeshFace: uint, flagsubdivMeshPoint: uint, flagsubdivMeshUV: uint, flagsurfaceEdge: uint, flagsurfaceFace: uint, flagsurfaceKnot: uint, flagsurfaceParameterPoint: uint, flagsurfaceRange: uint, flagtexture: uint, flagvertex: uint) -> int:
    """Synopsis:
---
---
 selectPriority([allComponents=uint], [allObjects=uint], [animBreakdown=uint], [animCurve=uint], [animInTangent=uint], [animKeyframe=uint], [animOutTangent=uint], [byName=[string, boolean]], [camera=uint], [cluster=uint], [collisionModel=uint], [controlVertex=uint], [curve=uint], [curveKnot=uint], [curveOnSurface=uint], [curveParameterPoint=uint], [dimension=uint], [dynamicConstraint=uint], [edge=uint], [editPoint=uint], [emitter=uint], [facet=uint], [field=uint], [fluid=uint], [follicle=uint], [hairSystem=uint], [handle=uint], [hull=uint], [ikEndEffector=uint], [ikHandle=uint], [imagePlane=uint], [implicitGeometry=uint], [isoparm=uint], [joint=uint], [jointPivot=uint], [lattice=uint], [latticePoint=uint], [light=uint], [localRotationAxis=uint], [locator=uint], [locatorUV=uint], [locatorXYZ=uint], [meshUVShell=uint], [motionTrailPoint=uint], [motionTrailTangent=uint], [nCloth=uint], [nParticle=uint], [nParticleShape=uint], [nRigid=uint], [nonlinear=uint], [nurbsCurve=uint], [nurbsSurface=uint], [orientationLocator=uint], [particle=uint], [particleShape=uint], [plane=uint], [polymesh=uint], [polymeshEdge=uint], [polymeshFace=uint], [polymeshFreeEdge=uint], [polymeshUV=uint], [polymeshVertex=uint], [polymeshVtxFace=uint], [queryByName=string], [rigidBody=uint], [rigidConstraint=uint], [rotatePivot=uint], [scalePivot=uint], [sculpt=uint], [selectHandle=uint], [spring=uint], [springComponent=uint], [stroke=uint], [subdiv=uint], [subdivMeshEdge=uint], [subdivMeshFace=uint], [subdivMeshPoint=uint], [subdivMeshUV=uint], [surfaceEdge=uint], [surfaceFace=uint], [surfaceKnot=uint], [surfaceParameterPoint=uint], [surfaceRange=uint], [texture=uint], [vertex=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectPriority is undoable, queryable, and NOT editable.selectPriority



Example:
---
import maya.cmds as cmds

cmds.selectPriority( q=True, nurbsCurve=True )
cmds.selectPriority( nurbsCurve=10 )
cmds.selectPriority( handle=9, ikHandle=8 )

---
Return:
---


    int: if a query operation

Flags:
---


---
allComponents(alc): uint
    properties: create, query
    Set all component selection priority

---
allObjects(alo): uint
    properties: create, query
    Set all object selection priority

---
animBreakdown(abd): uint
    properties: create, query
    Set animation breakdown selection priority

---
animCurve(ac): uint
    properties: create, query
    Set animation curve selection priority

---
animInTangent(ait): uint
    properties: create, query
    Set animation in-tangent selection priority

---
animKeyframe(ak): uint
    properties: create, query
    Set animation keyframe selection priority

---
animOutTangent(aot): uint
    properties: create, query
    Set animation out-tangent selection priority

---
byName(bn): [string, boolean]
    properties: create, multiuse
    Set selection priority for the specified user-defined selection type

---
camera(ca): uint
    properties: create, query
    Set camera selection priority

---
cluster(cl): uint
    properties: create, query
    Set cluster selection priority

---
collisionModel(clm): uint
    properties: create, query
    Set collision model selection priority

---
controlVertex(cv): uint
    properties: create, query
    Set control vertex selection priority

---
curve(c): uint
    properties: create, query
    Set curve selection priority

---
curveKnot(ck): uint
    properties: create, query
    Set curve knot selection priority

---
curveOnSurface(cos): uint
    properties: create, query
    Set curve-on-surface selection priority

---
curveParameterPoint(cpp): uint
    properties: create, query
    Set curve parameter point selection priority

---
dimension(dim): uint
    properties: create, query
    Set dimension shape selection priority

---
dynamicConstraint(dc): uint
    properties: create, query
    Set dynamicConstraint selection priority

---
edge(eg): uint
    properties: create, query
    Set mesh edge selection priority

---
editPoint(ep): uint
    properties: create, query
    Set edit-point selection priority

---
emitter(em): uint
    properties: create, query
    Set emitter selection priority

---
facet(fc): uint
    properties: create, query
    Set mesh face selection priority

---
field(fi): uint
    properties: create, query
    Set field selection priority

---
fluid(fl): uint
    properties: create, query
    Set fluid selection priority

---
follicle(fo): uint
    properties: create, query
    Set follicle selection priority

---
hairSystem(hs): uint
    properties: create, query
    Set hairSystem selection priority

---
handle(ha): uint
    properties: create, query
    Set object handle selection priority

---
hull(hl): uint
    properties: create, query
    Set hull selection priority

---
ikEndEffector(iee): uint
    properties: create, query
    Set ik end effector selection priority

---
ikHandle(ikh): uint
    properties: create, query
    Set ik handle selection priority

---
imagePlane(ip): uint
    properties: create, query
    Set image plane selection mask priority

---
implicitGeometry(ig): uint
    properties: create, query
    Set implicit geometry selection priority

---
isoparm(iso): uint
    properties: create, query
    Set surface iso-parm selection priority

---
joint(j): uint
    properties: create, query
    Set ik handle selection priority

---
jointPivot(jp): uint
    properties: create, query
    Set joint pivot selection priority

---
lattice(la): uint
    properties: create, query
    Set lattice selection priority

---
latticePoint(lp): uint
    properties: create, query
    Set lattice point selection priority

---
light(lt): uint
    properties: create, query
    Set light selection priority

---
localRotationAxis(ra): uint
    properties: create, query
    Set local rotation axis selection priority

---
locator(lc): uint
    properties: create, query
    Set locator (all types) selection priority

---
locatorUV(luv): uint
    properties: create, query
    Set uv locator selection priority

---
locatorXYZ(xyz): uint
    properties: create, query
    Set xyz locator selection priority

---
meshUVShell(msh): uint
    properties: create, query
    Set uv shell component mask on/off.

---
motionTrailPoint(mtp): uint
    properties: create, query
    Set motion point selection priority

---
motionTrailTangent(mtt): uint
    properties: create, query
    Set motion point tangent priority

---
nCloth(ncl): uint
    properties: create, query
    Set nCloth selection priority

---
nParticle(npr): uint
    properties: create, query
    Set nParticle point selection priority

---
nParticleShape(nps): uint
    properties: create, query
    Set nParticle shape selection priority

---
nRigid(nr): uint
    properties: create, query
    Set nRigid selection priority

---
nonlinear(nl): uint
    properties: create, query
    Set nonlinear selection priority

---
nurbsCurve(nc): uint
    properties: create, query
    Set nurbs-curve selection priority

---
nurbsSurface(ns): uint
    properties: create, query
    Set nurbs-surface selection priority

---
orientationLocator(ol): uint
    properties: create, query
    Set orientation locator selection priority

---
particle(pr): uint
    properties: create, query
    Set particle point selection priority

---
particleShape(ps): uint
    properties: create, query
    Set particle shape selection priority

---
plane(pl): uint
    properties: create, query
    Set sketch plane selection priority

---
polymesh(p): uint
    properties: create, query
    Set poly-mesh selection priority

---
polymeshEdge(pe): uint
    properties: create, query
    Set poly-mesh edge selection priority

---
polymeshFace(pf): uint
    properties: create, query
    Set poly-mesh face selection priority

---
polymeshFreeEdge(pfe): uint
    properties: create, query
    Set poly-mesh free-edge selection priority

---
polymeshUV(puv): uint
    properties: create, query
    Set poly-mesh UV point selection priority

---
polymeshVertex(pv): uint
    properties: create, query
    Set poly-mesh vertex selection priority

---
polymeshVtxFace(pvf): uint
    properties: create, query
    Set poly-mesh vtxFace selection priority

---
queryByName(qbn): string
    properties: query
    Query selection priority for the specified user-defined selection type
      In query mode, this flag needs a value.

---
rigidBody(rb): uint
    properties: create, query
    Set rigid body selection priority

---
rigidConstraint(rc): uint
    properties: create, query
    Set rigid constraint selection priority

---
rotatePivot(rp): uint
    properties: create, query
    Set rotate pivot selection priority

---
scalePivot(sp): uint
    properties: create, query
    Set scale pivot selection priority

---
sculpt(sc): uint
    properties: create, query
    Set sculpt selection priority

---
selectHandle(sh): uint
    properties: create, query
    Set select handle selection priority

---
spring(spr): uint
    properties: create, query
    Set spring shape selection priority

---
springComponent(spc): uint
    properties: create, query
    Set individual spring selection priority

---
stroke(str): uint
    properties: create, query
    Set stroke selection priority

---
subdiv(sd): uint
    properties: create, query
    Set subdivision surface selection priority

---
subdivMeshEdge(sme): uint
    properties: create, query
    Set subdivision surface mesh edge selection priority

---
subdivMeshFace(smf): uint
    properties: create, query
    Set subdivision surface mesh face selection priority

---
subdivMeshPoint(smp): uint
    properties: create, query
    Set subdivision surface mesh point selection priority

---
subdivMeshUV(smu): uint
    properties: create, query
    Set subdivision surface mesh UV map selection priority

---
surfaceEdge(se): uint
    properties: create, query
    Set surface edge selection priority

---
surfaceFace(sf): uint
    properties: create, query
    Set surface face selection priority

---
surfaceKnot(sk): uint
    properties: create, query
    Set surface knot selection priority

---
surfaceParameterPoint(spp): uint
    properties: create, query
    Set surface parameter point selection priority

---
surfaceRange(sr): uint
    properties: create, query
    Set surface range selection priority

---
texture(tx): uint
    properties: create, query
    Set texture selection priority

---
vertex(v): uint
    properties: create, query
    Set mesh vertex selection priority

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectPriority.html 
    """


def selectType(flagallComponents: boolean, flagallObjects: boolean, flaganimBreakdown: boolean, flaganimCurve: boolean, flaganimInTangent: boolean, flaganimKeyframe: boolean, flaganimOutTangent: boolean, flagbyName: tuple[string, boolean], flagcamera: boolean, flagcluster: boolean, flagcollisionModel: boolean, flagcontrolVertex: boolean, flagcurve: boolean, flagcurveKnot: boolean, flagcurveOnSurface: boolean, flagcurveParameterPoint: boolean, flagdimension: boolean, flagdynamicConstraint: boolean, flagedge: boolean, flageditPoint: boolean, flagemitter: boolean, flagfacet: boolean, flagfield: boolean, flagfluid: boolean, flagfollicle: boolean, flaghairSystem: boolean, flaghandle: boolean, flaghull: boolean, flagikEndEffector: boolean, flagikHandle: boolean, flagimagePlane: boolean, flagimplicitGeometry: boolean, flagisoparm: boolean, flagjoint: boolean, flagjointPivot: boolean, flaglattice: boolean, flaglatticePoint: boolean, flaglight: boolean, flaglocalRotationAxis: boolean, flaglocator: boolean, flaglocatorUV: boolean, flaglocatorXYZ: boolean, flagmeshUVShell: boolean, flagmotionTrailPoint: boolean, flagmotionTrailTangent: boolean, flagnCloth: boolean, flagnParticle: boolean, flagnParticleShape: boolean, flagnRigid: boolean, flagnonlinear: boolean, flagnurbsCurve: boolean, flagnurbsSurface: boolean, flagobjectComponent: boolean, flagorientationLocator: boolean, flagparticle: boolean, flagparticleShape: boolean, flagplane: boolean, flagpolymesh: boolean, flagpolymeshEdge: boolean, flagpolymeshFace: boolean, flagpolymeshFreeEdge: boolean, flagpolymeshUV: boolean, flagpolymeshVertex: boolean, flagpolymeshVtxFace: boolean, flagqueryByName: string, flagrigidBody: boolean, flagrigidConstraint: boolean, flagrotatePivot: boolean, flagscalePivot: boolean, flagsculpt: boolean, flagselectHandle: boolean, flagspring: boolean, flagspringComponent: boolean, flagstroke: boolean, flagsubdiv: boolean, flagsubdivMeshEdge: boolean, flagsubdivMeshFace: boolean, flagsubdivMeshPoint: boolean, flagsubdivMeshUV: boolean, flagsurfaceEdge: boolean, flagsurfaceFace: boolean, flagsurfaceKnot: boolean, flagsurfaceParameterPoint: boolean, flagsurfaceRange: boolean, flagsurfaceUV: boolean, flagtexture: boolean, flagvertex: boolean) -> boolean:
    """Synopsis:
---
---
 selectType([allComponents=boolean], [allObjects=boolean], [animBreakdown=boolean], [animCurve=boolean], [animInTangent=boolean], [animKeyframe=boolean], [animOutTangent=boolean], [byName=[string, boolean]], [camera=boolean], [cluster=boolean], [collisionModel=boolean], [controlVertex=boolean], [curve=boolean], [curveKnot=boolean], [curveOnSurface=boolean], [curveParameterPoint=boolean], [dimension=boolean], [dynamicConstraint=boolean], [edge=boolean], [editPoint=boolean], [emitter=boolean], [facet=boolean], [field=boolean], [fluid=boolean], [follicle=boolean], [hairSystem=boolean], [handle=boolean], [hull=boolean], [ikEndEffector=boolean], [ikHandle=boolean], [imagePlane=boolean], [implicitGeometry=boolean], [isoparm=boolean], [joint=boolean], [jointPivot=boolean], [lattice=boolean], [latticePoint=boolean], [light=boolean], [localRotationAxis=boolean], [locator=boolean], [locatorUV=boolean], [locatorXYZ=boolean], [meshUVShell=boolean], [motionTrailPoint=boolean], [motionTrailTangent=boolean], [nCloth=boolean], [nParticle=boolean], [nParticleShape=boolean], [nRigid=boolean], [nonlinear=boolean], [nurbsCurve=boolean], [nurbsSurface=boolean], [objectComponent=boolean], [orientationLocator=boolean], [particle=boolean], [particleShape=boolean], [plane=boolean], [polymesh=boolean], [polymeshEdge=boolean], [polymeshFace=boolean], [polymeshFreeEdge=boolean], [polymeshUV=boolean], [polymeshVertex=boolean], [polymeshVtxFace=boolean], [queryByName=string], [rigidBody=boolean], [rigidConstraint=boolean], [rotatePivot=boolean], [scalePivot=boolean], [sculpt=boolean], [selectHandle=boolean], [spring=boolean], [springComponent=boolean], [stroke=boolean], [subdiv=boolean], [subdivMeshEdge=boolean], [subdivMeshFace=boolean], [subdivMeshPoint=boolean], [subdivMeshUV=boolean], [surfaceEdge=boolean], [surfaceFace=boolean], [surfaceKnot=boolean], [surfaceParameterPoint=boolean], [surfaceRange=boolean], [surfaceUV=boolean], [texture=boolean], [vertex=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectType is undoable, queryable, and NOT editable.selectType
There are basically two different types of items that are selectable
when interactively selecting objects in the 3D views.  They are
classified as objects (entire objects) or components (parts of
objects).  The object and component command flags
control which class of objects are selectable.

It is possible to select components while in the object selection mode.
To set the components which are selectable in object
selection mode you must use the -ocm flag when specifying the component
flags.




Example:
---
import maya.cmds as cmds

cmds.selectType( allObjects=True )
cmds.selectType( q=True, cv=True )
cmds.selectType( allObjects=True, allComponents=False )

---
Return:
---


    boolean: if a query operation

Flags:
---


---
allComponents(alc): boolean
    properties: create, query
    Set all component selection masks on/off

---
allObjects(alo): boolean
    properties: create, query
    Set all object selection masks on/off

---
animBreakdown(abd): boolean
    properties: create, query
    Set animation breakdown selection mask on/off.

---
animCurve(ac): boolean
    properties: create, query
    Set animation curve selection mask on/off.

---
animInTangent(ait): boolean
    properties: create, query
    Set animation in-tangent selection mask on/off.

---
animKeyframe(ak): boolean
    properties: create, query
    Set animation keyframe selection mask on/off.

---
animOutTangent(aot): boolean
    properties: create, query
    Set animation out-tangent selection mask on/off.

---
byName(bn): [string, boolean]
    properties: create, multiuse
    Set the specified user-defined selection mask on/off. (object flag)

---
camera(ca): boolean
    properties: create, query
    Set camera selection mask on/off. (object flag)

---
cluster(cl): boolean
    properties: create, query
    Set cluster selection mask on/off. (object flag)

---
collisionModel(clm): boolean
    properties: create, query
    Set collision model selection mask on/off. (object flag)

---
controlVertex(cv): boolean
    properties: create, query
    Set control vertex selection mask on/off. (component flag)

---
curve(c): boolean
    properties: create, query
    Set curve selection mask on/off. (object flag)

---
curveKnot(ck): boolean
    properties: create, query
    Set curve knot selection mask on/off. (component flag)

---
curveOnSurface(cos): boolean
    properties: create, query
    Set curve-on-surface selection mask on/off. (object flag)

---
curveParameterPoint(cpp): boolean
    properties: create, query
    Set curve parameter point selection mask on/off. (component flag)

---
dimension(dim): boolean
    properties: create, query
    Set dimension shape selection mask on/off. (object flag)

---
dynamicConstraint(dc): boolean
    properties: create, query
    Set dynamicConstraint selection mask on/off. (object flag)

---
edge(eg): boolean
    properties: create, query
    Set mesh edge selection mask on/off. (component flag)

---
editPoint(ep): boolean
    properties: create, query
    Set edit-point selection mask on/off. (component flag)

---
emitter(em): boolean
    properties: create, query
    Set emitter selection mask on/off. (object flag)

---
facet(fc): boolean
    properties: create, query
    Set mesh face selection mask on/off. (component flag)

---
field(fi): boolean
    properties: create, query
    Set field selection mask on/off. (object flag)

---
fluid(fl): boolean
    properties: create, query
    Set fluid selection mask on/off. (object flag)

---
follicle(fo): boolean
    properties: create, query
    Set follicle selection mask on/off. (object flag)

---
hairSystem(hs): boolean
    properties: create, query
    Set hairSystem selection mask on/off. (object flag)

---
handle(ha): boolean
    properties: create, query
    Set object handle selection mask on/off. (object flag)

---
hull(hl): boolean
    properties: create, query
    Set hull selection mask on/off. (component flag)

---
ikEndEffector(iee): boolean
    properties: create, query
    Set ik end effector selection mask on/off. (object flag)

---
ikHandle(ikh): boolean
    properties: create, query
    Set ik handle selection mask on/off. (object flag)

---
imagePlane(ip): boolean
    properties: create, query
    Set image plane selection mask on/off. (component flag)

---
implicitGeometry(ig): boolean
    properties: create, query
    Set implicit geometry selection mask on/off. (object flag)

---
isoparm(iso): boolean
    properties: create, query
    Set surface iso-parm selection mask on/off. (component flag)

---
joint(j): boolean
    properties: create, query
    Set ik handle selection mask on/off. (object flag)

---
jointPivot(jp): boolean
    properties: create, query
    Set joint pivot selection mask on/off. (component flag)

---
lattice(la): boolean
    properties: create, query
    Set lattice selection mask on/off. (object flag)

---
latticePoint(lp): boolean
    properties: create, query
    Set lattice point selection mask on/off. (component flag)

---
light(lt): boolean
    properties: create, query
    Set light selection mask on/off. (object flag)

---
localRotationAxis(ra): boolean
    properties: create, query
    Set local rotation axis selection mask on/off. (component flag)

---
locator(lc): boolean
    properties: create, query
    Set locator (all types) selection mask on/off. (object flag)

---
locatorUV(luv): boolean
    properties: create, query
    Set uv locator selection mask on/off. (object flag)

---
locatorXYZ(xyz): boolean
    properties: create, query
    Set xyz locator selection mask on/off. (object flag)

---
meshUVShell(msh): boolean
    properties: create, query
    Set uv shell component mask on/off.

---
motionTrailPoint(mtp): boolean
    properties: create, query
    Set motion point selection mask on/off.

---
motionTrailTangent(mtt): boolean
    properties: create, query
    Set motion point tangent mask on/off.

---
nCloth(ncl): boolean
    properties: create, query
    Set nCloth selection mask on/off. (object flag)

---
nParticle(npr): boolean
    properties: create, query
    Set nParticle point selection mask on/off. (component flag)

---
nParticleShape(nps): boolean
    properties: create, query
    Set nParticle shape selection mask on/off. (object flag)

---
nRigid(nr): boolean
    properties: create, query
    Set nRigid selection mask on/off. (object flag)

---
nonlinear(nl): boolean
    properties: create, query
    Set nonlinear selection mask on/off. (object flag)

---
nurbsCurve(nc): boolean
    properties: create, query
    Set nurbs-curve selection mask on/off. (object flag)

---
nurbsSurface(ns): boolean
    properties: create, query
    Set nurbs-surface selection mask on/off. (object flag)

---
objectComponent(ocm): boolean
    properties: create, query
    Component flags apply to object mode.

---
orientationLocator(ol): boolean
    properties: create, query
    Set orientation locator selection mask on/off. (object flag)

---
particle(pr): boolean
    properties: create, query
    Set particle point selection mask on/off. (component flag)

---
particleShape(ps): boolean
    properties: create, query
    Set particle shape selection mask on/off. (object flag)

---
plane(pl): boolean
    properties: create, query
    Set sketch plane selection mask on/off. (object flag)

---
polymesh(p): boolean
    properties: create, query
    Set poly-mesh selection mask on/off. (object flag)

---
polymeshEdge(pe): boolean
    properties: create, query
    Set poly-mesh edge selection mask on/off. (component flag)

---
polymeshFace(pf): boolean
    properties: create, query
    Set poly-mesh face selection mask on/off. (component flag)

---
polymeshFreeEdge(pfe): boolean
    properties: create, query
    Set poly-mesh free-edge selection mask on/off. (component flag)

---
polymeshUV(puv): boolean
    properties: create, query
    Set poly-mesh UV point selection mask on/off. (component flag)

---
polymeshVertex(pv): boolean
    properties: create, query
    Set poly-mesh vertex selection mask on/off. (component flag)

---
polymeshVtxFace(pvf): boolean
    properties: create, query
    Set poly-mesh vertexFace selection mask on/off. (component flag)

---
queryByName(qbn): string
    properties: query
    Query the specified user-defined selection mask. (object flag)
      In query mode, this flag needs a value.

---
rigidBody(rb): boolean
    properties: create, query
    Set rigid body selection mask on/off. (object flag)

---
rigidConstraint(rc): boolean
    properties: create, query
    Set rigid constraint selection mask on/off. (object flag)

---
rotatePivot(rp): boolean
    properties: create, query
    Set rotate pivot selection mask on/off. (component flag)

---
scalePivot(sp): boolean
    properties: create, query
    Set scale pivot selection mask on/off. (component flag)

---
sculpt(sc): boolean
    properties: create, query
    Set sculpt selection mask on/off. (object flag)

---
selectHandle(sh): boolean
    properties: create, query
    Set select handle selection mask on/off. (component flag)

---
spring(spr): boolean
    properties: create, query
    Set spring shape selection mask on/off. (object flag)

---
springComponent(spc): boolean
    properties: create, query
    Set individual spring selection mask on/off. (component flag)

---
stroke(str): boolean
    properties: create, query
    Set the Paint Effects stroke selection mask on/off. (object flag)

---
subdiv(sd): boolean
    properties: create, query
    Set subdivision surfaces selection mask on/off. (object flag)

---
subdivMeshEdge(sme): boolean
    properties: create, query
    Set subdivision surfaces mesh edge selection mask on/off. (component flag)

---
subdivMeshFace(smf): boolean
    properties: create, query
    Set subdivision surfaces mesh face selection mask on/off. (component flag)

---
subdivMeshPoint(smp): boolean
    properties: create, query
    Set subdivision surfaces mesh point selection mask on/off. (component flag)

---
subdivMeshUV(smu): boolean
    properties: create, query
    Set subdivision surfaces mesh UV map selection mask on/off. (component flag)

---
surfaceEdge(se): boolean
    properties: create, query
    Set surface edge selection mask on/off. (component flag)

---
surfaceFace(sf): boolean
    properties: create, query
    Set surface face selection mask on/off. (component flag)

---
surfaceKnot(sk): boolean
    properties: create, query
    Set surface knot selection mask on/off. (component flag)

---
surfaceParameterPoint(spp): boolean
    properties: create, query
    Set surface parameter point selection mask on/off. (component flag)

---
surfaceRange(sr): boolean
    properties: create, query
    Set surface range selection mask on/off. (component flag)

---
surfaceUV(suv): boolean
    properties: create, query
    Set surface uv selection mask on/off. (component flag)

---
texture(tx): boolean
    properties: create, query
    Set texture selection mask on/off. (object flag)

---
vertex(v): boolean
    properties: create, query
    Set mesh vertex selection mask on/off. (component flag)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectType.html 
    """


def selectionConnection(flagactiveCacheList: boolean, flagactiveCharacterList: boolean, flagactiveList: boolean, flagaddScript: script, flagaddTo: string, flagcharacterList: boolean, flagclear: boolean, flagconnectionList: boolean, flagdefineTemplate: string, flagdeselect: name, flageditor: string, flagexists: boolean, flagfilter: string, flagfindObject: name, flagg: boolean, flaghighlightList: boolean, flagidentify: boolean, flagkeyframeList: boolean, flaglock: boolean, flagmodelList: boolean, flagobject: name, flagparent: string, flagremove: string, flagremoveScript: script, flagselect: name, flagsetList: boolean, flagswitch: boolean, flaguseTemplate: string, flagworldList: boolean) -> string:
    """Synopsis:
---
---
 selectionConnection(
string
    , [activeCacheList=boolean], [activeCharacterList=boolean], [activeList=boolean], [addScript=script], [addTo=string], [characterList=boolean], [clear=boolean], [connectionList=boolean], [defineTemplate=string], [deselect=name], [editor=string], [exists=boolean], [filter=string], [findObject=name], [g=boolean], [highlightList=boolean], [identify=boolean], [keyframeList=boolean], [lock=boolean], [modelList=boolean], [object=name], [parent=string], [remove=string], [removeScript=script], [select=name], [setList=boolean], [switch=boolean], [useTemplate=string], [worldList=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

selectionConnection is undoable, queryable, and editable.
Selection connections are UI objects which contain a list of model
objects. Selection connections are useful for specifying which objects
are to be displayed within a particular editor. Editor's have three
plug sockets where a selection connection may be attached.
They are:


mainListConnection
an input socket which contains a list of objects
that are to be displayed within the editor

selectionConnection
an output socket which contains a list of objects
that are selected within the editor

highlightConnection
an input socket which contains
a list of objects that are to be highlighted
within the editor


There are several different types of selection connections that may be
created. They include:


activeList
a selection connection which contains a list
of everything in the model which is active (which includes
geometry objects and keys)

modelList
a selection connection which contains a list
of all the geometry (i.e. excluding keys) objects that are currently
active

keyframeList
a selection connection which contains a list
of all the keys that are currently active

worldList
a selection connection which contains a list
of all the objects in the world

objectList
a selection connection which contains one
model object (which may be a set)

listList
a selection connection which contains a list
of selection connections

editorList
a selection connection which contains a list
of objects that are attached to the mainListConnection
of the specified editor

setList
a selection connection which contains a list
of all the sets in the world

characterList
a selection connection which contains a list
of all the characters in the world

highlightList
a selection connection which contains a list
of objects to be highlighted in some fashion


Below is an example selectionConnection network between two
editors. Editor 1 is setup to display objects on the activeList.
Editor 2 is setup to display objects which are selected within Editor
1, and objects that are selected in Editor 2 are highlighted within
Editor 1:


-- Editor 1--       -- Editor 2--
inputList-->| main |      |  |->| main |      |
|      | sele |--|  |      | sele |--|
|->| high |      |     | high |      |  |
|   -------------       -------------   |
|------------- fromEditor2 -------------|


The following commands will establish this network:


selectionConnection -activeList inputList;
selectionConnection fromEditor1;
selectionConnection fromEditor2;
editor -edit -mainListConnection inputList Editor1;
editor -edit -selectionConnection fromEditor1 Editor1;
editor -edit -mainListConnection fromEditor1 Editor2;
editor -edit -selectionConnection fromEditor2 Editor2;
editor -edit -highlightConnection fromEditor2 Editor1;


Note: to delete a selection connection use the deleteUI command
Note: commands which expect objects may be given a selection connection
instead, and the command will operate upon the objects wrapped by the
selection connection
Note: the graph editor and the dope sheet are the only editors which can use the
editor connection to the highlightConnection of another editor
WARNING: some flag combinations may not behave as you expect.  The command
is really intended for internal use for managing the outliner used by
the various editors.




Example:
---
import maya.cmds as cmds

   Example 1.
---

   Create a window with two Outliner editors and a
   selection connection network.  Editor 1 will display the
   current scene's active list.  Editor 2 will display the items
   selected in Editor 1.
---

window = cmds.window('window', wh=(400, 300))
cmds.paneLayout( configuration='vertical2' )
editor1 = cmds.outlinerEditor()
editor2 = cmds.outlinerEditor()

   Create the selection connection network.
---

inputList = cmds.selectionConnection( activeList=True )
fromEditor1 = cmds.selectionConnection()
fromEditor2 = cmds.selectionConnection()
cmds.editor( editor1, edit=True, mainListConnection=inputList )
cmds.editor( editor1, edit=True, selectionConnection=fromEditor1 )
cmds.editor( editor2, edit=True, mainListConnection=fromEditor1 )
cmds.editor( editor2, edit=True, selectionConnection=fromEditor2 )

cmds.showWindow( window )

   Create some objects and select them.
---

cmds.sphere()
cmds.cone()
cmds.cylinder()
cmds.select( all=True )

Now as you select objects on the left side, they will be
displayed on the right side.  You can also add a callback
script to do further processing on the list when objects
are added. (Use -removeScript for when objects are removed.)

def addScriptCallback( array ):
    print "Contents of callback array: %s\n" % array

cmds.selectionConnection( fromEditor1, e=True, addScript=addScriptCallback )


   Example 2.
---

   Create a selection connection for a paritcular object.  Delete
   the selection connection and the object.
---

cmds.sphere( name='sphere' )

   Create a selection connection to wrap the sphere.
---

cmds.selectionConnection( 'holder', object='sphere' )

   Select the sphere using the selection connection.
---

cmds.select( 'holder' )

   Delete the members (sphere) of the selection connection
---

cmds.delete( 'holder' )

   Delete the selection connection (does not delete the members of
   the selection connection.
---

cmds.deleteUI( 'holder' )

---
Return:
---


    string: Value of the queried flag

Flags:
---


---
activeCacheList(atc): boolean
    properties: create
    Specifies that this connection should reflect the cache that objects
on the active list belong to.

---
activeCharacterList(acl): boolean
    properties: create
    Specifies that this connection should reflect the characters that objects
on the active list belong to.

---
activeList(act): boolean
    properties: create
    Specifies that this connection should reflect the active
list (geometry objects and keys).

---
addScript(addScript): script
    properties: create, query, edit
    Specify a script to be called when something is added to the
selection.

---
addTo(add): string
    properties: create, edit
    The name of a selection connection that should be added to this
list of connections.

---
characterList(cl): boolean
    properties: create
    Specifies that this connection should reflect all the characters in
the world.

---
clear(clr): boolean
    properties: create, edit
    Remove everything from the selection connection.

---
connectionList(lst): boolean
    properties: create, query
    Specifies that this connection should contain a list of selection
connections.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deselect(d): name
    properties: create, edit
    Remove something from the selection.

---
editor(ed): string
    properties: create, query, edit
    Specifies that this connection should reflect the -mainListConnection
of the specified editor.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
filter(f): string
    properties: create, query, edit
    Optionally specifies an itemFilter for this connection.
An empty string ("") clears the current filter.
If a filter is specified, all the information going into
the selectionConnection must first pass through the filter
before being accepted.

NOTE: filters can only be attached to regular selectionConnections.
They cannot be attached to any connection created using
the -act, -mdl, -key, -wl, -sl, -cl, -lst, -obj, or -ren flags.
We strongly recommend that you do not attach filters to a
selectionConnection --- it is better to attach your filter
to the editor that is using the selectionConnection instead.

---
findObject(fo): name
    properties: query
    Find a selection connection in this list that wraps the specified
object.

---
g(g): boolean
    properties: create, query, edit
    A global selection connection cannot be deleted by any script
commands.

---
highlightList(hl): boolean
    properties: create
    Specifies that this connection is being used as a highlight list.

---
identify(id): boolean
    properties: query
    Find out what type of selection connection this is.  May be:
activeList | modelList | keyframeList | worldList | objectList
listList | editorList | connection | unknown

---
keyframeList(key): boolean
    properties: create
    Specifies that this connection should reflect the animation
portion of the active list.

---
lock(lck): boolean
    properties: create, query, edit
    For activeList connections, locking the connection means that
it will not listen to activeList changes.

---
modelList(mdl): boolean
    properties: create
    Specifies that this connection should reflect the modeling
(i.e. excluding keys) portion of the active list.

---
object(obj): name
    properties: create, query, edit
    Specifies that this connection should wrap around the specified
object (which may be a set).  Query will return all the members of the
selection connection (if the connection wraps a set, the set members will
be returned)

---
parent(p): string
    properties: create, query, edit
    The name of a UI object this should be attached to.  When the
parent is destroyed, the selectionConnection will auto-delete.
If no parent is specified, the connection is created in the
current controlLayout.

---
remove(rm): string
    properties: create, edit
    The name of a selection connection that should be removed from
this list of connections.

---
removeScript(rs): script
    properties: create, query, edit
    Specify a script to be called when something is removed from
the selection.

---
select(s): name
    properties: create, edit
    Add something to the selection. This does not replace the
existing selection.

---
setList(sl): boolean
    properties: create
    Specifies that this connection should reflect all the sets in
the world.

---
switch(sw): boolean
    properties: create, query
    Acts as a modifier to -connectionList which sets the list of objects
to be the first non-empty selection connection.  selection connections
are tested in the order in which they are added.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
worldList(wl): boolean
    properties: create
    Specifies that this connection should reflect all objects
in the world.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/selectionConnection.html 
    """


def separator(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontal: boolean, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flagstyle: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 separator(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [style=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

separator is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.window()
cmds.rowColumnLayout( numberOfColumns=2, columnAlign=(1, 'right'), columnAttach=(2, 'both', 0), columnWidth=(2, 150) )

cmds.text( label='Default' )
cmds.separator()
cmds.text( label='None' )
cmds.separator( style='none' )
cmds.text( label='Single' )
cmds.separator( style='single' )
cmds.text( label='Etched In' )
cmds.separator( height=40, style='in' )
cmds.text( label='Etched Out' )
cmds.separator( height=40, style='out' )
cmds.setParent( '..' )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
horizontal(hr): boolean
    properties: create, query, edit
    Specify the orientation of the separator.  True for
horizontal and false for vertical.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
style(st): string
    properties: create, query, edit
    Specify the style of the separator.  Valid values are
"none", "single", "in", "out" and "shelf".  Note: the values
"double", "singleDash" and "doubleDash" and no longer
supported.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/separator.html 
    """


def sequenceManager(flagaddSequencerAudio: string, flagattachSequencerAudio: string, flagcurrentShot: string, flagcurrentTime: time, flaglistSequencerAudio: string, flaglistShots: boolean, flagmodelPanel: string, flagnode: string, flagwritableSequencer: string) -> None:
    """Synopsis:
---
---
 sequenceManager([addSequencerAudio=string], [attachSequencerAudio=string], [currentShot=string], [currentTime=time], [listSequencerAudio=string], [listShots=boolean], [modelPanel=string], [node=string], [writableSequencer=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sequenceManager is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

// Get the current Maya time, based on the Sequence time
cmds.sequenceManager(q=True, currentTime=True);

---


Flags:
---


---
addSequencerAudio(asa): string
    properties: create
    Add an audio clip to the sequencer by specifying a filename

---
attachSequencerAudio(ata): string
    properties: create
    Add an audio clip to the sequencer by specifying an audio node

---
currentShot(cs): string
    properties: query
    Returns the shot that is being used at the current sequence time.

---
currentTime(ct): time
    properties: create, query
    Set the current sequence time

---
listSequencerAudio(lsa): string
    properties: create
    List the audio clips added to the sequencer

---
listShots(lsh): boolean
    properties: create
    List all the currently defined shots across all scene segments

---
modelPanel(mp): string
    properties: create, query
    Sets a dedicated modelPanel to be used as the panel that the sequencer will control.

---
node(nd): string
    properties: query
    Returns the SequenceManager node, of which there is only ever one.

---
writableSequencer(ws): string
    properties: query
    Get the writable sequencer node.  Create it if it doesn't exist.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sequenceManager.html 
    """


def setAttr(flagalteredValue: boolean, flagcaching: boolean, flagcapacityHint: uint, flagchannelBox: boolean, flagclamp: boolean, flagkeyable: boolean, flaglock: boolean, flagsize: uint, flagtype: string) -> None:
    """Synopsis:
---
---
 setAttr(
attribute Any [Any...]
    , [alteredValue=boolean], [caching=boolean], [capacityHint=uint], [channelBox=boolean], [clamp=boolean], [keyable=boolean], [lock=boolean], [size=uint], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setAttr is undoable, queryable, and editable.-l/-k/-s-type
For Ufe attributes, the input attribute string should be
"<ufe_path_string>.<ufe_attribute_name>".

The following chart outlines the syntax of setAttr for non-numeric
data types:

{TYPE} below means any number of values of type TYPE,
separated by a space
[TYPE] means that the value of type TYPE is optional
A|B means that either of A or B may appear


In order to run its examples, first execute these commands to
create the sample attribute types:

sphere -n node;
addAttr -ln short2Attr -at short2;
addAttr -ln short2a -p short2Attr -at short;
addAttr -ln short2b -p short2Attr -at short;
addAttr -ln short3Attr -at short3;
addAttr -ln short3a -p short3Attr -at short;
addAttr -ln short3b -p short3Attr -at short;
addAttr -ln short3c -p short3Attr -at short;
addAttr -ln long2Attr -at long2;
addAttr -ln long2a -p long2Attr -at long;
addAttr -ln long2b -p long2Attr -at long;
addAttr -ln long3Attr -at long3;
addAttr -ln long3a -p long3Attr -at long;
addAttr -ln long3b -p long3Attr -at long;
addAttr -ln long3c -p long3Attr -at long;
addAttr -ln float2Attr -at float2;
addAttr -ln float2a -p float2Attr -at "float";
addAttr -ln float2b -p float2Attr -at "float";
addAttr -ln float3Attr -at float3;
addAttr -ln float3a -p float3Attr -at "float";
addAttr -ln float3b -p float3Attr -at "float";
addAttr -ln float3c -p float3Attr -at "float";
addAttr -ln double2Attr -at double2;
addAttr -ln double2a -p double2Attr -at double;
addAttr -ln double2b -p double2Attr -at double;
addAttr -ln double3Attr -at double3;
addAttr -ln double3a -p double3Attr -at double;
addAttr -ln double3b -p double3Attr -at double;
addAttr -ln double3c -p double3Attr -at double;
addAttr -ln int32ArrayAttr -dt Int32Array;
addAttr -ln doubleArrayAttr -dt doubleArray;
addAttr -ln pointArrayAttr -dt pointArray;
addAttr -ln vectorArrayAttr -dt vectorArray;
addAttr -ln stringArrayAttr -dt stringArray;
addAttr -ln stringAttr -dt "string";
addAttr -ln matrixAttr -dt "matrix";
addAttr -ln sphereAttr -dt sphere;
addAttr -ln coneAttr -dt cone;
addAttr -ln meshAttr -dt mesh;
addAttr -ln latticeAttr -dt lattice;
addAttr -ln spectrumRGBAttr -dt spectrumRGB;
addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
addAttr -ln componentListAttr -dt componentList;
addAttr -ln attrAliasAttr -dt attributeAlias;
addAttr -ln curveAttr -dt nurbsCurve;
addAttr -ln surfaceAttr -dt nurbsSurface;
addAttr -ln trimFaceAttr -dt nurbsTrimface;
addAttr -ln polyFaceAttr -dt polyFaces;





-type short2


Array of two short integers


Value Syntax
short short


Value Meaning
value1 value2


Mel Example
setAttr node.short2Attr -type short2 1 2;


Python Example
cmds.setAttr('node.short2Attr',1,2,type='short2')





-type short3


Array of three short integers


Value Syntax
short short short


Value Meaning
value1 value2 value3


Mel Example
setAttr node.short3Attr -type short3 1 2 3;


Python Example
cmds.setAttr('node.short3Attr',1,2,3,type='short3')





-type long2


Array of two long integers


Value Syntax
long long


Value Meaning
value1 value2


Mel Example
setAttr node.long2Attr -type long2 1000000 2000000;


Python Example
cmds.setAttr('node.long2Attr',1000000,2000000,type='long2')





-type long3


Array of three long integers


Value Syntax
long long long


Value Meaning
value1 value2 value3


Mel Example
setAttr node.long3Attr -type long3 1000000 2000000 3000000;


Python Example
cmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')





-type Int32Array


Variable length array of long integers


Value Syntax
int {int}


Value Meaning
numberOfArrayValues {arrayValue}


Mel Example
setAttr node.int32ArrayAttr -type Int32Array 2 12 75;


Python Example
cmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')





-type float2


Array of two floats


Value Syntax
float float


Value Meaning
value1 value2


Mel Example
setAttr node.float2Attr -type float2 1.1 2.2;


Python Example
cmds.setAttr('node.float2Attr',1.1,2.2,type='float2')





-type float3


Array of three floats


Value Syntax
float float float


Value Meaning
value1 value2 value3


Mel Example
setAttr node.float3Attr -type float3 1.1 2.2 3.3;


Python Example
cmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')





-type double2


Array of two doubles


Value Syntax
double double


Value Meaning
value1 value2


Mel Example
setAttr node.double2Attr -type double2 1.1 2.2;


Python Example
cmds.setAttr('node.double2Attr',1.1,2.2,type='double2')





-type double3


Array of three doubles


Value Syntax
double double double


Value Meaning
value1 value2 value3


Mel Example
setAttr node.double3Attr -type double3 1.1 2.2 3.3;


Python Example
cmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')





-type doubleArray


Variable length array of doubles


Value Syntax
int {double}


Value Meaning
numberOfArrayValues {arrayValue}


Mel Example
setAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;


Python Example
cmds.setAttr( "node.doubleArrayAttr", (2, 3.14159, 2.782,), type="doubleArray")





-type matrix


4x4 matrix of doubles


Value Syntax
double double double double
double double double double
double double double double
double double double double


Value Meaning
row1col1 row1col2 row1col3 row1col4
row2col1 row2col2 row2col3 row2col4
row3col1 row3col2 row3col3 row3col4
row4col1 row4col2 row4col3 row4col4


Alternate Syntax
string double double double
double double double
integer
double double double
double double double
double double double
double double double
double double double
double double double
double double double double
double double double double
double double double
boolean


Alternate Meaning
"xform" scaleX scaleY scaleZ
rotateX rotateY rotateZ
rotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)
translateX translateY translateZ
shearXY shearXZ shearYZ
scalePivotX scalePivotY scalePivotZ
scaleTranslationX scaleTranslationY scaleTranslationZ
rotatePivotX rotatePivotY rotatePivotZ
rotateTranslationX rotateTranslationY rotateTranslationZ
rotateOrientW rotateOrientX rotateOrientY rotateOrientZ
jointOrientW jointOrientX jointOrientY jointOrientZ
inverseParentScaleX inverseParentScaleY inverseParentScaleZ
compensateForParentScale



Mel Example
setAttr node.matrixAttr -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;
setAttr node.matrixAttr -type "matrix" "xform" 1 1 1 0 0 0 0 2 3 4 0 0 00 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 false;


Python Example
cmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')
cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,type="matrix")





-type pointArray


Variable length array of points


Value Syntax
int {double double double double}


Value Meaning
numberOfArrayValues {xValue yValue zValue wValue}


Mel Example
setAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2 1;


Python Example
cmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')





-type vectorArray


Variable length array of vectors


Value Syntax
int {double double double}


Value Meaning
numberOfArrayValues {xValue yValue zValue}


Mel Example
setAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;


Python Example
cmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')





-type "string"


Character string


Value Syntax
string


Value Meaning
characterStringValue


Mel Example
setAttr node.stringAttr -type "string" "blarg";


Python Example
cmds.setAttr('node.stringAttr',"blarg",type="string")





-type stringArray


Variable length array of strings


Value Syntax
int {string}


Value Meaning
numberOfArrayValues {arrayValue}


Mel Example
setAttr node.stringArrayAttr -type stringArray 3 "a" "b" "c";


Python Example
cmds.setAttr('node.stringArrayAttr',3,"a","b","c",type='stringArray')





-type sphere


Sphere data


Value Syntax
double


Value Meaning
sphereRadius


Example
setAttr node.sphereAttr -type sphere 5.0;





-type cone


Cone data


Value Syntax
double double


Value Meaning
coneAngle coneCap


Mel Example
setAttr node.coneAttr -type cone 45.0 5.0;


Python Example
cmds.setAttr('node.coneAttr',45.0,5.0,type='cone')





-type reflectanceRGB


Reflectance data


Value Syntax
double double double


Value Meaning
redReflect greenReflect blueReflect


Mel Example
setAttr node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;


Python Example
cmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')





-type spectrumRGB


Spectrum data


Value Syntax
double double double


Value Meaning
redSpectrum greenSpectrum blueSpectrum


Mel Example
setAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;


Python Example
cmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')





-type componentList


Variable length array of components


Value Syntax
int {string}


Value Meaning
numberOfComponents {componentName}


Mel Example
setAttr node.componentListAttr -type componentList 3 cv[1] cv[12] cv[3];


Python Example
cmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')





-type attributeAlias


String alias data


Value Syntax
string string


Value Meaning
newAlias currentName


Mel Example
setAttr node.attrAliasAttr -type attributeAlias
{"GoUp", "translateY", "GoLeft", "translateX"};


Python Example
cmds.setAttr('node.attrAliasAttr',("GoUp", "translateY","GoLeft", "translateX"),type='attributeAlias')





-type nurbsCurve


NURBS curve data


Value Syntax
int int int bool int int {double}
int {double double double}


Value Meaning
degree spans form isRational dimension knotCount {knotValue}
cvCount {xCVValue yCVValue [zCVValue] [wCVValue]}


Mel Example
// degree is the degree of the curve(range 1-7)
// spans is the number of spans 
// form is open (0), closed (1), periodic (2)
// isRational is true if the curve CVs contain a rational component 
// dimension is 2 or 3, depending on the dimension of the curve
// knotCount is the size of the knot list
//  knotValue is a single entry in the knot list
// cvCount is the number of CVs in the curve
//  xCVValue,yCVValue,[zCVValue] [wCVValue] is a single CV.
//  zCVValue is only present when dimension is 3.
//  wCVValue is only present when isRational is true.
//
$curve = `createNode nurbsCurve`;
setAttr ($curve+".cc") -type nurbsCurve 3 1 0 no 3
6 0 0 0 1 1 1
4 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;


Python Example
# degree is the degree of the curve(range 1-7)
# spans is the number of spans 
# form is open (0), closed (1), periodic (2)
# isRational is true if the curve CVs contain a rational component
# dimension is 2 or 3, depending on the dimension of the curve
# knotList is the list of knots
# next argument is unused and can be set to 0
# cvCount is the number of CVs in the curve
#  (xCVValue,yCVValue,[zCVValue] [wCVValue]) is a single CV.
#  zCVValue is only present when dimension is 3.
#  wCVValue is only present when isRational is true.
#
curve = maya.cmds.createNode("nurbsCurve")
maya.cmds.setAttr(curve+".cc",
3, 1, 0, False, 3,
(0, 0, 0, 1, 1, 1), 0,
4,
(-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
type="nurbsCurve")





-type nurbsSurface


NURBS surface data


Value Syntax
int int int int bool 
int {double} 
int {double} 
[string] int {double double double}


Value Meaning
uDegree vDegree uForm vForm isRational
uKnotCount {uKnotValue}
vKnotCount {vKnotValue} ["TRIM"|"NOTRIM"] cvCount {xCVValue yCVValue
zCVValue [wCVValue]}


Mel Example
// uDegree is degree of the surface in U direction (range 1-7)
// vDegree is degree of the surface in V direction (range 1-7)
// uForm is open (0), closed (1), periodic (2) in U direction
// vForm is open (0), closed (1), periodic (2) in V direction
// isRational is true if the surface CVs contain a rational component
// uKnotCount is the size of the U knot list
//  uKnotValue is a single entry in the U knot list
// vKnotCount is the size of the V knot list
//  vKnotValue is a single entry in the V knot list
// If "TRIM" is specified then additional trim information is expected
// If "NOTRIM" is specified then the surface is not trimmed
// cvCount is the number of CVs in the surface
//  xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.
//  zCVValue is only present when dimension is 3.
//  wCVValue is only present when isRational is true
//
$surface = `createNode nurbsSurface`;
setAttr ($surface+".cc") -type nurbsSurface 3 3 0 0 no
6 0 0 0 1 1 1
6 0 0 0 1 1 1
16 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0
-1 3 0 -1 1 0 -1 -1 0 -1 -3 0
1 3 0 1 1 0 1 -1 0 1 -3 0
3 3 0 3 1 0 3 -1 0 3 -3 0;


Python Example
# uDegree is degree of the surface in U direction (range 1-7)
# vDegree is degree of the surface in V direction (range 1-7)
# uForm is open (0), closed (1), periodic (2) in U direction
# vForm is open (0), closed (1), periodic (2) in V direction
# isRational is true if the surface CVs contain a rational component
# uKnotList is the list of knots in U
# next argument is unused and can be set to 0
# vKnotList is the list of knots in V
# next argument is unused and can be set to 0
# If "TRIM" is specified then additional trim information is expected
# If "NOTRIM" is specified then the surface is not trimmed
# cvCount is the number of CVs in the surface
#  (xCVValue,yCVValue,zCVValue [wCVValue])is a single CV.
#  zCVValue is only present when dimension is 3.
#  wCVValue is only present when isRational is true
#
surface = maya.cmds.createNode("nurbsSurface")
maya.cmds.setAttr(surface+".cc",
3, 3, 0, 0, False,
(0, 0, 0, 1, 1, 1), 0,
(0, 0, 0, 1, 1, 1), 0,
16,
(-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
(-1, 3, 0), (-1, 1, 0), (-1, -1, 0), (-1, -3, 0),
(1, 3, 0), (1, 1, 0), (1, -1, 0), (1, -3, 0),
(3, 3, 0), (3, 1, 0), (3, -1, 0), (3, -3, 0),
type="nurbsSurface")





-type nurbsTrimface


NURBS trim face data


Value Syntax
bool int {int {int {double bool bool} int {bool double}}}


Value Meaning
flipNormal boundaryCount {boundaryType tedgeCountOnBoundary
{splineCountOnEdge {edgeTolerance isEdgeReversed geometricContinuity}
{splineCountOnPedge {isMonotone pedgeTolerance}}}



Example
// flipNormal if true turns the surface inside out
// boundaryCount: number of boundaries
// boundaryType: 
// tedgeCountOnBoundary    : number of edges in a boundary
// splineCountOnEdge    : number of splines in an edge in
// edgeTolerance        : tolerance used to build the 3d edge
// isEdgeReversed        : if true, the edge is backwards
// geometricContinuity    : if true, the edge is tangent continuous
// splineCountOnPedge    : number of splines in a 2d edge
// isMonotone            : if true, curvature is monotone
// pedgeTolerance        : tolerance for the 2d edge
//






-type polyFaces


Polygon face data


Value Syntax
{"f" int {int}}
{"h" int {int}}
{"mf" int {int}}
{"mh" int {int}}
{"mu" int int {int}}
{"mc" int int {int}}


Value Meaning
{"f" faceEdgeCount {edgeIdValue}}
{"h" holeEdgeCount {edgeIdValue}}
{"mf" faceUVCount {uvIdValue}}
{"mh" holeUVCount {uvIdValue}}
{"mu" uvSet faceUVCount {uvIdValue}}
{"mc" colorIndex multiColorCount {colorIdValue}}



Example
// This data type (polyFace) is meant to be used in file I/O
// after setAttrs have been written out for vertex position
// arrays, edge connectivity arrays (with corresponding start
// and end vertex descriptions), texture coordinate arrays and
// color arrays.  The reason is that this data type references
// all of its data through ids created by the former types.
//
// "f" specifies the ids of the edges making up a face -
//     negative value if the edge is reversed in the face
// "h" specifies the ids of the edges making up a hole -
//     negative value if the edge is reversed in the face
// "mf" specifies the ids of texture coordinates (uvs) for a face.
//     This data type is obsolete as of version 3.0. It is replaced by "mu".
// "mh" specifies the ids of texture coordinates (uvs) for a hole
//     This data type is obsolete as of version 3.0. It is replaced by "mu".
// "mu" The  first argument refers to the uv set. This is a zero-based
//     integer number. The second argument refers to the number of vertices (n)
//     on the face which have valid uv values. The last n values are the uv
//     ids of the texture coordinates (uvs) for the face. These indices
//     are what used to be represented by the "mf" and "mh" specification.
//     There may be more than one "mu" specification, one for each unique uv set.
// "mc" specifies the color index values for a face. The first argument
//     is color index. The second argument is the number of color ids to follow.
//     Rest of the arguments are color ids for the face.
//
setAttr node.polyFaceAttr -type polyFaces "f" 3 1 2 3 "mc" 0 4 0 1 2 3;





-type mesh


Polygonal mesh


Value Syntax
{string [int {double double double}]}
{string [int {double double double}]}
[{string [int {double double}]}]
{string [int {double double string}]}



Value Meaning
"v" [vertexCount {vertexX vertexY vertexZ}]
"vn" 0
["vt" [uvCount {uValue vValue}]]
"e" [edgeCount {startVertex endVertex "smooth"|"hard"}]
"face" ["l" edgeLoopCount edgeIndex1...] ]"lt" uvCount uvIndex1...]"
"face"...



Mel Example
// "v" specifies the vertices of the polygonal mesh
// "vn"must be set to 0
// "vt" is optional and specifies a U,V texture coordinate for
each vertex
// "e" specifies the edge connectivity information between
vertices
// "face" specifies face connectivity (edges/UVs) for a single face
//
$mesh = `createNode mesh`;
setAttr ($mesh+".o")
-type mesh "v" 3 0 0 0 0 1 0 0 0 1
"vn" 3 1 0 0 1 0 0 1 0 0
"vt" 3 0 0 0 1 1 0
"e" 3 0 1 "hard" 1 2 "hard" 2 0 "hard"
"face" "l" 3 0 1 2 "lt" 3 0 1 2;


Python Example
# "v" specifies the vertices of the polygonal mesh
# "vn"must be set to 0
# "vt" is optional and specifies a U,V texture coordinate for
each vertex
# "e" specifies the edge connectivity information between
vertices
# "face" specifies face connectivity (edges/UVs) for a single face
#
mesh = maya.cmds.createNode("mesh")
maya.cmds.setAttr(mesh+".o",
"v", 3, (0, 0, 0), (0, 1, 0), (0, 0, 1),
"vn", 0,
"vt", 3, (0, 0), (0, 1), (1, 0),
"e", 3, 0, 1, "hard", 1, 2, "hard", 2, 0, "hard",
"face", "l", 3, 0, 1, 2, "lt", 3, 0, 1, 2,
type="mesh")





-type lattice


Lattice data


Value Syntax
int int int int {double double double}


Value Meaning
sDivisionCount tDivisionCount uDivisionCount
pointCount {pointX pointY pointZ}


Mel Example
// sDivisionCount is the horizontal lattice division count
// tDivisionCount is the vertical lattice division count
// uDivisionCount is the depth lattice division count
// pointCount is the total number of lattice points
// pointX,pointY,pointZ is one lattice point.  The list is
//   specified varying first in S, then in T, last in U so the
//   first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
//
$lattice = `createNode lattice`;
setAttr ($lattice+".cc") -type lattice 2 5 2 20
-2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -2
2 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2
-2 -2 2 2 -2 2 -2 -1 2 2 -1 2 -2 0 2
2 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;


Python Example
# sDivisionCount is the horizontal lattice division count
# tDivisionCount is the vertical lattice division count
# uDivisionCount is the depth lattice division count
# pointCount is the total number of lattice points
# (pointX,pointY,pointZ) is one lattice point.  The list is
#   specified varying first in S, then in T, last in U so the
#   first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
#
lattice = maya.cmds.createNode("lattice")
maya.cmds.setAttr(lattice+".cc",
2, 5, 2, 20,
(-2, -2, -2), (2, -2, -2), (-2, -1, -2), (2, -1, -2), (-2, 0, -2),
(2, 0, -2), (-2, 1, -2), (2, 1, -2), (-2, 2, -2), (2, 2, -2),
(-2, -2, 2), (2, -2, 2), (-2, -1, 2), (2, -1, 2), (-2, 0, 2),
(2, 0, 2), (-2, 1, 2), (2, 1, 2), (-2, 2, 2), (2, 2, 2),
type="lattice")










Example:
---
import maya.cmds as cmds

cmds.sphere( n="sphere" )

Set a simple numeric value
cmds.setAttr( 'sphere.translateX', 5 )

Lock an attribute to prevent further modification
cmds.setAttr( 'sphere.translateX', lock=True )

Make an attribute unkeyable
cmds.setAttr( 'sphere.translateZ', keyable=False )

Set an entire list of multi-attribute values in one command
cmds.setAttr( 'sphereShape.weights[0:6]',1, 1, 2, 1, 1, 1, 2,size=7)
Set an attribute with a compound numeric type
cmds.setAttr('sphere.rotate', 0, 45, 90, type="double3")

Clamp the value of the attribute to the min/max
Useful floating point math leaves the value just
a little out of range - here the min is .01
cmds.setAttr( 'anisotropic1.roughness', 0.0099978, clamp=True )

Set a multi-attribute with a compound numeric type
cmds.setAttr( 'sphereShape.controlPoints[0:2]', 0, 0, 0, 1, 1, 1, 2, 2, 2,type="double3" )

---


Flags:
---


---
alteredValue(av): boolean
    properties: create
    The value is only the current value, which may change in the
next evalution (if the attribute has an incoming connection).
This flag is only used during file I/O, so that attributes
with incoming connections do not have their data overwritten
during the first evaluation after a file is opened.
Not supported for Ufe attributes.

---
caching(ca): boolean
    properties: create
    Sets the attribute's internal caching on or off. Not all attributes
can be defined as caching. Only those attributes that are not defined
by default to be cached can be made caching.  As well, multi attribute
elements cannot be made caching. Caching also affects child attributes
for compound attributes.
Not supported for Ufe attributes.

---
capacityHint(ch): uint
    properties: create
    Used to provide a memory allocation hint to attributes
where the -size flag cannot provide enough information.
This flag is optional and is primarily intended to be
used during file I/O.
Only certain attributes make use of this flag, and
the interpretation of the flag value varies per attribute.
Not supported for Ufe attributes.
This flag is currently used by (node.attribute):

mesh.face - hints the total number of elements in the face edge lists

---
channelBox(cb): boolean
    properties: create
    Sets the attribute's display in the channelBox on or off.
Keyable attributes are always display in the channelBox regardless of
the channelBox settting.
Not supported for Ufe attributes. The display of Ufe attributes in
the Channel Box is controlled using the channelBox command flag
-ual/ufeFixedAttrList.

---
clamp(c): boolean
    properties: create
    For numeric attributes, if the value is outside the
range of the attribute, clamp it to the min or max instead
of failing.
Not supported for Ufe attributes.

---
keyable(k): boolean
    properties: create
    Sets the attribute's keyable state on or off.
Not supported for Ufe attributes.

---
lock(l): boolean
    properties: create
    Sets the attribute's lock state on or off.

---
size(s): uint
    properties: create
    Defines the size of a multi-attribute array. This is only a hint,
used to help allocate memory as efficiently as possible.
Not supported for Ufe attributes.

---
type(typ): string
    properties: create
    Identifies the type of data.  If the -type flag
is not present, a numeric type is assumed.
Not supported for Ufe attributes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setAttr.html 
    """


def setAttrMapping(flagabsolute: boolean, flagattribute: string, flagaxis: string, flagclutch: string, flagdevice: string, flagoffset: float, flagrelative: boolean, flagscale: float, flagselection: boolean) -> None:
    """Synopsis:
---
---
 setAttrMapping([absolute=boolean], [attribute=string], [axis=string], [clutch=string], [device=string], [offset=float], [relative=boolean], [scale=float], [selection=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setAttrMapping is undoable, queryable, and NOT editable.
The value from the device is multiplied by the scale and the
offset is added to this product. With an absolute mapping, the
attached attribute gets the resulting value. If the mapping is
relative, the resulting value is added to the previous calculated
value. The calculated value will also take into account the
setInputDeviceMapping, if it was defined.

As an example, if the space ball is setup with absolute attachment
mappings, pressing in one direction will cause the
attached attribute to get a constant value. If a relative mapping
is used, and the spaceball is pressed in one direction, the
attached attribute will get a constantly increasing (or constantly
decreasing) value.

Note that the definition of relative is different than the definition
used by the setInputDeviceMapping command. In general, both
a relative attachment mapping (this command) and a relative
device mapping (setInputDeviceMapping) should not be used together
one the same axis.




Example:
---
import maya.cmds as cmds

cmds.attachDeviceAttr( d='spaceball', ax='XAxis', at='translateX' )
cmds.setAttrMapping( d='spaceball', ax='XAxis', at='translateX', scale=0.01 )

The first command will assign the XAxis of the spaceball to
the translateX attribute of the selected objects.
The second command sets the scaling of attribute value to
0.01 of the value of the axis. This results in finer control
since the motions of the spaceball are damped.

---


Flags:
---


---
absolute(a): boolean
    properties: create
    Make the mapping absolute.

---
attribute(at): string
    properties: create, multiuse
    The attribute used in the attachment.

---
axis(ax): string
    properties: create
    The axis on the device used in the attachment.

---
clutch(c): string
    properties: create
    The clutch button used in the attachment.

---
device(d): string
    properties: create
    The device used in the attachment.

---
offset(o): float
    properties: create
    Specify the offset value.

---
relative(r): boolean
    properties: create
    Make the mapping relative.

---
scale(s): float
    properties: create
    Specify the scale value.

---
selection(sl): boolean
    properties: create
    This flag specifies the mapping should be on the selected
objects

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setAttrMapping.html 
    """


def setDefaultShadingGroup() -> None:
    """Synopsis:
---
---
 setDefaultShadingGroup(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setDefaultShadingGroup is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a new blue shader
blinn = cmds.shadingNode( 'blinn', asShader=True )
cmds.setAttr( blinn+".color", 0.15, 0.35, 1.0,  type='double3' )
blinnSG = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='blinnSG' );
cmds.connectAttr( blinn+".outColor", blinnSG+".surfaceShader", force=True)

Make it the default
cmds.setDefaultShadingGroup( blinnSG )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setDefaultShadingGroup.html 
    """


def setDrivenKeyframe(flagattribute: string, flagcontrolPoints: boolean, flagcount: boolean, flagcurrentDriver: string, flagdriven: boolean, flagdriver: boolean, flagdriverValue: float, flaghierarchy: string, flaginTangentType: string, flaginsert: boolean, flaginsertBlend: boolean, flagoutTangentType: string, flagshape: boolean, flagvalue: float) -> int:
    """Synopsis:
---
---
 setDrivenKeyframe(
[objects]
    , [attribute=string], [controlPoints=boolean], [count=boolean], [currentDriver=string], [driven=boolean], [driver=boolean], [driverValue=float], [hierarchy=string], [inTangentType=string], [insert=boolean], [insertBlend=boolean], [outTangentType=string], [shape=boolean], [value=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setDrivenKeyframe is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a curve and a cone
---

cmds.curve(d=3,p=[(-10, 0, 0),(-6, 0, 10),(-3, 0, -10),(10, 0, 0)],k=[0, 0, 0, 1, 1, 1])
cmds.polyCone()

To set the keyframe on the selected object's translateX based on
curve1's rotateZ:
cmds.setDrivenKeyframe( at='translateX', cd='curve1.rz' )

To set the keyframe on pCone1.tx based on the value of curve1.rz:
cmds.setDrivenKeyframe( 'pCone1.tx', cd='curve1.rz' )

To query the current driver of pCone1.tx:
cmds.setDrivenKeyframe( 'pCone1.tx', q=True, cd=True )

To query the current driver count of pCone1.tx:
cmds.setDrivenKeyframe( 'pCone1.tx', q=True, cnt=True, cd=True )

To query the available drivers of pCone1.tx:
cmds.setDrivenKeyframe( 'pCone1.tx', q=True, dr=True )

To query the count of available drivers of pCone1.tx:
cmds.setDrivenKeyframe( 'pCone1.tx', q=True, cnt=True, dr=True )

---
Return:
---


    int: Number of keyframes set.

Flags:
---


---
attribute(at): string
    properties: create, multiuse
    Attribute name to set keyframes on.

---
controlPoints(cp): boolean
    properties: create
    Explicitly specify whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.

---
count(cnt): boolean
    properties: query
    Returns the count of driven/drivers attributes for the selected item
instead of the names

---
currentDriver(cd): string
    properties: create, query
    Set the driver to be used for the current driven keyframe to the
attribute passed as an argument.

---
driven(dn): boolean
    properties: query
    Returns list of driven attributes for the selected item.

---
driver(dr): boolean
    properties: query
    Returns list of available drivers for the attribute.

---
driverValue(dv): float
    properties: create, multiuse
    Value of the driver to use for this keyframe.
Default value is the current value.

---
hierarchy(hi): string
    properties: create
    Controls the objects this command acts on, relative to the specified
(or active) target objects.
Valid values are "above," "below," "both," and "none."
Default is "hierarchy -query"

---
inTangentType(itt): string
    properties: create
    The in tangent type for keyframes set by this command.
Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext"
Default is "keyTangent -q -g -inTangentType"

---
insert(i): boolean
    properties: create
    Insert keys at the given time(s) and preserve
the shape of the animation curve(s). Note: the tangent
type on inserted keys will be fixed so that the
curve shape can be preserved.

---
insertBlend(ib): boolean
    properties: create
    If true, a pairBlend node will be inserted for channels that have
nodes other than animCurves driving them, so that such channels can
have blended animation. If false, these channels will not have keys
inserted. If the flag is not specified, the blend will be inserted based
on the global preference for blending animation.

---
outTangentType(ott): string
    properties: create
    The out tangent type for keyframes set by this command.
Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext".
Default is "keyTangent -q -g -outTangentType"

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true

---
value(v): float
    properties: create
    Value to set the keyframe at. Default is the current value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setDrivenKeyframe.html 
    """


def setDynamic(flagallOnWhenRun: boolean, flagdisableAllOnWhenRun: boolean, flagsetAll: boolean, flagsetOff: boolean, flagsetOn: boolean) -> string:
    """Synopsis:
---
---
 setDynamic(
selectionList
    , [allOnWhenRun=boolean], [disableAllOnWhenRun=boolean], [setAll=boolean], [setOff=boolean], [setOn=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setDynamic is undoable, NOT queryable, and NOT editable.
WARNING: setDynamic is obsolescent.  This is the last version of
Maya in which it will be supported.




Example:
---
import maya.cmds as cmds

cmds.setDynamic( 'myParticles', on=True )
Sets myParticles.isDynamic true.

cmds.setDynamic( all=True, off=True )
Sets isDynamic false for all particle objects in the scene.

---
Return:
---


    string: array

Flags:
---


---
allOnWhenRun(awr): boolean
    properties: create
    Obsolete, no longer suppported or necessary.

---
disableAllOnWhenRun(dwr): boolean
    properties: create
    Obsolete, no longer suppported or necessary.

---
setAll(all): boolean
    properties: create
    Set for all objects.

---
setOff(off): boolean
    properties: create
    Sets isDynamic false.

---
setOn(on): boolean
    properties: create
    Sets isDynamic true.  This flag is set by default.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setDynamic.html 
    """


def setEditCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 setEditCtx(
name
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setEditCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.setEditCtx( 'setEditContext' )

---
Return:
---


    string: The name of the context

Flags:
---


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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setEditCtx.html 
    """


def setFluidAttr(flagaddValue: boolean, flagattribute: string, flagclear: boolean, flagfloatRandom: float, flagfloatValue: float, flaglowerFace: boolean, flagreset: boolean, flagvectorRandom: tuple[float, float, float], flagvectorValue: tuple[float, float, float], flagxIndex: int, flagxvalue: boolean, flagyIndex: int, flagyvalue: boolean, flagzIndex: int, flagzvalue: boolean) -> None:
    """Synopsis:
---
---
 setFluidAttr([addValue=boolean], [attribute=string], [clear=boolean], [floatRandom=float], [floatValue=float], [lowerFace=boolean], [reset=boolean], [vectorRandom=[float, float, float]], [vectorValue=[float, float, float]], [xIndex=int], [xvalue=boolean], [yIndex=int], [yvalue=boolean], [zIndex=int], [zvalue=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setFluidAttr is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

set density for entire fluid
cmds.setFluidAttr( at='density', fv=1.0 )

add 3.5 to the density at the cell x=1, y=2, z=3
cmds.setFluidAttr( at='density', ad=True, fv-3.5, xi=1, yi=2, zi=3 )

clear the density for the whole fluid
cmds.setFluidAttr( at='density', cl=True )

reset the velocity at the cell x=1, y=2, z=3
cmds.setFluidAttr( at='velocity', re=True, xi=1, yi=2, zi=3 )

set the velocity at the centers of the voxels on plane y=5
to approximately (-1, 0, 0)
cmds.setFluidAttr( at='velocity', vv=(-1, 0, 0), yi=5 )

set the Z-component of the velocity at the bottom of cell [0, 0, 0]
to exactly 1.3
cmds.setFluidAttr( at='velocity', z=True, xi=0, yi=0, zi=0, fv=1.3 )

set the X-component of the velocity at the right of cell [5, 3, 2]
(which is also the left of cell [6, 3, 2]) to exactly 4.8
cmds.setFluidAttr( at='velocity', x=True, xi=5, yi=3, zi=2, fv=4.8 )

set the density to a random value in the range 0.1 to 0.9
the fv flag specfies the base value, and then we add a a
random value in the range of -fr to +fr
cmds.setFluidAttr( at='density', fv=0.5, fr=0.4 )

---


Flags:
---


---
addValue(ad): boolean
    properties: 
    Add specified value to attribute

---
attribute(at): string
    properties: create
    Specifies the fluid attribute for which to set values.  Valid
attributes are "velocity", "density", "fuel", "color", "falloff", and "temperature".

---
clear(cl): boolean
    properties: 
    Set this attribute to 0

---
floatRandom(fr): float
    properties: 
    If this was a scalar (e.g. density) attribute, use a random value in +-VALUE
If fv is specified, it is used as the base value and combined with the
random value. If the fv flag is not specified, the  base is assumed to be 0.

---
floatValue(fv): float
    properties: 
    If this was a scalar (e.g. density) attribute, use this value

---
lowerFace(lf): boolean
    properties: create
    Only valid with "-at velocity".  Since velocity values are stored on the edges
of each voxel and not at the center, using voxel based indices to set velocity
necessarily affects neighboring voxels.  Use this flag to only set velocity
components on the lower left three faces of a voxel, rather than all six.

---
reset(re): boolean
    properties: 
    Set this attribute to default value

---
vectorRandom(vr): [float, float, float]
    properties: 
    If this was a vector (e.g. velocity) attribute, use a random value in +-VALUE
If vv is specified, it is used as the base value and combined with the
random value. If the vv flag is not specified, the  base is assumed to be 0,0,0.

---
vectorValue(vv): [float, float, float]
    properties: 
    If this was a vector (e.g. velocity) attribute, use this value

---
xIndex(xi): int
    properties: create
    Only return values for cells with this X index

---
xvalue(x): boolean
    properties: 
    Only set the first component of the vector-valued attribute specified by
the "-at/attribute" flag.

---
yIndex(yi): int
    properties: create
    Only return values for cells with this Y index

---
yvalue(y): boolean
    properties: 
    Only set the second component of the vector-valued attribute specified by
the "-at/attribute" flag.

---
zIndex(zi): int
    properties: create
    Only return values for cells with this Z index

---
zvalue(z): boolean
    properties: 
    Only set the third component of the vector-valued attribute specified by
the "-at/attribute" flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setFluidAttr.html 
    """


def setFocus() -> None:
    """Synopsis:
---
---
 setFocus(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setFocus is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.textField('tf0', changeCommand='cmds.setFocus("tf1")' )
cmds.textField('tf1', changeCommand='cmds.setFocus("tf2")' )
cmds.textField('tf2', changeCommand='cmds.setFocus("tf0")' )
cmds.showWindow()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setFocus.html 
    """


def setInfinity(flagattribute: string, flagcontrolPoints: boolean, flaghierarchy: string, flagpostInfinite: string, flagpreInfinite: string, flagshape: boolean) -> None:
    """Synopsis:
---
---
 setInfinity(
objects
    , [attribute=string], [controlPoints=boolean], [hierarchy=string], [postInfinite=string], [preInfinite=string], [shape=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setInfinity is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Set preInfinite and postInfinite type on curves of currently selected objects
---

cmds.setInfinity( pri='linear', poi='constant' )

Set postInfinite type of cube1's curves
---

cmds.setInfinity( 'cube1', poi='oscillate' )

Set preInfinite type of cube1's "Translate X" curve
---

cmds.setInfinity( 'cube1', pri='linear', attribute='translateX' )

---


Flags:
---


---
attribute(at): string
    properties: create, multiuse
    List of attributes to select
      In query mode, this flag needs a value.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
hierarchy(hi): string
    properties: create
    Hierarchy expansion options.  Valid values are "above,"
"below," "both," and "none." (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
postInfinite(poi): string
    properties: create, query
    Set the infinity type after a paramCurve's last keyframe. Valid
values are "constant", "linear", "cycle", "cycleRelative", "oscillate".

---
preInfinite(pri): string
    properties: create, query
    Set the infinity type before a paramCurve's first keyframe. Valid
values are "constant", "linear", "cycle", "cycleRelative", "oscillate".

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setInfinity.html 
    """


def setInputDeviceMapping(flagabsolute: boolean, flagaxis: string, flagdevice: string, flagoffset: float, flagrelative: boolean, flagscale: float, flagview: boolean, flagworld: boolean) -> None:
    """Synopsis:
---
---
 setInputDeviceMapping([absolute=boolean], [axis=string], [device=string], [offset=float], [relative=boolean], [scale=float], [view=boolean], [world=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setInputDeviceMapping is undoable, NOT queryable, and NOT editable.
The value from the device is multiplied by the scale and the
offset is added to this product. With an absolute mapping, the
attached attribute gets the resulting value. If the mapping is
relative, the final value is the offset added to the scaled
difference between the current device value and the previous
device value.

This mapping will be applied to the device data before any
mappings defined by the setAttrMapping command. A typical use
would be to scale a device's input so that it is within a usable
range. For example, the device mapping can be used to calibrate
a spaceball to work in a specific section of a scene.

As an example, if the space ball is setup with absolute device
mappings, constantly pressing in one direction will cause the
attached attribute to get a constant value. If a relative mapping
is used, and the spaceball is pressed in one direction, the
attached attribute will jump a constantly increasing (or constantly
decreasing) value and will find a rest value equal to the offset.

There are important differences between how the relative flag
is handled by this command and the setAttrMapping command. (See
the setAttrMapping documentation for specifics on how it calculates
relative values). In general,
both a relative device mapping (this command) and a relative
attachment mapping (setAttrMapping) should not be used together
on the same axis.




Example:
---
import maya.cmds as cmds

cmds.assignInputDevice( '"move -r XAxis YAxis ZAxis"', d='spaceball' )
cmds.setInputDeviceMapping( d='spaceball', ax=['XAxis', 'YAxis', 'ZAxis'], scale=0.01, r=True )

The first command will assign the move command to the spaceball.
The second command will scale the three named axes by 0.01 and
only return the changes in device position.

---


Flags:
---


---
absolute(a): boolean
    properties: create
    report absolute axis values

---
axis(ax): string
    properties: create, multiuse
    specify the axis to map

---
device(d): string
    properties: create
    specify which device to map

---
offset(o): float
    properties: create
    specify the axis offset value

---
relative(r): boolean
    properties: create
    report the change in axis value since
the last sample

---
scale(s): float
    properties: create
    specify the axis scale value

---
view(v): boolean
    properties: create
    translate the device coordinates into the coordinates
of the active camera

---
world(w): boolean
    properties: create
    translate the device coordinates into world space
coordinates

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setInputDeviceMapping.html 
    """


def setKeyCtx(flagbreakdown: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagpreserveTangent: boolean) -> boolean:
    """Synopsis:
---
---
 setKeyCtx(
contextName
    , [breakdown=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [preserveTangent=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a set key context for the graph editor
---

cmds.setKeyCtx( 'setKeyContext' )

---
Return:
---


    boolean: Value of the breakdown flag, when queried

Flags:
---


---
breakdown(bd): boolean
    properties: query, edit
    Specifies whether or not to create breakdown keys

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
preserveTangent(pt): boolean
    properties: query, edit
    Specifies whether or not to preserve tangent

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setKeyCtx.html 
    """


def setKeyPath() -> list[string]:
    """Synopsis:
---
---
 setKeyPath(
[object]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setKeyPath is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Apply setKeyPath command on the currently selected object at current time:
cmds.setKeyPath()

Apply setKeyPath command on an object named "ball" at current time:
cmds.setKeyPath( 'ball' )

---
Return:
---


    list[string]: (Names of the created curve node and motionPath node)

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setKeyPath.html 
    """


def setKeyframe(flagadjustTangent: boolean, flaganimLayer: string, flaganimated: boolean, flagattribute: string, flagbreakdown: boolean, flagclip: string, flagcontrolPoints: boolean, flagdirtyDG: boolean, flagfloat: float, flaghierarchy: string, flagidentity: boolean, flaginTangentType: string, flaginsert: boolean, flaginsertBlend: boolean, flagminimizeRotation: boolean, flagnoResolve: boolean, flagoutTangentType: string, flagpreserveCurveShape: boolean, flagrespectKeyable: boolean, flagshape: boolean, flagtime: time, flaguseCurrentLockedWeights: boolean, flagvalue: float) -> int:
    """Synopsis:
---
---
 setKeyframe(
[objects]
    , [adjustTangent=boolean], [animLayer=string], [animated=boolean], [attribute=string], [breakdown=boolean], [clip=string], [controlPoints=boolean], [dirtyDG=boolean], [float=float], [hierarchy=string], [identity=boolean], [inTangentType=string], [insert=boolean], [insertBlend=boolean], [minimizeRotation=boolean], [noResolve=boolean], [outTangentType=string], [preserveCurveShape=boolean], [respectKeyable=boolean], [shape=boolean], [time=time], [useCurrentLockedWeights=boolean], [value=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setKeyframe is undoable, queryable, and editable.
The default time for the new keyframes is the current time.
Override this behavior with the "-t" flag on the command line.

The default value for the keyframe is the current value
of the attribute for which a keyframe is set.  Override
this behavior with the "-v" flag on the command line.

When setting keyframes on animation curves that do not have
"time" as an input attribute (ie, they are unitless animation curves),
use "-f/-float" to specify the unitless value at which to set a
keyframe.

The -time and -float flags may be combined in one command.

This command sets up Dependency Graph relationships for
proper evaluation of a given attribute at a given time.




Example:
---
import maya.cmds as cmds

Set a keyframe at the current time on all "keyable"
attributes of the selected objects.
---

cmds.setKeyframe()

Set a keyframe so that translateX has a value of 10
at the current time, regardless of its current position
---

cmds.setKeyframe( v=10, at='translateX' )

Set keyframes for translateX on two objects at t=0 and
t=10 seconds.  (Note that if mysteryObject has no
attribute named translateX, no keyframe is set for mysteryObject.)
---

cmds.setKeyframe( 'nurbsSphere1', 'mysteryObject', attribute='translateX', t=['0sec','10sec'] )

---
Return:
---


    int: Number of keyframes set by this command.

Flags:
---


---
adjustTangent(adt): boolean
    properties: create
    Adjsut tangent if insert keys

---
animLayer(al): string
    properties: create
    Specifies that the new key should be placed in the specified animation layer.
Note that if the objects being keyframed are not already part of the
layer, this flag will be ignored.

---
animated(an): boolean
    properties: create
    Add the keyframe only to the attribute(s) that have already a keyframe on. Default: false

---
attribute(at): string
    properties: create, multiuse
    Attribute name to set keyframes on.

---
breakdown(bd): boolean
    properties: create, query, edit
    Sets the breakdown state for the key.  Default is false

---
clip(c): string
    properties: create
    Specifies that the new key should be placed in the specified clip.
Note that if the objects being keyframed are not already part of the
clip, this flag will be ignored.

---
controlPoints(cp): boolean
    properties: create
    Explicitly specify whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.

---
dirtyDG(dd): boolean
    properties: create
    Allow dirty messages to be sent out when a keyframe is set.

---
float(f): float
    properties: create, multiuse
    Float time at which to set a keyframe on float-based
animation curves.

---
hierarchy(hi): string
    properties: create
    Controls the objects this command acts on, relative to the specified
(or active) target objects.
Valid values are "above," "below," "both," and "none."
Default is "hierarchy -query"

---
identity(id): boolean
    properties: create
    Sets an identity key on an animation layer.  An identity key is one that
nullifies the effect of the anim layer.  This flag has effect only when the
attribute being keyed is being driven by animation layers.

---
inTangentType(itt): string
    properties: create
    The in tangent type for keyframes set by this command.
Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext"
Default is "keyTangent -q -g -inTangentType"

---
insert(i): boolean
    properties: create
    Insert keys at the given time(s) and preserve
the shape of the animation curve(s). Note: the tangent
type on inserted keys will be fixed so that the
curve shape can be preserved.

---
insertBlend(ib): boolean
    properties: create
    If true, a pairBlend node will be inserted for channels that have
nodes other than animCurves driving them, so that such channels can
have blended animation. If false, these channels will not have keys
inserted. If the flag is not specified, the blend will be inserted based
on the global preference for blending animation.

---
minimizeRotation(mr): boolean
    properties: create
    For rotations, ensures that the key that is set is a minimum distance
away from the previous key.  Default is false

---
noResolve(nr): boolean
    properties: create
    When used with the -value flag, causes the specified value to be set
directly onto the animation curve, without attempting to resolve the value
across animation layers.

---
outTangentType(ott): string
    properties: create
    The out tangent type for keyframes set by this command.
Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext".
Default is "keyTangent -q -g -outTangentType"

---
preserveCurveShape(pcs): boolean
    properties: create
    Sets the preserve curve shape when inserting keys.
Default value depend on your keySetPreserveCurveShape option.

---
respectKeyable(rk): boolean
    properties: create
    When used with the -attribute flag, prevents the keying of the non keyable attributes.

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true

---
time(t): time
    properties: create, multiuse
    Time at which to set a keyframe on time-based
animation curves.

---
useCurrentLockedWeights(lw): boolean
    properties: create
    If we are setting a key over an existing key, use that key tangent's locked weight value for the new
locked weight value.  Default is false

---
value(v): float
    properties: create
    Value at which to set the keyframe. Using the value flag will not
cause the keyed attribute to change to the specified value until the
scene re-evaluates. Therefore, if you want the attribute to update
to the new value immediately, use the setAttr command
in addition to setting the key.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setKeyframe.html 
    """


def setKeyframeBlendshapeTargetWts() -> int:
    """Synopsis:
---
---
 setKeyframeBlendshapeTargetWts()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setKeyframeBlendshapeTargetWts is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

first create a blendShape
---

cmds.polySphere()
cmds.duplicate()
cmds.duplicate()
cmds.select( 'pSphere2', 'pSphere1', 'pSphere3', r=True )
cmds.blendShape()

Select one of the targets, and key its per-point weights.
Typically this would be done after painting per-point weights
for the target.
---

cmds.select( 'pSphere2', r=True )
cmds.setKeyframeBlendshapeTargetWts()

---
Return:
---


    int: number of vertices for which the targets weights are keyed

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setKeyframeBlendshapeTargetWts.html 
    """


def setMenuMode() -> string:
    """Synopsis:
---
---
 setMenuMode([string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setMenuMode is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Use the "Rendering" Menu Set, and at the same time get the one currently used.
prevMenuMode = cmds.setMenuMode('renderingMenuSet')

Print the current Menu Set: "renderingMenuSet".
print( cmds.setMenuMode() )

---
Return:
---


    string: The current Menu Mode for the menu bar in the main Maya window.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setMenuMode.html 
    """


def setNodeTypeFlag(flagdisplay: boolean, flagthreadSafe: boolean) -> boolean:
    """Synopsis:
---
---
 setNodeTypeFlag(
[string]
    , [display=boolean], [threadSafe=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setNodeTypeFlag is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

don't display unit conversion nodes
cmds.setNodeTypeFlag( cmds.objectType(tagFromType='unitConversion'), display=False )
Returns True

don't display legacy render layers
cmds.setNodeTypeFlag("renderLayer", display=False)
Returns True

ask for the value of the display flag of unit conversion nodes
cmds.setNodeTypeFlag(cmds.objectType(tagFromType='unitConversion'), query=True, display=True)
Returns False

ask for the value of the display flag of legacy render layers nodes
cmds.setNodeTypeFlag("renderLayer", query=True, display=True)
Returns False

---
Return:
---


    boolean: Did the command succeed?

Flags:
---


---
display(dsp): boolean
    properties: create, query
    Sets whether the node type will appear in the UI or not.  Setting
display to false will cause the node type to not appear in the UI.
Query mode to obtain the value of the display flag.

---
threadSafe(ts): boolean
    properties: create, query
    This flag is obsolete.  Has no effect.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setNodeTypeFlag.html 
    """


def setParent(flagdefineTemplate: string, flagmenu: boolean, flagtopLevel: boolean, flagupLevel: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 setParent(
[string]
    , [defineTemplate=string], [menu=boolean], [topLevel=boolean], [upLevel=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setParent is undoable, queryable, and NOT editable.
 A control must be parented to a control layout.  A control layout may
be parented to another control layout or a window.  A menu may be parented
to a window or a menu bar layout.  For all of these cases
the setParent command (with no flags) will indicate the current
default parent.

 A menu item must be parented to a menu.  To specify the default menu
parent use the command setParent -m/menu.  Note that all menu item
objects created using the -sm/subMenu may also be treated as menu
objects.

 The default parent is ignored by any object that explicitly sets the
-p/parent flag when it is created.




Example:
---
import maya.cmds as cmds

 Create a window with a menu bar and two menu bar layouts.
---

window = cmds.window(menuBar=True, widthHeight=(300, 200) )
fileMenu = cmds.menu( label='File')
cmds.menuItem( label='Open' )

cmds.paneLayout( configuration='vertical2' )

leftMenuBarLayout = cmds.menuBarLayout()
leftMenu = cmds.menu( label='Left' )
cmds.menuItem( label='One' )
cmds.setParent( '..' )

cmds.menuBarLayout()
cmds.menu( label='Right' )
rightSubMenu = cmds.menuItem(subMenu=True, label='Colors' )
cmds.setParent( '..' )
cmds.showWindow( window )

 Add item to the "File" menu.
---

cmds.setParent( fileMenu, menu=True )
cmds.menuItem( label='Save' )

 Add item to the "Left" menu, explicitly ignore default parent
   by setting -p/parent flag.
---

cmds.menuItem( parent=leftMenu, label='Two' )

 Add more items to the "File" menu because it is still the
   default parent.
---

cmds.menuItem( divider=True )
cmds.menuItem( label='Close' )

 Add another menu to the left menu bar layout.
---

cmds.setParent( leftMenuBarLayout )
cmds.menu( label='Middle' )
cmds.menuItem( label='Three' )

 Add items to right sub menu.
---

cmds.setParent( rightSubMenu, menu=True )
cmds.menuItem( label='Red' )
cmds.menuItem( label='Blue' )
cmds.menuItem( label='Green' )

---
Return:
---


    string: Name of the parent if the parent changes. Empty string if the parent
doesn't change.

Flags:
---


---
defineTemplate(dt): string
    properties: create
    Put a command in a mode where any other flags and args
are parsed and added to the command template with the given name.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
menu(m): boolean
    properties: create, query
    Parent menu for menu items.

---
topLevel(top): boolean
    properties: create
    Move to the top level layout in the hierarchy. Equivalent to use "|"

---
upLevel(u): boolean
    properties: create
    Move up one level in the hierarchy. Equivalent to use ".."

---
useTemplate(ut): string
    properties: create
    Will force the command to use a command template given by the name other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setParent.html 
    """


def setParticleAttr(flagattribute: string, flagfloatValue: float, flagobject: string, flagrandomFloat: float, flagrandomVector: tuple[float, float, float], flagrelative: boolean, flagvectorValue: tuple[float, float, float]) -> None:
    """Synopsis:
---
---
 setParticleAttr(
selectionList
    , [attribute=string], [floatValue=float], [object=string], [randomFloat=float], [randomVector=[float, float, float]], [relative=boolean], [vectorValue=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setParticleAttr is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.setParticleAttr( 'particle1', at='velocity', vv=(1, 2, 3) )
This will set the velocity of all of the particles in particle1
to << 1, 2, 3 >>.

cmds.select( 'particleShape1.pt[0:7]', 'particleShape1.pt[11]' )
cmds.setParticleAttr( vv=(1, 2, 3), at='velocity' )
cmds.setParticleAttr( 'particleShape1', at='velocity' )

This will set the velocity of particles 0-7 and 11 of
particleShape1 to << 1, 2, 3 >>.  The rest of the particles are
not changed.

---


Flags:
---


---
attribute(at): string
    properties: create
    Tells the action which attribute you want to set

---
floatValue(fv): float
    properties: create
    Tells what you want the value to be set to of a float attribute

---
object(o): string
    properties: create
    If this flag is passed and the STRING is the name of a particle object's transform or shape,
then ONLY that object will be edited, ignoring the selection list or command line, and
ALL of its particles' values will be changed for the specified attribute.

---
randomFloat(rf): float
    properties: create
    Tells the command to add a random value from -FLOAT to +FLOAT to
the results of each particle.  The default is 0.0.

---
randomVector(rv): [float, float, float]
    properties: create
    Tells the command to add a random value from <<-x,-y,-z>> to <<x,y,z>> to
the results of each particle. The default 0 0 0.

---
relative(r): boolean
    properties: create
    If this is set to TRUE (the default is FALSE), then the float or vector value will be added to the current value
for each particle.

---
vectorValue(vv): [float, float, float]
    properties: create
    Tells what you want the value to be set to of a vector
attribute

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setParticleAttr.html 
    """


def setRenderPassType(flagdefaultDataType: boolean, flagnumChannels: int, flagtype: string) -> boolean:
    """Synopsis:
---
---
 setRenderPassType([defaultDataType=boolean], [numChannels=int], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setRenderPassType is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

create a render pass for diffuse reflection
---

cmds.createNode( 'renderPass', name='myDiffusePass' );
Result: myDiffusePass ---


cmds.setRenderPassType( 'myDiffusePass', type='diffuse' );
Result: true ---


---
Return:
---


    boolean: true/false

Flags:
---


---
defaultDataType(d): boolean
    properties: create
    If set, the render pass will use its default data type.

---
numChannels(n): int
    properties: create
    Specify the number of channels to use in the render pass. Note that
this flag is only valid if there is an implementation supporting the
requested number of channels.

---
type(t): string
    properties: create
    Specify the pass type to assign to the pass node(s).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setRenderPassType.html 
    """


def setStartupMessage() -> None:
    """Synopsis:
---
---
 setStartupMessage(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setStartupMessage is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.setStartupMessage( 'Initializing Main View' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setStartupMessage.html 
    """


def setToolTo() -> None:
    """Synopsis:
---
---
 setToolTo(
[string]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setToolTo is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.setToolTo( 'moveSuperContext' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setToolTo.html 
    """


def setUITemplate(flagpopTemplate: boolean, flagpushTemplate: boolean) -> string:
    """Synopsis:
---
---
 setUITemplate(
[string]
    , [popTemplate=boolean], [pushTemplate=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setUITemplate is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

   Create a new template.
---

if cmds.uiTemplate( 'ExampleTemplate', exists=True ):
        cmds.deleteUI( 'ExampleTemplate', uiTemplate=True )

cmds.uiTemplate( 'ExampleTemplate' )

cmds.button( defineTemplate='ExampleTemplate', width=100, height=40, align='left' )
cmds.frameLayout( defineTemplate='ExampleTemplate', borderVisible=True, labelVisible=False )

   Create a window and apply the template.
---

window = cmds.window()
cmds.setUITemplate( 'ExampleTemplate', pushTemplate=True )
cmds.columnLayout( rowSpacing=5 )

cmds.frameLayout()
cmds.columnLayout()
cmds.button( label='One' )
cmds.button( label='Two' )
cmds.button( label='Three' )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.frameLayout()
cmds.columnLayout()
cmds.button( label='Red' )
cmds.button( label='Green' )
cmds.button( label='Blue' )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.setUITemplate( popTemplate=True )

cmds.showWindow( window )

---
Return:
---


    string: The name of the currently selected command template.

Flags:
---


---
popTemplate(ppt): boolean
    properties: create
    Pop the current template off of the stack and sets the next template
on the stack to be current.

---
pushTemplate(pst): boolean
    properties: create
    Push the current template onto a stack that can later be popped.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setUITemplate.html 
    """


def setXformManip(flagshowUnits: boolean, flagsuppress: boolean, flaguseRotatePivot: boolean, flagworldSpace: boolean) -> None:
    """Synopsis:
---
---
 setXformManip([showUnits=boolean], [suppress=boolean], [useRotatePivot=boolean], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

setXformManip is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

makes manip disappear
cmds.setXformManip( suppress=True )

set manip to object space
cmds.setXformManip( worldSpace=False )

returns false
cmds.setXformManip( q=True, ws=True )

---


Flags:
---


---
showUnits(su): boolean
    properties: query
    If set to true, the xform manip displays current units;
otherwise, the manip hides them.

---
suppress(s): boolean
    properties: query
    If set to true, the xform manip is suppressed and therefore
not visible or usable.

---
useRotatePivot(urp): boolean
    properties: query
    If set to true, the xform manip uses the rotate pivot;
otherwise, the manip uses the bounding-box center. Defaults false.

---
worldSpace(ws): boolean
    properties: query
    If set to true, the xform manip is always in world space.
If false, the manip is in object space. (Note: when multiple
objects are selected the manip is always in world space, no
matter what this is set to)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/setXformManip.html 
    """


def sets(flagaddElement: name, flagafterFilters: boolean, flaganyMember: name, flagclear: name, flagcolor: int, flagcopy: name, flagedges: boolean, flageditPoints: boolean, flagempty: boolean, flagfacets: boolean, flagflatten: name, flagforceElement: name, flaginclude: name, flagintersection: name, flagisIntersecting: name, flagisMember: name, flaglayer: boolean, flagname: string, flagnoIntermediate: boolean, flagnoSurfaceShader: boolean, flagnoWarnings: boolean, flagnodesOnly: boolean, flagremove: name, flagrenderable: boolean, flagsize: boolean, flagsplit: name, flagsubtract: name, flagtext: string, flagunion: name, flagvertices: boolean) -> boolean | list[string] | string:
    """Synopsis:
---
---
 sets(
selectionList
    , [addElement=name], [afterFilters=boolean], [anyMember=name], [clear=name], [color=int], [copy=name], [edges=boolean], [editPoints=boolean], [empty=boolean], [facets=boolean], [flatten=name], [forceElement=name], [include=name], [intersection=name], [isIntersecting=name], [isMember=name], [layer=boolean], [name=string], [noIntermediate=boolean], [noSurfaceShader=boolean], [noWarnings=boolean], [nodesOnly=boolean], [remove=name], [renderable=boolean], [size=boolean], [split=name], [subtract=name], [text=string], [union=name], [vertices=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sets is undoable, queryable, and editable.
Sets are used throughout Maya in a multitude of ways. They are used
to define an association of material properties to objects, to define
an association of lights to objects, to define a bookmark or named
collection of objects, to define a character, and to define the
components to be deformed by some deformation operation.

Sets can be connected to any number of partitions. A partition is
a node which enforces mutual exclusivity amoung the sets in the
partition. That is, if an object is in a
set which is in a partition, that object cannot be a member of any
other set that is in the partition.

Without any flags, the sets command will create a set with a
default name of "set#" (where # is an integer). If no items are
specified on the command line, the currently selected items are added
to the set. The -em/empty flag can be used to create an empty
set and not have the selected items added to the set.

Sets can be created to have certain restrictions on membership. There
can be "renderable" sets which only allow renderable objects (such as
nurbs geometry or polymesh faces) to be members of the set. There can
also be vertex (or control point), edit point, edge, or face sets
which only allow those types of components to be members of a set.
Note that for these sets, if an object with a valid type of component
is to be added to a set, the components of the object are
added to the set instead.

Sets can have an associated color which is only of use
when creating vertex sets. The color can be one of the eight user
defined colors defined in the color preferences. This color can
be used, for example to distinguish which vertices are being deformed
by a particular deformation.

Objects, components, or attributes can be added to a set using one of
three flags. The -add/addElement flag will add the objects to a set as
long as this won't break any mutual exclusivity constraints. If there
are any items which can't be added, the command will fail. The
-in/include flag will only add those items which can be added and
warn of those which can't. The -fe/forceElement flag will add all the
items to the set but will also remove any of those items that are in
any other set which is in the same partition as the set.

There are several operations on sets that can be performed with the
sets command. Membership can be queried. Tests for whether
an item is in a set or whether two sets share the same item
can be performed. Also, the union, intersection and
difference of sets can be performed which returns a list of members
of the sets which are a result of the operation.




Example:
---
import maya.cmds as cmds

create some objects
cmds.sphere( n="sphere1" )
cmds.cone( n="cone1" )

create a set with whatever is currently active
cmds.select( 'sphere1' )
newSet1 = cmds.sets()
cmds.select( 'cone1' )
newSet2 = cmds.sets()

Query the members of a set
cmds.sets( newSet1, q=True )

create a set which contains two sets
cmds.sets( newSet1, newSet2, n="setOfSets" )

To select a set, the -noExpand flag must be used. Otherwise
the members of a set are selected instead.
cmds.select( newSet1, noExpand=True )
cmds.ls( selection=True )

Select the members of a set
cmds.select( newSet1 )
cmds.ls( selection=True )

Create a vertex set named ballVertices. This will contain
all the vertices of the sphere.
cmds.sets( 'sphere1', n="ballVertices", v=1 )
cmds.select( 'ballVertices' )

Return the union of two sets
cmds.sets( newSet2, un=newSet1 )

Test whether a list of sets have common members
cmds.sets( 'ballVertices',ii=newSet1)

Test whether the sphere is a member of the set
cmds.sets('sphere1',im=newSet1)

Remove the sphere from a set
cmds.sets( 'sphere1', rm=newSet1 )

Test again whether the sphere is a member of the set
cmds.sets( 'sphere1', im=newSet1 )

---
Return:
---


    string: For creation operations (name of the set that was created or edited)
    list[string]: For query operation (names of items in the set)
    boolean: For isIntersecting and isMember operations

Flags:
---


---
addElement(add): name
    properties: edit
    Adds the list of items to the given set.  If some of the
items cannot be added to the set because they are in another
set which is in the same partition as the set to edit, the
command will fail.

---
afterFilters(af): boolean
    properties: edit
    Default state is false. This flag is valid in edit mode only.
This flag is for use on sets that are acted on by deformers
such as sculpt, lattice, blendShape. The default edit mode
is to edit the membership of the group acted on by the deformer.
If you want to edit the group but not change the membership of
the deformer, set the flag to true.

---
anyMember(am): name
    properties: create
    An operation which tests whether any of the given items
are members of the given set.

---
clear(cl): name
    properties: edit
    An operation which removes all items from the given set making
the set empty.

---
color(co): int
    properties: create, query, edit
    Defines the hilite color of the set. Must be a value in
range [-1, 7] (one of the user defined colors).  -1 marks the
color has being undefined and therefore not having any affect.
Only the vertices of a vertex set will be displayed in this
color.

---
copy(cp): name
    properties: create
    Copies the members of the given set to a new set.
This flag is for use in creation mode only.

---
edges(eg): boolean
    properties: create, query
    Indicates the new set can contain edges only.
This flag is for use in creation or query mode only.
The default value is false.

---
editPoints(ep): boolean
    properties: create, query
    Indicates the new set can contain editPoints only.
This flag is for use in creation or query mode only.
The default value is false.

---
empty(em): boolean
    properties: create
    Indicates that the set to be created should be empty. That is,
it ignores any arguments identifying objects to be added to
the set. This flag is only valid for operations that create a new set.

---
facets(fc): boolean
    properties: create, query
    Indicates the new set can contain facets only.
This flag is for use in creation or query mode only.
The default value is false.

---
flatten(fl): name
    properties: edit
    An operation that flattens the structure of the given set.
That is, any sets contained by the given set will be replaced by
its members so that the set no longer contains other sets but
contains the other sets' members.

---
forceElement(fe): name
    properties: edit
    For use in edit mode only. Forces addition of the items
to the set. If the items are in another set which is in the
same partition as the given set, the items will be removed
from the other set in order to keep the sets in the partition
mutually exclusive with respect to membership.

---
include(include): name
    properties: edit
    Adds the list of items to the given set.  If some of the
items cannot be added to the set, a warning will be issued.
This is a less strict version of the -add/addElement operation.

---
intersection(int): name
    properties: create
    An operation that returns a list of items which are members of
all the sets in the list.

---
isIntersecting(ii): name
    properties: create
    An operation which tests whether the sets in the list have
common members.

---
isMember(im): name
    properties: create
    An operation which tests whether all the given items
are members of the given set.

---
layer(l): boolean
    properties: create
    OBSOLETE. DO NOT USE.

---
name(n): string
    properties: create
    Assigns string as the name for a new set. This flag is
only valid for operations that create a new set.

---
noIntermediate(ni): boolean
    properties: create, query
    Excludes intermediate objects when querying set members or
using the subtract, union, itersection, or isIntersecting
flags.

---
noSurfaceShader(nss): boolean
    properties: create
    If set is renderable, do not connect it to the default surface
shader.  Flag has no meaning or effect for non renderable sets.
This flag is for use in creation mode only.
The default value is false.

---
noWarnings(nw): boolean
    properties: create
    Indicates that warning messages should not be reported such
as when trying to add an invalid item to a set. (used by UI)

---
nodesOnly(no): boolean
    properties: query
    This flag is usable with the -q/query flag but is ignored if
used with another queryable flags. This flag modifies the results
of the set membership query such that
when there are attributes (e.g. sphere1.tx) or components of
nodes included in the set, only the nodes will be listed.
Each node will only be listed once, even if more than one attribute
or component of the node exists in the set.

---
remove(rm): name
    properties: edit
    Removes the list of items from the given set.

---
renderable(r): boolean
    properties: create, query
    This flag indicates that a special type of set should
be created. This type of set (shadingEngine as opposed to
objectSet) has certain restrictions on its membership in that
it can only contain renderable elements such as lights and
geometry. These sets are referred to as shading groups and
are automatically connected to the "renderPartition" node when
created (to ensure mutual exclusivity of the set's members with
the other sets in the partition).
This flag is for use in creation or query mode only.
The default value is false which means a normal set is
created.

---
size(s): boolean
    properties: query
    Use the size flag to query the length of the set.

---
split(sp): name
    properties: create
    Produces a new set with the list of items and removes
each item in the list of items from the given set.

---
subtract(sub): name
    properties: create
    An operation between two sets which returns the members of the
first set that are not in the second set.

---
text(t): string
    properties: create, query, edit
    Defines an annotation string to be stored with the set.

---
union(un): name
    properties: create
    An operation that returns a list of all the members of all sets
listed.

---
vertices(v): boolean
    properties: create, query
    Indicates the new set can contain vertices only.
This flag is for use in creation or query mode only.
The default value is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sets.html 
    """


def shadingConnection(flagconnectionState: boolean) -> None:
    """Synopsis:
---
---
 shadingConnection(
attribute
    , [connectionState=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shadingConnection is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.shadingConnection( 'lambert1.color', e=True, cs=0 )
cmds.shadingConnection( 'spotLightShape1.intensity', q=True, cs=True )

---


Flags:
---


---
connectionState(cs): boolean
    properties: create, query, edit
    Specifies the state of the connection.
On/True/1 means the connection is still active.
Off/False/0 means the connection is inactive.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shadingConnection.html 
    """


def shadingGeometryRelCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagoffCommand: string, flagonCommand: string, flagshadingCentric: boolean) -> string:
    """Synopsis:
---
---
 shadingGeometryRelCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [offCommand=string], [onCommand=string], [shadingCentric=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shadingGeometryRelCtx is undoable, queryable, and editable.
Specifying -shadingCentric false means that the geometry is to be selected
first.  The shading group associated with the geometry will then be selected
and subsequent selections will result in assignments being made.




Example:
---
import maya.cmds as cmds

cmds.shadingGeometryRelCtx()

---
Return:
---


    string: Name of the context created.

Flags:
---


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
offCommand(ofc): string
    properties: create, query, edit
    command to be issued when context is turned on

---
onCommand(onc): string
    properties: create, query, edit
    command to be issued when context is turned on

---
shadingCentric(s): boolean
    properties: create, query, edit
    shading-centric mode.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shadingGeometryRelCtx.html 
    """


def shadingLightRelCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagoffCommand: string, flagonCommand: string, flagshadingCentric: boolean) -> string:
    """Synopsis:
---
---
 shadingLightRelCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [offCommand=string], [onCommand=string], [shadingCentric=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shadingLightRelCtx is undoable, queryable, and editable.
Specifying -shadingCentric false means that the light is to be selected
first. The shading groups associated with the light will then be selected
and subsequent selections will result in assignments being made.




Example:
---
import maya.cmds as cmds

cmds.shadingLightRelCtx()

---
Return:
---


    string: Name of the context created.

Flags:
---


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
offCommand(ofc): string
    properties: create, query, edit
    command to be issued when context is turned on

---
onCommand(onc): string
    properties: create, query, edit
    command to be issued when context is turned on

---
shadingCentric(s): boolean
    properties: create, query, edit
    shading-centric mode.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shadingLightRelCtx.html 
    """


def shadingNetworkCompare(flagbyName: boolean, flagbyValue: boolean, flagdelete: boolean, flagequivalent: boolean, flagnetwork1: boolean, flagnetwork2: boolean, flagupstreamOnly: boolean) -> string[] | string | int:
    """Synopsis:
---
---
 shadingNetworkCompare([byName=boolean], [byValue=boolean], [delete=boolean], [equivalent=boolean], [network1=boolean], [network2=boolean], [upstreamOnly=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shadingNetworkCompare is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.shadingNetworkCompare( 'blinn1SG', 'blinn2SG' )
Result: shadingNetworkComparison1

cmds.shadingNetworkCompare( 'shadingNetworkComparison1', query=True, equivalent=True )
Result: 1

cmds.shadingNetworkCompare( 'shadingNetworkComparison1', query=True, network1=True )
Result: blinn1SG blinn1

cmds.shadingNetworkCompare( 'shadingNetworkComparison1', delete=True )

---
Return:
---


    string[]|string|int: Command result

Flags:
---


---
byName(nam): boolean
    properties: create
    Indicates whether the comparison should consider node names.
If true, two shading networks will be considered equivalent only
if the names of corresponding nodes are the same, ignoring namespaces.
If false, two shading networks will be considered equivalent even
if corresponding nodes are named differently.
Default is 'false'.

---
byValue(val): boolean
    properties: create
    Indicates whether the comparison should consider the values of
unconnected attributes.
If true, two shading networks will be considered equivalent only
if corresponding, unconnected attributes are the same type and have the
same value. Only attributes of type 'int', 'bool', 'float', and 'string'
will have their values compared.
If false, two shading networks will be considered equivalent even
if corresponding, unconnected attributes have different values or
are different types.
Default is 'true'.

---
delete(delete): boolean
    properties: create
    Deletes the specified comparison from memory.

---
equivalent(eq): boolean
    properties: query
    Returns an int. 1 if the shading networks in the specified comparison are
equivalent. 0 otherwise.

---
network1(n1): boolean
    properties: query
    Returns a string[]. Returns an empty string array if the shading networks
in the specified comparison are not equivalent. Otherwise returns the nodes
in the first shading network.

---
network2(n2): boolean
    properties: query
    Returns a string[]. Returns an empty string array if the shading networks
in the specified comparison are not equivalent. Otherwise returns the nodes
in the second shading network.

---
upstreamOnly(up): boolean
    properties: create
    Indicates whether the comparison should consider nodes which are
connected downstream from shading network nodes.
If true, only those nodes which are upstream from the shading
group will be considered. If, following only downstream connections,
there is no connection path from a node to one of the shader attributes on the
shading group, the node will not be considered.
If false, a node will be considered if a connection path can found, following
either upstream or downstream connections, which terminates with an input
connection to one of the shading groups shader attributes. These dangling nodes
do not directly contribute to the color, displacement, or volume
characteristics of the shading group.
Default is 'false'.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shadingNetworkCompare.html 
    """


def shadingNode(flagasLight: boolean, flagasPostProcess: boolean, flagasRendering: boolean, flagasShader: boolean, flagasTexture: boolean, flagasUtility: boolean, flagisColorManaged: boolean, flagname: string, flagparent: string, flagshared: boolean, flagskipSelect: boolean) -> string:
    """Synopsis:
---
---
 shadingNode(
node
string
    , [asLight=boolean], [asPostProcess=boolean], [asRendering=boolean], [asShader=boolean], [asTexture=boolean], [asUtility=boolean], [isColorManaged=boolean], [name=string], [parent=string], [shared=boolean], [skipSelect=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shadingNode is undoable, NOT queryable, and NOT editable.
The shadingNode command classifies any DG node as a shader, texture
light, post process, or utility so that it can be properly organized
in the multi-lister.  Recall that any DG node can be used a part of a
a shader, texture or light - regardless of how it is classified by this.
command. These classifications are provided for convenience in the UI.




Example:
---
import maya.cmds as cmds

cmds.createNode( 'transform', n='transform1' )
cmds.createNode( 'nurbsSurface', n='surface1', p='transform1' )
cmds.createNode( 'camera', shared=True, n='top' )

This transform will be selected when created
cmds.createNode( 'transform', n='selectedTransform' )

This will create a new transform node, but 'selectedTransform'
will still be selected.
cmds.createNode( 'transform', ss=True )

Create node under new namespace
cmds.createNode( 'transform', n='newNS:transform1' )

myShader = cmds.shadingNode('anisotropic', asShader=True)

---
Return:
---


    string: The name of the new node.
    string: (the name of the new node)

Flags:
---


---
asLight(al): boolean
    properties: create
    classify the current DG node as a light

---
asPostProcess(app): boolean
    properties: create
    classify the current DG node as a post process

---
asRendering(ar): boolean
    properties: create
    classify the current DG node as a rendering node

---
asShader(asShader): boolean
    properties: create
    classify the current DG node as a shader

---
asTexture(at): boolean
    properties: create
    classify the current DG node as a texture

---
asUtility(au): boolean
    properties: create
    classify the current DG node as a utility

---
isColorManaged(icm): boolean
    properties: create
    classify the current DG node as being color managed

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace doesn't exist, we
will create the namespace.

---
parent(p): string
    properties: create
    Specifies the parent in the DAG under which the new node belongs.

---
shared(s): boolean
    properties: create
    This node is shared across multiple files, so only create it if
it does not already exist.

---
skipSelect(ss): boolean
    properties: create
    This node is not to be selected after creation, the original selection
will be preserved.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shadingNode.html 
    """


def shapeCompare() -> int:
    """Synopsis:
---
---
 shapeCompare(
[object object]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shapeCompare is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.polySphere()
cmds.polySphere()
cmds.select( cl=True )
cmds.select( 'pSphere1', 'pSphere2', r=True )
cmds.shapeCompare()

---
Return:
---


    int: 0 if successful, 1 if both shapes are not determined to be equal
based on requested flags.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shapeCompare.html 
    """


def shapeEditor(flagclearSelection: boolean, flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaghighlightConnection: string, flaglockMainConnection: boolean, flaglowestSelection: boolean, flagmainListConnection: string, flagpanel: string, flagparent: string, flagselectionConnection: string, flagstateString: boolean, flagtargetControlList: boolean, flagtargetList: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string, flagverticalSliders: boolean) -> string:
    """Synopsis:
---
---
 shapeEditor(
string
    , [clearSelection=boolean], [control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightConnection=string], [lockMainConnection=boolean], [lowestSelection=boolean], [mainListConnection=string], [panel=string], [parent=string], [selectionConnection=string], [stateString=boolean], [targetControlList=boolean], [targetList=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string], [verticalSliders=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shapeEditor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.shapeEditor( 'shapeEd' )

---
Return:
---


    string: The name of the editor

Flags:
---


---
clearSelection(cs): boolean
    properties: edit
    Clear the shape editor selection.

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
filter(f): string
    properties: create, query, edit
    Specifies the name of an itemFilter object to be used with this editor.
This filters the information coming onto the main list
of the editor.

---
forceMainConnection(fmc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will only
display items contained in the selectionConnection object. This is
a variant of the -mainListConnection flag in that it will force a
change even when the connection is locked. This flag is used to
reduce the overhead when using the -unlockMainConnection
, -mainListConnection, -lockMainConnection flags in immediate
succession.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
lowestSelection(ls): boolean
    properties: query
    Query the lowest selection item.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
panel(pnl): string
    properties: create, query
    Specifies the panel for this editor. By default if
an editor is created in the create callback of a scripted panel it
will belong to that panel. If an editor does not belong to a panel
it will be deleted when the window that it is in is deleted.

---
parent(p): string
    properties: create, query, edit
    Specifies the parent layout for this editor. This flag will only
have an effect if the editor is currently un-parented.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
targetControlList(tcl): boolean
    properties: query
    Query the target control list.

---
targetList(tl): boolean
    properties: query
    Query the target list.

---
unParent(up): boolean
    properties: create, edit
    Specifies that the editor should be removed from its layout.
This cannot be used in query mode.

---
unlockMainConnection(ulk): boolean
    properties: create, edit
    Unlocks the mainConnection, effectively restoring the original
mainConnection (if it is still available), and dynamic updates.

---
updateMainConnection(upd): boolean
    properties: create, edit
    Causes a locked mainConnection to be updated from the orginal
mainConnection, but preserves the lock state.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
verticalSliders(vs): boolean
    properties: create, query, edit
    Should the sliders be vertical?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shapeEditor.html 
    """


def shapePanel(flagcontrol: boolean, flagcopy: string, flagcreateString: boolean, flagdefineTemplate: string, flagdocTag: string, flageditString: boolean, flagexists: boolean, flaginit: boolean, flagisUnique: boolean, flaglabel: string, flagmenuBarRepeatLast: boolean, flagmenuBarVisible: boolean, flagneedsInit: boolean, flagparent: string, flagpopupMenuProcedure: script, flagreplacePanel: string, flagshapeEditor: boolean, flagtearOff: boolean, flagtearOffCopy: string, flagtearOffRestore: boolean, flagunParent: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 shapePanel(
string
    , [control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [shapeEditor=boolean], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shapePanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.shapePanel( 'bsP' )

---
Return:
---


    string: The name of the panel

Flags:
---


---
control(ctl): boolean
    properties: query
    Returns the top level control for this panel.
Usually used for getting a parent to attach popup menus.
CAUTION: panels may not have controls at times.  This
flag can return "" if no control is present.

---
copy(cp): string
    properties: edit
    Makes this panel a copy of the specified panel.  Both
panels must be of the same type.

---
createString(cs): boolean
    properties: edit
    Command string used to create a panel

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the Maya panel.

---
editString(es): boolean
    properties: edit
    Command string used to edit a panel

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
init(init): boolean
    properties: create, edit
    Initializes the panel's default state.  This is usually done
automatically on file -new and file -open.

---
isUnique(iu): boolean
    properties: query
    Returns true if only one instance of this panel type is allowed.

---
label(l): string
    properties: query, edit
    Specifies the user readable label for the panel.

---
menuBarRepeatLast(mrl): boolean
    properties: create, query, edit
    Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.

---
menuBarVisible(mbv): boolean
    properties: create, query, edit
    Controls whether the menu bar for the panel is displayed.

---
needsInit(ni): boolean
    properties: query, edit
    (Internal) On Edit will mark the panel as requiring initialization.
Query will return whether the panel is marked for initialization.  Used
during file -new and file -open.

---
parent(p): string
    properties: create
    Specifies the parent layout for this panel.

---
popupMenuProcedure(pmp): script
    properties: query, edit
    Specifies the procedure called for building the panel's popup menu(s).
The default value is "buildPanelPopupMenu".  The procedure should take
one string argument which is the panel's name.

---
replacePanel(rp): string
    properties: edit
    Will replace the specified panel with this panel.  If the
target panel is within the same layout it will perform a swap.

---
shapeEditor(se): boolean
    properties: query
    Query only flag that returns the name of an editor to be associated with the panel.

---
tearOff(to): boolean
    properties: query, edit
    Will tear off this panel into a separate window with a paneLayout
as the parent of the panel. When queried this flag will return if the
panel has been torn off into its own window.

---
tearOffCopy(toc): string
    properties: create
    Will create this panel as a torn of copy of the specified source panel.

---
tearOffRestore(tor): boolean
    properties: create, edit
    Restores panel if it is torn off and focus is given to it.
If docked, becomes the active panel in the docked window.
This should be the default flag that is added to all panels
instead of -to/-tearOff flag which should only be used to tear off the panel.

---
unParent(up): boolean
    properties: edit
    Specifies that the panel should be removed from its layout.
This (obviously) cannot be used with query.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shapePanel.html 
    """


def shelfButton(flagalign: string, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcommand: script, flagcommandRepeatable: boolean, flagdefineTemplate: string, flagdisabledImage: string, flagdocTag: string, flagdoubleClickCommand: script, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableCommandRepeat: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagflat: boolean, flagflexibleWidthType: int, flagflexibleWidthValue: int, flagflipX: boolean, flagflipY: boolean, flagfont: string, flagfullPathName: boolean, flaghandleNodeDropCallback: script, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghighlightImage: string, flagimage: string, flagimage1: string, flagimage2: string, flagimage3: string, flagimageOverlayLabel: string, flagisObscured: boolean, flaglabel: string, flaglabelEditingCallback: script, flaglabelOffset: int, flagmanage: boolean, flagmarginHeight: uint, flagmarginWidth: uint, flagmenuItem: tuple[string, string], flagmenuItemPython: int, flagmenuItemWithOptionBox: tuple[string, string, string], flagnoBackground: boolean, flagnoDefaultPopup: boolean, flagnumberOfPopupMenus: boolean, flagoverlayLabelBackColor: tuple[float, float, float, float], flagoverlayLabelColor: tuple[float, float, float], flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrotation: float, flagscaleIcon: boolean, flagselectionImage: string, flagsourceType: string, flagstatusBarMessage: string, flagstyle: string, flaguseAlpha: boolean, flaguseTemplate: string, flagversion: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 shelfButton(
[string]
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [command=script], [commandRepeatable=boolean], [defineTemplate=string], [disabledImage=string], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableCommandRepeat=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [flat=boolean], [flexibleWidthType=int], [flexibleWidthValue=int], [flipX=boolean], [flipY=boolean], [font=string], [fullPathName=boolean], [handleNodeDropCallback=script], [height=int], [highlightColor=[float, float, float]], [highlightImage=string], [image=string], [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string], [labelEditingCallback=script], [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint], [menuItem=[string, string]], [menuItemPython=int], [menuItemWithOptionBox=[string, string, string]], [noBackground=boolean], [noDefaultPopup=boolean], [numberOfPopupMenus=boolean], [overlayLabelBackColor=[float, float, float, float]], [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rotation=float], [scaleIcon=boolean], [selectionImage=string], [sourceType=string], [statusBarMessage=string], [style=string], [useAlpha=boolean], [useTemplate=string], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shelfButton is undoable, queryable, and editable.
This command creates an iconTextButton that is designed to be on
the shelf. The button contains a command that can be drag'n'dropped.




Example:
---
import maya.cmds as cmds

   Create a window with a shelf in it.  You can add more items to
   this shelf by creating more 'shelfButton' objects or by dragging
   other shelf items to the window.  Similarly, you can delete the
   shelf items with the 'deleteUI' command or by dragging the items
   to the trash can located on the main Maya window shelf.
---

window = cmds.window( title = 'shelfButton Example')
tabs = cmds.tabLayout()
shelf = cmds.shelfLayout()

   Create some shelf buttons...
---

   1.  A button that prints a message to the Command Line.
---

cmds.shelfButton( annotation='Print "Hello".', image1='commandButton.png', command='print "Hello\\n"' )

   2.  A button that will create a sphere.
---

cmds.shelfButton( annotation='Create a sphere.', image1='sphere.png', command='cmds.sphere()' )

   3.  A button that will open the Attribute Editor window.
---

cmds.shelfButton(annotation='Show the Attribute Editor.', image1='menuIconWindow.png', command='import maya.mel; maya.mel.eval("openAEWindow")' )

   4.  A button with a label that will create a cone
---

cmds.shelfButton(annotation='Create a cone.', image1='cone.png', command='cmds.cone()', imageOverlayLabel='4th')

   5.  A button with a label and color that will call undo
---

cmds.shelfButton(annotation="Undo last operation.",
    image1="undo.png", command="undo", imageOverlayLabel="undo",
    overlayLabelColor=(1, .25, .25))

   6.  A button with a label, color and background that will call redo
---

cmds.shelfButton(annotation="Redo last operation.",
    image1="redo.png", command="redo", imageOverlayLabel="redo",
    overlayLabelColor=(1, 1, .25), overlayLabelBackColor=(.15, .9, .1, .4))

cmds.tabLayout( tabs, edit=True, tabLabel=(shelf, 'Example Shelf') )

cmds.showWindow( window )

---
Return:
---


    string: The full name of the button.

Flags:
---


---
align(al): string
    properties: create, query, edit
    The label alignment.  Alignment values are "left",
"right", and "center". By default, the label is aligned "center".
Currently only available when -st/style is set to "iconAndTextCentered".

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
command(c): script
    properties: create, query, edit
    Command executed when the control is pressed.

---
commandRepeatable(rpt): boolean
    properties: create, query, edit
    Set if the MEL command specified in the command flag should be repeatable
or not.  The "g" key, by default, is the shortcut to repeat the last executed command.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
disabledImage(di): string
    properties: create, query, edit
    Image used when the button is disabled. Image size must
be the same as the image specified with the i/image flag.
This is a Windows only flag.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
doubleClickCommand(dcc): script
    properties: create, query, edit
    Command executed when the control is double clicked.

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableCommandRepeat(ecr): boolean
    properties: create, query, edit
    This flag only affects menu items to which a command can be
attached.  Specify true and the command may be repeated by
executing the command repeatLast.  This flag is true by
default for all items except for option box items.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
flat(fla): boolean
    properties: create, query, edit
    Sets whether the control will be a flat button (0 false, 1 true).

---
flexibleWidthType(fwt): int
    properties: create, query, edit
    This flag is used to have the shelf button have a wider or thinner width.
The valid values are: Standard = 1, Custom = 2, Automatic = 3.
The Standard type will resize, keeping the aspect ratio, to 32x32 pixels.
The Automatic type will adjust the button width to make sure wide images are used properly.
The Custom type will allow the user to choose the desired width for the icon.
Default value is 3.

---
flexibleWidthValue(fwv): int
    properties: create, query, edit
    This flag is only useful when the Custom flexibleWidthType is chosen.
The value is a width in pixels.

---
flipX(fx): boolean
    properties: create, query, edit
    Is the image flipped horizontally?

---
flipY(fy): boolean
    properties: create, query, edit
    Is the image flipped vertically?

---
font(fn): string
    properties: create, query, edit
    The font for the text.  Valid values are
"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
"smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
handleNodeDropCallback(hnd): script
    properties: create, edit
    Specify a script callback which is called when a node is dropped
on the control.  The name of the node being dropped will be
passed to the function  (python callable) or appended to the end
(script) to form the command to be executed.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
highlightImage(hi): string
    properties: create, query, edit
    Highlight image displayed while the cursor is over the
control. Image size must be the same as the image specified with
the -i/image flag. This is a Windows only flag.

---
image(i): string
    properties: create, query, edit
    If you are not providing images with different sizes then you may
use this flag for the control's image. If the "iconOnly" style is
set, the icon will be scaled to the size of the control.

---
image1(i1): string
    properties: create, query, edit
    First of three possible icons. The icon that best fits the
current size of the control will be displayed.

---
image2(i2): string
    properties: create, query, edit
    Second of three possible icons. The icon that best fits the
current size of the control will be displayed.

---
image3(i3): string
    properties: create, query, edit
    Third of three possible icons. The icon that best fits the
current size of the control will be displayed.

---
imageOverlayLabel(iol): string
    properties: create, query, edit
    A short string, up to 6 characters, representing a label that will be displayed
on top of the image.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
label(l): string
    properties: create, query, edit
    The text that appears in the control.

---
labelEditingCallback(lec): script
    properties: create, edit
    Specify a callback which is called after the user
double clicks the label of the control to give it a new label.
The new label string will be passed to the callback.

---
labelOffset(lo): int
    properties: create, query, edit
    The label offset. Default is 0. Currently only available
when -st/style is set to "iconAndTextCentered".

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
marginHeight(mh): uint
    properties: create, query, edit
    The number of pixels above and below the control content.
The default value is 1 pixel.

---
marginWidth(mw): uint
    properties: create, query, edit
    The number of pixels on either side of the control content.
The default value is 1 pixel.

---
menuItem(mi): [string, string]
    properties: create, edit, multiuse
    Creates menu items for this button by passing in arguments for the menu item label and
command for each item.  These should be passed as strings: "label" "command" for each use
of this flag in the command.

---
menuItemPython(mip): int
    properties: create, edit, multiuse
    This flag is used to specify that a menu item is in Python. The integer value is
the index of the menuItem that is modified by this flag. This is 0 based, so it
corresponds to the (index+1)th occurrence of the /-mi/-menuItem flag.

---
menuItemWithOptionBox(mio): [string, string, string]
    properties: create, edit, multiuse
    Creates menu items that include an option box.  Arguments passed to the flag are "label"
"comand" "option box command";

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
noDefaultPopup(ndp): boolean
    properties: create
    Disable the default popup menus.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
overlayLabelBackColor(olb): [float, float, float, float]
    properties: create, query, edit
    The RGBA color of the shadow behind the label defined by
imageOverlayLabel. Default is 50% transparent black: 0 0 0 .5

---
overlayLabelColor(olc): [float, float, float]
    properties: create, query, edit
    The RGB color of the label defined by imageOverlayLabel. Default is a
light grey: .8 .8 .8

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
rotation(rot): float
    properties: create, query, edit
    The rotation value of the image in radians.

---
scaleIcon(sic): boolean
    properties: create, edit
    For "textOnly" and "iconOnly" style, this flag has no effect.
For other styles, if the flag is specified, the icon will be scaled to the size of the control.

---
selectionImage(si): string
    properties: create, query, edit
    Image displayed while the control is selected. Image size
must be the same as the image specified with the -i/image
flag. This is a Windows only flag.

---
sourceType(stp): string
    properties: create, query, edit
    Sets the language type for the command script. Can only be used in
conjunction with the c/command or dcc/doubleClickCommand flags.
Valid values are "mel" (enabled by default), and "python".

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
style(st): string
    properties: create, query, edit
    The draw style of the control.  Valid styles are "iconOnly",
"textOnly", "iconAndTextHorizontal", "iconAndTextVertical", and
"iconAndTextCentered". (Note: "iconAndTextCentered" is only available on Windows).
If the "iconOnly" style is set, the icon will be scaled to the size of the control.

---
useAlpha(ua): boolean
    properties: create, query, edit
    Is the image using alpha channel?

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
version(ver): string
    properties: create, query, edit
    Specify the version that this control feature was introduced.
The argument should be given as a string of the version number
(e.g. "2013", "2014"). Currently only accepts major version
numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shelfButton.html 
    """


def shelfLayout(flagalignment: string, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcellHeight: int, flagcellWidth: int, flagcellWidthHeight: tuple[int, int], flagchildArray: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontal: boolean, flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagposition: tuple[string, int], flagpreventOverride: boolean, flagspacing: int, flagstatusBarMessage: string, flagstyle: string, flaguseTemplate: string, flagversion: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 shelfLayout(
[string]
    , [alignment=string], [annotation=string], [backgroundColor=[float, float, float]], [cellHeight=int], [cellWidth=int], [cellWidthHeight=[int, int]], [childArray=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [position=[string, int]], [preventOverride=boolean], [spacing=int], [statusBarMessage=string], [style=string], [useTemplate=string], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shelfLayout is undoable, queryable, and editable.addNewShelfTab



Example:
---
import maya.cmds as cmds

Create 4 shelves with 3 icons
cmds.window()
cmds.tabLayout()

sh1 = cmds.shelfLayout("First", style="iconOnly",
                                           backgroundColor=(.9, .2, .2))
sh1b1 = cmds.shelfButton(image1="textureEditor.png",
                                                 label="textureEditor", annotation="textureEditor",
                                                 command="TextureViewWindow",
                                                 imageOverlayLabel="1",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(1, .25, .25, .5))
sh1b2 = cmds.shelfButton(image1="undo.png",
                                                 label="undo", annotation="undo",
                                                 command="undo",
                                                 imageOverlayLabel="1",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(1, .25, .25, .5))
sh1b3 = cmds.shelfButton(image1="redo.png",
                                                 label="redo", annotation="redo",
                                                 command="redo",
                                                 imageOverlayLabel="1",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(1, .25, .25, .5))
cmds.setParent('..')

sh2 = cmds.shelfLayout("Second", style="textOnly",
                                           backgroundColor=(.2, .9, .2))
sh2b1 = cmds.shelfButton(image1="textureEditor.png",
                                                 label="textureEditor", annotation="textureEditor",
                                                 command="TextureViewWindow",
                                                 imageOverlayLabel="2",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, 1, .25, .5))
sh2b2 = cmds.shelfButton(image1="undo.png",
                                                 label="undo", annotation="undo",
                                                 command="undo",
                                                 imageOverlayLabel="2",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, 1, .25, .5))
sh2b3 = cmds.shelfButton(image1="redo.png",
                                                 label="redo", annotation="redo",
                                                 command="redo",
                                                 imageOverlayLabel="2",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, 1, .25, .5))
cmds.setParent('..')

sh3 = cmds.shelfLayout("Third", style="iconAndTextHorizontal",
                                           backgroundColor=(.2, .2, .9))
sh3b1 = cmds.shelfButton(image1="textureEditor.png",
                                                 label="textureEditor", annotation="textureEditor",
                                                 command="TextureViewWindow",
                                                 imageOverlayLabel="3",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, .25, 1, .5))
sh3b2 = cmds.shelfButton(image1="undo.png",
                                                 label="undo", annotation="undo",
                                                 command="undo",
                                                 imageOverlayLabel="3",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, .25, 1, .5))
sh3b3 = cmds.shelfButton(image1="redo.png",
                                                 label="redo", annotation="redo",
                                                 command="redo",
                                                 imageOverlayLabel="3",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, .25, 1, .5))
cmds.setParent('..')


sh4 = cmds.shelfLayout("Fourth", style="iconAndTextVertical")
sh4b1 = cmds.shelfButton(image1="textureEditor.png",
                                                 label="textureEditor", annotation="textureEditor",
                                                 command="TextureViewWindow",
                                                 imageOverlayLabel="4",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, 1, 1, .5))
sh4b2 = cmds.shelfButton(image1="undo.png",
                                                 label="undo", annotation="undo",
                                                 command="undo",
                                                 imageOverlayLabel="4",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, 1, 1, .5))
sh4b3 = cmds.shelfButton(image1="redo.png",
                                                 label="redo", annotation="redo",
                                                 command="redo",
                                                 imageOverlayLabel="4",
                                                 overlayLabelColor=(.1, .1, .1),
                                                 overlayLabelBackColor=(.25, 1, 1, .5))
cmds.setParent('..')

cmds.setParent('..')
cmds.showWindow()

Move some icons around

Move undo to the first position in shelf 1
cmds.shelfLayout(sh1, edit=True, position=(sh1b2, 1))

This does nothing
cmds.shelfLayout(sh2, edit=True, position=(sh2b2, 2))

Move undo to the last position in shelf 3
cmds.shelfLayout(sh3, edit=True, position=(sh3b2, 3))

Swap textureEditor and redo in shelf 4
cmds.shelfLayout(sh4, edit=True, position=[(sh4b1, 3), (sh4b3, 1)])

---
Return:
---


    string: The name of the layout.

Flags:
---


---
alignment(aln): string
    properties: create, query, edit
    Sets the alignment of the buttons in the layout.
When horizontal is true, valid options are "left" and "right".
When horizontal is false, valid options are "top" and "bottom".

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
cellHeight(ch): int
    properties: create, query, edit
    Set or query the height of the items in the shelf.

---
cellWidth(cw): int
    properties: create, query, edit
    Set or query the width of the items in the shelf.

---
cellWidthHeight(cwh): [int, int]
    properties: create, query, edit
    Set the width and height of the items in the shelf.

---
childArray(ca): boolean
    properties: query
    Returns a string array of the names of the layout's
immediate children.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
generalSpacing(gsp) 2024: int
    properties: edit
    Sets the spacing for this layout.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
horizontal(hr): boolean
    properties: create, query, edit
    Orientation of the layout. This flag is true by default, which corresponds to a horizontally laid out shelf.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
margins(mar) 2024: int
    properties: edit
    Sets the content margins for this layout.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfChildren(nch): boolean
    properties: query
    Returns in an int the number of immediate children of the layout.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
position(pos): [string, int]
    properties: create, edit, multiuse
    Specify the name of a child control in the grid layout along with
a 1-based integer value indicating the desired
position of the child. Positions increase from left to right
within a row and then wrap around to the next row increasing from
top to bottom. For example, a grid layout with 3 columns and 2
rows has 6 visible positions where 1, 2 and 3 occupy the first row
and 4, 5 and 6 occupy the second.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
spacing(spa): int
    properties: create, query, edit
    Sets the space between children.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
style(st): string
    properties: create, query, edit
    Set or query the current style of the items in the shelf.  Valid
styles are "iconOnly", "textOnly", "iconAndTextHorizontal"
and "iconAndTextVertical".

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
version(ver): string
    properties: create, query, edit
    Specify the version that this feature was introduced.
The argument should be given as a string of the version number
(e.g. "2014", "2015"). Currently only accepts major version
numbers (e.g. 2014.5 should be given as "2014").

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shelfLayout.html 
    """


def shelfTabLayout(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagborderStyle: string, flagchangeCommand: script, flagchildArray: boolean, flagchildResizable: boolean, flagcloseTab: int, flagcloseTabCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdoubleClickCommand: script, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontalScrollBarThickness: int, flagimage: string, flagimageVisible: boolean, flaginnerMarginHeight: int, flaginnerMarginWidth: int, flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagminChildWidth: int, flagmoveTab: tuple[int, int], flagnewTabCommand: script, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpostMenuCommand: script, flagpreSelectCommand: script, flagpreventOverride: boolean, flagscrollable: boolean, flagscrollableTabs: boolean, flagselectCommand: script, flagselectTab: string, flagselectTabIndex: int, flagshowNewTab: boolean, flagstatusBarMessage: string, flagtabIcon: tuple[string, string], flagtabIconIndex: tuple[int, string], flagtabLabel: tuple[string, string], flagtabLabelIndex: tuple[int, string], flagtabPosition: string, flagtabTooltip: tuple[string, string], flagtabTooltipIndex: tuple[int, string], flagtabsClosable: boolean, flagtabsVisible: boolean, flaguseTemplate: string, flagverticalScrollBarThickness: int, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 shelfTabLayout(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [borderStyle=string], [changeCommand=script], [childArray=boolean], [childResizable=boolean], [closeTab=int], [closeTabCommand=script], [defineTemplate=string], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [horizontalScrollBarThickness=int], [image=string], [imageVisible=boolean], [innerMarginHeight=int], [innerMarginWidth=int], [isObscured=boolean], [manage=boolean], [margins=int], [minChildWidth=int], [moveTab=[int, int]], [newTabCommand=script], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [postMenuCommand=script], [preSelectCommand=script], [preventOverride=boolean], [scrollable=boolean], [scrollableTabs=boolean], [selectCommand=script], [selectTab=string], [selectTabIndex=int], [showNewTab=boolean], [statusBarMessage=string], [tabIcon=[string, string]], [tabIconIndex=[int, string]], [tabLabel=[string, string]], [tabLabelIndex=[int, string]], [tabPosition=string], [tabTooltip=[string, string]], [tabTooltipIndex=[int, string]], [tabsClosable=boolean], [tabsVisible=boolean], [useTemplate=string], [verticalScrollBarThickness=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shelfTabLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.shelfTabLayout( 'mainShelfTab', image='smallTrash.png', imageVisible=True )
cmds.shelfLayout( 'Dynamics' )
cmds.setParent( '..' )
cmds.shelfLayout( 'Rendering' )
cmds.setParent( '..' )
cmds.shelfLayout( 'Animation' )
cmds.setParent( '..' )
cmds.showWindow()

---
Return:
---


    string: The name of the shelfTabLayout.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
borderStyle(bs): string
    properties: create, query, edit
    Specify the style of the border for tab layout. Valid values are:
"none", "top", "notop" and "full". By default, it will use "full" to draw a simple frame
around the body area of the tab layout.

"none"  - Do not draw borders around the body area of the tab layout
"top"   - Only draw a simple line right below the tabs
"notop" - Draw a simple frame on the left/right/bottom (no top) of the tab layout
"full"  - Draw a simple frame around the body area of the tab layout

---
changeCommand(cc): script
    properties: create, edit
    Command executed when a tab is selected interactively.
This command is only invoked when the selected tab changes.
Re-selecting the current tab will not invoke this command.

---
childArray(ca): boolean
    properties: query
    Returns a string array of the names of the layout's
immediate children.

---
childResizable(cr): boolean
    properties: create, query
    Set to true if you want the child of the control layout to be
as wide as the scroll area.  You may also indicate a minimum
width for the child using the -mcw/minChildWidth flag.

---
closeTab(ct): int
    properties: create, edit
    Close the tab at the given index.

---
closeTabCommand(ctc): script
    properties: create, edit
    Specify a script to be executed when one of the tabs are closed by clicking on the
header widget (MMB or X button).

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
doubleClickCommand(dcc): script
    properties: create, edit
    Command executed when a tab is double clicked on.  Note
that the first click will select the tab and the second click
will execute the double click command.  Double clicking the
current tab will re-invoke the double click command.

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
generalSpacing(gsp) 2024: int
    properties: edit
    Sets the spacing for this layout.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
horizontalScrollBarThickness(hst): int
    properties: create, edit
    Thickness of the horizontal scroll bar.  Specify an
integer value greater than or equal to zero. This flag has
no effect on Windows systems.

---
image(i): string
    properties: create, query, edit
    Image appearing in top right corner of tab layout.

---
imageVisible(iv): boolean
    properties: create, query, edit
    Visibility of tab image.

---
innerMarginHeight(imh): int
    properties: create, query
    Margin height for all tab children.

---
innerMarginWidth(imw): int
    properties: create, query
    Margin width for all tab children.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
margins(mar) 2024: int
    properties: edit
    Sets the content margins for this layout.

---
minChildWidth(mcw): int
    properties: create, query
    Specify a positive non-zero integer value indicating the
minimum width the tab layout's children.  This flag only has
meaning when the -cr/childResizable flag is set to true.

---
moveTab(mt): [int, int]
    properties: create, edit
    Move the tab from the current index to a new index.

---
newTabCommand(ntc): script
    properties: create, edit
    Command executed when the 'New Tab' button (on the tab bar)
is clicked.  Note: in order to show the new tab button use
the -snt/showNewTab flag.  Using this command will
override any internal Maya logic for adding a new tab (only
this command will be executed).

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfChildren(nch): boolean
    properties: query
    Returns in an int the number of immediate children of the layout.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
postMenuCommand(pmc): script
    properties: create, edit
    Specify a script to be executed when the popup menu is about to be shown.

---
preSelectCommand(psc): script
    properties: create, edit
    Command executed when a tab is selected but before it's
contents become visible.  Re-selecting the current tab will not
invoke this command.  Note that this command is not executed by
using either of the -st/selectTab
or -sti/selectTabIndex flags.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
scrollable(scr): boolean
    properties: create, query
    Puts all children of this layout within a scroll area.

---
scrollableTabs(stb): boolean
    properties: create, query, edit
    If true, the active tab in the layout can be scrolled through with the mouse wheel.
Default is true.

---
selectCommand(sc): script
    properties: create, query, edit
    Command executed when a tab is selected interactively  This
command will be invoked whenever a tab is selected, ie.
re-selecting the current tab will invoke this command.  Note that
this command is not executed by using either of
the -st/selectTab or -sti/selectTabIndex flags.

---
selectTab(st): string
    properties: create, query, edit
    The name, in short form, of the selected tab.  An empty
string is returned on query if there are no child tabs.

---
selectTabIndex(sti): int
    properties: create, query, edit
    Identical to the -st/selectTab flag except this
flag takes a 1-based index to identify the selected tab.  A value of
0 is returned on query if there are no child tabs.

---
showNewTab(snt): boolean
    properties: create, query, edit
    Set to true if you want to have a 'New Tab' button shown at the end of
the tab bar.  Note: use the -ntc/newTabCommand flag to set the command
executed when this button is clicked.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
tabIcon(ti): [string, string]
    properties: create, query, edit, multiuse
    Set an icon for a tab.  The first argument is the name of a
control that must be a child of the tab layout.  The second
argument is the icon file name.

---
tabIconIndex(tii): [int, string]
    properties: create, query, edit, multiuse
    Identical to the -ti/tabIcon flag except this
flag takes a 1-based index to identify the tab you want to set the
icon for. If this flag is queried the tab icons for all the
children are returned.

---
tabLabel(tl): [string, string]
    properties: create, query, edit, multiuse
    Set a tab label.  The first argument is the name of a
control that must be a child of the tab layout.  The second
argument is the label for the tab associated with that child.
If this flag is queried then the tab labels for all the children
are returned.

---
tabLabelIndex(tli): [int, string]
    properties: create, query, edit, multiuse
    Identical to the -tl/tabLabel flag except this
flag takes a 1-based index to identify the tab you want to set the
label for. If this flag is queried the tab labels for all the
children are returned.

---
tabPosition(tp): string
    properties: create, query, edit
    Changes the tab position. The possible values are: "north", "east" and "west".

---
tabTooltip(tt): [string, string]
    properties: create, query, edit, multiuse
    Set a tab tooltip.  The first argument is the name of a
control that must be a child of the tab layout.  The second
argument is the tooltip for the tab associated with that child.
If this flag is queried then the tab tooltips for all the children
are returned.

---
tabTooltipIndex(tti): [int, string]
    properties: create, query, edit, multiuse
    Identical to the -tt/tabTooltip flag except this
flag takes a 1-based index to identify the tab you want to set the
tooltip for. If this flag is queried the tab tooltips for all the
children are returned.

---
tabsClosable(tc): boolean
    properties: create, query
    Set to true if you want to have a close button icon on all created tabs.

---
tabsVisible(tv): boolean
    properties: create, query, edit
    Visibility of the tab labels.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
verticalScrollBarThickness(vst): int
    properties: create, edit
    Thickness of the vertical scroll bar.  Specify an
integer value greater than or equal to zero. This flag has
no effect on Windows systems.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shelfTabLayout.html 
    """


def shot(flagaudio: string, flagclip: string, flagclipDuration: time, flagclipOpacity: float, flagclipSyncState: boolean, flagclipZeroOffset: time, flagcopy: boolean, flagcreateCustomAnim: boolean, flagcurrentCamera: string, flagcustomAnim: boolean, flagdeleteCustomAnim: boolean, flagdetermineTrack: boolean, flagendTime: time, flagfavorite: boolean, flagflag1: boolean, flagflag10: boolean, flagflag11: boolean, flagflag12: boolean, flagflag2: boolean, flagflag3: boolean, flagflag4: boolean, flagflag5: boolean, flagflag6: boolean, flagflag7: boolean, flagflag8: boolean, flagflag9: boolean, flaghasCameraSet: boolean, flaghasStereoCamera: boolean, flagimagePlaneVisibility: boolean, flaglinkAudio: string, flaglock: boolean, flagmute: boolean, flagpaste: boolean, flagpasteInstance: boolean, flagpostHoldTime: time, flagpreHoldTime: time, flagscale: float, flagselfmute: boolean, flagsequenceDuration: time, flagsequenceEndTime: time, flagsequenceStartTime: time, flagshotName: string, flagsourceDuration: time, flagstartTime: time, flagtrack: int, flagtransitionInLength: time, flagtransitionInType: int, flagtransitionOutLength: time, flagtransitionOutType: int, flagunlinkAudio: boolean) -> string:
    """Synopsis:
---
---
 shot([audio=string], [clip=string], [clipDuration=time], [clipOpacity=float], [clipSyncState=boolean], [clipZeroOffset=time], [copy=boolean], [createCustomAnim=boolean], [currentCamera=string], [customAnim=boolean], [deleteCustomAnim=boolean], [determineTrack=boolean], [endTime=time], [favorite=boolean], [flag1=boolean], [flag10=boolean], [flag11=boolean], [flag12=boolean], [flag2=boolean], [flag3=boolean], [flag4=boolean], [flag5=boolean], [flag6=boolean], [flag7=boolean], [flag8=boolean], [flag9=boolean], [hasCameraSet=boolean], [hasStereoCamera=boolean], [imagePlaneVisibility=boolean], [linkAudio=string], [lock=boolean], [mute=boolean], [paste=boolean], [pasteInstance=boolean], [postHoldTime=time], [preHoldTime=time], [scale=float], [selfmute=boolean], [sequenceDuration=time], [sequenceEndTime=time], [sequenceStartTime=time], [shotName=string], [sourceDuration=time], [startTime=time], [track=int], [transitionInLength=time], [transitionInType=int], [transitionOutLength=time], [transitionOutType=int], [unlinkAudio=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shot is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

myShot = cmds.shot('myShot', st=10, et=19);
cmds.shot(myShot, e=True, sst=100, set=119);

cmds.shot(myShot, q=True, st=True);
Result: 10.0 ---


cmds.shot(myShot, q=True, sst=True);
Result: 100.0 ---


cmds.shot(myShot, e=True, pst=10);
cmds.shot(myShot, q=True, set=True);
Result: 119.0 ---


cmds.shot(myShot, e=True, prt=5);
cmds.shot(myShot, q=True, set=True);
Result: 124.0 ---


cmds.shot(myShot, q=True, sd=True);
Result: 25.0 ---


---
Return:
---


    string: Shot name

Flags:
---


---
audio(aud): string
    properties: create, query, edit
    Specify the audio clip for this shot. Audio can be linked to a shot to allow playback of specific sounds when that shot is being displayed in the Sequencer. Refer to the shot node's documentation for details on how audio is used by shots and the Sequencer.

---
clip(cl): string
    properties: create, query, edit
    The clip associated with this shot. This clip will be posted to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.

---
clipDuration(cd): time
    properties: create, query, edit
    Length of clip. This is used for the display of the clip indicator bar in the Sequencer.

---
clipOpacity(co): float
    properties: create, query, edit
    Opacity for the shot's clip, this value is assigned to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.

---
clipSyncState(css): boolean
    properties: create, query, edit
    The viewport synchronization status of the clip associated with this shot.
Return values are,
0 = no clip associated with this shot
1 = clip is fully in sync with viewport, and frames are 1:1 with sequencer
2 = clip is partially in sync with viewport, movie may be scaled to match sequencer
3 = clip not in sync with viewport (i.e. could have scale/time/camera differences)

---
clipZeroOffset(czo): time
    properties: create, query, edit
    Specify which time of the clip corresponds to the beginning of the shot. This is used to properly align splitted clips.

---
copy(c): boolean
    properties: create, query, edit
    This flag is used to copy a shot to the clipboard. In query mode, this flag allows you to query what, if anything, has been copied into the shot clipboard.

---
createCustomAnim(cca): boolean
    properties: edit
    Creates an animation layer and links the shot node's customAnim attr to the weight
attr of the animation layer

---
currentCamera(cc): string
    properties: create, query, edit
    The camera associated with this shot. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.

---
customAnim(ca): boolean
    properties: query
    Returns the name of the animation layer node linked to this shot node's customAnim attr

---
deleteCustomAnim(dca): boolean
    properties: edit
    Disconnects the animation layer from this shot's customAnim attr and deletes the
animation layer node

---
determineTrack(dt): boolean
    properties: query, edit
    Determines an available track for the shot. Returns a new track number or the
existing track number if the current track is available.

---
endTime(et): time
    properties: create, query, edit
    The shot end time in the Maya timeline. Changing the startTime will extend the duration of a shot.

---
favorite(fav): boolean
    properties: create, query, edit
    Make the shot a favorite. This is a UI indicator only to streamline navigation in the Sequencer panel

---
flag1(f1): boolean
    properties: create, query, edit
    User specified state flag 1/12 for this shot

---
flag10(f10): boolean
    properties: create, query, edit
    User specified state flag 10/12 for this shot

---
flag11(f11): boolean
    properties: create, query, edit
    User specified state flag 11/12 for this shot

---
flag12(f12): boolean
    properties: create, query, edit
    User specified state flag 12/12 for this shot

---
flag2(f2): boolean
    properties: create, query, edit
    User specified state flag 2/12 for this shot

---
flag3(f3): boolean
    properties: create, query, edit
    User specified state flag 3/12 for this shot

---
flag4(f4): boolean
    properties: create, query, edit
    User specified state flag 4/12 for this shot

---
flag5(f5): boolean
    properties: create, query, edit
    User specified state flag 5/12 for this shot

---
flag6(f6): boolean
    properties: create, query, edit
    User specified state flag 6/12 for this shot

---
flag7(f7): boolean
    properties: create, query, edit
    User specified state flag 7/12 for this shot

---
flag8(f8): boolean
    properties: create, query, edit
    User specified state flag 8/12 for this shot

---
flag9(f9): boolean
    properties: create, query, edit
    User specified state flag 9/12 for this shot

---
hasCameraSet(hcs): boolean
    properties: create, query, edit
    Returns true if the camera associated with this shot is a camera set.

---
hasStereoCamera(hsc): boolean
    properties: create, query, edit
    Returns true if the camera associated with this shot is a stereo camera.

---
imagePlaneVisibility(ipv): boolean
    properties: create, query, edit
    Visibility of the shot imageplane, this value is assigned to the currentCamera's imagePlane.

---
linkAudio(la): string
    properties: create, query, edit
    Specify an audio clip to link to this shot. Any currently linked audio will be unlinked.

---
lock(lck): boolean
    properties: create, query, edit
    Lock a specific shot. This is different than locking an entire track, which is done via the shotTrack command

---
mute(m): boolean
    properties: create, query, edit
    Mute a specific shot. This is different than muting an entire track, which is done via the shotTrack command. Querying this attribute will return true if the shot is muted due to its own mute, its shot being muted, or its shot being unsoloed. See flag "selfmute" to query only the shot's own state.

---
paste(p): boolean
    properties: create, query, edit
    This flag is used to paste a shot or shots from the clipboard to the sequence timeline. Shots are added to the clipboard using the c/copy flag.

---
pasteInstance(pi): boolean
    properties: create, query, edit
    This flag is used to paste an instance of a shot or shots from the clipboard to the sequence timeline. Unlike the p/paste flag, which duplicates the camera and image plane from the original source shot, the pi/pasteInstance flag shares the camera and image plane from the source shot. The audio node is duplicated.

---
postHoldTime(pst): time
    properties: create, query, edit
    Specify the time length to append to the shot in the sequence timeline. This repeats the last frame of the shot, in sequence time, over the specified duration.

---
preHoldTime(prt): time
    properties: create, query, edit
    Specify the time length to prepend to the shot in the sequence timeline. This repeats the first frame of the shot, in sequence time, over the specified duration.

---
scale(s): float
    properties: create, query, edit
    Specify an amount to scale the Maya frame range of the shot. This will affect the sequenceEndFrame, leaving the sequenceStartFrame unchanged.

---
selfmute(sm): boolean
    properties: create, query, edit
    Query if this individual shot's own mute state is set. This is different from the flag "mute", which will return true if this shot is muted due to the track being muted or another track being soloed. Editing this flag will set this shot's own mute status (identical behavior as the flag "mute").

---
sequenceDuration(sqd): time
    properties: query, edit
    Return the sequence duration of the shot, which will include the holds and scale. This flag can only be queried.

---
sequenceEndTime(set): time
    properties: create, query, edit
    The shot end in the sequence timeline. Changing the endTime of a shot will scale it in sequence time.

---
sequenceStartTime(sst): time
    properties: create, query, edit
    The shot start in the sequence timeline. Changing the startTime of a shot will shift it in sequence time.

---
shotName(sn): string
    properties: create, query, edit
    Specify a user-defined name for this shot. This allows the assignment of names that are not valid as node names within Maya. Whenever the shotName attribute is defined its value is used in the UI.

---
sourceDuration(sd): time
    properties: query, edit
    Return the number of source frames in the shot. This flag can only be queried.

---
startTime(st): time
    properties: create, query, edit
    The shot start time in the Maya timeline. Changing the startTime will extend the duration of a shot.

---
track(trk): int
    properties: query, edit
    Specify the track in which this shot resides.

---
transitionInLength(til): time
    properties: create, query, edit
    Length of the transtion into the shot.

---
transitionInType(tit): int
    properties: query, edit
    Specify the the type of transition for the transition into the shot.
0 = Fade
1 = Dissolve

---
transitionOutLength(tol): time
    properties: create, query, edit
    Length of the transtion out of the shot.

---
transitionOutType(tot): int
    properties: query, edit
    Specify the the type of transition for the transition out of the shot.
0 = Fade
1 = Dissolve

---
unlinkAudio(ula): boolean
    properties: query, edit
    COMMENT
Unlinks any currently linked audio.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shot.html 
    """


def shotRipple(flagdeleted: boolean, flagendDelta: time, flagendTime: time, flagstartDelta: time, flagstartTime: time) -> None:
    """Synopsis:
---
---
 shotRipple([deleted=boolean], [endDelta=time], [endTime=time], [startDelta=time], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shotRipple is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds



// A shot initially starting at sequence time 0 was edited to start 10 frames later.
// adjust the rest of the shots accordingly
cmds.shotRipple(shotName, startTime=0, startDelta=10)

// A shot initially ending at frame 10 was edited to start 5 frames earlier.
// adjust the rest of the shots accordingly
cmds.shotRipple(shotName, endTime=10, endDelta=-5)

// A shot starting at frame 10 and ending at frame 20 was just deleted
// adjust the rest of the shots accordingly (if necessary)
cmds.shotRipple(shotName, delete=1,startTime=10,endTime=20)

---


Flags:
---


---
deleted(d): boolean
    properties: create, query, edit
    Specify whether this ripple edit is due to a shot deletion

---
endDelta(ed): time
    properties: create, query, edit
    Specify the change in the end time in frames

---
endTime(et): time
    properties: create, query, edit
    Specify the initial shot end time in the sequence timeline.

---
startDelta(sd): time
    properties: create, query, edit
    Specify the change in the start time in frames

---
startTime(st): time
    properties: create, query, edit
    Specify the initial shot start time in the sequence timeline.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shotRipple.html 
    """


def shotTrack(flaginsertTrack: uint, flaglock: boolean, flagmute: boolean, flagnumTracks: uint, flagremoveEmptyTracks: boolean, flagremoveTrack: uint, flagselfmute: boolean, flagsolo: boolean, flagswapTracks: tuple[uint, uint], flagtitle: string, flagtrack: uint, flagunsolo: boolean) -> None:
    """Synopsis:
---
---
 shotTrack([insertTrack=uint], [lock=boolean], [mute=boolean], [numTracks=uint], [removeEmptyTracks=boolean], [removeTrack=uint], [selfmute=boolean], [solo=boolean], [swapTracks=[uint, uint]], [title=string], [track=uint], [unsolo=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

shotTrack is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


Create 3 sequencer tracks with appropriate names.
Note that sequencer tracks are 1-indexed.
---

cmds.file(f=True,new=True)
for i in xrange(1,4):
    cmds.shotTrack(insertTrack=i, title="Track %d"%i)

Add some shots to the tracks.
By default, shots get added to the active track,
which is currently track 1. If tracks overlap in sequence time
they will be put onto a different track.
---

cmds.shot("shot1", sequenceStartTime=10, startTime=20, endTime=39)
cmds.shot("shot2", sequenceStartTime=30, startTime=10, endTime=29)
cmds.shot("shot3", sequenceStartTime=50, startTime=60, endTime=79)

Use the shot command to move shots to different tracks
cmds.shot("shot1", e=True, track=1)
cmds.shot("shot2", e=True, track=2)
cmds.shot("shot3", e=True, track=3)

Insert an empty track at index 2
cmds.shotTrack(insertTrack=2)

Lock the track containing shot3
cmds.shotTrack("shot3", lock=True)

Mute the track containing shot1
cmds.shotTrack("shot1", mute=True)

Remove track 2
cmds.shotTrack(removeTrack=2);

Query the track title for the first track
cmds.shotTrack(q=True, track=2, title=True)

---


Flags:
---


---
insertTrack(it): uint
    properties: create
    This flag is used to insert a new empty track at the track index specified.

---
lock(l): boolean
    properties: create, query, edit
    This flag specifies whether shots on a track are to be locked or not.

---
mute(m): boolean
    properties: create, query, edit
    This flag specifies whether shots on a track are to be muted or not.

---
numTracks(nt): uint
    properties: query
    To query the number of tracks

---
removeEmptyTracks(ret): boolean
    properties: create
    This flag is used to remove all tracks that have no clips.

---
removeTrack(rt): uint
    properties: create
    This flag is used to remove the track with the specified index.  The
track must have no clips on it before it can be removed.

---
selfmute(sm): boolean
    properties: create, query, edit
    This flag specifies whether shots on a track are to be muted or not (unlike mute, this disregards soloing).

---
solo(so): boolean
    properties: create, query, edit
    This flag specifies whether shots on a track are to be soloed or not.

---
swapTracks(st): [uint, uint]
    properties: create
    This flag is used to swap the contents of two specified tracks.

---
title(t): string
    properties: create, query, edit
    This flag specifies the title for the track.

---
track(tr): uint
    properties: create, query, edit
    Specify the track on which to operate by using the track's trackNumber.
                        In query mode, this flag needs a value.

---
unsolo(uso): boolean
    properties: query
    This flag specifies whether shots on a track are to be unsoloed or not.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/shotTrack.html 
    """


def showHelp(flagabsolute: boolean, flagdocs: boolean, flaghelpTable: boolean, flagversion: boolean) -> None:
    """Synopsis:
---
---
 showHelp([string], [absolute=boolean], [docs=boolean], [helpTable=boolean], [version=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

showHelp is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

View the documentation for the launchBrowser command
---

cmds.showHelp( 'Commands/showHelp.html', docs=True )

View the Autodesk home page
---

cmds.showHelp( 'http://www.autodesk.com/', absolute=True )

Query for the full path to the help page on the Align Tool
---

cmds.showHelp( 'AlignTool', q=True )

Set the help lookup-table to $MAYA_APP_DIR/customHelpTable
---

cmds.showHelp( 'customHelpTable', helpTable=True )

View the help topic "Particle" found in customHelpTable.dat
---

cmds.showHelp( 'Particle' )

---


Flags:
---


---
absolute(a): boolean
    properties: create
    The specified "URL" is an absolute URL that should be passed directly
to the web browser.

---
docs(d): boolean
    properties: create, query
    Use this flag to directly specify a help file relative to the
on-line documentation root.

---
helpTable(ht): boolean
    properties: create, query
    Use this flag to specify which file will be used to search for help
topics when the -d/docs and -a/absolute flags are not used. If only
a file name is specified and not a path, then the file is assumed to
be in the maya application directory.
If this flag does not accept an argument if it is queried.
The default value is "helpTable".

---
version(v): boolean
    properties: query
    Use this flag to get the Maya version that the showHelp command uses.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/showHelp.html 
    """


def showHidden(flagabove: boolean, flagallObjects: boolean, flagbelow: boolean, flaglastHidden: boolean) -> None:
    """Synopsis:
---
---
 showHidden(
[objects...]
    , [above=boolean], [allObjects=boolean], [below=boolean], [lastHidden=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

showHidden is undoable, NOT queryable, and NOT editable.showHidden
See also: hide




Example:
---
import maya.cmds as cmds

create a sphere and group it, then hide the sphere and the group.
cmds.sphere( n='sphere1' )
cmds.group( n='group1' )
cmds.hide( 'group1', 'sphere1' )

make the sphere visible. Note that you still can't see it
because the group is invisible.
cmds.showHidden( 'sphere1' )

make the sphere and the group visible.
cmds.showHidden( 'sphere1', above=True )

make everything visible. This will make the cameras (which are
normally invisible) visible as well.
cmds.showHidden( all=True )

---


Flags:
---


---
above(a): boolean
    properties: create
    Make objects and all their invisible ancestors visible.

---
allObjects(all): boolean
    properties: create
    Make all invisible objects visible.

---
below(b): boolean
    properties: create
    Make objects and all their invisible descendants visible.

---
lastHidden(lh): boolean
    properties: create
    Show everything that was hidden with the last hide command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/showHidden.html 
    """


def showManipCtx(flagaddAttr: string, flagcurrentNodeName: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagincSnap: tuple[uint, boolean], flagincSnapRelative: tuple[uint, boolean], flagincSnapUI: boolean, flagincSnapValue: tuple[uint, float], flagiveVisible: boolean, flaglockSelection: boolean, flagmoveActiveAttrDown: boolean, flagmoveActiveAttrToTop: boolean, flagmoveActiveAttrUp: boolean, flagname: string, flagremoveAttr: string, flagresetActiveAttr: boolean, flagselectedAttributes: boolean, flagsetAttrActive: string, flagsetNextAttrActive: boolean, flagsetPreviousAttrActive: boolean, flagtoggleIncSnap: boolean, flagtoolFinish: script, flagtoolStart: script) -> string:
    """Synopsis:
---
---
 showManipCtx(
string
    , [addAttr=string], [currentNodeName=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [incSnap=[uint, boolean]], [incSnapRelative=[uint, boolean]], [incSnapUI=boolean], [incSnapValue=[uint, float]], [iveVisible=boolean], [lockSelection=boolean], [moveActiveAttrDown=boolean], [moveActiveAttrToTop=boolean], [moveActiveAttrUp=boolean], [name=string], [removeAttr=string], [resetActiveAttr=boolean], [selectedAttributes=boolean], [setAttrActive=string], [setNextAttrActive=boolean], [setPreviousAttrActive=boolean], [toggleIncSnap=boolean], [toolFinish=script], [toolStart=script])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

showManipCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Creates a new show manip context.
cmds.showManipCtx()

---
Return:
---


    string: The name of the newly created context.

Flags:
---


---
addAttr(aa): string
    properties: edit
    Add a specific attribute to the In View Editor attribute list.

---
currentNodeName(cnn): boolean
    properties: query
    Returns the name of the first node that the context is attached to.

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
incSnap(incSnap): [uint, boolean]
    properties: create, query, edit, multiuse
    If true, the manipulator owned by the context will use incremental snapping for specified mode.

---
incSnapRelative(isr): [uint, boolean]
    properties: create, query, edit, multiuse
    If true, the manipulator owned by the context will use relative incremental snapping for specified mode.

---
incSnapUI(isu): boolean
    properties: query
    Returns an array of elements indicating what kind of incremental snap UI is
required by the manipulator owned by the context.
If no UI is required, the result array will contain a single element
of with the value 0. The other values and their meanings are:

1 - UI for linear incremental translate
2 - UI for incremental rotate
3 - UI for inclremental scale

---
incSnapValue(isv): [uint, float]
    properties: create, query, edit, multiuse
    Supply the step value which the manipulator owned by the context will use for specified mode.

---
iveVisible(iv): boolean
    properties: query, edit
    Set the In View Editor visible or not.

---
lockSelection(ls): boolean
    properties: create, query, edit
    If true, this context will never change the current selection.
By default this is set to false.

---
moveActiveAttrDown(md): boolean
    properties: edit
    Move the In View Editor active attribute down one in the list.

---
moveActiveAttrToTop(mtt): boolean
    properties: edit
    Move the In View Editor active attribute to the top of the list.

---
moveActiveAttrUp(mu): boolean
    properties: edit
    Move the In View Editor active attribute up one in the list.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
removeAttr(ra): string
    properties: edit
    Remove a specific attribute from the In View Editor attribute list.

---
resetActiveAttr(raa): boolean
    properties: edit
    Reset the In View Editor active attribute to its default value.

---
selectedAttributes(sa): boolean
    properties: query
    Returns a list of the names of the attributes that are currently visible
in the In View Editor.

---
setAttrActive(saa): string
    properties: edit
    Set a specific attribute from the In View Editor attribute list active.

---
setNextAttrActive(sna): boolean
    properties: edit
    Set the next attribute in the In View Editor attribute list active.

---
setPreviousAttrActive(spa): boolean
    properties: edit
    Set the previous attribute in the In View Editor attribute list active.

---
toggleIncSnap(tis): boolean
    properties: create, edit
    Toggles (enables/disables) snapping for all modes.

---
toolFinish(tf): script
    properties: create, query, edit
    Supply the script that will be run when the user exits
the script.

---
toolStart(ts): script
    properties: create, query, edit
    Supply the script that will be run when the user first
enters the script

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/showManipCtx.html 
    """


def showMetadata(flagauto: boolean, flagdataType: string, flaginterpolation: boolean, flagisActivated: boolean, flaglistAllStreams: boolean, flaglistMembers: boolean, flaglistValidMethods: boolean, flaglistVisibleStreams: boolean, flagmember: string, flagmethod: string, flagoff: boolean, flagrange: tuple[float, float], flagrayScale: float, flagstream: string) -> string:
    """Synopsis:
---
---
 showMetadata([auto=boolean], [dataType=string], [interpolation=boolean], [isActivated=boolean], [listAllStreams=boolean], [listMembers=boolean], [listValidMethods=boolean], [listVisibleStreams=boolean], [member=string], [method=string], [off=boolean], [range=[float, float]], [rayScale=float], [stream=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

showMetadata is undoable, queryable, and NOT editable.
This command is used to show metadata values which is in the
specified channels "vertex", "edge", "face", and "vertexFace" in
the viewport. You can view the data by three ways:

"color": draw color on the components. 
"ray": draw a ray on the components. 
"string": draw 2d strings on the components. 

For example, if the metadata of "shape.vtx[1]" is (1, 0, 0), you can turn on
the visualization with all three modes.
On "color" mode, you can see a red vertex which is on the position of "shape.vtx[1]".
On "ray" mode, you can see a ray with the direction (1, 0, 0).
On "string" mode, you can see strings "1 0 0" below the vertex in the viewport.


To use "color" or "ray" mode, you should make the member of the data structure
with three or less items, such as float[3]. The three items are mapped to "RGB" as a color, or "XYZ"
as a vector. The structure with two items works similarly. The only difference
is that the third value will always be zero.
However, if the structure has only one item, the value is mapped to all three variables.
That means if the structure is "int" and its value is 1, the color will be white(1, 1, 1)
and the vector will be (1, 1, 1).


You can get the current status of the flags on the query mode (using "-query").
But you can query only the status of one flag in a single command and
you cannot set values on the query mode.


You can use the command on some specified objects, or run it with no arguments
to make changes on all objects in the scene. The object must be a mesh shape.
Components are not allowed as the command arguments.




Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

---
Create a scene
cmds.file(force=True, new=True)
cmds.dataStructure(format="raw", asString="name=StructOne:int32=MemberOne")
cmds.polyPlane(constructionHistory=False, name="mesh")

---
Add Metadata
cmds.addMetadata('meshShape', streamName="StreamOne", channelName="vertex", structure="StructOne")
cmds.editMetadata('meshShape.vtx[1]', streamName="StreamOne", channelName="vertex", memberName="MemberOne", value=1)
cmds.select(clear=True)

cmds.showMetadata('meshShape', member="MemberOne", dataType="int32", stream="StreamOne")
---
Show metadata for which the member is "MemberOne" and the stream is "StreamOne"

cmds.showMetadata('meshShape', stream="StreamOne", member="MemberOne", dataType="int32", method="color")
---
StreamOne will be visualized by Component Color method. The other two visualization methods are
---
"string" and "ray". If "-method" flag is not defined, "color" will be used by default.

cmds.showMetadata(off=True)
---
Deactivate all streams to turn off metadata visualization

cmds.showMetadata(stream="StreamOne", member="MemberOne", dataType="int32", method="color", interpolation=True)
---
Enable interpolation on "color" mode. Interpolation must be used with "color" method

cmds.showMetadata(range=[0, 10], stream="StreamOne", member="MemberOne", dataType="int32")
---
Show metadata between a specified range from 0 to 10. If the method is "color",
the value 0 will be displayed in black, while the value 10 will be displayed
in white. The value beyond the range will be clamped to 0 or 10.

cmds.showMetadata('meshShape', auto=True, stream="StreamOne", member="MemberOne", dataType="int32")
---
Show metadata between the dynamic range, which is computed by the current min/max value

cmds.showMetadata(query=True, listAllStreams=True)
---
Return all streams in the scene, no matter if they are activated

cmds.showMetadata('meshShape', query=True, listAllStreams=True)
---
Return all streams of meshShape, no matter if they are activated

cmds.showMetadata(query=True, listVisibleStreams=True)
---
Return the stream name(s) being visualized in the scene

cmds.showMetadata('meshShape', query=True, listVisibleStreams=True)
---
Return the stream name being visualized that is attached to meshShape

cmds.showMetadata(query=True, stream="StreamOne", listMembers=True)
---
Return the member names and types in the specified stream
---
The names and types are returned in pair, such as "MemberOne int32 MemberTwo float"

cmds.showMetadata(query=True, stream="StreamOne", member="MemberOne", dataType="int32", method=True)
---
Return the visualization method of the visualized StreamOne

cmds.showMetadata(query=True, stream="StreamOne", member="MemberOne", dataType="int32", listValidMethods=True)
---
Return the valid visual methods of the activated stream that can be set

cmds.showMetadata(query=True, stream="StreamOne", member="MemberOne", dataType="int32", range=True)
---
Return the current range of visible metadata

cmds.showMetadata(query=True, stream="StreamOne", member="MemberOne", dataType="int32", auto=True)
---
Return the current state of the auto flag

---
Return:
---


    string: result of the operation or the queried status

Flags:
---


---
auto(a): boolean
    properties: create, query
    Similar to the flag "-range", but uses the min/max value from the metadata in the same stream
and member instead of the specified input value.
In query mode, you can use the flag to query if "auto" is on.

---
dataType(dt): string
    properties: create, query
    In create mode, when used with the flags "stream" and "member",
specify a member to show.
If the flag "off" is used, specify the member to turn off.
In query mode, when used with the flags "stream" and "member", query
the visualization state of the specified member.
Only one member of each shape can be visualized at a time.
                        In query mode, this flag can accept a value.

---
interpolation(i): boolean
    properties: create, query
    In create mode, enable/disable interpolation for "color" method.
When interpolation is on, the components will be displayed in the interpolated color,
which is computed by averaging their metadata values.
In query mode, query the current state of interpolation flag of
the selected objects.

---
isActivated(ia): boolean
    properties: create, query
    Used to check if the given stream is activated.
If some shapes are selected, query their states.
If no shape is selected, query the states of all shapes
in the scene.

---
listAllStreams(las): boolean
    properties: create, query
    Used with object names to list all streams of the specified objects.
no matter if they are visible in the viewport.
Or you can use the flag individually to list all streams in the scene.
Due to the fact that different objects may have the same stream name,
the returned list will merge the duplicated stream names automatically.

---
listMembers(lm): boolean
    properties: create, query
    Used with the flag 'stream' to get the
member list in the specified stream.

---
listValidMethods(lvm): boolean
    properties: create, query
    List the valid visual methods that can be set for the current stream and member. Some data type cannot be displayed
by some methods. For example, if the data type is "string", it cannot be displayed by "color" or by "ray".
In other words, only the method "string" will be returned when you list the methods.

---
listVisibleStreams(lvs): boolean
    properties: create, query
    Used with object names to list the name of the current visible streams of
the specified object. Or you can use the flag with no object name to list
all visible streams in the scene.

---
member(mb): string
    properties: create, query
    In create mode, when used with the flags "stream" and "dataType",
specify a member to show.
If the flag "off" is on, specify the member to turn off.
In query mode, when used with the flags "stream" and "dataType", query
the visualization state of the specified member.
Only one member of each shape can be visualized at a time.
                        In query mode, this flag can accept a value.

---
method(m): string
    properties: create, query
    Determine the method of visualization:
"color"         convert metadata to a color value and draw the components with the color
"ray"           convert metadata to a vector and draw this vector line which starts from the center of the component
"string"        display the metadata through 2d string beside the component in the viewport
The argument must be a string and must be one of the three words. The default method is "color".
If the data type is string, you can only show it with "string" method.
In query mode, you can use the flag with no arguments to query the method of a specified stream and member.

---
off(): boolean
    properties: create, query
    In create mode, turn off the member which is specified
by the flags "stream", "member" and "dataType".

---
range(r): [float, float]
    properties: create, query
    Specify the range of data to use. The value which is out of the range will be clamped to
the min/max value.
If the method of visualization is "color", the range will be mapped to the color. That means
the min value will be displayed in black while the max value will be in white.
In query mode, you can use the flag individually to query the current range.

---
rayScale(rs): float
    properties: create, query
    Specify the scale of the ray to display it with a proper length.

---
stream(s): string
    properties: create, query
    In create mode, when used with the flags "member" and "dataType", specify a member to show.
If the flag "off" is used, specify the member to turn off.
In query mode, when used with the flags "member" and "dataType", query
the visualization state of the specified member.
When used with the flag "listMembers", query the members in the
specified stream.
Only one member of each shape can be visualized at a time.
                        In query mode, this flag can accept a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/showMetadata.html 
    """


def showSelectionInTitle() -> None:
    """Synopsis:
---
---
 showSelectionInTitle(
[string]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

showSelectionInTitle is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

window = cmds.window(widthHeight=(400, 100))
cmds.paneLayout()
cmds.scrollField(wordWrap=True, text='The title of this window will reflect the current object selection.')
cmds.showWindow(window)

cmds.showSelectionInTitle(window)
cmds.sphere()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/showSelectionInTitle.html 
    """


def showShadingGroupAttrEditor() -> boolean:
    """Synopsis:
---
---
 showShadingGroupAttrEditor()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

showShadingGroupAttrEditor is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.showShadingGroupAttrEditor()

---
Return:
---


    boolean: true if a shading group is displayed, otherwise false.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/showShadingGroupAttrEditor.html 
    """


def showWindow() -> None:
    """Synopsis:
---
---
 showWindow(
[string]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

showWindow is undoable, NOT queryable, and NOT editable.windowvis/visible
If the specified window is iconified, it will be opened.




Example:
---
import maya.cmds as cmds

cmds.showWindow( 'myWindow1' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/showWindow.html 
    """


def simplify(flaganimation: string, flagattribute: string, flagcontrolPoints: boolean, flagfloat: floatrange, flagfloatTolerance: float, flaghierarchy: string, flagincludeUpperBound: boolean, flagindex: uint, flagshape: boolean, flagtime: timerange, flagtimeTolerance: time, flagvalueTolerance: float) -> int:
    """Synopsis:
---
---
 simplify(
animatedObject
    , [animation=string], [attribute=string], [controlPoints=boolean], [float=floatrange], [floatTolerance=float], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [shape=boolean], [time=timerange], [timeTolerance=time], [valueTolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

simplify is undoable, NOT queryable, and NOT editable.
The animation curves comprising a keyset depend on the value
of the "-animation" flag:


keysOrObjects:

Any active keys, when no target objects or -attribute
flags appear on the command line, or

All animation curves connected to all keyframable
attributes of objects specified as the command line's
targetList, when there are no active keys.




keys:
Only act on active keys or tangents.
If there are no active keys or tangents, don't do anything.



objects:
Only act on specified objects.  If there are no objects specified, don't
do anything.



Note that the "-animation" flag can be used to override
the curves uniquely identified by the multi-use
"-attribute" flag, which takes an argument of the form
attributeName, such as "translateX".

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given individually or as part of a list or range (see Examples).

This command will simplify (reduce the number of keyframes) an animation
curve.




Example:
---
import maya.cmds as cmds

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given as a range or list of ranges.

time=('10pal','10pal') means the key at frame 10 (PAL format).
time=[('1.0sec','1.0sec'),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
time=(10,None) means all keys from time 10 (in the current time unit) onwards.
time=(10,) means the same as (10,10)
time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
time=(None,None) is a short form to specify all keys.
index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.

cmds.polySphere()
cmds.setKeyframe( '.tx' )
cmds.simplify( time=(1,10) )

---
Return:
---


    int: Number of animation curves simplified

Flags:
---


---
animation(an): string
    properties: create
    Where this command should get the animation to act
on.  Valid values are "objects," "keys," and
"keysOrObjects" Default: "keysOrObjects."  (See
Description for details.)

---
attribute(at): string
    properties: create, multiuse
    List of attributes to select
      In query mode, this flag needs a value.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
float(f): floatrange
    properties: create, multiuse
    value uniquely representing a non-time-based
key (or key range) on a time-based animCurve.  Valid
floatRange include single values (-f 10) or a
string with a lower and upper bound, separated by a
colon (-f "10:20")
      In query mode, this flag needs a value.

---
floatTolerance(ft): float
    properties: create
    Specify the x-axis tolerance (defaults to 0.05) for
float-input animCurves such as those created by "Set Driven Keyframe".
This flag is ignored on animCurves driven by time. Higher floatTolerance
values will result in sparser keys which may less accurately represent
the initial curve.

---
hierarchy(hi): string
    properties: create
    Hierarchy expansion options.  Valid values are "above,"
"below," "both," and "none." (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
includeUpperBound(iub): boolean
    properties: create
    When the -t/time or -f/float flags represent a range
of keys, this flag determines whether the keys at the
upper bound of the range are included in the keyset.
Default value: true.  This flag is only valid when
the argument to the -t/time flag is a time range with
a lower and upper bound.  (When used with the "pasteKey"
command, this flag refers only to the time range of the
target curve that is replaced, when using options such
as "replace," "fitReplace," or "scaleReplace."  This
flag has no effect on the curve pasted from the clipboard.)

---
index(index): uint
    properties: create, multiuse
    index of a key on an animCurve
      In query mode, this flag needs a value.

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

---
timeTolerance(tt): time
    properties: create
    Specify the x-axis tolerance (defaults to 0.05 seconds)
for time-input animCurves. This flag is ignored on animCurves
driven by floats. Higher time tolerance values will result in
sparser keys which may less accurately represent
the initial curve.

---
valueTolerance(vt): float
    properties: create
    Specify the value tolerance (defaults to 0.01)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/simplify.html 
    """


def singleProfileBirailSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagpolygon: int, flagtangentContinuityProfile1: boolean, flagtransformMode: int) -> list[string]:
    """Synopsis:
---
---
 singleProfileBirailSurface(
curve curve curve
    , [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean], [polygon=int], [tangentContinuityProfile1=boolean], [transformMode=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

singleProfileBirailSurface is undoable, queryable, and editable.
The first argument represetns the profile curve, the second and third
the rails.




Example:
---
import maya.cmds as cmds

---
Create a surface by sweeping profile "curve1" along the two rails
---
given by isoparms surface1.u[0] and surface2.u[0.5].
cmds.singleProfileBirailSurface( 'curve1', 'surface1.u[0]', 'surface2.u[0.5]', ch=True )

create a tangent continuous surface across the profile.
cmds.singleProfileBirailSurface( 'surface1.u[0]', 'curve1', 'curve2', ch=True, tp1=True )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
tangentContinuityProfile1(tp1): boolean
    properties: create, query, edit
    Need to be tangent continuous across the profile. The profile must be a surface curve.
Default: false

---
transformMode(tm): int
    properties: create, query, edit
    transform mode ( Non proportional, proportional ). Non proportional is default value.
Default: 0

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
polygon(po): int
    properties: create
    The value of this argument controls the type of the object
created by this operation

 0: nurbs surface
 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)
 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)
 3: Bezier surface
 4: subdivision surface solid (use nurbsToSubdivPref to set the
parameters for the conversion)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/singleProfileBirailSurface.html 
    """


def skeletonEmbed(flagmergedMesh: boolean, flagsegmentationMethod: uint, flagsegmentationResolution: uint) -> None:
    """Synopsis:
---
---
 skeletonEmbed([mergedMesh=boolean], [segmentationMethod=uint], [segmentationResolution=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

skeletonEmbed is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


First select the shape, not the transform.
cmds.select( 'characterShape' , r=True )

Embed skeleton using default parameter.
cmds.skeletonEmbed( )
Result: u'{ [...] (A JSON dictionary with the description of the embedding. }' ---


For debugging: get the merged mesh that will be used
cmds.skeletonEmbed( query=True , mergedMesh=True )
Result: u'{ [...] (A JSON dictionary with the description of the merged mesh. }' ---


Embed skeleton using polygon soup and 512 resolution.
cmds.skeletonEmbed( segmentationMethod=3 , segmentationResolution=512 )


This method creates a few joints to see the embedding.
import json
def createJointsFromEmbedding( embeddingString ):
    embedding = json.loads( embeddingString )
    for name , position in embedding[ 'joints' ].items( ):
        joint = cmds.createNode( 'joint' , name=name )
        cmds.xform( joint , worldSpace=True , translation=position )

result = cmds.skeletonEmbed( )
createJointsFromEmbedding( result )


This method creates a mesh from the merged mesh to see it.
import json
import maya.OpenMaya as OpenMaya
def createMeshFromDescription( meshString ):
    mesh = json.loads( meshString )

    meshPoints = mesh[ 'points' ]
    meshFaces  = mesh[ 'faces' ]
    factor     = 1.0 / mesh[ 'conversionFactor' ]

    Vertices
    vertexArray = OpenMaya.MFloatPointArray()
    for i in range( 0 , len( meshPoints ) , 3 ):
        vertex = OpenMaya.MFloatPoint( meshPoints[ i ] * factor , meshPoints[ i + 1 ] * factor , meshPoints[ i + 2 ] * factor )
        vertexArray.append( vertex )
    numVertices = vertexArray.length()

    Faces
    polygonCounts   = OpenMaya.MIntArray()
    polygonConnects = OpenMaya.MIntArray()
    for face in meshFaces:
        for i in face:
            polygonConnects.append( i )
        polygonCounts.append( len( face ) )
    numPolygons = polygonCounts.length()

    fnMesh = OpenMaya.MFnMesh()
    newMesh = fnMesh.create( numVertices , numPolygons , vertexArray , polygonCounts , polygonConnects )
    fnMesh.updateSurface()

    Assign new mesh to default shading group
    nodeName = fnMesh.name()
    cmds.sets( nodeName , e=True , fe='initialShadingGroup' )

    return nodeName

result = cmds.skeletonEmbed( query=True , mergedMesh=True )
createMeshFromDescription( result )

---


Flags:
---


---
mergedMesh(mm): boolean
    properties: query
    When specified, the query command merges selected meshes together and returns a
Python object representing the merged mesh.

---
segmentationMethod(sm): uint
    properties: create
    Specifies which segmentation algorithm to use to determine what is inside the mesh
and what is outside the mesh.  By default, boundary-and-fill-and-grow voxelization
will be used.

Available algorithms are:


0  : Perfect mesh (no voxelization).
This method works for "perfect meshes", i.e. meshes that are closed, watertight,
2-manifold and without self-intersection or interior/hidden geometry.  It segments
the interior region of the mesh from the exterior using a pseudo-normal test.
It does not use voxelization.  If mesh conditions are not respected, the segmentation
is likely to be wrong.  This can make the segmentation process significantly longer
and prevent successful skeleton embedding.


1 : Watertight mesh (flood fill).
This method works for "watertight meshes", i.e. meshes for which faces completely
separate the interior region of the mesh from the exterior.  The mesh can have
degenerated faces, wrong face orientation, self-intersection, etc.  The method
uses surface voxelization to classify as part of the interior region all voxels
intersecting with a mesh face.  It then performs flood-filling from the outside,
marking all reached voxels as part of the exterior region of the model.  Finally,
all unreached voxels are marked as part of the interior region.  This method works
so long as the mesh is watertight, i.e. without holes up to the voxelization resolution.
Otherwise, flood-filling reaches the interior region and creates inaccurate segmentation.


2 : Imperfect mesh (flood fill + growing).
This method works for meshes where holes could make the flood-filling step reach the
interior region of the mesh, but that have face orientation consistent enough so filling
them is possible.  First, it uses surface voxelization to classify as part of the interior
region all voxels intersecting with a mesh face.  It then alternates flood-filling and
growing steps.  The flood-filling tries to reach all voxels from the outside so that
unreached voxels are marked as part of the interior region.  The growing step uses a
relatively computation-intensive process to check for interior voxels in all neighbors
to those already identified.  Any voxel identified as interior is likely to fill holes,
allowing subsequent flood-filling steps to identify more interior voxels.


3 : Polygon soup (repair).
This method has no manifold or face orientation requirements.  It reconstructs a mesh
that wraps the input mesh with a given offset (3 times the voxel size) and uses this
perfect 2-manifold mesh to segment the interior region from the exterior region of the model.
Because of the offset, it might lose some of the details and merge parts that are proximal.
However, this usually is not an issue with common models where body parts are not too close
to one another.


99 : Direct skeleton (no embedding).
This method does not try to perform embedding.  It simply returns the skeleton in its initial
pose without any attempt at embedding inside the meshes, other than placing it in the meshes
bounding box.

---
segmentationResolution(sr): uint
    properties: create
    Specifies which segmentation resolution to use for the voxel grid.  By default,
256x256x256 voxels will be used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/skeletonEmbed.html 
    """


def skinBindCtx(flagabout: string, flagaxis: string, flagcolorRamp: string, flagcurrentInfluence: string, flagdisplayInactiveMode: int, flagdisplayNormalized: boolean, flagexists: boolean, flagfalloffCurve: string, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagsymmetry: boolean, flagtolerance: float) -> string:
    """Synopsis:
---
---
 skinBindCtx(
string
    , [about=string], [axis=string], [colorRamp=string], [currentInfluence=string], [displayInactiveMode=int], [displayNormalized=boolean], [exists=boolean], [falloffCurve=string], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [symmetry=boolean], [tolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

skinBindCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.skinBindCtx( 'skinBindContext' )

---
Return:
---


    string: The name of the context created

Flags:
---


---
about(a): string
    properties: create, query, edit
    The space in which the axis should be mirrored. Valid values are: "world" and "object".

---
axis(ax): string
    properties: create, query, edit
    The mirror axis. Valid values are: "x","y", and "z".

---
colorRamp(cr): string
    properties: create, query, edit
    Set the values on the color ramp used to display the weight values.

---
currentInfluence(ci): string
    properties: create, query, edit
    Set the index of the current influence or volume to be adjusted by the manipulator.

---
displayInactiveMode(di): int
    properties: create, query, edit
    Determines the display mode for drawing volumes that are not selected,
in particular which volume cages if any are displayed.
0 - None
1 - Nearby volumes
2 - All volumes

---
displayNormalized(dn): boolean
    properties: create, query, edit
    Display raw select weights (false) or finalized normalized weights (true).

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
falloffCurve(fc): string
    properties: create, query, edit
    Set the values on the falloff curve control.

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
symmetry(s): boolean
    properties: create, query, edit
    Controls whether or not the tool operates in symmetric (mirrored) mode.

---
tolerance(t): float
    properties: create, query, edit
    The tolerance setting for determining whether another influence is symmetric to the the current influence.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/skinBindCtx.html 
    """


def skinCluster(flagaddInfluence: string, flagaddToSelection: boolean, flagafter: boolean, flagafterReference: boolean, flagbaseShape: string, flagbefore: boolean, flagbindMethod: int, flagcomponents: boolean, flagdeformerTools: boolean, flagdropoffRate: float, flagexclusive: string, flagforceNormalizeWeights: boolean, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagheatmapFalloff: float, flagignoreBindPose: boolean, flagignoreHierarchy: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flaginfluence: string, flaglockWeights: boolean, flagmaximumInfluences: int, flagmoveJointsMode: boolean, flagmulti: boolean, flagname: string, flagnormalizeWeights: int, flagnurbsSamples: int, flagobeyMaxInfluences: boolean, flagparallel: boolean, flagpolySmoothness: float, flagprune: boolean, flagrecacheBindMatrices: boolean, flagremove: boolean, flagremoveFromSelection: boolean, flagremoveInfluence: string, flagremoveUnusedInfluence: boolean, flagselectInfluenceVerts: string, flagselectedComponents: boolean, flagskinMethod: int, flagsmoothWeights: float, flagsmoothWeightsMaxIterations: int, flagsplit: boolean, flagtoSelectedBones: boolean, flagtoSkeletonAndTransforms: boolean, flagunbind: boolean, flagunbindKeepHistory: boolean, flaguseComponentTags: boolean, flaguseGeometry: boolean, flagvolumeBind: float, flagvolumeType: int, flagweight: float, flagweightDistribution: int, flagweightedInfluence: boolean) -> string:
    """Synopsis:
---
---
 skinCluster(
objects
    , [addInfluence=string], [addToSelection=boolean], [after=boolean], [afterReference=boolean], [baseShape=string], [before=boolean], [bindMethod=int], [components=boolean], [deformerTools=boolean], [dropoffRate=float], [exclusive=string], [forceNormalizeWeights=boolean], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [heatmapFalloff=float], [ignoreBindPose=boolean], [ignoreHierarchy=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [influence=string], [lockWeights=boolean], [maximumInfluences=int], [moveJointsMode=boolean], [multi=boolean], [name=string], [normalizeWeights=int], [nurbsSamples=int], [obeyMaxInfluences=boolean], [parallel=boolean], [polySmoothness=float], [prune=boolean], [recacheBindMatrices=boolean], [remove=boolean], [removeFromSelection=boolean], [removeInfluence=string], [removeUnusedInfluence=boolean], [selectInfluenceVerts=string], [selectedComponents=boolean], [skinMethod=int], [smoothWeights=float], [smoothWeightsMaxIterations=int], [split=boolean], [toSelectedBones=boolean], [toSkeletonAndTransforms=boolean], [unbind=boolean], [unbindKeepHistory=boolean], [useComponentTags=boolean], [useGeometry=boolean], [volumeBind=float], [volumeType=int], [weight=float], [weightDistribution=int], [weightedInfluence=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

skinCluster is undoable, queryable, and editable.
The skinCluster binds only a single geometry at a time. Thus, to bind
multiple geometries, multiple skinCluster commands must be issued.

Upon creation of a new skinCluster, the command can be used to add
and remove transforms (not necessarily joints) that influence the
motion of the bound skin points.  

The skinCluster command can also be used to adjust parameters such
as the dropoff, nurbs samples, polygon smoothness on a particular
influence object. Note: Any custom weights on a skin point that
the influence object affects will be lost after adjusting these
parameters.




Example:
---
import maya.cmds as cmds

Create a joint chain and a polygonal plane.
cmds.select(d=True)
cmds.joint(p=(-3.0, 0.0,-12.0))
cmds.joint(p=(-3.0, 0.0, -5.0))
cmds.joint(p=(1.0, 0.0, 5.5))
cmds.joint(p=(6.0, 0.0, 10.0))
cmds.polyPlane(w=20.0,h=20.0,sx=25,sy=25)

Bind the joint chain that contains joint1 to pPlane1
and assign a dropoff of 4.5 to all the joints
---

cmds.skinCluster( 'joint1', 'pPlane1', dr=4.5)

Undo the previous command and bind only joint1 and joint3 to pPlane1
---

cmds.undo();
cmds.skinCluster('joint1', 'joint3', 'pPlane1',tsb=True)

Set the maximum number of transforms influencing each
point to 3
cmds.skinCluster('skinCluster1',e=True,mi=3)

Add transform joint2 to the list of transforms
that influence the bound skin
---

cmds.select('pPlane1')
cmds.skinCluster(edit=True,ai='joint2')

Query the influences for the skinCluster
---

cmds.skinCluster('skinCluster1',query=True,inf=True)

Add a curve influence object
---

cmds.curve(d=3,p=[(2.0, 0.0, -7.0),(5.0, 0.0, -4.0),(6.0, 0.0, 1.0),(6.0, 0.0, 4.0),(5.0, 0.0, 6.0)],k=[0,0,0,1,2,2,2])

Get the number of nurbsSamples taken along curve1
---

cmds.skinCluster('skinCluster1',edit=True,ai='curve1')
cmds.skinCluster('skinCluster1',inf='curve1',query=True,ns=True)

Set the dropoff for joint3 to 5.0
---

cmds.skinCluster('skinCluster1',e=True,inf='joint3',dr=5.0)

Query for the dropoff for joint3
---

cmds.skinCluster('skinCluster1',inf='joint3',q=True,dr=True)

---
Return:
---


    string: (the skinCluster node name)

Flags:
---


---
addInfluence(ai): string
    properties: edit, multiuse
    The specified transform or joint will be added to the
list of transforms that influence the bound geometry.
The maximum number of influences will be observed
and only the weights of the cv's that the specified
transform effects will change.
This flag is multi-use.

---
addToSelection(ats): boolean
    properties: edit
    When used in conjunction with the selectInfluenceVerts flag, causes the vertices
afftected by the influence to be added to the current selection, without first
de-selecting other vertices.

---
after(af): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node after the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
afterReference(ar): boolean
    properties: create, edit
    The -afterReference flag is used to specify deformer ordering in a hybrid way that
choses between -before and -after automatically. If the geometry being
deformed is referenced then the -after mode is used when adding the new deformer,
otherwise the -before mode is used. The net effect when using -afterReference to build
deformer chains is that internal shape nodes in the deformer chain will only
appear at reference file boundaries, leading to lightweight deformer networks that
may be more amicable to reference swapping.

---
baseShape(bsh): string
    properties: edit, multiuse
    This flag can be used in conjunction with
the -addInfluence flag to specify the shape that will
be used as the base shape when an influence object with
geometry is added to the skinCluster.  If the flag
is not used then the command will make a copy of the
influence object's shape and use that as a base shape.

---
before(bf): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node before the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
bindMethod(bm): int
    properties: create, query
    This flag sets the binding method.
0 - Closest distance between a joint and a point of the geometry.
1 - Closest distance between a joint, considering the skeleton
hierarchy, and a point of the geometry.
2 - Surface heat map diffusion.
3 - Geodesic voxel binding.  geomBind command must be called after creating a skinCluster with this method.

---
components(cmp): boolean
    properties: query
    Returns the components used by the deformer

---
deformerTools(dt): boolean
    properties: query
    Returns the name of the deformer tool objects (if any)
as string string ...

---
dropoffRate(dr): float
    properties: create, query, edit
    Sets the rate at which the influence of a transform
drops as the distance from that transform increases.
The valid range is between 0.1 and 10.0.  In Create
mode it sets the dropoff rate for all the bound
joints.  In Edit mode the flag is used together with the
inf/influence flag to set the dropoff rate of a
particular influence.  Note: When the flag is used in
Edit mode, any custom weights on the skin points the
given transform influences will be lost.

---
exclusive(ex): string
    properties: create, query
    Puts the deformation set in a deform partition.

---
forceNormalizeWeights(fnw): boolean
    properties: edit
    If the normalization mode is none or post, it is possible (indeed likely) for the weights in the skin
cluster to no longer add up to 1.  This flag forces all weights to add back to 1 again.

---
frontOfChain(foc): boolean
    properties: create, edit
    This command is used to specify that the new deformer
node should be placed ahead (upstream) of existing deformer
and skin nodes in the shape's history (but not ahead of
existing tweak nodes). The input to the
deformer will be the upstream shape rather than the visible
downstream shape, so the behavior of this flag is the most
intuitive if the downstream deformers are in their reset
(hasNoEffect) position when the new deformer is added.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
geometry(g): string
    properties: query, edit, multiuse
    The specified object will be added to the list of
objects being deformed by this deformer object, unless
the -rm flag is also specified. When queried, this flag
returns string string string ...

---
geometryIndices(gi): boolean
    properties: query
    Complements the -geometry flag in query mode. Returns
the multi index of each geometry.

---
heatmapFalloff(hmf): float
    properties: create
    This flag sets the heatmap binding falloff. If set to 0.0 (default) the
deformation will be smoother due to many small weights spread over the mesh
surface per influence. However, if set to 1.0, corresponding to maximum falloff,
the number of influences per point will be reduced and points will tend to be
greatly influenced by their closest joint decreasing the overall spread of small
weights.
This flag only works when using heatmap binding.

---
ignoreBindPose(ibp): boolean
    properties: create, edit
    This flag is deprecated and no longer used.  It will be ignored
if used.

---
ignoreHierarchy(ih): boolean
    properties: create, query
    Deprecated. Use bindMethod flag instead.
Disregard the place of the joints in the skeleton
hierarchy when computing the closest joints that influence
a point of the geometry.

---
ignoreSelected(ignoreSelected): boolean
    properties: create
    Tells the command to not deform objects on the
current selection list

---
includeHiddenSelections(ihs): boolean
    properties: create
    Apply the deformer to any visible and hidden objects in the selection list.
Default is false.

---
influence(inf): string
    properties: query, edit
    This flag specifies the influence object that
will be used for the current edit operation. In query
mode, returns a string array of the influence objects
(joints and transform).
      In query mode, this flag can accept a value.

---
lockWeights(lw): boolean
    properties: query, edit
    Lock the weights of the specified influence object
to their current value or to the value specified by
the -weight flag.

---
maximumInfluences(mi): int
    properties: create, query, edit
    Sets the maximum number of transforms that can influence
a point (have non-zero weight for the point) when
the skinCluster is first created or a new influence
is added.  Note: When this flag is used in Edit mode
any custom weights will be lost and new weights will be
reassigned to the whole skin.

---
moveJointsMode(mjm): boolean
    properties: edit
    If set to true, puts the skin into a mode where joints can be moved
without modifying the skinning. If set to false, takes the skin out
of move joints mode.

---
multi(mul) 2024: boolean
    properties: create
    If true then the command will allow multiple skin clusters to be created
on the target geometry. If false the command will generate an error if
when trying to add a second skin cluster to the geometry.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
normalizeWeights(nw): int
    properties: create, query, edit
    This flag sets the normalization mode. 0 - none,
1 - interactive, 2 - post (default)
Interactive normalization makes sure the weights on the influences add up to 1.0, always.
Everytime a weight is changed, the weights are automatically normalized.  This may make
it difficult to perform weighting operations, as the normalization may interfere with
the weights the user has set.  Post normalization leaves the weights the user has set
as is, and only normalizes the weights at the moment it is needed
(by dividing by the sum of the weights).  This makes it easier for users to weight their skins.

---
nurbsSamples(ns): int
    properties: create, edit
    Sets the number of sample points that will be used
along an influence curve or in each direction on an
influence NURBS surface to influence the bound skin.
The more the sample points the more closely the skin
follows the influence NURBS curve/surface.

---
obeyMaxInfluences(omi): boolean
    properties: create, query, edit
    When true, the skinCluster will continue to enforce the maximum
influences each time the user modifies the weight, so that any
given point is only weighted by the number of influences in the
skinCluster's maximumInfluences attribute.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
polySmoothness(ps): float
    properties: create, edit
    This flag controls how accurately the skin control
points follow a given polygon influence object.
The higher the value of polySmoothnmess the
more rounded the deformation resulting from a polygonal
influence object will be.

---
prune(pr): boolean
    properties: edit
    Removes any points not being deformed by the deformer in
its current configuration from the deformer set.

---
recacheBindMatrices(rbm): boolean
    properties: edit
    Forces the skinCluster node to recache its bind matrices.

---
remove(rm): boolean
    properties: edit, multiuse
    Specifies that objects listed after the -g flag should
be removed from this deformer.

---
removeFromSelection(rfs): boolean
    properties: edit
    When used in conjunction with the selectInfluenceVerts flag, causes the vertices
afftected by the influence to be removed from the current selection.

---
removeInfluence(ri): string
    properties: edit, multiuse
    Remove the specified transform or joint from the list of
transforms that influence the bound geometry
The weights for the affected points are renormalized.
This flag is multi-use.

---
removeUnusedInfluence(rui): boolean
    properties: create, query, edit
    If this flag is set to true then transform or joint whose weights are all zero
(they have no effect) will not be bound to the geometry.  Having this
option set will help speed-up the playback of animation. In query mode,
returns the number of transforms or joints whose weights are all zero.

---
selectInfluenceVerts(siv): string
    properties: edit
    Given the name of a transform, this will select the verts or control points
being influenced by this transform, so users may visualize which vertices are
being influenced by the transform.

---
selectedComponents(cms): boolean
    properties: query
    Returns the components used by the deformer that are currently selected.
This intersects the current selection with the components affected by the deformer.

---
skinMethod(sm): int
    properties: create, query, edit
    This flag set the skinning method. 0 - classical linear skinning (default).
1 - dual quaternion (volume preserving), 2 - a weighted blend between the two.

---
smoothWeights(sw): float
    properties: edit
    This flag is used to detect sudden jumps in skin weight values, which often
indicates bad weighting, and then smooth out those jaggies in skin weights.
The argument is the error tolerance ranging from 0 to 1.  A value of 1 means
that the algorithm will smooth a vertex only if there is a 100% change in
weight values from its neighbors.  The recommended default to use is 0.5
(50% change in weight value from the neighbors).

---
smoothWeightsMaxIterations(swi): int
    properties: edit
    This flag is valid only with the smooth weights flag.  It is possible that not
all the vertices detected as needing smoothing can be smoothed in 1 iteration
(because all of their neighbors also have bad weighting and need to be smoothed).
With more iterations, more vertices can be smoothed.  This flag controls the
maximum number of iterations the algorithm will attempt to smooth weights.
The default is 2 for this flag.

---
split(sp): boolean
    properties: create, edit
    Branches off a new chain in the dependency graph instead
of inserting/appending the deformer into/onto an
existing chain.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
toSelectedBones(tsb): boolean
    properties: create
    geometry will be bound to the selected bones only.

---
toSkeletonAndTransforms(tst): boolean
    properties: create
    geometry will be bound to the skeleton and any transforms in the hierarchy.
If any of the transforms are also bindable objects, assume that only the
last object passed to the command is the bindable object. The rest are
treated as influences.

---
unbind(ub): boolean
    properties: edit
    Unbinds the geometry from the skinCluster and deletes
the skinCluster node

---
unbindKeepHistory(ubk): boolean
    properties: edit
    Unbinds the geometry from the skinCluster, but keeps
the skinCluster node so that its weights can be used
when the skin is rebound. To rebind, use the skinCluster
command.

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

---
useGeometry(ug): boolean
    properties: edit
    When adding an influence to a skinCluster, use the geometry
parented under the influence transform to determine
the weight dropoff of that influence.

---
volumeBind(vb): float
    properties: create
    Creates a volume bind node and attaches it to the new skin cluster node. This
node holds hull geometry parameters for a volume based weighting system. This system is
used in interactive skinning. The value passed will determine the minimum weight
value when initializing the volume. The volume in be increase to enclose all the vertices
that are above this value.

---
volumeType(vt): int
    properties: create
    Defines the initial shape of the binding volume (see volumeBind). 0 - Default (currently set to a capsule)
1 - Capsule, 2 - Cylinder.

---
weight(wt): float
    properties: edit
    This flag is only valid in conjunction with the -addInfluence flag.
It sets the weight for the influence object that is being added.

---
weightDistribution(wd): int
    properties: create, query, edit
    This flag sets the weight distribution mode.
0 - distance (default), 1 - neighbors
When normalizeWeights is in effect, and a weight has been reduced
or removed altogether, the sum is usually brought back up to 1.0
by increasing the contributions of the other non-zero weights.
However, if there are no other non-zero weights, the algorithm
has to create some weights from thin air and distribute the residual
weight between them.
This attribute controls how that is done.
"Distance" - the algorithm calculates weights from
the world-space distances from the component to the transforms.
"Neighbors" - the algorithm calculates weights from
the weights on the neighboring components.

---
weightedInfluence(wi): boolean
    properties: query
    This flag returns a string array of the influence objects
(joints and transform) that have non-zero weighting.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/skinCluster.html 
    """


def skinPercent(flagignoreBelow: float, flagnormalize: boolean, flagpruneWeights: float, flagrelative: boolean, flagresetToDefault: boolean, flagtransform: string, flagtransformMoveWeights: string, flagtransformValue: tuple[string, float], flagvalue: boolean, flagzeroRemainingInfluences: boolean) -> None:
    """Synopsis:
---
---
 skinPercent(
[object] [selectionList]
    , [ignoreBelow=float], [normalize=boolean], [pruneWeights=float], [relative=boolean], [resetToDefault=boolean], [transform=string], [transformMoveWeights=string], [transformValue=[string, float]], [value=boolean], [zeroRemainingInfluences=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

skinPercent is undoable, queryable, and NOT editable.
Note that setting multiple weights in a single invocation of this
command is far more efficient than calling it once per weighted
vertex.




Example:
---
import maya.cmds as cmds

Create a joint chain and a polygonal plane and bind them as skin
cmds.select(d=True)
cmds.joint(p=(-3.0, 0.0,-12.0))
cmds.joint(p=(-3.0, 0.0, -5.0))
cmds.joint(p=(1.0, 0.0, 5.5))
cmds.joint(p=(6.0, 0.0, 10.0))
cmds.polyPlane(w=20.0,h=20.0,sx=25,sy=25)
cmds.skinCluster( 'joint1', 'pPlane1' )

For vtx[100], set the weight wrt joint1 to 0.2, the weight
wrt joint3 to 0.8 and adjust the remaining weights to keep
the overall weight normalized (i.e. set all other joints to zero,
since the weights we are setting sum to 1.0)
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', transformValue=[('joint1', 0.2), ('joint3', 0.8)])

Get the weight values corresponding to all of the influences
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', query=True, value=True )

Get the weight values that are above 0.5
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', ignoreBelow=0.5, query=True, value=True )

Get the weight of vtx[100] corresponding to joint3
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', transform='joint3', query=True )

Get the names of the joints influencing vtx[100]
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', transform=None, query=True )

Normalize the existing weights for vtx[100]
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', normalize=True )

Reset the weights for vtx[100] to their default values
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', resetToDefault=True )

Zero all the weights that are below 0.1
---

cmds.skinPercent( 'skinCluster1', 'pPlane1', pruneWeights=0.1 )

Zero all the weights
---

cmds.skinPercent( 'skinCluster1', 'pPlane1', pruneWeights=100, normalize=False )

Assign weights to a large number of vertices,
several at a time to reduce the number of calls
to the skinPercent command.
---

for i in range(0,675,10):
   cmds.select('pPlane1.vtx[%i]' % i,'pPlane1.vtx[%i]' % (i+1), 'pPlane1.vtx[%i]' % (i+2), 'pPlane1.vtx[%i]' % (i+3), 'pPlane1.vtx[%i]' % (i+4), 'pPlane1.vtx[%i]' % (i+5), 'pPlane1.vtx[%i]' % (i+6), 'pPlane1.vtx[%i]' % (i+7), 'pPlane1.vtx[%i]' % (i+8), 'pPlane1.vtx[%i]' % (i+9))
   cmds.skinPercent( 'skinCluster1',transformValue=[('joint1', 0.5),('joint2', 0.5)] )

---


Flags:
---


---
ignoreBelow(ib): float
    properties: query
    Limits the output of the -value and -transform queries
to the entries whose weight values are over the specified
limit.  This flag has to be used before the -query flag.
      In query mode, this flag needs a value.

---
normalize(nrm): boolean
    properties: create
    If set, the weights not assigned by the -transformValue
flag are normalized so that the sum of the all weights
for the selected object component add up to 1. The default
is on. NOTE: The skinCluster has a normalizeWeights attribute
which when set to OFF overrides this attribute! If the
skinCluster.normalizeWeights attribute is OFF, you must
set it to Interactive in order to normalize weights using the
skinPercent command.

---
pruneWeights(prw): float
    properties: create
    Sets to zero any weight smaller than the given value for
all the selected components. To use this command to set
all the weights to zero, you must turn the -normalize flag
"off" or the skinCluster node will normalize the weights
to sum to one after pruning them. Weights for influences with
a true value on their "Hold Weights" attribute will not
be pruned.

---
relative(r): boolean
    properties: create
    Used with -transformValue to specify a relative setting of values.
If -relative is true, the value passed to -tv is added to the
previous value.  Otherwise, it replaces the previous value.

---
resetToDefault(rtd): boolean
    properties: create
    Sets the weights of the selected components to their
default values, overwriting any custom weights.

---
transform(t): string
    properties: query
    In Mel, when used after the -query flag (without an argument)
the command returns an array of strings corresponding to
the names of the transforms influencing the selected object
components.  If used before the -query flag (with a
transform name), the command returns the weight of the
selected object component corresponding to the given
transform. The command will return an average weight if several
components have been selected.

In Python, when used with None instead of the name of the transform,
the command returns an array of strings corresponding to
the names of the transforms influencing the selected object
components. If used with a transform name, the command returns the weight of the
selected object. The command will return an average weight if several
components have been selected.

      In query mode, this flag can accept a value.

---
transformMoveWeights(tmw): string
    properties: create, multiuse
    This flag is used to transfer weights from a source influence to one or more target influences. It acts on the selected vertices. The flag must be used at least twice to generate a valid command. The first flag usage indicates the source influence from which the weights will be copied. Subsequent flag usages indicate the target influences.

---
transformValue(tv): [string, float]
    properties: create, multiuse
    Accepts a pair consisting of a transform name and a value
and assigns that value as the weight of the selected
object components corresponding to the given transform.

---
value(v): boolean
    properties: query
    Returns an array of doubles corresponding to the
joint weights for the selected object component.

---
zeroRemainingInfluences(zri): boolean
    properties: create
    If set, the weights not assigned by the -transformValue
flag are set to 0. The default is off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/skinPercent.html 
    """


def smoothCurve(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagreplaceOriginal: boolean, flagsmoothness: float) -> list[string]:
    """Synopsis:
---
---
 smoothCurve(
selectionList
    , [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean], [replaceOriginal=boolean], [smoothness=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

smoothCurve is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

---
Create a curve, then smooth it
cmds.curve(p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)], n='curve1')
cmds.smoothCurve('curve1.cv[*]', s=10)

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
smoothness(s): float
    properties: create, query, edit
    smoothness factor
Default: 10.0

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/smoothCurve.html 
    """


def smoothTangentSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagdirection: int, flagname: string, flagnodeState: int, flagobject: boolean, flagparameter: float, flagreplaceOriginal: boolean, flagsmoothness: int) -> list[string]:
    """Synopsis:
---
---
 smoothTangentSurface(
surface
    , [caching=boolean], [constructionHistory=boolean], [direction=int], [name=string], [nodeState=int], [object=boolean], [parameter=float], [replaceOriginal=boolean], [smoothness=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

smoothTangentSurface is undoable, queryable, and editable.
Note: A single smoothTangentSurface command cannot smooth in both directions
at once; you must use two separate commands to do this.




Example:
---
import maya.cmds as cmds

cmds.smoothTangentSurface( 'surface1', ch=True, p=0.3, d=0 )
cmds.smoothTangentSurface( 'surface1.v[0.3]', ch=True )
Smoothes surface1 along parameter value v = 0.3. When the
isoparm is specified, the direction and parameter value is
implied and the "p" and "d" flags can be omitted.

cmds.smoothTangentSurface( 'surface1', ch= True, p= (0.3, 0.5, 0.8), nk=2, d=0 )
Smoothes along parameter values v = 0.3, 0.5 and 0.8.

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
direction(d): int
    properties: create, query, edit
    Direction in which to smooth knot:
0 - V direction,
1 - U direction
Default: 1

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
parameter(p): float
    properties: create, query, edit, multiuse
    Parameter value(s) where knots are added
Default: 0.0

---
smoothness(s): int
    properties: create, query, edit
    Smoothness to get:
0 - Tangent,
1 - Maximum (based on the degree)
Default: 1

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/smoothTangentSurface.html 
    """


def snapKey(flaganimation: string, flagattribute: string, flagcontrolPoints: boolean, flagfloat: floatrange, flaghierarchy: string, flagincludeUpperBound: boolean, flagindex: uint, flagmergeDuplicate: boolean, flagshape: boolean, flagtime: timerange, flagtimeMultiple: float, flagvalueMultiple: float) -> int:
    """Synopsis:
---
---
 snapKey(
animatedObject
    , [animation=string], [attribute=string], [controlPoints=boolean], [float=floatrange], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [mergeDuplicate=boolean], [shape=boolean], [time=timerange], [timeMultiple=float], [valueMultiple=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

snapKey is undoable, NOT queryable, and NOT editable.
The animation curves comprising a keyset depend on the value
of the "-animation" flag:


keysOrObjects:

Any active keys, when no target objects or -attribute
flags appear on the command line, or

All animation curves connected to all keyframable
attributes of objects specified as the command line's
targetList, when there are no active keys.




keys:
Only act on active keys or tangents.
If there are no active keys or tangents, don't do anything.



objects:
Only act on specified objects.  If there are no objects specified, don't
do anything.



Note that the "-animation" flag can be used to override
the curves uniquely identified by the multi-use
"-attribute" flag, which takes an argument of the form
attributeName, such as "translateX".

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given individually or as part of a list or range (see Examples).

This command "snaps" all target key times and/or values
so that they have times and/or values that are multiples
of the specified flag arguments.  If neither multiple is
specified, default is time snapping with a multiple of 1.0.
Note that this command will fail to move keys over other
neighboring keys: a key's index will not change as a result
of a snapKey operation.

TbaseKeySetCmd.h




Example:
---
import maya.cmds as cmds

Keys on animation curves are identified by either
their time values or their indices.  Times and indices can
be given as a range or list of ranges.

time=('10pal','10pal') means the key at frame 10 (PAL format).
time=[('1.0sec','1.0sec'),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
time=(10,None) means all keys from time 10 (in the current time unit) onwards.
time=(10,) means the same as (10,10)
time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
time=(None,None) is a short form to specify all keys.
index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.

Two ways to snap all keys on nurbsSphere1 to integer values.
---

cmds.snapKey( 'nurbsSphere1', tm=1.0 )
cmds.snapKey( 'nurbsSphere1' )

Snap active objects' keys between times 10 and 20 so that
they have times that are multiples of 0.5.
---

cmds.snapKey( t=(10,20), tm=0.5 )

Snap active objects' keys between times 10 and 20 so that
they have times that are multiples of 0.5 and values that
are multiples of 1.0.
---

cmds.snapKey( t=(10,20), tm=0.5, vm=1.0 )

---
Return:
---


    int: Number of animation curves
with keys that were not snapped because of time-snapping
conflicts.

Flags:
---


---
animation(an): string
    properties: create
    Where this command should get the animation to act
on.  Valid values are "objects," "keys," and
"keysOrObjects" Default: "keysOrObjects."  (See
Description for details.)

---
attribute(at): string
    properties: create, multiuse
    List of attributes to select
      In query mode, this flag needs a value.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
float(f): floatrange
    properties: create, multiuse
    value uniquely representing a non-time-based
key (or key range) on a time-based animCurve.  Valid
floatRange include single values (-f 10) or a
string with a lower and upper bound, separated by a
colon (-f "10:20")
      In query mode, this flag needs a value.

---
hierarchy(hi): string
    properties: create
    Hierarchy expansion options.  Valid values are "above,"
"below," "both," and "none." (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
includeUpperBound(iub): boolean
    properties: create
    When the -t/time or -f/float flags represent a range
of keys, this flag determines whether the keys at the
upper bound of the range are included in the keyset.
Default value: true.  This flag is only valid when
the argument to the -t/time flag is a time range with
a lower and upper bound.  (When used with the "pasteKey"
command, this flag refers only to the time range of the
target curve that is replaced, when using options such
as "replace," "fitReplace," or "scaleReplace."  This
flag has no effect on the curve pasted from the clipboard.)

---
index(index): uint
    properties: create, multiuse
    index of a key on an animCurve
      In query mode, this flag needs a value.

---
mergeDuplicate(md): boolean
    properties: create
    If this flag is present, keys with duplicated frame will be merged into 1.
Default false

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

---
timeMultiple(tm): float
    properties: create
    If this flag is present, key times will be snapped
to a multiple of the specified float value.

---
valueMultiple(vm): float
    properties: create
    If this flag is present, key values will be snapped
to a multiple of the specified float value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/snapKey.html 
    """


def snapMode(flagcurve: boolean, flagdistanceIncrement: linear, flagedgeMagnet: uint, flagedgeMagnetTolerance: float, flaggrid: boolean, flagliveFaceCenter: boolean, flaglivePoint: boolean, flagmeshCenter: boolean, flagpixelCenter: boolean, flagpixelSnap: boolean, flagpoint: boolean, flagtolerance: uint, flaguseTolerance: boolean, flaguvTolerance: uint, flagviewPlane: boolean) -> boolean:
    """Synopsis:
---
---
 snapMode([curve=boolean], [distanceIncrement=linear], [edgeMagnet=uint], [edgeMagnetTolerance=float], [grid=boolean], [liveFaceCenter=boolean], [livePoint=boolean], [meshCenter=boolean], [pixelCenter=boolean], [pixelSnap=boolean], [point=boolean], [tolerance=uint], [useTolerance=boolean], [uvTolerance=uint], [viewPlane=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

snapMode is undoable, queryable, and NOT editable.




Example:
---
import maya.cmds as cmds

Turn curve snapping on
cmds.snapMode( curve=True )

Returns true if point snapping is on
cmds.snapMode( q=True, point=True )

---
Return:
---


    boolean: if command is a query

Flags:
---


---
curve(c): boolean
    properties: create, query
    Set curve snap mode

---
distanceIncrement(dsi): linear
    properties: create, query
    Set the distance for the snapping to objects such as a lines or planes.

---
edgeMagnet(em): uint
    properties: create, query
    Number of extra magnets to snap onto, regularly spaced
along the edge.

---
edgeMagnetTolerance(emt): float
    properties: create, query
    Precision for edge magnet snapping.

---
grid(gr): boolean
    properties: create, query
    Set grid snap mode

---
liveFaceCenter(lfc): boolean
    properties: create, query
    While moving on live polygon objects, snap to its
face centers.

---
livePoint(lp): boolean
    properties: create, query
    While moving on live polygon objects, snap to its
vertices.

---
meshCenter(mc): boolean
    properties: create, query
    While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.

---
pixelCenter(pc): boolean
    properties: create, query
    Snap UV to the center of the pixel instead of the corner.

---
pixelSnap(ps): boolean
    properties: create, query
    Snap UVs to the nearest pixel center or corner.

---
point(p): boolean
    properties: create, query
    Set point snap mode

---
tolerance(t): uint
    properties: create, query
    Tolerance defines the size of the square region
in which points must lie in order to be snapped to. The
tolerance value is the distance from the cursor position
to the boundary of the square (in all four directions).

---
useTolerance(ut): boolean
    properties: create, query
    If useTolerance is set, then point snapping
is limited to points that are within a square region
surrounding the cursor position. The size of the square
is determined by the tolerance value.

---
uvTolerance(uvt): uint
    properties: create, query
    uvTolerance defines the size of the square region
in which points must lie in order to be snapped to, in the
UV Editor.  The tolerance value is the distance
from the cursor position to the boundary of the square
(in all four directions).

---
viewPlane(vp): boolean
    properties: create, query
    Set view-plane snap mode

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/snapMode.html 
    """


def snapTogetherCtx(flagclearSelection: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagsetOrientation: boolean, flagsnapPolygonFace: boolean) -> string:
    """Synopsis:
---
---
 snapTogetherCtx(
[contextName]
    , [clearSelection=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [setOrientation=boolean], [snapPolygonFace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

snapTogetherCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create two nurbs spheres, then move them apart
cmds.sphere(r=3, n='nurbsSphere1')
cmds.move(5, 0, 0)
cmds.sphere(r=3, n='nurbsSphere2')
cmds.move(-5, 0, 0)

Create a new snap together tool context, set it to move objects only, then switch to it
You can use this tool to snap two spheres together
cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
cmds.setToolTo('snapTogetherCtx1')

---
Return:
---


    string: (name of the new context)

Flags:
---


---
clearSelection(cs): boolean
    properties: create, query, edit
    Sets whether the tool should clear the selection
on entry to the tool. Default true.

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
setOrientation(so): boolean
    properties: create, query, edit
    Sets whether the tool should orient as well as moving
an item. Default true.

---
snapPolygonFace(spf): boolean
    properties: create, query, edit
    Sets whether the tool should snap the cursor to
polygon face centers. Default false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/snapTogetherCtx.html 
    """


def snapshot(flagconstructionHistory: boolean, flagendTime: time, flagincrement: time, flagmotionTrail: boolean, flagname: string, flagstartTime: time, flagupdate: string) -> list[string]:
    """Synopsis:
---
---
 snapshot(
[objects]
    , [constructionHistory=boolean], [endTime=time], [increment=time], [motionTrail=boolean], [name=string], [startTime=time], [update=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

snapshot is undoable, queryable, and editable.

If the constructionHistory flag is true, the output shapes or motion trail
will re-update when modifications are made to the animation or construction
history of the original shape. When construction history is used, the forceUpdate
flag can be set to false to control when the snapshot recomputes, which will
typically improve performance.




Example:
---
import maya.cmds as cmds

animate a sphere
cmds.sphere(n='sphere1')
cmds.currentTime('0')
cmds.setKeyframe('.t')
cmds.currentTime('30')
cmds.move(10,0,1)
cmds.setKeyframe('.t')

Evaluate and display "sphere1" as it appears
at times 0, 10, 20, and 30.  Modifications to sphere1
will update the copies.
---

cmds.snapshot( 'sphere1', constructionHistory=True, startTime=0, endTime=30, increment=10 )

Evaluate and display "sphere1" as it appears
at times 0, 10, 20, and 30.  Further modifications to sphere1
should have no affect on the copies since constructionHistory is off.
---

cmds.snapshot( 'sphere1', constructionHistory=False, startTime=0, endTime=30, increment=10 )

---
Return:
---


    list[string]: names of nodes created or edited: transform-name [snapshot-node-name]

Flags:
---


---
constructionHistory(ch): boolean
    properties: create, query
    update with changes to original geometry

---
endTime(et): time
    properties: create, query, edit
    time to stop copying target geometry
Default: 10.0

---
increment(i): time
    properties: create, query, edit
    time increment between copies
Default: 1.0

---
motionTrail(mt): boolean
    properties: create
    Rather than create a series of surfaces, create a motion trail
displaying the location of the object's pivot point at the
specified time steps. Default is false.

---
name(n): string
    properties: create, query, edit
    the name of the snapshot node. Query returns string.

---
startTime(st): time
    properties: create, query, edit
    time to begin copying target geometry
Default: 1.0

---
update(u): string
    properties: create, query, edit
    This flag can only be used if the snapshot has
constructionHistory. It sets the snapshot node's update
value. The update value controls whether the snapshot updates
on demand (most efficient), when keyframes change (efficient),
or whenever any history changes (least efficient). Valid values
are "demand", "animCurve", "always".
Default: "always"

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/snapshot.html 
    """


def snapshotBeadCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaginTangent: boolean, flagname: string, flagoutTangent: boolean) -> string:
    """Synopsis:
---
---
 snapshotBeadCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [inTangent=boolean], [name=string], [outTangent=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

snapshotBeadCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a snapshot bead context that will show in tangents
ctx = cmds.snapshotBeadCtx(inTangent = True)
cmds.setToolTo(ctx)

---
Return:
---


    string: (name of the new context)

Flags:
---


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
inTangent(i): boolean
    properties: query, edit
    Indicates that we will be showing beads for the in tangent when
entering the context

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
outTangent(o): boolean
    properties: query, edit
    Indicates that we will be showing beads for the out tangent when
entering the context

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/snapshotBeadCtx.html 
    """


def snapshotModifyKeyCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 snapshotModifyKeyCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

snapshotModifyKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create an insert key context
ctx = cmds.snapshotModifyKeyCtx()
cmds.setToolTo(ctx)

---
Return:
---


    string: (name of the new context)

Flags:
---


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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/snapshotModifyKeyCtx.html 
    """


def soft(flagconvert: boolean, flagduplicate: boolean, flagduplicateHistory: boolean, flaggoal: float, flaghideOriginal: boolean, flagname: string) -> string:
    """Synopsis:
---
---
 soft(
selectionList
    , [convert=boolean], [duplicate=boolean], [duplicateHistory=boolean], [goal=float], [hideOriginal=boolean], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

soft is undoable, queryable, and NOT editable.

            T    
            / \  
           T   G 
          /      
        P        


Dynamics are applied to the particle shape and the resulting particle
positions then drive the locations of the geometry's CVs, vertices, or
lattice points.

With the convert option, the particle shape and its transform are simply
inserted below the original shape's hierarchy.
With the duplicate option, the original geometry's transform and shape are
duplicated underneath its parent, and the particle shape is placed under
the duplicate.  Note that any animation on
the hierarchy will affect the particle shape as well.  If you do not want
then, then reparent the structure outside the hierarchy.

When duplicating, the soft portion (the duplicate) is given the name
"copyOf" + "original object name".  The particle portion is always
given the name "original object name" + "Particles."

None of the flags of the soft command can be queried.  The soft -q
command is used only to identify when an object is a soft body,
or when two objects are part of the same soft body.
See the examples.




Example:
---
import maya.cmds as cmds

cmds.sphere()
cmds.soft( 'nurbsSphere1', c=True )

Creates a sphere named nurbsSphere1 and converts nurbSphere1 into
a soft object.  The particle portion of the soft object will
be parented (with its own transform) under nurbsSphere1.

cmds.sphere()
cmds.soft( 'nurbsSphere1', d=True )

Same as the previous example, except that the soft command will make
a duplicate of nurbsSphereShape1.  The resulting soft body will be
completely independent of nurbSphere1 and its children.  Input connections
to nurbsSphereShape1 will be duplicated, but not any upstream history
(in other words, just plain "duplicate").

cmds.sphere()
cmds.soft( 'nurbsSphere1', dh=True )

Same as the previous example, except that upstream history on
nurbsSphereShape1 will be duplicated as well (equivalent to
"duplicate history").

cmds.sphere()
cmds.soft( 'nurbSphere1', g=0.3 )

This will make a duplicate of the shape under nurbSphere1 (as for -d),
and  use it as the shape for the newly created soft object.
The original nurbsSphereShape1 will be made a goal for the particles of
softy, with a goal weight of 0.3.  This will make those particles try to
follow nurbSphere1 loosely as it moves around.

cmds.soft( 'foobar', q=True )
Returns true if foobar is a soft object.

cmds.soft( 'foobar', 'foobarParticles', q=True )

Returns true if foobar and foobarParticles are parts of the same
soft object.  This is useful because when you select a soft body,
both the overall transform and the particle transform get put into
the selection list.

---
Return:
---


    string: array

Flags:
---


---
convert(c): boolean
    properties: create
    This tells the command that you want the original object
to be the actual deformed object.  The particle shape portion of the
soft body will be inserted in the same hierarchy as the original,
under the same parent (with one additional intervening transform
which is initially the identity).  If no flags are passed, then this
is assumed.  The combination -c -h 1 is not valid; if you have
this in your scripts, remove the -h 1.

---
duplicate(d): boolean
    properties: create
    This tells the command that you want to make a copy of
the original object and use the copy as the deforming geometry.
Input connections to the original object are duplicated.  You would
do this if you wanted to keep the original object in your scene and
also have a copy of it that was a soft body.
This flag and -dh are mutually exclusive.

---
duplicateHistory(dh): boolean
    properties: create
    This is the same as -d, except that upstream history,
is duplicated as well, instead of just input connections.
This flag and -d are mutually exclusive.

---
goal(g): float
    properties: create
    This is the same as -d, but in addition it tells the command that
you want the resulting soft body to try to
follow the original geometry, using the set goal weight as the value
that controls how strongly it is to follow it.  A value of 1.0 will
try to follow exactly, and a value of 0.0 will not follow at all.
The default value is 0.5.  This value must be from 0.0 to 1.0.
You could use -d with -g, but it is redundant.  If you want history to
be duplicated, you can use -dh and -g together.

---
hideOriginal(h): boolean
    properties: create
    This flag is used only when duplicating (-d, -g, or -dh).  If set to true,
whichever of the two objects is NOT the soft object will be hidden.
In other words, with -d -h true, the original object will be hidden;
with -d -c -h 1 the duplicate object will be hidden.
You would typically do this if you want to use the non-dynamic object as
a goal for the soft one (see -g) but you do not want it visible in the scene.
The flags -h 1 and -c are mutually exclusive.

---
name(n): string
    properties: 
    This flag is obsolete.  If you wish to give your new soft object a name,
use the rename command (or from the UI, use the outliner).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/soft.html 
    """


def softMod(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagbindState: boolean, flagcomponents: boolean, flagcurveInterpolation: int, flagcurvePoint: float, flagcurveValue: float, flagdeformerTools: boolean, flagenvelope: float, flagexclusive: string, flagfalloffAroundSelection: boolean, flagfalloffBasedOnX: boolean, flagfalloffBasedOnY: boolean, flagfalloffBasedOnZ: boolean, flagfalloffCenter: tuple[float, float, float], flagfalloffMasking: boolean, flagfalloffMode: int, flagfalloffRadius: float, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flagname: string, flagparallel: boolean, flagprune: boolean, flagrelative: boolean, flagremove: boolean, flagresetGeometry: boolean, flagselectedComponents: boolean, flagsplit: boolean, flaguseComponentTags: boolean, flagweightedNode: tuple[string, string]) -> string:
    """Synopsis:
---
---
 softMod(
[objects]
    , [after=boolean], [afterReference=boolean], [before=boolean], [bindState=boolean], [components=boolean], [curveInterpolation=int], [curvePoint=float], [curveValue=float], [deformerTools=boolean], [envelope=float], [exclusive=string], [falloffAroundSelection=boolean], [falloffBasedOnX=boolean], [falloffBasedOnY=boolean], [falloffBasedOnZ=boolean], [falloffCenter=[float, float, float]], [falloffMasking=boolean], [falloffMode=int], [falloffRadius=float], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string], [parallel=boolean], [prune=boolean], [relative=boolean], [remove=boolean], [resetGeometry=boolean], [selectedComponents=boolean], [split=boolean], [useComponentTags=boolean], [weightedNode=[string, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

softMod is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a softMod which uses the transformation of elbow1
---

cmds.joint(p=(2,0,0),name="elbow1")
cmds.joint(p=(4,0,0),name="wrist1")

cmds.sphere()
cmds.softMod( wn=('elbow1', 'elbow1') )

Edit softMod1 to use the transformation of wrist1.
---

cmds.softMod( 'softMod1', e=True, wn=('wrist1', 'wrist1') )

Create a relative softMod with its own softMod handle. The
softMod handle is drawn as the letter "S".
---

cmds.polyCube();
cmds.softMod( rel=True )

Modify the membership of an existing softMod. First, find
the name of the softMod's associated set, then use the sets
command to edit the set membership (add a cube and remove a plane).
---

cmds.listConnections( 'softMod1', type='objectSet' )
Result:[u'softMod1Set'] ---

cmds.sets( 'pCube2', add='softMod1Set' )
cmds.sets( 'pCube1', rm='softMod1Set' )

---
Return:
---


    string: [] (the softMod node name and the softMod handle name)

Flags:
---


---
after(af): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node after the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
afterReference(ar): boolean
    properties: create, edit
    The -afterReference flag is used to specify deformer ordering in a hybrid way that
choses between -before and -after automatically. If the geometry being
deformed is referenced then the -after mode is used when adding the new deformer,
otherwise the -before mode is used. The net effect when using -afterReference to build
deformer chains is that internal shape nodes in the deformer chain will only
appear at reference file boundaries, leading to lightweight deformer networks that
may be more amicable to reference swapping.

---
before(bf): boolean
    properties: create, edit
    If the default behavior for insertion/appending into/onto
the existing chain is not the desired behavior then this flag
can be used to force the command to place the deformer
node before the selected node in the chain even if
a new geometry shape has to be created in order to do so.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
bindState(bs): boolean
    properties: create
    Specifying this flag adds in a compensation to ensure
the softModed objects preserve their spatial position
when softModed. This is required to prevent the geometry
from jumping at the time the softMod is created
in situations when the
softMod transforms at softMod time are not identity.

---
components(cmp): boolean
    properties: query
    Returns the components used by the deformer

---
curveInterpolation(ci): int
    properties: create, multiuse
    Ramp interpolation corresponding to the specified curvePoint position.
Integer values of 0-3 are valid, corresponding to "none", "linear", "smooth"
and "spline" respectively.
This flag may only be used in conjunction with the curvePoint and curveValue
flag.

---
curvePoint(cp): float
    properties: create, multiuse
    Position of ramp value on normalized 0-1 scale.
This flag may only be used in conjunction with the curveInterpolation and
curveValue flags.

---
curveValue(cv): float
    properties: create, multiuse
    Ramp value corresponding to the specified curvePoint position. This flag
may only be used in conjunction with the curveInterpolation and curvePoint
flags.

---
deformerTools(dt): boolean
    properties: query
    Returns the name of the deformer tool objects (if any)
as string string ...

---
envelope(en): float
    properties: create, query, edit
    Set the envelope value for the deformer. Default is 1.0

---
exclusive(ex): string
    properties: create, query
    Puts the deformation set in a deform partition.

---
falloffAroundSelection(fas): boolean
    properties: create
    Falloff will be calculated around any selected components

---
falloffBasedOnX(fbx): boolean
    properties: create
    Falloff will be calculated using the X component.

---
falloffBasedOnY(fby): boolean
    properties: create
    Falloff will be calculated using the Y component.

---
falloffBasedOnZ(fbz): boolean
    properties: create
    Falloff will be calculated using the Z component.

---
falloffCenter(fc): [float, float, float]
    properties: create
    Set the falloff center point of the softMod.

---
falloffMasking(fm): boolean
    properties: create
    Deformation will be restricted to selected components

---
falloffMode(fom): int
    properties: create
    Set the falloff method used for the softMod.

---
falloffRadius(fr): float
    properties: create
    Set the falloff radius of the softMod.

---
frontOfChain(foc): boolean
    properties: create, edit
    This command is used to specify that the new deformer
node should be placed ahead (upstream) of existing deformer
and skin nodes in the shape's history (but not ahead of
existing tweak nodes). The input to the
deformer will be the upstream shape rather than the visible
downstream shape, so the behavior of this flag is the most
intuitive if the downstream deformers are in their reset
(hasNoEffect) position when the new deformer is added.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
geometry(g): string
    properties: query, edit, multiuse
    The specified object will be added to the list of
objects being deformed by this deformer object, unless
the -rm flag is also specified. When queried, this flag
returns string string string ...

---
geometryIndices(gi): boolean
    properties: query
    Complements the -geometry flag in query mode. Returns
the multi index of each geometry.

---
ignoreSelected(ignoreSelected): boolean
    properties: create
    Tells the command to not deform objects on the
current selection list

---
includeHiddenSelections(ihs): boolean
    properties: create
    Apply the deformer to any visible and hidden objects in the selection list.
Default is false.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
prune(pr): boolean
    properties: edit
    Removes any points not being deformed by the deformer in
its current configuration from the deformer set.

---
relative(rel): boolean
    properties: create
    Enable relative mode for the softMod. In relative mode,
Only the transformations directly above the softMod are used
by the softMod. Default is off.

---
remove(rm): boolean
    properties: edit, multiuse
    Specifies that objects listed after the -g flag should
be removed from this deformer.

---
resetGeometry(rg): boolean
    properties: edit
    Reset the geometry matrices for the objects being deformed
by the softMod. This flag is used to get rid of undesirable
effects that happen if you scale an object that
is deformed by a softMod.

---
selectedComponents(cms): boolean
    properties: query
    Returns the components used by the deformer that are currently selected.
This intersects the current selection with the components affected by the deformer.

---
split(sp): boolean
    properties: create, edit
    Branches off a new chain in the dependency graph instead
of inserting/appending the deformer into/onto an
existing chain.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

---
weightedNode(wn): [string, string]
    properties: create, query, edit
    Transform node in the DAG above the softMod to which all percents are
applied. The second node specifies the descendent of the first node
from where the transformation matrix is evaluated. Default is the
softMod handle.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/softMod.html 
    """


def softModCtx(flagdragSlider: string, flagexists: boolean, flagfalseColor: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagreset: boolean) -> string:
    """Synopsis:
---
---
 softModCtx(
string
    , [dragSlider=string], [exists=boolean], [falseColor=boolean], [image1=string], [image2=string], [image3=string], [reset=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

softModCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.softModCtx()

---
Return:
---


    string: - name of the new context created

Flags:
---


---
dragSlider(ds): string
    properties: edit
    Specify the slider mode for hotkey radius resizing.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
falseColor(fc): boolean
    properties: edit
    Enable or disable false color display on the soft mod manipulator.

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
reset(rst): boolean
    properties: query, edit
    Reset the tool options to their default values.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/softModCtx.html 
    """


def softSelect(flagcompressUndo: int, flagenableFalseColor: int, flagsoftSelectColorCurve: string, flagsoftSelectCurve: string, flagsoftSelectDistance: float, flagsoftSelectEnabled: int, flagsoftSelectFalloff: int, flagsoftSelectReset: boolean, flagsoftSelectUVDistance: float) -> None:
    """Synopsis:
---
---
 softSelect([compressUndo=int], [enableFalseColor=int], [softSelectColorCurve=string], [softSelectCurve=string], [softSelectDistance=float], [softSelectEnabled=int], [softSelectFalloff=int], [softSelectReset=boolean], [softSelectUVDistance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

softSelect is undoable, queryable, and editable.
Soft modelling is an option that allows for reflection of basic
manipulator actions such as move, rotate, and scale.




Example:
---
import maya.cmds as cmds

Enable soft selection
cmds.softSelect(sse=1)

Setup global soft select with radius and curve
cmds.softSelect(sse=1,ssd=2.0,ssc='0,1,2,1,0,2',ssf=2)

---


Flags:
---


---
compressUndo(cu): int
    properties: create, query, edit
    Controls how soft selection settings behave in undo:

0 means all changes undo individually
1 means all consecutive changes undo as a group
2 means only interactive changes undo as a group

When queried, returns an int indicating the current undo behaviour.

---
enableFalseColor(efc): int
    properties: create, query, edit
    Set soft select color feedback on or off.
When queried, returns an int indicating whether color feedback
is currently enabled.

---
softSelectColorCurve(scc): string
    properties: create, query, edit
    Sets the color ramp used to display false color feedback for soft selected
components in the viewport. The color curve is encoded as a string of comma
separated floating point values representing the falloff curve CVs. Each
CV is represented by 5 successive values: 3 RGB values (the color to use),
an input value (the selection weight), and a curve interpolation type.
When queried, returns a string containing the encoded CVs of the current
color feedback curve.

---
softSelectCurve(ssc): string
    properties: create, query, edit
    Sets the falloff curve used to calculate selection weights for components
within the falloff distance. The curve is encoded as a string of comma
separated floating point values representing the falloff curve CVs. Each
CV is represented by 3 successive values: an output value (the selection
weight at this point), an input value (the normalised falloff distance)
and a curve interpolation type.
When queried, returns a string containing the encoded CVs of the current
falloff curve.

---
softSelectDistance(ssd): float
    properties: create, query, edit
    Sets the falloff distance (radius) used for world and object space soft selection.
When queried, returns a float indicating the current falloff distance.

---
softSelectEnabled(sse): int
    properties: create, query, edit
    Sets soft selection based modeling on or off.
When queried, returns an int indicating the current state of the option.

---
softSelectFalloff(ssf): int
    properties: create, query, edit
    Sets the falloff mode:

0 for volume based falloff
1 for surface based falloff
2 for global falloff

When queried, returns an int indicating the falloff mode.

---
softSelectReset(ssr): boolean
    properties: create, edit
    Resets soft selection to its default settings.

---
softSelectUVDistance(sud): float
    properties: create, query, edit
    Sets the falloff distance (radius) used for UV space soft selection.
When queried, returns a float indicating the current falloff distance.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/softSelect.html 
    """


def soloMaterial(flagattr: string, flaglast: boolean, flagnode: string, flagunsolo: boolean) -> boolean:
    """Synopsis:
---
---
 soloMaterial([attr=string], [last=boolean], [node=string], [unsolo=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

soloMaterial is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.soloMaterial( node="file1", attr="outAlpha" )
cmds.soloMaterial( unsolo=True )
cmds.soloMaterial( last=True )

---
Return:
---


    boolean: Success or Failure

Flags:
---


---
attr(a): string
    properties: create, query
    The attr flag specifies a node attribute to solo.

---
last(l): boolean
    properties: create, query
    Whether to solo the last material node and attribute.

---
node(n): string
    properties: create, query
    The node flag specifies the node to solo.

---
unsolo(us): boolean
    properties: create, query
    Whether to remove soloing.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/soloMaterial.html 
    """


def sortCaseInsensitive() -> list[string]:
    """Synopsis:
---
---
 sortCaseInsensitive()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sortCaseInsensitive is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.sortCaseInsensitive( stringArray );
Returns the sorted string from stringArray

---
Return:
---


    list[string]: string to sort

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sortCaseInsensitive.html 
    """


def sound(flagendTime: time, flagfile: string, flaglength: boolean, flagmute: boolean, flagname: string, flagoffset: time, flagsourceEnd: time, flagsourceStart: time) -> string:
    """Synopsis:
---
---
 sound(
[objects]
    , [endTime=time], [file=string], [length=boolean], [mute=boolean], [name=string], [offset=time], [sourceEnd=time], [sourceStart=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sound is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create an audio node for a sound file, and have it
start at time 10.  This command will return the name
of the created node, something like "audio1".
---

cmds.sound( offset=10, file='ohNo.aiff' )

In order to have this sound displayed in a
timeControl widget (like the timeSlider) use a
command like this one, where the global MEL variable
$gPlayBackSlider is the name of the widget to display
the sound in.
---

import maya.mel
gPlayBackSlider = maya.mel.eval( '$tmpVar=$gPlayBackSlider' )
cmds.timeControl( gPlayBackSlider, edit=True, sound='audio1' )

---
Return:
---


    string: Name of resulting audio node

Flags:
---


---
endTime(et): time
    properties: create, query, edit
    Time at which to end the sound.

---
file(f): string
    properties: create, query, edit
    Name of sound file.

---
length(l): boolean
    properties: query
    Query the length (in the current time unit) of the sound.

---
mute(m): boolean
    properties: create, query, edit
    Mute the audio clip.

---
name(n): string
    properties: create, query, edit
    Name to give the resulting audio node.

---
offset(o): time
    properties: create, query, edit
    Time at which to start the sound.

---
sourceEnd(se): time
    properties: create, query, edit
    Time offset from the start of the sound file at which to end the sound.

---
sourceStart(ss): time
    properties: create, query, edit
    Time offset from the start of the sound file at which to start the sound.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sound.html 
    """


def soundControl(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagbeginScrub: boolean, flagdefineTemplate: string, flagdisplaySound: boolean, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagendScrub: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmaxTime: time, flagminTime: time, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpressCommand: string, flagpreventOverride: boolean, flagreleaseCommand: string, flagrepeatChunkSize: float, flagrepeatOnHold: boolean, flagresample: boolean, flagsound: string, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwaveform: string, flagwidth: int) -> string:
    """Synopsis:
---
---
 soundControl(
string
    , [annotation=string], [backgroundColor=[float, float, float]], [beginScrub=boolean], [defineTemplate=string], [displaySound=boolean], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [endScrub=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [maxTime=time], [minTime=time], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [pressCommand=string], [preventOverride=boolean], [releaseCommand=string], [repeatChunkSize=float], [repeatOnHold=boolean], [resample=boolean], [sound=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [waveform=string], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

soundControl is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To display sound in a soundControl, there must first be a sound
node in the scene. We'll create one and give it the name "ohNo".
Note that the argument to the -file flag must be a path to a valid
soundfile.
---

cmds.sound( file='ohNo.aiff', name='ohNo' )

Create a sound control (named "soundScrubber")
and have it display the sound associated with audio node "ohNo".
---

cmds.window()
cmds.frameLayout( lv=False )
cmds.soundControl( 'soundScrubber', width=600, height=45, sound='ohNo', displaySound=True, waveform='both' )
cmds.showWindow()

Now setup "soundScrubber" to actually scrub with
mouse drags.
---

pressCmd = "soundControl -e -beginScrub soundScrubber"
releaseCmd = "soundControl -e -endScrub soundScrubber"
cmds.soundControl( 'soundScrubber', e=True, pc=cmds.soundControl('soundScrubber',e=True,beginScrub=True, rc=cmds.sound('soundScrubber',e=True,endScrub=True)))

---
Return:
---


    string: Name of created or edited control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
beginScrub(bs): boolean
    properties: edit
    Set this widget up for sound scrubbing.
Subsequent changes to current time will result
in "sound scrubbing" behavior, until the
"-endScrub" command is issued for this widget.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
displaySound(ds): boolean
    properties: query, edit
    Turn sound display off.  Query returns int.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
endScrub(es): boolean
    properties: edit
    End sound scubbing for this widget.  This stops
sound scrubbing behavior and should be issued
before any subsequent "-beginScrub" flags

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxTime(max): time
    properties: create, query, edit
    Controls the max time of the range displayed in the control.
Query returns float.

---
minTime(min): time
    properties: create, query, edit
    Controls the min time of the range displayed in the control.
Query returns float.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
pressCommand(pc): string
    properties: create, edit
    script to run on mouse-down in this control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
releaseCommand(rc): string
    properties: create, edit
    script to run on mouse-up in this control.

---
repeatChunkSize(rcs): float
    properties: query, edit
    How much sound (in the current time unit) is repeated
when -repeatOnHold is true.  Default is 1.0.

---
repeatOnHold(roh): boolean
    properties: query, edit
    Repeat sound during mouse-down events

---
resample(r): boolean
    properties: edit
    Resample the sound display to fit the widget

---
sound(s): string
    properties: query, edit
    Name of audio depend node whose data should display in the
sound-display widget. Query returns string.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
waveform(wf): string
    properties: query, edit
    Determines what part of the sound waveform to display,
when -displaySound is "true". Valid values are "top", "bottom",
and "both".  Default is "top". Query returns string.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/soundControl.html 
    """


def soundPopup(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 soundPopup(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

soundPopup is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( adjustableColumn=True )
cmds.soundPopup()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
annotation(ann): string
    properties: create
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: create
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
isObscured(io): boolean
    properties: create
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: create
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: create
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
statusBarMessage(sbm): string
    properties: create
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/soundPopup.html 
    """


def spaceLocator(flagabsolute: boolean, flagname: string, flagposition: tuple[linear, linear, linear], flagrelative: boolean) -> list[string]:
    """Synopsis:
---
---
 spaceLocator([absolute=boolean], [name=string], [position=[linear, linear, linear]], [relative=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

spaceLocator is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Creates a space locator at (1, 1, 1).
cmds.spaceLocator( p=(1, 1, 1) )
Creates a space locator at (1, 1, 1) in inches.
cmds.spaceLocator( p=('1in', '1in', '1in') )
Creates a space locator at the default position (0, 0, 0).
cmds.spaceLocator()

---
Return:
---


    list[string]: The name for the new locator in space.

Flags:
---


---
absolute(a): boolean
    properties: create, edit
    If set, the locator's position is in world space.

---
name(n): string
    properties: create, edit
    Name for the locator.

---
position(p): [linear, linear, linear]
    properties: create, query, edit
    Location in  3-dimensional space where locator is to be created.

---
relative(r): boolean
    properties: create, edit
    If set, the locator's position is relative to its local space. The locator is created in relative mode by default.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/spaceLocator.html 
    """


def sphere(flagaxis: tuple[linear, linear, linear], flagcaching: boolean, flagconstructionHistory: boolean, flagdegree: int, flagendSweep: angle, flagheightRatio: float, flagname: string, flagnodeState: int, flagobject: boolean, flagpivot: tuple[linear, linear, linear], flagpolygon: int, flagradius: linear, flagsections: int, flagspans: int, flagstartSweep: angle, flagtolerance: linear, flaguseTolerance: boolean) -> list[string]:
    """Synopsis:
---
---
 sphere([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean], [degree=int], [endSweep=angle], [heightRatio=float], [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [radius=linear], [sections=int], [spans=int], [startSweep=angle], [tolerance=linear], [useTolerance=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sphere is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create sphere with radius 10
cmds.sphere( r=10 )

Query the radius of the new sphere
r = cmds.sphere( 'nurbsSphere1', q=True, r=True )

Create half sphere
cmds.sphere( ssw=0, esw=180 )

Use tolerance to determine how many spans the new sphere has
cmds.sphere( ut=True, tol=0.01 )

Use sections to determine how many spans the new sphere has
cmds.sphere( ut=False, s=8 )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
axis(ax): [linear, linear, linear]
    properties: create, query, edit
    The primitive's axis

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
degree(d): int
    properties: create, query, edit
    The degree of the resulting surface:
1 - linear,
3 - cubic
Default: 3

---
endSweep(esw): angle
    properties: create, query, edit
    The angle at which to end the surface of revolution.
Default is 2Pi radians, or 360 degrees.
Default: 6.2831853

---
heightRatio(hr): float
    properties: create, query, edit
    Ratio of "height" to "width"
Default: 2.0

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
pivot(p): [linear, linear, linear]
    properties: create, query, edit
    The primitive's pivot point

---
radius(r): linear
    properties: create, query, edit
    The radius of the object
Default: 1.0

---
sections(s): int
    properties: create, query, edit
    The number of sections determines the resolution of the surface in the sweep direction.
Used only if useTolerance is false.
Default: 8

---
spans(nsp): int
    properties: create, query, edit
    The number of spans determines the resolution of the surface in the opposite direction.
Default: 1

---
startSweep(ssw): angle
    properties: create, query, edit
    The angle at which to start the surface of revolution
Default: 0

---
tolerance(tol): linear
    properties: create, query, edit
    The tolerance with which to build the surface.
Used only if useTolerance is true
Default: 0.01

---
useTolerance(ut): boolean
    properties: create, query, edit
    Use the specified tolerance to determine resolution.
Otherwise number of sections will be used.
Default: false

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
polygon(po): int
    properties: create
    The value of this argument controls the type of the object
created by this operation

 0: nurbs surface
 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)
 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)
 3: Bezier surface
 4: subdivision surface solid (use nurbsToSubdivPref to set the
parameters for the conversion)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sphere.html 
    """


def spotLight(flagbarnDoors: boolean, flagbottomBarnDoorAngle: angle, flagconeAngle: angle, flagdecayRate: int, flagdiscRadius: linear, flagdropOff: float, flagexclusive: boolean, flagintensity: float, flagleftBarnDoorAngle: angle, flagname: string, flagpenumbra: angle, flagposition: tuple[linear, linear, linear], flagrgb: tuple[float, float, float], flagrightBarnDoorAngle: angle, flagrotation: tuple[angle, angle, angle], flagshadowColor: tuple[float, float, float], flagshadowDither: float, flagshadowSamples: int, flagsoftShadow: boolean, flagtopBarnDoorAngle: angle, flaguseRayTraceShadows: boolean) -> double[] | int | string:
    """Synopsis:
---
---
 spotLight([barnDoors=boolean], [bottomBarnDoorAngle=angle], [coneAngle=angle], [decayRate=int], [discRadius=linear], [dropOff=float], [exclusive=boolean], [intensity=float], [leftBarnDoorAngle=angle], [name=string], [penumbra=angle], [position=[linear, linear, linear]], [rgb=[float, float, float]], [rightBarnDoorAngle=angle], [rotation=[angle, angle, angle]], [shadowColor=[float, float, float]], [shadowDither=float], [shadowSamples=int], [softShadow=boolean], [topBarnDoorAngle=angle], [useRayTraceShadows=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

spotLight is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a spot light
light = cmds.spotLight(coneAngle=45)

Change the cone angle value
cmds.spotLight( light, e=True, coneAngle=33 )

Query it
cmds.spotLight( light, q=True, coneAngle=True )
Result:33---


---
Return:
---


    string: Light shape name
boolean Barn door enabled state
angle Left barn door angle
angle Right barn door angle
angle Top barn door angle
angle Bottom barn door angle
angle Cone angle
angle Penumbra angle
float Dropoff value
    double[]: when querying the rgb or shadowColor flags
double when querying the intensity flag
boolean when querying the useRayTraceShadows or exclusive flags
linear[] when querying the position flag
angle[] when querying the rotation flag
string when querying the name flag
    int: rate of light decay, when querying the decayRate flag
    int: Number of shadow samples, when querying the shadowSamples flag
boolean True if soft shadows are enabled, when querying the softShadow flag
float Shadow dithering value, when querying the shadowDither flag
float Disc radius value, when querying the discRadius flag

Flags:
---


---
barnDoors(bd): boolean
    properties: create, query, edit
    Are the barn doors enabled?

---
bottomBarnDoorAngle(bbd): angle
    properties: create, query, edit
    Angle of the bottom of the barn door.

---
coneAngle(ca): angle
    properties: create, query, edit
    angle of the spotLight

---
decayRate(d): int
    properties: create
    Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)

---
discRadius(drs): linear
    properties: create, query
    Radius of shadow disc.

---
dropOff(do): float
    properties: create, query, edit
    dropOff of the spotLight

---
exclusive(exc): boolean
    properties: create, query
    True if the light is exclusively assigned

---
intensity(i): float
    properties: create, query
    Intensity of the light

---
leftBarnDoorAngle(lbd): angle
    properties: create, query, edit
    Angle of the left of the barn door.

---
name(n): string
    properties: create, query
    Name of the light

---
penumbra(p): angle
    properties: create, query, edit
    specify penumbra region

---
position(pos): [linear, linear, linear]
    properties: create, query
    Position of the light

---
rgb(rgb): [float, float, float]
    properties: create, query
    RGB colour of the light

---
rightBarnDoorAngle(rbd): angle
    properties: create, query, edit
    Angle of the right of the barn door.

---
rotation(rot): [angle, angle, angle]
    properties: create, query
    Rotation of the light for orientation, where applicable

---
shadowColor(sc): [float, float, float]
    properties: create, query
    Color of the light's shadow

---
shadowDither(sd): float
    properties: create, query
    Shadow dithering value.

---
shadowSamples(sh): int
    properties: create, query
    Numbr of shadow samples to use

---
softShadow(ss): boolean
    properties: create, query
    True if soft shadowing is to be enabled

---
topBarnDoorAngle(tbd): angle
    properties: create, query, edit
    Angle of the top of the barn door.

---
useRayTraceShadows(rs): boolean
    properties: create, query
    True if ray trace shadows are to be used

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/spotLight.html 
    """


def spotLightPreviewPort(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagspotLight: name, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int, flagwidthHeight: tuple[int, int]) -> string:
    """Synopsis:
---
---
 spotLightPreviewPort(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [spotLight=name], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int], [widthHeight=[int, int]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

spotLightPreviewPort is undoable, queryable, and editable.
The optional argument is the name of the 3dPort.




Example:
---
import maya.cmds as cmds

light = cmds.spotLight()
cmds.window()
cmds.columnLayout('r')
cmds.spotLightPreviewPort('slPP', widthHeight=(256, 256), spotLight=light)
cmds.showWindow()

---
Return:
---


    string: - the name of the port created or modified

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
spotLight(sl): name
    properties: create
    Name of the spotLight.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
widthHeight(wh): [int, int]
    properties: create
    The width and height of the port.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/spotLightPreviewPort.html 
    """


def spreadSheetEditor(flagallAttr: boolean, flagattrRegExp: string, flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexecute: string, flagexists: boolean, flagfilter: string, flagfixedAttrList: list[string], flagforceMainConnection: string, flaghighlightConnection: string, flagkeyableOnly: boolean, flaglockMainConnection: boolean, flaglongNames: boolean, flagmainListConnection: string, flagniceNames: boolean, flagpanel: string, flagparent: string, flagprecision: int, flagselectedAttr: boolean, flagselectionConnection: string, flagshowShapes: boolean, flagstateString: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 spreadSheetEditor(
[name]
    , [allAttr=boolean], [attrRegExp=string], [control=boolean], [defineTemplate=string], [docTag=string], [execute=string], [exists=boolean], [filter=string], [fixedAttrList=string[]], [forceMainConnection=string], [highlightConnection=string], [keyableOnly=boolean], [lockMainConnection=boolean], [longNames=boolean], [mainListConnection=string], [niceNames=boolean], [panel=string], [parent=string], [precision=int], [selectedAttr=boolean], [selectionConnection=string], [showShapes=boolean], [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

spreadSheetEditor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

window = cmds.window( widthHeight=(400, 300) )
cmds.paneLayout()
activeList = cmds.selectionConnection( activeList=True )
cmds.spreadSheetEditor( mainListConnection=activeList )
cmds.showWindow( window )

---
Return:
---


    string: The name of the editor

Flags:
---


---
allAttr(aa): boolean
    properties: query
    Returns a list of all the attribute names
currently being displayed.  This flag is ignored when not being queried.

---
attrRegExp(are): string
    properties: create, query, edit
    Filter the current displayed attribute names.
This expression matches the case-insensitive substring of attribute names.

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
execute(exe): string
    properties: edit
    Immediately executes the command string once for every selected
cell in the spreadSheet.  Before the command is executed, "#A" is
substituted with the name of the cell's attribute, "#N" is substituted
with the name of the cell's node, and "#P" is substituted with the
full path name of the node.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
filter(f): string
    properties: create, query, edit
    Specifies the name of an itemFilter object to be used with this editor.
This filters the information coming onto the main list
of the editor.

---
fixedAttrList(fal): string[]
    properties: create, query, edit
    Forces the editor to only display attributes with the
specified names.

---
forceMainConnection(fmc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will only
display items contained in the selectionConnection object. This is
a variant of the -mainListConnection flag in that it will force a
change even when the connection is locked. This flag is used to
reduce the overhead when using the -unlockMainConnection
, -mainListConnection, -lockMainConnection flags in immediate
succession.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
keyableOnly(ko): boolean
    properties: create, query, edit
    Limits the displayed attributes to be those that are keyable.
True by default

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
longNames(ln): boolean
    properties: create, query, edit
    Controls whether the attributes are displayed using their
long names or their short names.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
niceNames(nn): boolean
    properties: create, query, edit
    Controls whether the attribute names will be displayed in
a more user-friendly, readable way.  When this is on, the longNames
flag is ignored.  When this is off, attribute names will be displayed
either long or short, according to the longNames flag.
Default is on. Queried, returns a boolean.

---
panel(pnl): string
    properties: create, query
    Specifies the panel for this editor. By default if
an editor is created in the create callback of a scripted panel it
will belong to that panel. If an editor does not belong to a panel
it will be deleted when the window that it is in is deleted.

---
parent(p): string
    properties: create, query, edit
    Specifies the parent layout for this editor. This flag will only
have an effect if the editor is currently un-parented.

---
precision(pre): int
    properties: create, query, edit
    Specifies the maximum number of digits displayed to the right
of the decimal place.  Can be 0 to 20.

---
selectedAttr(sla): boolean
    properties: query
    Returns a list of all the attribute names
that are selected.  This flag is ignored when not being queried.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
showShapes(ss): boolean
    properties: create, query, edit
    If true, when transforms are selected their shapes will
be displayed instead.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
unParent(up): boolean
    properties: create, edit
    Specifies that the editor should be removed from its layout.
This cannot be used in query mode.

---
unlockMainConnection(ulk): boolean
    properties: create, edit
    Unlocks the mainConnection, effectively restoring the original
mainConnection (if it is still available), and dynamic updates.

---
updateMainConnection(upd): boolean
    properties: create, edit
    Causes a locked mainConnection to be updated from the orginal
mainConnection, but preserves the lock state.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/spreadSheetEditor.html 
    """


def spring(flagaddSprings: boolean, flagallPoints: boolean, flagcount: boolean, flagdamping: float, flagdampingPS: float, flagendForceWeight: float, flagexclusive: boolean, flaglength: float, flagmaxDistance: float, flagminDistance: float, flagminMax: boolean, flagname: string, flagnoDuplicate: boolean, flagrestLength: float, flagrestLengthPS: float, flagstartForceWeight: float, flagstiffness: float, flagstiffnessPS: float, flaguseDampingPS: boolean, flaguseRestLengthPS: boolean, flaguseStiffnessPS: boolean, flagwalkLength: uint, flagwireframe: boolean) -> string:
    """Synopsis:
---
---
 spring(
objects
    , [addSprings=boolean], [allPoints=boolean], [count=boolean], [damping=float], [dampingPS=float], [endForceWeight=float], [exclusive=boolean], [length=float], [maxDistance=float], [minDistance=float], [minMax=boolean], [name=string], [noDuplicate=boolean], [restLength=float], [restLengthPS=float], [startForceWeight=float], [stiffness=float], [stiffnessPS=float], [useDampingPS=boolean], [useRestLengthPS=boolean], [useStiffnessPS=boolean], [walkLength=uint], [wireframe=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

spring is undoable, queryable, and editable.
* create a new spring object (shape plus transform).  The shape
contains springs between the points (particles, cvs, etc.)
of the objects selected or listed on the command line.
* create new springs and add them to an existing spring object
* edit or query certain attributes of an existing spring object

One "spring object" may have hundreds or even thousands of individual springs.
Certain attributes of the spring object specify exactly where the springs
are attached to which other objects.

Springs may be attached to the following: particles, vertices of soft
bodies, CVs or edit points of curves or surfaces, vertices of polygonal
objects, and points of lattices. In the case where one endpoint of a
spring is non-dynamic (a CV, edit point, etc.), the spring does not affect
its motion, but the motion of the point affects the spring. A spring will
be created only if at least one of the endpoints is dynamic: for example,
a spring will never be created between two CVs. A single spring object can
hold springs which are incident to any number of other objects.

The spring has creation-only flags and editable flags.  Creation-only flags
(minDistance, maxDistance, add, exclusive, all, wireframe, walklength,
checkExisting) can be used only when creating new springs (including adding
springs to existing spring object).  Editable flags modify attributes of an
existing spring object.

If a spring object is created, this command returns the names of
the shape and transform.  If a spring object is queried, the command returns
the results of the query.




Example:
---
import maya.cmds as cmds

cmds.spring( 'particle1', s=1.5, d=.3, mnd=0, mxd=5, n='spring1' )
Creates a spring object named spring1 with a strength of 1.5 and a
damping factor of 0.3 containing a spring between every pair of points in
particle1 that are within 0.0 and 5.0 units apart (except those already
connected by a spring).

cmds.spring( 'particle1', 'spring1', add=True, mnd=0, mxd=5 )
Creates between every pair of points in particle1 that are within 0.0
and 5.0 units apart (except those already connected by a spring), and adds
them to the existing spring object spring1.

cmds.spring( 'particle1', 'spring1', add=True, mnd=0, mxd=5, ce='false' )
Same as the previous example, but will not check for existing springs
in order to avoid duplication, and will create a new spring even between
pairs of particles which already have one.

cmds.spring( 'particle1', 'particle2', exclusive=1, all=1 )
Creates a spring between every pair of particles such that one
particle is in particle1 and the other is in particle2.  Does not create
any springs between pairs in the same object.  Does not create springs
between particles already connected by a spring.

---
Return:
---


    string: Command result

Flags:
---


---
addSprings(add): boolean
    properties: create
    If specified, springs will be added to the existing selected set of springs.
(Default is to create a new spring object.)

---
allPoints(all): boolean
    properties: create, edit
    If True, sets the mode of spring application to All.  This will add
springs between all points selected.
(Default is False.)

---
count(ct): boolean
    properties: query
    Return the number of springs in the shape.  Query-only.
We maintain this flag only for compatibility with earlier versions
of Maya.  To get the count of springs, it is much faster and simpler
to use the spring shape's count attribute: getAttr <shapeName>.count.

---
damping(d): float
    properties: create, query, edit
    Damping factor for the springs created in the spring object.
(Default = 0.2 )

---
dampingPS(dPS): float
    properties: create, query, edit
    Damping factor for the springs created in the spring object. This will
initialize all the entries in dampingPS to the specified value.
In both the flag and the attribute name, "PS" stands for "per-spring."
(Default = 0.2 )

---
endForceWeight(efw): float
    properties: create, query, edit
    Amount of the force of the spring that gets applied to the point to which
the spring ends. Valid range is from 0.0 to 1.0. (Default = 1.0 )

---
exclusive(exc): boolean
    properties: create
    If true, tells the command to create springs only between pairs of
points which are not in the same object.
(Default is False.)

---
length(l): float
    properties: create, query, edit
    Vestigial form of "restLength." Please use "restLength" instead.

---
maxDistance(mxd): float
    properties: create, edit
    Maximum distance between two points that a spring would be
considered.

---
minDistance(mnd): float
    properties: create
    Minimum distance between two points that a spring would be considered.
(Default = 0.0. See Defaults for more information on this flag's default.)

---
minMax(mm): boolean
    properties: create
    If True, sets the mode of the spring application to Min/Max.
This will add springs between all points from the specified point groups
that are between the minimum and maximum distance values set with min and max.
(Default is False.)
Note: This gets automatically set if either the min or max flags are used.

---
name(n): string
    properties: create, query
    Name of spring object.

---
noDuplicate(nd): boolean
    properties: create
    Check for existing springs and don't add a new spring between
two points already connected by a spring in the same object.
Only the object the command is working on is checked.  This flag
is relevant only when using -add. (Default = false)

---
restLength(rl): float
    properties: create, query, edit
    Per-object rest length for the new springs. Springs can use either
their per-object or per-spring rest length.  See the -lPS and -ulp flags.

---
restLengthPS(rPS): float
    properties: create, query, edit
    Per-spring rest length for the new springs. This will
initialize all the entries in restLengthPS to the specified value.
If this flag is not thrown, each rest length will be initialized to
the distance between the two  points at the time the spring is created
(i.e., the initial length of the spring).   When playing back, springs
can use either their per-spring or per-object rest length.  See the
-rl and -urp flags.
In both the flag and the attribute name, "PS" stands for "per-spring."

---
startForceWeight(sfw): float
    properties: create, query, edit
    Amount of the force of the spring that gets applied to the point from
which the spring starts. Valid range is from 0.0 to 1.0. (Default = 1.0 )

---
stiffness(s): float
    properties: create, query, edit
    Stiffness of the springs created in the spring object. (Default = 1.0 )
-damp float
Vestigial form of "damping."  Please use "damping" instead.

---
stiffnessPS(sPS): float
    properties: create, query, edit
    Stiffness of the springs created in the spring object. This will
initialize all the entries in stiffnessPS to the specified value.
In both the flag and the attribute name, "PS" stands for "per-spring."
(Default = 1.0 )

---
useDampingPS(udp): boolean
    properties: create, query, edit
    Specifies whether to use dampingPS (per spring damping).
If set to false, the per object damping attribute value will be used.
This flag simply sets the useDampingPS attribute of the spring shape.
In both the flag and the attribute name, "PS" stands for "per-spring."
(Default = false )

---
useRestLengthPS(urp): boolean
    properties: create, query, edit
    Specifies whether to use restLengthPS (per spring restLength).
If set to false, the per object restLength attribute value will be used.
This flag simply sets the useRestLengthPS attribute of the spring shape.
In both the flag and the attribute name, "PS" stands for "per-spring."
(Default = false )

---
useStiffnessPS(usp): boolean
    properties: create, query, edit
    Specifies whether to use stiffnessPS (per spring stiffness).
If set to false, the per object stiffness attribute value will be used.
This flag simply sets the useStiffnessPS attribute of the spring shape.
In both the flag and the attribute name, "PS" stands for "per-spring."
(Default = false )

---
walkLength(wl): uint
    properties: create
    This flag is valid only when doing wireframe creation.
It will create springs between pairs of points connected by the specified
number of edges.  For example, if walk length is 2, each pair of points
separated by no more than 2 edges will get a spring.  Walk length measures
the distance between pairs of vertices just like the number of blocks measures
the distance between two intersections in a city.

---
wireframe(wf): boolean
    properties: create
    If True, sets the mode of the spring application to Wireframe.
This is valid only for springs created on a soft body.
It will add springs along all edges connecting the adjacent points
(vertices or CV's) of curves and surfaces.
(Default is False.)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/spring.html 
    """


def squareSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagcontinuityType1: int, flagcontinuityType2: int, flagcontinuityType3: int, flagcontinuityType4: int, flagcurveFitCheckpoints: int, flagendPointTolerance: linear, flagname: string, flagnodeState: int, flagobject: boolean, flagpolygon: int, flagrebuildCurve1: boolean, flagrebuildCurve2: boolean, flagrebuildCurve3: boolean, flagrebuildCurve4: boolean) -> list[string]:
    """Synopsis:
---
---
 squareSurface(
string string string [string]
    , [caching=boolean], [constructionHistory=boolean], [continuityType1=int], [continuityType2=int], [continuityType3=int], [continuityType4=int], [curveFitCheckpoints=int], [endPointTolerance=linear], [name=string], [nodeState=int], [object=boolean], [polygon=int], [rebuildCurve1=boolean], [rebuildCurve2=boolean], [rebuildCurve3=boolean], [rebuildCurve4=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

squareSurface is undoable, queryable, and editable.
You must specify one continuity type flag for each selected curve.
If continuity type is 1 (fixed, no tangent continuity) then the
curveFitCheckpoints flag (cfc) is not required.




Example:
---
import maya.cmds as cmds

Creating square surfaces with three curves and fixed continuity type:

crv1 = cmds.curve( d=3, p=( (8, 0, 3), (5, 0, 3), (2, 0, 2), (0, 0, 0)) )
crv2 = cmds.curve( d=3, p=( (8, 0, -4), (5, 0, -3), (2, 0, -2), (0, 0, 0)) )
crv3 = cmds.curve( d=3, p=( (8, 0, 3), (9, 3, 2), (11, 3, 1), (8, 0, -4)) )

These curves form a rough triangle shape pointing at the origin.

cmds.squareSurface( crv3, crv1, crv2, ct1=1, ct2=1, ct3=1 )

Creating square surfaces with four curves, tangent continuity
type and to use 6 points per span in checking the continuity:

crv1 = cmds.curve( d=3, p=( (-2, 0, 4), (-2, 0, 5), (1, 0, 3), (3, 0, 4), (6, 0, 5) ) )
crv2 = cmds.curve( d=3, p=( (6, 0, 5), (8, 0, 2), (8, 0, -3), (7, 0, -4 ) ) )
crv3 = cmds.curve( d=3, p=( (7, 0, -4), (2, 0, -3), (-1, 0, -5), (-2, 0, -4) ) )
crv4 = cmds.curve( d=3, p=( (-2, 0, 4), (-4, 0, 1), (-4, 0, -3), (-2, 0, -4) ) )

These curves form a rough square shape around the origin.

cmds.squareSurface( crv1, crv2, crv3, crv4, cfc=6, ct1=2, ct2=2, ct3=2, ct4=2 )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
continuityType1(ct1): int
    properties: create, query, edit
    Continuity type legal values for curve 1:
1 - fixed boundary
2 - tangent continuity
3 - implied tangent continuity
Default: 2

---
continuityType2(ct2): int
    properties: create, query, edit
    Continuity type legal values for curve 2:
1 - fixed boundary
2 - tangent continuity
3 - implied tangent continuity
Default: 2

---
continuityType3(ct3): int
    properties: create, query, edit
    Continuity type legal values for curve 3:
1 - fixed boundary
2 - tangent continuity
3 - implied tangent continuity
Default: 2

---
continuityType4(ct4): int
    properties: create, query, edit
    Continuity type legal values for curve 4:
1 - fixed boundary
2 - tangent continuity
3 - implied tangent continuity
Default: 2

---
curveFitCheckpoints(cfc): int
    properties: create, query, edit
    The number of points per span to check the tangency deviation between the boundary curve and the created tangent square surface. Only available for the tangent continuity type.
Default: 5

---
endPointTolerance(ept): linear
    properties: create, query, edit
    Tolerance for end points, only used if endPoint attribute is true.
Default: 0.1

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
rebuildCurve1(rc1): boolean
    properties: create, query, edit
    A boolean to determine if input curve 1 should be rebuilt (with curvature continuity).
Default: false

---
rebuildCurve2(rc2): boolean
    properties: create, query, edit
    A boolean to determine if input curve 2 should be rebuilt (with curvature continuity).
Default: false

---
rebuildCurve3(rc3): boolean
    properties: create, query, edit
    A boolean to determine if input curve 3 should be rebuilt (with curvature continuity).
Default: false

---
rebuildCurve4(rc4): boolean
    properties: create, query, edit
    A boolean to determine if input curve 4 should be rebuilt (with curvature continuity).
Default: false

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
polygon(po): int
    properties: create
    The value of this argument controls the type of the object
created by this operation

 0: nurbs surface
 1: polygon (use nurbsToPolygonsPref to set the parameters for the conversion)
 2: subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)
 3: Bezier surface
 4: subdivision surface solid (use nurbsToSubdivPref to set the
parameters for the conversion)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/squareSurface.html 
    """


def srtContext(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 srtContext([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

srtContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To see if an srtContext named "Transform" exists:
cmds.srtContext( 'Transform', q=True, exists=True )

---
Return:
---


    string: - name of the newly created context

Flags:
---


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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/srtContext.html 
    """


def stereoCameraView(flagactiveComponentsXray: boolean, flagactiveCustomEnvironment: string, flagactiveCustomGeometry: string, flagactiveCustomLighSet: string, flagactiveCustomOverrideGeometry: string, flagactiveCustomRenderer: string, flagactiveOnly: boolean, flagactiveShadingGraph: string, flagactiveSupported: boolean, flagactiveView: boolean, flagaddObjects: string, flagaddSelected: boolean, flagallObjects: boolean, flagbackfaceCulling: boolean, flagbluePencil: boolean, flagbufferMode: string, flagbumpResolution: tuple[uint, uint], flagcamera: string, flagcameraName: string, flagcameraSet: string, flagcameraSetup: boolean, flagcameras: boolean, flagcapture: string, flagcaptureSequenceNumber: int, flagcenterCamera: string, flagcolorMap: boolean, flagcolorResolution: tuple[uint, uint], flagcontrol: boolean, flagcontrolVertices: boolean, flagcullingOverride: string, flagdefault: boolean, flagdefineTemplate: string, flagdeformers: boolean, flagdimensions: boolean, flagdisplayAppearance: string, flagdisplayLights: string, flagdisplayMode: string, flagdisplayTextures: boolean, flagdocTag: string, flagdynamicConstraints: boolean, flagdynamics: boolean, flageditorChanged: script, flagexists: boolean, flagfilter: string, flagfilteredObjectList: boolean, flagfluids: boolean, flagfogColor: tuple[float, float, float, float], flagfogDensity: float, flagfogEnd: float, flagfogMode: string, flagfogSource: string, flagfogStart: float, flagfogging: boolean, flagfollicles: boolean, flagforceMainConnection: string, flaggrid: boolean, flaghairSystems: boolean, flaghandles: boolean, flagheadsUpDisplay: boolean, flagheight: boolean, flaghighlightConnection: string, flaghulls: boolean, flagignorePanZoom: boolean, flagikHandles: boolean, flagimagePlane: boolean, flaginteractive: boolean, flaginteractiveBackFaceCull: boolean, flaginteractiveDisableShadows: boolean, flagisFiltered: boolean, flagjointXray: boolean, flagjoints: boolean, flagleftCamera: string, flaglights: boolean, flaglineWidth: float, flaglocators: boolean, flaglockMainConnection: boolean, flaglowQualityLighting: boolean, flagmainListConnection: string, flagmanipulators: boolean, flagmaxConstantTransparency: float, flagmaximumNumHardwareLights: boolean, flagmodelPanel: string, flagmotionTrails: boolean, flagnCloths: boolean, flagnParticles: boolean, flagnRigids: boolean, flagnoUndo: boolean, flagnurbsCurves: boolean, flagnurbsSurfaces: boolean, flagobjectFilter: script, flagobjectFilterList: script, flagobjectFilterListUI: script, flagobjectFilterShowInHUD: boolean, flagobjectFilterUI: script, flagocclusionCulling: boolean, flagpanel: string, flagparent: string, flagpivots: boolean, flagplanes: boolean, flagpluginObjects: tuple[string, boolean], flagpluginShapes: boolean, flagpolymeshes: boolean, flagqueryPluginObjects: string, flagremoveSelected: boolean, flagrendererDeviceName: boolean, flagrendererList: boolean, flagrendererListUI: boolean, flagrendererName: string, flagrendererOverrideList: boolean, flagrendererOverrideListUI: boolean, flagrendererOverrideName: string, flagresetCustomCamera: boolean, flagrigRoot: string, flagrightCamera: string, flagsceneRenderFilter: string, flagselectionConnection: string, flagselectionHiliteDisplay: boolean, flagsetSelected: boolean, flagshadingModel: int, flagshadows: boolean, flagsmallObjectCulling: boolean, flagsmallObjectThreshold: float, flagsmoothWireframe: boolean, flagsortTransparent: boolean, flagstateString: boolean, flagstereoDrawMode: boolean, flagstrokes: boolean, flagsubdivSurfaces: boolean, flagswapEyes: boolean, flagtextureAnisotropic: boolean, flagtextureCompression: boolean, flagtextureDisplay: string, flagtextureEnvironmentMap: boolean, flagtextureHilight: boolean, flagtextureMaxSize: int, flagtextureMemoryUsed: boolean, flagtextureSampling: int, flagtextures: boolean, flagtranspInShadows: boolean, flagtransparencyAlgorithm: string, flagtwoSidedLighting: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateColorMode: boolean, flagupdateMainConnection: boolean, flaguseBaseRenderer: boolean, flaguseColorIndex: boolean, flaguseCustomBackground: boolean, flaguseDefaultMaterial: boolean, flaguseInteractiveMode: boolean, flaguseRGBImagePlane: boolean, flaguseReducedRenderer: boolean, flaguseTemplate: string, flaguserNode: string, flagviewColor: tuple[float, float, float, float], flagviewObjects: boolean, flagviewSelected: boolean, flagviewType: boolean, flagwidth: boolean, flagwireframeBackingStore: boolean, flagwireframeOnShaded: boolean, flagxray: boolean) -> string:
    """Synopsis:
---
---
 stereoCameraView(
objects
[editorName]
    , [activeComponentsXray=boolean], [activeCustomEnvironment=string], [activeCustomGeometry=string], [activeCustomLighSet=string], [activeCustomOverrideGeometry=string], [activeCustomRenderer=string], [activeOnly=boolean], [activeShadingGraph=string], [activeSupported=boolean], [activeView=boolean], [addObjects=string], [addSelected=boolean], [allObjects=boolean], [backfaceCulling=boolean], [bluePencil=boolean], [bufferMode=string], [bumpResolution=[uint, uint]], [camera=string], [cameraName=string], [cameraSet=string], [cameraSetup=boolean], [cameras=boolean], [capture=string], [captureSequenceNumber=int], [centerCamera=string], [colorMap=boolean], [colorResolution=[uint, uint]], [control=boolean], [controlVertices=boolean], [cullingOverride=string], [default=boolean], [defineTemplate=string], [deformers=boolean], [dimensions=boolean], [displayAppearance=string], [displayLights=string], [displayMode=string], [displayTextures=boolean], [docTag=string], [dynamicConstraints=boolean], [dynamics=boolean], [editorChanged=script], [exists=boolean], [filter=string], [filteredObjectList=boolean], [fluids=boolean], [fogColor=[float, float, float, float]], [fogDensity=float], [fogEnd=float], [fogMode=string], [fogSource=string], [fogStart=float], [fogging=boolean], [follicles=boolean], [forceMainConnection=string], [grid=boolean], [hairSystems=boolean], [handles=boolean], [headsUpDisplay=boolean], [height=boolean], [highlightConnection=string], [hulls=boolean], [ignorePanZoom=boolean], [ikHandles=boolean], [imagePlane=boolean], [interactive=boolean], [interactiveBackFaceCull=boolean], [interactiveDisableShadows=boolean], [isFiltered=boolean], [jointXray=boolean], [joints=boolean], [leftCamera=string], [lights=boolean], [lineWidth=float], [locators=boolean], [lockMainConnection=boolean], [lowQualityLighting=boolean], [mainListConnection=string], [manipulators=boolean], [maxConstantTransparency=float], [maximumNumHardwareLights=boolean], [modelPanel=string], [motionTrails=boolean], [nCloths=boolean], [nParticles=boolean], [nRigids=boolean], [noUndo=boolean], [nurbsCurves=boolean], [nurbsSurfaces=boolean], [objectFilter=script], [objectFilterList=script], [objectFilterListUI=script], [objectFilterShowInHUD=boolean], [objectFilterUI=script], [occlusionCulling=boolean], [panel=string], [parent=string], [pivots=boolean], [planes=boolean], [pluginObjects=[string, boolean]], [pluginShapes=boolean], [polymeshes=boolean], [queryPluginObjects=string], [removeSelected=boolean], [rendererDeviceName=boolean], [rendererList=boolean], [rendererListUI=boolean], [rendererName=string], [rendererOverrideList=boolean], [rendererOverrideListUI=boolean], [rendererOverrideName=string], [resetCustomCamera=boolean], [rigRoot=string], [rightCamera=string], [sceneRenderFilter=string], [selectionConnection=string], [selectionHiliteDisplay=boolean], [setSelected=boolean], [shadingModel=int], [shadows=boolean], [smallObjectCulling=boolean], [smallObjectThreshold=float], [smoothWireframe=boolean], [sortTransparent=boolean], [stateString=boolean], [stereoDrawMode=boolean], [strokes=boolean], [subdivSurfaces=boolean], [swapEyes=boolean], [textureAnisotropic=boolean], [textureCompression=boolean], [textureDisplay=string], [textureEnvironmentMap=boolean], [textureHilight=boolean], [textureMaxSize=int], [textureMemoryUsed=boolean], [textureSampling=int], [textures=boolean], [transpInShadows=boolean], [transparencyAlgorithm=string], [twoSidedLighting=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateColorMode=boolean], [updateMainConnection=boolean], [useBaseRenderer=boolean], [useColorIndex=boolean], [useCustomBackground=boolean], [useDefaultMaterial=boolean], [useInteractiveMode=boolean], [useRGBImagePlane=boolean], [useReducedRenderer=boolean], [useTemplate=string], [userNode=string], [viewColor=[float, float, float, float]], [viewObjects=boolean], [viewSelected=boolean], [viewType=boolean], [width=boolean], [wireframeBackingStore=boolean], [wireframeOnShaded=boolean], [xray=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

stereoCameraView is undoable, queryable, and editable.
Note that some of the flags of this command may have different settings
for normal mode and for interactive/playback mode.  For example, a
modelEditor can be set to use shaded mode normally, but to use wireframe
during playback for greater speed.  Some flags also support having
defaults set so that new model editors will be created with those settings.

This is the main command for creating stereo editors. This commands
only acts as an interface to the actual viewport. It is derived off of
MPxModelEditorCommand. This command manages the set of stereo rig
tools.




Example:
---
import maya.cmds as cmds

   Create a window with a model editor and some buttons that
   change the editor's display of objects in the scene.
---

window = cmds.window('window')
form = cmds.formLayout()
editor = cmds.modelEditor()
column = cmds.columnLayout('true')

   Create some buttons that will alter the display appearance of
   objects in the model editor, eg. wireframe vs. shaded mode.
---

cmds.button(label='Wireframe', command= "cmds.modelEditor(editor, edit=True, displayAppearance='wireframe')")
cmds.button(label='Points', command= "cmds.modelEditor(editor, edit=True, displayAppearance='points')")
cmds.button(label='Bounding Box', command= "cmds.modelEditor(editor, edit=True, displayAppearance='boundingBox')")
cmds.button(label='Smooth Shaded', command= "cmds.modelEditor(editor, edit=True, displayAppearance='smoothShaded')")
cmds.button(label='Flat Shaded', command= "cmds.modelEditor(editor, edit=True, displayAppearance='flatShaded')")

   Set up the window layout attachments.
---

cmds.formLayout( form, edit=True, attachForm=[(column, 'top', 0), (column, 'left', 0), (editor, 'top', 0), (editor, 'bottom', 0), (editor, 'right', 0)], attachNone=[(column, 'bottom'), (column, 'right')], attachControl=(editor, 'left', 0, column))

   Create a camera for the editor.  This particular camera will
   have a close up perspective view of the centre of the ground plane.
---

camera= cmds.camera(centerOfInterest=2.450351,
                        position = (1.535314, 1.135712, 1.535314),
                        rotation = (-27.612504, 45, 0),
                        worldUp = (-0.1290301, 0.3488592, -0.1290301))

   Attach the camera to the model editor.
---

cmds.modelEditor( editor, edit=True, camera=camera[0] )

   Put an object in the scene.
---

cmds.cone()

cmds.showWindow( window )

   The following two examples assume a custom model editor command
   defined via the MPxModelEditorCommand API class, named 'myEditor'.
---


   Create a custom editor, and use it as the model editor of Maya's
   default modelPanel4 (the perspective view).
---

cmds.myEditor( modelPanel='modelPanel4' )

   Restore the default model editor.
---

cmds.modelEditor( modelPanel='modelPanel4' )
---

---
         The following example shows usage of the render override flags
---
         with model panel 'modelPanel4'
---

cmds.modelEditor( 'modelPanel4', q=True, rol=True ) Query for non-UI names for any render overrides
cmds.modelEditor( 'modelPanel4', q=True, rou=True ) Query for UI names for any render overrides
cmds.modelEditor( 'modelPanel4', q=True, rom=True ) Query for any active override
cmds.modelEditor( 'modelPanel4', e=True, rom='myOverride' ) Set active override to 'myOverride' if it exists
cmds.modelEditor( 'modelPanel4', e=True, rom='' ) Clear out the active override

cmds.modelEditor( 'modelPanel4', e=True, rnm='base_OpenGL_Renderer' ) Set the renderer used for a 3d modeling viewport
cmds.modelEditor( 'modelPanel4', q=True, rnm=True ) Query for the renderer used for a 3d modeling viewport
cmds.modelEditor( 'modelPanel4', q=True, rdn=True ) Query for device name for current renderer.

Test if the panel exists
stereoCameraView("StereoPanel", query=True, exists=True)

---
Return:
---


    string: the name of the editor.

Flags:
---


---
activeComponentsXray(acx): boolean
    properties: query, edit
    Turns on or off Xray mode for active components.

---
activeCustomEnvironment(ace): string
    properties: edit
    Specifies a path to an image file to be used as environment map.
It is only enabled when a valid scene render filter is specified.

---
activeCustomGeometry(acg): string
    properties: query, edit
    Specifies an identifier for custom geometry to override the geometry
to display. It is only enabled when a valid scene render filter is specified.

---
activeCustomLighSet(acl): string
    properties: query, edit
    Specifies an identifier for the light set to use
with a scene render filter. It is only enabled when a valid scene render filter is specified.

---
activeCustomOverrideGeometry(aog): string
    properties: query, edit
    Specifies an identifier for an override on the custom geometry for a scene
render filter.

---
activeCustomRenderer(acr): string
    properties: query, edit
    Specifies an identifier for custom renderer to use when
a valid scene render filter is also specified.

---
activeOnly(ao): boolean
    properties: query, edit
    Sets whether only active objects should appear shaded in
shaded display.

---
activeShadingGraph(asg): string
    properties: query, edit
    Specifies the shading graph to use to override material display.
Only enabled when a valid scene render filter is specified.

---
activeSupported(ams): boolean
    properties: query
    True if the viewer is capable of drawing in active mode which takes
advantage of the graphics card's built-in stereoscopic support. This
includes support for shutter glasses and stereo support in clone mode.

---
activeView(av): boolean
    properties: query, edit
    Sets this model editor to be the active view.  Returns true
if successful.  On query this flag will return whether the view is
the active view.

---
addObjects(aob): string
    properties: edit
    This flag causes the objects contained within the selection
connection to be added to the list of objects visible in the view
(if viewSelected is true).

---
addSelected(addSelected): boolean
    properties: edit
    This flag causes the currently active objects to be added
to the list of objects visible in the view (if viewSelected is true).

---
allObjects(alo): boolean
    properties: query, edit
    Turn on/off the display of all objects for the view of
the model editor. This excludes NURBS, CVs, hulls, grids and
manipulators.

---
backfaceCulling(bfc): boolean
    properties: query, edit
    Turns on or off backface culling for the whole view.  This
setting overrides the culling settings of individual objects.  All
objects draw in the view will be backface culled.  When backface
culling is turned on, surfaces becomes invisible in areas where the
normal is pointing away from the camera.

---
bluePencil(bp): boolean
    properties: create, query, edit
    Define whether the blue pencil should be added or not

---
bufferMode(bm): string
    properties: query, edit
    Deprecated: this is not supported in Viewport 2.0.  Sets the
graphic buffer mode.  Possible values are "single" or "double".

---
bumpResolution(brz): [uint, uint]
    properties: query, edit
    Set the resolution for "baked" bump map textures when using the
hardware renderer. The default value is 512, 512 respectively.

---
camera(cam): string
    properties: query, edit
    Change or query the name of the camera in model editor.

---
cameraName(cn): string
    properties: create, edit
    Set the name of the panel's camera transform and shape. The
shape name is computed by appending the string "Shape" to the
transform name. This flag may not be queried.

---
cameraSet(cst): string
    properties: create, query, edit
    Name of the camera set

---
cameraSetup(cs): boolean
    properties: query
    Based on the model editor name passed in will
returns a string list containing camera setups.
A camera setup can contain one or more cameras
which are associated with each other.
Camera setups are defined as pairs of consecutive
strings in the list. Each pair is comprised of:
a string which identifies an active camera,
and a string which defines a script
to set up a given active camera. As many pairs of strings
can be returned as the number of active cameras. If nothing
is returned then it is assumed that no set up is
required to activate a given camera.

---
cameras(ca): boolean
    properties: query, edit
    Turn on/off the display of cameras for the view of the
model editor.

---
capture(cpt): string
    properties: query, edit
    Perform an one-time capture of the viewport to the named image file on disk.

---
captureSequenceNumber(csn): int
    properties: query, edit
    When a number greater or equal to 0 is specified each subsequent refresh will
save an image file to disk if the capture flag has been enabled.

The naming of the file is:

{root name}.#.{extension}

if the name {root name}.{extension} is used for the capture flag argument.

The value of # starts at the number specified to for this argument and
increments for each subsequent refresh.

Sequence capture can be disabled by specifying a number less than 0 or an
empty file name for the capture flag.

---
centerCamera(ccm): string
    properties: query
    Only available in query mode: returns the current center camera of this view.

---
colorMap(cm): boolean
    properties: query
    Queries the color map style for the model panel. Possible
values are "colorIndex" and "rgb".

---
colorResolution(crz): [uint, uint]
    properties: query, edit
    Set the resolution for "baked" color textures when using the
hardware renderer. The default value is 256, 256 respectively.

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
controlVertices(cv): boolean
    properties: query, edit
    Turn on/off the display of NURBS CVs for the view of the
model editor.

---
cullingOverride(cov): string
    properties: query, edit
    Set whether to override the culling attributes on objects when using
the hardware renderer. The options are:

"none" : Use the culling object attributes per object.
"doubleSided" : Force all objects to be double sided.
"singleSided": Force all objects to be single sided.

The default value is "none".

---
default(d): boolean
    properties: query, edit
    Causes this command to modify the default value of this setting.
Newly created model editors will inherit the values.  This flag may
be used with the -interactive to set default interactive settings.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deformers(df): boolean
    properties: query, edit
    Turn on/off the display of deformer objects for the view
of the model editor.

---
dimensions(dim): boolean
    properties: query, edit
    Turn on/off the display of dimension objects for the view
of the model editor.

---
displayAppearance(da): string
    properties: query, edit
    Sets the display appearance of the model panel.  Possible
values are "wireframe", "points", "boundingBox", "smoothShaded",
"flatShaded".  This flag may be used with the -interactive
and -default flags.  Note that only "wireframe", "points", and
"boundingBox" are valid for the interactive mode.

---
displayLights(dl): string
    properties: query, edit
    Sets the lighting for shaded mode.  Possible values are
"selected", "active", "all", "default", "none".

---
displayMode(dm): string
    properties: create, query, edit
    Defines the display mode for this view. Some modes are available
only for certain types of graphics hardware. Valid values are:

active: uses the graphics card's built-in stereoscopic mode is available
leftEye: displays only the view from the left camera.
rightEye: displays only the view from the rigth camera.
centerEye: displays only the view from the center camera.
anaglyph: displays both left and right cameras, filtered using
red and blue
anaglyphLum: same as anaglyph, except the luminance is computed
before the red and blue filtering
interlace: displays an interlaced view of left and right cameras
checkerboard: Same as interlace, except a checkerboard pattern is
used to mix both images
freeview: displays both left and right images, half size next to
each other
freeviewX: same as freeview, except left and right cameras are swapped

---
displayTextures(dtx): boolean
    properties: query, edit
    Turns on or off display of textures in shaded mode

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
dynamicConstraints(dc): boolean
    properties: query, edit
    Turn on/off the display of dynamicConstraints for the view
of the model editor.

---
dynamics(dy): boolean
    properties: query, edit
    Turn on/off the display of dynamics objects for the view
of the model editor.

---
editorChanged(ec): script
    properties: create, query, edit
    An optional script callback which is called when the editors
options have changed.  This is useful in a situation where a scripted
panel contains a modelEditor and wants to be notified when the contained
editor changes its options.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
filter(f): string
    properties: create, query, edit
    Specifies the name of an itemFilter object to be used with this editor.
This filters the information coming onto the main list
of the editor.

---
filteredObjectList(fol): boolean
    properties: query
    For model editors with filtering on (either using an object filter, or isolate
select), this flag returns a string list of the objects which are displayed in
this editor. Note that this list does not take into account visibility (based on
camera frustum or flags), it purely captures the objects which are considered
when rendering the view.

---
fluids(fl): boolean
    properties: query, edit
    Turn on/off the display of fluids for the view
of the model editor.

---
fogColor(fcl): [float, float, float, float]
    properties: query, edit
    The color used for hardware fogging.

---
fogDensity(fdn): float
    properties: query, edit
    Determines the density of hardware fogging.

---
fogEnd(fen): float
    properties: query, edit
    The end location of hardware fogging.

---
fogMode(fmd): string
    properties: query, edit
    This determines the drop-off mode for fog. The possibilities are:

"linear" : linear drop-off
"exponent" : exponential drop-off
"exponent2" : squared exponential drop-off

---
fogSource(fsc): string
    properties: query, edit
    Set the type of fog algorithm to use. If the argument
is "fragment" (default) then fog is computed per pixel. If
the argument is "coordinate" then if the geometry has
specified vertex fog coordinates, and the OpenGL extension
for vertex fog is supported by the graphics system, then
fog is computed per vertex.

---
fogStart(fst): float
    properties: query, edit
    The start location of hardware fogging.

---
fogging(fg): boolean
    properties: query, edit
    Set whether hardware fogging is enabled or not.

---
follicles(fo): boolean
    properties: query, edit
    Turn on/off the display of follicles for the view
of the model editor.

---
forceMainConnection(fmc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will only
display items contained in the selectionConnection object. This is
a variant of the -mainListConnection flag in that it will force a
change even when the connection is locked. This flag is used to
reduce the overhead when using the -unlockMainConnection
, -mainListConnection, -lockMainConnection flags in immediate
succession.

---
grid(gr): boolean
    properties: query, edit
    Turn on/off the display of the grid for the view of the
model editor.

---
hairSystems(hs): boolean
    properties: query, edit
    Turn on/off the display of hairSystems for the view
of the model editor.

---
handles(ha): boolean
    properties: query, edit
    Turn on/off the display of select handles for the view
of the model editor.

---
headsUpDisplay(hud): boolean
    properties: query, edit
    Sets whether the model panel will draw any enabled heads up
display	elements in this window (if true).  Currently this requires
the HUD elements to be globally enabled.

---
height(h): boolean
    properties: query
    Return the height of the associated viewport in pixels

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
hulls(hu): boolean
    properties: query, edit
    Turn on/off the display of NURBS hulls for the view of the
model editor.

---
ignorePanZoom(ipz): boolean
    properties: query, edit
    Sets whether the model panel will ignore the 2D pan/zoom value to
give an overview of the scene.

---
ikHandles(ikh): boolean
    properties: query, edit
    Turn on/off the display of ik handles and end effectors
for the view of the model editor.

---
imagePlane(imp): boolean
    properties: query, edit
    Turn on/off the display of image plane for the view

---
interactive(i): boolean
    properties: query, edit
    Causes this command to modify the interactive refresh settings of
the view.  In this way it is possible to change the behavior of the
model editor during playback for improved performance.

---
interactiveBackFaceCull(ibc): boolean
    properties: create, query, edit
    Define whether interactive backface culling should be on or not

---
interactiveDisableShadows(dis): boolean
    properties: create, query, edit
    Define whether interactive shadows should be disabled or not

---
isFiltered(isFiltered): boolean
    properties: query
    Returns true for model editors with filtering applied to their view of the
scene. This could either be an explicit object filter, or a display option such
as isolate select which filters the objects that are displayed.

---
jointXray(jx): boolean
    properties: query, edit
    Turns on or off Xray mode for joints.

---
joints(j): boolean
    properties: query, edit
    Turn on/off the display of joints for the view of the
model editor.

---
leftCamera(lcm): string
    properties: query
    Only available in query mode: returns the current left camera of this view.

---
lights(lt): boolean
    properties: query, edit
    Turn on/off the display of lights for the view of the
model editor.

---
lineWidth(lw): float
    properties: query, edit
    Set width of lines for display

---
locators(lc): boolean
    properties: query, edit
    Turn on/off the display of locator objects for the view
of the model editor.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
lowQualityLighting(lql): boolean
    properties: query, edit
    Set whether to use "low quality lighting" when using the
hardware renderer. The default value is false.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
manipulators(m): boolean
    properties: query, edit
    Turn on/off the display of manipulator objects for the view
of the model editor.

---
maxConstantTransparency(mct): float
    properties: query, edit
    Sets the maximum constant transparency.  Setting this value remaps
constant transparency values from the range [0.0, 1.0] to the range
[0.0, maxConstantTransparency]. All transparency values are shifted
linearly to the new range, so a fully transparency object
(transparency 1.0) would
appear with a transparency of maxConstantTransparency in the viewport,
allowing highly transparent objects to be made visible.  This flag only
affects constant (non-textured) transparent objects.

---
maximumNumHardwareLights(mhl): boolean
    properties: create, query, edit
    Define whether the hardware light maximum should be respected or not

---
modelPanel(mp): string
    properties: create
    Allows the created model editor to be embedded in the named model panel.
Intended for use with custom model editors created via the API (i.e. the
flag would be used on the derived MPxModelEditorCommand), though the flag
may also be used on the base modelEditor command to restore a default Maya
model editor to the panel.
Note that the model editor previously owned by the panel is deleted.

---
motionTrails(mt): boolean
    properties: query, edit
    Turn on/off the Motion Trail display in the Viewport.

---
nCloths(ncl): boolean
    properties: query, edit
    Turn on/off the display of nCloths for the view
of the model editor.

---
nParticles(npa): boolean
    properties: query, edit
    Turn on/off the display of nParticles for the view
of the model editor.

---
nRigids(nr): boolean
    properties: query, edit
    Turn on/off the display of nRigids for the view
of the model editor.

---
noUndo(nud): boolean
    properties: edit
    This flag prevents some viewport operations (such as isolate
select) from being added to the undo queue.

---
nurbsCurves(nc): boolean
    properties: query, edit
    Turn on/off the display of nurbs curves for the view
of the model editor.

---
nurbsSurfaces(ns): boolean
    properties: query, edit
    Turn on/off the display of nurbs surfaces for the view
of the model editor.

---
objectFilter(obf): script
    properties: query, edit
    Set or query the current object filter name. An object filter
is required to have already been registered.

---
objectFilterList(ofl): script
    properties: query
    Return a list of names of registered filters.

---
objectFilterListUI(ofu): script
    properties: query
    Return a list of UI names of registered filters.

---
objectFilterShowInHUD(ofs): boolean
    properties: query, edit
    Sets whether or not to display the object filter UI name in the heads
up display when an object filter is active. This string is concatenated
with the camera name.

---
objectFilterUI(obu): script
    properties: query
    Query the current object filter UI name. The object filter
is required to have already been registered.

---
occlusionCulling(ocl): boolean
    properties: query, edit
    Set whether to enable occlusion culling testing when using
the hardware renderer. The default value is false.

---
panel(pnl): string
    properties: create, query
    Specifies the panel for this editor. By default if
an editor is created in the create callback of a scripted panel it
will belong to that panel. If an editor does not belong to a panel
it will be deleted when the window that it is in is deleted.

---
parent(p): string
    properties: create, query, edit
    Specifies the parent layout for this editor. This flag will only
have an effect if the editor is currently un-parented.

---
pivots(pv): boolean
    properties: query, edit
    Turn on/off the display of transform pivots for the view
of the model editor.

---
planes(pl): boolean
    properties: query, edit
    Turn on/off the display of sketch planes for the view
of the model editor.

---
pluginObjects(po): [string, boolean]
    properties: edit, multiuse
    Turn on/off the display of plug-in objects for the view.
It depends on the plug-in implementation whether to respect this flag.

---
pluginShapes(ps): boolean
    properties: edit
    Turn on/off the display of plug-in shapes for the view.
It depends on the plug-in implementation whether to respect this flag.

---
polymeshes(pm): boolean
    properties: query, edit
    Turn on/off the display of polygon meshes for the view
of the model editor.

---
queryPluginObjects(qpo): string
    properties: query
    Query the on/off state of plug-in objects display for the view.
To set the on/off state, use -pluginObjects instead.

---
removeSelected(rs): boolean
    properties: edit
    This flag causes the currently active objects to be removed
from the list of objects visible in the view (if viewSelected is true).

---
rendererDeviceName(rdn): boolean
    properties: query
    Query for the name of the draw API used by the Viewport 2.0 renderer for a 3d modeling viewport.
The possible return values are "VirtualDeviceGL" if Maya is set to use "OpenGL - Legacy" for Viewport 2.0,
"VirtualDeviceGLCore" if Maya is set to use "OpenGL - Core Profile" (either Compatibility or Strict) for
Viewport 2.0, or "VirtualDeviceDx11" if Maya is set to use DirectX for Viewport 2.0.
If the renderer for the 3d modeling viewport is not Viewport 2.0, an empty string will be returned.

---
rendererList(rls): boolean
    properties: query
    Query for a list of the internal names for renderers available for use with the
3d modeling viewport. The default list contains at least "vp2Renderer", if supported. See
rendererName for more details on these renderers. Any plug-in viewport renderers will also appear
in this list.

---
rendererListUI(rlu): boolean
    properties: query
    Query for a list of the UI names for renderers available for use with the
3d modeling viewport. The default list consists of the UI name for "vp2Renderer", if it is supported.
Any plug-in viewport renderer's UI names will also appear in this list. This list
and the list returned from rendererList have a 1:1 correspondance.

---
rendererName(rnm): string
    properties: query, edit
    Set or get the renderer used for a 3d modeling viewport. The name provided
should be an internal name of a renderer. The 'rendererList' flag
can be used to query for a list of available names.
The default renderer is "vp2Renderer": Viewport 2.0.

---
rendererOverrideList(rol): boolean
    properties: query
    Query for a list of the internal names for renderer overrides for a 3d viewport renderer.
Currently only the "Viewport 2" renderer supports renderer overrides.

---
rendererOverrideListUI(rou): boolean
    properties: query
    Query for a list of the UI names for renderer overrides for a 3d viewport renderer.
Currently only the "Viewport 2" renderer supports renderer overrides.

---
rendererOverrideName(rom): string
    properties: query, edit
    Set or get the override used for a 3d viewport renderer. The name provided
should be the internal name for an override.  The 'rendererOverrideList' flag
can be used to query for a list of available names.
Currently only the "Viewport 2" renderer  supports renderer overrides.
Setting an empty string will unset any currently active override.

---
resetCustomCamera(rcc): boolean
    properties: edit
    When specified will reset the camera transform for the active custom camera
used for a scene render filter. It is only enabled when a valid scene render filter is specified.

---
rigRoot(rr): string
    properties: create, query, edit
    Defines the rig root associated with this view.

---
rightCamera(rcm): string
    properties: query
    Only available in query mode: returns the current right camera of this view.

---
sceneRenderFilter(srf): string
    properties: query, edit
    Specifies the name of a scene render filter

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
selectionHiliteDisplay(sel): boolean
    properties: query, edit
    Sets whether the model panel will draw any selection hiliting
on the objects in this window.

---
setSelected(ss): boolean
    properties: edit
    This flag causes the currently active objects to be the
only objects visible in the view (if viewSelected is true).

---
shadingModel(sml): int
    properties: create, query, edit
    Shading model to use

---
shadows(sdw): boolean
    properties: query, edit
    Turn on/off the display of hardware shadows in shaded mode.

---
smallObjectCulling(soc): boolean
    properties: create, query, edit
    Define whether small object culling should be enabled or not

---
smallObjectThreshold(sot): float
    properties: create, query, edit
    Threshold used for small object culling

---
smoothWireframe(swf): boolean
    properties: query, edit
    Turns on or off smoothing of wireframe lines and points

---
sortTransparent(st): boolean
    properties: query, edit
    This flag turns on/off sorting of transparent objects during
shaded mode refresh. Normally, objects are sorted according to their
origin in camera space but when this flag is turned off they will be
drawn according to their (depth-first traversal) order in the scene
graph. This is a global flag that affects all model editors.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
stereoDrawMode(sdm): boolean
    properties: create, query, edit
    If this flag is used then set stereo draw mode

---
strokes(str): boolean
    properties: query, edit
    Turn on/off the display of Paint Effects strokes for the view

---
subdivSurfaces(sds): boolean
    properties: query, edit
    Turn on/off the display of subdivision surfaces for the view
of the model editor.

---
swapEyes(se): boolean
    properties: create, query, edit
    Swap the display of the left and right cameras. The left camera
becomes the right draw pass and the right camera becomes the left draw
pass.
This flag is intended for advanced users, for situations where the
hardware uses the opposite left/right convention.

---
textureAnisotropic(ta): boolean
    properties: query, edit
    Set whether to perform anisotropic texture filtering.
Will work only if the anisotropic texture filtering extension
is supported in OpenGL on the graphics system.

---
textureCompression(tcp): boolean
    properties: create, query, edit
    Defines whether texture compression should be used or not

---
textureDisplay(td): string
    properties: query, edit
    Set the type of blending to use for textures.
The blend is performed between the destination fragment
and the texture fragment. The source is usually the
material color. Argument options are:
"modulate" : multiply the destination and texture fragment
"decal" : overwrite the destination with the texture fragment

---
textureEnvironmentMap(tem): boolean
    properties: create, query, edit
    If true then use a texture environment map

---
textureHilight(th): boolean
    properties: query, edit
    Set whether to show specular hilighting
when the display is in shaded textured mode.

---
textureMaxSize(tms): int
    properties: query, edit
    Set maximum texture size for hardware texturing.  The integer
value must be a power of 2.  Recommended values are 128 or 256.  If
the value specified is larger than the OpenGL maximim textures size
for the graphics hardware it will be clamped to the OpenGL size.  If
many large textures are used in a scene reducing this value improves
performance.  On Impact texture memory is pinned in RAM so using
large textures can cause reliability and performance problems. Again
reducing this value will help. Software rendering does not use this
value.
This flag is obsolete as of Maya 6.5. The maxTextureResolution/mtr
argument on the displayPref command should be used instead.

---
textureMemoryUsed(tmu): boolean
    properties: query
    Returns the total number of bytes used by all texture maps.  This
is typicly width*height*channels for all texture objects in the scene
If the texture is mip mapped all mip map levels are included in the
total though not never more than two level will be in use at one time

---
textureSampling(ts): int
    properties: query, edit
    Set the type of sampling to be used for texture
display. The argument can be either:

1 : means to perform point sample
2 : means to perform bilinear interpolation (default)

---
textures(tx): boolean
    properties: query, edit
    Turn on/off the display of texture objects for the view

---
transpInShadows(tis): boolean
    properties: query, edit
    Set whether to enable display of transparency in shadows when
using the hardware renderer. The default value is false.

---
transparencyAlgorithm(tal): string
    properties: query, edit
    Set the transparency algorithm.
The options are:

1) "frontAndBackCull" : Two pass front and back culling technique.
2) "perPolygonSort" : Draw transparent polygons in back-to-front order technique.

transparency pptions 1) and 2) are supported by the hardware renderer. Options 1) is
supported by the interactive modeling viewports.
The default value is "frontAndBackCull".

---
twoSidedLighting(tsl): boolean
    properties: query, edit
    Turns on or off two sided lighting.  This may be used with
the -default flag.

---
unParent(up): boolean
    properties: create, edit
    Specifies that the editor should be removed from its layout.
This cannot be used in query mode.

---
unlockMainConnection(ulk): boolean
    properties: create, edit
    Unlocks the mainConnection, effectively restoring the original
mainConnection (if it is still available), and dynamic updates.

---
updateColorMode(ucm): boolean
    properties: edit
    Using this flag tells the model panel to check which color
mode it should be in, and to switch accordingly.  This flag may
be used to update a model panel after a camera image plane has
been added or removed.

---
updateMainConnection(upd): boolean
    properties: create, edit
    Causes a locked mainConnection to be updated from the orginal
mainConnection, but preserves the lock state.

---
useBaseRenderer(ubr): boolean
    properties: query, edit
    Set whether to use the "base" renderer when using
the hardware renderer and in "interactive display mode" (-useInteractiveMode)
The default value is false.

---
useColorIndex(uci): boolean
    properties: query, edit
    Sets whether the model panel will attempt to use color index
mode when possible.  Color index mode can provide a performance
increase for point, bounding box, and wireframe display modes.
This may be used with the -default flag.

---
useCustomBackground(ucb): boolean
    properties: create, query, edit
    When set to true, instead of using the standard background, draw a solid
background using the viewColor.

---
useDefaultMaterial(udm): boolean
    properties: query, edit
    Sets whether the model panel will draw all the shaded surfaces
using the default material as opposed to using the material(s) currently
assigned to the surfaces.

---
useInteractiveMode(ui): boolean
    properties: query, edit
    Turns on or off the use of the special interaction settings
during playback.  This flag may be used with the -default flag.

---
useRGBImagePlane(ip): boolean
    properties: query, edit
    Sets whether the model panel will be forced into RGB mode
when there is an image plane attached to the panel's camera.

---
useReducedRenderer(urr): boolean
    properties: create, query, edit
    Set true if using the reduced renderer

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
userNode(un): string
    properties: query, edit
    Allows the user to associate a node name with the modelEditor.
The value is automatically updated in the event the node is deleted
or renamed.

---
viewColor(vc): [float, float, float, float]
    properties: create, query, edit
    Specifies the background color for the stereoscopic model editor. The
default value is black which provides optimal stereoscopic viewing.
This only applies if 'useCustomBackground' is on (which is the default).

---
viewObjects(vo): boolean
    properties: query
    Returns the name (if any) of the objectSet which contains the
list of objects visible in the view if viewSelected is true and the
list of objects being displayed does not come from the
active list.

---
viewSelected(vs): boolean
    properties: query, edit
    This flag turns on/off viewing of selected objects. When the
flag is set to true, the currently active objects are captured and
used as the list of objects to view.

---
viewType(vt): boolean
    properties: query
    Returns a string indicating the type of the model editor. For the
default model editor, returns the empty string. For custom model
editor types created via the API, returns the same string as is
returned via the method MPx3dModelView::viewType().

---
width(w): boolean
    properties: query
    Return the width of the associated viewport in pixels.

---
wireframeBackingStore(wbs): boolean
    properties: query, edit
    Sets whether a backing store is used to optimization the drawing
of active objects. This mode can provide a performance increase in
wireframe mode for certain scenes.

---
wireframeOnShaded(wos): boolean
    properties: query, edit
    Sets whether the model panel will draw the wireframe on
all shaded objects (if true) or only for active objects (if false).

---
xray(xr): boolean
    properties: query, edit
    Turns on or off Xray mode.  This may be used with the -default
flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/stereoCameraView.html 
    """


def stereoRigManager(flagaddRig: tuple[string, string, string], flagcameraSetFunc: tuple[string, string], flagcreationProcedure: tuple[string, string], flagdefaultRig: string, flagdelete: string, flaglanguage: tuple[string, string], flaglistRigs: boolean, flagrigDefinition: string) -> None:
    """Synopsis:
---
---
 stereoRigManager(
objects
    , [addRig=[string, string, string]], [cameraSetFunc=[string, string]], [creationProcedure=[string, string]], [defaultRig=string], [delete=string], [language=[string, string]], [listRigs=boolean], [rigDefinition=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

stereoRigManager is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Make sure the stereo plug-in is loaded
cmds.loadPlugin("stereoCamera", quiet=True)

Remember the default rig
defRigBefore = cmds.stereoRigManager(query=True, defaultRig=True)

Register new rig types, using MEL or Python implementations.
cmds.stereoRigManager(add=['StereoCameraHier', 'Python', 'maya.app.stereo.stereoCameraHierarchicalRig.createRig'])
cmds.stereoRigManager(add=['StereoCameraMulti', 'Python', 'maya.app.stereo.stereoCameraComplexRig.createRig'])
cmds.stereoRigManager(add=['StereoCameraSimple', 'MEL', 'stereoCameraSimpleRig'])

Make the second one the default rig
cmds.stereoRigManager(defaultRig='StereoCameraMulti')

Remove it
cmds.stereoRigManager(delete='StereoCameraMulti')

Query the default rig.
defRig = cmds.stereoRigManager(query=True, defaultRig=True)
print 'Default rig is now "'+defRig+'"'

Print the definition of each rig type
rigs = cmds.stereoRigManager(listRigs=True)
for rig in rigs:
  defs = cmds.stereoRigManager(rigDefinition=rig)
  print 'Rig "'+rig+'": (language '+defs[0]+') create callback: '+defs[1]

Cleanup after we are done
cmds.stereoRigManager(delete='myDefaultRig')
cmds.stereoRigManager(delete='mySimpleRig')
cmds.stereoRigManager(defaultRig=defRigBefore)

print 'After cleanup'

defRig = cmds.stereoRigManager(query=True, defaultRig=True)
print 'Default rig is now "'+defRig+'"'

rigs = cmds.stereoRigManager(listRigs=True)
for rig in rigs:
  defs = cmds.stereoRigManager(rigDefinition=rig)
  print 'Rig "'+rig+'": (language '+defs[0]+') create callback: '+defs[1]

---


Flags:
---


---
addRig(add): [string, string, string]
    properties: create
    Adds a new stereo rig definition. This flag takes 3 arguments:
name, language, create:

name: A unique name for the rig type.
lang: The language used for the callback. Valid values are
"Python" and "MEL". Use the Python interface when
possible.
create: Procedure used to create a new rig of this type. This
procedure takes no argument, and must return an array of strings.
The first element is the root DAG node of the rig. The second and
third elements are respectively the left and right cameras.

---
cameraSetFunc(csf): [string, string]
    properties: create
    Specifies the function to call when a rig is about to be added to
a camera set. This function must be the same language as originally
defined by the tool.

---
creationProcedure(cp): [string, string]
    properties: create
    Changes the creation procedure of an existing rig definition.

This flag takes 2 arguments: the name of the existing rig definition
and the procedure.

---
defaultRig(dr): string
    properties: create, query
    Sets the default rig tool. The argument must be the name of one of the
rigs added using the add flag.

Returns True if the default could be set, False otherwise.

---
delete(d): string
    properties: create
    Removes the definition of a stereo rig. The argument must be the name
of one of the rigs added using the add flag.

---
language(l): [string, string]
    properties: create
    Changes the language of an existing rig definition. Valid values are
"Python" and "MEL".

This flag takes 2 arguments: the name of the existing rig definition
and the language keyword.

---
listRigs(lr): boolean
    properties: create
    When present, returns the list of all defined rigs. All other flags
are ignored.

---
rigDefinition(rd): string
    properties: create
    Returns the definition of a rig, in the same format as the add
flag. A string array containing lang, create cameraSet.

If an empty string is passed as the argument, then the default rig is used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/stereoRigManager.html 
    """


def stitchSurface(flagbias: float, flagcaching: boolean, flagcascade: boolean, flagconstructionHistory: boolean, flagcvIthIndex: int, flagcvJthIndex: int, flagfixBoundary: boolean, flagkeepG0Continuity: boolean, flagkeepG1Continuity: boolean, flagname: string, flagnodeState: int, flagnumberOfSamples: int, flagobject: boolean, flagparameterU: float, flagparameterV: float, flagpositionalContinuity: boolean, flagreplaceOriginal: boolean, flagstepCount: int, flagtangentialContinuity: boolean, flagtogglePointNormals: boolean, flagtogglePointPosition: boolean, flagtoggleTolerance: boolean, flagtolerance: linear, flagweight0: float, flagweight1: float) -> list[string]:
    """Synopsis:
---
---
 stitchSurface(
[surfaceIsoparm] [surfaceIsoparm]
    , [bias=float], [caching=boolean], [cascade=boolean], [constructionHistory=boolean], [cvIthIndex=int], [cvJthIndex=int], [fixBoundary=boolean], [keepG0Continuity=boolean], [keepG1Continuity=boolean], [name=string], [nodeState=int], [numberOfSamples=int], [object=boolean], [parameterU=float], [parameterV=float], [positionalContinuity=boolean], [replaceOriginal=boolean], [stepCount=int], [tangentialContinuity=boolean], [togglePointNormals=boolean], [togglePointPosition=boolean], [toggleTolerance=boolean], [tolerance=linear], [weight0=float], [weight1=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

stitchSurface is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Stitch the two surfaces along the two specified surface isoparam with C0 continuity.
Since wt0 = 0.0, both the surfaces are stitched to surface2.vn[0] really.
cmds.stitchSurface( 'surface1.vn[1.0]', 'surface2.vn[0.0]', kg0=False, kg1=True, cascade=False, ns=100, wt0=0.0, wt1=1.0 )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
bias(b): float
    properties: create, query, edit
    Blend CVs in between input surface and result from stitch. A value of 0.0 returns the input surface.
Default: 1.0

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
cvIthIndex(ci): int
    properties: create, query, edit, multiuse
    The ith boundary CV index on the input surface.
Default: -1

---
cvJthIndex(cj): int
    properties: create, query, edit, multiuse
    The jth boundary CV index on the input surface.
Default: -1

---
fixBoundary(fb): boolean
    properties: create, query, edit
    Fix Boundary CVs while solving for any G1 constraints.
Default: false

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
parameterU(u): float
    properties: create, query, edit, multiuse
    The U parameter value on surface for a point constraint.
Default: -10000

---
parameterV(v): float
    properties: create, query, edit, multiuse
    The V parameter value on surface for a point constraint.
Default: -10000

---
positionalContinuity(pc): boolean
    properties: create, query, edit, multiuse
    Toggle on (off) G0 continuity at edge corresponding to multi index.
Default: true

---
stepCount(sc): int
    properties: create, query, edit, multiuse
    Step count for the number of discretizations.
Default: 20

---
tangentialContinuity(tc): boolean
    properties: create, query, edit, multiuse
    Toggle on (off) G1 continuity across edge corresponding to multi index.
Default: false

---
togglePointNormals(tpn): boolean
    properties: create, query, edit
    Toggle on (off) normal point constraints on the surface.
Default: false

---
togglePointPosition(tpp): boolean
    properties: create, query, edit
    Toggle on (off) position point constraints on the surface.
Default: true

---
toggleTolerance(tt): boolean
    properties: create, query, edit, multiuse
    Toggle on (off) so as to use Tolerance or specified steps for discretization.
Default: false

---
tolerance(tol): linear
    properties: create, query, edit, multiuse
    Tolerance to use while discretizing the edge.
Default: 0.1

---
cascade(c): boolean
    properties: create
    Cascade the created stitch node. (Only if the surface has a stitch
history)
Default is 'false'.

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
keepG0Continuity(kg0): boolean
    properties: create
    Stitch together with positional continuity.
Default is 'true'.

---
keepG1Continuity(kg1): boolean
    properties: create
    Stitch together with tangent continuity.
Default is 'false'.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
numberOfSamples(ns): int
    properties: create
    The number of samples on the edge.
Default is 20.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

---
weight0(wt0): float
    properties: create
    The weighting factor for the first edge.
Default is 0.5.

---
weight1(wt1): float
    properties: create
    The weighting factor for the second edge.
Default is 0.5.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/stitchSurface.html 
    """


def stitchSurfacePoints(flagbias: float, flagcaching: boolean, flagcascade: boolean, flagconstructionHistory: boolean, flagcvIthIndex: int, flagcvJthIndex: int, flagequalWeight: boolean, flagfixBoundary: boolean, flagkeepG0Continuity: boolean, flagkeepG1Continuity: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagparameterU: float, flagparameterV: float, flagpositionalContinuity: boolean, flagreplaceOriginal: boolean, flagstepCount: int, flagtangentialContinuity: boolean, flagtogglePointNormals: boolean, flagtogglePointPosition: boolean, flagtoggleTolerance: boolean, flagtolerance: linear) -> list[string]:
    """Synopsis:
---
---
 stitchSurfacePoints(
selectionList
    , [bias=float], [caching=boolean], [cascade=boolean], [constructionHistory=boolean], [cvIthIndex=int], [cvJthIndex=int], [equalWeight=boolean], [fixBoundary=boolean], [keepG0Continuity=boolean], [keepG1Continuity=boolean], [name=string], [nodeState=int], [object=boolean], [parameterU=float], [parameterV=float], [positionalContinuity=boolean], [replaceOriginal=boolean], [stepCount=int], [tangentialContinuity=boolean], [togglePointNormals=boolean], [togglePointPosition=boolean], [toggleTolerance=boolean], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

stitchSurfacePoints is undoable, queryable, and editable.
Note: No two points can lie on the same surface.




Example:
---
import maya.cmds as cmds

stitch together four corner control vertices to the average of the four corners.
cmds.stitchSurfacePoints( 'nurbsPlane2.cv[0][0]', 'nurbsPlane1.cv[3][0]', 'nurbsPlane4.cv[0][3]', 'nurbsPlane3.cv[3][3]', ewt=True )

stitch together two edit points to the edit point nurbsPlane2.ep[0][0].
cmds.stitchSurfacePoints( 'nurbsPlane2.ep[0][0]', 'nurbsPlane1.ep[1][0]', ewt=False )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
bias(b): float
    properties: create, query, edit
    Blend CVs in between input surface and result from stitch. A value of 0.0 returns the input surface.
Default: 1.0

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
cvIthIndex(ci): int
    properties: create, query, edit, multiuse
    The ith boundary CV index on the input surface.
Default: -1

---
cvJthIndex(cj): int
    properties: create, query, edit, multiuse
    The jth boundary CV index on the input surface.
Default: -1

---
fixBoundary(fb): boolean
    properties: create, query, edit
    Fix Boundary CVs while solving for any G1 constraints.
Default: false

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
parameterU(u): float
    properties: create, query, edit, multiuse
    The U parameter value on surface for a point constraint.
Default: -10000

---
parameterV(v): float
    properties: create, query, edit, multiuse
    The V parameter value on surface for a point constraint.
Default: -10000

---
positionalContinuity(pc): boolean
    properties: create, query, edit, multiuse
    Toggle on (off) G0 continuity at edge corresponding to multi index.
Default: true

---
stepCount(sc): int
    properties: create, query, edit, multiuse
    Step count for the number of discretizations.
Default: 20

---
tangentialContinuity(tc): boolean
    properties: create, query, edit, multiuse
    Toggle on (off) G1 continuity across edge corresponding to multi index.
Default: false

---
togglePointNormals(tpn): boolean
    properties: create, query, edit
    Toggle on (off) normal point constraints on the surface.
Default: false

---
togglePointPosition(tpp): boolean
    properties: create, query, edit
    Toggle on (off) position point constraints on the surface.
Default: true

---
toggleTolerance(tt): boolean
    properties: create, query, edit, multiuse
    Toggle on (off) so as to use Tolerance or specified steps for discretization.
Default: false

---
tolerance(tol): linear
    properties: create, query, edit, multiuse
    Tolerance to use while discretizing the edge.
Default: 0.1

---
cascade(c): boolean
    properties: create
    Cascade the created stitch node. (Only if the surface has a stitch
history)
Default is 'false'.

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
equalWeight(ewt): boolean
    properties: create
    Assign equal weights to all the points being stitched together.
Default is 'true'. If false, the first point is assigned a weight of
1.0 and the rest are assigned 0.0.

---
keepG0Continuity(kg0): boolean
    properties: create
    Stitch together the points with positional continuity.
Default is 'true'.

---
keepG1Continuity(kg1): boolean
    properties: create
    Stitch together the points with tangent continuity.
Default is 'false'.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/stitchSurfacePoints.html 
    """


def stringArrayIntersector(flagallowDuplicates: boolean, flagdefineTemplate: string, flagexists: boolean, flagintersect: list[string], flagreset: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 stringArrayIntersector(
string
    , [allowDuplicates=boolean], [defineTemplate=string], [exists=boolean], [intersect=string[]], [reset=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

stringArrayIntersector is undoable, queryable, and editable.
Note that the string intersector object may be deleted using the deleteUI
command.




Example:
---
import maya.cmds as cmds

Create an intersector
---

myIntersector = cmds.stringArrayIntersector('stringArrayIntersector')

Intersect some string arrays using the intersector
---

initialArray = ['Excellent', 'Smithers', 'doh']
cmds.stringArrayIntersector( myIntersector, edit=True, intersect=initialArray )
cmds.stringArrayIntersector( myIntersector, edit=True, intersect=['Smithers', 'Homer'] )

Query the intersector to see what the intersection is so far
---

cmds.stringArrayIntersector( myIntersector, query=True )
Result: Smithers ---


Reset the intersector so that you can use it again with new string
arrays
---

cmds.stringArrayIntersector( myIntersector, edit=True, reset=True )

Delete the intersector as we are now done with it
---

cmds.deleteUI( myIntersector )

---
Return:
---


    string: The name of the intersector.

Flags:
---


---
allowDuplicates(ad): boolean
    properties: create
    Should the intersector allow duplicates in the input arrays (true),
or combine all duplicate entries into a single, unique entry (false).
This flag must be used when initially creating the intersector.
Default is 'false'.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
intersect(i): string[]
    properties: create, edit
    Intersect the specified string array with the current intersection
being maintained by the intersector.

---
reset(r): boolean
    properties: edit
    Reset the intersector to begin a new intersection.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/stringArrayIntersector.html 
    """


def stroke(flagname: string, flagpressure: boolean, flagseed: int) -> string:
    """Synopsis:
---
---
 stroke(
[string]
    , [name=string], [pressure=boolean], [seed=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

stroke is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.stroke( s=10, n='armScar' )

---
Return:
---


    string: (The path to the new stroke or the replaced stroke)

Flags:
---


---
name(n): string
    properties: create
    Sets the name of the stroke to the input string

---
pressure(pr): boolean
    properties: create
    On creation, allows the copying of the pressure
mapping settings from the Paint Effects Tool. Default
is false.

---
seed(s): int
    properties: create
    Sets the random seed for this stroke.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/stroke.html 
    """


def subdAutoProjection(flagcaching: boolean, flagconstructionHistory: boolean, flaglayout: int, flaglayoutMethod: int, flagname: string, flagnodeState: int, flagoptimize: int, flagpercentageSpace: float, flagplanes: int, flagscale: int, flagskipIntersect: boolean, flagworldSpace: boolean) -> string:
    """Synopsis:
---
---
 subdAutoProjection(
selectionList
    , [caching=boolean], [constructionHistory=boolean], [layout=int], [layoutMethod=int], [name=string], [nodeState=int], [optimize=int], [percentageSpace=float], [planes=int], [scale=int], [skipIntersect=boolean], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdAutoProjection is undoable, queryable, and editable.
The argument is a face selection list.




Example:
---
import maya.cmds as cmds

Create a subd sphere with default UVs.
mel.eval( "createSubdSphereProc" )

Automatic projections with 6 planes.
cmds.subdAutoProjection( 'subdivSphere1.smf[*][*]' )

---
Return:
---


    string: The node name.

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
layout(l): int
    properties: create, query, edit
    What layout algorithm should be used:
0 UV pieces are aligned along the U axis.
1 UV pieces are moved in a square shape.

---
layoutMethod(lm): int
    properties: create, query, edit
    Which layout method to use:
0 Block Stacking.
1 Shape Stacking.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
optimize(o): int
    properties: create, query, edit
    Use two different flavors for the cut generation.
0 Every face is assigned to the best plane. This optimizes the
map distortion.
1 Small UV pieces are incorporated into larger ones, when the
extra distortion introduced is reasonable. This tends to produce fewer
UV pieces.

---
percentageSpace(ps): float
    properties: create, query, edit
    When layout is set to square, this value is a percentage of
the texture area which is added around each UV piece. It can be
used to ensure each UV piece uses different pixels in the texture.
Maximum value is 5 percent.

---
planes(p): int
    properties: create, query, edit
    Number of intermediate projections used. Valid numbers
are 4, 5, 6, 8, and 12.
C: Default is 6.

---
scale(sc): int
    properties: create, query, edit
    How to scale the pieces, after projections:
0 No scale is applied.
1 Uniform scale to fit in unit square.
2 Non proportional scale to fit in unit square.

---
skipIntersect(si): boolean
    properties: create, query, edit
    When on, self intersection of UV pieces are not
tested. This makes the projection faster and produces fewer pieces,
but may lead to overlaps in UV space.

---
worldSpace(ws): boolean
    properties: create, query, edit
    This flag specifies which reference to use.
If "on" : all geometrical values are taken in world reference.
If "off" : all geometrical values are taken in object reference.
C: Default is "off".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdAutoProjection.html 
    """


def subdCleanTopology() -> boolean:
    """Synopsis:
---
---
 subdCleanTopology()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdCleanTopology is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

To clean topology of two subdiv surfaces.
cmds.subdCleanTopology( 'surface', 'surface2' )

---
Return:
---


    boolean: Success or Failure.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdCleanTopology.html 
    """


def subdCollapse(flagcaching: boolean, flagconstructionHistory: boolean, flaglevel: int, flagname: string, flagnodeState: int, flagobject: boolean) -> list[string]:
    """Synopsis:
---
---
 subdCollapse(
[string]
    , [caching=boolean], [constructionHistory=boolean], [level=int], [name=string], [nodeState=int], [object=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdCollapse is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new subd surface whose level 0 (base mesh) matches
the level 3 vertices of the given surface.
cmds.subdCollapse( 'subdivShape1', level=3 )

---
Return:
---


    list[string]: The subd surface and optionally the dependency node name

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
level(l): int
    properties: create, query, edit
    The level that will now become the base mesh.
Default: 0

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdCollapse.html 
    """


def subdDuplicateAndConnect() -> None:
    """Synopsis:
---
---
 subdDuplicateAndConnect(
object
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdDuplicateAndConnect is undoable, NOT queryable, and NOT editable.
The command will fail if no objects are selected or sent as
argument or if the object sent as argument is not a subdivision surface
object.





Example:
---
import maya.cmds as cmds

cmds.subdDuplicateAndConnect( 'pSubd1' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdDuplicateAndConnect.html 
    """


def subdEditUV(flagangle: float, flagpivotU: float, flagpivotV: float, flagrelative: boolean, flagrotateRatio: float, flagrotation: boolean, flagscale: boolean, flagscaleU: float, flagscaleV: float, flaguValue: float, flaguvSetName: string, flagvValue: float) -> boolean:
    """Synopsis:
---
---
 subdEditUV([angle=float], [pivotU=float], [pivotV=float], [relative=boolean], [rotateRatio=float], [rotation=boolean], [scale=boolean], [scaleU=float], [scaleV=float], [uValue=float], [uvSetName=string], [vValue=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdEditUV is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

To tweak the u and v values of selected uvs:
cmds.subdEditUV( relative=True, uValue=0.05925926, vValue=0.05555556 )

To set absolute values for u and v values of selected uvs:
cmds.subdEditUV( relative=False, uValue=0.556, vValue=0.56 )

To rotate selected uv points about a pivot:
cmds.subdEditUV( pivotU=0.5, pivotV=0.5, angle=-15 )

To scale selected uv points about a pivot:
cmds.subdEditUV( pivotU=0.5, pivotV=0.5, scaleU=-0.06, scaleV=-0.06 )

---
Return:
---


    boolean: Success or Failure.

Flags:
---


---
angle(a): float
    properties: create, query
    Specifies the angle value (in degrees) that the uv values are to be rotated
by.

---
pivotU(pu): float
    properties: create, query
    Specifies the pivot value, in the u direction, about which the scale or
rotate is to be performed.

---
pivotV(pv): float
    properties: create, query
    Specifies the pivot value, in the v direction, about which the scale or
rotate is to be performed.

---
relative(r): boolean
    properties: create, query
    Specifies whether this command is editing the values relative to the currently
existing values. Default is true;

---
rotateRatio(rr): float
    properties: create, query
    Specifies the ratio value that the uv values are to be rotated by
Default is 1.0

---
rotation(rot): boolean
    properties: create, query
    Specifies whether this command is editing the values with rotation values

---
scale(s): boolean
    properties: create, query
    Specifies whether this command is editing the values with scale values

---
scaleU(su): float
    properties: create, query
    Specifies the scale value in the u direction.

---
scaleV(sv): float
    properties: create, query
    Specifies the scale value in the v direction.

---
uValue(u): float
    properties: create, query
    Specifies the value, in the u direction - absolute if relative flag is false..

---
uvSetName(uvs): string
    properties: create, query
    Specifies the name of the uv set to edit uvs on. If not specified
will use the current uv set if it exists.

---
vValue(v): float
    properties: create, query
    Specifies the value, in the v direction - absolute if relative flag is false..

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdEditUV.html 
    """


def subdLayoutUV(flagcaching: boolean, flagconstructionHistory: boolean, flagflipReversed: boolean, flaglayout: int, flaglayoutMethod: int, flagname: string, flagnodeState: int, flagpercentageSpace: float, flagrotateForBestFit: int, flagscale: int, flagseparate: int, flagworldSpace: boolean) -> string:
    """Synopsis:
---
---
 subdLayoutUV([caching=boolean], [constructionHistory=boolean], [flipReversed=boolean], [layout=int], [layoutMethod=int], [name=string], [nodeState=int], [percentageSpace=float], [rotateForBestFit=int], [scale=int], [separate=int], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdLayoutUV is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a cube
mel.eval( "createSubdCubeProc" )

Layout all UVs in the texture plane.
cmds.subdLayoutUV( 'subdivCube1.smf[*][*]', l=2, fr=True, se=2, sc=1 )

---
Return:
---


    string: The node name.

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
flipReversed(fr): boolean
    properties: create, query, edit
    If this flag is turned on, the reversed UV pieces are fliped.

---
layout(l): int
    properties: create, query, edit
    How to move the UV pieces, after cuts are applied:
0 No move is applied.
1 Layout the pieces along the U axis.
2 Layout the pieces in a square shape.

---
layoutMethod(lm): int
    properties: create, query, edit
    Which layout method to use:
0 Block Stacking.
1 Shape Stacking.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
percentageSpace(ps): float
    properties: create, query, edit
    When layout is set to square, this value is a percentage of
the texture area which is added around each UV piece. It can be
used to ensure each UV piece uses different pixels in the texture.
Maximum value is 5 percent.

---
rotateForBestFit(rbf): int
    properties: create, query, edit
    0 No rotation is applied.
1 Only allow 90 degree rotations.
2 Allow free rotations.

---
scale(sc): int
    properties: create, query, edit
    How to scale the pieces, after move and cuts:
0 No scale is applied.
1 Uniform scale to fit in unit square.
2 Non proportional scale to fit in unit square.

---
separate(se): int
    properties: create, query, edit
    Which UV edges should be cut:
0 No cuts.
1 Cut only along folds.
2 Make all necessary cuts to avoid all intersections.

---
worldSpace(ws): boolean
    properties: create, query, edit
    If true, performs the operation in world space coordinates as
opposed to local space.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdLayoutUV.html 
    """


def subdListComponentConversion(flagborder: boolean, flagfromEdge: boolean, flagfromFace: boolean, flagfromUV: boolean, flagfromVertex: boolean, flaginternal: boolean, flagtoEdge: boolean, flagtoFace: boolean, flagtoUV: boolean, flagtoVertex: boolean, flaguvShell: boolean, flaguvShellBorder: boolean) -> list[string]:
    """Synopsis:
---
---
 subdListComponentConversion(
[objects...]
    , [border=boolean], [fromEdge=boolean], [fromFace=boolean], [fromUV=boolean], [fromVertex=boolean], [internal=boolean], [toEdge=boolean], [toFace=boolean], [toUV=boolean], [toVertex=boolean], [uvShell=boolean], [uvShellBorder=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdListComponentConversion is undoable, NOT queryable, and NOT editable.
Use the "-in/internal" flag to specify conversion to
"connected" vs. "contained" components.  For example,
if the internal flag is specified when converting
from subdivision surface vertices to faces, then
only faces that are entirely contained by the vertices
will be returned.  If the internal flag is not specified,
then all faces that are connected to the vertices will
be returned.




Example:
---
import maya.cmds as cmds

cmds.subdListComponentConversion( 'subdShape.smp[5][6]', 'subdShape.smp[9][10]', fv=True, tf=True )
Returns a list of faces that are connected to the given vertices.

cmds.subdListComponentConversion( 'subdShape.sme[0][0]', 'subdShape.smp[3][0]', 'subdShape.smp[8][0]', tf=True )
Returns a list of faces that are connected to the given components.

cmds.subdListComponentConversion( 'subdShape.smp[5][9]', fv=True, tf=True, in=True )
Returns a list of only those faces that are completely contained
by the given vertices.

cmds.select( 'subdShape.smp[0][0]', 'subdShape.smp[3][0]', 'subdShape.smp[8][0]', r=True )
cmds.subdListComponentConversion( fv=True, tf=True )
Returns the conversion of selected vertices to faces.

cmds.subdListComponentConversion( 'subdShape.smm[3]', fuv=True, tuv=True, uvs=True )
Returns a list of all UV map components in the
same UV shell (contiguous region in texture space).
(You can view these regions in the UV Editor.)

cmds.subdListComponentConversion( 'subdShape.smm[3]', fuv=True, tuv=True, uvb=True )
Returns a list of the UV map components on the border of the
same UV shell (contiguous region in texture space).  (You can
view these regions in the UV Editor.)

---
Return:
---


    list[string]: List of subdivision surface components

Flags:
---


---
border(bo): boolean
    properties: create
    Convert to a border.

---
fromEdge(fe): boolean
    properties: create
    Indicates the component type to convert
from: Edges

---
fromFace(ff): boolean
    properties: create
    Indicates the component type to convert
from: Faces

---
fromUV(fuv): boolean
    properties: create
    Indicates the component type to convert
from: UVs

---
fromVertex(fv): boolean
    properties: create
    Indicates the component type to convert
from: Vertex

---
internal(internal): boolean
    properties: create
    Applicable when converting from
"smaller" component types to larger ones.
Specifies conversion to "connected" vs.
"contained" components.
See examples below.

---
toEdge(te): boolean
    properties: create
    Indicates the component type to convert
to: Edges

---
toFace(tf): boolean
    properties: create
    Indicates the component type to convert
to: Faces

---
toUV(tuv): boolean
    properties: create
    Indicates the component type to convert
to: UVs

---
toVertex(tv): boolean
    properties: create
    Indicates the component type to convert
to: Vertices

---
uvShell(uvs): boolean
    properties: create
    Will return UV components within the same UV
shell. Only works with -tuv and -fuv flags.

---
uvShellBorder(uvb): boolean
    properties: create
    Will return UV components on the border
within the same UV shell. Only works with
-tuv and -fuv flags.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdListComponentConversion.html 
    """


def subdMapCut(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int) -> string:
    """Synopsis:
---
---
 subdMapCut([caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdMapCut is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Opening up the textureView will make this example much easier to visualize.

Create a cube
mel.eval( "createSubdCube" )

Cut the map.
cmds.subdMapCut( 'subdivCube1.sme[2560][2]', 'subdivCube1.sme[2816][2]' )
now that it's cut, we may move the row separately

Move some UVs
cmds.subdEditUV( 'subdivCube1.smm[21:22]', 'subdivCube1.smm[25]', u=0, v=0.05 )

---
Return:
---


    string: The node name.

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdMapCut.html 
    """


def subdMapSewMove(flagcaching: boolean, flagconstructionHistory: boolean, flaglimitPieceSize: boolean, flagname: string, flagnodeState: int, flagnumberFaces: int, flagworldSpace: boolean) -> string:
    """Synopsis:
---
---
 subdMapSewMove(
selectionList
    , [caching=boolean], [constructionHistory=boolean], [limitPieceSize=boolean], [name=string], [nodeState=int], [numberFaces=int], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdMapSewMove is undoable, queryable, and editable.
The argument is a UV selection list.




Example:
---
import maya.cmds as cmds

Create a subd sphere with default UVs.
import maya.mel as mel
mel.eval( "createSubdSphere" )

Automatic projections with 6 planes.
cmds.subdAutoProjection( 'subdivSphere1.smf[*][*]' )

Select the seams
cmds.select( 'subdivSphere1.sme[0:1][67108864]', 'subdivSphere1.sme[256][67108867]', 'subdivSphere1.sme[513][67108864]' )

merge them, with the appropriate move.
cmds.subdMapSewMove()

---
Return:
---


    string: The node name.

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
limitPieceSize(lps): boolean
    properties: create, query, edit
    When on, this flag specifies that the face number limit
described above should be used.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
numberFaces(nf): int
    properties: create, query, edit
    Maximum number of faces in a UV piece. When trying to
combine two UV pieces into a single one, the merge operation is
rejected if the smaller piece has more faces than the number specified
by this flag.
This flag is only used when limitPieceSize is set to on.

---
worldSpace(ws): boolean
    properties: create, query, edit
    If true, performs the operation in world space coordinates as
opposed to local space.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdMapSewMove.html 
    """


def subdMatchTopology(flagfrontOfChain: boolean) -> boolean:
    """Synopsis:
---
---
 subdMatchTopology([frontOfChain=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdMatchTopology is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

To match topology across two subdiv surfaces.
cmds.subdMatchTopology( 'surface', 'surface2' )

---
Return:
---


    boolean: Success or Failure.

Flags:
---


---
frontOfChain(foc): boolean
    properties: create
    This command is used to specify that the new addTopology node should be
placed ahead (upstream) of existing deformer and skin nodes in the shape's
history (but not ahead of existing tweak nodes). The input to the addTopology
node will be the upstream shape rather than the visible downstream shape, so
the behavior of this flag is the most intuitive if the downstream deformers
are in their reset (hasNoEffect) position when the new deformer is added.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdMatchTopology.html 
    """


def subdMirror(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagxMirror: boolean, flagyMirror: boolean, flagzMirror: boolean) -> list[string]:
    """Synopsis:
---
---
 subdMirror(
[string]
    , [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean], [xMirror=boolean], [yMirror=boolean], [zMirror=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdMirror is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new subd surface mirrored in the X direction.
cmds.subdMirror( 'subdivShape1', xMirror=True )

---
Return:
---


    list[string]: The subdivision surface and optionally the dependency node name

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
xMirror(xm): boolean
    properties: create, query, edit
    Mirror the vertices in X
Default: false

---
yMirror(ym): boolean
    properties: create, query, edit
    Mirror the vertices in Y
Default: false

---
zMirror(zm): boolean
    properties: create, query, edit
    Mirror the vertices in Z
Default: false

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdMirror.html 
    """


def subdPlanarProjection(flagcaching: boolean, flagconstructionHistory: boolean, flagcreateNewMap: boolean, flagimageCenter: tuple[float, float], flagimageCenterX: float, flagimageCenterY: float, flagimageScale: tuple[float, float], flagimageScaleU: float, flagimageScaleV: float, flaginsertBeforeDeformers: boolean, flagkeepImageRatio: boolean, flagmapDirection: string, flagname: string, flagnodeState: int, flagprojectionCenter: tuple[linear, linear, linear], flagprojectionCenterX: linear, flagprojectionCenterY: linear, flagprojectionCenterZ: linear, flagprojectionHeight: linear, flagprojectionScale: tuple[linear, linear], flagprojectionWidth: linear, flagrotate: tuple[angle, angle, angle], flagrotateX: angle, flagrotateY: angle, flagrotateZ: angle, flagrotationAngle: angle, flagsmartFit: boolean, flagworldSpace: boolean) -> string:
    """Synopsis:
---
---
 subdPlanarProjection([caching=boolean], [constructionHistory=boolean], [createNewMap=boolean], [imageCenter=[float, float]], [imageCenterX=float], [imageCenterY=float], [imageScale=[float, float]], [imageScaleU=float], [imageScaleV=float], [insertBeforeDeformers=boolean], [keepImageRatio=boolean], [mapDirection=string], [name=string], [nodeState=int], [projectionCenter=[linear, linear, linear]], [projectionCenterX=linear], [projectionCenterY=linear], [projectionCenterZ=linear], [projectionHeight=linear], [projectionScale=[linear, linear]], [projectionWidth=linear], [rotate=[angle, angle, angle]], [rotateX=angle], [rotateY=angle], [rotateZ=angle], [rotationAngle=angle], [smartFit=boolean], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdPlanarProjection is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a cube
mel.eval( "createSubdCubeProc" )

Layout all UVs in the texture plane.
cmds.subdPlanarProjection( 'subdivCube1.smf[*][*]',  rx=90, ra=45.0, pc= (0, 0, 0), imageScale=(0.5, 0.5))

---
Return:
---


    string: The node name.

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
createNewMap(cm): boolean
    properties: create, query, edit
    This flag when set true will create a new map with
a the name passed in, if the map does not already exist.

---
imageCenter(ic2): [float, float]
    properties: create, query, edit
    This flag specifies the center point of the 2D model layout.
C: Default is 0.5 0.5.
Q: When queried, this flag returns a float[2].

---
imageCenterX(icx): float
    properties: create, query, edit
    This flag specifies X for the center point of the 2D model layout.
C: Default is 0.5.
Q: When queried, this flag returns a float.

---
imageCenterY(icy): float
    properties: create, query, edit
    This flag specifies Y for the center point of the 2D model layout.
C: Default is 0.5.
Q: When queried, this flag returns a float.

---
imageScale(is2): [float, float]
    properties: create, query, edit
    This flag specifies the UV scale : Enlarges or reduces the 2D version of the model in U or V space relative to the 2D centerpoint.
C: Default is 1.0 1.0.
Q: When queried, this flag returns a float[2].

---
imageScaleU(isu): float
    properties: create, query, edit
    This flag specifies the U scale : Enlarges or reduces the 2D version of the model in U space relative to the 2D centerpoint.
C: Default is 1.0.
Q: When queried, this flag returns a float.

---
imageScaleV(isv): float
    properties: create, query, edit
    This flag specifies the V scale : Enlarges or reduces the 2D version of the model in V space relative to the 2D centerpoint.
C: Default is 1.0.
Q: When queried, this flag returns a float.

---
insertBeforeDeformers(ibd): boolean
    properties: create
    This flag specifies if the projection node should be inserted before
or after deformer nodes already applied to the shape. Inserting the
projection after the deformer leads to texture swimming during
animation and is most often undesirable.
C: Default is on.

---
keepImageRatio(kir): boolean
    properties: create
    True means keep any image ratio

---
mapDirection(md): string
    properties: create
    This flag specifies the mapping direction.
'x', 'y' and 'z' projects the map along the corresponding axis.
'c' projects along the current camera viewing direction.
'p' does perspective projection if current camera is perspective.
'b' projects along the best plane fitting the objects selected.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
projectionCenter(pc): [linear, linear, linear]
    properties: create, query, edit
    This flag specifies the origin point from which the map is projected.
C: Default is 0.0 0.0 0.0.
Q: When queried, this flag returns a float[3].

---
projectionCenterX(pcx): linear
    properties: create, query, edit
    This flag specifies X for the origin point from which the map is projected.
C: Default is 0.0.
Q: When queried, this flag returns a float.

---
projectionCenterY(pcy): linear
    properties: create, query, edit
    This flag specifies Y for the origin point from which the map is projected.
C: Default is 0.0.
Q: When queried, this flag returns a float.

---
projectionCenterZ(pcz): linear
    properties: create, query, edit
    This flag specifies Z for the origin point from which the map is projected.
C: Default is 0.0.
Q: When queried, this flag returns a float.

---
projectionHeight(ph): linear
    properties: create, query, edit
    This flag specifies the height of the map relative to the 3D projection axis.
C: Default is 1.0
Q: When queried, this flag returns a float.

---
projectionScale(ps): [linear, linear]
    properties: create, query, edit
    This flag specifies the width and the height of the map relative to the 3D projection axis.
C: Default is 1.0 1.0.
Q: When queried, this flag returns a float[2].

---
projectionWidth(pw): linear
    properties: create, query, edit
    This flag specifies the width of the map relative to the 3D projection axis.
C: Default is 1.0
Q: When queried, this flag returns a float.

---
rotate(ro): [angle, angle, angle]
    properties: create, query, edit
    This flag specifies the mapping rotate angles.
C: Default is 0.0 0.0 0.0.
Q: When queried, this flag returns a float[3].

---
rotateX(rx): angle
    properties: create, query, edit
    This flag specifies X mapping rotate angle.
C: Default is 0.0.
Q: When queried, this flag returns a float[3].

---
rotateY(ry): angle
    properties: create, query, edit
    This flag specifies Y mapping rotate angle.
C: Default is 0.0.
Q: When queried, this flag returns a float.

---
rotateZ(rz): angle
    properties: create, query, edit
    This flag specifies Z mapping rotate angle.
C: Default is 0.0.
Q: When queried, this flag returns a float.

---
rotationAngle(ra): angle
    properties: create, query, edit
    This flag specifies the rotation angle in the mapping space.
When the angle is positive, then the map rotates
counterclockwise on the mapped model, whereas when it is
negative then the map rotates lockwise on the mapped model.
C: Default is 10.0.
Q: When queried, this flag returns a float.

---
smartFit(sf): boolean
    properties: create
    True means use the smart fit algorithm

---
worldSpace(ws): boolean
    properties: create, query, edit
    This flag specifies which reference to use.
If "on" : all geometrical values are taken in world reference.
If "off" : all geometrical values are taken in object reference.
C: Default is "off".
Q: When queried, this flag returns an int.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdPlanarProjection.html 
    """


def subdToBlind(flagabsolutePosition: boolean, flagincludeCreases: boolean, flagincludeZeroOffsets: boolean) -> boolean:
    """Synopsis:
---
---
 subdToBlind([absolutePosition=boolean], [includeCreases=boolean], [includeZeroOffsets=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdToBlind is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.subdToBlind( 'subdShape1', 'polyShape4' )

---
Return:
---


    boolean: Command result

Flags:
---


---
absolutePosition(ap): boolean
    properties: create
    If set to true, the hierarchical edits are represented as the point positions,
not the point offsets.  Most of the time, this is not desirable, but if you're
just going to be merging/deleting a bunch of things and not move any vertices,
then you could set it to true.  False is the default and saves the offsets.

---
includeCreases(ic): boolean
    properties: create
    If set, the creases get transfered as well.  With it false, the subdivision
surface created from the blind data + polygon will have lost all the craese
information.  The default is false.

---
includeZeroOffsets(izo): boolean
    properties: create
    If set, the zero offset will get included in the blind data.  This will
greatly increase the size of the blind data, but will also let you keep
all created vertices in the conversion back to polys.  This flag does
not change the behaviour for the vertices up to and including level 2
as they're always created.  If not set, only the edited vertices will
be included in the blind data.  This will still maintain the shape of
your object faithfully.  The default is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdToBlind.html 
    """


def subdToPoly(flagaddUnderTransform: boolean, flagapplyMatrixToResult: boolean, flagcaching: boolean, flagconnectShaders: boolean, flagconstructionHistory: boolean, flagcopyUVTopology: boolean, flagdepth: int, flagextractPointPosition: boolean, flagformat: int, flaginSubdCVId: tuple[int, int], flaginSubdCVIdLeft: int, flaginSubdCVIdRight: int, flagmaxPolys: int, flagname: string, flagnodeState: int, flagobject: boolean, flagoutSubdCVId: tuple[int, int], flagoutSubdCVIdLeft: int, flagoutSubdCVIdRight: int, flagoutv: int, flagpreserveVertexOrdering: boolean, flagsampleCount: int, flagshareUVs: boolean, flagsubdNormals: boolean) -> list[string]:
    """Synopsis:
---
---
 subdToPoly(
[subd]
    , [addUnderTransform=boolean], [applyMatrixToResult=boolean], [caching=boolean], [connectShaders=boolean], [constructionHistory=boolean], [copyUVTopology=boolean], [depth=int], [extractPointPosition=boolean], [format=int], [inSubdCVId=[int, int]], [inSubdCVIdLeft=int], [inSubdCVIdRight=int], [maxPolys=int], [name=string], [nodeState=int], [object=boolean], [outSubdCVId=[int, int]], [outSubdCVIdLeft=int], [outSubdCVIdRight=int], [outv=int], [preserveVertexOrdering=boolean], [sampleCount=int], [shareUVs=boolean], [subdNormals=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdToPoly is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new polygon from a subdivision surface:
cmds.subdToPoly( 'subd1' )

---
Return:
---


    list[string]: The polygon and optionally the dependency node name

Flags:
---


---
applyMatrixToResult(amr): boolean
    properties: create, query, edit
    If true, the matrix on the input geometry is applied to the object
and the resulting geometry will have identity matrix on it.  If false
the conversion is done on the local space object and the resulting
geometry has the input object's matrix on it.
Default: true

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
copyUVTopology(cut): boolean
    properties: create, query, edit
    Copy over uv topology (shared/unshared) from the original subdivision
surface to the converted polygonal mesh.
Default: false

---
depth(d): int
    properties: create, query, edit
    The depth at which constant-depth tessellates the surface
Default: 0

---
extractPointPosition(epp): boolean
    properties: create, query, edit
    Determines how the position of a mesh point is calculated
If on the position of the mesh point is returned. If off the
position of the point of the surface is returned.
Default: false

---
format(f): int
    properties: create, query, edit
    Format:

0 - Uniform
1 - Adaptive
2 - Polygon Count
3 - Vertices

Default: 0

---
inSubdCVId(inSubdCVId): [int, int]
    properties: create, query, edit, multiuse
    Input CV Id

---
inSubdCVIdLeft(isl): int
    properties: create, query, edit
    Higher 32 bit integer of the input CV Id

---
inSubdCVIdRight(isr): int
    properties: create, query, edit
    Lower 32 bit integer of the input CV Id

---
maxPolys(mp): int
    properties: create, query, edit
    The maximum number of polygons at which by polygons tessellates.
If this attribute is greater than zero, it will override the
sample count and depth attributes.
Default: 0

---
nodeState(nds): int
    properties: create, query, edit
    Maya dependency nodes have 6 possible states.
The Normal (0), HasNoEffect (1), and Blocking (2) states can be
used to alter how the graph is evaluated.



The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)
are for internal use only. They temporarily shut off parts of the graph during interaction
(e.g., manipulation). The understanding is that once the operation is done,
the state will be reset appropriately, e.g. Waiting-Blocking will reset
back to Blocking.



The Normal and Blocking cases apply to all nodes, while
HasNoEffect is node specific; many nodes do not support this option.
Plug-ins store state in the MPxNode::state attribute. Anyone can set
it or check this attribute.  Additional details about each of these 3 states follow.




State
Description


Normal
The normal node state. This is the default.


HasNoEffect


The HasNoEffect option (a.k.a. pass-through), is used in cases where
there is an operation on an input producing an output of the same data type.
Nearly all deformers support this state, as do a few other nodes.
As stated earlier, it is not supported by all nodes.


It’s typical to implement support for the HasNoEffect state in
the node’s compute method and to perform appropriate operations.
Plug-ins can also support HasNoEffect.


The usual implementation of this state is to copy the input directly to the
matching output without applying the algorithm in the node. For deformers,
applying this state leaves the input geometry undeformed on the output.




Blocking


This is implemented in the depend node base class and applies to all nodes.
Blocking is applied during the evaluation phase to connections.
An evaluation request to a blocked connection will return as failures,
causing the destination plug to retain its current value. Dirty propagation
is indirectly affected by this state since blocked connections are never cleaned.


When a node is set to Blocking the behavior is supposed to be the same as
if all outgoing connections were broken. As long as nobody requests evaluation
of the blocked node directly it won’t evaluate after that. Note that a blocked
node will still respond to getAttr requests but a getAttr on a
downstream node will not reevaluate the blocked node.


Setting the root transform of a hierarchy to Blocking won’t automatically
influence child transforms in the hierarchy. To do this, you’d need to
explicitly set all child nodes to the Blocking state.


For example, to set all child transforms to Blocking, you could use the
following script.



import maya.cmds as cmds
def blockTree(root):
nodesToBlock = []
for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys():
nodesToBlock += cmds.listConnections(node, source=True, destination=True )
for node in {source:1 for source in nodesToBlock}.keys():
cmds.setAttr( '%s.nodeState' % node, 2 )



Applying this script would continue to draw objects but things would not be animated.




Default: kdnNormal

---
outSubdCVId(os): [int, int]
    properties: create, query, edit, multiuse
    Output CV Id

---
outSubdCVIdLeft(osl): int
    properties: create, query, edit
    Higher 32 bit integer of the output CV Id

---
outSubdCVIdRight(osr): int
    properties: create, query, edit
    Lower 32 bit integer of the output CV Id

---
outv(ov): int
    properties: create, query, edit, multiuse
    Out Vertices corresponding to the inSubDCVs.

---
preserveVertexOrdering(pvo): boolean
    properties: create, query, edit
    Preserve vertex ordering in conversion
Default: true

---
sampleCount(sc): int
    properties: create, query, edit
    The number of samples per face
Default: 1

---
shareUVs(suv): boolean
    properties: create, query, edit
    Force sharing of uvs on all common vertices - the value of this
attribute gets overridden by the value of the copyUVTopology attribute.
Default: false

---
subdNormals(un): boolean
    properties: create, query, edit
    Keep subdiv surface normals
Default: false

---
addUnderTransform(aut): boolean
    properties: create, query
    If true then add the result underneath a transform node

---
connectShaders(cs): boolean
    properties: create
    If true, all shader assignment will be copied from the
original subdiv surface to the converted polygonal surface.
Default: true

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdToPoly.html 
    """


def subdTransferUVsToCache() -> boolean:
    """Synopsis:
---
---
 subdTransferUVsToCache()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdTransferUVsToCache is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.subdTransferUVsToCache( 'subdShape1', 'polyShape4' )

---
Return:
---


    boolean: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdTransferUVsToCache.html 
    """


def subdiv(flagcurrentLevel: boolean, flagcurrentSubdLevel: boolean, flagdeepestLevel: int, flagdisplayLoad: boolean, flagedgeStats: boolean, flagfaceStats: boolean, flagmaxPossibleLevel: int, flagproxyMode: int, flagsmallOffsets: boolean) -> None:
    """Synopsis:
---
---
 subdiv([currentLevel=boolean], [currentSubdLevel=boolean], [deepestLevel=int], [displayLoad=boolean], [edgeStats=boolean], [faceStats=boolean], [maxPossibleLevel=int], [proxyMode=int], [smallOffsets=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdiv is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

To find the deepest subdivided level of polyToSubdShape1
---

cmds.subdiv( 'polyToSubdShape1', query=True, deepestLevel=True )

To find the level of the  selected subdiv CV
---

cmds.select( 'polyToSubdShape1.smp[2][67108865]', r=True)
cmds.subdiv( currentLevel=True )
Result: 1 ---


---


Flags:
---


---
currentLevel(cl): boolean
    properties: create, query
    When queried, this flag returns an integer representing
the level of the currently selected subdiv surface component(s).
Returns -1, if there are more than one level of CVs are selected,
(even if they are from different objects)
Returns -2, if there are no input subdiv CVs to process.

---
currentSubdLevel(csl): boolean
    properties: create, query
    When queried, this flag returns an integer representing
the level of the currently selected subdiv surface, regardless
of whether components are selected or not.
Returns -2, if there are no input subdiv CVs to process.

---
deepestLevel(dl): int
    properties: create, query
    When queried, this flag returns an integer representing the
deepest level to which the queried subdiv surface has
been subdivided.

---
displayLoad(dsl): boolean
    properties: create, query
    When queried, this flag prints the display load of selected subdiv

---
edgeStats(est): boolean
    properties: create, query
    When queried, this flag prints stats on the current subd.

---
faceStats(fst): boolean
    properties: create, query
    When queried, this flag prints stats on the current subd.

---
maxPossibleLevel(mpl): int
    properties: create, query
    When queried, this flag returns an integer representing
the maximum possible level to which the queried subdiv surface can
been subdivided.

---
proxyMode(pm): int
    properties: create, query
    When queried, this flag returns an integer representing
whether or not the subdivision surface is in "polygon proxy" mode.
"Proxy" mode allows the base mesh of a subdivision surface
without construction history to be edited using the polygonal
editing tools.
Returns 1, if the subdivision surface is in "polygon proxy" mode.
Returns 0, if the surface is not currently in "proxy" mode, but could
be put into "proxy" mode since it has no construction history.  (This state
is also known as "standard" mode.)
Returns 2, if the surface is not in "proxy" mode and cannot be put
into proxy mode, as it has construction history.

---
smallOffsets(so): boolean
    properties: create, query
    When queried, this flag prints the number of subdiv vertices in the
hierarchy that have a small enough offset so that the vertex is not required

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdiv.html 
    """


def subdivCrease(flagsharpness: boolean) -> boolean:
    """Synopsis:
---
---
 subdivCrease([sharpness=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdivCrease is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

after selecting components of a subdivision surface
cmds.subdivCrease()

---
Return:
---


    boolean: Command result

Flags:
---


---
sharpness(sh): boolean
    properties: create
    Specifies the sharpness value to set the crease to

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdivCrease.html 
    """


def subdivDisplaySmoothness(flagall: boolean, flagsmoothness: int) -> boolean:
    """Synopsis:
---
---
 subdivDisplaySmoothness([all=boolean], [smoothness=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

subdivDisplaySmoothness is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.subdivDisplaySmoothness( s=0 )Set smoothness to hull for selected subdivs
cmds.subdivDisplaySmoothness( s=1 )Set smoothness to rough for selected subdivs
cmds.subdivDisplaySmoothness( s=2 )Set smoothness to medium for selected subdivs
cmds.subdivDisplaySmoothness( s=3 )Set smoothness to fine for selected subdivs
cmds.subdivDisplaySmoothness( s=1, all=True )Set smoothness to rough for all subdivs
cmds.subdivDisplaySmoothness( query=True )Query display smoothness for selected subdivs

---
Return:
---


    boolean: Command result

Flags:
---


---
all(): boolean
    properties: create, query
    If set, change smoothness for all subdivision surfaces

---
smoothness(s): int
    properties: create, query
    Smoothness - 1 rough, 2 medium, 3 fine

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/subdivDisplaySmoothness.html 
    """


def substituteGeometry(flagdisableNonSkinDeformers: boolean, flagnewGeometryToLayer: boolean, flagoldGeometryToLayer: boolean, flagreWeightDistTolerance: float, flagretainOldGeometry: boolean) -> string:
    """Synopsis:
---
---
 substituteGeometry([disableNonSkinDeformers=boolean], [newGeometryToLayer=boolean], [oldGeometryToLayer=boolean], [reWeightDistTolerance=float], [retainOldGeometry=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

substituteGeometry is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


substitute the smooth skinned outPutGeom with newInputShape.
---

cmds.substituteGeometry( 'outPutGeom', 'newInputShape' )

---
Return:
---


    string: Name of shapes that were replaced

Flags:
---


---
disableNonSkinDeformers(dnd): boolean
    properties: create
    This flag controls the state of deformers other than skin deformers after
the substitution has taken place. If the flag is true then non-skin deformer
nodes are left in a disabled state at the completion of the command.
Default value is false.

---
newGeometryToLayer(ngl): boolean
    properties: create
    Create a new layer for the new geometry.

---
oldGeometryToLayer(ogl): boolean
    properties: create
    Create a new layer and move the old geometry to this layer

---
reWeightDistTolerance(wdt): float
    properties: create
    Specify the distance tolerance value to be used for retargeting weights.
While transferring weights the command tries to find the corresponding
vertices by overlapping the geometries with all deformers disabled. Sometimes
this results in selection of unrelated vertices. (Example when a hole in
the old geometry has been filled with new vertices in the new geometry.)
This distance tolerance value is used to detect this kind of faults and
either ignore these cases or to vary algorithm to find more corresponding
vertices.

---
retainOldGeometry(rog): boolean
    properties: create
    A copy of the old geometry should be retained

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/substituteGeometry.html 
    """


def suitePrefs(flagapplyToSuite: string, flaginstalledAsSuite: boolean, flagisCompleteSuite: boolean) -> None:
    """Synopsis:
---
---
 suitePrefs([applyToSuite=string], [installedAsSuite=boolean], [isCompleteSuite=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

suitePrefs is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Check if Maya is part of a Suites install
isSuiteInstall = cmds.suitePrefs(q=True, installedAsSuite=True)
if isSuiteInstall:
  Check whether Maya mouse and keyboard interaction
  has been applied to the Suite.
    applyMayaToSuite = cmds.suitePrefs(q=True, applyToSuite=True)
    if applyMayaToSuite:
      Apply Maya mouse and keyboard interaction to
      the Suite.
        cmds.suitePrefs(applyToSuite=True)

---


Flags:
---


---
applyToSuite(ats): string
    properties: create
    Apply the mouse and keyboard interaction settings
for the given application to all applications in the
Suite (if Maya is part of a Suites install). Valid
values are "Maya", "3dsMax", or "undefined", which
signifies that each app is to use their own settings.

---
installedAsSuite(ias): boolean
    properties: create
    Returns true if Maya is part of a Suites install, false
otherwise.

---
isCompleteSuite(ics): boolean
    properties: create
    Returns true if the Suites install contains all Entertainment
Creation Suite products, false otherwise.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/suitePrefs.html 
    """


def surface(flagdegreeU: int, flagdegreeV: int, flagformU: string, flagformV: string, flagknotU: float, flagknotV: float, flagname: string, flagobjectSpace: boolean, flagpoint: tuple[linear, linear, linear], flagpointWeight: tuple[linear, linear, linear, linear], flagworldSpace: boolean) -> string:
    """Synopsis:
---
---
 surface([degreeU=int], [degreeV=int], [formU=string], [formV=string], [knotU=float], [knotV=float], [name=string], [objectSpace=boolean], [point=[linear, linear, linear]], [pointWeight=[linear, linear, linear, linear]], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

surface is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

This following command produces a flat, rectangular surface that is degree 3
in both directions.  This means that there must be at least 4 x 4
points to define the surface, since 4 is the (degree + 1).  There
must be 6 knots in each direction, because the knot vector must
be (number of points + degree - 1), ie. (4 points + degree 3 - 1).
The CVs are specified in rows of U and columns of V, as you
would read a book from left to right, up to down. ie. in this order:
surface.cv[0][0] surface.cv[0][1] surface.cv[0][2] surface.cv[0][3]
surface.cv[1][0] surface.cv[1][1] surface.cv[1][2] surface.cv[1][3]
surface.cv[2][0] surface.cv[2][1] surface.cv[2][2] surface.cv[2][3]
surface.cv[3][0] surface.cv[3][1] surface.cv[3][2] surface.cv[3][3]

cmds.surface( du=3, dv=3, ku=(0, 0, 0, 1, 1, 1), kv=(0, 0, 0, 1, 1, 1), p=((-0.5, 0, 0.5), (-0.5, 0, 0.16), (-0.5, 0, -0.16), (-0.5, 0, -0.5), (-0.16, 0, 0.5), (-0.16, 0, 0.16), (-0.16, 0, -0.16), (-0.16, 0, -0.5), (0.16, 0, 0.5), (0.16, 0, 0.16), (0.16, 0, -0.16), (0.16, 0, -0.5), (0.5, 0, 0.5), (0.5, 0, 0.16), (0.5, 0, -0.16), (0.1, 0, -0.1)) )

This following command produces a surface that is degree 3 and periodic in
the U direction, and degree 1 in the V direction.  Notice that
the first 3 pairs of points match the last 3 pairs of
points, which is required for a degree 3 periodic surface.

cmds.surface( du=3, dv=1, fu='periodic', fv='open', ku=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), kv=(0, 1), pw=((4, -4, 0, 1), (4, -4, -2.5, 1), (5.5, 0, 0, 1), (5.5, 0, -2.5, 1), (4, 4, 0, 1), (4, 4, -2.5, 1), (0, 5.5, 0, 1), (0, 5.5, -2.5, 1), (-4, 4, 0, 1), (-4, 4, -2.5, 1), (-5.5, 0, 0, 1), (-5.5, 0, -2.5, 1), (-4, -4, 0, 1), (-4, -4, -2.5, 1), (0, -5.5, 0, 1), (0, -5.5, -2.5, 1), (4, -4, 0, 1), (4, -4, -2.5, 1), (5.5, 0, 0, 1), (5.5, 0, -2.5, 1), (4, 4, 0, 1), (4, 4, -2.5, 1)) )

This following command produces a surface that is degree 5 in both directions.

cmds.surface( du=5, dv=5, fu='open', fv='open', p=((-7, 0, 1), (-6, 0, 4), (-3, 0, 6), (0, 0, 7), (4, 0, 5), (6, 0, 3), (-7, 2, 1), (-6, 2, 4), (-3, 2, 7), (0, 2, 8), (4, 2, 5), (6, 2, 3), (-7, 3, 1), (-6, 3, 4), (-3, 3, 8), (0, 3, 9), (4, 3, 5), (6, 3, 3), (-7, 4, 1), (-6, 4, 4), (-3, 4, 9), (0, 4, 8), (4, 4, 5), (6, 4, 3), (-7, 5, 1), (-6, 5, 4), (-3, 5, 8), (0, 5, 7.5), (4, 5, 5), (6, 5, 3), (-7, 6, 1), (-6, 6, 4), (-3, 6, 6), (0, 6, 7), (4, 6, 5), (6, 6, 3)), ku=(0, 0, 0, 0, 0, 1, 1, 1, 1, 1), kv=(0, 0, 0, 0, 0, 1, 1, 1, 1, 1) )


How to query surface properties:

cmds.getAttr( 'surface1.degreeU' )
Returns an integer that is the surface degree in U

cmds.getAttr( 'surface1.degreeV' )
Returns an integer that is the surface degree in V

cmds.getAttr( 'surface1.spansU' )
Returns an integer that is the spans in U

cmds.getAttr( 'surface1.spansV' )
Returns an integer that is the spans in V

cmds.getAttr( 'surface1.formU' )
Return 0 = open, 1 = closed, 2 = periodic

cmds.getAttr( 'surface1.formV' )
Returns 0 = open, 1 = closed, 2 = periodic

cmds.getAttr( 'surface1.minValueU' )
cmds.getAttr( 'surface1.maxValueU' )
cmds.getAttr( 'surface1.minValueV' )
cmds.getAttr( 'surface1.maxValueV' )
These return the minimum and maximum parameter ranges in each direction.

cmds.getAttr( 'surface1.cv[0][0]' )
Returns the position of a CV of surface1 in local space.  If the
surface is a result of construction history, use a surface info
node instead to get the CV position.

cmds.getAttr( 'surface1.cv[*][0]' )
Returns the positions of a row of CVs of surface1 in local space.
If the surface is a result of construction history, use a surface info
node instead to get the CV positions.

cmds.createNode( 'surfaceInfo' )
cmds.connectAttr( 'surfaceShape1.worldSpace', 'surfaceInfo1.inputSurface', f=True )
cmds.getAttr( 'surfaceInfo1.controlPoints[*]' )
Returns the surface CVs in world space.   A surface info node can
also be used to query the surface knot vectors.

---
Return:
---


    string: The path to the new surface

Flags:
---


---
degreeU(du): int
    properties: create
    Degree in surface U direction.  Default is degree 3.

---
degreeV(dv): int
    properties: create
    Degree in surface V direction.  Default is degree 3.

---
formU(fu): string
    properties: create
    The string for open is "open" , for closed is "closed"  or
for periodic is "periodic" in U.

---
formV(fv): string
    properties: create
    The string for open is "open" , for closed is "closed"  or
for periodic is "periodic" in V.

---
knotU(ku): float
    properties: create, multiuse
    Knot value(s) in U direction.  One flag per knot value. There must
be (numberOfPointsInU + degreeInU - 1) knots and the knot
vector must be non-decreasing.

---
knotV(kv): float
    properties: create, multiuse
    Knot value(s) in V direction.  One flag per knot value. There must
be (numberOfPointsInV + degreeInV - 1) knots and the knot
vector must be non-decreasing.

---
name(n): string
    properties: create
    Name to use for new transforms.

---
objectSpace(ob): boolean
    properties: create
    Should the operation happen in objectSpace?

---
point(p): [linear, linear, linear]
    properties: create, multiuse
    To specify non rational CV with (x, y, z) values.  "linear" means
that this flag can take values with units.  Note that you
must specify (degree+1) surface points in any direction to create
a visible surface span.  eg.  if the surface is degree 3 in the U
direction, you must specify 4 CVs in the U direction.
Points are specified in rows of U and columns of V.  If you
want to incorporate units, add the unit name to the value, eg.
"-p 3.3in 5.5ft 6.6yd"

---
pointWeight(pw): [linear, linear, linear, linear]
    properties: create, multiuse
    To specify rational CV with (x, y, z, w) values.  "linear" means
that this flag can take values with units.  Note that you
must specify (degree+1) surface points in any direction to create
a visible surface span.  eg.  if the surface is degree 3 in the U
direction, you must specify 4 CVs in the U direction.
Points are specified in rows of U and columns of V.

---
worldSpace(ws): boolean
    properties: create
    Should the operation happen in worldSpace?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/surface.html 
    """


def surfaceSampler(flagcamera: name, flagfileFormat: string, flagfilename: string, flagfilterSize: float, flagfilterType: uint, flagflipU: boolean, flagflipV: boolean, flagignoreMirroredFaces: boolean, flagignoreTransforms: boolean, flagmapHeight: uint, flagmapMaterials: boolean, flagmapOutput: string, flagmapSpace: string, flagmapWidth: uint, flagmaxSearchDistance: linear, flagmaximumValue: linear, flagoverscan: uint, flagsearchCage: string, flagsearchMethod: uint, flagsearchOffset: linear, flagshadows: boolean, flagsource: string, flagsourceUVSpace: string, flagsuperSampling: uint, flagtarget: string, flagtargetUVSpace: string, flaguseGeometryNormals: boolean, flaguvSet: string) -> None:
    """Synopsis:
---
---
 surfaceSampler([camera=name], [fileFormat=string], [filename=string], [filterSize=float], [filterType=uint], [flipU=boolean], [flipV=boolean], [ignoreMirroredFaces=boolean], [ignoreTransforms=boolean], [mapHeight=uint], [mapMaterials=boolean], [mapOutput=string], [mapSpace=string], [mapWidth=uint], [maxSearchDistance=linear], [maximumValue=linear], [overscan=uint], [searchCage=string], [searchMethod=uint], [searchOffset=linear], [shadows=boolean], [source=string], [sourceUVSpace=string], [superSampling=uint], [target=string], [targetUVSpace=string], [useGeometryNormals=boolean], [uvSet=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

surfaceSampler is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Generate an object space normal map of a cube onto a sphere called test.dds
cmds.surfaceSampler( mapOutput='normal', filename='C:/test', fileFormat='dds', source='pCube1', target='pSphere1', uv='map1' )

---


Flags:
---


---
camera(cam): name
    properties: create
    Specify the camera to use for camera specific lighting calculations such as
specular highlights or reflections.

---
fileFormat(ff): string
    properties: create, multiuse
    The image format as a file extension (e.g. "dds").
This must be included once for every output map specified.

---
filename(fn): string
    properties: create, multiuse
    The filename to use when creating the map.
This must be included once for every output map specified.

---
filterSize(fs): float
    properties: create
    The filter size to use in pixels. Larger values (e.g. over 2.0) will produce smoother/softer
results, while values closer to 1.0 will produce sharper results.

---
filterType(ft): uint
    properties: create
    The filter type to use. 0 is a Guassian filter, 1 is a triangular filter, 2 is a box filter.

---
flipU(fu): boolean
    properties: create
    Flip the U coordinate of the generated image.

---
flipV(fv): boolean
    properties: create
    Flip the V coordinate of the generated image.

---
ignoreMirroredFaces(imf): boolean
    properties: create
    Stops reverse wound (i.e. mirrored) faces from contributing to the map
generation.

---
ignoreTransforms(it): boolean
    properties: create
    Controls whether transforms are used (meaning the search is performed in worldspace),
or not (meaning the search is performed in object space).

---
mapHeight(mh): uint
    properties: create, multiuse
    Pixel width of the generated map.
This must be included once for every output map specified.

---
mapMaterials(mm): boolean
    properties: create, multiuse
    Where appropriate (e.g. normal maps), this controls whether the material
should be included when sampling the map attribute.
This must be included once for every output map specified.

---
mapOutput(mo): string
    properties: create, multiuse
    Specifies a new output map to create. One of "normal", "displacement"
"diffuseRGB", "litAndShadedRGB", or "alpha"

---
mapSpace(sp): string
    properties: create, multiuse
    The space to generate the map in. Valid keyword is "object". Default
is tangent space.
This must be included once for every output map specified.

---
mapWidth(mw): uint
    properties: create, multiuse
    Pixel width of the generated map. Some output image formats require even or power of 2.
This must be included once for every output map specified.

---
maxSearchDistance(msd): linear
    properties: create, multiuse
    Controls the maximum distance away from a target surface that will
be searched for source surfaces. A value of 0 indicates no limit.
When generated maps include artifacts from the "other side" of an
object, try setting this value to a distance approximately equal to
the radius of the object.
If this flag is included, it must be included once for every target.

---
maximumValue(max): linear
    properties: create, multiuse
    The maximum value to include in the map. This allows control of how floating
point values (like displacement) are quantised into integer image formats.

---
overscan(os): uint
    properties: create
    The number of additional pixels to render around UV borders.
This will help to minimise texel filtering artifacts on
UV seams. When mipmaps are going to be generated for the texture
a higher value may be necessary (in addition to a filterSize
greater than 1).

---
searchCage(sc): string
    properties: create, multiuse
    Specifies a search envelope surface to use as a search guide
when looking for source surfaces.
If this flag is included, it must be included once for every target.

---
searchMethod(sm): uint
    properties: create
    Controls the search method used to match sample points on a target surface
to points on the sources. 0 is closest to envelope, 1 is prefer any intersection
inside envelope to intersections outside it, and 2 is only use intersections
inside envelope.

---
searchOffset(so): linear
    properties: create, multiuse
    Specifies a fixed offset from a target surface to use as the
starting point when looking for source surfaces. This value is
only used when no search cage is specified for a given target.
If this flag is included, it must be included once for every target.

---
shadows(sh): boolean
    properties: create, multiuse
    Where appropriate (e.g. lit and shaded), this controls whether
shadows are included in the calculation. Currently only depth
map shadows are supported.

---
source(s): string
    properties: create, multiuse
    Specifies a surface to use as a sampling source

---
sourceUVSpace(sus): string
    properties: create, multiuse
    Specifies that the transfer of data between the surfaces should be
done in UV space and specifies the name of the UV set on the source
surface(s) that should be used as the transfer space.

---
superSampling(ss): uint
    properties: create
    Controls the number of sampling points calculated for each output value. The algorithm will
use 2 ^ n squared samples for each point (so a value of 0 will use a single sample, while a value
of 3 will calculate 64 samples for each point).

---
target(t): string
    properties: create, multiuse
    Specified a surface to sample output information for.

---
targetUVSpace(tus): string
    properties: create, multiuse
    Specifies that the transfer of data between the surfaces should be
done in UV space and specifies the name of the UV set on the target
surface(s) that should be used as the transfer space.

---
useGeometryNormals(ugn): boolean
    properties: create
    Controls whether geometry or surface normals are used for surface searching.
Using geometry normals will ensure a smooth mapping but can introduce distorted
mappings where there are large distances between the source and target surfaces.
Surface normals can introduce overlapping or discontinuous mappings, but does
allow map distortion to be influenced by surface normal direction.

---
uvSet(uv): string
    properties: create, multiuse
    The name of the UV set to use when creating output maps.
If this flag is included, it must be included once for every target.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/surfaceSampler.html 
    """


def surfaceShaderList(flagadd: name, flagremove: name) -> None:
    """Synopsis:
---
---
 surfaceShaderList([add=name], [remove=name])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

surfaceShaderList is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a NURBS plane.
cmds.nurbsPlane( d=3, p=(0, 0, 0), lr=1, axis=(0, 0, 0), n='plane1' )

Make it red.
cmds.sets( name='redMaterialGroup', renderable=True, empty=True )
cmds.shadingNode( 'phong', name='redShader', asShader=True )
cmds.setAttr( 'redShader.color', 1, 0, 0, type='double3' )
cmds.surfaceShaderList( 'redShader', add='redMaterialGroup' )
cmds.sets( 'plane1', e=True, forceElement='redMaterialGroup' )

---


Flags:
---


---
add(add): name
    properties: create
    add object(s) to shader group list.

---
remove(rm): name
    properties: create
    remove object(s) to shader group list.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/surfaceShaderList.html 
    """


def swatchDisplayPort(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagborderColor: tuple[float, float, float], flagborderWidth: int, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpressCommand: script, flagpreventOverride: boolean, flagrenderPriority: int, flagrenderSize: int, flagshadingNode: name, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int, flagwidthHeight: tuple[int, int]) -> string:
    """Synopsis:
---
---
 swatchDisplayPort(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [borderColor=[float, float, float]], [borderWidth=int], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [pressCommand=script], [preventOverride=boolean], [renderPriority=int], [renderSize=int], [shadingNode=name], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int], [widthHeight=[int, int]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

swatchDisplayPort is undoable, queryable, and editable.
The optional argument is the name of the 3dPort.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout('r')
myShader = cmds.shadingNode('anisotropic', asShader=True)
cmds.swatchDisplayPort('slPP', wh=(256, 256), sn=myShader)
cmds.showWindow()

---
Return:
---


    string: - the name of the port created or modified

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
borderColor(bc): [float, float, float]
    properties: create, query, edit
    The border color of the swatch.

---
borderWidth(bw): int
    properties: create, query, edit
    The border width of the swatch.  The value will be clamped
between 0 and 4.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
pressCommand(pc): script
    properties: create, edit
    Specifies the command to be run when the swatch is clicked on.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
renderPriority(rp): int
    properties: create, edit
    Specifies the priority to render the swatch.
This flag can only be used in parallel swatch rendering.
When more than one swatch are waiting in the render queue,
this flag can be used to specify which one has the higher priority to be rendered.
By default, the flag is set to 0 - low priority.
The larger the number, the higher priority is used to render the swatch.

Maya pre-defined the render priority for the swatch in Node Editor, Attribute Editor and Hypershade as below:

0: The lowest render priority.
1: The render priority for the swatch in Node Editor.
2: The render priority for the swatch in the working area of HyperShade
3: The render priority for the swatch in Attribute Editor.

For example, when creating a display port in AE using the swatchDisplayPort command, option "-rp 3" is used.

---
renderSize(rs): int
    properties: create, query, edit
    The render size of the swatch.  The value will be clamped
between 32 and 512.

---
shadingNode(sn): name
    properties: create, query, edit
    Name of the shadingNode.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
widthHeight(wh): [int, int]
    properties: create, edit
    The width and height of the port.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/swatchDisplayPort.html 
    """


def swatchRefresh() -> boolean:
    """Synopsis:
---
---
 swatchRefresh()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

swatchRefresh is NOT undoable, NOT queryable, and NOT editable.swatchRefresh


Example:
---
import maya.cmds as cmds


Refresh the swatch for the layer1 node
cmds.swatchRefresh('layer1')

---
Return:
---


    boolean: true if all arguments are valid image source nodes and the operation succeded.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/swatchRefresh.html 
    """


def switchTable(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel1: string, flaglabel2: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagselectedRow: boolean, flagstatusBarMessage: string, flagswitchNode: name, flagunderPointerRow: boolean, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 switchTable(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label1=string], [label2=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [selectedRow=boolean], [statusBarMessage=string], [switchNode=name], [underPointerRow=boolean], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

switchTable is undoable, queryable, and editable.
The optional argument is the name of the control.




Example:
---
import maya.cmds as cmds

cmds.window(width=200)
cmds.formLayout('theForm')
cmds.switchTable('theSwitch')
cmds.formLayout('theForm', e=True,
                af=(('theSwitch', 'top', 0),
                    ('theSwitch', 'left', 0),
                    ('theSwitch', 'bottom', 0),
                    ('theSwitch', 'right', 0)))
cmds.showWindow()

---
Return:
---


    string: The name of the switch table control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
label1(l1): string
    properties: edit
    Set the label of the first column

---
label2(l2): string
    properties: edit
    Set the label of the second column

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
selectedRow(sr): boolean
    properties: query
    The current row selected.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
switchNode(sn): name
    properties: query, edit
    The switch node to be displayed in the control.

---
underPointerRow(upr): boolean
    properties: query
    The row under the pointer.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/switchTable.html 
    """


def symbolButton(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagimage: string, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 symbolButton(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [command=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

symbolButton is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.symbolButton( image='circle.png' )
cmds.symbolButton( image='sphere.png' )
cmds.symbolButton( image='cube.png' )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
command(c): script
    properties: create, query, edit
    Command executed when the symbol button is pressed.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
image(i): string
    properties: create, query, edit
    Image for the button.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/symbolButton.html 
    """


def symbolCheckBox(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdisableOffImage: string, flagdisableOnImage: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagimage: string, flaginnerMargin: boolean, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagoffCommand: script, flagoffImage: string, flagonCommand: script, flagonImage: string, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvalue: boolean, flagversion: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 symbolCheckBox(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [disableOffImage=string], [disableOnImage=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image=string], [innerMargin=boolean], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script], [offImage=string], [onCommand=script], [onImage=string], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [value=boolean], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

symbolCheckBox is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.symbolCheckBox( image='circle.png' )
cmds.symbolCheckBox( image='sphere.png' )
cmds.symbolCheckBox( image='cube.png' )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
backgroundColor(bgc): [float, float, float]
    properties: create, query, edit
    The background color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.
When setting backgroundColor, the background is automatically
enabled, unless enableBackground is also specified with a false
value.

---
changeCommand(cc): script
    properties: create, edit
    Command executed when the check box's state is changed.
Note that this flag should not be used in conjunction with
onCommand and offCommand. That is, one should either use
changeCommand and test the state of the check box from inside
the callback, or use onCommand and offCommand as separate
callbacks.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
disableOffImage(dfi): string
    properties: create, query, edit
    Image displayed when the check box is off and disabled.

---
disableOnImage(dni): string
    properties: create, query, edit
    Image displayed when the check box is on and disabled.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragCallback(dgc): script
    properties: create, edit
    Adds a callback that is called when the middle mouse button
is pressed.  The MEL version of the callback is of the form:

global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)

The proc returns a string array that is transferred to the drop site.
By convention the first string in the array describes the user settable
message type.  Controls that are application defined drag sources may
ignore the callback. $mods allows testing for the key modifiers CTRL and
SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,
3 == CTRL + SHIFT.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def callbackName( dragControl, x, y, modifiers ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "x", "y", "modifiers".  The
"dragControl" value is a string and the other values are integers (eg the
callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")

---
dropCallback(dpc): script
    properties: create, edit
    Adds a callback that is called when a drag and drop
operation is released above the drop site.  The MEL version of the callback is
of the form:

global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)

The proc receives a string array that is transferred from the drag source.
The first string in the msgs array describes the user defined message type.
Controls that are application defined drop sites may ignore the
callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.

In Python, it is similar, but there are two ways to specify the callback.  The
recommended way is to pass a Python function object as the argument.  In that
case, the Python callback should have the form:

def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):

The values of these arguments are the same as those for the MEL version above.

The other way to specify the callback in Python is to specify a string to be
executed.  In that case, the string will have the values substituted into it
via the standard Python format operator.  The format values are passed in a
dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",
"type".  The "dragControl" value is a string and the other values are integers
(eg the callback string could be
"print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
height(h): int
    properties: create, query, edit
    The height of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
image(i): string
    properties: create, query, edit
    Image of the check box.

---
innerMargin(im): boolean
    properties: create, query, edit
    This flag will revert the symbolCheckBox to its pre Maya 2.5
behaviour of having a 2 pixel inner margin.
This flag is for backward compatibility on Linux only, and will
be removed in future releases.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
offCommand(ofc): script
    properties: create, edit
    Command executed when the symbol check box is turned off.

---
offImage(ofi): string
    properties: create, query, edit
    Image displayed when the check box is off.

---
onCommand(onc): script
    properties: create, edit
    Command executed when the symbol check box is turned on.

---
onImage(oni): string
    properties: create, query, edit
    Image displayed when the check box is on.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): boolean
    properties: create, query, edit
    Value of the check box.

---
version(ver): string
    properties: create, query, edit
    Specify the version that this control feature was introduced.
The argument should be given as a string of the version number
(e.g. "2017", "2018"). Currently only accepts major version
numbers (e.g. 2017 Ext 1, or 2017.5 should be given as "2018").

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the control.  A control is created
visible by default.  Note that a control's actual appearance is
also dependent on the visible state of its parent layout(s).

---
visibleChangeCommand(vcc): script
    properties: create, query, edit
    Command that gets executed when visible state of the control changes.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/symbolCheckBox.html 
    """


def symmetricModelling(flagabout: string, flagallowPartial: boolean, flagaxis: string, flagpreserveSeam: int, flagreset: boolean, flagseamFalloffCurve: string, flagseamTolerance: float, flagsymmetry: int, flagtolerance: float, flagtopoSymmetry: boolean) -> None:
    """Synopsis:
---
---
 symmetricModelling([about=string], [allowPartial=boolean], [axis=string], [preserveSeam=int], [reset=boolean], [seamFalloffCurve=string], [seamTolerance=float], [symmetry=int], [tolerance=float], [topoSymmetry=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

symmetricModelling is undoable, queryable, and editable.
Symmetric modelling is an option that allows for reflection of basic
manipulator actions such as move, rotate, and scale.




Example:
---
import maya.cmds as cmds

What is the current reflection setting
cmds.symmetricModelling(query=True, symmetry=True)

What is the current reflection axis
cmds.symmetricModelling(query=True, axis=True)

Change the space to apply reflection to (object or world)
cmds.symmetricModelling(about='world')

Change the current tolerance to 0.34
cmds.symmetricModelling(tolerance=0.34)

---


Flags:
---


---
about(a): string
    properties: create, query, edit
    Set the space in which symmetry should be calculated (object or world or topo).
When queried, returns a string which is the current space being used.

---
allowPartial(ap): boolean
    properties: create, query, edit
    Specifies whether partial symmetry should be allowed when enabling topological symmetry.

---
axis(ax): string
    properties: create, query, edit
    Set the current axis to be reflected over.
When queried, returns a string which is the current axis.

---
preserveSeam(ps): int
    properties: create, query, edit
    Controls whether selection or symmetry should take priority on the plane
of symmetry.
When queried, returns an int for the option.

---
reset(r): boolean
    properties: create, edit
    Reset the redo information before starting.

---
seamFalloffCurve(sf): string
    properties: create, query, edit
    Set the seam's falloff curve, used to control the seam strength within the
seam tolerance. The string is a comma separated list of sets of 3 values
for each curve point.
When queried, returns a string which is the current space being used.

---
seamTolerance(st): float
    properties: create, query, edit
    Set the seam tolerance used for reflection. When preserveSeam is enabled, this
tolerance controls the width of the enforced seam.
When queried, returns a float of the seamTolerance.

---
symmetry(s): int
    properties: create, query, edit
    Set the symmetry option on or off.
When queried, returns an int for the option.

---
tolerance(t): float
    properties: create, query, edit
    Set the tolerance of reflection.
When queried, returns a float of the tolerance.

---
topoSymmetry(ts): boolean
    properties: create, query, edit
    Enable/disable topological symmetry.
When enabled, the supplied component/active list will be used to define the topological symmetry seam.
When queried, returns the name of the active topological symmetry object.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/symmetricModelling.html 
    """


def sysFile(flagcopy: string, flagdelete: boolean, flagmakeDir: boolean, flagmove: string, flagremoveEmptyDir: boolean, flagrename: string) -> boolean:
    """Synopsis:
---
---
 sysFile(
string
    , [copy=string], [delete=boolean], [makeDir=boolean], [move=string], [removeEmptyDir=boolean], [rename=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

sysFile is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a new directory path
cmds.sysFile( 'C:/temp/mayaStuff', makeDir=True )Windows
cmds.sysFile( '/tmp/mayaStuff', makeDir=True )Unix

Move a scene to the new directory (we can rename it at the same time).
cmds.sysFile( 'C:/maya/projects/default/scenes/myScene.mb', rename='C:/temp/mayaStuff/myScene.mb.trash' )Windows
cmds.sysFile( '/maya/projects/default/scenes/myScene.mb', rename='/tmp/mayaStuff/myScene.mb.trash' )Unix


Rename the scene to "myScene.will.be.deleted"
cmds.sysFile( 'C:/temp/mayaStuff/myScene.mb.trash', rename='C:/temp/mayaStuff/myScene.will.be.deleted' )Windows
cmds.sysFile( '/tmp/mayaStuff/myScene.mb.trash', rename='/tmp/mayaStuff/myScene.will.be.deleted' )Unix

Copy a scene to the new directory
destWindows = "C:/temp/mayaStuff/myScene.mb.trash"
srcWindows = "C:/maya/projects/default/scenes/myScene.mb"
cmds.sysFile( srcWindows, copy=destWindows )Windows

destUnix = "/tmp/mayaStuff/myScene.mb.trash"
srcUnix = "maya/projects/default/scenes/myScene.mb"
cmds.sysFile( srcUnix, copy=destUnix )Unix

Delete the scene
cmds.sysFile( 'C:/temp/mayaStuff/myScene.will.be.deleted', delete=True )Windows
cmds.sysFile( '/tmp/mayaStuff/myScene.will.be.deleted', delete=True )Unix

---
Return:
---


    boolean: True if successful, false otherwise.

Flags:
---


---
copy(cp): string
    properties: create
    Copy the file to the name given by the newFileName paramter.

---
delete(delete): boolean
    properties: create
    Deletes the file.

---
makeDir(md): boolean
    properties: create
    Create the directory path given in the parameter.
This will create the entire path if more than one
directory needs to be created.

---
move(mov): string
    properties: create
    Behaves identically to the -rename flag and remains for
compatibility with old scripts

---
removeEmptyDir(red): boolean
    properties: create
    Delete the directory path given in the parameter if
the directory is empty. The command will not delete a directory
which is not empty.

---
rename(ren): string
    properties: create
    Rename the file to the name given by the newFileName parameter.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/sysFile.html 
    """
