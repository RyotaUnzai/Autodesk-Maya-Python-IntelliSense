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


def tabLayout(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagborderStyle: string, flagchangeCommand: script, flagchildArray: boolean, flagchildResizable: boolean, flagcloseTab: int, flagcloseTabCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdoubleClickCommand: script, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontalScrollBarThickness: int, flagimage: string, flagimageVisible: boolean, flaginnerMarginHeight: int, flaginnerMarginWidth: int, flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagminChildWidth: int, flagmoveTab: tuple[int, int], flagnewTabCommand: script, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpostMenuCommand: script, flagpreSelectCommand: script, flagpreventOverride: boolean, flagscrollable: boolean, flagscrollableTabs: boolean, flagselectCommand: script, flagselectTab: string, flagselectTabIndex: int, flagshowNewTab: boolean, flagstatusBarMessage: string, flagtabIcon: tuple[string, string], flagtabIconIndex: tuple[int, string], flagtabLabel: tuple[string, string], flagtabLabelIndex: tuple[int, string], flagtabPosition: string, flagtabTooltip: tuple[string, string], flagtabTooltipIndex: tuple[int, string], flagtabsClosable: boolean, flagtabsVisible: boolean, flaguseTemplate: string, flagverticalScrollBarThickness: int, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 tabLayout(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [borderStyle=string], [changeCommand=script], [childArray=boolean], [childResizable=boolean], [closeTab=int], [closeTabCommand=script], [defineTemplate=string], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [horizontalScrollBarThickness=int], [image=string], [imageVisible=boolean], [innerMarginHeight=int], [innerMarginWidth=int], [isObscured=boolean], [manage=boolean], [margins=int], [minChildWidth=int], [moveTab=[int, int]], [newTabCommand=script], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [postMenuCommand=script], [preSelectCommand=script], [preventOverride=boolean], [scrollable=boolean], [scrollableTabs=boolean], [selectCommand=script], [selectTab=string], [selectTabIndex=int], [showNewTab=boolean], [statusBarMessage=string], [tabIcon=[string, string]], [tabIconIndex=[int, string]], [tabLabel=[string, string]], [tabLabelIndex=[int, string]], [tabPosition=string], [tabTooltip=[string, string]], [tabTooltipIndex=[int, string]], [tabsClosable=boolean], [tabsVisible=boolean], [useTemplate=string], [verticalScrollBarThickness=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

tabLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window( widthHeight=(200, 150) )
form = cmds.formLayout()
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

child1 = cmds.rowColumnLayout(numberOfColumns=2)
cmds.button()
cmds.button()
cmds.button()
cmds.setParent( '..' )

child2 = cmds.rowColumnLayout(numberOfColumns=2)
cmds.button()
cmds.button()
cmds.button()
cmds.setParent( '..' )

cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'One'), (child2, 'Two')) )

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/tabLayout.html 
    """


def tangentConstraint(flagaimVector: tuple[float, float, float], flaglayer: string, flagname: string, flagremove: boolean, flagtargetList: boolean, flagupVector: tuple[float, float, float], flagweight: float, flagweightAliasList: boolean, flagworldUpObject: name, flagworldUpType: string, flagworldUpVector: tuple[float, float, float]) -> list[string]:
    """Synopsis:
---
---
 tangentConstraint(
[target...] object
    , [aimVector=[float, float, float]], [layer=string], [name=string], [remove=boolean], [targetList=boolean], [upVector=[float, float, float]], [weight=float], [weightAliasList=boolean], [worldUpObject=name], [worldUpType=string], [worldUpVector=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

tangentConstraint is undoable, queryable, and editable.
A tangentConstraint takes as input one or more NURBS curves (the
targets) and a DAG transform node (the object).  The tangentConstraint
orients the constrained object such that the aimVector (in the
object's local coordinate system) aligns in world space to combined
tangent vector.  The upVector (again the the object's local coordinate
system) is aligned in world space with the worldUpVector.  The
combined tangent vector is a weighted average of the tangent vector
for each target curve at the point closest to the constrained object.




Example:
---
import maya.cmds as cmds

orients the aim vector of cube1 in it's local coordinate space,
to the tangent vector of curve1 at the closest point to  cube1.
cmds.tangentConstraint( 'curve1', 'cube1' )

uses the average of the tangents from curve1 and curve2.
cmds.tangentConstraint( 'curve1', 'curve2', 'cube2', w=.1 )

sets the weight for curve1's effect on cube2 to 10.
cmds.tangentConstraint( 'curve1', 'cube2', e=True, w=10. )

removes curve2 from cube2's tangentConstraint
cmds.tangentConstraint( 'curve2', 'cube2', e=True, rm=True )

adds curve3 to cube2's tangent constraint with the default weight
cmds.tangentConstraint( 'curve3', 'cube2' )

---
Return:
---


    list[string]: Name of the created constraint node

Flags:
---


---
aimVector(aim): [float, float, float]
    properties: create, query, edit
    Set the aim vector.  This is the vector in local
coordinates that points at the target.  If not given at creation
time, the default value of (1.0, 0.0, 0.0) is used.

---
layer(l): string
    properties: create, edit
    Specify the name of the animation layer where the constraint should be added.

---
name(n): string
    properties: create, query, edit
    Sets the name of the constraint node to the specified
name.  Default name is constrainedObjectName_constraintType

---
remove(rm): boolean
    properties: edit
    removes the listed target(s) from the constraint.

---
targetList(tl): boolean
    properties: query
    Return the list of target objects.

---
upVector(u): [float, float, float]
    properties: create, query, edit
    Set local up vector.  This is the vector in local
coordinates that aligns with the world up vector.  If not given
at creation time, the default value of (0.0, 1.0, 0.0) is used.

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

---
worldUpObject(wuo): name
    properties: create, query, edit
    Set the DAG object use for worldUpType "object" and
"objectrotation". See worldUpType for greater detail.
The default value is no up object, which is interpreted
as world space.

---
worldUpType(wut): string
    properties: create, query, edit
    Set the type of the world up vector computation.
The worldUpType can have one of 5 values: "scene",
"object", "objectrotation", "vector", or "none".
If the value is "scene", the upVector is
aligned with the up axis of the scene and
worldUpVector and worldUpObject are ignored.
If the value is "object", the upVector is
aimed as closely as possible to the
origin of the space of the worldUpObject and
the worldUpVector is ignored.
If the value is "objectrotation" then the
worldUpVector is interpreted as being in
the coordinate space of the worldUpObject, transformed into
world space and the upVector is aligned as
closely as possible to the result.
If the value is "vector", the upVector
is aligned with worldUpVector as closely as
possible and worldUpMatrix is ignored.
Finally, if the value is "none" no twist calculation
is performed by the constraint, with the resulting "upVector"
orientation based previous orientation of the
constrained object, and the "great circle" rotation needed
to align the aim vector with its constraint.
The default worldUpType is "vector".

---
worldUpVector(wu): [float, float, float]
    properties: create, query, edit
    Set world up vector.  This is the vector in world
coordinates that up vector should align with.
See -wut/worldUpType (below)for greater detail.
If not given at creation time, the default
value of (0.0, 1.0, 0.0) is used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/tangentConstraint.html 
    """


def targetWeldCtx(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagmergeToCenter: boolean, flagpreserveUV: boolean) -> None:
    """Synopsis:
---
---
 targetWeldCtx([exists=boolean], [image1=string], [image2=string], [image3=string], [mergeToCenter=boolean], [preserveUV=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

targetWeldCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To create a new target weld context:
cmds.targetWeldCtx()

To query if it is set to merge to the center:
cmds.targetWeldCtx('targetWeldCtx1', q=True, mergeToCenter=True )

To set it to merge at the target:
cmds.targetWeldCtx('targetWeldCtx1', e=True, mergeToCenter=False )

---


Flags:
---


---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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
mergeToCenter(mtc): boolean
    properties: create, query, edit
    If mergeToCenter is set to true then the source and target vertices's
will be moved to the center before doing the merge.  If set to false
the source vertex will be moved to the target vertex before doing the
merge.

---
preserveUV(puv): boolean
    properties: query, edit
    When false, UVs are not changed when welding components.
When true, the UVs are modified to stop texture swimming
when welding components. Default is true.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/targetWeldCtx.html 
    """


def tension(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagenvelope: float, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flaginwardConstraint: float, flagname: string, flagoutwardConstraint: float, flagparallel: boolean, flagpinBorderVertices: boolean, flagprune: boolean, flagremove: boolean, flagselectedComponents: boolean, flagsmoothingIterations: uint, flagsmoothingStep: float, flagsplit: boolean, flaguseComponentTags: boolean) -> string:
    """Synopsis:
---
---
 tension(
selectionList
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [deformerTools=boolean], [envelope=float], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [inwardConstraint=float], [name=string], [outwardConstraint=float], [parallel=boolean], [pinBorderVertices=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean], [smoothingIterations=uint], [smoothingStep=float], [split=boolean], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

tension is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Create a poly sphere
cmds.polySphere()

Attach a tension deformer to the sphere performing
20 smoothing iterations with a step of 0.8
cmds.tension( smoothingIterations=20, smoothingStep=0.8 )

---
Return:
---


    string: Tension deformer node name

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
envelope(en): float
    properties: create, query, edit
    Envelope of the tension node. The envelope determines the percent of
deformation. Value is clamped to [0, 1] range.
Default is 1.

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
inwardConstraint(iwc): float
    properties: create, query, edit
    Constrains the movement of the vertex to not move inward from the input
deforming shape to preserve the contour. Value is in the [0,1] range.
Default is 0.0.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
outwardConstraint(owc): float
    properties: create, query, edit
    Constrains the movement of the vertex to not move outward from the input
deforming shape to preserve the contour. Value is in the [0,1] range.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
pinBorderVertices(pbv): boolean
    properties: create, query, edit
    If enabled, vertices on mesh borders will be pinned to their current
position during smoothing. Default is true.

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
selectedComponents(cms): boolean
    properties: query
    Returns the components used by the deformer that are currently selected.
This intersects the current selection with the components affected by the deformer.

---
smoothingIterations(si): uint
    properties: create, query, edit
    Number of smoothing iterations performed by the tension node.
Default is 10.

---
smoothingStep(ss): float
    properties: create, query, edit
    Step amount used per smoothing iteration. Value is clamped to [0, 1] range.
A higher value may lead to instabilities but converges faster compared
to a lower value. Default is 0.5.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/tension.html 
    """


def texCutContext(flagadjustSize: boolean, flagdisplayShellBorders: boolean, flagedgeSelectSensitive: float, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagmode: string, flagmoveRatio: float, flagname: string, flagsize: float, flagsteadyStroke: boolean, flagsteadyStrokeDistance: float, flagtouchToSew: boolean) -> boolean | float | string:
    """Synopsis:
---
---
 texCutContext(
contextName
    , [adjustSize=boolean], [displayShellBorders=boolean], [edgeSelectSensitive=float], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [mode=string], [moveRatio=float], [name=string], [size=float], [steadyStroke=boolean], [steadyStrokeDistance=float], [touchToSew=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texCutContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

// Create a new cut UV tool context, then switch to it
// In order to use this tool, you must open the UV editor
cmds.texCutContext('texCutContext1')
cmds.setToolTo('texCutContext1')

---
Return:
---


    float: Size of the brush rung, when querying brushSize
    float: The value of the edge selection sensitivity, when querying the edgeSelectSensitive flag.
    boolean: Whether steady stroke is on or not, when querying the steadyStroke flag.
    float: The distance for a steady stroke, when querying the steadyStrokeDistance flag.
    float: The cut open ratio relative to edge length, when querying the moveRatio flag.
    string: The type of effect the brush will perform, when querying the mode flag.
    boolean: Whether shell borders are displayed, when querying the displayShellBorders flag.
    boolean: Current touch-to-sew mode, when querying the touchToSew flag.

Flags:
---


---
adjustSize(asz): boolean
    properties: edit
    If true, puts the tool into the mode where dragging the mouse will edit the brush size.
If false, puts the tool back into the previous mode.

---
displayShellBorders(dsb): boolean
    properties: query, edit
    Toggle the display of shell borders.

---
edgeSelectSensitive(ess): float
    properties: query, edit
    Set the value of the edge selection sensitivity.

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
mode(m): string
    properties: query, edit
    Specifies the type of effect the brush will perform, Cut or Sew.

---
moveRatio(mvr): float
    properties: query, edit
    The cut open ratio relative to edge length.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
size(sz): float
    properties: query, edit
    Brush size value of the brush ring.

---
steadyStroke(ss): boolean
    properties: query, edit
    Turn on steady stroke or not.

---
steadyStrokeDistance(ssd): float
    properties: query, edit
    The distance for steady stroke.

---
touchToSew(tts): boolean
    properties: query, edit
    Toggle the touch to sew mode.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texCutContext.html 
    """


def texLatticeDeformContext(flagenvelope: float, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglatticeColumns: uint, flaglatticeRows: uint, flagname: string, flagshowMoveManipulator: boolean, flagsnapPixelMode: boolean, flaguseBoundingRect: boolean) -> boolean | float | int:
    """Synopsis:
---
---
 texLatticeDeformContext(
contextName
    , [envelope=float], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [latticeColumns=uint], [latticeRows=uint], [name=string], [showMoveManipulator=boolean], [snapPixelMode=boolean], [useBoundingRect=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texLatticeDeformContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a lattice manipulator with 4 x 4 lattice.
---

cmds.texLatticeDeformContext( 'latticeContext', latticeColumns=4, latticeRows=4 )

---
Return:
---


    int: Number of column divisions, when querying the latticeColumns flag.
    int: Number of row divisions, when querying the latticeRows flag.
    float: Value of the deform envelope, when querying the envelope flag.
    boolean: Whether snapping to pixels is on, when querying the snapPixelMode flag.
    boolean: Whether the bounding rectangle is to be used for deforemation, when querying the useBoundingRect flag.

Flags:
---


---
envelope(ev): float
    properties: create, query, edit
    Specifies the influence of the lattice.

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
latticeColumns(lc): uint
    properties: create, query, edit
    Specifies the number column points the lattice contains.  The
maximum size lattice is restricted to 8 columns.

---
latticeRows(lr): uint
    properties: create, query, edit
    Specifies the number of rows the lattice contains. The
maximum size lattice is restricted to 8 rows.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
showMoveManipulator(smm): boolean
    properties: create, query, edit
    Specifies whether show move manipulator in UV Editor

---
snapPixelMode(spm): boolean
    properties: create, query, edit
    Specifies the influenced uv points should be snapped to a pixel
center or corner.

---
useBoundingRect(ubr): boolean
    properties: create, query, edit
    When constructing the lattice use the bounding box of the
selected UVs for the extents of the lattice.  When this is
disabled the extents of the marquee selections are used as the
extents for the lattice.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texLatticeDeformContext.html 
    """


def texManipContext(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string) -> string:
    """Synopsis:
---
---
 texManipContext([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texManipContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.texSelectContext()

cmds.texManipContext()

---
Return:
---


    string: : name of the context created
    string: : name of the context created

Flags:
---


---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texManipContext.html 
    """


def texMoveContext(flageditPivotMode: boolean, flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagposition: boolean, flagsnap: boolean, flagsnapComponentsRelative: boolean, flagsnapPixelMode: int, flagsnapValue: float, flagtweakMode: boolean) -> string:
    """Synopsis:
---
---
 texMoveContext(
[object]
    , [editPivotMode=boolean], [exists=boolean], [image1=string], [image2=string], [image3=string], [position=boolean], [snap=boolean], [snapComponentsRelative=boolean], [snapPixelMode=int], [snapValue=float], [tweakMode=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texMoveContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new move context:
cmds.texMoveContext()

To query the position of the manipulator
cmds.texMoveContext( 'texMoveContext', q=True, position=True )

---
Return:
---


    string: (the name of the new context)

Flags:
---


---
editPivotMode(epm): boolean
    properties: query
    Returns true when the manipulator is in edit pivot mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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
position(p): boolean
    properties: query
    Returns the current position of the manipulator

---
snap(s): boolean
    properties: query, edit
    Sets or queries whether snapping is to be used.

---
snapComponentsRelative(scr): boolean
    properties: query, edit
    Value can be : true or false.
If true, while snapping a group of UVs, the
relative spacing between them will be preserved.
If false, all the UVs will be snapped to the
target point

---
snapPixelMode(spm): int
    properties: query, edit
    Sets the snapping mode to be the pixel center or upper
left corner.

---
snapValue(sv): float
    properties: query, edit
    Sets or queries the size of the snapping increment.

---
tweakMode(twk): boolean
    properties: query, edit
    When true, the manipulator is hidden and highlighted components can be selected
and moved in one step using a click-drag interaction.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texMoveContext.html 
    """


def texMoveUVShellContext(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagiterations: int, flagmask: boolean, flagposition: boolean, flagshellBorder: float) -> string:
    """Synopsis:
---
---
 texMoveUVShellContext(
[object]
    , [exists=boolean], [image1=string], [image2=string], [image3=string], [iterations=int], [mask=boolean], [position=boolean], [shellBorder=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texMoveUVShellContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new move context:
cmds.texMoveUVShellContext()

To query the position of the manipulator
cmds.texMoveUVShellContext( 'texMoveUVShellContext', q=True, position=True )

---
Return:
---


    string: (the name of the new context)

Flags:
---


---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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
iterations(it): int
    properties: query, edit
    Sets or queries the number of iterations to perform.

---
mask(m): boolean
    properties: query, edit
    Sets or queries masking on the shell.

---
position(p): boolean
    properties: query
    Returns the current position of the manipulator

---
shellBorder(sb): float
    properties: query, edit
    Sets or queries the size of the shell border.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texMoveUVShellContext.html 
    """


def texRotateContext(flageditPivotMode: boolean, flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagposition: boolean, flagsnap: boolean, flagsnapRelative: boolean, flagsnapValue: float, flagtweakMode: boolean) -> string:
    """Synopsis:
---
---
 texRotateContext([editPivotMode=boolean], [exists=boolean], [image1=string], [image2=string], [image3=string], [position=boolean], [snap=boolean], [snapRelative=boolean], [snapValue=float], [tweakMode=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texRotateContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new rotate context:
cmds.texRotateContext()

To query the position of the manipulator
cmds.texRotateContext( 'texRotateContext', q=True, position=True )

---
Return:
---


    string: : name of the context created

Flags:
---


---
editPivotMode(epm): boolean
    properties: query
    Returns true when the manipulator is in edit pivot mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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
position(p): boolean
    properties: query
    Returns the current position of the manipulator.

---
snap(s): boolean
    properties: query, edit
    Sets or queries whether snapping is to be used.

---
snapRelative(sr): boolean
    properties: query, edit
    Sets or queries whether snapping is relative.

---
snapValue(sv): float
    properties: query, edit
    Sets or queries the size of the snapping increment.

---
tweakMode(twk): boolean
    properties: query, edit
    When true, the manipulator is hidden and highlighted components can be selected
and rotated in one step using a click-drag interaction.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texRotateContext.html 
    """


def texScaleContext(flageditPivotMode: boolean, flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagposition: boolean, flagpreventNegativeScale: boolean, flagsnap: boolean, flagsnapRelative: boolean, flagsnapValue: float, flagtweakMode: boolean) -> string:
    """Synopsis:
---
---
 texScaleContext([editPivotMode=boolean], [exists=boolean], [image1=string], [image2=string], [image3=string], [position=boolean], [preventNegativeScale=boolean], [snap=boolean], [snapRelative=boolean], [snapValue=float], [tweakMode=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texScaleContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new scale context:
cmds.texScaleContext()

To query the position of the manipulator
cmds.texScaleContext( 'texScaleContext', q=True, position=True )

---
Return:
---


    string: : name of the context created

Flags:
---


---
editPivotMode(epm): boolean
    properties: query
    Returns true when manipulator is in edit pivot mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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
position(p): boolean
    properties: query
    Returns the current position of the manipulator.

---
preventNegativeScale(pns): boolean
    properties: query, edit
    Prevent negative scale for components.

---
snap(s): boolean
    properties: query, edit
    Sets or queries whether snapping is to be used.

---
snapRelative(sr): boolean
    properties: query, edit
    Sets or queries whether snapping is relative.

---
snapValue(sv): float
    properties: query, edit
    Sets or queries the size of the snapping increment.

---
tweakMode(twk): boolean
    properties: query, edit
    When true, the manipulator is hidden and highlighted components can be selected
and scaled in one step using a click-drag interaction.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texScaleContext.html 
    """


def texSculptCacheContext(flagadjustSize: boolean, flagadjustStrength: boolean, flagdirection: int, flagfalloffType: int, flagfloodPin: float, flaggrabTwist: boolean, flaginverted: boolean, flagmode: string, flagsculptFalloffCurve: string, flagshowBrushRingDuringStroke: boolean, flagsize: float, flagstrength: float) -> None:
    """Synopsis:
---
---
 texSculptCacheContext([adjustSize=boolean], [adjustStrength=boolean], [direction=int], [falloffType=int], [floodPin=float], [grabTwist=boolean], [inverted=boolean], [mode=string], [sculptFalloffCurve=string], [showBrushRingDuringStroke=boolean], [size=float], [strength=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texSculptCacheContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a new sculpting context, then switch to it
cmds.texSculptCacheContext('uvSculptCtx')
cmds.setToolTo('uvSculptCtx')

Set uvSculptCtx's brush size to 10.0
cmds.texSculptCacheContext('uvSculptCtx', edit=True, bs=10.0)

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
direction(d): int
    properties: query, edit
    Specifies how the brush determines where the uvs go.

---
falloffType(ft): int
    properties: query, edit
    Specifies how the brush determines which uvs to affect.

---
floodPin(fp): float
    properties: create, edit
    Sets the pin value for each UV to the given value

---
grabTwist(gtw): boolean
    properties: create, query, edit
    If true, the grab brush twists the UVs

---
inverted(inv): boolean
    properties: create, query, edit
    If true, inverts the effect of the brush.

---
mode(m): string
    properties: query, edit
    Specifies the type of sculpting effect the brush will perform.

---
sculptFalloffCurve(sfc): string
    properties: query, edit
    Specifies the falloff curve that affects the brush.

---
showBrushRingDuringStroke(sbr): boolean
    properties: query, edit
    Specifies whether or not to show the brush ring during stroke.

---
size(sz): float
    properties: query, edit
    Specifies the world-space size of the current brush.

---
strength(st): float
    properties: query, edit
    Specifies the world-space strength of the current brush.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texSculptCacheContext.html 
    """


def texSelectContext(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string) -> string:
    """Synopsis:
---
---
 texSelectContext([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texSelectContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.texSelectContext()

---
Return:
---


    string: : name of the context created

Flags:
---


---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texSelectContext.html 
    """


def texSelectShortestPathCtx(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string) -> None:
    """Synopsis:
---
---
 texSelectShortestPathCtx([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texSelectShortestPathCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new poly shortest edge path context:
---

cmds.texSelectShortestPathCtx( 'PolyTexShortestPath' )

---


Flags:
---


---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texSelectShortestPathCtx.html 
    """


def texSmudgeUVContext(flagdragSlider: string, flageffectType: string, flagexists: boolean, flagfunctionType: string, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagpressure: float, flagradius: float, flagsmudgeIsMiddle: boolean) -> string:
    """Synopsis:
---
---
 texSmudgeUVContext(
contextName
    , [dragSlider=string], [effectType=string], [exists=boolean], [functionType=string], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [pressure=float], [radius=float], [smudgeIsMiddle=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texSmudgeUVContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a poly plane
cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')

Select all UVs
cmds.select('pPlane1.map[0:120]', r=True)

Create a new smudge UV tool context, set the effect type to smudge mode, set the radius to 0.1 and pressure to 0.2, then switch to it
In order to use this tool to smudge the UVs of pPlane1, you must open the texture UV editor
cmds.texSmudgeUVContext('texSmudgeUVContext1', effectType='smudge', r=0.1, prs=0.2)
cmds.setToolTo('texSmudgeUVContext1')

---
Return:
---


    string: Name of the effect type created.

Flags:
---


---
dragSlider(ds): string
    properties: query, edit
    radius | none
Enables the drag slider mode. This is to support brush
resizing while holding the 'b' or 'B' button.

---
effectType(et): string
    properties: query, edit
    fixed | smudge
Specifies the effect of the tool. In fixed mode, the UVs
move as if they are attached by a rubber band. In smudge mode the
UVs are moved as the cursor is dragged over the UVs.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
functionType(ft): string
    properties: query, edit
    exponential | linear | constant.
Specifies how UVs fall off from the center of influence.

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
pressure(prs): float
    properties: query, edit
    Pressure value when effect type is set to smudge.

---
radius(r): float
    properties: query, edit
    Radius of the smudge tool. All UVs within this radius are
affected by the tool

---
smudgeIsMiddle(sim): boolean
    properties: query, edit
    By default, the left mouse button initiates the smudge.
However, this conflicts with selection. When smudgeIsMiddle is
on, smudge mode is activated by the middle mouse button
instead of the left mouse button.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texSmudgeUVContext.html 
    """


def texTweakUVContext(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagposition: boolean, flagtolerance: float) -> string:
    """Synopsis:
---
---
 texTweakUVContext(
[object]
    , [exists=boolean], [image1=string], [image2=string], [image3=string], [position=boolean], [tolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texTweakUVContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new move context:
cmds.texTweakUVContext()

To query the position of the manipulator
cmds.texTweakUVContext( 'texMoveUVShellContext', q=True, position=True )

---
Return:
---


    string: (the name of the new context)

Flags:
---


---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

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
position(p): boolean
    properties: query
    Returns the current position of the manipulator

---
tolerance(t): float
    properties: create, query, edit
    Controls the initial selection snapping tolerance.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texTweakUVContext.html 
    """


def texWinToolCtx(flagalternateContext: boolean, flagboxzoom: boolean, flagdolly: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagtoolName: string, flagtrack: boolean) -> string:
    """Synopsis:
---
---
 texWinToolCtx([alternateContext=boolean], [boxzoom=boolean], [dolly=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [toolName=string], [track=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texWinToolCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a new texture window tool context, set this tool to dolly in the texture window, then switch to it
cmds.texWinToolCtx('texWinToolCtx1', do=True)
cmds.setToolTo('texWinToolCtx1')

---
Return:
---


    string: Context name

Flags:
---


---
alternateContext(ac): boolean
    properties: create, query
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

---
boxzoom(bz): boolean
    properties: create, query, edit
    Perform Box Zoom

---
dolly(do): boolean
    properties: create, query, edit
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
    properties: create, query, edit
    Tracks the view

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texWinToolCtx.html 
    """


def text(flagalign: string, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagdropRectCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfont: string, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghyperlink: boolean, flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrecomputeSize: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int, flagwordWrap: boolean) -> string:
    """Synopsis:
---
---
 text(
[string]
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [dropRectCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [hyperlink=boolean], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [recomputeSize=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int], [wordWrap=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

text is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.window( width=150 )
cmds.columnLayout( adjustableColumn=True )
cmds.text( label='Default' )
cmds.text( label='Left', align='left' )
cmds.text( label='Centre', align='center' )
cmds.text( label='Right', align='right' )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
align(al): string
    properties: create, query, edit
    The label alignment.  Alignment values are "left",
"right", and "center".  Note that the alignment will
only be noticable if the control is wider than the label length.
By default, the label is aligned "center".

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
dropRectCallback(drc): script
    properties: edit
    Adds a callback that is called when a drag and drop
operation is hovering above the drop site.  It returns the shape of the
rectangle to be drawn to highlight the entry, if the control can receive
the dropped data. The MEL version of the callback is of the form:

global proc int[] callbackName(string $dropControl, int $x, int $y)

The return value is an array of size 4, with the parameters, in order, being
the left and top coordinates of the rectangle to be drawn, followed by the
width and height.
This functionality is currently only implemented in MEL.

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
hyperlink(hl): boolean
    properties: create, query, edit
    Sets the label text to be a hyperlink if the argument is true.  The label text
must be a proper HTML link.
In MEL, double quotes in the link will most likely have to be protected from
the MEL interpreter by preceding them with a backslash.  Clicking on
the link will open it in an external Web browser.

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
    The label text.  The default label is the name of
the control.

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
recomputeSize(rs): boolean
    properties: create, query, edit
    If true then the control will recompute it's size to
just fit the size of the label.  If false then the control size
will remain fixed as you change the size of the label.  The
default value of this flag is true.

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
wordWrap(ww): boolean
    properties: create, query
    If true then label text is wrapped where necessary at
word-breaks. If false, it is not wrapped at all. The
default value of this flag is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/text.html 
    """


def textCurves(flagfont: string, flagname: string, flagobject: boolean, flagtext: string) -> list[string]:
    """Synopsis:
---
---
 textCurves(
[string]
    , [font=string], [name=string], [object=boolean], [text=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textCurves is undoable, queryable, and editable.
A single letter can be made up of more than one NURBS curve.
The number of curves per letter varies with the font.




Example:
---
import maya.cmds as cmds

Create curves for text string "Maya" in the "Times-Roman" font:
cmds.textCurves( f='Times-Roman', t='Maya' )

Create curves for text "hello world" in the "Courier" font.
The "-n" flag specifies the name of the resulting transform
and shape.
cmds.textCurves( n= 'first', f='Courier', t='hello world' )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
font(f): string
    properties: create
    The font to use.

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
text(t): string
    properties: create
    The string to create the curves for.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textCurves.html 
    """


def textField(flagalwaysInvokeEnterCommandOnReturn: boolean, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdisableButtons: boolean, flagdisableClearButton: boolean, flagdisableHistoryButton: boolean, flagdocTag: string, flagdragCallback: script, flagdrawInactiveFrame: boolean, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagenterCommand: script, flagexists: boolean, flagfileName: string, flagfont: string, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaginsertText: string, flaginsertionPosition: int, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagplaceholderText: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagreceiveFocusCommand: script, flagsearchField: boolean, flagstatusBarMessage: string, flagtext: string, flagtextChangedCommand: script, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 textField(
[string]
    , [alwaysInvokeEnterCommandOnReturn=boolean], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [disableButtons=boolean], [disableClearButton=boolean], [disableHistoryButton=boolean], [docTag=string], [dragCallback=script], [drawInactiveFrame=boolean], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean], [fileName=string], [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [insertText=string], [insertionPosition=int], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [placeholderText=string], [popupMenuArray=boolean], [preventOverride=boolean], [receiveFocusCommand=script], [searchField=boolean], [statusBarMessage=string], [text=string], [textChangedCommand=script], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textField is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

   Create a window with a some fields for entering text.
---

window = cmds.window()
cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
cmds.text( label='Name' )
name = cmds.textField()
cmds.text( label='Address' )
address = cmds.textField()
cmds.text( label='Phone Number' )
phoneNumber = cmds.textField()
cmds.text( label='Email' )
email = cmds.textField()

   Attach commands to pass focus to the next field if the Enter
   key is pressed. Hitting just the Return key will keep focus
   in the current field.
---

cmds.textField( name, edit=True, enterCommand=('cmds.setFocus(\"' + address + '\")') )
cmds.textField( address, edit=True, enterCommand=('cmds.setFocus(\"' + phoneNumber + '\")') )
cmds.textField( phoneNumber, edit=True, enterCommand=('cmds.setFocus(\"' + email + '\")') )
cmds.textField( email, edit=True, enterCommand=('cmds.setFocus(\"' + name + '\")') )

cmds.showWindow( window )

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
alwaysInvokeEnterCommandOnReturn(aie): boolean
    properties: create, query, edit
    Sets whether to always invoke the enter command when the return key is
pressed by the user.
By default, this option is false.

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
    Command executed when the text changes.  This command is
not invoked when the value changes via the -tx/text flag.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
disableButtons(db): boolean
    properties: create, query, edit
    Sets the visibility state of search field buttons to true/false depending on the passed value.
In Query mode returns whether both buttons are visible or not.

---
disableClearButton(dcb): boolean
    properties: create, query, edit
    Sets the visibility state of search field clear button to true/false depending on the passed value.
In Query mode returns whether clear button of search field is visible or not.

---
disableHistoryButton(dhb): boolean
    properties: create, query, edit
    Sets the visibility state of search field history button to true/false depending on the passed value.
In Query mode returns whether history button of search field is visible or not.

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
drawInactiveFrame(dif): boolean
    properties: create, query, edit
    Sets whether the text field draws itself with a frame when it's inactive.
By default, this option is false.

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
    Command executed when the keypad 'Enter' key is pressed.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fileName(fi): string
    properties: create, query, edit
    Text in the field as a filename. This does conversions between
internal and external (UI) file representation.

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
placeholderText(pht): string
    properties: create, query, edit
    Setting this property makes the line edit display a grayed-out placeholder text as long as the text field is empty and the widget doesn't have focus.
By default, this property contains an empty string.

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
receiveFocusCommand(rfc): script
    properties: create, edit
    Command executed when the field receives focus.

---
searchField(sf): boolean
    properties: create
    Creates a search field instead of a text field.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
text(tx): string
    properties: create, query, edit
    The field text.

---
textChangedCommand(tcc): script
    properties: create, edit
    Command executed immediately when the field text changes.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textField.html 
    """


def textFieldButtonGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagbuttonCommand: script, flagbuttonLabel: string, flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableButton: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfileName: string, flagforceChangeCommand: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaginsertText: string, flaginsertionPosition: int, flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagplaceholderText: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flagtext: string, flagtextChangedCommand: script, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 textFieldButtonGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [buttonCommand=script], [buttonLabel=string], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableButton=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fileName=string], [forceChangeCommand=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [insertText=string], [insertionPosition=int], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [placeholderText=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [text=string], [textChangedCommand=script], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textFieldButtonGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command adds a button to the textFieldGrp command.




Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
cmds.textFieldButtonGrp( label='Label', text='Text', buttonLabel='Button' )
cmds.showWindow( window )

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
adjustableColumn(adj): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with the
sizing of the layout.  The column value is a 1-based index.
Passing 0 as argument turns off the previous adjustable column.

---
adjustableColumn2(ad2): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
two columns.

---
adjustableColumn3(ad3): int
    properties: create, edit
    Specifies that the column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
three columns.

---
adjustableColumn4(ad4): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
four columns.

---
adjustableColumn5(ad5): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
five columns.

---
adjustableColumn6(ad6): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
six columns.

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
buttonCommand(bc): script
    properties: create, edit
    Command attached to the button.

---
buttonLabel(bl): string
    properties: create, query, edit
    Label text of the button.

---
changeCommand(cc): script
    properties: create, edit
    Command executed when the field text changes and user presses Enter or Return.

---
columnAlign(cal): [int, string]
    properties: create, edit, multiuse
    Arguments are : column number, alignment type.
Possible alignments are: left | right | center.
Specifies alignment type for the specified column.

---
columnAlign2(cl2): [string, string]
    properties: create, edit
    Sets the text alignment of both columns.  Ignored if there are not
exactly two columns. Valid values are "left", "right", and "center".

---
columnAlign3(cl3): [string, string, string]
    properties: create, edit
    Sets the text alignment for all three columns.  Ignored if there are not
exactly three columns. Valid values are "left", "right", and "center".

---
columnAlign4(cl4): [string, string, string, string]
    properties: create, edit
    Sets the text alignment for all four columns.  Ignored if there are not
exactly four columns. Valid values are "left", "right", and "center".

---
columnAlign5(cl5): [string, string, string, string, string]
    properties: create, edit
    Sets the text alignment for all five columns.  Ignored if there are not
exactly five columns. Valid values are "left", "right", and "center".

---
columnAlign6(cl6): [string, string, string, string, string, string]
    properties: create, edit
    Sets the text alignment for all six columns.  Ignored if there are not
exactly six columns. Valid values are "left", "right", and "center".

---
columnAttach(cat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column number, attachment type, and offset.
Possible attachments are: left | right | both.
Specifies column attachment types and offets.

---
columnAttach2(ct2): [string, string]
    properties: create, edit
    Sets the attachment type of both columns. Ignored if there are not
exactly two columns. Valid values are "left", "right", and "both".

---
columnAttach3(ct3): [string, string, string]
    properties: create, edit
    Sets the attachment type for all three columns. Ignored if there are not
exactly three columns. Valid values are "left", "right", and "both".

---
columnAttach4(ct4): [string, string, string, string]
    properties: create, edit
    Sets the attachment type for all four columns. Ignored if there are not
exactly four columns. Valid values are "left", "right", and "both".

---
columnAttach5(ct5): [string, string, string, string, string]
    properties: create, edit
    Sets the attachment type for all five columns. Ignored if there are not
exactly five columns. Valid values are "left", "right", and "both".

---
columnAttach6(ct6): [string, string, string, string, string, string]
    properties: create, edit
    Sets the attachment type for all six columns. Ignored if there are not
exactly six columns. Valid values are "left", "right", and "both".

---
columnOffset2(co2): [int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach2 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the two columns.  The offsets applied are based on the attachments
specified with the -columnAttach2 flag.  Ignored if there are not exactly
two columns.

---
columnOffset3(co3): [int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach3 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the three columns.  The offsets applied are based on the attachments
specified with the -columnAttach3 flag.  Ignored if there are not exactly
three columns.

---
columnOffset4(co4): [int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach4 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the four columns.  The offsets applied are based on the attachments
specified with the -columnAttach4 flag.  Ignored if there are not exactly
four columns.

---
columnOffset5(co5): [int, int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach5 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the five columns.  The offsets applied are based on the attachments
specified with the -columnAttach5 flag.  Ignored if there are not exactly
five columns.

---
columnOffset6(co6): [int, int, int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach6 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the six columns.  The offsets applied are based on the attachments
specified with the -columnAttach6 flag.  Ignored if there are not exactly
six columns.

---
columnWidth(cw): [int, int]
    properties: create, edit, multiuse
    Arguments are : column number, column width.
Sets the width of the specified column where the first parameter specifies
the column (1 based index) and the second parameter specifies the width.

---
columnWidth1(cw1): int
    properties: create, edit
    Sets the width of the first column. Ignored if there is not
exactly one column.

---
columnWidth2(cw2): [int, int]
    properties: create, edit
    Sets the column widths of both columns. Ignored if there are not
exactly two columns.

---
columnWidth3(cw3): [int, int, int]
    properties: create, edit
    Sets the column widths for all 3 columns. Ignored if there are not
exactly 3 columns.

---
columnWidth4(cw4): [int, int, int, int]
    properties: create, edit
    Sets the column widths for all 4 columns. Ignored if there are not
exactly 4 columns.

---
columnWidth5(cw5): [int, int, int, int, int]
    properties: create, edit
    Sets the column widths for all 5 columns. Ignored if there are not
exactly 5 columns.

---
columnWidth6(cw6): [int, int, int, int, int, int]
    properties: create, edit
    Sets the column widths for all 6 columns. Ignored if there are not
exactly 6 columns.

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
The text in the field can always be changed with
the -tx/text flag regardless of the state of
the -ed/editable flag.

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
enableButton(eb): boolean
    properties: create, query, edit
    Enable state of the button.  By default, this flag is
set to true and the button is enabled.  Specify true, and the
button will appear dimmed or greyed-out indicating it is
disabled.

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
fileName(fi): string
    properties: create, query, edit
    Text in the field as a filename. This does conversions between
internal and external (UI) file representation.

---
forceChangeCommand(fcc): boolean
    properties: create, edit
    If used together with -text or -inserText flag, change command
will be executed after text modification.

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
label(l): string
    properties: create, query, edit
    Label text for the group.

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
placeholderText(pht): string
    properties: create, query, edit
    Setting this property makes the line edit display a grayed-out placeholder text as long as the text field is empty and the widget doesn't have focus.
By default, this property contains an empty string.

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
rowAttach(rat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column, attachment type, offset.
Possible attachments are: top | bottom | both.
Specifies attachment types and offsets for the entire row.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
text(tx): string
    properties: create, query, edit
    Text in the field.

---
textChangedCommand(tcc): script
    properties: create, edit
    Command executed immediately when the field text changes.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textFieldButtonGrp.html 
    """


def textFieldGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfileName: string, flagforceChangeCommand: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaginsertText: string, flaginsertionPosition: int, flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagplaceholderText: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flagtext: string, flagtextChangedCommand: script, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 textFieldGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fileName=string], [forceChangeCommand=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [insertText=string], [insertionPosition=int], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [placeholderText=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [text=string], [textChangedCommand=script], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textFieldGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label text and
editable text field.  The label text is optional.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.textFieldGrp( label='Group 1', text='Editable' )
cmds.textFieldGrp( label='Group 2', text='Non-editable', editable=False )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
adjustableColumn(adj): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with the
sizing of the layout.  The column value is a 1-based index.
Passing 0 as argument turns off the previous adjustable column.

---
adjustableColumn2(ad2): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
two columns.

---
adjustableColumn3(ad3): int
    properties: create, edit
    Specifies that the column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
three columns.

---
adjustableColumn4(ad4): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
four columns.

---
adjustableColumn5(ad5): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
five columns.

---
adjustableColumn6(ad6): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
six columns.

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
    Command executed when the field text changes and user presses Enter or Return.

---
columnAlign(cal): [int, string]
    properties: create, edit, multiuse
    Arguments are : column number, alignment type.
Possible alignments are: left | right | center.
Specifies alignment type for the specified column.

---
columnAlign2(cl2): [string, string]
    properties: create, edit
    Sets the text alignment of both columns.  Ignored if there are not
exactly two columns. Valid values are "left", "right", and "center".

---
columnAlign3(cl3): [string, string, string]
    properties: create, edit
    Sets the text alignment for all three columns.  Ignored if there are not
exactly three columns. Valid values are "left", "right", and "center".

---
columnAlign4(cl4): [string, string, string, string]
    properties: create, edit
    Sets the text alignment for all four columns.  Ignored if there are not
exactly four columns. Valid values are "left", "right", and "center".

---
columnAlign5(cl5): [string, string, string, string, string]
    properties: create, edit
    Sets the text alignment for all five columns.  Ignored if there are not
exactly five columns. Valid values are "left", "right", and "center".

---
columnAlign6(cl6): [string, string, string, string, string, string]
    properties: create, edit
    Sets the text alignment for all six columns.  Ignored if there are not
exactly six columns. Valid values are "left", "right", and "center".

---
columnAttach(cat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column number, attachment type, and offset.
Possible attachments are: left | right | both.
Specifies column attachment types and offets.

---
columnAttach2(ct2): [string, string]
    properties: create, edit
    Sets the attachment type of both columns. Ignored if there are not
exactly two columns. Valid values are "left", "right", and "both".

---
columnAttach3(ct3): [string, string, string]
    properties: create, edit
    Sets the attachment type for all three columns. Ignored if there are not
exactly three columns. Valid values are "left", "right", and "both".

---
columnAttach4(ct4): [string, string, string, string]
    properties: create, edit
    Sets the attachment type for all four columns. Ignored if there are not
exactly four columns. Valid values are "left", "right", and "both".

---
columnAttach5(ct5): [string, string, string, string, string]
    properties: create, edit
    Sets the attachment type for all five columns. Ignored if there are not
exactly five columns. Valid values are "left", "right", and "both".

---
columnAttach6(ct6): [string, string, string, string, string, string]
    properties: create, edit
    Sets the attachment type for all six columns. Ignored if there are not
exactly six columns. Valid values are "left", "right", and "both".

---
columnOffset2(co2): [int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach2 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the two columns.  The offsets applied are based on the attachments
specified with the -columnAttach2 flag.  Ignored if there are not exactly
two columns.

---
columnOffset3(co3): [int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach3 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the three columns.  The offsets applied are based on the attachments
specified with the -columnAttach3 flag.  Ignored if there are not exactly
three columns.

---
columnOffset4(co4): [int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach4 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the four columns.  The offsets applied are based on the attachments
specified with the -columnAttach4 flag.  Ignored if there are not exactly
four columns.

---
columnOffset5(co5): [int, int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach5 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the five columns.  The offsets applied are based on the attachments
specified with the -columnAttach5 flag.  Ignored if there are not exactly
five columns.

---
columnOffset6(co6): [int, int, int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach6 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the six columns.  The offsets applied are based on the attachments
specified with the -columnAttach6 flag.  Ignored if there are not exactly
six columns.

---
columnWidth(cw): [int, int]
    properties: create, edit, multiuse
    Arguments are : column number, column width.
Sets the width of the specified column where the first parameter specifies
the column (1 based index) and the second parameter specifies the width.

---
columnWidth1(cw1): int
    properties: create, edit
    Sets the width of the first column. Ignored if there is not
exactly one column.

---
columnWidth2(cw2): [int, int]
    properties: create, edit
    Sets the column widths of both columns. Ignored if there are not
exactly two columns.

---
columnWidth3(cw3): [int, int, int]
    properties: create, edit
    Sets the column widths for all 3 columns. Ignored if there are not
exactly 3 columns.

---
columnWidth4(cw4): [int, int, int, int]
    properties: create, edit
    Sets the column widths for all 4 columns. Ignored if there are not
exactly 4 columns.

---
columnWidth5(cw5): [int, int, int, int, int]
    properties: create, edit
    Sets the column widths for all 5 columns. Ignored if there are not
exactly 5 columns.

---
columnWidth6(cw6): [int, int, int, int, int, int]
    properties: create, edit
    Sets the column widths for all 6 columns. Ignored if there are not
exactly 6 columns.

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
The text in the field can always be changed with
the -tx/text flag regardless of the state of
the -ed/editable flag.

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
fileName(fi): string
    properties: create, query, edit
    Text in the field as a filename. This does conversions between
internal and external (UI) file representation.

---
forceChangeCommand(fcc): boolean
    properties: create, edit
    If used together with -text or -inserText flag, change command
will be executed after text modification.

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
label(l): string
    properties: create, query, edit
    Label text for the group.

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
placeholderText(pht): string
    properties: create, query, edit
    Setting this property makes the line edit display a grayed-out placeholder text as long as the text field is empty and the widget doesn't have focus.
By default, this property contains an empty string.

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
rowAttach(rat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column, attachment type, offset.
Possible attachments are: top | bottom | both.
Specifies attachment types and offsets for the entire row.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
text(tx): string
    properties: create, query, edit
    Text in the field.

---
textChangedCommand(tcc): script
    properties: create, edit
    Command executed immediately when the field text changes.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textFieldGrp.html 
    """


def textManip(flagvisible: boolean) -> None:
    """Synopsis:
---
---
 textManip([visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textManip is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Hide the text manip, then call headsUpMessage to draw a message in the 3d view. You can't see the message now because it's invisible
cmds.textManip(v=False)
cmds.headsUpMessage('Ouch!', time=5.0)

Show the text manip
cmds.textManip(v=True)

---


Flags:
---


---
visible(v): boolean
    properties: create, query
    Shows/hides the text manip.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textManip.html 
    """


def textScrollList(flagallItems: boolean, flagallItemsUniqueTags: boolean, flagallowAutomaticSelection: boolean, flagallowMultiSelection: boolean, flagannotation: string, flagappend: string, flagappendPosition: tuple[int, string], flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdeleteKeyCommand: script, flagdeselectAll: boolean, flagdeselectIndexedItem: int, flagdeselectItem: string, flagdocTag: string, flagdoubleClickCommand: script, flagdragCallback: script, flagdropCallback: script, flagemptyLabel: string, flagenable: boolean, flagenableAll: boolean, flagenableBackground: boolean, flagenableIndexedItem: tuple[int, boolean], flagenableItem: tuple[string, boolean], flagenableKeyboardFocus: boolean, flagenableUniqueTagItem: tuple[string, boolean], flagexists: boolean, flagfont: string, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglineFont: tuple[int, string], flagmanage: boolean, flagnoBackground: boolean, flagnumberOfItems: boolean, flagnumberOfPopupMenus: boolean, flagnumberOfRows: int, flagnumberOfSelectedItems: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagremoveAll: boolean, flagremoveIndexedItem: int, flagremoveItem: string, flagselectCommand: script, flagselectIndexedItem: int, flagselectItem: string, flagselectUniqueTagItem: string, flagshowIndexedItem: int, flagstatusBarMessage: string, flaguniqueTag: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 textScrollList(
[string]
    , [allItems=boolean], [allItemsUniqueTags=boolean], [allowAutomaticSelection=boolean], [allowMultiSelection=boolean], [annotation=string], [append=string], [appendPosition=[int, string]], [backgroundColor=[float, float, float]], [defineTemplate=string], [deleteKeyCommand=script], [deselectAll=boolean], [deselectIndexedItem=int], [deselectItem=string], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dropCallback=script], [emptyLabel=string], [enable=boolean], [enableAll=boolean], [enableBackground=boolean], [enableIndexedItem=[int, boolean]], [enableItem=[string, boolean]], [enableKeyboardFocus=boolean], [enableUniqueTagItem=[string, boolean]], [exists=boolean], [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [lineFont=[int, string]], [manage=boolean], [noBackground=boolean], [numberOfItems=boolean], [numberOfPopupMenus=boolean], [numberOfRows=int], [numberOfSelectedItems=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [removeAll=boolean], [removeIndexedItem=int], [removeItem=string], [selectCommand=script], [selectIndexedItem=int], [selectItem=string], [selectUniqueTagItem=string], [showIndexedItem=int], [statusBarMessage=string], [uniqueTag=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textScrollList is undoable, queryable, and editable.
Note: The -dgc/dragCallback flag works only on Windows.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.paneLayout()
cmds.textScrollList( numberOfRows=8, allowMultiSelection=True,
            append=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'],
            selectItem='six', showIndexedItem=4 )
cmds.showWindow()

cmds.window()
cmds.paneLayout()
cmds.textScrollList( "myControlObj", allowMultiSelection=True,
            append=[ "Only two things are infinite, the universe and human stupidity, and I'm not sure about the former.",
                     "Each problem that I solved became a rule, which served afterwards to solve other problems."],
            uniqueTag=["Albert Einstein","Rene Descartes"])
cmds.showWindow()
cmds.textScrollList( "myControlObj", edit=True, selectUniqueTagItem=["Albert Einstein"])
cmds.textScrollList( "myControlObj", query=True, selectUniqueTagItem=True)
cmds.textScrollList( "myControlObj", edit=True, append=["Your theory is crazy, but it's not crazy enough to be true."],
                                                uniqueTag=["Niels Bohr"] )
cmds.textScrollList( "myControlObj", edit=True, selectUniqueTagItem=["Rene Descartes", "Niels Bohr"])
cmds.textScrollList( "myControlObj", query=True, selectUniqueTagItem=True)

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
allItems(ai): boolean
    properties: query
    All the items.

---
allItemsUniqueTags(ait) 2024: boolean
    properties: query
    Return all the items as unique tags.

---
allowAutomaticSelection(aas): boolean
    properties: create, query, edit
    Specify automatic selection mode.  When automaticSelection
is on each item that the mouse is over (during dragging once an
item has been selected) will be selected.  Thus,
if -sc/selectCommand someCommand is set, someCommand
will be called for each selected item.
If -aas/allowAutomaticSelection is off, then only the item
selected when the mouse button is up will be the selected item,
so -sc/selectCommand someCommand is only called once if
it is set.

---
allowMultiSelection(ams): boolean
    properties: create, query, edit
    Specify multi or single selection mode.

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
append(a): string
    properties: create, edit, multiuse
    Add an item to the end of the list.

---
appendPosition(ap): [int, string]
    properties: create, edit, multiuse
    Append an item at the specified position.
The position is a 1-based index.

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
deleteKeyCommand(dkc): script
    properties: create, edit
    Specify the command to be executed when the delete or
backspace key is pressed.

---
deselectAll(da): boolean
    properties: create, edit
    Deselect all items.

---
deselectIndexedItem(dii): int
    properties: create, edit, multiuse
    Deselect the indexed item.  Indices are 1-based.

---
deselectItem(di): string
    properties: create, edit, multiuse
    Deselect the item that contains the specified text.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
doubleClickCommand(dcc): script
    properties: create, edit
    Specify the command to be executed when an item is double
clicked.

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
emptyLabel(el) 2024: string
    properties: create, query, edit
    String that is displayed when the list is empty.

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enableAll(ea) 2024: boolean
    properties: create, edit
    Enable all items.

---
enableBackground(ebg): boolean
    properties: create, query, edit
    Enables the background color of the control.

---
enableIndexedItem(eii) 2024: [int, boolean]
    properties: create, edit, multiuse
    Enable/disable an item using on the item index. Indices are 1-based.

---
enableItem(ei) 2024: [string, boolean]
    properties: create, edit, multiuse
    Enable/disable an item using the item text.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
enableUniqueTagItem(eut) 2024: [string, boolean]
    properties: create, edit, multiuse
    Enable/disable an item using on the unique item tag.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
font(fn): string
    properties: create, query, edit
    The font for the list items.  Valid values are
"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
"smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".

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
lineFont(lf): [int, string]
    properties: create, edit, multiuse
    Specify the font for a specific line of the list.
The indices are 1-based. Valid font values are
"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
"smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".

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
numberOfItems(ni): boolean
    properties: query
    Number of items.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
numberOfRows(nr): int
    properties: create, query, edit
    Number of visible rows.

---
numberOfSelectedItems(nsi): boolean
    properties: query
    Number of selected items.

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
removeAll(ra): boolean
    properties: create, edit
    Remove all items.

---
removeIndexedItem(rii): int
    properties: create, edit, multiuse
    Remove the indexed item. Indices are 1-based.

---
removeItem(ri): string
    properties: create, edit, multiuse
    Remove the item with the specified text.

---
selectCommand(sc): script
    properties: create, edit
    Specify the command to be executed when an item is selected.

---
selectIndexedItem(sii): int
    properties: create, query, edit, multiuse
    Select the indexed item. Indices are 1-based.

---
selectItem(si): string
    properties: create, query, edit, multiuse
    Select the item that contains the specified text.

---
selectUniqueTagItem(sut): string
    properties: create, query, edit, multiuse
    Allow item selections based on the unique tag.
In query mode, it will return the unique tag of the selected items.

---
showIndexedItem(shi): int
    properties: create, edit
    Show the indexed item.  Scroll the list as necessary so that
the indexed item is visible.  Indices are 1-based.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
uniqueTag(utg): string
    properties: create, edit, multiuse
    This flag can only be used in conjunction with the append or the appendPosition flag.
The string specifies a unique tag for the appended item; the tag can then be used to query an item.
This tag provides an alternate way to uniquely identify a list item using a string instead of by index.
Tags are case insensitive.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textScrollList.html 
    """


def textureDeformer(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagdirection: string, flagenvelope: float, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flagname: string, flagoffset: float, flagparallel: boolean, flagpointSpace: string, flagprune: boolean, flagremove: boolean, flagselectedComponents: boolean, flagsplit: boolean, flagstrength: float, flaguseComponentTags: boolean, flagvectorOffset: tuple[float, float, float], flagvectorSpace: string, flagvectorStrength: tuple[float, float, float]) -> string:
    """Synopsis:
---
---
 textureDeformer(
selectionList
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [deformerTools=boolean], [direction=string], [envelope=float], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string], [offset=float], [parallel=boolean], [pointSpace=string], [prune=boolean], [remove=boolean], [selectedComponents=boolean], [split=boolean], [strength=float], [useComponentTags=boolean], [vectorOffset=[float, float, float]], [vectorSpace=string], [vectorStrength=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textureDeformer is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.polySphere(constructionHistory=True, object=True, radius=3.0)

Deforms whatever is currently on the selection list
and set the attributes value for the deformer node
cmds.textureDeformer(envelope=0.8, strength=1.0, offset=1.0, direction="Normal", pointSpace="World")

---
Return:
---


    string: Texture deformer node name

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
direction(d): string
    properties: create
    Set the deformation direction of texture deformer
It can only handle three types: "Normal", "Handle" and "Vector".
"Normal"  each vertices use its own normal vector.
"Handle"  all vertices use Up vector of the handle.
"Vector"  each vertices use RGB color vector
strings.

---
envelope(en): float
    properties: create
    Set the envelope of texture deformer.
Envelope determines the percent
of deformation. The final result is
(color * normal * strength + offset) * envelope

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
offset(o): float
    properties: create
    Set the offset of texture deformer.
Offset plus a translation on the final
deformed vertices.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
pointSpace(ps): string
    properties: create
    Set the point space of texture deformer.
It can only handle three strings: "World", "Local" and "UV".
"World"   map world space to color space.
"Local"	  map local space to color space.
"UV"	  map UV space to color space.
strings.

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
strength(s): float
    properties: create
    Set the strength of texture deformer.
Strength determines how strong the
object is deformed.

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

---
vectorOffset(vo): [float, float, float]
    properties: create
    Set the vector offset of texture deformer.
Vector offset indicates the offset of the
deformation on the vector mode.

---
vectorSpace(vsp): string
    properties: create
    Set the vector space of texture deformer.
It can only handle three strings: "Object", "World" and "Tangent".
"Object"   	use color vector in object space
"World"	 	use color vector in world space
"Tangent"	use color vector in tangent space
strings.

---
vectorStrength(vs): [float, float, float]
    properties: create
    Set the vector strength of texture deformer.
Vector strength determines how strong the
object is deformed on the vector mode.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textureDeformer.html 
    """


def texturePlacementContext(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglabelMapping: boolean, flagname: string) -> string:
    """Synopsis:
---
---
 texturePlacementContext([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [labelMapping=boolean], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

texturePlacementContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.texturePlacementContext()

---
Return:
---


    string: The name of the context created

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
labelMapping(lm): boolean
    properties: create, query, edit
    Set the context to label mapping.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/texturePlacementContext.html 
    """


def textureWindow(flagactiveSelectionOnTop: boolean, flagaxesColor: tuple[float, float, float], flagbackFacingColor: tuple[float, float, float, float], flagcapture: string, flagcaptureSequenceNumber: int, flagchangeCommand: tuple[string, string, string, string], flagcheckerColor1: tuple[float, float, float], flagcheckerColor2: tuple[float, float, float], flagcheckerColorMode: int, flagcheckerDensity: int, flagcheckerDrawTileLabels: boolean, flagcheckerGradient1: tuple[float, float, float], flagcheckerGradient2: tuple[float, float, float], flagcheckerGradientOverlay: boolean, flagcheckerTileLabelColor: tuple[float, float, float], flagclearImage: boolean, flagcmEnabled: boolean, flagcontrol: boolean, flagdefineTemplate: string, flagdisplayAxes: boolean, flagdisplayCheckered: boolean, flagdisplayDistortion: boolean, flagdisplayDivisionLines: boolean, flagdisplayGridLines: boolean, flagdisplayImage: int, flagdisplayIsolateSelectHUD: boolean, flagdisplayLabels: boolean, flagdisplayOverlappingUVCountHUD: boolean, flagdisplayPreselection: boolean, flagdisplayReversedUVCountHUD: boolean, flagdisplaySolidMap: boolean, flagdisplayStyle: string, flagdisplayTextureBorder: boolean, flagdisplayUVPositionHUD: boolean, flagdisplayUVShellCountHUD: boolean, flagdisplayUVStatisticsHUD: boolean, flagdisplayUsedPercentageHUD: boolean, flagdistortionAlpha: float, flagdistortionPerObject: boolean, flagdivisions: int, flagdocTag: string, flagdoubleBuffer: boolean, flagdrawAxis: boolean, flagdrawSubregions: boolean, flagexists: boolean, flagexposure: float, flagfilter: string, flagforceMainConnection: string, flagforceRebake: boolean, flagframeAll: boolean, flagframeSelected: boolean, flagfrontFacingColor: tuple[float, float, float, float], flaggamma: float, flaggridLinesColor: tuple[float, float, float], flaggridNumbersColor: tuple[float, float, float], flaghighlightConnection: string, flagimageBaseColor: tuple[float, float, float], flagimageDim: boolean, flagimageDisplay: boolean, flagimageNames: boolean, flagimageNumber: int, flagimagePixelSnap: boolean, flagimageRatio: boolean, flagimageRatioValue: float, flagimageSize: boolean, flagimageTileRange: tuple[float, float, float, float], flagimageUnfiltered: boolean, flaginternalFaces: boolean, flaglabelPosition: string, flagloadImage: string, flaglockMainConnection: boolean, flagmainListConnection: string, flagmaxResolution: int, flagmultiColorAlpha: float, flagnbImages: boolean, flagnextView: boolean, flagnumUvSets: boolean, flagnumberOfImages: int, flagnumberOfTextures: int, flagpanel: string, flagparent: string, flagpreviousView: boolean, flagrealSize: boolean, flagrefresh: boolean, flagrelatedFaces: boolean, flagremoveAllImages: boolean, flagremoveImage: boolean, flagrendererString: string, flagreset: boolean, flagsaveImage: boolean, flagscaleBlue: float, flagscaleGreen: float, flagscaleRed: float, flagselectInternalFaces: boolean, flagselectRelatedFaces: boolean, flagselectionConnection: string, flagsetUvSet: int, flagsingleBuffer: boolean, flagsize: float, flagsolidMap3dView: boolean, flagsolidMapColorSeed: int, flagsolidMapPerShell: boolean, flagspacing: float, flagstateString: boolean, flagstyle: int, flagsubdivisionLinesColor: tuple[float, float, float], flagtextureBorder3dView: boolean, flagtextureBorderColor: tuple[float, float, float], flagtextureBorderWidth: int, flagtextureNames: boolean, flagtextureNumber: int, flagtileLabels: boolean, flagtileLinesColor: tuple[float, float, float], flagtoggle: boolean, flagtoggleExposure: boolean, flagtoggleGamma: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseFaceGroup: boolean, flaguseTemplate: string, flagusedPercentageHUDRange: tuple[float, float, float, float], flaguvSets: boolean, flagviewPortImage: boolean, flagviewTransformName: string, flagwireframeComponentColor: tuple[float, float, float, float], flagwireframeObjectColor: tuple[float, float, float, float], flagwriteImage: string) -> string:
    """Synopsis:
---
---
 textureWindow(
string
    , [activeSelectionOnTop=boolean], [axesColor=[float, float, float]], [backFacingColor=[float, float, float, float]], [capture=string], [captureSequenceNumber=int], [changeCommand=[string, string, string, string]], [checkerColor1=[float, float, float]], [checkerColor2=[float, float, float]], [checkerColorMode=int], [checkerDensity=int], [checkerDrawTileLabels=boolean], [checkerGradient1=[float, float, float]], [checkerGradient2=[float, float, float]], [checkerGradientOverlay=boolean], [checkerTileLabelColor=[float, float, float]], [clearImage=boolean], [cmEnabled=boolean], [control=boolean], [defineTemplate=string], [displayAxes=boolean], [displayCheckered=boolean], [displayDistortion=boolean], [displayDivisionLines=boolean], [displayGridLines=boolean], [displayImage=int], [displayIsolateSelectHUD=boolean], [displayLabels=boolean], [displayOverlappingUVCountHUD=boolean], [displayPreselection=boolean], [displayReversedUVCountHUD=boolean], [displaySolidMap=boolean], [displayStyle=string], [displayTextureBorder=boolean], [displayUVPositionHUD=boolean], [displayUVShellCountHUD=boolean], [displayUVStatisticsHUD=boolean], [displayUsedPercentageHUD=boolean], [distortionAlpha=float], [distortionPerObject=boolean], [divisions=int], [docTag=string], [doubleBuffer=boolean], [drawAxis=boolean], [drawSubregions=boolean], [exists=boolean], [exposure=float], [filter=string], [forceMainConnection=string], [forceRebake=boolean], [frameAll=boolean], [frameSelected=boolean], [frontFacingColor=[float, float, float, float]], [gamma=float], [gridLinesColor=[float, float, float]], [gridNumbersColor=[float, float, float]], [highlightConnection=string], [imageBaseColor=[float, float, float]], [imageDim=boolean], [imageDisplay=boolean], [imageNames=boolean], [imageNumber=int], [imagePixelSnap=boolean], [imageRatio=boolean], [imageRatioValue=float], [imageSize=boolean], [imageTileRange=[float, float, float, float]], [imageUnfiltered=boolean], [internalFaces=boolean], [labelPosition=string], [loadImage=string], [lockMainConnection=boolean], [mainListConnection=string], [maxResolution=int], [multiColorAlpha=float], [nbImages=boolean], [nextView=boolean], [numUvSets=boolean], [numberOfImages=int], [numberOfTextures=int], [panel=string], [parent=string], [previousView=boolean], [realSize=boolean], [refresh=boolean], [relatedFaces=boolean], [removeAllImages=boolean], [removeImage=boolean], [rendererString=string], [reset=boolean], [saveImage=boolean], [scaleBlue=float], [scaleGreen=float], [scaleRed=float], [selectInternalFaces=boolean], [selectRelatedFaces=boolean], [selectionConnection=string], [setUvSet=int], [singleBuffer=boolean], [size=float], [solidMap3dView=boolean], [solidMapColorSeed=int], [solidMapPerShell=boolean], [spacing=float], [stateString=boolean], [style=int], [subdivisionLinesColor=[float, float, float]], [textureBorder3dView=boolean], [textureBorderColor=[float, float, float]], [textureBorderWidth=int], [textureNames=boolean], [textureNumber=int], [tileLabels=boolean], [tileLinesColor=[float, float, float]], [toggle=boolean], [toggleExposure=boolean], [toggleGamma=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useFaceGroup=boolean], [useTemplate=string], [usedPercentageHUDRange=[float, float, float, float]], [uvSets=boolean], [viewPortImage=boolean], [viewTransformName=string], [wireframeComponentColor=[float, float, float, float]], [wireframeObjectColor=[float, float, float, float]], [writeImage=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

textureWindow is undoable, queryable, and editable.
The UV Editor displays texture mapped polygon objects in 2D
texture space. Only active objects are visible in this window.

The UV Editor has the ability to display two types of images. The
Texture Image is a visualisation of the current texture and associated
placement parameters. The Editor Image is a user specified image loaded
from disk.

A UV Editor can be invoked by selecting the "Window -> UV
Texture Editor..." menu item from the main maya menu listing that
appears at the top of the maya window. It can also be invoked by
selecting the "Panel -> UV Editor" item under the "Panels"
menu item that appears at the top right hand corner of the view.

As a UV Editor typically exists at start-up time, and as only
one of these can exist at any given time, this command is normally
used to query and edit the editor settings.




Example:
---
import maya.cmds as cmds

As a UV Editor typically exists on start-up, you normally
will not need to create one.. Hence all the examples that follow
explain how to query and edit the editor settings.

Get the panel that the editor belongs to.
texWinName = cmds.getPanel(sty='polyTexturePlacementPanel')

Get the space between main grid lines
cmds.textureWindow(texWinName[0], q=True, sp=True)
Result: 0.05 ---


Change the space between main grid lines
cmds.textureWindow( texWinName[0], e=True, sp=0.1 )

Get the size of the grid
cmds.textureWindow( texWinName[0], q=True, s=True )
Result: 12 ---


Change the size of the grid
cmds.textureWindow( texWinName[0], e=True, s=0.8 )

Zoom on the whole scene
cmds.textureWindow( texWinName[0], e=True, fa=True )

Set display mode to related (connected) faces
cmds.textureWindow(texWinName[0], e=True, rf=True )

---
Return:
---


    string: The name of the texture window

Flags:
---


---
activeSelectionOnTop(ast): boolean
    properties: create, query, edit
    Display the solid map / distortion of active selection on top of others.

---
axesColor(axc): [float, float, float]
    properties: create, query, edit
    The color of axes, default is 0.0 0.0 1.0

---
backFacingColor(bfc): [float, float, float, float]
    properties: create, query, edit
    Sets or queries the RGBA back facing color.

---
capture(cpt): string
    properties: edit
    Perform an one-time capture of the viewport to the named image file on disk.

---
captureSequenceNumber(csn): int
    properties: edit
    When a number greater or equal to 0 is specified each
subsequent refresh will save an image file to disk if the
capture flag has been enabled.

The naming of the file is:

{root name}.#.{extension}

if the name {root name}.{extension} is used for the capture flag argument.
The value of # starts at the number specified to for this argument and
increments for each subsequent refresh.

Sequence capture can be disabled by specifying a number less
than 0 or an empty file name for the capture flag.

---
changeCommand(cc): [string, string, string, string]
    properties: create, query, edit
    Parameters:

First string: command
Second string: editorName
Third string: editorCmd
Fourth string: updateFunc


Call the command when something changes in the editor The command
should have this prototype :

command(string $editor, string $editorCmd, string $updateFunc, int $reason)

The possible reasons could be :

0: no particular reason
1: scale color
2: buffer (single/double)
3: axis 
4: image displayed
5: image saved in memory

---
checkerColor1(cc1): [float, float, float]
    properties: create, query, edit
    Sets the first color of the checker and identification pattern, when color mode is 2-colors.

---
checkerColor2(cc2): [float, float, float]
    properties: create, query, edit
    Sets the second color of the checker and identification pattern, when color mode is 2-colors.

---
checkerColorMode(ccm): int
    properties: create, query, edit
    Sets the color mode of the checker and identification pattern.
0: multi-colors;
1: 2-colors;

---
checkerDensity(cd): int
    properties: create, query, edit
    Sets the density of the checker and identification pattern.

---
checkerDrawTileLabels(cdt): boolean
    properties: create, query, edit
    Toggles the checker tile label display.

---
checkerGradient1(cg1): [float, float, float]
    properties: create, query, edit
    Sets the first gradient of the checker and identification pattern, when color mode is 2-colors.

---
checkerGradient2(cg2): [float, float, float]
    properties: create, query, edit
    Sets the second gradient of the checker and identification pattern, when color mode is 2-colors.

---
checkerGradientOverlay(cgo): boolean
    properties: create, query, edit
    Toggle application of the gradient.

---
checkerTileLabelColor(ctc): [float, float, float]
    properties: create, query, edit
    Sets the checker tile label color.

---
clearImage(ci): boolean
    properties: edit
    Clears the current Editor Image.

---
cmEnabled(cme): boolean
    properties: query, edit
    Turn on or off applying color management in the editor.  If set, the color
management configuration set in the current editor is used.

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
displayAxes(dax): boolean
    properties: query, edit
    Specify true to display the grid axes.

---
displayCheckered(dct): boolean
    properties: create, query, edit
    Display a unique checker and identification pattern for each UV tiles.

---
displayDistortion(ddt): boolean
    properties: create, query, edit
    Display the layout in shaded colors to indentify areas with stretched/squashed UVs

---
displayDivisionLines(ddl): boolean
    properties: query, edit
    Specify true to display the subdivision lines between
grid lines.

---
displayGridLines(dgl): boolean
    properties: query, edit
    Specify true to display the grid lines.

---
displayImage(di): int
    properties: query, edit
    Set a particular image in the Editor Image Stack as the current Editor Image.
Images are added to the Editor Image Stack using the "si/saveImage" flag.

---
displayIsolateSelectHUD(dih): boolean
    properties: create, query, edit
    Show heads-up display of isolate selection

---
displayLabels(dl): boolean
    properties: query, edit
    Specify true to display the grid line numeric labels.

---
displayOverlappingUVCountHUD(doh): boolean
    properties: create, query, edit
    Show heads-up display of overlapping UV count, as a part UV Statistics HUD

---
displayPreselection(dps): boolean
    properties: create, query, edit
    Toggles the pre-selection display.

---
displayReversedUVCountHUD(drh): boolean
    properties: create, query, edit
    Show heads-up display of UV Shells, as a part UV Statistics HUD

---
displaySolidMap(dsm): boolean
    properties: create, query, edit
    Display a solid overlay for the active texture map.

---
displayStyle(dst): string
    properties: create, query, edit
    Set the mode to display the image. Valid values are:

"color" to display the basic RGB image
"mask" to display the mask channel
"lum" to display the luminance of the image

---
displayTextureBorder(dtb): boolean
    properties: create, query, edit
    Toggles the texture borders display.

---
displayUVPositionHUD(duv): boolean
    properties: create, query, edit
    Show heads-up display of UV positions

---
displayUVShellCountHUD(dsh): boolean
    properties: create, query, edit
    Show heads-up display of UV Shell count, as a part UV Statistics HUD

---
displayUVStatisticsHUD(duh): boolean
    properties: create, query, edit
    Show heads-up display of UV Statistics

---
displayUsedPercentageHUD(dph): boolean
    properties: create, query, edit
    Show heads-up display of used UV space percentage, as a part UV Statistics HUD

---
distortionAlpha(dta): float
    properties: create, query, edit
    Set or query the distortion display alpha.

---
distortionPerObject(dpo): boolean
    properties: create, query, edit
    Toggles the per-object distortion display.

---
divisions(d): int
    properties: create, query, edit
    Sets the number of subdivisions between main grid lines.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
doubleBuffer(dbf): boolean
    properties: create, query, edit
    Set the display in double buffer mode

---
drawAxis(da): boolean
    properties: create, query, edit
    Set or query whether the axis will be drawn.

---
drawSubregions(dsr): boolean
    properties: create, query, edit
    Toggles the subregion display.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
exposure(exp): float
    properties: query, edit
    The exposure value used by the color management of the current editor.

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
forceRebake(frb): boolean
    properties: create, edit
    Forces the current cache texture to refresh.

---
frameAll(fa): boolean
    properties: create
    This will zoom on the whole scene.

---
frameSelected(fs): boolean
    properties: create
    This will zoom on the currently selected objects.

---
frontFacingColor(ffc): [float, float, float, float]
    properties: create, query, edit
    Sets or queries the RGBA front facing color.

---
gamma(ga): float
    properties: query, edit
    The gamma value used by the color management of the current editor.

---
gridLinesColor(glc): [float, float, float]
    properties: create, query, edit
    The color of grid lines, default is 0.325 0.325 0.325

---
gridNumbersColor(gnc): [float, float, float]
    properties: create, query, edit
    The color of grid numbers, default is 0.2 0.2 0.2

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
imageBaseColor(ibc): [float, float, float]
    properties: create, query, edit
    The base color of the image, default is white 1.0 1.0 1.0

---
imageDim(idm): boolean
    properties: create, query, edit
    Toggles the image dimming.

---
imageDisplay(id): boolean
    properties: query, edit
    Toggles the Texture Image display.

---
imageNames(imn): boolean
    properties: query
    List image names for all Texture Images available for display,
if any.

---
imageNumber(imageNumber): int
    properties: query, edit
    Sets the number of Texture Images to display.
This depends on the number of textures corresponding to
the current selection. If there are N textures, then the
possible Texture Image numbers are 0 to N-1.

---
imagePixelSnap(ip): boolean
    properties: query, edit
    Sets a mode so that UV transformations in
the UV Texture Editor will cause UV values to snap
to image pixel corners. Which pixels are used depends on whether
a Texture Image or an Editor Image is being displayed. If both
are displayed, the Texture Image pixels will be used.

---
imageRatio(imr): boolean
    properties: query, edit
    Sets the window to draw using the Texture Image's height versus
width ratio. If the width is greater than the height,
then the width is set to be 1 "unit" in the window,
and the height is adjusted by width divided by height. This
only affects the display of a Texture Image, not an Editor Image.

---
imageRatioValue(irv): float
    properties: query
    Query current image ratio value in UV Editor.

---
imageSize(imageSize): boolean
    properties: query
    Returns the size of the Texture Image currently being displayed.
The values returned are width followed by height.
Image size can only be queried.

---
imageTileRange(itr): [float, float, float, float]
    properties: query, edit
    Sets the UV range of the display. The 4 values specify the
minimum U, V and maximum U, V in that order. When viewing a texture
image, these values affect how many times the image is tiled based on
appropriate parameters (e.g. Repeat UV, Mirror, Wrap, etc...)
When viewing an Editor Image these values determine the visible size
of the image. For example, setting the range to ( 0, 0, 2, 1 ) will
cause the Editor Image to be loaded into a 2x1 rectangle, distorting
it as necessary to fill the available space.

---
imageUnfiltered(iuf): boolean
    properties: query, edit
    Sets the Texture Image to draw unfiltered. The image will
appear "pixelated" when the display resolution is higher than the
resolution of the image.

---
internalFaces(internalFaces): boolean
    properties: create, query, edit
    Display contained faces by the selected components.

---
labelPosition(lp): string
    properties: query, edit
    The position of the grid's numeric labels. Valid values are
"axis" and "edge".

---
loadImage(li): string
    properties: edit
    load an image from disk and set it as the current Editor Image

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
maxResolution(mrs): int
    properties: create, query, edit
    This flag will set the current cached texture's maximum resolution.

---
multiColorAlpha(mca): float
    properties: create, query, edit
    Sets the multi-color alpha of shaded UVs.

---
nbImages(nim): boolean
    properties: query
    returns the number of images

---
nextView(nv): boolean
    properties: edit
    Switches to the next view.

---
numUvSets(nuv): boolean
    properties: create, query, edit
    This flag will return the number of UV sets for selected
objects in the texture window.

---
numberOfImages(ni): int
    properties: query
    The number of Texture Images currently available.
for display.

---
numberOfTextures(nt): int
    properties: query
    The number of textures currently available.
for display.

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
previousView(pv): boolean
    properties: edit
    Switches to the previous view.

---
realSize(rs): boolean
    properties: create
    This will display the image with the size of the
internal buffer. Note: This argument no long has
any affect on image display.

---
refresh(ref): boolean
    properties: edit
    requests a refresh of the current Editor Image.

---
relatedFaces(rf): boolean
    properties: create, query, edit
    Display connected faces by the selected components.

---
removeAllImages(ra): boolean
    properties: edit
    remove all the Editor Images from the Editor Image Stack

---
removeImage(ri): boolean
    properties: edit
    remove the current Editor Image from the Editor Image Stack

---
rendererString(rds): string
    properties: create, query, edit
    Set or query the string describing the current renderer.

---
reset(r): boolean
    properties: create
    Resets the ground plane to its default values.

---
saveImage(si): boolean
    properties: edit
    save the current Editor Image to memory. Saved Editor Images are
stored in an Editor Image Stack. The most recently saved image is stored in
position 0, the second most recently saved image in position 1,
and so on... To set the current Editor Image to a previously saved
image use the "di/displayImage" flag.

---
scaleBlue(sb): float
    properties: create, query, edit
    Define the scaling factor for the blue component
in the View. The default value is 1 and can be
between -1000 to +1000

---
scaleGreen(sg): float
    properties: create, query, edit
    Define the scaling factor for the green component
in the View. The default value is 1 and can be
between -1000 to +1000

---
scaleRed(sr): float
    properties: create, query, edit
    Define the scaling factor for the red component
in the View. The default value is 1 and can be
between -1000 to +1000

---
selectInternalFaces(sif): boolean
    properties: create, query, edit
    Add to selectionList the faces which are contained by
(internal to) selected components.

---
selectRelatedFaces(srf): boolean
    properties: create
    Add to selectionList the faces which are connected to
(non-internally related to) selected components.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
setUvSet(suv): int
    properties: create, edit
    This flag will set the current UV set on one given
selected object within the texture window.

---
singleBuffer(sbf): boolean
    properties: create, query, edit
    Set the display in single buffer mode

---
size(s): float
    properties: create, query, edit
    Sets the size of the grid.

---
solidMap3dView(s3d): boolean
    properties: create, query, edit
    Display a solid overlay for the active texture map in 3D viewport.

---
solidMapColorSeed(scs): int
    properties: create, query, edit
    Sets the multi-color seed of shaded UVs.

---
solidMapPerShell(sps): boolean
    properties: create, query, edit
    Display a solid overlay with a random color per shell.

---
spacing(sp): float
    properties: create
    Sets the spacing between main grid lines.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
style(st): int
    properties: query, edit
    This flag is obsolete and should not be used.

---
subdivisionLinesColor(sdc): [float, float, float]
    properties: create, query, edit
    The color of subdivision lines, default is 0.25 0.25 0.25

---
textureBorder3dView(t3d): boolean
    properties: create, query, edit
    Toggles the texture borders display in 3d viewport.

---
textureBorderColor(tbc): [float, float, float]
    properties: create, query, edit
    Sets the display color of texture border.

---
textureBorderWidth(tbw): int
    properties: create, query, edit
    Set the display edge width of texture border.

---
textureNames(txn): boolean
    properties: query
    Texture names for all Texture Images available for display,
if any.

---
textureNumber(tn): int
    properties: query, edit
    Sets the number of textures to display
This depends on the number of textures corresponding to
the current selection. If there are N textures, then the
possible Texture Image numbers are 0 to N-1.

---
tileLabels(tlb): boolean
    properties: create, query, edit
    Toggles the texture tile label display.

---
tileLinesColor(tlc): [float, float, float]
    properties: create, query, edit
    The color of tile lines, default is 0.0 0.0 0.0

---
toggle(tgl): boolean
    properties: create, query, edit
    Toggles the ground plane display.

---
toggleExposure(tge): boolean
    properties: edit
    Toggles between the current and the default exposure value of the editor.

---
toggleGamma(tgg): boolean
    properties: edit
    Toggles between the current and the default gamma value of the editor.

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
useFaceGroup(uf): boolean
    properties: create, query, edit
    Display faces that are associated with the groupId
that is set on the mesh node that is drawn.
(The attribute "displayFacesWithGroupId")

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
usedPercentageHUDRange(upr): [float, float, float, float]
    properties: create, query, edit
    Sets the range when calculating used UV space percentage. The 4 values specify the minimum U, V and maximum U, V in that order., default is 0 0 1 1.

---
uvSets(uvs): boolean
    properties: create, query, edit
    This flag will return strings containing
UV set and object name pairs for selected
objects in the texture window. The syntax of
each pair is "objectName | uvSetName", where |
is a literal character.

---
viewPortImage(vpi): boolean
    properties: create, edit
    Toggles the view port/ caching Texture Images.

---
viewTransformName(vtn): string
    properties: query, edit
    Sets the view pipeline to be applied if color management is enabled in the
current editor.

---
wireframeComponentColor(wcc): [float, float, float, float]
    properties: create, query, edit
    Sets or queries the RGBA component wireframe color.

---
wireframeObjectColor(woc): [float, float, float, float]
    properties: create, query, edit
    Sets or queries the RGBA object wireframe color.

---
writeImage(wi): string
    properties: edit
    write the current Editor Image to disk

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/textureWindow.html 
    """


def threadCount(flagnumberOfThreads: int) -> None:
    """Synopsis:
---
---
 threadCount([numberOfThreads=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

threadCount is undoable, queryable, and NOT editable.

A physical CPU with hyperthreading counts as two logical CPUs
A dual-core CPU counts as two logical CPUs

With some workloads, using one thread per logical CPU may
not perform well. This is sometimes the case with
hyperthreading. It is worth experimenting with different
numbers of threads to see which gives the best performance.
Note that having more threads can mean Maya uses more memory.

Setting a value of zero means the number of threads used will
equal the number of logical processors in the system.




Example:
---
import maya.cmds as cmds

sets Maya to use 4 threads for multithreaded evaluation
cmds.threadCount( n=4 )

sets Maya to use one thread per logical CPU
cmds.threadCount( n=0 )

query number of threads currently set
cmds.threadCount( q=True, n=True )

---


Flags:
---


---
numberOfThreads(n): int
    properties: create, query
    Sets the number of threads to use

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/threadCount.html 
    """


def threePointArcCtx(flagdegree: uint, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagspans: uint) -> string:
    """Synopsis:
---
---
 threePointArcCtx([degree=uint], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [spans=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

threePointArcCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To create a new context that will create curves of degree 1:
cmds.threePointArcCtx( "arcContext", degree=1 )
cmds.setToolTo("arcContext")

To query the degree of an existing context:
cmds.threePointArcCtx( "arcContext", q=True, degree=True )

To edit the degree of an existing context:
cmds.threePointArcCtx( "arcContext", e=True, degree=3 )

---
Return:
---


    string: (name of the new context)

Flags:
---


---
degree(d): uint
    properties: create, query, edit
    VAlid values are 1 or 3. Default degree 3.

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
spans(s): uint
    properties: create, query, edit
    Default is 8.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/threePointArcCtx.html 
    """


def thumbnailCaptureComponent(flagcapture: boolean, flagcapturedFrameCount: boolean, flagcloseCurrentSession: boolean, flagdelete: boolean, flagendFrame: int, flagfileDialogCallback: string, flagisSessionOpened: boolean, flaglaunchedFromOptionsBox: boolean, flagpreviewPath: boolean, flagremoveProjectThumbnail: string, flagsave: string, flagstartFrame: int) -> None:
    """Synopsis:
---
---
 thumbnailCaptureComponent(
[string]
    , [capture=boolean], [capturedFrameCount=boolean], [closeCurrentSession=boolean], [delete=boolean], [endFrame=int], [fileDialogCallback=string], [isSessionOpened=boolean], [launchedFromOptionsBox=boolean], [previewPath=boolean], [removeProjectThumbnail=string], [save=string], [startFrame=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

thumbnailCaptureComponent is NOT undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds


   Launch an option box used to capture the scene between frame 20 and 60


cmds.thumbnailCaptureComponent(capture=True, startFrame=20, endFrame=60)


   Save the generated image sequence for "mesh.mb"


cmds.thumbnailCaptureComponent(save='C:/maya/projects/default/scenes/mesh.mb')


   Delete generated thumbnails for current capture session

cmds.thumbnailCaptureComponent(delete=True)


   Return the path of generated sequence preview.


cmds.thumbnailCaptureComponent(q=True, previewPath=True)
Result: C:/Users/perradw/Documents/maya/projects/default/images/.MayaTempCaptureComponent/tmp.preview ---


---


Flags:
---


---
capture(c): boolean
    properties: create
    Create a new component to capture a sequence of image for the current scene.

---
capturedFrameCount(cfc): boolean
    properties: query
    Query only. Return the number of frames that have been captured.

---
closeCurrentSession(ccs): boolean
    properties: create
    Delete the current thumbnail component (preview image will be destroyed).

---
delete(d): boolean
    properties: create
    Delete the generated image sequence and preview for the current capture session.

---
endFrame(ef): int
    properties: create, query
    Set the end captured frame. Only valid when the -c/capture flag is set.
If -sf/startFrame is set and not -ef/endFrame, or if endFrame is smaller than startFrame, endFrame will be automatically set to startFrame.

---
fileDialogCallback(fdc): string
    properties: create
    MEL only. Set the callback file dialog which is called after the capture component window has been closed. Only valid when the -c/capture flag is set.

---
isSessionOpened(iso): boolean
    properties: query
    Returns true if a thumbnail/playblast capture session is currently running (already opened and still not cancelled/saved).

---
launchedFromOptionsBox(lfo): boolean
    properties: query
    Returns true if the thumbnail capture component was launched through the options dialog box, else false.

---
previewPath(pp): boolean
    properties: query
    Returns the generated preview path (the first frame of generated sequence resized to 100x100 px).

---
removeProjectThumbnail(rpt): string
    properties: create
    Remove all captured thumbnail/playblast from the given project file path.

---
save(s): string
    properties: create
    Save the generated image sequence for the given file to disk. The file path must be an absolute path.

---
startFrame(sf): int
    properties: create, query
    Set the start captured frame. Only valid when -c/capture flag is set.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/thumbnailCaptureComponent.html 
    """


def timeCode(flagmayaStartFrame: float, flagproductionStartFrame: float, flagproductionStartHour: float, flagproductionStartMinute: float, flagproductionStartSecond: float) -> time:
    """Synopsis:
---
---
 timeCode([mayaStartFrame=float], [productionStartFrame=float], [productionStartHour=float], [productionStartMinute=float], [productionStartSecond=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeCode is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds



set the production start time to 1 hour, 33 min, 52 seconds, and 23 frames
cmds.timeCode(productionStartHour=1,productionStartMinute=33,productionStartSecond=52,productionStartFrame=23)

query the production start time
---

cmds.timeCode(query=1,productionStartHour=True)
// result: 1
cmds.timeCode(query=1,productionStartMinute=True)
// result: 33

---
Return:
---


    time: values

Flags:
---


---
mayaStartFrame(msf): float
    properties: create, query, edit
    Sets the Maya start time of the time code, in frames.
In query mode, returns the Maya start frame of the time code.

---
productionStartFrame(psf): float
    properties: create, query, edit
    Sets the production start time of the time code, in terms of frames.
In query mode, returns the sub-second frame of production start time.

---
productionStartHour(psh): float
    properties: create, query, edit
    Sets the production start time of the time code, in terms of hours.
In query mode, returns the hour of production start time.

---
productionStartMinute(psm): float
    properties: create, query, edit
    Sets the production start time of the time code, in terms of minutes.
In query mode, returns the minute of production start time.

---
productionStartSecond(pss): float
    properties: create, query, edit
    Sets the production start time of the time code, in terms of seconds.
In query mode, returns the second of production start time.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeCode.html 
    """


def timeControl(flaganimCurveNames: boolean, flaganimLayerFilterOptions: string, flaganimLayerShowWeight: boolean, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagbeginScrub: boolean, flagcurrentFrameColor: tuple[float, float, float, float], flagdefineTemplate: string, flagdisplaySound: boolean, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagendScrub: boolean, flagexists: boolean, flagforceRedraw: boolean, flagforceRefresh: boolean, flagforegroundColor: tuple[float, float, float], flagfullPathName: boolean, flagglobalTime: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmainListConnection: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpressCommand: script, flagpreventOverride: boolean, flagrange: boolean, flagrangeArray: boolean, flagrangeVisible: boolean, flagreleaseCommand: script, flagrepeatChunkSize: float, flagrepeatOnHold: boolean, flagresample: boolean, flagshowKeys: string, flagshowKeysCombined: boolean, flagsnap: boolean, flagsound: string, flagstatusBarMessage: string, flagtickSize: int, flagtickSpan: int, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwaveform: string, flagwidth: int) -> string:
    """Synopsis:
---
---
 timeControl(
string
    , [animCurveNames=boolean], [animLayerFilterOptions=string], [animLayerShowWeight=boolean], [annotation=string], [backgroundColor=[float, float, float]], [beginScrub=boolean], [currentFrameColor=[float, float, float, float]], [defineTemplate=string], [displaySound=boolean], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [endScrub=boolean], [exists=boolean], [forceRedraw=boolean], [forceRefresh=boolean], [foregroundColor=[float, float, float]], [fullPathName=boolean], [globalTime=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [mainListConnection=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [pressCommand=script], [preventOverride=boolean], [range=boolean], [rangeArray=boolean], [rangeVisible=boolean], [releaseCommand=script], [repeatChunkSize=float], [repeatOnHold=boolean], [resample=boolean], [showKeys=string], [showKeysCombined=boolean], [snap=boolean], [sound=string], [statusBarMessage=string], [tickSize=int], [tickSpan=int], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [waveform=string], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeControl is undoable, queryable, and editable.Note



Example:
---
import maya.cmds as cmds

To display sound in the time slider, there must first be a sound
node in the scene. We'll create one and give it the name "ohNo".
Note that the argument to the -file flag must be a path to a valid
soundfile.
---

cmds.sound( file='C:/My Documents/maya/projects/default/sound/ohNo.aiff', name='ohNo' )


To display sound in the time slider, you must specify
the sound node to display and turn display of sound "on."
First we need to get the name of the playback slider from
the global mel variable called gPlayBackSlider
---

import maya.mel
aPlayBackSliderPython = maya.mel.eval('$tmpVar=$gPlayBackSlider')
cmds.timeControl( aPlayBackSliderPython, e=True, sound='ohNo', displaySound=True )

To hear sound while scrubbing in the time slider, set the press and
release commands to begin and end sound scrubbing.
---

cmds.timeControl( aPlayBackSliderPython,edit=True,pressCommand='cmds.timeControl(aPlayBackSliderPython,edit=True,beginScrub=True)')
cmds.timeControl( aPlayBackSliderPython,edit=True,releaseCommand='cmds.timeControl(aPlayBackSliderPython,edit=True,endScrub=True)')

---
Return:
---


    string: Name of created or edited control

Flags:
---


---
animCurveNames(acn): boolean
    properties: create, query
    When "showKeys" is not "none", querying this flag will
return the names of all the animCurves for which keyframe
ticks are being displayed.  Query returns string[].

---
animLayerFilterOptions(alf): string
    properties: create, query, edit
    Specifies whether a filter is to be applied when displaying animation layers.
If so, the options can be "allAffecting" (no filter), "active" (only the active
layers on the object will be displayed) and "animLayerEditor" (the settings will
be taken from the animation layer editor).

---
animLayerShowWeight(asw): boolean
    properties: create, query, edit
    Specifies or queries whether weights are to be shown when displaying animation layers.

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
currentFrameColor(cfc): [float, float, float, float]
    properties: edit
    This flag is used to specify the rgba color of the
current frame overlay rectangle in the timeControl.

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
forceRedraw(fd): boolean
    properties: create, edit
    Force a redraw of the time control UI. Similiar to forceRefresh but
does not rebuild key information.

---
forceRefresh(fr): boolean
    properties: create, edit
    Force a refresh of the time control UI.

---
foregroundColor(fgc): [float, float, float]
    properties: edit
    This flag is used to specify the rgb color of the
vertical lines and numeric text in the timeControl.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
globalTime(gt): boolean
    properties: create, query, edit
    "true" means this widget controls and displays the global,
dependency graph time.  "false" means time changes here
do NOT affect the dependency graph. Query returns int.

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
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
time slider will use as its source of content.  The time slider will
only display keys for items contained in the selectionConnection object.

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
    script to run on mouse-down in this control.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
range(rng): boolean
    properties: create, query
    Returns string representing the currently highlighted
range visible on the time slider.  A range from 10 to 20
would be returned as "10:20".  When there's no range
visible on the time slider, the query returns a range
spanning the current time: for example, "10:11".  These
values are in the current time unit.

---
rangeArray(ra): boolean
    properties: create, query
    Returns a float array representing the currently highlighted
range visible on the time slider.  A range from 10 to 20
would be returned as { 10.0, 20.0 }.  When there's no range
visible on the time slider, the query returns values spanning
the current time: { 10.0, 11.0 }.  These values are in the current time unit.

---
rangeVisible(rv): boolean
    properties: create, query
    Returns true if a currently highlighted range is visible
on the time slider, false if no.

---
releaseCommand(rc): script
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
showKeys(sk): string
    properties: create, query, edit
    "active" will show tick marks for keyframes on all active
objects.  "none" shows no tick marks.  Any other name is
taken as the name of a channel box whose selected attributes
will display tick marks.  Default "active".  Query returns string.

---
showKeysCombined(skc): boolean
    properties: create, query, edit
    This flag can be used in conjunction with the showKeys flag to
enable a combination of "active" + "channel box" behavior.
Specifically, if channel box attributes are selected, tick marks will
be shown for those attributes. If no channel box attributes are
selected, tick marks will be shown for keyframes on all active objects.

---
snap(sn): boolean
    properties: create, query, edit
    "true" means this widget is constrained to having
values that are integers representing the current time unit..
"false" means the current time indicator is "free floating"
and not constrained.

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
tickSize(ts): int
    properties: create, query, edit
    Specifies the width of keyframe ticks drawn in the time slider.
The value will be clamped to the range [1, 63].

---
tickSpan(tsp): int
    properties: create, query, edit
    Specifies the interval between keyframe ticks in the timeControl. For example,
a value of 10, will place ticks at 0, 10, 20, etc.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeControl.html 
    """


def timeEditor(flagallClips: string, flagclipId: int, flagcommonParentTrack: boolean, flagcomposition: string, flagdrivingClipsForAttr: string, flagdrivingClipsForObj: tuple[string, int], flagincludeParent: boolean, flagmute: boolean, flagselectedClips: string, flagtopLevelClips: string) -> string:
    """Synopsis:
---
---
 timeEditor([allClips=string], [clipId=int], [commonParentTrack=boolean], [composition=string], [drivingClipsForAttr=string], [drivingClipsForObj=[string, int]], [includeParent=boolean], [mute=boolean], [selectedClips=string], [topLevelClips=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditor is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.timeEditor(mute=True)

Get clip IDs of current selected group clips
cmds.timeEditor(selectedClips='group')

Get clip IDs of all selected clips
cmds.timeEditor(selectedClips='')

Get all top-level group clip IDs in the active composition
cmds.timeEditor(topLevelClips='group')

Recursively get all container clip IDs in the active composition
cmds.timeEditor(allClips='container')

Recursively get all clip IDs under the specified group clip (id=2)
cmds.timeEditor(allClips='', clipId=2)

Get all group clips directly under the specified group clip (id=21)
cmds.timeEditor(topLevelClips='group', clipId=21)

Find the common parent track of the given clip IDs
cmds.timeEditor(commonParentTrack=True, clipId=[1,2,3])

---
Return:
---


    string: Command result

Flags:
---


---
allClips(alc): string
    properties: create
    Return an exhaustive (recursive) list of all clip IDs from the active composition.
Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:

 roster 
 container 
 group

---
clipId(id): int
    properties: create, multiuse
    ID of the clip to be edited.

---
commonParentTrack(cpt): boolean
    properties: create
    Locate the common parent track node and track index of the given clip IDs.
Requires a list of clip IDs to be specified using the clipId flag.
The format of the returned string is "track_node:track_index". If the clips specified
are on the same track node but in different track indexes, only the track node
will be returned.

---
composition(cp): string
    properties: create
    A flag to use in conjunction with -dca/drivingClipsForObj to indicate the name of composition to use.
By default if this flag is not provided, current active composition will be used.

---
drivingClipsForAttr(dca): string
    properties: create
    Return a list of clips driving the specified attribute(s).
If the composition is not specified, current active composition will be used.

---
drivingClipsForObj(dco): [string, int]
    properties: create
    Return a list of clips driving the specified object(s) with an integer value indicating the matching mode.
If no object is specified explicitly, the selected object(s) will be used.
Objects that cannot be driven by clips are ignored.
If the composition is not specified, current active composition will be used.
Default match mode is 0.

0: Include only the clip that has an exact match
1: Include any clip that contains all of the specified objects
2: Include any clip that contains any of the specified objects
3: Include all clips that do not include any of the specified objects

---
includeParent(ip): boolean
    properties: create
    A toggle flag to use in conjunction with -dca/drivingClipsForObj.
When toggled, parent clip is included in selection (the entire hierarchy will be selected).

---
mute(m): boolean
    properties: create, query
    Mute/unmute Time Editor.

---
selectedClips(sc): string
    properties: create
    Return a list of clip IDs of currently selected Time Editor clips.
Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:

 roster 
 container 
 group

---
topLevelClips(tlc): string
    properties: create
    Return a list of all top-level clip IDs from the active composition.
Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:

 roster 
 container 
 group

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditor.html 
    """


def timeEditorAnimSource(flagaddObjects: string, flagaddRelatedKG: boolean, flagaddSelectedObjects: boolean, flagaddSource: string, flagapply: boolean, flagattribute: string, flagbakeToAnimSource: string, flagcalculateTiming: boolean, flagcopyAnimation: boolean, flagdrivenClips: boolean, flagexclusive: boolean, flagexport: string, flagimportAllFbxTakes: boolean, flagimportFbx: string, flagimportFbxTakes: string, flagimportMayaFile: string, flagimportOption: string, flagimportPopulateOption: string, flagimportedContainerNames: string, flagincludeRoot: boolean, flagisUnique: boolean, flagpopulateImportedAnimSources: string, flagposeClip: boolean, flagrecursively: boolean, flagremoveSceneAnimation: boolean, flagremoveSource: string, flagshowAnimSourceRemapping: boolean, flagtakeList: string, flagtakesToImport: string, flagtargetIndex: string, flagtargets: boolean, flagtype: string) -> string:
    """Synopsis:
---
---
 timeEditorAnimSource([addObjects=string], [addRelatedKG=boolean], [addSelectedObjects=boolean], [addSource=string], [apply=boolean], [attribute=string], [bakeToAnimSource=string], [calculateTiming=boolean], [copyAnimation=boolean], [drivenClips=boolean], [exclusive=boolean], [export=string], [importAllFbxTakes=boolean], [importFbx=string], [importFbxTakes=string], [importMayaFile=string], [importOption=string], [importPopulateOption=string], [importedContainerNames=string], [includeRoot=boolean], [isUnique=boolean], [populateImportedAnimSources=string], [poseClip=boolean], [recursively=boolean], [removeSceneAnimation=boolean], [removeSource=string], [showAnimSourceRemapping=boolean], [takeList=string], [takesToImport=string], [targetIndex=string], [targets=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorAnimSource is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds
def setKey(time, value):
    cmds.currentTime(time)
    cmds.setAttr('cube.tx', value)
    cmds.setKeyframe('cube.tx')

cmds.file(f=True, new=True)
cmds.polyCube(name='cube')
setKey( 1,  0)
setKey( 5, -5)
setKey(10,  5)

Add cube.translateX with its animation to the anim source and calculate and save timing afterwards
cmds.timeEditorAnimSource("AnimSourceNode", edit=1, addSource="cube.translateX", calculateTiming=1)

Add cube.translateX with a copy of its animation to the anim source
cmds.timeEditorAnimSource("AnimSourceNode", edit=1, addSource="cube.translateX", copyAnimation=1)

Remove cube.translateX from the anim source
cmds.timeEditorAnimSource("AnimSourceNode", edit=1, removeSource="cube.translateX")

---
Return:
---


    string: Command result

Flags:
---


---
addSource(asc): string
    properties: edit
    Add single new target attribute with its animation.

---
apply(ap): boolean
    properties: edit
    Connect anim source's animation directly to the target objects. If the Time Editor is not muted, connect to scene storage instead.

---
bakeToAnimSource(bas): string
    properties: edit
    Create a new anim source with the same animation as this anim source. All non-curve inputs will be baked down, whereas curve sources will be shared.

---
calculateTiming(ct): boolean
    properties: query, edit
    Adjust start/duration when adding/removing sources. If query it returns the [start,duration] pair.

---
copyAnimation(cp): boolean
    properties: edit
    Copy animation when adding source.

---
drivenClips(dc): boolean
    properties: query
    Return all clips driven by the given anim source.

---
export(ex): string
    properties: edit
    Export given anim source and the animation curves to a specified Maya file.

---
isUnique(iu): boolean
    properties: query
    Return true if the anim source node is only driving a single clip.

---
removeSource(rs): string
    properties: edit
    Remove single attribute.

---
targetIndex(ti): string
    properties: query
    Get target index.

---
targets(trg): boolean
    properties: query
    Get a list of all targets in this anim source.

---
addObjects(ao): string
    properties: create, query, edit
    Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon.
In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s).
Similar to -addSelectedObjects flag but acts on given object(s) instead.
This flag will override the flag -addSelectedObjects.

---
addRelatedKG(akg): boolean
    properties: create, query, edit
    During population, determine if associated keying groups should be populated
or not. Normally used for populating HIK. By default the value is false.

---
addSelectedObjects(aso): boolean
    properties: create, query, edit
    Populate the currently selected objects and their attributes to anim source or Time Editor.
In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.

---
attribute(at): string
    properties: create, edit, multiuse
    Populate a specific attribute on a object.

---
exclusive(exc): boolean
    properties: create, edit
    Populate all types of animation sources which are not listed by "type" Flag.

---
importAllFbxTakes(aft): boolean
    properties: create
    Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

---
importFbx(fbx): string
    properties: create
    Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).

---
importFbxTakes(ft): string
    properties: create
    Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

---
importMayaFile(mf): string
    properties: create
    Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

---
importOption(io): string
    properties: edit
    Option for importing animation source. Specify either 'connect' or 'generate'.
connect:  Only connect with nodes already existing in the scene.
                  Importing an animation source that does not match with any element
                  of the current scene will not create any clip.
                  (connect is the default mode).
generate: Import everything and generate new nodes for items not existing in the scene.

---
importPopulateOption(ipo): string
    properties: edit
    Option for population when importing.

---
importedContainerNames(icn): string
    properties: create
    Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.

---
includeRoot(irt): boolean
    properties: create, edit
    Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.

---
populateImportedAnimSources(pia): string
    properties: create
    Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).

---
poseClip(poc): boolean
    properties: create
    Populate as pose clip with current attribute values.

---
recursively(rec): boolean
    properties: create, edit
    Populate selection recursively, adding all the children.

---
removeSceneAnimation(rsa): boolean
    properties: create, edit
    If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.

---
showAnimSourceRemapping(sar): boolean
    properties: create
    Show a remapping dialog when the imported anim source attributes do not match the scene attributes.

---
takeList(tl): string
    properties: create
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.

---
takesToImport(toi): string
    properties: create
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.

---
type(typ): string
    properties: create, query, edit, multiuse
    Only populate the specified type of animation source.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorAnimSource.html 
    """


def timeEditorBakeClips(flagbakeToAnimSource: string, flagbakeToClip: string, flagclipId: int, flagcombineLayers: boolean, flagforceSampling: boolean, flagkeepOriginalClip: boolean, flagpath: string, flagsampleBy: time, flagtargetTrackIndex: int, flagtargetTracksNode: string) -> int:
    """Synopsis:
---
---
 timeEditorBakeClips(
objects
    , [bakeToAnimSource=string], [bakeToClip=string], [clipId=int], [combineLayers=boolean], [forceSampling=boolean], [keepOriginalClip=boolean], [path=string], [sampleBy=time], [targetTrackIndex=int], [targetTracksNode=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorBakeClips is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Bakes the currently selected clips to a new clip named "testClip"
cmds.timeEditorBakeClips(bakeToClip="testClip")

---
Return:
---


    int: Command result

Flags:
---


---
bakeToAnimSource(bas): string
    properties: create
    Bake/merge the selected clips into the animation source.

---
bakeToClip(btc): string
    properties: create
    Bake/merge the selected clips into a clip.

---
clipId(id): int
    properties: create, multiuse
    Clip IDs of the clips to bake.

---
combineLayers(cl): boolean
    properties: create
    Combine the layers of the input clip.

---
forceSampling(fs): boolean
    properties: create
    Force sampling on the whole time range when baking.

---
keepOriginalClip(koc): boolean
    properties: create
    Keep the source clips after baking.

---
path(pt): string
    properties: create, multiuse
    Full path of clips on which to operate. For example: composition1|track1|group; composition1|track1|group|track2|clip1.

---
sampleBy(sb): time
    properties: create
    Sampling interval when baking crossfades and timewarps.

---
targetTrackIndex(tti): int
    properties: create
    Specify the target track when baking containers.
If targetTrackIndex is specified, the track index within the specified node is used.
If targetTrackIndex is not specified or is the default value (-1), the track index within the current node is used.
If targetTrackIndex is -2, a new track will be created.

---
targetTracksNode(ttn): string
    properties: create
    Target tracks node when baking containers.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorBakeClips.html 
    """


def timeEditorClip(flagabsolute: boolean, flagaddAttribute: string, flagaddObjects: string, flagaddRelatedKG: boolean, flagaddSelectedObjects: boolean, flagallowShrinking: boolean, flaganimSource: string, flagattribute: string, flagaudio: string, flagblendMode: int, flagchildren: int, flagclipAfter: boolean, flagclipBefore: boolean, flagclipDataType: boolean, flagclipId: int, flagclipIdFromNodeName: int, flagclipIdFromPath: boolean, flagclipNode: boolean, flagclipPath: boolean, flagcopyClip: boolean, flagcrossfadeMode: int, flagcrossfadePlug: boolean, flagcurveTime: time, flagdefaultGhostRoot: boolean, flagdrivenAttributes: boolean, flagdrivenClipsBySource: string, flagdrivenObjects: boolean, flagdrivenRootObjects: boolean, flagdrivingSources: string, flagduplicateClip: boolean, flagduration: time, flagemptySource: boolean, flagendTime: time, flagexclusive: boolean, flagexistingOnly: boolean, flagexists: boolean, flagexplode: int, flagexportAllClips: boolean, flagexportFbx: string, flagextend: boolean, flagextendParent: boolean, flagghost: boolean, flagghostRootAdd: string, flagghostRootRemove: string, flaggroup: boolean, flagholdEnd: time, flagholdStart: time, flagimportAllFbxTakes: boolean, flagimportFbx: string, flagimportFbxTakes: string, flagimportMayaFile: string, flagimportOption: string, flagimportPopulateOption: string, flagimportTakeDestination: int, flagimportedContainerNames: string, flagincludeRoot: boolean, flagisContainer: boolean, flaglistUserGhostRoot: boolean, flagloopEnd: time, flagloopStart: time, flagminClipDuration: boolean, flagmodifyAnimSource: boolean, flagmoveClip: time, flagmute: boolean, flagname: string, flagparent: int, flagparentClipId: int, flagparentGroupId: boolean, flagpasteClip: time, flagpath: string, flagpopulateImportedAnimSources: string, flagposeClip: boolean, flagpreserveAnimationTiming: boolean, flagrazorClip: time, flagrecursively: boolean, flagremap: tuple[string, string], flagremapNamespace: tuple[string, string], flagremapSource: tuple[string, string], flagremappedSourceAttrs: boolean, flagremappedTargetAttrs: boolean, flagremoveAttribute: string, flagremoveClip: boolean, flagremoveCrossfade: boolean, flagremoveSceneAnimation: boolean, flagremoveWeightCurve: boolean, flagresetTiming: boolean, flagresetTransition: boolean, flagripple: boolean, flagrootClipId: int, flagrootPath: string, flagscaleEnd: time, flagscalePivot: time, flagscaleStart: time, flagsetKeyframe: string, flagshowAnimSourceRemapping: boolean, flagspeedRamping: int, flagstartTime: time, flagtakeList: string, flagtakesToImport: string, flagtimeWarp: boolean, flagtimeWarpCurve: boolean, flagtimeWarpType: int, flagtrack: string, flagtracksNode: boolean, flagtransition: boolean, flagtrimEnd: time, flagtrimStart: time, flagtruncated: boolean, flagtype: string, flaguniqueAnimSource: boolean, flaguserGhostRoot: boolean, flagweightCurve: boolean, flagzeroKeying: boolean) -> string:
    """Synopsis:
---
---
 timeEditorClip([absolute=boolean], [addAttribute=string], [addObjects=string], [addRelatedKG=boolean], [addSelectedObjects=boolean], [allowShrinking=boolean], [animSource=string], [attribute=string], [audio=string], [blendMode=int], [children=int], [clipAfter=boolean], [clipBefore=boolean], [clipDataType=boolean], [clipId=int], [clipIdFromNodeName=int], [clipIdFromPath=boolean], [clipNode=boolean], [clipPath=boolean], [copyClip=boolean], [crossfadeMode=int], [crossfadePlug=boolean], [curveTime=time], [defaultGhostRoot=boolean], [drivenAttributes=boolean], [drivenClipsBySource=string], [drivenObjects=boolean], [drivenRootObjects=boolean], [drivingSources=string], [duplicateClip=boolean], [duration=time], [emptySource=boolean], [endTime=time], [exclusive=boolean], [existingOnly=boolean], [exists=boolean], [explode=int], [exportAllClips=boolean], [exportFbx=string], [extend=boolean], [extendParent=boolean], [ghost=boolean], [ghostRootAdd=string], [ghostRootRemove=string], [group=boolean], [holdEnd=time], [holdStart=time], [importAllFbxTakes=boolean], [importFbx=string], [importFbxTakes=string], [importMayaFile=string], [importOption=string], [importPopulateOption=string], [importTakeDestination=int], [importedContainerNames=string], [includeRoot=boolean], [isContainer=boolean], [listUserGhostRoot=boolean], [loopEnd=time], [loopStart=time], [minClipDuration=boolean], [modifyAnimSource=boolean], [moveClip=time], [mute=boolean], [name=string], [parent=int], [parentClipId=int], [parentGroupId=boolean], [pasteClip=time], [path=string], [populateImportedAnimSources=string], [poseClip=boolean], [preserveAnimationTiming=boolean], [razorClip=time], [recursively=boolean], [remap=[string, string]], [remapNamespace=[string, string]], [remapSource=[string, string]], [remappedSourceAttrs=boolean], [remappedTargetAttrs=boolean], [removeAttribute=string], [removeClip=boolean], [removeCrossfade=boolean], [removeSceneAnimation=boolean], [removeWeightCurve=boolean], [resetTiming=boolean], [resetTransition=boolean], [ripple=boolean], [rootClipId=int], [rootPath=string], [scaleEnd=time], [scalePivot=time], [scaleStart=time], [setKeyframe=string], [showAnimSourceRemapping=boolean], [speedRamping=int], [startTime=time], [takeList=string], [takesToImport=string], [timeWarp=boolean], [timeWarpCurve=boolean], [timeWarpType=int], [track=string], [tracksNode=boolean], [transition=boolean], [trimEnd=time], [trimStart=time], [truncated=boolean], [type=string], [uniqueAnimSource=boolean], [userGhostRoot=boolean], [weightCurve=boolean], [zeroKeying=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorClip is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


Move clips 1 and 2
cmds.timeEditorClip(edit=True, moveClip=20, clipId=[1,2])

Create new container clip on track 4 of Container_A tracks
cmds.timeEditorClip("ClipNodeName", track="Container_A_Tracks:4")

Create new container clip on track path
cmds.timeEditorClip("ClipNodeName", track="composition1|track1")

Populate selected objects with attributes driven by specific types of animation sources
cmds.timeEditorClip("teClip1", addSelectedObjects=True, type=["animCurveTL","animCurveTA"], track="Composition1:1")

Populate selected objects and their associated keying groups (normally used for populating complete HIK rig)
cmds.timeEditorClip("teClip1", addSelectedObjects=True, addRelatedKG=True, track="Composition1:1")

Populate selected objects into a newly created container
cmds.timeEditorClip("ContainerName", track="Container_A_Tracks:0", addSelectedObjects=True)

Move a container(s) to a different track
The "New_Track:2" has the same format as when creating a new clip,
where "New_Track" is the TimeEditor "Tracks node" and "2" is the track index in that node.
A "Tracks" node maintains a list of tracks at a given level in the TimeEditor hierarchy
and is either a composition or a group clip.
cmds.timeEditorClip(edit=True, track="New_Track:2", clipId=[1,2,3])

Move a container(s) to a different track by clip path
cmds.timeEditorClip(edit=True, track="composition1|track1", path=["composition1|track2|clip1","composition1|track2|clip2","composition1|track2|clip3"])

Create a group from specified containers
cmds.timeEditorClip("GroupName", track="New_Track:1", group=True, clipId=[1,2,3])

Import animation from selected object into the TimeEditor.
cmds.timeEditorClip("container_A", aso=True, track="composition1|track1")

Return the Anim Source for a given clip ID 1
cmds.timeEditorClip(1, query=True, animSource=True)

Create a clip from an Anim Source starting at frame 30 into track2 of composition1
cmds.timeEditorClip("Container_B", track="composition1|track2", animSource="someAnimSourceName", startTime=30)

Return the start time of the clip with clip ID 1
cmds.timeEditorClip(1, query=True, startTime=True, absolute=True)

Return the duration of the clip with clip ID 1
cmds.timeEditorClip(1, query=True, duration=True, absolute=True)

Remap cube 1 translate X attribute to cube 1 translate Y attribute
cmds.timeEditorClip(edit=True, remapSource=["cube1.translateY", "cube1.translateX"], clipId=1)
cmds.timeEditorClip(edit=True, animSource="AnimSourceName", clipId=1)

Setup the crossfading mode between 2 clips to linear
cmds.timeEditorClip(edit=True, crossfadeMode=-1, clipId=[1,2])

Remove clips with clip ID 1 and 2.
cmds.timeEditorClip(edit=True, removeClip=True, clipId=[1,2])

---
Return:
---


    string: Return created clip's name.

Flags:
---


---
absolute(abs): boolean
    properties: query
    This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc.
to query (global) absolute time.

---
addAttribute(aa): string
    properties: edit, multiuse
    Add new attribute to the clip.

---
allowShrinking(eas): boolean
    properties: edit
    When extending clip, allow shrinking.

---
animSource(asr): string
    properties: create, query, edit
    Populate based on animation source.

---
audio(au): string
    properties: create
    Create a clip with audio inside.

---
blendMode(bm): int
    properties: query, edit
    Set the blending mode for the clips specified with the -clipId flags:

0 : normal          - absolute blend
1 : additive        - relative blend

---
children(chl): int
    properties: query
    Get children clip IDs.

---
clipAfter(ca): boolean
    properties: query
    Get the clip ID of the next clip.

---
clipBefore(cb): boolean
    properties: query
    Get the clip ID of the previous clip.

---
clipDataType(cdt): boolean
    properties: query
    Query the type of data being driven by the given clip ID.
Return values are:

0 : Animation       - Clip drives animation curves
1 : Audio           - Clip drives audio
3 : Group           - Clip is a group

---
clipId(id): int
    properties: create, edit, multiuse
    ID of the clip to be edited.

---
clipIdFromNodeName(idn): int
    properties: query
    Get clip ID from clip node name.

---
clipIdFromPath(idp): boolean
    properties: query
    Flag for querying the clip ID given the path. Clip path is a vertical-bar-delimited string to indicate
a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented.
For example: composition1|track1|clip1
Note: To specify the path, this flag must appear before -query flag.

---
clipNode(cln): boolean
    properties: query
    Flag for querying the name of the clip node.

---
clipPath(clp): boolean
    properties: query
    Flag for querying the path given the clip ID. Clip path is a vertical bar delimited string to indicate
a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented.
For example: composition1|track1|clip1.
Note: If the clip is not connected to any track, it will return empty string.

---
copyClip(ccl): boolean
    properties: edit
    Get the selected clip IDs and store them in a list that could be used for pasting.

---
crossfadeMode(cfm): int
    properties: query, edit
    Set the crossfading mode between two clips that lie on the same track, and that are specified with the -clipId flags:

0 : linear          - Two clips are blended with a constant ratio
1 : step            - Left clip keeps its value until the middle of the crossfading region and then right clip's value is used
2 : hold left       - Use only left clip's value
3 : hold right      - Use only right clip's value
4 : custom          - User defined crossfade curve
5 : custom (spline) - User defined crossfade curve with spline preset

---
crossfadePlug(cfp): boolean
    properties: query
    Get plug path for a custom crossfade curve between 2 clips.

---
curveTime(cvt): time
    properties: query
    Query the curve local time in relation to the given clip.

---
defaultGhostRoot(dgr): boolean
    properties: query, edit
    Edit or query default ghost root variable.
Determine whether to use the default ghost root (object driven by clip).

---
drivenAttributes(dat): boolean
    properties: query
    Return a list of attributes driven by a clip.

---
drivenClipsBySource(dcs): string
    properties: query
    Returns the clips driven by the given source. Can filter the return result by the specified type, like animCurve, expression, constraint, etc.
This flag must come before the -query flag.

---
drivenObjects(dos): boolean
    properties: query
    Return an array of strings consisting of the names of all objects driven by the current clip and its children clips.

---
drivenRootObjects(dro): boolean
    properties: query
    Return an array of strings consisting of the names of all root objects driven by this clip and its children clips.

---
drivingSources(dsc): string
    properties: query
    Return all sources driving the given clip. Can filter the return result by the specified type, like animCurve, expression, constraint, etc.
If used after the -query flag (without an argument), the command returns all sources driving the given clip.
To specify the type, this flag must appear before the -query flag.
                        In query mode, this flag can accept a value.

---
duplicateClip(dcl): boolean
    properties: edit
    Duplicate clip into two clips with the same timing info.

---
duration(d): time
    properties: create, query
    Relative duration of the new clip.

---
emptySource(ems): boolean
    properties: create
    Create a clip with an empty source.

---
endTime(et): time
    properties: query
    Query the relative end time of the clip.

---
existingOnly(exo): boolean
    properties: edit
    This flag can only be used in edit mode, in conjunction with the animSource flag. Retain the animSource flag functionality but
only bind attributes that are already part of the clip. It does not attempt to populate unbound
source attributes to their default destination.

---
exists(exs): boolean
    properties: query
    Return true if the specified clip exists.

---
explode(epl): int
    properties: edit
    Reparent all tracks and their clips within a group out to its parent track node and remove the group.

---
exportAllClips(eac): boolean
    properties: edit
    When used with the ef/exportFbx flag, export all clips.

---
exportFbx(ef): string
    properties: edit
    Export currently selected clips to FBX files.

---
extend(ex): boolean
    properties: edit
    Extend the clip to encompass all children.

---
extendParent(exp): boolean
    properties: edit
    Extend parent to fit this clip.

---
ghost(gh): boolean
    properties: query, edit
    Enable/disable ghosting for the specified clip.

---
ghostRootAdd(gra): string
    properties: edit, multiuse
    Add path to specified node as a custom ghost root.

---
ghostRootRemove(grr): string
    properties: edit, multiuse
    Remove path to specified node as a custom ghost root.

---
group(grp): boolean
    properties: create
    Specify if the new container should be created as a group, containing other specified clips.

---
holdEnd(he): time
    properties: query, edit
    Hold clip's end to time.

---
holdStart(hs): time
    properties: query, edit
    Hold clip's start to time.

---
importTakeDestination(itd): int
    properties: create
    Specify how to organize imported FBX takes:
0 - Import takes into a group (default)
1 - Import takes into multiple compositions
2 - Import takes as a sequence of clips

---
isContainer(ict): boolean
    properties: query
    Indicate if given clip ID is a container.

---
listUserGhostRoot(lug): boolean
    properties: query
    Get user defined ghost root object for indicated clips.

---
loopEnd(le): time
    properties: query, edit
    Loop clip's end to time.

---
loopStart(ls): time
    properties: query, edit
    Loop clip's start to time.

---
minClipDuration(mcd): boolean
    properties: query
    Returns the minimum allowed clip duration.

---
modifyAnimSource(mas): boolean
    properties: create, edit
    When populating, automatically modify Anim Source without asking the user.

---
moveClip(mcl): time
    properties: edit
    Move clip by adding delta to its start time.

---
mute(m): boolean
    properties: query, edit
    Mute/Unmute the clip given a clip ID. In query mode, return the muted state of the clip. Clips muted by soloing are not affected by this flag.

---
name(n): string
    properties: query, edit
    Name of the clip. A clip will never have an empty name.
If an empty string is provided, it will be replaced with "_".

---
parent(p): int
    properties: edit
    Specify group/object parent ID.

---
parentClipId(pid): int
    properties: create, query
    Specify the parent clip ID of a clip to be created.

---
parentGroupId(pgd): boolean
    properties: query
    Return the parent group ID of the given clip.

---
pasteClip(pcl): time
    properties: edit
    Paste clip to the given time and track. Destination track is required to be specified through the track flag in the format "tracksNode:trackIndex".
A trackIndex of -1 indicates that a new track will be created.

---
path(pt): string
    properties: edit, multiuse
    Full path of the clip to be edited. For example: composition1|track1|clip1.
                        In query mode, this flag can accept a value.

---
preserveAnimationTiming(pat): boolean
    properties: create
    When used with the population command, it ensures the animation is offset within a clip in such way that it matches its original scene timing, regardless of the new clip's position.

---
razorClip(rcl): time
    properties: edit
    Razor clip into two clips at the specified time.

---
remap(rmp): [string, string]
    properties: edit
    Change animation source for a given clip item to a new one, specified by the target path.
This removes all clips for the roster item and creates new clips from the Anim Source for the new target path.

---
remapNamespace(rns): [string, string]
    properties: create, multiuse
    Remap namespace(s). Can only be used in create mode, in conjunction with the
-importFbx/fbx, -importMayaFile/mf, or -attribute/at flags.
This flag will replace any occurrences of a given namespace to
an alternate specified namespace.  It takes in two string arguments. The
first argument specifies the namespace to replace. The second argument
specifies the replacement namespace. This flag cannot be used in conjunction
with the -sar/showAnimSourceRemapping flag.
Note that a track must be specified, and  must exist prior to invoking the
timeEditorClip command with the -remapNamespace flag.

---
remapSource(rs): [string, string]
    properties: edit
    Set animation source to be remapped for a given clip item to new one, specified by the target path.

---
remappedSourceAttrs(rms): boolean
    properties: query
    Return an array of attribute indices and names of the source attributes of a remapped clip.

---
remappedTargetAttrs(rmt): boolean
    properties: query
    Return an array of attribute indices and names of the target attributes of a remapped clip.

---
removeAttribute(ra): string
    properties: edit, multiuse
    Remove attribute from the clip.

---
removeClip(rmc): boolean
    properties: edit
    Remove clip of specified ID.

---
removeCrossfade(rcf): boolean
    properties: edit
    Remove custom crossfade between two clips specified by -clipId flags.

---
removeWeightCurve(rwc): boolean
    properties: create, query, edit
    Remove the weight curve connected to the clip.

---
resetTiming(rt): boolean
    properties: edit
    Reset start and duration of a clip with the given clip ID to the values stored in its Anim Source.

---
resetTransition(rtr): boolean
    properties: edit
    Reset transition intervals between specified clips.

---
ripple(rpl): boolean
    properties: edit
    Apply rippling to a clip operation.

---
rootClipId(rti): int
    properties: edit
    ID of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip.
For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.

---
rootPath(rpt): string
    properties: edit
    Path of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip.
For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.

---
scaleEnd(sce): time
    properties: edit
    Scale the end time of the clip to the given time.

---
scalePivot(scp): time
    properties: edit
    Scale the time of the clip based on the pivot. This should be used together with -scs/scaleStart or -sce/scaleEnd.

---
scaleStart(scs): time
    properties: edit
    Scale the start time of the clip to the given time.

---
setKeyframe(k): string
    properties: edit, multiuse
    Set keyframe on a specific clip for a specified attribute.

---
speedRamping(src): int
    properties: query, edit
    To control the playback speed of the clip by animation curve:

1 : create - Attach a speed curve and a time warp curve to the clip to control the playback speed
2 : edit - Open the Graph editor to edit the speed curve
3 : enable - Create a time warp curve from current speed curve and attach to clip
4 : disable - Remove the time warp curve from clip
5 : delete - Delete the attached speed curve and time warp curve
6 : reset - Reset the speed curve back to the default
7 : convert to speed curve from time warp
8 : convert to time warp from speed curve

In query mode, return true if a speed curve is attached to the clip.

---
startTime(s): time
    properties: create, query
    Relative start time of the new clip.

---
timeWarp(tw): boolean
    properties: query
    Return true if the clip is being warped by the speed curve. If no speed curve is attached to the clip, it will always return false.

---
timeWarpCurve(twc): boolean
    properties: query
    Returns the name of the time warp curve connected to the clip.

---
timeWarpType(twt): int
    properties: query, edit
    Time warp mode:

0: remapping - Connected time warp curve performs frame by frame remapping
1: speed curve - Connected time warp curve acts as a speed curve

In query mode, return time warp mode of a clip.

---
track(trk): string
    properties: create, query, edit
    The new clip container will be created on the track in the format "trackNode:trackNumber", or on a track path, for example "composition1|track1".
In query mode, return a string containing the track number and tracks node of the given clip ID.
In create mode, if the track number is '-1' or not given at all, then a new track will be created. For example: "trackNode:-1"; "composition1|".

---
tracksNode(trn): boolean
    properties: query
    Get tracks node if specified clip is a group clip.

---
transition(tra): boolean
    properties: edit
    Create transition intervals between specified clips.

---
trimEnd(tre): time
    properties: edit
    Trim the end time of the clip to the given time.

---
trimStart(trs): time
    properties: edit
    Trim the start time of the clip to the given time.

---
truncated(trc): boolean
    properties: query
    This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc.
to query (global) truncated time.

---
uniqueAnimSource(uas): boolean
    properties: edit
    If a given clip is sharing its Anim Source node with another clip, make the Anim Source of this clip unique.

---
userGhostRoot(ugr): boolean
    properties: query, edit
    Edit or query custom ghost root variable.
Determine whether to use user defined ghost root.

---
weightCurve(wc): boolean
    properties: create, query, edit
    In edit mode, create a weight curve and connect it to the clip.
In query mode, return the name of the weight curve connected to the clip.

---
zeroKeying(zk): boolean
    properties: edit
    A toggle flag to use in conjunction with k/setKeyframe, set the value of the key frame(s) to be keyed to zero.

---
addObjects(ao): string
    properties: create, query, edit
    Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon.
In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s).
Similar to -addSelectedObjects flag but acts on given object(s) instead.
This flag will override the flag -addSelectedObjects.

---
addRelatedKG(akg): boolean
    properties: create, query, edit
    During population, determine if associated keying groups should be populated
or not. Normally used for populating HIK. By default the value is false.

---
addSelectedObjects(aso): boolean
    properties: create, query, edit
    Populate the currently selected objects and their attributes to anim source or Time Editor.
In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.

---
attribute(at): string
    properties: create, edit, multiuse
    Populate a specific attribute on a object.

---
exclusive(exc): boolean
    properties: create, edit
    Populate all types of animation sources which are not listed by "type" Flag.

---
importAllFbxTakes(aft): boolean
    properties: create
    Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

---
importFbx(fbx): string
    properties: create
    Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).

---
importFbxTakes(ft): string
    properties: create
    Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

---
importMayaFile(mf): string
    properties: create
    Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).

---
importOption(io): string
    properties: edit
    Option for importing animation source. Specify either 'connect' or 'generate'.
connect:  Only connect with nodes already existing in the scene.
                  Importing an animation source that does not match with any element
                  of the current scene will not create any clip.
                  (connect is the default mode).
generate: Import everything and generate new nodes for items not existing in the scene.

---
importPopulateOption(ipo): string
    properties: edit
    Option for population when importing.

---
importedContainerNames(icn): string
    properties: create
    Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.

---
includeRoot(irt): boolean
    properties: create, edit
    Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.

---
populateImportedAnimSources(pia): string
    properties: create
    Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).

---
poseClip(poc): boolean
    properties: create
    Populate as pose clip with current attribute values.

---
recursively(rec): boolean
    properties: create, edit
    Populate selection recursively, adding all the children.

---
removeSceneAnimation(rsa): boolean
    properties: create, edit
    If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.

---
showAnimSourceRemapping(sar): boolean
    properties: create
    Show a remapping dialog when the imported anim source attributes do not match the scene attributes.

---
takeList(tl): string
    properties: create
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.

---
takesToImport(toi): string
    properties: create
    Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.

---
type(typ): string
    properties: create, query, edit, multiuse
    Only populate the specified type of animation source.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClip.html 
    """


def timeEditorClipLayer(flagaddAttribute: string, flagaddLayer: string, flagaddObject: string, flagallLayers: boolean, flagattribute: string, flagattributeKeyable: string, flagclipId: int, flagindex: int, flagkeySiblings: boolean, flaglayerId: int, flaglayerName: string, flagmode: int, flagmute: boolean, flagname: boolean, flagpath: string, flagremoveAttribute: string, flagremoveLayer: boolean, flagremoveObject: string, flagresetSolo: boolean, flagsetKeyframe: boolean, flagsolo: boolean, flagzeroKeying: boolean) -> string:
    """Synopsis:
---
---
 timeEditorClipLayer([addAttribute=string], [addLayer=string], [addObject=string], [allLayers=boolean], [attribute=string], [attributeKeyable=string], [clipId=int], [index=int], [keySiblings=boolean], [layerId=int], [layerName=string], [mode=int], [mute=boolean], [name=boolean], [path=string], [removeAttribute=string], [removeLayer=boolean], [removeObject=string], [resetSolo=boolean], [setKeyframe=boolean], [solo=boolean], [zeroKeying=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorClipLayer is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Add an additive clip layer  by clip ID
cmds.timeEditorClipLayer(e=True, clipId=1, addLayer="Layer A", mode=0)

Add an additive clip layer by clip path
cmds.timeEditorClipLayer(e=True, path='Composition1|track1|Group|track1|Clip1', addLayer="Layer A", mode=0)

Add an attribute to the given layer by clip ID and layer ID
cmds.timeEditorClipLayer(e=True, clipId=1, layerId=1, addAttribute="cube.tx")

Add an attribute to the given layer by layer path
cmds.timeEditorClipLayer(e=True, path='Composition1|track1|Clip1|Layer1', addAttribute="cube.tx")

Set key in the given layer
cmds.select("cube")
cmds.move(10, 0, 0, r=True)
cmds.timeEditorClipLayer(e=True, clipId=1, layerId=1, setKeyframe=True, attribute="cube.tx")

Remove layer attribute
cmds.timeEditorClipLayer(e=True, clipId=1, layerId=1, removeAttribute="cube.tx")

Query the layer name
cmds.timeEditorClipLayer(clipId=1, layerId=1, layerName=True, q=True)

Remove the specified layer by clip ID and layer ID
cmds.timeEditorClipLayer(e=True, clipId=1, removeLayer=True, layerId=1);

Remove the specified layer by layer path
cmds.timeEditorClipLayer(e=True, path='Composition1|track1|Clip1|Layer1', removeLayer=True);

---
Return:
---


    string: Command result

Flags:
---


---
addAttribute(aa): string
    properties: edit
    Add given plug to a layer with a supplied layerId.

---
addLayer(al): string
    properties: edit
    Add a new layer with a given name.

---
addObject(ao): string
    properties: edit
    Add given object with all its attributes in the clip to a layer with a supplied layerId.

---
allLayers(all): boolean
    properties: query
    Return all layers given clip ID.

---
attribute(a): string
    properties: edit, multiuse
    The attribute path to key.

---
attributeKeyable(ak): string
    properties: query
    Return whether specified attribute is keyable.

---
clipId(cid): int
    properties: edit
    ID of the clip this layer command operates on.
                        In query mode, this flag can accept a value.

---
index(idx): int
    properties: edit
    Layer index, used when adding new layer at specific location in the stack.

---
keySiblings(ks): boolean
    properties: edit
    If set to true, additional attributes might be keyed while keying to achieve desired result.

---
layerId(lid): int
    properties: edit
    Layer ID used in conjunction with other edit flags.
                        In query mode, this flag can accept a value.

---
layerName(ln): string
    properties: query, edit
    Edit layer name.
In query mode, return the layer name given its layer ID and clip ID.

---
mode(m): int
    properties: edit
    To control the playback speed of the clip by animation curve:

0 : additive
1 : additive override
2 : override
3 : override passthrough

---
mute(mu): boolean
    properties: edit
    Mute/unmute a layer given its layer ID and clip ID.

---
name(n): boolean
    properties: query
    Query the attribute name of a layer given its layer ID and clip ID.

---
path(pt): string
    properties: edit
    Full path of a layer or a clip on which to operate. For example: composition1|track1|clip1|layer1; composition1|track1|group|track1|clip1.
                        In query mode, this flag can accept a value.

---
removeAttribute(ra): string
    properties: edit
    Remove given plug from a layer with a supplied layerId.

---
removeLayer(rl): boolean
    properties: edit
    Remove layer with an ID.

---
removeObject(ro): string
    properties: edit
    Remove given object with all its attributes in the clip to a layer with a supplied layerId.

---
resetSolo(rs): boolean
    properties: edit
    Unsolo all soloed layers in a given clip ID.

---
setKeyframe(k): boolean
    properties: edit
    Set keyframe on specified attributes on specified layer of a clip.
Use -clipId to indicate the specified clip.
Use -layerId to indicate the specified layer of the clip.
Use -attribute to indicate the specified attributes (if no attribute flag is used, all attribute will be keyed).
Use -zeroKeying to indicate that zero offset from original animation should be keyed.

---
solo(sl): boolean
    properties: edit
    Solo/unsolo a layer given its layers ID and clip ID.

---
zeroKeying(zk): boolean
    properties: edit
    Indicate if the key to set should be zero offset from original animation.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClipLayer.html 
    """


def timeEditorClipOffset(flagapplyToAllRoots: boolean, flagclipId: int, flagmatchClipId: int, flagmatchDstTime: time, flagmatchObj: name, flagmatchOffsetRot: boolean, flagmatchOffsetTrans: boolean, flagmatchPath: string, flagmatchRotOp: int, flagmatchSrcTime: time, flagmatchTransOp: int, flagoffsetTransform: boolean, flagpath: string, flagresetMatch: int, flagresetMatchPath: string, flagrootObj: string, flagupVectorX: float, flagupVectorY: float, flagupVectorZ: float) -> None:
    """Synopsis:
---
---
 timeEditorClipOffset([applyToAllRoots=boolean], [clipId=int], [matchClipId=int], [matchDstTime=time], [matchObj=name], [matchOffsetRot=boolean], [matchOffsetTrans=boolean], [matchPath=string], [matchRotOp=int], [matchSrcTime=time], [matchTransOp=int], [offsetTransform=boolean], [path=string], [resetMatch=int], [resetMatchPath=string], [rootObj=string], [upVectorX=float], [upVectorY=float], [upVectorZ=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorClipOffset is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


Match position and rotation
---

cmds.timeEditorClipOffset( clipId=1, matchClipId=2, matchObj="cube", matchSrcTime=45, matchDstTime=45, matchTransOp=0, matchRotOp=1, applyToAllRoots=1 )

Match position and rotation by clip paths
---

cmds.timeEditorClipOffset( path='composition1|track1|clip1', matchPath='composition1|track1|clip2', matchObj="cube", matchSrcTime=45, matchDstTime=45, matchTransOp=0, matchRotOp=1, applyToAllRoots=1 )

---


Flags:
---


---
applyToAllRoots(atr): boolean
    properties: create
    Apply root offsets to all roots in the population. However, if the root objects are specified by rootObj flag, this flag will be ignored.

---
clipId(id): int
    properties: create, edit, multiuse
    ID of the clip to be edited.

---
matchClipId(mci): int
    properties: create
    Specify the ID of a clip to match.

---
matchDstTime(mdt): time
    properties: create
    Specify the time on target clip.

---
matchObj(mob): name
    properties: create
    Specify the object to match.

---
matchOffsetRot(mor): boolean
    properties: query
    Get the rotation of the match offset matrix.

---
matchOffsetTrans(mot): boolean
    properties: query
    Get the translation of the match offset matrix.

---
matchPath(mpt): string
    properties: create
    Full path of the clip to match. For example: composition1|track1|Group|track2|clip1

---
matchRotOp(mro): int
    properties: create
    Specify the option for matching rotation.

0 : full - All rotation components are matched
1 : Y    - Y component is matched
2 : none - No rotation matching

---
matchSrcTime(mst): time
    properties: create
    Specify the time on source clip.

---
matchTransOp(mto): int
    properties: create
    Specify the option for matching translation.

0 : full - All translation components are matched
1 : XZ   - X and Z components are matched
2 : none - No translation matching

---
offsetTransform(oft): boolean
    properties: create, query
    Create/get an offset for the specified clip.

---
path(pt): string
    properties: create, edit, multiuse
    Full path of a clip to be edited. For example: composition1|track1|group; composition1|track1|group|track2|clip1.
                        In query mode, this flag can accept a value.

---
resetMatch(rsm): int
    properties: create
    Specify clip ID to remove offset.

---
resetMatchPath(rmp): string
    properties: create
    Specify clip's full path to remove offset. For example: composition1|track1|Group|track2|clip1

---
rootObj(rob): string
    properties: create, query, edit, multiuse
    Specify the root objects. If specified, this flag will take precedence over applyToAllRoots flag.
When used in query mode, returns list of roots defined for the relocator.

---
upVectorX(upx): float
    properties: create
    Specify the X coordinate of the up vector.

---
upVectorY(upy): float
    properties: create
    Specify the Y coordinate of the up vector.

---
upVectorZ(upz): float
    properties: create
    Specify the Z coordinate of the up vector.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClipOffset.html 
    """


def timeEditorComposition(flagactive: boolean, flagallCompositions: boolean, flagcreateTrack: boolean, flagdelete: boolean, flagduplicateFrom: string, flagrename: tuple[string, string], flagtracksNode: boolean) -> string:
    """Synopsis:
---
---
 timeEditorComposition([active=boolean], [allCompositions=boolean], [createTrack=boolean], [delete=boolean], [duplicateFrom=string], [rename=[string, string]], [tracksNode=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorComposition is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


To create composition "Take1"
cmds.timeEditorComposition("Take1")

To query active composition (returns name of the tracks node for that composition)
cmds.timeEditorComposition(query=1, active=1)

To set active composition by specifying the associated tracks node
cmds.timeEditorComposition("TE_Tracks_Take2", edit=1, active=1)

---
Return:
---


    string: Return values currently not documented.

Flags:
---


---
active(act): boolean
    properties: query, edit
    Query or edit the active composition.

---
allCompositions(acp): boolean
    properties: query
    Return all compositions inside Time Editor.

---
createTrack(ct): boolean
    properties: create
    Create a default track when creating a new composition.

---
delete(delete): boolean
    properties: query, edit
    Delete the composition.

---
duplicateFrom(df): string
    properties: create
    Duplicate the composition.

---
rename(ren): [string, string]
    properties: edit
    Rename the composition of the first name to the second name.

---
tracksNode(tn): boolean
    properties: query
    Query the tracks node of a composition.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorComposition.html 
    """


def timeEditorPanel(flagactiveClipEditMode: int, flagactiveTabRootClipId: boolean, flagactiveTabTime: boolean, flagactiveTabView: int, flagautoFit: string, flagautoFitTime: string, flagcontrol: boolean, flagdefineTemplate: string, flagdisplayActiveKeyTangents: string, flagdisplayActiveKeys: string, flagdisplayInfinities: string, flagdisplayKeys: string, flagdisplayTangents: string, flagdisplayValues: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaggroupIdForTabView: int, flaghighlightConnection: string, flagkeyingTarget: int, flaglayerId: int, flaglockMainConnection: boolean, flaglookAt: string, flagmainListConnection: string, flagmenu: script, flagminClipWidth: int, flagpanel: string, flagparent: string, flagselectionConnection: string, flagsetToPrevClipEditMode: boolean, flagsnapTime: string, flagsnapToClip: boolean, flagsnapToFrame: boolean, flagsnapTolerance: int, flagsnapValue: string, flagstateString: boolean, flagtabView: int, flagtimeCursor: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 timeEditorPanel(
editorName
    , [activeClipEditMode=int], [activeTabRootClipId=boolean], [activeTabTime=boolean], [activeTabView=int], [autoFit=string], [autoFitTime=string], [control=boolean], [defineTemplate=string], [displayActiveKeyTangents=string], [displayActiveKeys=string], [displayInfinities=string], [displayKeys=string], [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [groupIdForTabView=int], [highlightConnection=string], [keyingTarget=int], [layerId=int], [lockMainConnection=boolean], [lookAt=string], [mainListConnection=string], [menu=script], [minClipWidth=int], [panel=string], [parent=string], [selectionConnection=string], [setToPrevClipEditMode=boolean], [snapTime=string], [snapToClip=boolean], [snapToFrame=boolean], [snapTolerance=int], [snapValue=string], [stateString=boolean], [tabView=int], [timeCursor=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorPanel is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Check to see if the "default" time editor has been created
---

cmds.timeEditorPanel( 'timeEditorPanel1TimeEd', exists=True )

Open the group(id=1) in local time tab
---

cmds.timeEditorPanel( 'timeEditorPanel1TimeEd', e=True, tabView=1 );

Query the current active tab view
---

cmds.timeEditorPanel( 'timeEditorPanel1TimeEd', q=True, activeTabView=True ) ;

Query the corresponding group given the tab view index
---

cmds.timeEditorPanel( 'timeEditorPanel1TimeEd', q=True, activeTabTime=True ) ;

Query the corresponding group given the tab view index
---

cmds.timeEditorPanel( 'timeEditorPanel1TimeEd', groupIdForTabView=1, q=True );

---
Return:
---


    string: Command result

Flags:
---


---
activeClipEditMode(ace): int
    properties: query, edit
    Set the appropriate clip edit mode for the editor.

0: Default Mode
1: Trim Mode
2: Scale Mode
3: Loop Mode
4: Hold Mode

---
activeTabRootClipId(atr): boolean
    properties: query
    Get the clip id for which current active tab has been opened. In case of main tab, this will return -1
meaning there is no root clip.

---
activeTabTime(att): boolean
    properties: query
    Get current time displayed inside the active tab. This will be global time in case of the main tab and
local time for others.

---
activeTabView(atv): int
    properties: query, edit
    Get/set the index of the tab widget's (active) visible tab. Note: the index is zero-based.

---
autoFit(af): string
    properties: query, edit
    on | off | tgl
Auto fit-to-view.

---
autoFitTime(aft): string
    properties: query, edit
    on | off | tgl
Auto fit-to-view along the time axis, as well.

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
displayActiveKeyTangents(dat): string
    properties: edit
    on | off | tgl
Display active key tangents in the editor.

---
displayActiveKeys(dak): string
    properties: edit
    on | off | tgl
Display active keys in the editor.

---
displayInfinities(di): string
    properties: edit
    on | off | tgl
Display infinities in the editor.

---
displayKeys(dk): string
    properties: edit
    on | off | tgl
Display keyframes in the editor.

---
displayTangents(dtn): string
    properties: edit
    on | off | tgl
Display tangents in the editor.

---
displayValues(dv): string
    properties: edit
    on | off | tgl
Display active keys and tangents values in the editor.

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
groupIdForTabView(gtv): int
    properties: query
    Get the group clip id for the given tab view index.
To specify the tab index, this flag must appear before the -query flag.
      In query mode, this flag needs a value.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
keyingTarget(kt): int
    properties: query, edit
    Set keying target to specified clip ID.
If keying into layer, '-layer' flag must be used.
In query mode, the clip id is omitted, and the name of the keying target will be returned.

---
layerId(l): int
    properties: edit
    Indicate layer ID of keying target.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
lookAt(la): string
    properties: edit
    all | selected | currentTime
FitView helpers.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
menu(m): script
    properties: create
    Specify a script to be run when the editor
is created.  The function will be passed one string
argument which is the new editor's name.

---
minClipWidth(mcw): int
    properties: query, edit
    Set the minimum clip width.

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
setToPrevClipEditMode(spe): boolean
    properties: edit
    Revert to previous clip edit mode.

---
snapTime(st): string
    properties: query, edit
    none | integer | keyframe
Keyframe move snap in time.

---
snapToClip(stc): boolean
    properties: query, edit
    Enable/Disable snap-to-clip option in Time Editor while manipulating and drag-and-drop clips.
When snapToClip is on all manipulated timing will land on a clip boundary if it is close to it.

---
snapToFrame(stf): boolean
    properties: query, edit
    Enable/Disable snap-to-frame option in Time Editor while manipulating and drag-and-drop clips.
When snapToFrame is on all manipulated timing will land on an exact frame.

---
snapTolerance(sto): int
    properties: query, edit
    Set the tolerance value for snapping.

---
snapValue(sv): string
    properties: query, edit
    none | integer | keyframe
Keyframe move snap in values.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
tabView(tv): int
    properties: edit
    Create a tab view for the given group clip ID.

---
timeCursor(tc): boolean
    properties: query, edit
    Activate the time cursor in Time Editor for scrubbing.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorPanel.html 
    """


def timeEditorTracks(flagactiveClipWeight: time, flagactiveClipWeightId: time, flagaddTrack: int, flagallClips: boolean, flagallTracks: boolean, flagallTracksRecursive: boolean, flagcomposition: boolean, flagpath: string, flagplugIndex: int, flagremoveTrack: int, flagremoveTrackByPath: string, flagreorderTrack: tuple[int, int], flagresetMute: boolean, flagresetSolo: boolean, flagselectedTracks: boolean, flagtrackGhost: boolean, flagtrackIndex: int, flagtrackMuted: boolean, flagtrackName: string, flagtrackSolo: boolean, flagtrackType: int) -> Int:
    """Synopsis:
---
---
 timeEditorTracks([activeClipWeight=time], [activeClipWeightId=time], [addTrack=int], [allClips=boolean], [allTracks=boolean], [allTracksRecursive=boolean], [composition=boolean], [path=string], [plugIndex=int], [removeTrack=int], [removeTrackByPath=string], [reorderTrack=[int, int]], [resetMute=boolean], [resetSolo=boolean], [selectedTracks=boolean], [trackGhost=boolean], [trackIndex=int], [trackMuted=boolean], [trackName=string], [trackSolo=boolean], [trackType=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeEditorTracks is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

 Insert a track at the end
---

cmds.timeEditorTracks( 'container1_tracks', e=1, addTrack=-1 )

 Insert a track at the end by path, inside a composition
---

cmds.timeEditorTracks( path='composition1', e=1, addTrack=-1 )

 Insert a track at the end by path, inside a group clip
---

cmds.timeEditorTracks( path='composition1|track1|groupClip', e=1, addTrack=-1 )

Remove the track from "container1_tracks"
---

cmds.timeEditorTracks( 'container1_tracks', e=1, removeTrack=1 )

Remove the track by paths
---

cmds.timeEditorTracks( e=1, removeTrackByPath=['composition1|track2', 'composition1|track1|group|track3'] )

Move track 0 forward 1 siblings
---

cmds.timeEditorTracks( 'container1_tracks', e=1, reorderTrack=(0, 1) )

Set the track name
---

cmds.timeEditorTracks( 'container1_tracks', e=1, trackName="Test", trackIndex=0 )

Set the track name by path
---

cmds.timeEditorTracks( e=1, trackName="Test", path='composition1|track2' )

Mute the track
---

cmds.timeEditorTracks( 'container1_tracks', e=1, trackMuted=True, trackIndex=0 )

---
Return:
---


    Int: In edit mode, return the newly created Track index.

Flags:
---


---
activeClipWeight(acw): time
    properties: query
    Get the clip weight at the specified time.

---
activeClipWeightId(aci): time
    properties: query
    Get the clip ID carrying the active clip weight at the specified time.

---
addTrack(at): int
    properties: edit
    Add new track at the track index specified. Indices are 0-based.
Specify -1 to add the track at the end.

---
allClips(ac): boolean
    properties: query
    Return a list of clip IDs under the specified track.

---
allTracks(atc): boolean
    properties: query
    Return a list of strings for all the immediate tracks for the given tracks node in the format "tracksNode:trackIndex".

---
allTracksRecursive(atr): boolean
    properties: query
    Return a list of strings for all the tracks for the given tracks node, or
return a list of strings for all tracks of all tracks nodes in the format "tracksNode:trackIndex".
If the given root tracks node is from a composition, this command returns the tracks under that composition, including the tracks within groups that is under the same composition.

---
composition(cp): boolean
    properties: query
    Return the composition the specified track belongs to.

---
path(pt): string
    properties: edit
    Full path of a track node or a track on which to operate. For example: composition1|track1|group; composition1|track1.
                        In query mode, this flag can accept a value.

---
plugIndex(pi): int
    properties: query, edit
    Get the plug index of the specified track.

---
removeTrack(rt): int
    properties: edit, multiuse
    Remove track at given index. It is a multi-use flag.

---
removeTrackByPath(rtp): string
    properties: edit, multiuse
    Remove track at given path. It is a multi-use flag. For example: composition1|track1|group|track1;

---
reorderTrack(rot): [int, int]
    properties: edit
    Move the track relative to other tracks. The first argument is the track index (0-based). The second argument can be a positive or negative number
to indicate the steps to move. Positive numbers move forward and negative numbers move backward.

---
resetMute(rm): boolean
    properties: create
    Reset all the muted tracks in the active composition.

---
resetSolo(rs): boolean
    properties: create
    Reset the soloing of all tracks on the active composition.

---
selectedTracks(st): boolean
    properties: query
    Return a list of the indices for all the selected tracks for the given tracks node, or
return a list of strings for all selected tracks of all tracks nodes in the format "tracksNode:trackIndex".

---
trackGhost(tgh): boolean
    properties: query, edit
    Ghost all clips under track.

---
trackIndex(ti): int
    properties: query, edit
    Specify the track index. This flag is used in conjunction with the other flags.
                        In query mode, this flag can accept a value.

---
trackMuted(tm): boolean
    properties: query, edit
    Return whether the track is muted.

---
trackName(tn): string
    properties: query, edit
    Display name of the track.

---
trackSolo(ts): boolean
    properties: query, edit
    Return whether the track is soloed.

---
trackType(tt): int
    properties: query, edit
    Specify the track type. Can only be used together with -at/addTrack. Does not work by itself.
In query mode, return the integer corresponding to the track type.

 0: Animation Track (Default)
 1: Audio Track

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeEditorTracks.html 
    """


def timeField(flagannotation: string, flagautoUnitWidth: int, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagenterCommand: script, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagreceiveFocusCommand: script, flagstatusBarMessage: string, flagstep: time, flaguseTemplate: string, flagvalue: time, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 timeField(
[string]
    , [annotation=string], [autoUnitWidth=int], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [receiveFocusCommand=script], [statusBarMessage=string], [step=time], [useTemplate=string], [value=time], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeField is undoable, queryable, and editable.-s/step



Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
cmds.timeField()
cmds.timeField( editable=False )
cmds.timeField( value=0 )
cmds.timeField( precision=2 )
cmds.timeField( precision=4, step=.01 )
cmds.timeField( autoUnitWidth=6, value=123 )
cmds.showWindow( window )

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
autoUnitWidth(auw): int
    properties: create, query, edit
    When this is non-zero the widget will automatically scale
based on the unit time settings (frame or timecode). The value
of autoUnitWidth specifies the number of digits that should be
able to be displayed as the frame number. So a value of 4 will
make sure frame number 8723 can be displayed.
When the value is zero the normal widget width will be used.

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
    Command executed when the field changes.  This command is
not invoked when the value changes via the -v/value flag.

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
dragCommand(dc): script
    properties: create, edit
    Command executed when dragging in the field.

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
    The edit state of the field.  By default, this flag is set
to true and the field value may be changed by typing into it.  If
false then the field cannot be changed interactively.  However,
the field text can be changed using the -v/value flag
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
    Command executed when the keypad 'Enter' key is pressed.

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
precision(pre): int
    properties: create, query, edit
    Number of digits to the right of the decimal place.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
receiveFocusCommand(rfc): script
    properties: create, edit
    Command executed when the field receives focus.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): time
    properties: create, query, edit
    Increment for the invisible slider.   The field value
will change by this amount when the invisible slider is dragged.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): time
    properties: create, query, edit
    Value of the field.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeField.html 
    """


def timeFieldGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenable1: boolean, flagenable2: boolean, flagenable3: boolean, flagenable4: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagextraLabel: string, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfFields: int, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flagstep: time, flaguseTemplate: string, flagvalue: tuple[time, time, time, time], flagvalue1: time, flagvalue2: time, flagvalue3: time, flagvalue4: time, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 timeFieldGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean], [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfFields=int], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [step=time], [useTemplate=string], [value=[time, time, time, time]], [value1=time], [value2=time], [value3=time], [value4=time], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeFieldGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label text and
editable time fields.  The label text is optional and one to four
time fields can be created.




Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
cmds.timeFieldGrp( numberOfFields=3, label='Scale', extraLabel='cm', value1=0.3, value2=0.5, value3=0.1 )
cmds.showWindow( window )

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
adjustableColumn(adj): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with the
sizing of the layout.  The column value is a 1-based index.
Passing 0 as argument turns off the previous adjustable column.

---
adjustableColumn2(ad2): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
two columns.

---
adjustableColumn3(ad3): int
    properties: create, edit
    Specifies that the column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
three columns.

---
adjustableColumn4(ad4): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
four columns.

---
adjustableColumn5(ad5): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
five columns.

---
adjustableColumn6(ad6): int
    properties: create, edit
    Specifies which column has an adjustable size that changes with
the size of the parent layout. Ignored if there are not exactly
six columns.

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
    Command string executed when the value of any of the
fields changes.

---
columnAlign(cal): [int, string]
    properties: create, edit, multiuse
    Arguments are : column number, alignment type.
Possible alignments are: left | right | center.
Specifies alignment type for the specified column.

---
columnAlign2(cl2): [string, string]
    properties: create, edit
    Sets the text alignment of both columns.  Ignored if there are not
exactly two columns. Valid values are "left", "right", and "center".

---
columnAlign3(cl3): [string, string, string]
    properties: create, edit
    Sets the text alignment for all three columns.  Ignored if there are not
exactly three columns. Valid values are "left", "right", and "center".

---
columnAlign4(cl4): [string, string, string, string]
    properties: create, edit
    Sets the text alignment for all four columns.  Ignored if there are not
exactly four columns. Valid values are "left", "right", and "center".

---
columnAlign5(cl5): [string, string, string, string, string]
    properties: create, edit
    Sets the text alignment for all five columns.  Ignored if there are not
exactly five columns. Valid values are "left", "right", and "center".

---
columnAlign6(cl6): [string, string, string, string, string, string]
    properties: create, edit
    Sets the text alignment for all six columns.  Ignored if there are not
exactly six columns. Valid values are "left", "right", and "center".

---
columnAttach(cat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column number, attachment type, and offset.
Possible attachments are: left | right | both.
Specifies column attachment types and offets.

---
columnAttach2(ct2): [string, string]
    properties: create, edit
    Sets the attachment type of both columns. Ignored if there are not
exactly two columns. Valid values are "left", "right", and "both".

---
columnAttach3(ct3): [string, string, string]
    properties: create, edit
    Sets the attachment type for all three columns. Ignored if there are not
exactly three columns. Valid values are "left", "right", and "both".

---
columnAttach4(ct4): [string, string, string, string]
    properties: create, edit
    Sets the attachment type for all four columns. Ignored if there are not
exactly four columns. Valid values are "left", "right", and "both".

---
columnAttach5(ct5): [string, string, string, string, string]
    properties: create, edit
    Sets the attachment type for all five columns. Ignored if there are not
exactly five columns. Valid values are "left", "right", and "both".

---
columnAttach6(ct6): [string, string, string, string, string, string]
    properties: create, edit
    Sets the attachment type for all six columns. Ignored if there are not
exactly six columns. Valid values are "left", "right", and "both".

---
columnOffset2(co2): [int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach2 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the two columns.  The offsets applied are based on the attachments
specified with the -columnAttach2 flag.  Ignored if there are not exactly
two columns.

---
columnOffset3(co3): [int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach3 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the three columns.  The offsets applied are based on the attachments
specified with the -columnAttach3 flag.  Ignored if there are not exactly
three columns.

---
columnOffset4(co4): [int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach4 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the four columns.  The offsets applied are based on the attachments
specified with the -columnAttach4 flag.  Ignored if there are not exactly
four columns.

---
columnOffset5(co5): [int, int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach5 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the five columns.  The offsets applied are based on the attachments
specified with the -columnAttach5 flag.  Ignored if there are not exactly
five columns.

---
columnOffset6(co6): [int, int, int, int, int, int]
    properties: create, edit
    This flag is used in conjunction with the -columnAttach6 flag.  If that
flag is not used then this flag will be ignored.  It sets the offset for
the six columns.  The offsets applied are based on the attachments
specified with the -columnAttach6 flag.  Ignored if there are not exactly
six columns.

---
columnWidth(cw): [int, int]
    properties: create, edit, multiuse
    Arguments are : column number, column width.
Sets the width of the specified column where the first parameter specifies
the column (1 based index) and the second parameter specifies the width.

---
columnWidth1(cw1): int
    properties: create, edit
    Sets the width of the first column. Ignored if there is not
exactly one column.

---
columnWidth2(cw2): [int, int]
    properties: create, edit
    Sets the column widths of both columns. Ignored if there are not
exactly two columns.

---
columnWidth3(cw3): [int, int, int]
    properties: create, edit
    Sets the column widths for all 3 columns. Ignored if there are not
exactly 3 columns.

---
columnWidth4(cw4): [int, int, int, int]
    properties: create, edit
    Sets the column widths for all 4 columns. Ignored if there are not
exactly 4 columns.

---
columnWidth5(cw5): [int, int, int, int, int]
    properties: create, edit
    Sets the column widths for all 5 columns. Ignored if there are not
exactly 5 columns.

---
columnWidth6(cw6): [int, int, int, int, int, int]
    properties: create, edit
    Sets the column widths for all 6 columns. Ignored if there are not
exactly 6 columns.

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
dragCommand(dc): script
    properties: create, edit
    Command string executed when dragging the invisible slider
in any of the fields.

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
enable4(en4): boolean
    properties: create, query, edit
    Enable state for the respective field.

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
extraLabel(el): string
    properties: create, query, edit
    If present on creation this specifies that there will be
an extra label in the group.  Sets the string to be label text to
the right of fields.

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
label(l): string
    properties: create, query, edit
    If present on creation this specifies that there will be
a label to the left of the fields.  Sets the string to be the label
text.

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
numberOfFields(nf): int
    properties: create
    Set the number of fields on creation. One to four fields are
available.  The default is one field.

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
precision(pre): int
    properties: create, edit
    Set the number of digits to the right of the decimal.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
rowAttach(rat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column, attachment type, offset.
Possible attachments are: top | bottom | both.
Specifies attachment types and offsets for the entire row.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): time
    properties: create, query, edit
    Set the delta of invisioSlider delta , the invisioSlider
step is delta/10.0 in LMB , delta in MMB,delta*10.0 in RMB.
Default is 10.0

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): [time, time, time, time]
    properties: create, query, edit
    Values for all fields.

---
value4(v4): time
    properties: create, query, edit
    Value for the respective field.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeFieldGrp.html 
    """


def timePort(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagglobalTime: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagsnap: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 timePort(
name
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [globalTime=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [snap=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timePort is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a window that has a timePort in it
---

cmds.window( w=500, h=35 )
cmds.columnLayout()
cmds.timePort( 'myTimePort', w=500, h=35)
cmds.showWindow()

Turn snapping off on the above timePort
---

cmds.timePort( 'myTimePort', e=True, snap=False )

---
Return:
---


    string: Widget name

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
globalTime(gt): boolean
    properties: create, query, edit
    "true" means this widget controls and displays the global,
dependency graph time.  "false" means time changes here
do NOT affect the dependency graph. Query returns int.

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
snap(sn): boolean
    properties: create, query, edit
    "true" means this widget is constrained to having
values that are integers representing the current time unit..
"false" means the current time indicator is "free floating"
and not constrained.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timePort.html 
    """


def timeWarp(flagdeleteFrame: int, flagframe: float, flagg: boolean, flaginterpType: tuple[int, string], flagmoveFrame: tuple[int, float]) -> string:
    """Synopsis:
---
---
 timeWarp([deleteFrame=int], [frame=float], [g=boolean], [interpType=[int, string]], [moveFrame=[int, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timeWarp is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a time warp on the animation curves driving a cylinder and a sphere,
and specify the warping is to occur at frames 1 and 20.
Note: Time warps are only applied to animated objects.
---

warp = cmds.timeWarp( 'pCylinder1', 'pSphere1',f=[1,20])

Move the first warp to frame 5
---

cmds.timeWarp(warp,e=1,mf=(0,5))

Move the 2nd warp to frame 10
---

cmds.timeWarp(warp,e=1,mf=(1,10))

Modify the interpolation between the 1st and 2nd warp to easeIn
---

cmds.timeWarp(warp,e=1,it=(0,'easeIn'))

query the original frames
---

cmds.timeWarp(warp,q=1,f=1)
Result: [1.0, 20.0, 30.0] ---


query the modified frames
---

cmds.timeWarp(warp,q=1,mf=1)
Result: [5.0, 10.0, 30.0] ---


query the interpolation
---

cmds.timeWarp(warp,q=1,it=1)
Result: [u'easeIn', u'linear'] ---


---
Return:
---


    string: timeWarp name

Flags:
---


---
deleteFrame(df): int
    properties: edit
    The flag value indicates the 0-based index of the warp frame to delete. This flag can only be used in edit mode.

---
frame(f): float
    properties: create, query, edit, multiuse
    In create and edit mode, this flag can be used to specify warp frames added to the warp operation.
In query mode, this flag returns a list of the frame values where warping occurs. The moveFrame flag command can be used to query the associated warped values.

---
g(g): boolean
    properties: create, query, edit
    In create mode, creates a global time warp node which impacts every animated object in the scene. In query mode, returns the global time warp node. Note: only one global time warp can exist in the scene.

---
interpType(it): [int, string]
    properties: create, query, edit
    This flag can be used to set the interpolation type for a given span. Valid interpolation types are linear, easeIn and easeOut. When queried, it returns a string array of the interpolation types for the specified time warp.

---
moveFrame(mf): [int, float]
    properties: query, edit
    This flag can be used to move a singular warp frame. The first value specified indicates the 0-based index of the warp frame to move. The second value indicates the new warp frame value. This flag can only be used in edit and query mode. When queried, it returns an array of the warped frame values.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timeWarp.html 
    """


def timer(flagendTimer: boolean, flaglapTime: boolean, flagname: string, flagstartTimer: boolean) -> None:
    """Synopsis:
---
---
 timer([endTimer=boolean], [lapTime=boolean], [name=string], [startTimer=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timer is NOT undoable, NOT queryable, and NOT editable.
Allow simple timing of scripts and commands. The resolution of this timer
is at the level of your OS's gettimeofday() function.


Note:This command does not handle stacked calls. For
example, this code below will give an incorrect answer on the
second timer -e call.
timer -s;
timer -s;
timer -e;
timer -e;

To do this use named timers:
timer -s;
timer -s -name "innerTimer";
timer -e -name "innerTimer";
timer -e;


I the -e flag or -lap flag return the time elapsed since
the last 'timer -s' call.
I the -s flag has no return value.




Example:
---
import maya.cmds as cmds


cmds.timer( s=True )
code being timed
print "START: time this"
for i in range (0, 50):
        print ("time this "+str(i))
print "END: time this"
cmds.timer( e=True )

Named timers can be used for nesting
cmds.timer( s=True, name="outerLoop" )
print "START: macro loop timing"
for i in range(0,50):
        cmds.timer( s=True )
        for j in range(5,50):
                newObjs = cmds.sphere( spans=j )
                cmds.delete( newObjs )
        innerTime = cmds.timer( e=True )
        lapTime = cmds.timer( lap=True, name="outerLoop" )
        print "\tInner loop %d = %g" % (i, innerTime)
        print "\t       SUB = %g" % lapTime
fullTime = cmds.timer( e=True, name="outerLoop" )
print "END: Full timing was %g" % fullTime

---


Flags:
---


---
endTimer(e): boolean
    properties: create
    Stop the timer and return the time elapsed since the timer was
started (in seconds). Once a timer is turned off it no longer exists,
though it can be recreated with a new start

---
lapTime(lap): boolean
    properties: create
    Get the lap time of the timer (time elapsed since start in seconds).
Unlike the end flag this keeps the timer running.

---
name(n): string
    properties: create
    Use a named timer for the operation. If this is omitted then the default
timer is assumed.

---
startTimer(s): boolean
    properties: create
    Start the timer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timer.html 
    """


def timerX(flagstartTime: float) -> float:
    """Synopsis:
---
---
 timerX([startTime=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

timerX is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Example 1: Simple timing
---

start = cmds.timerX()
code that is being timed
totalTime = cmds.timerX(startTime=start)
print "Total time: ", totalTime

Example 2: Iterative timing
---

startTime = cmds.timerX()
for i in range(0,5):
  elapsedTime = cmds.timerX()
  print "Elapsed Time: ", elapsedTime

Example 3: Stacked timing calls
---

startTime1 = cmds.timerX()
startTime2 = cmds.timerX()
for i in range(0,5):
  elapsedTime = cmds.timerX()
  print "Elapsed Time: ", elapsedTime

totalTime = cmds.timerX(startTime=startTime1)
print "Total Time: ", totalTime

---
Return:
---


    float: This command returns a different value depending on
the flag used. If no flag is used, then the start time
is returned. If the "-st" flag is used, then it returns
the elapsed time since the start time.

Flags:
---


---
startTime(st): float
    properties: create
    When this flag is used, the command returns the elapsed time since the specified start time.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/timerX.html 
    """


def toggle(flagabove: boolean, flagbelow: boolean, flagboundary: boolean, flagboundingBox: boolean, flagcontrolVertex: boolean, flagdoNotWrite: boolean, flageditPoint: boolean, flagextent: boolean, flagfacet: boolean, flaggeometry: boolean, flaggl: boolean, flaghighPrecisionNurbs: boolean, flaghull: boolean, flaglatticePoint: boolean, flaglatticeShape: boolean, flaglocalAxis: boolean, flagnewCurve: boolean, flagnewPolymesh: boolean, flagnewSurface: boolean, flagnormal: boolean, flagorigin: boolean, flagpoint: boolean, flagpointDisplay: boolean, flagpointFacet: boolean, flagrotatePivot: boolean, flagscalePivot: boolean, flagselectHandle: boolean, flagstate: boolean, flagsurfaceFace: boolean, flagtemplate: boolean, flaguvCoords: boolean, flagvertex: boolean) -> boolean:
    """Synopsis:
---
---
 toggle(
[objects]
    , [above=boolean], [below=boolean], [boundary=boolean], [boundingBox=boolean], [controlVertex=boolean], [doNotWrite=boolean], [editPoint=boolean], [extent=boolean], [facet=boolean], [geometry=boolean], [gl=boolean], [highPrecisionNurbs=boolean], [hull=boolean], [latticePoint=boolean], [latticeShape=boolean], [localAxis=boolean], [newCurve=boolean], [newPolymesh=boolean], [newSurface=boolean], [normal=boolean], [origin=boolean], [point=boolean], [pointDisplay=boolean], [pointFacet=boolean], [rotatePivot=boolean], [scalePivot=boolean], [selectHandle=boolean], [state=boolean], [surfaceFace=boolean], [template=boolean], [uvCoords=boolean], [vertex=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toggle is undoable, queryable, and NOT editable.
Note: This command is not undoable.




Example:
---
import maya.cmds as cmds

surface1 = cmds.sphere()
cmds.toggle( surface1, cv=True )
cmds.toggle( g=True, cv=True )
cmds.toggle( q=True, cv=True )
Returns 0 if the queried state is false.
Returns 1 if the queried state is true.

---
Return:
---


    boolean: when in the query mode. none otherwise.

Flags:
---


---
above(a): boolean
    properties: create
    Toggle state for all objects above listed objects.

---
below(b): boolean
    properties: create
    Toggle state for all objects below listed objects.

---
boundary(bn): boolean
    properties: create, query
    Toggle boundary display of listed mesh objects.

---
boundingBox(box): boolean
    properties: create, query
    Toggle or query the bounding box display of listed objects.

---
controlVertex(cv): boolean
    properties: create, query
    Toggle CV display of listed curves and surfaces.

---
doNotWrite(dnw): boolean
    properties: create, query
    Toggle the "this should be written to the file" state.

---
editPoint(ep): boolean
    properties: create, query
    Toggle edit point display of listed curves and surfaces.

---
extent(et): boolean
    properties: create, query
    Toggle display of extents of listed mesh objects.

---
facet(f): boolean
    properties: create, query
    For use with normal flag. Set the normal display style to facet display.

---
geometry(g): boolean
    properties: create, query
    Toggle geometry display of listed objects.

---
gl(gl): boolean
    properties: create
    Toggle state for all objects

---
highPrecisionNurbs(hpn): boolean
    properties: create, query
    Toggle high precision display for Nurbs

---
hull(hl): boolean
    properties: create, query
    Toggle hull display of listed curves and surfaces.

---
latticePoint(lp): boolean
    properties: create, query
    Toggle point display of listed lattices

---
latticeShape(ls): boolean
    properties: create, query
    Toggle display of listed lattices

---
localAxis(la): boolean
    properties: create, query
    Toggle local axis display of listed objects.

---
newCurve(nc): boolean
    properties: create, query
    Set component display state of new curve objects

---
newPolymesh(np): boolean
    properties: create, query
    Set component display state of new polymesh objects

---
newSurface(ns): boolean
    properties: create, query
    Set component display state of new surface objects

---
normal(nr): boolean
    properties: create, query
    Toggle display of normals of listed surface and mesh objects.

---
origin(o): boolean
    properties: create, query
    Toggle origin display of listed surfaces.

---
point(pt): boolean
    properties: create, query
    For use with normal flag. Set the normal display style to vertex display.

---
pointDisplay(pd): boolean
    properties: create, query
    Toggle point display of listed surfaces.

---
pointFacet(pf): boolean
    properties: create, query
    For use with normal flag. Set the normal display style to vertex and face display.

---
rotatePivot(rp): boolean
    properties: create, query
    Toggle rotate pivot display of listed objects.

---
scalePivot(sp): boolean
    properties: create, query
    Toggle scale pivot display of listed objects.

---
selectHandle(sh): boolean
    properties: create, query
    Toggle select handle display of listed objects.

---
state(st): boolean
    properties: create
    Explicitly set the state to true or false instead of toggling the state.
Can not be queried.

---
surfaceFace(sf): boolean
    properties: create, query
    Toggle surface face handle display of listed surfaces.

---
template(te): boolean
    properties: create, query
    Toggle template state of listed objects

---
uvCoords(uv): boolean
    properties: create, query
    Toggle display uv coords of listed mesh objects.

---
vertex(vt): boolean
    properties: create, query
    Toggle vertex display of listed mesh objects.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toggle.html 
    """


def toggleAxis(flagorigin: boolean, flagview: boolean) -> boolean:
    """Synopsis:
---
---
 toggleAxis([origin=boolean], [view=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toggleAxis is undoable, queryable, and NOT editable.
Note: the display of the axis in the bottom left corner has
been rendered obsolete by the headsUpDisplay command.




Example:
---
import maya.cmds as cmds

Turns origin axis on
cmds.toggleAxis( o=True )

Turns origin axis off.
cmds.toggleAxis( o=False )

Returns true if the axis at the origin is on.
cmds.toggleAxis( q=True, o=True )

Toggles the display of the axis
cmds.toggleAxis()

---
Return:
---


    boolean: if in the query mode, otherwise none.

Flags:
---


---
origin(o): boolean
    properties: create, query
    Turns display of the axis at the origin of the ground plane
on or off.

---
view(v): boolean
    properties: create, query
    Turns display of the axis at the bottom left of each view
on or off. (Obsolete - refer to the headsUpDisplay command)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toggleAxis.html 
    """


def toggleDisplacement() -> None:
    """Synopsis:
---
---
 toggleDisplacement(
[objects]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toggleDisplacement is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Toggle the displacement preview of the selected polygons.
cmds.toggleDisplacement()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toggleDisplacement.html 
    """


def toggleWindowVisibility() -> None:
    """Synopsis:
---
---
 toggleWindowVisibility(
[string]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toggleWindowVisibility is undoable, NOT queryable, and NOT editable.windowvis/visible



Example:
---
import maya.cmds as cmds

window1 = cmds.window( retain=True )
cmds.columnLayout()
cmds.checkBox()
cmds.checkBox()
cmds.checkBox()
cmds.button( label='Close', command='cmds.window( window1, edit=True, visible=False )' )

   Create another window with a button that will toggle the visibility
   of the first window.
---

window2 = cmds.window()
cmds.columnLayout()
cmds.button( label='Toggle Window Visibility', command=('cmds.toggleWindowVisibility(\"' + window1 +'\")' ) )

cmds.showWindow( window1 )
cmds.showWindow( window2 )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toggleWindowVisibility.html 
    """


def tolerance(flagangular: angle, flaglinear: linear) -> None:
    """Synopsis:
---
---
 tolerance([angular=angle], [linear=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

tolerance is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.tolerance( linear=0.02 )sets the tolerance to 0.02, in the current unit
cmds.tolerance( linear='0.02cm' )sets the tolerance to 0.02 cm
cmds.tolerance( angular='0.02rad' )sets the angle tolerance to 0.02 radians
cmds.tolerance( q=True, linear=True )returns the current tolerance in the current unit
cmds.tolerance( q=True, angular=True )returns the current tolerance in the current unit

---


Flags:
---


---
angular(a): angle
    properties: create, query
    Sets the angular, or "tangential" tolerance.

---
linear(l): linear
    properties: create, query
    Sets the linear, or "positonal" tolerance.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/tolerance.html 
    """


def toolBar(flagallowedArea: string, flagannotation: string, flagarea: string, flagbackgroundColor: tuple[float, float, float], flagcontent: string, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 toolBar(
[name]
    , [allowedArea=string], [annotation=string], [area=string], [backgroundColor=[float, float, float]], [content=string], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toolBar is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

myWindow = cmds.window()
buttonForm = cmds.formLayout( parent = myWindow )
cmds.button( parent = buttonForm )
allowedAreas = ['top', 'bottom']
cmds.toolBar( area='top', content=myWindow, allowedArea=allowedAreas )

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
allowedArea(aa): string
    properties: create, query, edit, multiuse
    Areas where the dock control may be placed. Valid values are "top", "left", "bottom", "right" and "all".  The default is "all".

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
area(a): string
    properties: create, query, edit
    The initial dock area for this dock control. Valid values are "top", "left", "bottom" and "right". This is a required flag.

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
content(con): string
    properties: create, query
    The name of the control that is a content of this dock control. This is a required flag.

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
label(l): string
    properties: create, query, edit
    The label text.  The default label is the name of the control.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toolBar.html 
    """


def toolButton(flagallowMultipleTools: boolean, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcollection: string, flagdefineTemplate: string, flagdocTag: string, flagdoubleClickCommand: script, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagimage1: string, flagimage2: string, flagimage3: string, flagimageOverlayLabel: string, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagoffCommand: script, flagonCommand: script, flagparent: string, flagpopupIndicatorVisible: boolean, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagselect: boolean, flagstatusBarMessage: string, flagstyle: string, flagtool: string, flagtoolArray: boolean, flagtoolCount: boolean, flagtoolImage1: tuple[string, string], flagtoolImage2: tuple[string, string], flagtoolImage3: tuple[string, string], flaguseTemplate: string, flagversion: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 toolButton(
[string]
    , [allowMultipleTools=boolean], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [collection=string], [defineTemplate=string], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script], [parent=string], [popupIndicatorVisible=boolean], [popupMenuArray=boolean], [preventOverride=boolean], [select=boolean], [statusBarMessage=string], [style=string], [tool=string], [toolArray=boolean], [toolCount=boolean], [toolImage1=[string, string]], [toolImage2=[string, string]], [toolImage3=[string, string]], [useTemplate=string], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toolButton is undoable, queryable, and editable.cl/collection
By default, this control only handles one tool at a time.  Using
the t/tool flag to associate a new tool will simply override the
previous attached tool.  If you use the amt/allowMultipleTools
flag then you will be able to attach more than one tool with this
control.  Only one tool will be current within the control.  To access
the other tools press the right mouse button to display a popup menu
containing all the tools associated with this control.  If you set
the piv/popupIndicatorVisible flag then a small arrow will be
drawn on the control to indicate that additional tools are attached to
this control.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.toolCollection()
cmds.toolButton( tool='selectSuperContext', toolImage1=('selectSuperContext', 'aselect.xpm') )
cmds.toolButton( tool='moveSuperContext', toolImage1=('moveSuperContext', 'move_M.xpm') )
cmds.toolButton( tool='scaleSuperContext', toolImage1=('scaleSuperContext', 'scale_M.png') )
cmds.showWindow()

example showing how to create tool buttons for artisan tools
---

create the contexts
selectCtx = cmds.artSelectCtx()
puttyCtx = cmds.artPuttyCtx()
setPaintCtx = cmds.artSetPaintCtx()

cmds.window()
cmds.gridLayout()
cmds.toolCollection()
create the tool buttons using the contexts returned
cmds.toolButton(
                amt=True, piv=True,
                doubleClickCommand='cmds.toolPropertyWindow()',
                tool=(selectCtx, puttyCtx, setPaintCtx),
                toolImage1=(selectCtx, 'artSelect.xpm'),
                toolImage2=(puttyCtx, 'putty.png'),
                toolImage3=(setPaintCtx, 'paintSetMembership.png') )
cmds.showWindow()

---
Return:
---


    string: The name of the toolButton created.

Flags:
---


---
allowMultipleTools(amt): boolean
    properties: create, query
    Indicates whether this control will allow you to attach more
than one tool.  By default, this control accepts only one tool.
You can add multiple tools by setting this flag to true.
Only one tool will be current and displayed at any one time.
Use the pop up menu attached to the right mouse button to view
all the tools.

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
    Command executed when the control's state is changed.
Note that this flag should not be used in conjunction with
onCommand and offCommand. That is, one should either use
changeCommand and test the state of the control from inside
the callback, or use onCommand and offCommand as separate
callbacks.

---
collection(cl): string
    properties: create, edit
    To explicitly add a tool button to a tool collection.

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
image3(i3): string
    properties: create, query, edit
    This control supports three images.  The image that best fits the
current size of the control will be displayed.  This flag
applies the image to the current tool.

---
imageOverlayLabel(iol): string
    properties: create, query, edit
    A short string (5 characters) label that will be displayed
on top of the icon.

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
    Command executed when the control is turned off.

---
onCommand(onc): script
    properties: create, edit
    Command executed when the control is turned on.

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
popupIndicatorVisible(piv): boolean
    properties: create, query, edit
    Edit this flag to set the visibility of the popup tool indicator.
The indicator is a simple image that appears in the top right corner
of the button when more that one tool is associated with this control.
This flag is queryable and true by default.

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
select(sl): boolean
    properties: create, edit
    Will set this button as the selected one.  This flag also
queries the select state of the control.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
style(st): string
    properties: create, edit
    The draw style of the control.  Valid styles are "iconOnly",
"textOnly", "iconAndTextHorizontal" and "iconAndTextVertical".

---
tool(t): string
    properties: create, query, edit, multiuse
    The name of the tool to be attached to the button.  If the
tool specified is already attached to this button then it will
be selected.  Query this flag to return the current tool.  This
flag may be specified more than once to attach more than one
tool.

---
toolArray(ta): boolean
    properties: query
    This query only flag returns the names of all the tools attached
to the toolButton control.

---
toolCount(tc): boolean
    properties: query
    This query only flag return the number of tools attached to the
toolButton control.

---
toolImage3(ti3): [string, string]
    properties: create, query, edit, multiuse
    This control supports three images.  The image that best fits the
current size of the control will be displayed.  This flag
applies the image to the specified tool.  The first argument is the
name of the tool and the second is the name of the image.  When
queried an array of tool icon pairs is returned.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
version(ver): string
    properties: create, query, edit
    Specify the version that this tool button feature was introduced.
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toolButton.html 
    """


def toolCollection(flagcollectionItemArray: boolean, flagdefineTemplate: string, flagexists: boolean, flaggl: boolean, flagnumberOfCollectionItems: boolean, flagparent: string, flagselect: string, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 toolCollection(
[string]
    , [collectionItemArray=boolean], [defineTemplate=string], [exists=boolean], [gl=boolean], [numberOfCollectionItems=boolean], [parent=string], [select=string], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toolCollection is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.toolCollection()
cmds.toolButton( tool='selectSuperContext', toolImage1=('selectSuperContext', 'aselect.xpm') )
cmds.toolButton( tool='moveSuperContext', toolImage1=('moveSuperContext', 'move_M.png') )
cmds.toolButton( tool='scaleSuperContext', toolImage1=('scaleSuperContext', 'scale_M.png') )
cmds.showWindow()

---
Return:
---


    string: The name of the toolCollection created.

Flags:
---


---
collectionItemArray(cia): boolean
    properties: query
    Returns a string list giving the long names of all the items
in this collection.

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
gl(gl): boolean
    properties: create, query
    Set the collection to have no parent layout.  This flag must be
specified when the collection is created and can not be queried
or edited.  Consequently, global collections must be explicitly
deleted.

---
numberOfCollectionItems(nci): boolean
    properties: query
    Returns the number of items that are in this collection.

---
parent(p): string
    properties: create
    Specify the parent to associate the collection with.  The collection
will be deleted along with the parent.  This flag must be specified
when the collection is created and can not be edited.

---
select(sl): string
    properties: create, query, edit
    Select the specified collection item.  If queried will return
the name of the currently selected collection item.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toolCollection.html 
    """


def toolDropped() -> None:
    """Synopsis:
---
---
 toolDropped(
[string]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toolDropped is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create move tool button and scale tool button in a new window
cmds.window()
cmds.columnLayout()
cmds.toolCollection()
cmds.toolButton( tool='moveSuperContext', toolImage1=('moveSuperContext', 'move_M.png') )
cmds.toolButton( tool='scaleSuperContext', toolImage1=('scaleSuperContext', 'scale_M.png') )
cmds.showWindow()

Drop select tool to the created window
cmds.toolDropped('selectTool')

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toolDropped.html 
    """


def toolHasOptions() -> boolean:
    """Synopsis:
---
---
 toolHasOptions(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toolHasOptions is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

if cmds.toolHasOptions('moveSuperContext'):
        print 'moveSuperContext tool has options'

---
Return:
---


    boolean: True if the queried tool has options, otherwise false.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toolHasOptions.html 
    """


def toolPropertyWindow(flagfield: string, flaghelpButton: string, flagicon: string, flaginMainWindow: boolean, flaglocation: string, flagnoviceMode: boolean, flagresetButton: string, flagrestore: boolean, flagselectCommand: string, flagshowCommand: string) -> None:
    """Synopsis:
---
---
 toolPropertyWindow([field=string], [helpButton=string], [icon=string], [inMainWindow=boolean], [location=string], [noviceMode=boolean], [resetButton=string], [restore=boolean], [selectCommand=string], [showCommand=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

toolPropertyWindow is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.toolPropertyWindow()
pictureObject = cmds.toolPropertyWindow(q=True, icon=True)

---


Flags:
---


---
field(fld): string
    properties: query, edit
    Sets/returns the name of the text field used to store the
tool name in the property sheet.

---
helpButton(hb): string
    properties: query, edit
    Sets/returns the name of the button used to show help
on the tool in the property sheet.

---
icon(icn): string
    properties: query, edit
    Sets/returns the name of the static picture object (used to display the
tool icon in the property sheet).

---
inMainWindow(imw): boolean
    properties: create
    Specify true if you want the tool settings to appear in the main
window rather than a separate window.

---
location(loc): string
    properties: query, edit
    Sets/returns the location of the current tool property sheet, or an empty
string if there is none.

---
noviceMode(nm): boolean
    properties: query, edit
    Sets/returns the 'novice mode' flag.(unused at the moment)

---
resetButton(rb): string
    properties: query, edit
    Sets/returns the name of the button used to restore the
tool settings in the property sheet.

---
restore(rs): boolean
    properties: create
    Reopens the tool settings window.
This flag can be used with the flag inMainWindow for the fall back location if the tool settings can't be restored.

---
selectCommand(sel): string
    properties: query, edit
    Sets/returns the property sheet's select command.

---
showCommand(shw): string
    properties: query, edit
    Sets/returns the property sheet's display command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/toolPropertyWindow.html 
    """


def torus(flagaxis: tuple[linear, linear, linear], flagcaching: boolean, flagconstructionHistory: boolean, flagdegree: int, flagendSweep: angle, flagheightRatio: float, flagminorSweep: angle, flagname: string, flagnodeState: int, flagobject: boolean, flagpivot: tuple[linear, linear, linear], flagpolygon: int, flagradius: linear, flagsections: int, flagspans: int, flagstartSweep: angle, flagtolerance: linear, flaguseTolerance: boolean) -> list[string]:
    """Synopsis:
---
---
 torus([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean], [degree=int], [endSweep=angle], [heightRatio=float], [minorSweep=angle], [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [radius=linear], [sections=int], [spans=int], [startSweep=angle], [tolerance=linear], [useTolerance=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

torus is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.torus()
cmds.torus( ch=True, radius=10, hr=3 )
cmds.torus( r=5, axis=(1, 1, 1), pivot=(0, 0, 1), ssw='0deg', esw='90deg', msw='45deg' )
cmds.torus( ut=True, tol=0.01 )
query the torus radius
r = cmds.torus( 'nurbsTorus1', r=True, q=True )

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
minorSweep(msw): angle
    properties: create, query, edit
    The sweep angle for the minor circle in the torus
Default: 6.2831853

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/torus.html 
    """


def track(flagdown: linear, flagleft: linear, flagright: linear, flagupDistance01: linear, flagupDistance02: linear) -> None:
    """Synopsis:
---
---
 track(
[camera]
    , [down=linear], [left=linear], [right=linear], [upDistance01=linear], [upDistance02=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

track is undoable, NOT queryable, and NOT editable.
The track command can be applied to either a perspective or an
orthographic camera.

When no camera name is supplied, this command is applied to the
camera in the active view.




Example:
---
import maya.cmds as cmds

cmds.camera()

cmds.track( 'cameraShape1', d=10 )To track the camera down

cmds.track( 'cameraShape1', u=-10 )

cmds.track( u=-10 )

---


Flags:
---


---
down(d): linear
    properties: create
    Set the amount of down translation in unit distance.

---
left(l): linear
    properties: create
    Set the amount of left translation in unit distance.

---
right(r): linear
    properties: create
    Set the amount of right translation in unit distance.

---
upDistance01(u): linear
    properties: create
    Set the amount of up translation in unit distance. This is equivalent
to using up/upDistance02 flag.

---
upDistance02(up): linear
    properties: create
    Set the amount of up translation in unit distance. This is equivalent
to using u/upDistance01 flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/track.html 
    """


def trackCtx(flagalternateContext: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagtoolName: string, flagtrackGeometry: boolean, flagtrackScale: float) -> string:
    """Synopsis:
---
---
 trackCtx([alternateContext=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [toolName=string], [trackGeometry=boolean], [trackScale=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

trackCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.trackCtx( 'trackContext', ac=False, tg=False, ts=1.0 )

---
Return:
---


    string: The name of the context

Flags:
---


---
alternateContext(ac): boolean
    properties: create, query
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

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
trackGeometry(tg): boolean
    properties: create, query, edit
    Toggle whether the drag should try to track geometry. The
context will compute a track plane by intersecting the initial
press with geometry or the live object.

---
trackScale(ts): float
    properties: create, query, edit
    Specify the distance to the track plane from the camera. The
smaller the scale the slower the drag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/trackCtx.html 
    """


def transferAttributes(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcolorBorders: uint, flagcomponents: boolean, flagdeformerTools: boolean, flagexclusive: string, flagflipUVs: uint, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flagmatchChoice: uint, flagname: string, flagparallel: boolean, flagprune: boolean, flagremove: boolean, flagsampleSpace: uint, flagsearchMethod: uint, flagsearchScaleX: float, flagsearchScaleY: float, flagsearchScaleZ: float, flagselectedComponents: boolean, flagsourceColorSet: string, flagsourceUvSet: string, flagsourceUvSpace: string, flagsplit: boolean, flagtargetColorSet: string, flagtargetUvSet: string, flagtargetUvSpace: string, flagtransferColors: uint, flagtransferNormals: uint, flagtransferPositions: uint, flagtransferUVs: uint, flaguseComponentTags: boolean) -> string:
    """Synopsis:
---
---
 transferAttributes(
object object
    , [after=boolean], [afterReference=boolean], [before=boolean], [colorBorders=uint], [components=boolean], [deformerTools=boolean], [exclusive=string], [flipUVs=uint], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [matchChoice=uint], [name=string], [parallel=boolean], [prune=boolean], [remove=boolean], [sampleSpace=uint], [searchMethod=uint], [searchScaleX=float], [searchScaleY=float], [searchScaleZ=float], [selectedComponents=boolean], [sourceColorSet=string], [sourceUvSet=string], [sourceUvSpace=string], [split=boolean], [targetColorSet=string], [targetUvSet=string], [targetUvSpace=string], [transferColors=uint], [transferNormals=uint], [transferPositions=uint], [transferUVs=uint], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

transferAttributes is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Transfer all UV and color sets from pCube1 onto pSphere1
cmds.transferAttributes( 'pCube1', 'pSphere1', transferUVs=2, transferColors=2 )

---
Return:
---


    string: The node name.

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
colorBorders(clb): uint
    properties: create, edit
    Controls whether color borders are preserved when transferring color
data. If this is non-zero, any color borders will be mapped onto the nearest
edge on the target geometry. 0 means any color borders will be
smoothly blended onto the vertices of the target geometry.

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
exclusive(ex): string
    properties: create, query
    Puts the deformation set in a deform partition.

---
flipUVs(fuv): uint
    properties: create, edit
    Controls how sampled UV data is flipped before being transferred
to the target. 0 means no flipping; 1 means UV data is flipped in the
U direction; 2 means UV data is flipped in the V direction; and 3 means
it is flipped in both directions. In conjunction with mirroring, this
allows the creation of symmetric UV mappings (e.g. the left hand side of the
character on one side of the UV map, the right hand side on the other).

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
matchChoice(mch): uint
    properties: create, edit
    When using topological component matching, selects between possible matches.
If the meshes involved in the transfer operation have symmetries in their
topologies, there may be more than one possible topological match.
Maya scores the possible matches (by comparing the shapes of the meshes)
and assigns them an index, starting at zero.
Match zero, the default, is considered the best, but in the event that Maya
chooses the wrong one, changing this value will allow the user to explore the
other matches.

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
remove(rm): boolean
    properties: edit, multiuse
    Specifies that objects listed after the -g flag should
be removed from this deformer.

---
sampleSpace(spa): uint
    properties: create, edit
    Selects which space the attribute transfer is performed in.
0 is world space, 1 is model space, 4 is component-based, 5 is topology-based. The default is world space.

---
searchMethod(sm): uint
    properties: create, edit
    Specifies which search method to use when correlating points.
0 is closest along normal, 3 is closest to point. The default is closest to point.

---
searchScaleX(ssx): float
    properties: create, edit
    Specifies an optional scale that should be applied to the x-axis
of the target model before transferring data. A value of 1.0 (the
default) means no scaling; a value of -1.0 would indicate mirroring
along the x-axis.

---
searchScaleY(ssy): float
    properties: create, edit
    Specifies an optional scale that should be applied to the y-axis
of the target model before transferring data. A value of 1.0 (the
default) means no scaling; a value of -1.0 would indicate mirroring
along the y-axis.

---
searchScaleZ(ssz): float
    properties: create, edit
    Specifies an optional scale that should be applied to the z-axis
of the target model before transferring data. A value of 1.0 (the
default) means no scaling; a value of -1.0 would indicate mirroring
along the z-axis.

---
selectedComponents(cms): boolean
    properties: query
    Returns the components used by the deformer that are currently selected.
This intersects the current selection with the components affected by the deformer.

---
sourceColorSet(scs): string
    properties: create
    Specifies the name of a single color set on the source surface(s) that
should be transferred to the target. This value is only used when
the operation is configured to transfer a single color set (see the
transferColors flag).

---
sourceUvSet(suv): string
    properties: create
    Specifies the name of a single UV set on the source surface(s) that
should be transferred to the target. This value is only used when
the operation is configured to transfer a single UV set (see the
transferUVs flag).

---
sourceUvSpace(sus): string
    properties: create
    Specifies the name of the UV set on the source surface(s) that
should be used as the transfer space. This value is only used when
the operation is configured to transfer attributes in UV space.

---
split(sp): boolean
    properties: create, edit
    Branches off a new chain in the dependency graph instead
of inserting/appending the deformer into/onto an
existing chain.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
targetColorSet(tcs): string
    properties: create
    Specifies the name of a single color set on the target surface that
should be receive the sampled color data. This value is only used when
the operation is configured to transfer a single color set (see the
transferColors flag).

---
targetUvSet(tuv): string
    properties: create
    Specifies the name of a single UV set on the target surface that
should be receive the sampled UV data. This value is only used when
the operation is configured to transfer a single UV set (see the
transferUVs flag).

---
targetUvSpace(tus): string
    properties: create
    Specifies the name of the UV set on the target surface( that
should be used as the transfer space. This value is only used when
the operation is configured to transfer attributes in UV space.

---
transferColors(col): uint
    properties: create, edit
    Controls color set transfer. 0 means no color sets are transferred,
1 means that a single color set (specified by sourceColorSet and targetColorSet)
is transferred, and 2 means that all color sets are transferred.

---
transferNormals(nml): uint
    properties: create, edit
    A non-zero value indicates vertex normals should be sampled
and written into user normals on the target surface.

---
transferPositions(pos): uint
    properties: create, edit
    A non-zero value indicates vertex position should be sampled,
causing the target surface to "wrap" to the source surface(s).

---
transferUVs(uvs): uint
    properties: create, edit
    Controls UV set transfer. 0 means no UV sets are transferred,
1 means that a single UV set (specified by sourceUVSet and targetUVSet)
is transferred, and 2 means that all UV sets are transferred.

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/transferAttributes.html 
    """


def transferShadingSets(flagsampleSpace: uint, flagsearchMethod: uint) -> None:
    """Synopsis:
---
---
 transferShadingSets([sampleSpace=uint], [searchMethod=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

transferShadingSets is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

make a low res sphere with shaders
low = cmds.polySphere( sx=6, sy=6 )[0]
lowShape = cmds.listRelatives( low, fullPath=True, shapes=True )[0]
redSG = cmds.sets( r=True, em=True )
redMat = cmds.shadingNode( "lambert", asShader=True )
cmds.setAttr( redMat + ".color", 1, 0, 0, type='double3' )
cmds.connectAttr( redMat + ".outColor", redSG + ".surfaceShader", f=True )
greenSG = cmds.sets( r=True, em=True )
greenMat = cmds.shadingNode( "lambert", asShader=True )
cmds.setAttr( greenMat + ".color", 0, 1, 0, type='double3' )
cmds.connectAttr( greenMat + ".outColor", greenSG + ".surfaceShader", f=True )
cmds.sets( lowShape + '.f[0:17]', e=True, fe=redSG )
cmds.sets( lowShape + '.f[18:36]', e=True, fe=greenSG )

make a high res sphere
high = cmds.polySphere( sx=20, sy=20 )[0]
highShape = cmds.listRelatives( high, fullPath=True, shapes=True )[0]
cmds.xform( high, ws=True, t=(2, 0, 0) )

transfer the shading sets
cmds.select( low, r=True )
cmds.select( high, tgl=True )
cmds.transferShadingSets( sampleSpace=1 )

---


Flags:
---


---
sampleSpace(spa): uint
    properties: create, query, edit
    Selects which space the attribute transfer is performed in.
0 is world space, 1 is model space. The default is world space.

---
searchMethod(sm): uint
    properties: create, query, edit
    Specifies which search method to use when correlating points.
0 is closest along normal, 3 is closest to point. The default is closest to point.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/transferShadingSets.html 
    """


def transformCompare(flagroot: boolean) -> int:
    """Synopsis:
---
---
 transformCompare(
[dagObject dagObject]
    , [root=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

transformCompare is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create some joints
---

cmds.select( d=True )
cmds.joint( p=(-3.226531, 0, -4.866136) )
cmds.joint( p=(2.817897, 0, -4.016915) )
cmds.joint( 'joint1', e=True, zso=True, oj='xyz', sao='yup' )

Compare 2 different joints, a 1 will be returned
---

cmds.select( 'joint1', 'joint2', r=True )
cmds.transformCompare()

Duplicate joint1 and compare the duplicate
---

cmds.select( 'joint1', r=True )
cmds.duplicate()
cmds.select( cl=True )
cmds.select( 'joint1', 'joint3', r=True )
cmds.transformCompare()

---
Return:
---


    int: 0 if successful, 1 if transform1 and transform2 are not determined to be equal.

Flags:
---


---
root(r): boolean
    properties: create
    Compare the root only, rather than the entire hierarchy below the roots.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/transformCompare.html 
    """


def transformLimits(flagenableRotationX: tuple[boolean, boolean], flagenableRotationY: tuple[boolean, boolean], flagenableRotationZ: tuple[boolean, boolean], flagenableScaleX: tuple[boolean, boolean], flagenableScaleY: tuple[boolean, boolean], flagenableScaleZ: tuple[boolean, boolean], flagenableTranslationX: tuple[boolean, boolean], flagenableTranslationY: tuple[boolean, boolean], flagenableTranslationZ: tuple[boolean, boolean], flagremove: boolean, flagrotationX: tuple[angle, angle], flagrotationY: tuple[angle, angle], flagrotationZ: tuple[angle, angle], flagscaleX: tuple[float, float], flagscaleY: tuple[float, float], flagscaleZ: tuple[float, float], flagtranslationX: tuple[linear, linear], flagtranslationY: tuple[linear, linear], flagtranslationZ: tuple[linear, linear]) -> None:
    """Synopsis:
---
---
 transformLimits(
[object]
    , [enableRotationX=[boolean, boolean]], [enableRotationY=[boolean, boolean]], [enableRotationZ=[boolean, boolean]], [enableScaleX=[boolean, boolean]], [enableScaleY=[boolean, boolean]], [enableScaleZ=[boolean, boolean]], [enableTranslationX=[boolean, boolean]], [enableTranslationY=[boolean, boolean]], [enableTranslationZ=[boolean, boolean]], [remove=boolean], [rotationX=[angle, angle]], [rotationY=[angle, angle]], [rotationZ=[angle, angle]], [scaleX=[float, float]], [scaleY=[float, float]], [scaleZ=[float, float]], [translationX=[linear, linear]], [translationY=[linear, linear]], [translationZ=[linear, linear]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

transformLimits is undoable, queryable, and editable.
We can also turn any limits off which may have been previously set.
When an object is first created, all the transformation limits are off
by default.

Transformation limits allow us to control how much an object can
be transformed. This is most useful for joints, although it can be
used any place we would like to limit the movement of an object.

Default values are:
( -1, 1) for translation,
( -1, 1) for scaling, and
(-45,45) for rotation.




Example:
---
import maya.cmds as cmds

Create an object, e.g.
cmds.cone()

1. To set the limits for the translation of the cone to within
a unit volume centered at the origin
cmds.transformLimits( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1) )

2. To disable the lower limits
cmds.transformLimits( etx=(False, True), ety=(False, True), etz=(False, True ) )

---


Flags:
---


---
enableRotationX(erx): [boolean, boolean]
    properties: query
    enable/disable the lower and upper x-rotation limits
When queried, it returns boolean boolean

---
enableRotationY(ery): [boolean, boolean]
    properties: query
    enable/disable the lower and upper y-rotation limits
When queried, it returns boolean boolean

---
enableRotationZ(erz): [boolean, boolean]
    properties: query
    enable/disable the lower and upper z-rotation limits
When queried, it returns boolean boolean

---
enableScaleX(esx): [boolean, boolean]
    properties: query
    enable/disable the lower and upper x-scale limits
When queried, it returns boolean boolean

---
enableScaleY(esy): [boolean, boolean]
    properties: query
    enable/disable the lower and upper y-scale limits
When queried, it returns boolean boolean

---
enableScaleZ(esz): [boolean, boolean]
    properties: query
    enable/disable the lower and upper z-scale limits
When queried, it returns boolean boolean

---
enableTranslationX(etx): [boolean, boolean]
    properties: query
    enable/disable the  ower and upper x-translation limits
When queried, it returns boolean boolean

---
enableTranslationY(ety): [boolean, boolean]
    properties: query
    enable/disable the lower and upper y-translation limits
When queried, it returns boolean boolean

---
enableTranslationZ(etz): [boolean, boolean]
    properties: query
    enable/disable the lower and upper z-translation limits
When queried, it returns boolean boolean

---
remove(rm): boolean
    properties: create
    turn all the limits off and reset them to their default values

---
rotationX(rx): [angle, angle]
    properties: query
    set the lower and upper x-rotation limits
When queried, it returns angle angle

---
rotationY(ry): [angle, angle]
    properties: query
    set the lower and upper y-rotation limits
When queried, it returns angle angle

---
rotationZ(rz): [angle, angle]
    properties: query
    set the lower and upper z-rotation limits
When queried, it returns angle angle

---
scaleX(sx): [float, float]
    properties: query
    set the lower and upper x-scale limits
When queried, it returns float float

---
scaleY(sy): [float, float]
    properties: query
    set the lower and upper y-scale limits
When queried, it returns float float

---
scaleZ(sz): [float, float]
    properties: query
    set the lower and upper z-scale limits
When queried, it returns float float

---
translationX(tx): [linear, linear]
    properties: query
    set the lower and upper x-translation limits
When queried, it returns linear linear

---
translationY(ty): [linear, linear]
    properties: query
    set the lower and upper y-translation limits
When queried, it returns linear linear

---
translationZ(tz): [linear, linear]
    properties: query
    set the lower and upper z-translation limits
When queried, it returns linear linear

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/transformLimits.html 
    """


def translator(flagdefaultFileRule: boolean, flagdefaultOptions: string, flagextension: boolean, flagfileCompression: string, flagfilter: boolean, flagfindTranslator: tuple[string, int], flaglist: boolean, flagloaded: boolean, flagobjectType: boolean, flagoptionsScript: boolean, flagreadSupport: boolean, flagwriteSupport: boolean) -> boolean:
    """Synopsis:
---
---
 translator(
[string]
    , [defaultFileRule=boolean], [defaultOptions=string], [extension=boolean], [fileCompression=string], [filter=boolean], [findTranslator=[string, int]], [list=boolean], [loaded=boolean], [objectType=boolean], [optionsScript=boolean], [readSupport=boolean], [writeSupport=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

translator is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Returns true if dxf files can be read.
cmds.translator( 'dxf', q=True, rs=True )

---
Return:
---


    boolean: or string array depending upon which flags are specified.

Flags:
---


---
defaultFileRule(dfr): boolean
    properties: query
    Returns the default file rule value, can return "" as well

---
defaultOptions(do): string
    properties: query
    Return/set a string of default options used by this translator.

---
extension(ext): boolean
    properties: query
    Returns the default file extension for this translator.

---
fileCompression(cmp): string
    properties: query
    Specifies the compression action to take when a file is saved.
Possible values are "compressed", "uncompressed" "asCompressed".

---
filter(f): boolean
    properties: query
    Returns the filter string used for this translator.

---
findTranslator(ft): [string, int]
    properties: create
    Returns the name of the translator that can handle the given file.
String argument is a file path.
Int argument is read and write attributes.
0: A translator that can read
1: A translator that can write
2: A translator that can read and write

---
list(l): boolean
    properties: query
    Return a string array of all the translators that are loaded.

---
loaded(ld): boolean
    properties: query
    Returns true if the given translator is currently loaded.

---
objectType(ot): boolean
    properties: query
    This flag is obsolete. This will now return the same results as
defaultFileRule going forward.

---
optionsScript(os): boolean
    properties: query
    Query the name of the options script to use to post the user
options UI. When this script is invoked it will expect the name of the
parent layout in which the options will be displayed as well as the name
of the callback to be invoked once the apply button has been depressed
in the options area.

---
readSupport(rs): boolean
    properties: query
    Returns true if this translator supports read operations.

---
writeSupport(ws): boolean
    properties: query
    Returns true if this translator supports write operations.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/translator.html 
    """


def treeLister(flagaddFavorite: string, flagaddItem: tuple[string, string, script], flagaddVnnItem: tuple[string, string, string, string], flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagclearContents: boolean, flagcollapsePath: string, flagdefineTemplate: string, flagdisplayName: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexecuteItem: string, flagexists: boolean, flagexpandPath: string, flagexpandToDepth: int, flagfavoritesCallback: script, flagfavoritesList: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagitemScript: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrefreshCommand: script, flagremoveFavorite: string, flagremoveItem: string, flagresultsPathUnderCursor: boolean, flagselectPath: string, flagsetDisplayName: tuple[string, string], flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagvnnString: boolean, flagwidth: int) -> string:
    """Synopsis:
---
---
 treeLister(
[string]
    , [addFavorite=string], [addItem=[string, string, script]], [addVnnItem=[string, string, string, string]], [annotation=string], [backgroundColor=[float, float, float]], [clearContents=boolean], [collapsePath=string], [defineTemplate=string], [displayName=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [executeItem=string], [exists=boolean], [expandPath=string], [expandToDepth=int], [favoritesCallback=script], [favoritesList=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [itemScript=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [refreshCommand=script], [removeFavorite=string], [removeItem=string], [resultsPathUnderCursor=boolean], [selectPath=string], [setDisplayName=[string, string]], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [vnnString=boolean], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

treeLister is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

w = cmds.window(width=200)
fl = cmds.formLayout()
tl = cmds.treeLister()
cmds.formLayout(fl, e=True,
                af=((tl, 'top', 0),
                    (tl, 'left', 0),
                    (tl, 'bottom', 0),
                    (tl, 'right', 0)))
cmds.showWindow(w)
items=['root/branchone/leafone',
       'root/branchone/leaftwo',
       'root/branchtwo/leafthree']
cmds.treeLister(tl, e=True, add=[(i, 'sphere.png', cmds.sphere) for i in items])

---
Return:
---


    string: The name of the created control.

Flags:
---


---
addFavorite(af): string
    properties: create, edit, multiuse
    Add an item path to the favorites folder.  The item path does not have to actually be in the tree.

---
addItem(add): [string, string, script]
    properties: create, edit, multiuse
    Add an item to the control.  The arguments are item-path,icon path,command
where item-path is the path from the root of the tree to the item's name
icon path is the icon displayed in the results list
command is the script which is executed when the item is LMB clicked

---
addVnnItem(avi): [string, string, string, string]
    properties: create, edit, multiuse
    Add a VNN (Virtual Node Network) item to the control.  The arguments are:
item-path, icon-path, vnn-string, vnn-action.
Where item-path is the path from the root of the tree to the item's name,
icon-path is the icon displayed in the results list,
vnn-string is used for drag data when MMB dragging the item
and vnn-action is the script which is executed when the item is LMB clicked.
The vnn-string should be comprised of: 'VNN runtime,VNN library,VNN node',
where the VNN library can contain sub-libraries, using / to separate.

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
clearContents(clr): boolean
    properties: edit
    Clears the contents of the control.

---
collapsePath(cp): string
    properties: edit, multiuse
    Collapse a path in the tree.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
displayName(dn) 2024.1: string
    properties: query
    Query the display name of a given item.

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
executeItem(ei): string
    properties: edit
    Execute the command associated with an item.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
expandPath(ep): string
    properties: edit, multiuse
    Expand a path in the tree.

---
expandToDepth(etd): int
    properties: edit
    Expand the tree to the given depth.

---
favoritesCallback(fcb): script
    properties: create, edit
    This script is called whenever a favorite is added or removed.
It is passed two arguments: The item's path and a boolean indicating if it
is being added to favorites (True) or removed (False).

---
favoritesList(fl): boolean
    properties: query
    Returns the list of favorite items.

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
itemScript(isc): string
    properties: query
    Returns the language and script command of the passed item path as a
two-element list, the first element is the string "MEL" or "Python" and
the second is the command script. Note that items with Python callable
commands will be returned as strings.
      In query mode, this flag needs a value.

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
refreshCommand(rc): script
    properties: create, query, edit
    Command executed when the refresh button is pressed.  Note: by default the
refresh button is hidden and will be shown automatically when this command
script is attached.

---
removeFavorite(rf): string
    properties: edit, multiuse
    Remove an item from favorites.  Accepts the full favorite path or the tail of the full path.

---
removeItem(rem): string
    properties: edit, multiuse
    Remove an item path.

---
resultsPathUnderCursor(ruc): boolean
    properties: query
    Returns the path to the result (right-pane) item under the mouse cursor.
Returns an empty string if there is no such item.

---
selectPath(sp): string
    properties: edit, multiuse
    Select a path in the tree.

---
setDisplayName(sdn) 2024.1: [string, string]
    properties: edit, multiuse
    Edit the displayed name of a given item.

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
vnnString(vnn): boolean
    properties: query
    Returns the VNN (Virtual Node Network) string of the passed item path.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/treeLister.html 
    """


def treeView(flagaddItem: tuple[string, string], flagallowDragAndDrop: boolean, flagallowHiddenParents: boolean, flagallowMultiSelection: boolean, flagallowReparenting: boolean, flagannotation: string, flagattachButtonRight: int, flagbackgroundColor: tuple[float, float, float], flagborderHighlite: tuple[string, boolean], flagborderHighliteColor: tuple[string, float, float, float], flagbuttonErase: tuple[string, boolean], flagbuttonState: tuple[string, int, string], flagbuttonStyle: tuple[string, int, string], flagbuttonTextIcon: tuple[string, int, string], flagbuttonTooltip: tuple[string, int, string], flagbuttonTransparencyColor: tuple[string, int, float, float, float], flagbuttonTransparencyOverride: tuple[string, int, boolean], flagbuttonVisible: tuple[string, int, boolean], flagchildren: string, flagclearSelection: boolean, flagcontextMenuCommand: script, flagdefineTemplate: string, flagdisplayLabel: tuple[string, string], flagdisplayLabelSuffix: tuple[string, string], flagdocTag: string, flagdragAndDropCommand: script, flagdragCallback: script, flagdropCallback: script, flageditLabelCommand: script, flagenable: boolean, flagenableBackground: boolean, flagenableButton: tuple[string, int, int], flagenableKeyboardFocus: boolean, flagenableKeys: boolean, flagenableLabel: tuple[string, int], flagexists: boolean, flagexpandCollapseCommand: script, flagexpandItem: tuple[string, boolean], flagflatButton: int, flagfont: tuple[string, string], flagfontFace: tuple[string, int], flagfullPathName: boolean, flagheight: int, flaghideButtons: boolean, flaghighlightColor: tuple[float, float, float], flaghighlite: tuple[string, boolean], flaghighliteColor: tuple[string, float, float, float], flagignoreButtonClick: tuple[string, int, int], flagimage: tuple[string, int, string], flaginsertItem: tuple[string, string, int], flagisItemExpanded: string, flagisLeaf: string, flagisObscured: boolean, flagitem: string, flagitemAnnotation: tuple[string, string], flagitemDblClickCommand: script, flagitemDblClickCommand2: script, flagitemExists: string, flagitemIndex: string, flagitemParent: string, flagitemRenamedCommand: script, flagitemSelected: string, flagitemVisible: tuple[string, boolean], flaglabelBackgroundColor: tuple[string, float, float, float], flagmanage: boolean, flagnoBackground: boolean, flagnumberOfButtons: int, flagnumberOfPopupMenus: boolean, flagornament: tuple[string, int, int, int], flagornamentColor: tuple[string, float, float, float], flagparent: string, flagpopupMenuArray: boolean, flagpressCommand: tuple[int, script], flagpreventOverride: boolean, flagremoveAll: boolean, flagremoveItem: string, flagreverseTreeOrder: boolean, flagrightPressCommand: tuple[int, script], flagselect: tuple[string, int], flagselectCommand: script, flagselectItem: tuple[string, boolean], flagselectionChangedCommand: script, flagselectionColor: tuple[string, float, float, float], flagshowItem: string, flagstatusBarMessage: string, flagtextColor: tuple[string, float, float, float], flaguseTemplate: string, flagverticalScrollPosition: int, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 treeView(
[string]
    , [addItem=[string, string]], [allowDragAndDrop=boolean], [allowHiddenParents=boolean], [allowMultiSelection=boolean], [allowReparenting=boolean], [annotation=string], [attachButtonRight=int], [backgroundColor=[float, float, float]], [borderHighlite=[string, boolean]], [borderHighliteColor=[string, float, float, float]], [buttonErase=[string, boolean]], [buttonState=[string, int, string]], [buttonStyle=[string, int, string]], [buttonTextIcon=[string, int, string]], [buttonTooltip=[string, int, string]], [buttonTransparencyColor=[string, int, float, float, float]], [buttonTransparencyOverride=[string, int, boolean]], [buttonVisible=[string, int, boolean]], [children=string], [clearSelection=boolean], [contextMenuCommand=script], [defineTemplate=string], [displayLabel=[string, string]], [displayLabelSuffix=[string, string]], [docTag=string], [dragAndDropCommand=script], [dragCallback=script], [dropCallback=script], [editLabelCommand=script], [enable=boolean], [enableBackground=boolean], [enableButton=[string, int, int]], [enableKeyboardFocus=boolean], [enableKeys=boolean], [enableLabel=[string, int]], [exists=boolean], [expandCollapseCommand=script], [expandItem=[string, boolean]], [flatButton=int], [font=[string, string]], [fontFace=[string, int]], [fullPathName=boolean], [height=int], [hideButtons=boolean], [highlightColor=[float, float, float]], [highlite=[string, boolean]], [highliteColor=[string, float, float, float]], [ignoreButtonClick=[string, int, int]], [image=[string, int, string]], [insertItem=[string, string, int]], [isItemExpanded=string], [isLeaf=string], [isObscured=boolean], [item=string], [itemAnnotation=[string, string]], [itemDblClickCommand=script], [itemDblClickCommand2=script], [itemExists=string], [itemIndex=string], [itemParent=string], [itemRenamedCommand=script], [itemSelected=string], [itemVisible=[string, boolean]], [labelBackgroundColor=[string, float, float, float]], [manage=boolean], [noBackground=boolean], [numberOfButtons=int], [numberOfPopupMenus=boolean], [ornament=[string, int, int, int]], [ornamentColor=[string, float, float, float]], [parent=string], [popupMenuArray=boolean], [pressCommand=[int, script]], [preventOverride=boolean], [removeAll=boolean], [removeItem=string], [reverseTreeOrder=boolean], [rightPressCommand=[int, script]], [select=[string, int]], [selectCommand=script], [selectItem=[string, boolean]], [selectionChangedCommand=script], [selectionColor=[string, float, float, float]], [showItem=string], [statusBarMessage=string], [textColor=[string, float, float, float]], [useTemplate=string], [verticalScrollPosition=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

treeView is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

def selectTreeCallBack(*args):
  print 'selection :- str= ' + args[0] + ' onoff= ' + str(args[1])
  return True

def pressTreeCallBack(*args):
  print 'press :- str= ' + args[0] + ' onoff= ' + str(args[1])

from maya import cmds
window = cmds.window()
layout = cmds.formLayout()

control = cmds.treeView( parent = layout, numberOfButtons = 3, abr = False )

cmds.formLayout(layout,e=True, attachForm=(control,'top', 2))
cmds.formLayout(layout,e=True, attachForm=(control,'left', 2))
cmds.formLayout(layout,e=True, attachForm=(control,'bottom', 2))
cmds.formLayout(layout,e=True, attachForm=(control,'right', 2))

cmds.showWindow( window )

cmds.treeView( control, e=True, addItem = ("layer 1", ""))
cmds.treeView( control, e=True, addItem = ("layer 2", ""))
cmds.treeView( control, e=True, addItem = ("layer 3", ""))
cmds.treeView( control, e=True, addItem = ("layer 4", ""))
cmds.treeView( control, e=True, addItem = ("layer 5", ""))
cmds.treeView( control, e=True, addItem = ("layer 6", ""))
cmds.treeView( control, e=True, addItem = ("layer 7", "layer 2"))
cmds.treeView( control, e=True, addItem = ("layer 8", "layer 2"))
cmds.treeView( control, e=True, addItem = ("layer 9", "layer 2"))
cmds.treeView( control, e=True, addItem = ("layer 10", "layer 8"))
cmds.treeView( control, e=True, addItem = ("layer 11", "layer 2"))
cmds.treeView( control, e=True, addItem = ("layer 12", ""))
cmds.treeView( control, e=True, addItem = ("layer 13", "layer 10"))
cmds.treeView(control,edit=True,pressCommand=[(1,pressTreeCallBack),(2,pressTreeCallBack),(3,pressTreeCallBack)])
cmds.treeView(control,edit=True,selectCommand=selectTreeCallBack)


cmds.treeView( control, edit=True, removeAll = True )

---
Return:
---


    string: The full name of the control.

Flags:
---


---
addItem(ai): [string, string]
    properties: create, edit, multiuse
    Adds a tree view item to the tree view.
First argument specifies the item's name, second argument specifies the item's parent (use an empty string to have it at the top level of the tree)

---
allowDragAndDrop(adr): boolean
    properties: create, query, edit
    Allow the user to perform drag and drop of treeView items.  If enabled,
re-ordering / re-parenting operations can be perfomed with the middle mouse button.
This flag takes precendence over other drag and drop related flags.
Defaults to true.

---
allowHiddenParents(ahp): boolean
    properties: create, query, edit
    If not cleared(default), the treeView will make parent nodes of visible nodes automatically visible

---
allowMultiSelection(ams): boolean
    properties: create, query, edit
    Specify multi or single selection mode.
Allow the user to perform multiple selection by holding
ctrl or shift key while selecting items of treeView items.
Defaults to true.

---
allowReparenting(arp): boolean
    properties: create, query, edit
    Allow the user to reparent items in the tree view using the middle
mouse button. Defaults to true. If false, user can still reorder items
within a group using the middle mouse button.

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
attachButtonRight(abr): int
    properties: create, edit
    Sets tree view item's buttons to appear on the right or left.
Argument specifies if they are to be attached to the right, if it is set to false they will attach on the left.

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
borderHighlite(bh): [string, boolean]
    properties: create, edit
    Sets an item's border as highlit or not.
First Argument specifies item, second argument specifies on or off.

---
borderHighliteColor(bcl): [string, float, float, float]
    properties: create, edit
    Sets the color an item's border highlite will turn when highlite is enabled.
first parameter specifies layer
three float values specify RGB values, between 0 and 1.

---
buttonErase(bef): [string, boolean]
    properties: create, query, edit, multiuse
    If buttonErase was set true , then even if the button of the treeView item  is set invisible , the treeView will still erase the buttonRect of this treeView item with background .
First argument is the item name, second argument is whether buttonErase was set true or false

---
buttonState(bst): [string, int, string]
    properties: create, edit, multiuse
    Sets the state of a button.
First argument specifies the layer, second argument specifies which button, third argument specifies the state
Possible states:
"buttonUp" - button is up
"buttonDown" - button is down
"buttonThirdState" - button is in state three (used by the "3StateButton" button style)

---
buttonStyle(bs): [string, int, string]
    properties: create, edit, multiuse
    Sets the type of button, used to indicate possible states and if the button is reset upon release.
First argument specifies the layer, second argument specifies which button, third argument specifies the type of button
Possible button types:
"pushButton" - two possible states, button is reset to up upon release
"2StateButton" - two possible states, button changes state on click
"3StateButton" - three button states, button changes state on click

---
buttonTextIcon(bti): [string, int, string]
    properties: create, edit, multiuse
    Sets a one letter text to use as the icon to use for a specific button on a specific item.
First argument specifies the item, second argument specifies the button, third argument specifies the icon text.

---
buttonTooltip(btp): [string, int, string]
    properties: create, edit, multiuse
    Sets a tooltip for specific button on a specific item.
First argument specifies the item, second argument specifies the button, third argument specifies the tooltip.

---
buttonTransparencyColor(btc): [string, int, float, float, float]
    properties: create, edit, multiuse
    Sets the background color of a button that will be used if buttonTransparencyOverride is enabled.
First argument specifies item, second argument specifies button,
three floats specify RGB values, between 0 and 1.

---
buttonTransparencyOverride(bto): [string, int, boolean]
    properties: create, edit, multiuse
    Sets a button's background as being overridden or not.
First argument specifies item, second argument specifies button, third argument specifies overridden or not.

---
buttonVisible(bvf): [string, int, boolean]
    properties: create, multiuse
    Sets a button as visible or not.
First Argument specifies item.
Second Argument specifies a button.
Third Argument specifies visible or not.

---
children(ch): string
    properties: query
    Query the children of an item. If the argument is null, all items will be returned.
      In query mode, this flag needs a value.

---
clearSelection(cs): boolean
    properties: create, edit
    Clears all selected items.

---
contextMenuCommand(cmc): script
    properties: create, edit
    Set the callback function to be invoked just before any attached context
menu is shown. This can be used as a replacement to, or in addition to the
postMenuCommand flag on the popupMenu command. The function should accept
a string which will be the item that was clicked on (empty if no item was hit).
The function should return true if the menu should be shown, false otherwise.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
displayLabel(dl): [string, string]
    properties: create, edit, multiuse
    Set a label for the item that is different than the
string that identifies the item. This label will be used in the
display of the item. The first parameter specifies
the item, the second specifies the display label.

---
displayLabelSuffix(dls): [string, string]
    properties: create, edit, multiuse
    Set a suffix for the display label for the item. This suffix will
not be shown when renaming the item in the tree view.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
dragAndDropCommand(dad): script
    properties: create, edit
    Sets the callback function to be invoked upon drag and drop of layers.
the callback function should take as parameters:
- a string array of the dropped items
- a string array of the items previous parents
- an integer array of the items previous indexes
- a string for the item(s) new parent
- an integer array for the item's new indexes
- a string for the item that now comes before the dropped items
- a string for the item that now comes after the dropped items

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
editLabelCommand(elc): script
    properties: create, edit
    Set the callback function to be invoked when the user changes
the name of an item by double clicking it in the UI. The callback should
accept two string arguments: the item name and the new name. The item
name refers to the name of the item and not the display label. The callback
function should return a string. An empty string indicates that the rename
operation was invalid and the control should revert to the original name.
If the rename operation is valid the callback should return a string that
identifies the item, possibly different from the new display name entered
by the user.

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
enableButton(eb): [string, int, int]
    properties: create, edit, multiuse
    Sets a specific button on a specific item to being usable or not.
First argument specifies the item, second argument specifies the button, third argument specifies on or off.

---
enableKeyboardFocus(ekf): boolean
    properties: create, query, edit
    If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.
This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.
If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).

---
enableKeys(enk): boolean
    properties: edit
    By default the treeview does not accept input from the keyboard.  By enabling keyboard support
The treeview will support up/down navigation using the up/down arrow keys.

---
enableLabel(enl): [string, int]
    properties: create, edit
    enables or disables the label of a tree view item from being displayed. The first parameter specifies
the item, the second specifies on or off.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
expandCollapseCommand(ecc): script
    properties: create, edit
    Set the callback function to be invoked upon hitting the expand/collapse button.
The function should take as parameters:
- a string for the item for which the expand/collapse button was hit
- an integer for the state of expansion

---
expandItem(ei): [string, boolean]
    properties: create, edit
    Expands or collapses an item's children.
First argument specifies the item, second argument specifies expanded or collapsed.

---
flatButton(fb): int
    properties: create, query, edit
    Type of flat button to use.

---
font(fn): [string, string]
    properties: create, query, edit
    The first parameter specifies the item string for
the TtreeViewNode in the TtreeNodeMap.
The second string specifies the font for the text.
Valid values are
"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
"smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".

---
fontFace(ff): [string, int]
    properties: create, edit
    Sets the font face used for the specified item's text:
0 for normal,
1 for bold,
2 for italic.

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
hideButtons(hb): boolean
    properties: create, edit
    Hides the buttons for an item in the tree view. Can only be used when
adding the item to the tree with the "addItem" flag. Space for the buttons
is left to make sure items still line up correctly under their parent.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
highlite(hl): [string, boolean]
    properties: create, edit
    Sets an item as highlit. Highliting is shown by outlining the item.
First parameter specifies the item, the second specifies the highliting
or not.

---
highliteColor(hc): [string, float, float, float]
    properties: create, edit
    Sets the color an item's highlite will turn when highlite is enabled.
first parameter specifies layer
three float values specify RGB values, between 0 and 1.

---
ignoreButtonClick(ibc): [string, int, int]
    properties: create, edit, multiuse
    Sets a specific button on a specific item to ignore the button clicks
First argument specifies the item ,second argument specifies the button, third argument specifies on or off

---
image(i): [string, int, string]
    properties: create, edit, multiuse
    Sets an image to use as the icon for the button.
First argument specifies the item, second argument specifies the button, third argument specifies the image.

---
insertItem(ii): [string, string, int]
    properties: create, edit, multiuse
    Create and insert a tree view item to the tree view.
First argument specifies the item's name, second argument specifies the item's parent (use an empty string to have it at the top level of the tree), third argument is the child's index position in the children list.  An index less than or equal to 0 inserts as the first child, greater than or equal to the number of children inserts as last child.

---
isItemExpanded(iie): string
    properties: query
    Is the item in the tree view expanded.
      In query mode, this flag needs a value.

---
isLeaf(il): string
    properties: query
    Query whether an item is a leaf.
      In query mode, this flag needs a value.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
item(it): string
    properties: query
    Specify the item to query. Used with the flag "selectionColor" and "itemAnnotation".
      In query mode, this flag needs a value.

---
itemAnnotation(ia): [string, string]
    properties: create, query, edit
    Annotate the specified item with an extra string value.
When used for query, this flag has no argument and needs to be used with the
flag "item".

---
itemDblClickCommand(idc): script
    properties: create, edit
    Set the callback function to be invoked when an item in the tree has been
double clicked. The callback should accept one string, the display label of the
item that was double clicked. If this callback is defined, it supersedes
the normal item renaming behavior.

---
itemDblClickCommand2(dc2): script
    properties: create, edit
    Set the callback function to be invoked when an item in the tree has been
double clicked. This callback is similar to itemDblClickCommand(idc), but it accepts two strings:
the name and the display label of the item that was double clicked. If this callback is defined,
it supersedes the normal item renaming behavior

---
itemExists(iex): string
    properties: create, query
    Queries the existence of the specified Tree View item.
      In query mode, this flag needs a value.

---
itemIndex(idx): string
    properties: create, query
    Get the index for the specified item in the list of children of the item's
parent. Index is 0-based.
      In query mode, this flag needs a value.

---
itemParent(ip): string
    properties: create, query
    If the specified item is a child, it returns the parent item. If the specified item is not a child it returns nothing.
      In query mode, this flag needs a value.

---
itemRenamedCommand(irc): script
    properties: create, edit
    Set the callback function to be invoked when an item in the tree has been
renamed. This occurs if there is a successful return of the command attached
by "editLabelCommand" or unconditionally if there is no editLabelCommand.
The callback should accept two strings, the old name and the new name of the
item that was renamed.

---
itemSelected(isl): string
    properties: query
    Queries the item is currently selected or not.
      In query mode, this flag needs a value.

---
itemVisible(iv): [string, boolean]
    properties: create, query, edit
    Control the given item's visibility.

---
labelBackgroundColor(lbc): [string, float, float, float]
    properties: create, edit
    Set the background color for text label for a particular item
in the tree. The first parameter specifies layer.
Set (-1.0, -1.0, -1.0) to restore the background
to the default of "transparent"

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
numberOfButtons(nb): int
    properties: create, edit
    Specifies the number of buttons for items in the tree.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
ornament(ornament): [string, int, int, int]
    properties: create, edit
    Sets an item as having an ornament (a small colored circle), its on/off state, if it should have a dot, and its size.
First Argument specifies item,
second argument specifies on or off,
third argument specifies dotted or not,
fourth argument specifies radius (in pixels).

---
ornamentColor(orc): [string, float, float, float]
    properties: create, edit
    Sets the color an ornament will be draw with for the specified layer.

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
pressCommand(pc): [int, script]
    properties: create, edit, multiuse
    Sets the callback function to be invoked upon clicking a treeView button.
First argument specifies which treeView button.
Second argument specifies the callback function to be executed
the callback function should take as parameters:
- a string for the clicked button's item
- an int for the clicked button's state

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
removeAll(ra): boolean
    properties: create, edit
    Removes all items from the tree view.

---
removeItem(ri): string
    properties: create, edit
    Removes a tree view item from the tree view. If this item has children items, all children items are removed.
First argument specifies the item's name.

---
reverseTreeOrder(rto): boolean
    properties: create, edit
    Controls the order the tree will be drawn in (reversed if true).

---
rightPressCommand(rpc): [int, script]
    properties: create, edit, multiuse
    Sets the callback function to be invoked upon right clicking a treeView button.
First argument specifies which treeView button.
Second argument specifies the callback function to be executed
the callback function should take as parameters:
- a string for the clicked button's item
- an int for the clicked button's state

---
select(sl): [string, int]
    properties: create, edit
    Set selection on an element. The first parameter specifies the item, the second specifies on or off.

---
selectCommand(sc): script
    properties: create, edit
    Set the callback function to be invoked when an item is selected or deselected
in the tree. The function should accept one string argument and
one integer argument: the item name and the select state respectively. If the
function returns true, the select/deselect is considered valid and will
occur normally, otherwise it will be disallowed.
name and

---
selectItem(si): [string, boolean]
    properties: create, query, edit
    Sets an item's selected state.
first argument specifies the item, second argument specifies selection status.
When used for query without arguments, return all selected items in the treeview.

---
selectionChangedCommand(scc): script
    properties: create, edit
    Set the callback function to be invoked when a complete selection operation
triggered by the user has occurred successfully. The callback is invoked if
the "selectCommand" callback has returned a non-empty value (or always there
is no "selectCommand" callback). This differs from selectCommand in that a
simple selection replacement will generate two callbacks with "selectCommand"
(one for deselect of the old item and one for select of the new), whereas
"selectionChangedCommand" will only be invoked once, after the selection is
complete. The callback is not passed any parameters and does not need to
return any value (i.e. It is simply a notification mechanism).

---
selectionColor(scl): [string, float, float, float]
    properties: create, query, edit
    Sets the color an item will turn to indicate that it is selected.
first parameter specifies the item
three float values specify RGB values, between 0 and 1.
When used for query, this flag has no argument and needs to be used with the
flag "item". It returns the color an item will become if it is selected.

---
showItem(shi): string
    properties: create, edit
    Show the  item. Scroll the list as necessary so that item is visible.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
textColor(tc): [string, float, float, float]
    properties: create, edit
    Sets the label's text color for the specified layer.
first argument specifies layer.
three float values specify RGB values, between 0 and 1.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
verticalScrollPosition(vsp): int
    properties: create, query, edit
    The position of the vertical scrollbar.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/treeView.html 
    """


def trim(flagcaching: boolean, flagconstructionHistory: boolean, flaglocatorU: float, flaglocatorV: float, flagname: string, flagnodeState: int, flagobject: boolean, flagselected: int, flagshrink: boolean, flagtolerance: linear) -> list[string]:
    """Synopsis:
---
---
 trim(
objects
    , [caching=boolean], [constructionHistory=boolean], [locatorU=float], [locatorV=float], [name=string], [nodeState=int], [object=boolean], [selected=int], [shrink=boolean], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

trim is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Keep all selected regions
cmds.trim( sl=0 )

Discard all selected regions
cmds.trim( sl=1 )

shrink the underlying surface to just outside the
outermost boundary curve
cmds.trim( sh=1 )

---
Return:
---


    list[string]: Object name and node name.

Flags:
---


---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
locatorU(lu): float
    properties: create, query, edit, multiuse
    u parameter value to position a locator on the surface.
Default: 0.5

---
locatorV(lv): float
    properties: create, query, edit, multiuse
    v parameter value to position a locator on the surface.
Default: 0.5

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
selected(sl): int
    properties: create, query, edit
    Specify whether to keep or discard selected regions.
Default: 0

---
shrink(sh): boolean
    properties: create, query, edit
    If true, shrink underlying surface to outer boundaries of trimmed surface.
Default: false

---
tolerance(tol): linear
    properties: create, query, edit
    The tolerance with which to trim.
Default: 0.001

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/trim.html 
    """


def truncateFluidCache() -> None:
    """Synopsis:
---
---
 truncateFluidCache()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

truncateFluidCache is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Truncate a fluid cache that has a start time of 1
and an end time of 25 so that only the first 10
frames are preserved and the end time of the
cache is set to 10.
---

cmds.currentTime( 10 )
cmds.truncateFluidCache()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/truncateFluidCache.html 
    """


def truncateHairCache() -> None:
    """Synopsis:
---
---
 truncateHairCache()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

truncateHairCache is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Truncate a hair cache that has a start time of 1
and an end time of 25 so that only the first 10
frames are preserved and the end time of the
cache is set to 10.
---

cmds.currentTime( 10 )
cmds.truncateHairCache()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/truncateHairCache.html 
    """


def tumble(flagazimuthAngle: angle, flagelevationAngle: angle, flaglocalTumble: int, flagpivotPoint: tuple[linear, linear, linear], flagrotationAngles: tuple[angle, angle]) -> None:
    """Synopsis:
---
---
 tumble(
[camera]
    , [azimuthAngle=angle], [elevationAngle=angle], [localTumble=int], [pivotPoint=[linear, linear, linear]], [rotationAngles=[angle, angle]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

tumble is undoable, NOT queryable, and NOT editable.

When no camera name is supplied, this command is applied to the
camera in the active view. 

The camera's rotate pivot will override a specified pivot point if
the rotate pivot is not at the camera's eye point. 




Example:
---
import maya.cmds as cmds

cmds.camera()
cmds.tumble( 'cameraShape1', aa=-30 )To change the azimuth angle

cmds.tumble( 'cameraShape1', ea=15 )To change the elevation angle

cmds.tumble( ra=(-30, 15) )To change the azimuth angle and the elevation angle

---


Flags:
---


---
azimuthAngle(aa): angle
    properties: create
    Degrees to change the azimuth angle.

---
elevationAngle(ea): angle
    properties: create
    Degrees to change the elevation angle.

---
localTumble(lt): int
    properties: create
    Describes what point the camera will tumble around:
0 for the camera's tumble pivot,
1 for the camera's center of interest, and
2 for the camera's local axis, offset by its tumble pivot.

---
pivotPoint(pp): [linear, linear, linear]
    properties: create
    Three dimensional point used as the pivot point in the world
space.

---
rotationAngles(ra): [angle, angle]
    properties: create
    Two values in degrees to change the azimuth and elevation
angles.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/tumble.html 
    """


def tumbleCtx(flagalternateContext: boolean, flagautoOrthoConstrain: boolean, flagautoSetPivot: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglocalTumble: int, flagname: string, flagobjectTumble: boolean, flagorthoLock: boolean, flagorthoStep: angle, flagtoolName: string, flagtumbleScale: float) -> string:
    """Synopsis:
---
---
 tumbleCtx([alternateContext=boolean], [autoOrthoConstrain=boolean], [autoSetPivot=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [localTumble=int], [name=string], [objectTumble=boolean], [orthoLock=boolean], [orthoStep=angle], [toolName=string], [tumbleScale=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

tumbleCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.tumbleCtx( 'tumbleContext', ts=1.0, lt=False, ac=False, ol=True )

---
Return:
---


    string: The name of the context

Flags:
---


---
alternateContext(ac): boolean
    properties: create, query
    Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.

---
autoOrthoConstrain(aoc): boolean
    properties: create, query, edit
    Automatically constrain horizontal and vertical rotations when
the camera is orthographic. The shift key can be used to
unconstrain the rotation.

---
autoSetPivot(asp): boolean
    properties: create, query, edit
    Automatically set the camera pivot to the selection or tool effect region

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
localTumble(lt): int
    properties: create, query, edit
    Describes what point the camera will tumble around:

0 for the camera's tumble pivot
1 for the camera's center of interest
2 for the camera's local axis, offset by its tumble pivot

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
objectTumble(ot): boolean
    properties: create, query, edit
    Make the camera tumble around the selected object, if true.

---
orthoLock(ol): boolean
    properties: create, query, edit
    Orthographic cameras cannot be tumbled while orthoLock is on.

---
orthoStep(os): angle
    properties: create, query, edit
    Specify the angular step in degrees for orthographic
rotation. If camera is orthographic and autoOrthoConstrain is
toggled on the rotation will be stepped by this amount.

---
toolName(tn): string
    properties: create, query
    Name of the specific tool to which this command refers.

---
tumbleScale(ts): float
    properties: create, query, edit
    Set the rotation speed. A tumble scale of 1.0 will result in
in 40 degrees of rotation per 100 pixels of cursor drag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/tumbleCtx.html 
    """


def turbulence(flagattenuation: float, flagfrequency: float, flagmagnitude: float, flagmaxDistance: linear, flagname: string, flagnoiseLevel: int, flagnoiseRatio: float, flagperVertex: boolean, flagphase: float, flagphaseX: float, flagphaseY: float, flagphaseZ: float, flagposition: tuple[linear, linear, linear], flagtorusSectionRadius: linear, flagvolumeExclusion: boolean, flagvolumeOffset: tuple[linear, linear, linear], flagvolumeShape: string, flagvolumeSweep: angle) -> string:
    """Synopsis:
---
---
 turbulence(
selectionList
    , [attenuation=float], [frequency=float], [magnitude=float], [maxDistance=linear], [name=string], [noiseLevel=int], [noiseRatio=float], [perVertex=boolean], [phase=float], [phaseX=float], [phaseY=float], [phaseZ=float], [position=[linear, linear, linear]], [torusSectionRadius=linear], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

turbulence is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
A turbulence field causes irregularities (also called 'noise' or
'jitter') in the motion of affected objects.

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

Creates a new field
cmds.turbulence( n='turbulenceF', m=5.0, pos=(0.25, 0, 0) )

Edits the frequency value of the field named turbulenceF
cmds.turbulence( 'turbulenceF', e=True, f=0.5 )

Queries turbulenceF for its frequency value
cmds.turbulence( 'turbulenceF', q=True, f=1 )

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
frequency(f): float
    properties: query, edit
    Frequency of turbulence field. This determines how often
motion is disrupted.

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
noiseLevel(nsl): int
    properties: query, edit
    If the noiseLevel parameter is greater than zero, the field
will do multiple lookups in the table.  Each additional lookup is
weighted using noiseRatio (which see).  The noiseLevel is the
number of additional lookups, so if noiseLevel is 0, there is just
one lookup.  A value of 0 (the default) corresponds to the way
the field behaved prior to Maya 3.0.

---
noiseRatio(nsr): float
    properties: query, edit
    If noiseLevel is greater than zero, then noiseRatio is
the relative magnitude for each consecutive noise evaluation.
These are cumulative: for example, if noiseRatio is 0.5, then
the first evaluation is weighted 0.5, the second 0.25, and so on.
Has no effect if noiseLevel is zero.

---
perVertex(pv): boolean
    properties: query, edit
    Per-vertex application. If this flag is set true, then each
individual point (CV, particle, vertex,etc.) of the chosen object
exerts an identical copy of the force field. If this flag is set to
false, then the froce is exerted only from the geometric center of
the set of points.

---
phase(p): float
    properties: query, edit
    Phase shift of turbulence field. This influences the direction
of the disruption.  This flag is obsolete and is retained only
for backward compatibility.  It is replaced by -phaseX, -phaseY, and
-phaseZ.  Setting -phase is identical to setting -phaseZ (the
phase shift was always in the Z dimension).

---
phaseX(px): float
    properties: query, edit
    X component of phase shift of turbulence field. This influences
the direction of the disruption.

---
phaseY(py): float
    properties: query, edit
    Y component of phase shift of turbulence field. This influences
the direction of the disruption.

---
phaseZ(pz): float
    properties: query, edit
    Z component of phase shift of turbulence field. This influences
the direction of the disruption.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/turbulence.html 
    """


def twoPointArcCtx(flagdegree: uint, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagspans: uint) -> string:
    """Synopsis:
---
---
 twoPointArcCtx([degree=uint], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [spans=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

twoPointArcCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To create a new context that will create curves of degree 1:
cmds.twoPointArcCtx( degree=1 )

To query the degree of an existing context:
cmds.twoPointArcCtx( 'arcContext1', q=True, degree=True )

---
Return:
---


    string: Name of the new context

Flags:
---


---
degree(d): uint
    properties: create, query, edit
    Valid values are 1 or 3. Default degree 3.

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
spans(s): uint
    properties: create, query, edit
    Default is 4.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/twoPointArcCtx.html 
    """
