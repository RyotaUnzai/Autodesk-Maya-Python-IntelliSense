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


def falloffCurve(flagaddControlVertex: string, flagannotation: string, flagasString: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcurrentKey: int, flagcurrentKeyValue: tuple[float, float], flagcustomCurveWidget: boolean, flagdefineTemplate: string, flagdeleteControlVertex: int, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagoptionVar: string, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagreadOnly: boolean, flagsnapToGrid: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 falloffCurve(
[string]
    , [addControlVertex=string], [annotation=string], [asString=string], [backgroundColor=[float, float, float]], [changeCommand=script], [currentKey=int], [currentKeyValue=[float, float]], [customCurveWidget=boolean], [defineTemplate=string], [deleteControlVertex=int], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [optionVar=string], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [readOnly=boolean], [snapToGrid=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

falloffCurve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a window with a curve control for an optionVar
---

cmds.window( title='Curve Control For OptionVar' )
cmds.optionVar(stringValueAppend=['falloffCurveOptionVar', '0,1'])
cmds.optionVar(stringValueAppend=['falloffCurveOptionVar', '0.5,1'])
cmds.optionVar(stringValueAppend=['falloffCurveOptionVar', '0.5,0'])
cmds.optionVar(stringValueAppend=['falloffCurveOptionVar', '1,0'])
cmds.columnLayout()
cmds.falloffCurve( 'fCurve', h=200)
cmds.falloffCurve( 'fCurve', e=True, optionVar='falloffCurveOptionVar' )
cmds.showWindow()

Query for the control vertices' values of the curve.
---

cmds.falloffCurve( 'fCurve', q=True, asString=True )

---
Return:
---


    string: The name of the port created or modified

Flags:
---


---
addControlVertex(acv): string
    properties: edit
    Used to add a control vertex for the curve.

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
asString(asString): string
    properties: query, edit
    Used to query and set the value of the curve as a string of comma
separated values

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
    properties: edit
    Specifies a command to be executed whenever the value of this curve
is modified. This option should not be used when specifying an
optionVar.

---
currentKey(ck): int
    properties: create, query, edit
    Returns the index of the currently selected key.

---
currentKeyValue(ckv): [float, float]
    properties: query, edit
    Get or set the value of the currently selected key.

---
customCurveWidget(ccw): boolean
    properties: create, query, edit
    Determines whether or not the curve widget is using a custom curve. When a custom curve is used, it is stored by a falloff curve in the brush tool settings, and the flag should be true.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deleteControlVertex(dcv): int
    properties: edit
    Used to delete a control vertex of the curve.

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
optionVar(ov): string
    properties: create, query, edit
    Specifies the name of the option var used to store and
retrieve the string value capturing the curve.

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
readOnly(ro): boolean
    properties: create, query, edit
    Specifies if the curve is read only or not. If true, the curve can't be edited.

---
snapToGrid(stg): boolean
    properties: create, query, edit
    Specifies whether or not curve control points snap to grid when they are being moved.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/falloffCurve.html 
    """


def falloffCurveAttr(flagaddControlVertex: string, flagannotation: string, flagasString: string, flagattribute: name, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcurrentKey: int, flagcurrentKeyValue: tuple[float, float], flagcustomCurveWidget: int, flagdefineTemplate: string, flagdeleteControlVertex: int, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagreadOnly: int, flagselectedPositionControl: string, flagselectedValueControl: string, flagsnapToGrid: int, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 falloffCurveAttr(
[string]
    , [addControlVertex=string], [annotation=string], [asString=string], [attribute=name], [backgroundColor=[float, float, float]], [changeCommand=script], [currentKey=int], [currentKeyValue=[float, float]], [customCurveWidget=int], [defineTemplate=string], [deleteControlVertex=int], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [readOnly=int], [selectedPositionControl=string], [selectedValueControl=string], [snapToGrid=int], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

falloffCurveAttr is undoable, queryable, and editable.
A single float for control point position
A single float for control point value




Example:
---
import maya.cmds as cmds

Create a window with a curve control for a curve attribute
---

cmds.window( title='Curve Control For Attribute' )
objName = cmds.createNode('vectorExtrude')
cmds.columnLayout()
cmds.falloffCurveAttr( at='%s.extrudeCurve[1]' % objName )
cmds.showWindow()

---
Return:
---


    string: The name of the port created or modified

Flags:
---


---
addControlVertex(acv): string
    properties: edit
    Used to add a control vertex for the curve.

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
asString(asString): string
    properties: query, edit
    Used to query and set the value of the curve as a string of comma
separated values

---
attribute(at): name
    properties: create
    Specifies the name of the curve attribute to control.

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
    properties: edit
    Specifies a command to be executed whenever the value of this curve
is modified.

---
currentKey(ck): int
    properties: create, query, edit
    Returns the index of the currently selected key.

---
currentKeyValue(ckv): [float, float]
    properties: query, edit
    Get or set the value of the currently selected key.

---
customCurveWidget(ccw): int
    properties: create, query, edit
    Determines whether or not the curve widget is using a custom curve. When a custom curve is used, it is stored by a falloff curve in the brush tool settings, and the flag should be non-zero.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deleteControlVertex(dcv): int
    properties: edit
    Used to delete a control vertex of the curve.

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
readOnly(ro): int
    properties: create, query, edit
    Specifies if the curve is read only or not. If true, the curve can't be edited.

---
selectedPositionControl(spc): string
    properties: create, edit
    Specifies the name of a float slider to edit the selected key position.

---
selectedValueControl(svc): string
    properties: create, edit
    Specifies the name of a float slider to edit the selected key value.

---
snapToGrid(stg): int
    properties: create, query, edit
    Specifies whether or not curve control points snap to grid when they are being moved.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/falloffCurveAttr.html 
    """


def fcheck() -> None:
    """Synopsis:
---
---
 fcheck()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fcheck is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

View the image "myImage.iff"
---

cmds.fcheck( 'myImage.iff' )

You can also display several images at once using filenames with
wildcards (each in a separate window)
---

cmds.fcheck( 'myTest*' )

You can display an animation using a trailing dot (.) on the
filename.
---

cmds.fcheck( 'mySequence.' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fcheck.html 
    """


def file(flagabsoluteName: boolean, flagactivate: boolean, flagactiveProxy: boolean, flagadd: boolean, flaganyModified: boolean, flagapplyTo: string, flagbuildLoadSettings: boolean, flagchannels: boolean, flagcleanReference: string, flagcommand: tuple[string, string], flagcompress: boolean, flagconstraints: boolean, flagconstructionHistory: boolean, flagcopyNumberList: boolean, flagdefaultExtensions: boolean, flagdefaultNamespace: boolean, flagdeferReference: boolean, flageditCommand: string, flagerrorStatus: boolean, flagexecuteScriptNodes: boolean, flagexists: boolean, flagexpandName: boolean, flagexportAll: boolean, flagexportAnim: boolean, flagexportAnimFromReference: boolean, flagexportAsReference: boolean, flagexportAsSegment: boolean, flagexportSelected: boolean, flagexportSelectedAnim: boolean, flagexportSelectedAnimFromReference: boolean, flagexportSelectedNoReference: boolean, flagexportSelectedStrict: boolean, flagexportSnapshotCallback: tuple[script, string], flagexportUnloadedReferences: boolean, flagexpressions: boolean, flagfileMetaData: boolean, flagflushReference: string, flagforce: boolean, flaggroupLocator: boolean, flaggroupName: string, flaggroupReference: boolean, flagi: boolean, flagignoreVersion: boolean, flagimportFrameRate: boolean, flagimportReference: boolean, flagimportTimeRange: string, flaglastFileOption: boolean, flaglastTempFile: boolean, flaglist: boolean, flagloadAllDeferred: boolean, flagloadAllReferences: boolean, flagloadNoReferences: boolean, flagloadReference: string, flagloadReferenceDepth: string, flagloadReferencePreview: string, flagloadSettings: string, flaglocation: boolean, flaglockContainerUnpublished: boolean, flaglockFile: boolean, flaglockReference: boolean, flagmapPlaceHolderNamespace: tuple[string, string], flagmergeBaseAnimLayer: boolean, flagmergeNamespaceWithParent: boolean, flagmergeNamespaceWithRoot: boolean, flagmergeNamespacesOnClash: boolean, flagmodified: boolean, flagmoveSelected: boolean, flagnamespace: string, flagnewFile: boolean, flagopen: boolean, flagoptions: string, flagparentNamespace: boolean, flagpostSaveScript: string, flagpreSaveScript: string, flagpreserveName: boolean, flagpreserveReferences: boolean, flagpreview: boolean, flagprompt: boolean, flagproxyManager: string, flagproxyTag: string, flagreference: boolean, flagreferenceDepthInfo: uint, flagreferenceNode: string, flagrelativeNamespace: string, flagremoveDuplicateNetworks: boolean, flagremoveReference: boolean, flagrename: string, flagrenameAll: boolean, flagrenameToSave: boolean, flagrenamingPrefix: string, flagrenamingPrefixList: boolean, flagreplaceName: tuple[string, string], flagreserveNamespaces: boolean, flagresetError: boolean, flagreturnNewNodes: boolean, flagsave: boolean, flagsaveDiskCache: string, flagsaveReference: boolean, flagsaveReferencesUnloaded: boolean, flagsaveTextures: string, flagsceneName: boolean, flagsegment: string, flagselectAll: boolean, flagshader: boolean, flagsharedNodes: string, flagsharedReferenceFile: boolean, flagshortName: boolean, flagstrict: boolean, flagswapNamespace: tuple[string, string], flagtype: string, flaguiConfiguration: boolean, flaguiLoadConfiguration: boolean, flagunloadReference: string, flagunresolvedName: boolean, flagusingNamespaces: boolean, flagwithoutCopyNumber: boolean, flagwritable: boolean) -> string:
    """Synopsis:
---
---
 file(
string
    , [absoluteName=boolean], [activate=boolean], [activeProxy=boolean], [add=boolean], [anyModified=boolean], [applyTo=string], [buildLoadSettings=boolean], [channels=boolean], [cleanReference=string], [command=[string, string]], [compress=boolean], [constraints=boolean], [constructionHistory=boolean], [copyNumberList=boolean], [defaultExtensions=boolean], [defaultNamespace=boolean], [deferReference=boolean], [editCommand=string], [errorStatus=boolean], [executeScriptNodes=boolean], [exists=boolean], [expandName=boolean], [exportAll=boolean], [exportAnim=boolean], [exportAnimFromReference=boolean], [exportAsReference=boolean], [exportAsSegment=boolean], [exportSelected=boolean], [exportSelectedAnim=boolean], [exportSelectedAnimFromReference=boolean], [exportSelectedNoReference=boolean], [exportSelectedStrict=boolean], [exportSnapshotCallback=[script, string]], [exportUnloadedReferences=boolean], [expressions=boolean], [fileMetaData=boolean], [flushReference=string], [force=boolean], [groupLocator=boolean], [groupName=string], [groupReference=boolean], [i=boolean], [ignoreVersion=boolean], [importFrameRate=boolean], [importReference=boolean], [importTimeRange=string], [lastFileOption=boolean], [lastTempFile=boolean], [list=boolean], [loadAllDeferred=boolean], [loadAllReferences=boolean], [loadNoReferences=boolean], [loadReference=string], [loadReferenceDepth=string], [loadReferencePreview=string], [loadSettings=string], [location=boolean], [lockContainerUnpublished=boolean], [lockFile=boolean], [lockReference=boolean], [mapPlaceHolderNamespace=[string, string]], [mergeBaseAnimLayer=boolean], [mergeNamespaceWithParent=boolean], [mergeNamespaceWithRoot=boolean], [mergeNamespacesOnClash=boolean], [modified=boolean], [moveSelected=boolean], [namespace=string], [newFile=boolean], [open=boolean], [options=string], [parentNamespace=boolean], [postSaveScript=string], [preSaveScript=string], [preserveName=boolean], [preserveReferences=boolean], [preview=boolean], [prompt=boolean], [proxyManager=string], [proxyTag=string], [reference=boolean], [referenceDepthInfo=uint], [referenceNode=string], [relativeNamespace=string], [removeDuplicateNetworks=boolean], [removeReference=boolean], [rename=string], [renameAll=boolean], [renameToSave=boolean], [renamingPrefix=string], [renamingPrefixList=boolean], [replaceName=[string, string]], [reserveNamespaces=boolean], [resetError=boolean], [returnNewNodes=boolean], [save=boolean], [saveDiskCache=string], [saveReference=boolean], [saveReferencesUnloaded=boolean], [saveTextures=string], [sceneName=boolean], [segment=string], [selectAll=boolean], [shader=boolean], [sharedNodes=string], [sharedReferenceFile=boolean], [shortName=boolean], [strict=boolean], [swapNamespace=[string, string]], [type=string], [uiConfiguration=boolean], [uiLoadConfiguration=boolean], [unloadReference=string], [unresolvedName=boolean], [usingNamespaces=boolean], [withoutCopyNumber=boolean], [writable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

file is undoable, queryable, and editable.Opening, importing, exporting, referencing, saving, or renaming a
file

This command needs a single main flag that specifies the action to take.
Some of the main flags also take optional secondary flags to modify
that action.



The main flags are:

cr ea
ean ear eas
er esa es


esn ex
fr i ir
l lr lrp


loc ltf
mf new o
op ot pmt


r rdi
rn rr rts
s sa sdx


st stx
typ uc ur
w





o/open can be modified by the following secondary flags:

f lad
lad lnr rnn





es/exportSelected can be modified by the following
secondary flags:

ch chn
con exp sh





r/reference can be modified by the following secondary
flags:

dns dr
gr gl gn
mnc
ns rfn rpr
sns srf shd
rnn





i/import can be modified by the following secondary
flags:

dns dr
gr gn
mnc
pr
ra rdn rnn
rpr sns





n/new and s/save can be modified by the following
secondary flags:

f





er/exportAsReference can be modified by the following
secondary flags:

ns rpr





ea/exportAll and es/exportSelected can be modified by
the following secondary flags:

f pr





ean/exportAnim,  eas/exportSelectedAnim
can be modified by the following secondary flags:

f





ear/exportAnimFromReference, esa/exportSelectedAnimFromReference
can be modified by the following secondary flags:

f rfn




Querying information about a file


This command needs a single main query flag that specifies the query to take
and then optional secondary flags to modify that query.



The main query flags are:

amf ch
chn con dr
err ex exn


exp l
loc ltf mf
ns op ot


pmt pns
r rfn rpl
rpr rts sdc


sh sn
stx typ uc
w





dr/deferReference can be modified by the following
secondary flags:

rfn





exn/expandName, l/list, r/reference, sn/sceneName can
be modified by the following secondary flags:

un shn
wcn



Querying file names


When querying a file name there are a number of ways to format the result:

Resolved vs. unresolved name:
When a file is loaded into Maya (e.g., by opening or referencing it),
the file path provided may not be complete. It could, for example, be
a relative path (ex: "scenes/myScene.ma"), it could contain environment
variables (ex: "$PRODUCTION_DIR/myScene.ma"), and it could even be a path
which simply doesn't exist on the local disk. In each of these cases Maya
goes through a number of steps to resolve the path and find the file on disk.
By default the 'file' command will return the resolved file name (i.e., the
location from which Maya is actually reading the file), but if the
un/unresolved flag is used, the unresolved file (e.g., the one that
was originally specified) will be returned. When providing a file path with
an environment variable; for example, when using the -rename flag, the
environment variable should be set to a relative path ( such as "/scenes/scenesSetA"; ).
Providing a path using an environment variable that is set to an absolute path
( for example, "C:/scenes/" ) is not supported.

Full vs. short name:
By default the 'file' command will return the full
path to a file, but if the shn/shortName flag is used just the
file name will be returned.

With vs. without copy number:
When the same file is loaded into Maya more
than once (for example by referencing the same file twice), Maya
distinguishes between the various copies by appending a copy number to the
end of the file name. The first time the file is loaded, no copy number is
appended. The second time the file is loaded a "{1}" is appended, the third
time a "{2}" is used, and so on. By default the 'file' command will return
the file name with the copy number appended, but if the
wcn/withoutCopyNumber flag is used the file name will be returned
without the copy number.

Additional Details

The file command usually expects a file name as its argument, if none
is specified then the root scene is used.
See the individual flag descriptions for details and limitations.





Example:
---
import maya.cmds as cmds

save the current scene to an ascii file named "fred.ma"
---

cmds.file( rename='fred.ma' )
cmds.file( save=True, type='mayaAscii' )

save the current scene to an ascii file without the ".ma" extension
---

cmds.file( rename='tmp' )
cmds.file( save=True, defaultExtensions=False, type='mayaAscii' )

open the file fred.ma, using the default load settings. Any references will
be brought in in the same state they were in when fred.ma was last saved.
---

cmds.file( 'fred.ma', open=True )

reference the file wilma.mb
---

cmds.file( 'C:/mystuff/wilma.mb', reference=True )

get the name of the reference node for wilma.mb
cmds.file( 'C:/mystuff/wilma.mb', query=True, referenceNode=True )
Result: wilmaRN ---


does the wilmaRN reference node represent a deferred reference?
cmds.file(query=True, referenceNode='wilmaRN', deferReference=True)
Result: False ---


reference the file barney.mb into a namespace called "rubble".
---

cmds.file( 'C:/maya/projects/default/scenes/barney.ma', reference=True, type='mayaAscii', namespace='rubble' )

change the namespace containing barney.mb.
---

cmds.file( 'C:/maya/projects/default/scenes/barney.ma', edit=True, namespace='purpleDinosaur' )

retrieve a string array of all files such as main scene and reference files in the scene
---

cmds.file( query=True, list=True )
Result: C:/maya/projects/default/scenes/fred.ma C:/mystuff/wilma.mb C:/maya/projects/default/scenes/barney.ma

Select "betty" and export betty to a separate file called "betty.mb".
Reference the new betty file into this scene, replacing the
previous betty object from this scene with the reference to betty.
---

cmds.file( 'c:/mystuff/betty.mb', type='mayaBinary', namespace='rubble', exportAsReference=True )

Select all the objects associated with file betty.mb
---

cmds.file( 'c:/mystuff/betty.mb', selectAll=True )
Result: rubble:betty

Remove the reference file betty.mb. All nodes in betty.mb will
be removed from the scene
cmds.file( 'c:/mystuff/betty.mb', removeReference=True )

Query whether the file named "foo.mb" exists on disk
---

cmds.file( 'foo.mb', query=True, exists=True )
Result: 0 ---


Query whether the reference node "rubble:betty is deferred loaded.
Note, -referenceNode flag has to come before -q flag.
cmds.file(referenceNode='rubbleRN', query=True, deferReference=True )

Query the last temp file during file save
---

cmds.file( query=True, lastTempFile=True)

---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
/
---
/   Example for the '-buildLoadSettings' and '-loadSettings' flags  ---
/
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
/

Build load settings for "ref.ma"
cmds.file( 'ref.ma', open=True, buildLoadSettings=True )
Edit those settings, to indicate that some reference should
be brought in unloaded.
Note: the following command is primarily intended for internal
use. It may not be easy to determine the numeric ID of a given
reference ("2" in this case) .
cmds.loadSettings( '2', deferReference=1 )
Use the edited settings when opening the file
cmds.file('ref.ma', open=True, loadSettings='implicitLoadSettings')

---

  Example for the '-cleanReference' and '-editCommand' flags
---


Create a simple reference to a sphere
---

cmds.file( force=True, new=True )
cmds.polySphere()
cmds.file( rename='ref.ma' )
cmds.file( force=True, type='mayaAscii', save=True )
cmds.file( force=True, new=True )
cmds.file( 'ref.ma', reference=True, namespace='ref' )

Scale the sphere
---

cmds.setAttr( 'ref:pSphere1.s', 5, 5, 5 )
cmds.getAttr( 'ref:pSphere1.s' )
Result: 5 5 5 ---


The 'cleanReference' and 'editCommand' flags only work on
unloaded references.
---

cmds.file( unloadReference='refRN' )

Query the setAttr edits:
---

cmds.reference( referenceNode='refRN', query=True, editCommand=True )
Result: setAttr ref:pSphere1.s -type "double3" 5 5 5 setAttr ref:lightLinker1.lnk -s 2 ---


Remove all setAttr edits on refRN:
---

cmds.file( cleanReference='refRN', editCommand='setAttr' )
cmds.reference( referenceNode='refRN', query=True, editCommand=True )
Note that nothing is returned

cmds.file( loadReference='refRN' )

cmds.getAttr( 'ref:pSphere1.s' )
Result: 1 1 1 ---

Note that scale has returned to 1 1 1

apply the edit file to a reference
cmds.file("translateSphere.editMA", reference=True, applyTo="refRN")
Result: maps <main> to refRN's namespace

apply the edit file to nodes in the main scene
cmds.file("translateSphere.editMA", i=True, applyTo=":")
Result: maps <main> to the root namespace

apply the edit file to a reference, but it also has connections between two refs
cmds.file("connectionsBetweenRefs.editMA", reference=True, applyTo="refRN", mapPlaceHolderNamespace=("<otherRef>", "otherRefRN"))
Result: maps <main> to refRN's namespace and <otherRef> to otherRefRN's namespace

Change the modified state of the file.
cmds.file(modified=True)

Set the file options
cmds.file( force=True, save=True, options='v=1;p=17',type='mayaAscii');
Result:The saved file uses full names for attributes on nodes and flags in command.Also the precision of values in file is 17.

Load Reference Preview

Create a nested reference with a child reference under a parent reference.
cmds.file( force=True, new=True )
cmds.polySphere()
cmds.file( rename='child.ma' )
cmds.file( force=True, type='mayaAscii', save=True )
cmds.file( force=True, new=True )
cmds.file( 'child.ma', reference=True, namespace='child_namespace' )
cmds.file( rename='parent.ma' )
cmds.file( force=True, type='mayaAscii', save=True )

Preview the unloaded child reference under the unloaded parent reference.
cmds.file( force=True, new=True )
cmds.file( 'parent.ma', reference=True, namespace='parent_namespace' )
cmds.file( 'parent.ma', unloadReference=True )
cmds.file( 'parent.ma', loadReferencePreview=True )

---

---
                           Example for 'mergeNamespacesOnClash'
---


Create a reference
cmds.file( force=True, new=True )
cmds.namespace( add="bar" )
cmds.namespace( set="bar" )
cmds.polySphere();
cmds.file( rename="ref.ma" )
cmds.file( force=True, type='mayaAscii', save=True )

Create a scene with some namespaces and objects
cmds.file( force=True, new=True )
cmds.namespace( add="ref:foo:bar" )
cmds.namespace( set="ref:foo:bar" )
cmds.polySphere();

Merge into root
cmds.file('ref.ma', reference=True, mergeNamespacesOnClash=True, namespace=':');

Merge into nested namespace
cmds.file('ref.ma', i=True, mergeNamespacesOnClash=True, namespace=':ref:foo');

Don't merge namespace
cmds.file('ref.ma', reference=True, mergeNamespacesOnClash=False, namespace=':ref:foo');

Now Edit the new namespace and merge it
cmds.file('ref.ma', edit=True, mergeNamespacesOnClash=True, namespace=':ref:foo');




---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
/
---
/ Example for export with relativeNamespace  ---
/
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
/

cmds.file(new=True,force=True)
cmds.sphere(name=":A:sphereA")
cmds.sphere(name=":A:B:sphereB")
cmds.sphere(name=":A:B:C:sphereC")
cmds.sphere(name=":D:sphereD")

Select all the spheres.
---

cmds.select(":A:sphereA", replace=True)
cmds.select(":A:B:sphereB",add=True)
cmds.select(":A:B:C:sphereC",add=True)
cmds.select(":D:sphereD",add=True)

Export all these spheres with -relativeNamespace flag.
---

cmds.file(rename="exp.ma")
cmds.file(force=True, exportSelected=True, type="mayaAscii", relativeNamespace=":A:B")
The result in the exported file:
:A:sphereA
:C:sphereC
:D:sphereD
-sphereB
---


---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
/
---
/ Example for export with exportSnapshotCallback  ---
/
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
/

def python_export_callback():
    """
    Print all nodes to be exported and triangulate all mesh shapes.
    """
    oldRelNames = cmds.namespace(q=True, relativeNames=True)
    cmds.namespace(relativeNames=True)
    nodes = cmds.ls("*", r=True)
    for node in nodes:
        print("Exporting " + node)
    meshes = cmds.ls("*", r=True, typ="mesh")
    for mesh in meshes:
        print("Triangulating " + mesh)
        cmds.polyTriangulate(mesh)
    cmds.namespace( relativeNames=oldRelNames )

cmds.file( f=True, new=True)
sphere = cmds.polySphere()
cube = cmds.polyCube()
cyl = cmds.polyCylinder()
cmds.parent( sphere[0], cube[0] )
cmds.parent( cube[0], cyl[0] )
cmds.file( 'export.ma', force=True, options="v=0;", type="mayaAscii", ea=True, esc=(python_export_callback, "TEMP_EXPORT"))

---
Return:
---


    string: The name of the specified file for most actions. When the returnNewNodes flag is used, an array of strings will be returned indicating the names of the nodes that were read.

Flags:
---


---
absoluteName(an): boolean
    properties: create, query
    This is a general flag which can be used to specify the desired format for
the namespace(s) returned by the command.
The absolute name of the namespace is a full namespace path, starting from the root namespace ":"
and including all parent namespaces.  For example ":ns:ball" is an absolute namespace
name while "ns:ball" is not.

---
activate(a): boolean
    properties: 
    This flag is obsolete.

---
activeProxy(ap): boolean
    properties: create
    This flag is intended for internal use by Maya during file referencing.
It specifes which file is the active proxy when the file is loaded when
used with the reference flag. It is also used to specify which file is
the active proxy in the file referencing preload information when used
with the referenceDepthInfo flag.

---
add(add): boolean
    properties: create
    When used with selectAll it indicates that the specified items should be
added to the active list without removing existing
items from the active list.

---
anyModified(amf): boolean
    properties: query
    This flag is obsolete. Please use file -q -modified instead.

---
applyTo(at): string
    properties: create
    When importing or referencing an offline edit file, apply it to
to the given reference (i.e., determine what <main> gets mapped to).
Specify the reference node name as argument. To apply the edits to nodes in
the main scene (i.e., the root namespace), pass in ":".
To collapse <main> (i.e., map it to "None"), pass in "".
May only be used with the file -i/import or -r/reference flags.

---
buildLoadSettings(bls): boolean
    properties: create
    When used with the "o/open" flag it indicates that the specified
file should be read for reference hierarchy information only.
This information will be stored in temporary load settings under
the name "implicitLoadSettings". When this flag is used the
specified scene file will not be loaded: no objects/nodes will be
created or modified.
Note: most users will not need to use this flag or the
"implicitLoadSettings" it builds. They can access the same
functionality by setting the "Selective Load" option in the
File > Open Option Box.

---
channels(chn): boolean
    properties: create, query
    For use with exportSelected to specify whether attached channels should be included in the export.

---
cleanReference(cr): string
    properties: create
    Remove edits from the passed in reference node.
The reference must be in an unloaded state. To remove a particular
type of edit, use the editCommand flag. If no flag is specified,
all edits will be removed.

---
command(c): [string, string]
    properties: create, query
    Specifies the callback to execute before any file operation.
This is an internal flag used only in the file format.

---
compress(cmp): boolean
    properties: create
    When used with save, it will compress (gzip) the file on output.

---
constraints(con): boolean
    properties: create, query
    For use with exportSelected to specify whether attached constraints should be included in the export.

---
constructionHistory(ch): boolean
    properties: create, query
    For use with exportSelected to specify whether attached construction history should be included in the export.

---
copyNumberList(cnl): boolean
    properties: query
    When queried, this flag returns a string array containing
a number that uniquely identifies each instance the file
is used.

---
defaultExtensions(de): boolean
    properties: create, query
    Use the default extensions to rename the files. This defaults to true, but
is a persistent setting within a given session of Maya, meaning that if
you set it to true or false, that value will
continue to be used in subsequent file commands until a new value is set.

---
defaultNamespace(dns): boolean
    properties: create
    Use the default name space for import and referencing.  This is
an advanced option.  If set, then on import or reference, Maya will
attempt to place all nodes from the imported or referenced file
directly into the root (default) name space, without invoking any
name clash resolution algorithms.  If the names of any of the new
objects    already exist in the root namespace, then errors will result.
The user of this flag is responsible for creating a name clash
resolution mechanism outside of Maya to avoid such errors.
Note: This flag    is intended only for use with custom file
translators written through    the API. Use at your own risk.

---
deferReference(dr): boolean
    properties: create, query
    When used in conjunction with the -reference flag, this
flag determines if the reference is loaded, or if loading is
deferred.
C: The default is false.
Q: When queried, this flag returns true if the reference is deferred,
or false if the reference is not deferred. If this is used
with -rfn/referenceNode, the -rfn flag must come before -q.

---
editCommand(ec): string
    properties: create
    For use with cleanReference. Remove only this type of edit.
Supported edits are: setAttr addAttr deleteAttr connectAttr
disconnectAttr and parent

---
errorStatus(err): boolean
    properties: query
    Query the error status of the last file read. Returns true if and error occurred during the last file read.

---
executeScriptNodes(esn): boolean
    properties: create
    If true, allow the appropriate script nodes to execute. If false,
do not allow any script node scripts to run.
For more information, see the documentation for script nodes.
Default: true.

---
exists(ex): boolean
    properties: query
    Query if the file exists. Returns true if the file exists.

---
expandName(exn): boolean
    properties: query
    This is a query only flag that can be used to query for the
file path name of the file.

---
exportAll(ea): boolean
    properties: create
    Export everything into a single file.
Returns the name of the exported file.

---
exportAnim(ean): boolean
    properties: create
    Export all animation nodes and animation helper nodes from all objects in the
scene.
The resulting animation export file will contain connections to objects that are
not included in the animation file. As a result, importing/referencing this file
back in will require objects of the same name to be present, else errors will occur.
The -sns/swapNamespace flag is available for swapping the namespaces of given objects
to another namespace. This use of namespaces can be used to re-purpose the animation
file to multiple targets using a consistent naming scheme.

The exportAnim flag will not export animation layers. For generalized file export of
animLayers and other types of nodes,
refer to the exportEdits command. Or
use the Export Layers functionality.

---
exportAnimFromReference(ear): boolean
    properties: create
    Export the main scene animation nodes and animation helper nodes from all referenced
objects. This flag, when used in conjunction with the -rfn/referenceNode flag,
can be constrained to only export animation nodes from the specified reference
file. See -ean/exportAnim flag description for details on usage of animation files.

---
exportAsReference(er): boolean
    properties: create
    Export the selected objects into a reference file with the given
name. The file is saved on disk during the process.
Returns the name of the reference created.

---
exportAsSegment(exs): boolean
    properties: 
    This flag is obsolete.

---
exportSelected(es): boolean
    properties: create
    Export the selected items into the specified file.
Returns the name of the exported file.

---
exportSelectedAnim(eas): boolean
    properties: create
    Export all animation nodes and animation helper nodes from the selected objects
in the scene. See -ean/exportAnim flag description for details on usage of animation
files.

---
exportSelectedAnimFromReference(esa): boolean
    properties: create
    Export the main scene animation nodes and animation helper nodes from the selected
referenced objects. This flag, when used in conjunction with the -rfn/referenceNode
flag, can be constrained to only export animation nodes from the selected nodes
of a specified reference file. See -ean/exportAnim flag description for details on
usage of animation files.

---
exportSelectedNoReference(esr): boolean
    properties: 
    This flag is obsolete.

---
exportSelectedStrict(ess): boolean
    properties: create
    Export the selected items into the specified file. This flag differs from exportSelected
in that it will only export the nodes that are explicitly on the selection list. Related
nodes (both history and DAG related) are not automatically exported unless those nodes
are also on the selection list. Node relationships are only preserved if both nodes in the
relationship (parent/child, source/destination) are exported.
It is important to note that there is potential for scene data loss in the exported
scene since not all related nodes are not exported by default. The user is responsible for
selecting all relevant nodes before exporting.
Returns the name of the exported file.

---
exportSnapshotCallback(esc): [script, string]
    properties: create
    When specified alongside -ea/exportAll, es/exportSelected and -ess/exportSelectedStrict,
this flag enables Maya to temporarily duplicate the export targets into a specified
namespace and invoke a callback to interact with the duplicate export targets before
writing the duplicate export targets to disk. Once written to disk, the duplicate
export targets, new nodes created by the callback and temporary namespace are removed
from the scene. Implicitly created nodes (eg. persp, top, etc.) are not duplicated.

For the duration of the callback:
1. The specified namespace will be made current.
2. All nodes added by the callback are tracked as a temporary export target.
3. Although the intent of the callback is to only operate on the duplicate export
targets, there is nothing limiting the callback from modifying the main scene.
Thus, the callback should be written with care.

This flag accepts two arguments:
a. [string] Callback to invoke prior to write to disk.
b. [string] Temporary namespace to store duplicate export targets.

This flag can only be used in conjunction with -ea/exportAll, -es/exportSelected and
-ess/exportSelectedStrict.

Note that the -pv/preview flag still only previews the contents of the export targets
_prior_ to the snapshot duplication. It does not preview the final output after the
callback.

Referenced nodes are duplicated in the same manner as duplicating those nodes
manually in the scene. Similarly, scene assembly nodes will duplicate as they would
if manually duplicated, however scene assembly nodes have special duplication
behavior, so the callback should be aware of these differences when anticipating
the duplicate export targets.

---
exportUnloadedReferences(eur): boolean
    properties: create
    Only effective when preserveReferences is used.
When used with the exportAll flag, tells the exporter to
include all unloaded references in the export.
When used with the exportSelected flag, tells the exporter to
include all unloaded proxy references that are related to
any node in the selection.

---
expressions(exp): boolean
    properties: create, query
    For use with exportSelected to specify whether attached expressions should be included in the export.

---
fileMetaData(fmd): boolean
    properties: query
    This is a query only flag to get the file metadata for audio files. It returns the referenceTime. This field is only extracted from BWAVE files,
for other files it returns 0

---
flushReference(fr): string
    properties: create
    This flag will unload the reference file associated with the
passed reference node, retaining all associated reference nodes
and scene files. ** This option only works when using namespaces **.
More Details: This flag is primarily intended to be
used as part of a custom asset management system. It can be used to
defer loading of a reference which contains child references without
losing information about those child references. Prior to reloading a
flushed    reference which contains child references, the
'createNode reference' lines should be manually removed from the
children's Maya ASCII files. If this is not done, extra reference
nodes will be created.

---
force(f): boolean
    properties: create
    Force an action to take place.
(new, open, save, remove reference, unload reference)
Used with removeReference to force remove reference namespace even if it has contents.
Cannot be used with removeReference if the reference resides in the root namespace.
Used with unloadReference to force unload reference even if the reference node is locked,
without prompting a dialog that warns user about the lost of edits.

---
groupLocator(gl): boolean
    properties: create
    Used only with the -r and the -gr flag.
Used to group the output of groupReference under a locator

---
groupName(gn): string
    properties: create
    Used only with the -gr flag.
Optionally used to set the name of the transform node that the imported/referenced
items will be grouped under.

---
groupReference(gr): boolean
    properties: create
    Used only with the -r or the -i flag.
Used to group all the imported/referenced items under a single transform.

---
ignoreVersion(iv): boolean
    properties: create
    Used to open files with versions other than those officially supported.
Success is not guaranteed. Data loss, data corruption or failure to open are all possible outcomes.
Can only be used with the -o and -i flags.

---
i(i): boolean
    properties: create
    Import the specified file.
Returns the name of the imported file.

---
importFrameRate(ifr): boolean
    properties: create
    Used only with the -i flag.
Used to import the frame rate and set it as Maya's frame rate.

---
importReference(ir): boolean
    properties: create
    Remove the encapsulation of the reference around the data within
the specified file.    This makes the contents of the specified file
part of the current scene and all references to the original file
are lost.
Returns the name of the reference that was imported.

---
importTimeRange(itr): string
    properties: create
    Used only with the -i flag.
Used to import the time range and apply it to Maya's playback range in one
of three different ways as specified by the string.  The valid strings are
"keep", which keeps Maya's playback range untouched, "override", which overrides
Maya's playback range with the imported range, and "combine", which extends Maya's
playback range to encompass the imported range.

---
lastFileOption(lfo): boolean
    properties: query
    On query, returns the last option string used by the file command.

---
lastTempFile(ltf): boolean
    properties: query
    When queried, this flag returns the temp file name used during
file save. The temp file will be left in the same directory
as the intended file name if the save fails.

---
list(l): boolean
    properties: query
    List all files.
Returns a string array of the names of all segment/reference files.
Duplicates will be removed. So if a file is referenced more than
once, and the -withoutCopyNumber flag is set, it will only be listed once.
in the scene.

---
loadAllDeferred(lad): boolean
    properties: create
    This flag is obsolete, and has been replaced by
the loadReferenceDepth flag. When used with the -open flag, determines
if the -deferReference flag is respected when reading in the file. If
true is passed, all of the references are loaded. If false is passed,
the -deferReference flag is respected.

---
loadAllReferences(lar): boolean
    properties: create
    This flag is obsolete and has been replaced with the
loadReferenceDepth flag. When used with the -open flag,
this will cause all references to be loaded.

---
loadNoReferences(lnr): boolean
    properties: create
    This flag is obsolete and has been replaced witht the
loadReferenceDepth flag. When used with the -open flag,
no references will be loaded. When used with -i/import,
-r/reference or -lr/loadReference flags, will load the
top-most reference only.

---
loadReference(lr): string
    properties: create, query
    This flag loads a file and associates it with the passed reference
node. If the reference node does not exist, the command will fail. If
the file is already loaded, then this flag will reload the same file.
If a file is not given, the command will load (or reload) the last used
reference file.

---
loadReferenceDepth(lrd): string
    properties: create
    Used to specify which references should be loaded. Valid types are
"all", "none" and "topOnly", which will load all references,
no references and top-level references only, respectively. May only be used
with the -o/open, -i/import, -r/reference or -lr/loadReference flags.
When "none"
is used with -lr/loadReference, only path validation is performed. This
can be used to replace a reference without triggering reload. Not using
loadReferenceDepth will load references in the same loaded or
unloaded state that they were in when the file was saved.
Additionally, the -lr/loadReference flag supports a fourth type, "asPrefs".
This will force any nested references to be loaded according to the
state (if any) stored in the current scene file, rather than according to the
state saved in the reference file itself.

---
loadReferencePreview(lrp): string
    properties: create
    This flag will perform a special preview-only load of a reference file.
A preview-only reference file is not completely loaded, but instead is
partially loaded so that certain information, such as nested references
it contains, can be determined.
Nested references that are previewed remain in a special preview-only state.

---
loadSettings(ls): string
    properties: create
    When used with the "o/open" flag this flag specifies which reference
load settings should be used. Reference load settings specify which
references should be brought in loaded and which unloaded. Those
reference files that are brought in unloaded will usually not need
to be read and interpreted by Maya. This can potentially reduce the
time it takes Maya to load the whole scene.
If no "ls/loadSettings" flag is specified, or the empty string ("") is
used as the flag argument, the default load settings are used. The
default load settings represent the state of all references when the file
was last saved. The load settings "implicitLoadSettings" refer to the
temporary load settings generated by the "bls/buildLoadSettings" flag and
edited with the "loadSettings" command.
Currently on the default and implicit load settings are supported.

---
location(loc): boolean
    properties: query
    Query the location of the given file name.

---
lockContainerUnpublished(lcu): boolean
    properties: create
    Set the unpublised lock state for all containers in this file. This will not lock
the attributes in the main scene directly, but any file that references this scene
will have all its containers come in as unpublished locked.

---
lockFile(lf): boolean
    properties: create
    Lock or unlock the main scene. Any file referencing this scene will
automatically lock all attributes and nodes. Also prevents reference
edits from being saved to it from a parent file.

---
lockReference(lck): boolean
    properties: create
    Locks attributes and nodes from the referenced file.

---
mapPlaceHolderNamespace(mns): [string, string]
    properties: create, query, edit, multiuse
    Map a placeHolderNamespace to the given reference. Must be
used with the file -i/import, -r/reference flags in create mode.
The first string is the place holder namespace, including the angle
brackets (ex: "<foo>"). The second string is the reference node
whose namespace it should be mapped to (ex: "refRN"). If the namespace
should be mapped to the root namespace, use ":".
To collapse the namespace (i.e., map it to "None"), use "".
When queried, namespaces that are mapped to "None" will return "(None)" for clarity.

---
mergeBaseAnimLayer(mbl): boolean
    properties: create
    When set, Maya will merge the base animation layer imported from the file with
the base layer already existing in the scene.

---
mergeNamespaceWithParent(mnp): boolean
    properties: create
    Used with the removeReference flag.
When removing a file reference and its namespace, move the rest of the namespace
content to parent namespace.
Cannot be used if the reference resides in the root namespace.

---
mergeNamespaceWithRoot(mnr): boolean
    properties: create
    Used with the removeReference flag.
When removing a file reference and its namespace, move the rest of the namespace
content to root namespace.
Cannot be used if the reference resides in the root namespace.

---
mergeNamespacesOnClash(mnc): boolean
    properties: create
    Used with the import, reference or edit flags, this option will prevent new namespaces
from being created when namespaces of the same name already exist within Maya.
The default value is false.
For example, if an object "pSphere1", which is being imported, refers to the
namespace "ref" and there is already a namespace called "ref" defined in Maya.
If mergeNamespacesOnClash is true, the existing "ref" namespace will be reused
and pSphere1 will be moved into the existing namespace; and if the namespace has
another object which is also named "pSphere1", then the imported one will be
renamed with an incremental number("pSphere2"). On the other hand, if
mergeNamespacesOnClash is false, a new namespace will be created with an incremental
number (in first case is "ref1") and pSphere1 will be moved into the "ref1" namespace.
This flag also support nested namespace, for example, if an object "pSphere1" which is
imported and refers to namespace "ref:foo" and mergeNamespacesOnClash
is true this time, then the existing "ref:foo" will be reused and the object will be
moved into "ref:foo". Also if mergeNamespacesOnClash is false, then a new namespace
"ref:foo1" will be created and "pSphere1" will be moved into that new namespace.

---
modified(mf): boolean
    properties: create, query
    Set the modified state of the entire scene. If the scene is modified
it will need to be saved before a new file is opened or created.
Normally there is no need to edit this flag as the state of the file
is updated automatically whenever an object is created or modified.
If editing of the state is desired, it is done without use of
the edit flag as covered in the example section below.
In query mode, if the scene has been modified 1 is returned. Otherwise 0
is returned.

---
moveSelected(ms): boolean
    properties: edit
    This flag is obsolete.

---
namespace(ns): string
    properties: edit
    The namespace name to use that will group all objects during
importing and referencing.
Change the namespace used to group all the objects from
the specified referenced file. The reference must have been created
with the "Using Namespaces" option, and must be loaded. Non-referenced
nodes contained in the existing namespace will also be moved to the new
namespace. The new namespace will be created by this command and can
not already exist. The old namespace will be removed.

---
newFile(new): boolean
    properties: create
    Initialize the scene.
Returns untitled scene with default location.

---
open(o): boolean
    properties: create
    Open the specified file.
Returns the name of the opened file.

---
options(op): string
    properties: create, query
    Set/query the currently set file options.
file options are used while saving a maya file.
Two file option flags supported in current file command are v and p.

v(verbose) indicates whether long or short attribute names and command flags names are used
when saving the file. Used by both maya ascii and maya binary file formats.
It only can be 0 or 1.
Setting v=1 indicates that long attribute names and command flag names will be used.
By default, or by setting v=0, short attribute names will be used.


p(precision) defines the maya file IO's precision when saving the file. Only used by maya ascii file format.
It is an integer value. The default value is 17.

The option format is "flag1=XXX;flag2=XXX".Maya uses the last v and p as the final result.
Note:
1. Use a semicolon(";") to separate several flags.
2. No blank space(" ") in option string.

---
parentNamespace(pns): boolean
    properties: query
    Returns the name(s) of a referenced file's parent namespaces.

---
postSaveScript(pos): string
    properties: create
    When used with the save flag, the specified script will be executed
after the file is saved.

---
preSaveScript(prs): string
    properties: create
    When used with the save flag, the specified script will be executed
before the file is saved.

---
preserveName(pn): boolean
    properties: create
    When used with compress, it will retain the regular extension rather than appending .gz.

---
preserveReferences(pr): boolean
    properties: create
    Modifies the various import/export flags such that
references are imported/exported as actual references
rather than copies of those references.

---
preview(pv): boolean
    properties: create
    Used in conjunction with any of the -exportXXX flags, causes Maya
to return a list of the nodes that would be exported, without
actually writing the exported file to disk.

---
prompt(pmt): boolean
    properties: create, query
    This flag controls the display of file prompting dialogs.
Some examples of file prompting dialogs include error
messages that require user confirmation and missing file
reference dialogs. Once this flag is used, every instance
of the file command will use the last set value of this flag.
Some interactive file operations may post dialogs even when
the flag is set to false, but every scripted file command
will not display any dialogs when this flag is set to
false.  The default value is true.

---
proxyManager(pm): string
    properties: create
    When a one or more proxy references are added to an existing file reference,
the proxy manage node is used to define the proxies associated with that
reference. This flag is used in conjunction with the activeProxy and proxyTag
flag to specify the proxyManager of interest. This flag is also used to
specify the proxyManager for a proxy reference in the file referencing
preload information, when used in conjunction with the referenceDepthInfo flag.

---
proxyTag(pt): string
    properties: create
    This flag is intended for internal use only during file load or preload.
Proxy tags are names you assign to proxy references to more easily
manage the proxy references from the reference editor. Proxy tags are
unique within a given proxy set.
This flag must be  used in conjunction with the proxyManager flag.

---
reference(r): boolean
    properties: query
    Create a reference to the specified file. Returns the
name of the file referenced.
Query all file references from the specified file.

---
referenceDepthInfo(rdi): uint
    properties: create
    This flag is used to store reference loading preferences
associated with a Maya ascii file (.ma). This flag is only useful
during file I/O so users should not have any need to use this flag.

---
referenceNode(rfn): string
    properties: query
    This flag is only used during queries. In MEL, if it appears before -query
then it must be followed by the name of one of the scene's reference
nodes. That will determine the reference to be queried by whatever flags
appear after -query. If the named reference node does not exist within
the scene the command will fail with an error.

In Python the equivalent behavior is obtained by passing the name of the
reference node as the flag's value.

In MEL, if this flag appears after -query then it takes no argument and will
cause the command to return the name of the reference node associated with the
file given as the command's argument. If the file is not a reference or
for some reason does not have a reference node (e.g., the user deleted it)
then an empty string will be returned. If the file is not part of the
current scene then the command will fail with an error.

In Python the equivalent behavior is obtained by passing True as the flag's
value.
      In query mode, this flag can accept a value.

---
relativeNamespace(rns): string
    properties: create
    This flag can be used with the exportSelected, exportSelectedStrict and exportAll operations to specify
that the nodes in the exported file are to be written out relative to a specified
namespace. This provides the ability to remove undesired levels of namespacing from
the node names as they are exported. The relativeNamespace value specifies the
namespace to use as the relative root for the exported nodes, and must be specified
as an absolute namespace. Nodes in the exported file not residing within the specified
relative namespace will be written out using absolute namespace names.
Note: this flag cannot be used in conjunction with the preserveReferences flag.

---
removeDuplicateNetworks(rdn): boolean
    properties: create
    When set, Maya will remove imported networks if the same network is also
detected in the current scene. You can explicitly specify that certain types of
networks be exempted from removal by this flag. For example, if you set to the
optionVar removeDuplicateShadingNetworksOnImport to 0 (or disable the option
Remove Duplicate Shading Networks from the File > Import options), then shading
networks will be exempted from removal by this flag.This flag can only be used
in conjunction with the -i/import flag.

---
removeReference(rr): boolean
    properties: create
    Remove the given file reference from its parent. This will also
Remove everything this file references.
Returns the name of the file removed.
If the reference is alone in its namespace, remove the namespace.
If there are objects remaining in the namespace after the file reference is removed,
by default, keep the remaining objects in the namespace.
To merge the objects remaining in the namespace to the parent or root
namespace, use flags mergeNamespaceWithParent
or mergeNamespaceWithRoot. The empty file reference namespace is then removed.
To forcibly delete all objects, use flag force. The empty file reference namespace is then removed.

---
rename(rn): string
    properties: create
    Rename the scene.
Used mostly during save to set the saveAs name.
Returns the new name of the scene.

---
renameAll(ra): boolean
    properties: create
    If true, rename all newly-created
nodes, not just those whose names clash with existing nodes.
Only available with -i/import.

---
renameToSave(rts): boolean
    properties: create, query
    If true, the scene will need to be renamed before it can be
saved. When queried this flag returns true if the scene must be
renamed before it can be saved. 
The default is false.

---
renamingPrefix(rpr): string
    properties: create, query
    The string to use as a prefix for all objects from this file.
This flag has been replaced by -ns/namespace.

---
renamingPrefixList(rpl): boolean
    properties: query
    This flag returns a list of all of the renaming prefixes used
by the file.

---
replaceName(rep): [string, string]
    properties: create, query, edit, multiuse
    Define a search and replace string. Will apply search and replace to
leaf node names. The search string can include namespaces and wild-cards,
but will only apply to leaf nodes in a dag hierarchy. Intended for use
with offline edits files. May only be used with file -i/import
or -r/reference. If a nested reference also defines a substitution, it
will become the active substitution table while loading the nested reference.
Note: if used with the -e/edit flag, the replacement will only be applied
the next time the reference is loaded
Examples: -replace "*pCube1" "prop" will change "foo:pCube1" to
"foo:prop" and "|A:pCube1|B:pCube1" to "|A:pCube1|prop".

---
reserveNamespaces(rvn): boolean
    properties: create
    When this flag is enabled namespaces for unloaded references will be
created after loading the file to reduce the chances of unexpected
namespace collisions when loading or adding references later on.

---
resetError(rer): boolean
    properties: create
    Turn off any pre-existing global file errors.

---
returnNewNodes(rnn): boolean
    properties: create
    Used to control the return value in open, import, loadReference,
and reference operations. It will force the file command to return
a list of new nodes added to the current scene.

---
save(s): boolean
    properties: create
    Save the specified file.
Returns the name of the saved file.

---
saveDiskCache(sdc): string
    properties: create, query
    This flag sets the saveAs option for Jiggle disk caches.
The valid inputs are "always" - always copy a file texture to a
new location, "never" - do not copy at all. 
C: The default is "always". 
Q: When queried it returns a string ("always", "never").

---
saveReference(sr): boolean
    properties: create
    Save reference node edits and connections to reference file.
This includes newly added history and animation, provided that
these do not apply to any objects outside the reference being saved.

---
saveReferencesUnloaded(sru): boolean
    properties: create
    This flag can only be used in conjunction with the save flag. It specifies
that the saved file will be saved with all references unloaded.

---
saveTextures(stx): string
    properties: create, query
    This flag sets the saveAs option for 3d Paint file textures.
The valid inputs are "always" - always copy a file texture to a
new location, "unlessRef" - copy only if this is not a referenced
file texture, "never" - do not copy at all. 
C: The default is "unlessRef". 
Q: When queried it returns a string ("always", unlessRef", "never").

---
sceneName(sn): boolean
    properties: query
    return the name of the current scene.

---
segment(seg): string
    properties: 
    This flag is obsolete.

---
selectAll(sa): boolean
    properties: create
    Select all the components of this file as well as its child
files.  Note that the file specified must be one that is
already opened in this Maya session.
The default behavior is to replace the existing selection.
Use with the "add" flag to keep the active selection list.

---
shader(sh): boolean
    properties: create, query
    For use with exportSelected to specify whether attached shaders should be included in the export.

---
sharedNodes(shd): string
    properties: create, multiuse
    This flag modifies the '-r/reference' flag to indicate that
certain    types of nodes within that reference should be treated as
shared nodes. All shared nodes will be placed in the default
namespace. New copies of those nodes will not be created if a copy
already exists in the default namespace, instead the shared node
will be merged with the    existing node. The specifics of what
happens when two nodes are merged depends on the node type. In
general attribute values will not be merged, meaning the values set
on any existing shared nodes will be retained, and the values of
the nodes being merged in will be ignored.
The valid options are "displayLayers", "shadingNetworks",
"renderLayersByName", and "renderLayersById". This flag is
multi-use; it may be specified multiple times to for
example, share both display layers and shading networks.
Two shading networks will only be merged if    they are identical:
the network    of nodes feeding into the shading group must be
arranged identically with equivalent nodes have the same name and
node type. Additionally if a network is animated or contains a DAG
object or expression it will not be mergeable.
This flag cannot be used in conjunction with -srf/sharedReferenceFile.

---
sharedReferenceFile(srf): boolean
    properties: create
    Can only be used in conjunction with the -r/reference flag and
the -ns/namespace flag (there is no prefix support). This flag modifies
the '-r/reference' flag to indicate that all nodes within that
reference should be treated as shared nodes. New copies    of
those nodes will not be created if a copy already exists. Instead,
the shared node will be merged with the existing node. The specifics of
what happens when two nodes are merged depends on the node type.
This flag cannot be used in conjunction with -shd/sharedNodes.

---
shortName(shn): boolean
    properties: query
    When used with a main query flag it indicates that the file name
returned will be the short name (i.e., just a file name without
any directory paths). If this flag is not present, the full name
and directory path will be returned.

---
strict(str): boolean
    properties: create
    Set strict file path resolution. If true, all paths will be matched
exactly, both relative and absolute. Relative paths will be considered
relative to the project root directory. May only be used with the -o/open,
-i/import, -ir/importReference or -r/reference flags.

---
swapNamespace(sns): [string, string]
    properties: create, multiuse
    Can only be used in conjunction with the -r/reference or -i/import
flags. This flag will replace any occurrences of a given namespace to
an alternate specified namespace. This namespace "swap" will occur
as the file is referenced in. It takes in two string arguments. The
first argument specifies the namespace to replace. The second argument
specifies the replacement namespace. Use of this flag, implicitly
enables the use of namespaces and cannot be used with deferReference.

---
type(typ): string
    properties: create, query
    Set the type of this file.  By default this can be any one of:
"mayaAscii", "mayaBinary", "mel",  "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Adobe(R) Illustrator(R)", "image"
plug-ins may define their own types as well.
Return a string array of file types that match this file.

---
uiConfiguration(uc): boolean
    properties: create, query
    Save the ui configuration with the scene in a uiConfiguration
script node. (eg. panes, etc.)
The current default is on and is set in initialStartup.mel.

---
uiLoadConfiguration(ulc): boolean
    properties: create, query
    Load the scene's ui configuration. (eg. panes, etc.)
The current default is on and is set in initialStartup.mel.

---
unloadReference(ur): string
    properties: create
    This flag will unload the reference file associated with the
passed reference node.

---
unresolvedName(un): boolean
    properties: query
    When used with a main query flag it indicates that the file name
returned will be unresolved (i.e., it will be the path originally
specified when the file was loaded into Maya; this path may
contain environment variables and may not exist on disk). If this
flag is not present, the resolved name will be returned.

---
usingNamespaces(uns): boolean
    properties: query
    Returns boolean.
Queries whether the specified reference file uses namespaces
or renaming prefixes.

---
withoutCopyNumber(wcn): boolean
    properties: query
    When used with a main query flag it indicates that the file name
returned will not have a copy number appended to the end. If this
flag is not present, the file name returned may have a copy number
appended to the end.

---
writable(w): boolean
    properties: query
    Query whether the given file is writable in the current scene. For
main scene files this indicates writable to the file system by the
current user. Files referenced by the main scene file are always not
writable (referenced files are by nature read only). Files not present
in the current scene always return false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/file.html 
    """


def fileBrowserDialog(flagactionName: string, flagdialogStyle: int, flagfileCommand: script, flagfileType: string, flagfilterList: string, flagincludeName: string, flagmode: int, flagoperationMode: string, flagtipMessage: string, flagwindowTitle: string) -> string:
    """Synopsis:
---
---
 fileBrowserDialog([actionName=string], [dialogStyle=int], [fileCommand=script], [fileType=string], [filterList=string], [includeName=string], [mode=int], [operationMode=string], [tipMessage=string], [windowTitle=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fileBrowserDialog is undoable, NOT queryable, and NOT editable.
See below for an example of how to change a script to use fileDialog2.





Example:
---
import maya.cmds as cmds

Old way:
def importImage( fileName, fileType):
   cmds.file( fileName, i=True );
   return 1

cmds.fileBrowserDialog( m=0, fc=importImage, ft='image', an='Import_Image', om='Import' )

Recommended way:
filename = cmds.fileDialog2(fileMode=1, caption="Import Image")
cmds.file( filename[0], i=True );

---
Return:
---


    string: Dialog name

Flags:
---


---
actionName(an): string
    properties: create
    Script to be called when the file is validated.

---
dialogStyle(ds): int
    properties: create
    0 for old style dialog
1 for Windows 2000 style Explorer style
2 for Explorer style with "Shortcut" tip at bottom

---
fileCommand(fc): script
    properties: create
    The script to run on command action

---
fileType(ft): string
    properties: create
    Set the type of file to filter.  By default this can be any one of:
"mayaAscii", "mayaBinary", "mel", "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Illustrator", "image".
plug-ins may define their own types as well.

---
filterList(fl): string
    properties: create, multiuse
    Specify file filters. Used with dialog style
1 and 2. Each string should be a description followed by a
comma followed by a semi-colon separated list of file
extensions with wildcard.

---
includeName(includeName): string
    properties: create
    Include the given string after the actionName in parentheses.
If the name is too long, it will be shortened to fit on the
dialog (for example, /usr/alias/commands/scripts/fileBrowser.mel
might be shortened to /usr/...pts/fileBrowser.mel)

---
mode(m): int
    properties: create
    Defines the mode in which to run the file brower:

0 for read
1 for write
2 for write without paths (segmented files)
4 for directories have meaning when used with the action

+100 for returning short names

---
operationMode(om): string
    properties: create
    Enables the option dialog. Valid strings are:

"Import"
"Reference"
"SaveAs"
"ExportAll"
"ExportActive"

---
tipMessage(tm): string
    properties: create
    Message to be displayed at the bottom of the style 2 dialog box.

---
windowTitle(wt): string
    properties: create
    Set the window title of a style 1 or 2 dialog box

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fileBrowserDialog.html 
    """


def fileDialog(flagapplication: boolean, flagdefaultFileName: string, flagdirectoryMask: string, flagmode: int, flagtitle: string) -> string:
    """Synopsis:
---
---
 fileDialog([application=boolean], [defaultFileName=string], [directoryMask=string], [mode=int], [title=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fileDialog is undoable, NOT queryable, and NOT editable.
See below for an example of how to change a script to use fileDialog2.




Example:
---
import maya.cmds as cmds

Old way:
cmds.fileDialog()
cmds.fileDialog( directoryMask='/usr/u/bozo/myFiles/*.ma' )
cmds.fileDialog( dm='*.cc' )

Recommended way:
cmds.fileDialog2(startingDirectory ="/usr/u/bozo/myFiles/", fileFilter="Maya Ascii (*.ma)")

---
Return:
---


    string: Name of dialog

Flags:
---


---
application(app): boolean
    properties: create
    This is a "Mac" only flag. This brings up the dialog which
selects only the application bundle.

---
defaultFileName(dfn): string
    properties: create
    Set default file name. This flag is available under "write" mode

---
directoryMask(dm): string
    properties: create
    This can be used to specify what directory and file names
will be displayed in the dialog.  If not specified, the
current directory will be used, with all files displayed.
The string may contain a path name, and must contain a
wild-carded file specifier. (eg "*.cc" or "/usr/u/*") If
just a path is specified, then the last directory in the
path is taken to be a file specifier, and this will not
produce the desired results.

---
mode(m): int
    properties: create
    Defines the mode in which to run the file dialog:

0 for read
1 for write

Write mode can not be used in conjunction with the -application flag.

---
title(t): string
    properties: create
    Set title text. The default value under "write" mode is "Save As". The default value under "read" mode is "Open".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fileDialog.html 
    """


def fileDialog2(flagbuttonBoxOrientation: int, flagcancelCaption: string, flagcaption: string, flagdialogStyle: int, flagfileFilter: string, flagfileMode: int, flagfileTypeChanged: script, flaghideNameEdit: boolean, flagokCaption: string, flagoptionsUICancel: script, flagoptionsUICommit: script, flagoptionsUICommit2: script, flagoptionsUICreate: script, flagoptionsUIInit: script, flagoptionsUITitle: string, flagreturnFilter: boolean, flagselectFileFilter: string, flagselectionChanged: script, flagsetProjectBtnEnabled: boolean, flagstartingDirectory: string) -> string:
    """Synopsis:
---
---
 fileDialog2([buttonBoxOrientation=int], [cancelCaption=string], [caption=string], [dialogStyle=int], [fileFilter=string], [fileMode=int], [fileTypeChanged=script], [hideNameEdit=boolean], [okCaption=string], [optionsUICancel=script], [optionsUICommit=script], [optionsUICommit2=script], [optionsUICreate=script], [optionsUIInit=script], [optionsUITitle=string], [returnFilter=boolean], [selectFileFilter=string], [selectionChanged=script], [setProjectBtnEnabled=boolean], [startingDirectory=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fileDialog2 is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

basicFilter = "*.mb"
cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2)

singleFilter = "All Files (*.*)"
cmds.fileDialog2(fileFilter=singleFilter, dialogStyle=2)

multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2)

---
Return:
---


    string: array

Flags:
---


---
buttonBoxOrientation(bbo): int
    properties: create
    1 Vertical button box layout. Cancel button is below the accept button. 
2 Horizontal button box layout. Cancel button is to the right of the accept button.

---
cancelCaption(cc): string
    properties: create
    If the dialogStyle flag is set to 2 then this provides a caption for the
Cancel button within the dialog.

---
caption(cap): string
    properties: create
    Provide a title for the dialog.

---
dialogStyle(ds): int
    properties: create
    1 On Windows or Mac OS X will use a native style file dialog.
2 Use a custom file dialog with a style that is consistent across platforms.

---
fileFilter(ff): string
    properties: create
    Provide a list of file type filters to the dialog.  Multiple filters should be
separated by double semi-colons.  See the examples section.

---
fileMode(fm): int
    properties: create
    Indicate what the dialog is to return.

0 Any file, whether it exists or not.
1 A single existing file.
2 The name of a directory.  Both directories and files are displayed in the dialog.
3 The name of a directory.  Only directories are displayed in the dialog.
4 The names of one or more existing files.

---
fileTypeChanged(ftc): script
    properties: create
    MEL only.  The string is interpreted as a MEL callback, to be called
when the user-selected file type changes.  The callback is of the form:

global proc MyCustomFileTypeChanged(string $parent, string $newType)

The parent argument is the parent layout into which controls have been
added using the optionsUICreate flag.  The newType argument is the new
file type.

---
hideNameEdit(hne): boolean
    properties: create
    Hide name editing input field.

---
okCaption(okc): string
    properties: create
    If the dialogStyle flag is set to 2 then this provides a caption for the
OK, or Accept, button within the dialog.

---
optionsUICancel(oca): script
    properties: create
    MEL only.  The string is interpreted as a MEL callback, to be called
when the dialog is cancelled (with Cancel button or close button to close window).
The callback is of the form:

global proc MyCustomOptionsUICancel()

---
optionsUICommit(ocm): script
    properties: create
    MEL only.  The string is interpreted as a MEL callback, to be called
when the dialog is successfully dismissed.  It will not be called if
the user cancels the dialog, or closes the window using window title
bar controls or other window system means.  The callback is of the form:

global proc MyCustomOptionsUICommit(string $parent)

The parent argument is the parent layout into which controls have been
added using the optionsUICreate flag.

---
optionsUICommit2(oc2): script
    properties: create
    MEL only.  As optionsUICommit, the given string is interpreted as a MEL
callback, to be called when the dialog is successfully dismissed. The
difference is that this callback takes one additional argument which is
the file name selected by the user before the dialog validation.
It will not be called if the user cancels the dialog, or closes the window using
window title bar controls or other window system means.  The callback is of the form:

global proc MyCustomOptionsUICommit(string $parent, string $selectedFile)

The parent argument is the parent layout into which controls have been
added using the optionsUICreate flag.

---
optionsUICreate(ocr): script
    properties: create
    MEL only.  The string is interpreted as a MEL callback, to be called
on creation of the file dialog.  The callback is of the form:

global proc MyCustomOptionsUISetup(string $parent)

The parent argument is the parent layout into which controls can be
added.  This parent is the right-hand pane of the file dialog.

---
optionsUIInit(oin): script
    properties: create
    MEL only.  The string is interpreted as a MEL callback, to be called
just after file dialog creation, to initialize controls.  The callback is of
the form:

global proc MyCustomOptionsUIInitValues(string $parent, string $filterType)

The parent argument is the parent layout into which controls have been
added using the optionsUICreate flag.  The filterType argument is the
initial file filter.

---
optionsUITitle(oti): string
    properties: create
    MEL only. If optionsUICreate is set, user can set a custom title
to their option window using this flag. If no title is desired, an
empty string i.e. "" can be used.

---
returnFilter(rf): boolean
    properties: create
    If true, the selected filter will be returned as the last item in the string array along
with the selected files.

---
selectFileFilter(sff): string
    properties: create
    Specify the initial file filter to select.  Specify just the begining text and not the full wildcard spec.

---
selectionChanged(sc): script
    properties: create
    MEL only.  The string is interpreted as a MEL callback, to be called
when the user changes the file selection in the file dialog.  The
callback is of the form:

global proc MyCustomSelectionChanged(string $parent, string $selection)

The parent argument is the parent layout into which controls have been
added using the optionsUICreate flag.  The selection argument is the
full path to the newly-selected file.

---
setProjectBtnEnabled(spe): boolean
    properties: create
    Define whether the project button should be enabled

---
startingDirectory(dir): string
    properties: create
    Provide the starting directory for the dialog.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fileDialog2.html 
    """


def fileInfo(flagreferenceNode: string, flagremove: string) -> list[string]:
    """Synopsis:
---
---
 fileInfo([string][string], [referenceNode=string], [remove=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fileInfo is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.fileInfo( 'application', 'maya' )
cmds.fileInfo( 'product', 'Maya Unlimited 4.5' )
cmds.fileInfo( 'version', '4.5' )
cmds.fileInfo( 'cutIdentifier', '200111091529' )
cmds.fileInfo( 'osv', 'IRIX 6.5 04151556 IP32' )

cmds.fileInfo( 'application', query=True )
maya

cmds.fileInfo( query=True )
returns a list of all keyword/value pairs, in the order they were
defined.

---
Return:
---


    list[string]: Command result

Flags:
---


---
referenceNode(rfn): string
    properties: query
    Specify the name of a referenceNode to indicate the scene file to query.
This flag is only valid during query.
                        In query mode, this flag needs a value.

---
remove(rm): string
    properties: create, query
    If the remove flag is specified, the string following it is a keyword to
remove from the list of fileInfo to be saved with the scene file.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fileInfo.html 
    """


def filePathEditor(flagattributeOnly: boolean, flagattributeType: string, flagbyType: string, flagcopyAndRepath: tuple[string, string], flagderegisterType: string, flagforce: boolean, flaglistDirectories: string, flaglistFiles: string, flaglistRegisteredTypes: boolean, flagpreview: boolean, flagrecursive: boolean, flagrefresh: boolean, flagregisterType: string, flagrelativeNames: boolean, flagrepath: string, flagreplaceAll: boolean, flagreplaceField: string, flagreplaceString: tuple[string, string], flagstatus: boolean, flagtemporary: boolean, flagtypeLabel: string, flagunresolved: boolean, flagwithAttribute: boolean) -> None:
    """Synopsis:
---
---
 filePathEditor([attributeOnly=boolean], [attributeType=string], [byType=string], [copyAndRepath=[string, string]], [deregisterType=string], [force=boolean], [listDirectories=string], [listFiles=string], [listRegisteredTypes=boolean], [preview=boolean], [recursive=boolean], [refresh=boolean], [registerType=string], [relativeNames=boolean], [repath=string], [replaceAll=boolean], [replaceField=string], [replaceString=[string, string]], [status=boolean], [temporary=boolean], [typeLabel=string], [unresolved=boolean], [withAttribute=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filePathEditor is undoable, queryable, and NOT editable.
Maya can reference and use external files, such as textures or other Maya
scenes. This command is used to get the information about those file paths and
modify them in bulk.
By default, only the most frequently used types of files are presented to the
user:


Texture
Scene reference
Audio
Image plane


For the command to manage more file types, those must be explicitly requested by
the caller using the "registerType" flag. This flag tells the command about
attributes or nodes that are to reveal their paths when the command is used.


Currently, the attributes specified through this flag must have the
"usedAsFileName" property. Supported nodes are "reference" and plug-in nodes.
For example: "brush.flowerImage" or "reference" can be used as value for this
flag.


Conversely, the "deregisterType" flag can be used to tell the command to stop
handling certain attributes or nodes.


Once the set of attributes and nodes to be searched for external files is
selected, the command can be used to obtain a list of plugs that contain file
names. Additional information can be obtained, such as each file's name,
directory, and report whether the file exists. Additional information about the
associated node or plug can also be obtained, such as its name, type and label.


Finally, the command can be used to perform various manipulations such as
editing the paths, remapping the files or verifying the presence of
identically-named files in target directories. See the "repath",
"copyAndRepath" and "replaceField" flags for more information.


The results of these manipulations can be previewed before they are applied
using the "preview" flag.




Example:
---
import maya.cmds as cmds


---
Return the directories of the external files in the Maya scene.
---

cmds.filePathEditor(query=True, listDirectories="")

---
Return the directories of the external files that are saved at the target
---
location.
---

cmds.filePathEditor(query=True, listDirectories="c:/textures/", status=True)

---
Return the files present in the specified directory, but not including the
---
files in the sub directories.If no specified directory, search all external
---
files in the scene.
---

---
Use "withAttribute" to return the associated plugs.
---

---
Use "status" to return whether the file exists.
---

---
Use "unresolved" to return the broken files only.
---

---
Use "attributeOnly" to return node and attribute name only.
---

---
Use "byType" to specify the node and attribute type.
---

---
For example, if "stone.jpg" exists and it is used by the plug
---
"node1.imageName", then the returned result will be an ordered pair:
---
"stone.jpg node1.imageName 1".
---

cmds.filePathEditor(query=True, listFiles="c:/textures/", withAttribute=True, status=True)
---

---
If "rock.jpg" does not exists and it is used by the plug
---
"node1.imageName", then this broken file and its plug
---
can be found by the command.
---

cmds.filePathEditor(query=True, listFiles="", unresolved=True, withAttribute=True)
---
Result: [u'rock.jpg', u'node1.imageName']
---

---
List files that are used in the specified attribute of imagePlane
---

cmds.filePathEditor(query=True, listFiles="", byType="imagePlane.imageName")
---

---
List all files that are used in the imagePlane node
---

cmds.filePathEditor(query=True, listFiles="", byType="imagePlane")
---

---
Get all nodes or attributes that are using broken files to repath them
---

cmds.filePathEditor(query=True, listFiles="", unresolved=True, attributeOnly=True)
---

---
Get the imagePlane file attributes that are using broken files to repath them
---

cmds.filePathEditor(query=True, listFiles="", unresolved=True, attributeOnly=True, byType="imagePlane.imageName")

---
Return the label for the specified type.
---

---
Strings are only guaranteed to be localized for the default types. For the
---
other types, the strings are user-specified.
---

cmds.filePathEditor(query=True, typeLabel="imagePlane")

---
Register and save a new file type and type label.
---

---
These are persistent and can be used in future sessions.
---

cmds.filePathEditor(registerType="containerBase.iconName", typeLabel="ContainerIcon")

---
Deregister a file type and clean the saved information.
---

cmds.filePathEditor(deregisterType="containerBase.iconName")

---
Register a new non-persistent file type and type label.
---

cmds.filePathEditor(registerType="containerBase.iconName", typeLabel="ContainerIcon", temporary=True)

---
Deregister a file type without affecting the persistent information.
---

cmds.filePathEditor(deregisterType="containerBase.iconName", temporary=True)

---
Return all registered types, including default types.
---

cmds.filePathEditor(query=True, listRegisteredTypes=True)

---
Query the attribute type for a plug instance.
---

cmds.filePathEditor("node1.fileTextureName", query=True, attributeType=True)

---
Refresh all the file path editor's information for the current scene.
---

cmds.filePathEditor(refresh=True)

---
Recursively look for files with the same name in the target directory. Repath
---
the plugs value to those files.
---

---
Use "force" to edit all the given plugs, even if the original path does not
---
exist.
---

---
Use "recursive" to find files recursively and to make sure the files do exist.
---

cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName", repath="e:/textures/",
                                                force=True, recursive=True)

---
Preview the result of an operation without doing it.
---

---
Returns the file name and whether the new file exists. This is returned as a
---
list of pairs.
---

cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName", repath="e:/textures/", preview=True)

---
Replace strings in file paths.
---

---
Here, the string "image" in the directory part will be replaced by "texture".
---

cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName", replaceField="pathOnly", replaceString=("image", "texture"), replaceAll=True)

---
Copy a file from the source to the destination and repath the plug data to the new file.
---

---
Use "force" to overwrite the file at the destination if it has a name clash.
---

cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName",  copyAndRepath=("e:/textures", "g:/image"), force=True)

---


Flags:
---


---
attributeOnly(ao): boolean
    properties: query
    Used with "listFiles" to return the node and attribute name that
are using the files.

---
attributeType(at): string
    properties: query
    Query the attribute type for the specified plug.

---
byType(bt): string
    properties: query
    Used with "listFiles" to query files that are
used by the specified node type or attribute type.
                        In query mode, this flag needs a value.

---
copyAndRepath(cr): [string, string]
    properties: create
    Copy a source file to the destination path and repath the plug data to the new
file.
The source file must have the same name as the one in the plug.
The command will look for the file at the specified location first. If not
found, the command will try to use the original file in the plug.
If the file is still not found, nothing is done.

---
deregisterType(dt): string
    properties: create
    Deregister a file type from the list of registered types so the command stops
handling it.
Unless the "temporary" flag is used, the type will be removed from the
preferences will not reappear on application restart. When the "temporary" flag
is specified, the deregistration is only effective for the current session.
The deregistration will be rejected if the type has already been unregistered.
However, it is valid to deregister permanently (without the "temporary" flag)
a type after it has been temporarily deregistered.

---
force(f): boolean
    properties: create
    Used with flag "repath" to repath all files to the new location, including
the resolved files. Otherwise, "repath" will only deal with the missing files.
Used with flag "copyAndRepath" to overwrite any colliding file at the
destination. Otherwise, "copyAndRepath" will use the existing file at the
destination instead of overwriting it.
The default value is off.

---
listDirectories(ld): string
    properties: query
    List all sub directories of the specified directory.  Only directories
containing at least one file whose type is registered (see "registerType") will
be listed.
If no directory is provided, all directories applicable to the scene will be
returned.
                        In query mode, this flag needs a value.

---
listFiles(lf): string
    properties: query
    List files in the specified directory. No recursion in subdirectories will be
performed.
                        In query mode, this flag needs a value.

---
listRegisteredTypes(lrt): boolean
    properties: query
    Query the list of registered attribute types. The registered types include
the auto-loaded types from the preference file and the types explicitly
registered by the user, both with and without the "temporary" flag.

---
preview(p): boolean
    properties: create
    Used with "repath", "replaceString" or "copyAndRepath" to preview the result of
the operation instead of excuting it.
When it is used with "repath" or "replaceString", the command returns the new
file path and a status flag indicating whether the new file exists (1) or not
(0).
The path name and the file status are listed in pairs.
When it is used with "copyAndRepath", the command returns the files that need
copying.

---
recursive(rc): boolean
    properties: create
    Used with flag "repath" to search the files in the target directory and its
subdirectories recursively. If the flag is on, the command will repath the plug
to a file that has the same name in the target directory or sub directories.
If the flag is off, the command will apply the directory change without
verifying that the resulting file exists.

---
refresh(rf): boolean
    properties: create
    Clear and re-collect the file information in the scene.
The command does not automatically track file path modifications in the scene.
So it is the users responsibility to cause refreshes in order to get up-to-date
information.

---
registerType(rt): string
    properties: create
    Register a new file type that the command will handle and recognize from now on.
Unless the "temporary" flag is used, the registered type is saved in the
preferences and reappears on application restart.
The new type will be rejected if it collides with an existing type or label.
One exception to this is when registering a type without the "temporary" flag
after the type has been registered with it. This is considered as modifying
the persistent/temporary property of the existing type, rather than registering
a new type.

---
relativeNames(rel): boolean
    properties: query
    Used with "listDirectories" or "listFiles" to return the relative path
of each directory or file.  Paths are relative to the current project
folder.
If a file or the directory is not under the current project folder,
the returned path will still be a full path.

---
repath(r): string
    properties: create
    Replace the directory part of a file path with a specified location.
The file name will be preserved.

---
replaceAll(ra): boolean
    properties: create
    Used with flag "replaceString", specifies how many times the matched string will
be replaced. When the flag is false, only the first matched string will be
replaced. Otherwise, all matched strings will be replaced.
The default value is false.

---
replaceField(rfd): string
    properties: create
    Used with the "replaceString" flag to control the scope of the replacement.
Possible values are:
"pathOnly" - only replace strings in the directory part.
"nameOnly" - only replace strings in the file name, without the directory.
"fullPath" - replace strings anywhere in the full name.
The default argument is "fullPath".

---
replaceString(rs): [string, string]
    properties: create
    Replace the target string with the new string in the file paths.
The flag needs two arguments: the first one is the target string and the second
one is the new string.
See the "replaceField" and "replaceAll" flags to control how the replacement is
performed.

---
status(s): boolean
    properties: query
    Used with "listFiles", this will cause the returned list of files to include
one status flag per file: 0 if it cannot be resolved and 1 if it can.
Used with "listDirectories", this will cause the returned list of directories to
include one status flag per directory: 0 if it cannot be resolved, 1 if it can
and 2 if the resolution is partial.
The status will be interleaved with the file/directory names, with the name
appearing first. See the example for "listFiles".  See the "withAttribute" flag
for another way of getting per-file information.  When multiple per-entry items
appear in the list (e.g.: plug name), the status is always last.

---
temporary(tmp): boolean
    properties: create
    Make the effect of the "register"/"deregister" flag only applicable in the
current session.
Normally, a type registration/deregistration is permanent and is made persistent
via a preference file. When the "temporary" flag is specified, the changes will
not be saved to the preference file. When the application restarts, any type
that has been previously temporarily registered will not appear and any type
that was temporarily deregistered will re-appear.

---
typeLabel(tl): string
    properties: create, query
    Used with "registerType" to set the label name for the new file type.
Used with "query" to return the type label for the specified attribute type.
For default types, the type label is the localized string.
For other types, the type label is supplied by user.
                        In query mode, this flag needs a value.

---
unresolved(u): boolean
    properties: query
    Used with "listFiles" to query the unresolved files
that are being used in the scene.

---
withAttribute(wa): boolean
    properties: query
    Used with "listFiles" to return the name of the plug using a given file.
For example, if "file.jpg" is used by the plug "node1.fileTextureName",
then the returned string will become the pair
"file.jpg node1.fileTextureName".  See the "status" flag for another
way to get per-file information.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filePathEditor.html 
    """


def filletCurve(flagbias: linear, flagblendControl: boolean, flagcaching: boolean, flagcircular: boolean, flagconstructionHistory: boolean, flagcurveParameter1: float, flagcurveParameter2: float, flagdepth: linear, flagfreeformBlend: boolean, flagjoin: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagradius: linear, flagreplaceOriginal: boolean, flagtrim: boolean) -> list[string]:
    """Synopsis:
---
---
 filletCurve(
[curve] [curve]
    , [bias=linear], [blendControl=boolean], [caching=boolean], [circular=boolean], [constructionHistory=boolean], [curveParameter1=float], [curveParameter2=float], [depth=linear], [freeformBlend=boolean], [join=boolean], [name=string], [nodeState=int], [object=boolean], [radius=linear], [replaceOriginal=boolean], [trim=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filletCurve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a circular fillet (by default) having radius 2.5 between the
active curves:
cmds.filletCurve( r=2.5 )

Create a freeform curve fillet between the two specified curves at
these parameter values:
cmds.filletCurve( 'curve1', 'curve2', cir=True, cp1=0.5, cp2=2.0 )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
bias(b): linear
    properties: create, query, edit
    Adjusting the bias value causes the fillet curve to be skewed to one of the input curves. Available only if blendControl is true.
Default: 0.0

---
blendControl(bc): boolean
    properties: create, query, edit
    If true then depth and bias can be controlled. Otherwise, depth and bias are not available options.
Default: false

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
circular(cir): boolean
    properties: create, query, edit
    Curve fillet will be created as circular if true or freeform if false.
Default: true

---
curveParameter1(cp1): float
    properties: create, query, edit
    Parameter where fillet curve will contact the primary input curve.
Default: 0.0

---
curveParameter2(cp2): float
    properties: create, query, edit
    Parameter where fillet curve will contact the secondary input curve.
Default: 0.0

---
depth(d): linear
    properties: create, query, edit
    Adjusts the depth of the fillet curve. Available only if blendControl is true.
Default: 0.5

---
freeformBlend(fb): boolean
    properties: create, query, edit
    The freeform type is blend if true or tangent if false. Available if the fillet type is freeform.
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
radius(r): linear
    properties: create, query, edit
    The radius if creating a circular fillet.
Default: 1.0

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
join(jn): boolean
    properties: create
    Should the fillet be joined?

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

---
trim(t): boolean
    properties: create
    Should the fillet be trimmed?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filletCurve.html 
    """


def filter(flagname: string, flagtype: string) -> string:
    """Synopsis:
---
---
 filter([name=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filter is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.filter( t='filterEuler', n='houston' )
cmds.filter( 'houston', edit=True, irx=0.0 )
cmds.filter( 'houston', query=True, irx=True )

---
Return:
---


    string: filter name

Flags:
---


---
name(n): string
    properties: create, query, edit
    Name for created filter

---
type(t): string
    properties: create, query, edit
    Filter type to create, One of:

filterEuler            Euler angle "demangler"
filterResample        
Resamples input data at fixed output rate with several filtering options
filterSimplify        
Combines groups of data points that are almost linear into lines segments
filterClosestSample    
Resamples input data a fixed output rate using the closest sample point

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filter.html 
    """


def filterButterworthCtx(flagapply: boolean, flagcutoffFrequency: float, flagendTime: time, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagkeepKeysOnFrame: boolean, flagname: string, flagsamplingRate: float, flagselectedKeys: boolean, flagstartTime: time) -> string:
    """Synopsis:
---
---
 filterButterworthCtx(
contextName
    , [apply=boolean], [cutoffFrequency=float], [endTime=time], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [keepKeysOnFrame=boolean], [name=string], [samplingRate=float], [selectedKeys=boolean], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filterButterworthCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Create a context
ctx = cmds.filterButterworthCtx()

Activate the tool context
cmds.setToolTo( ctx )

Adjust the Butterworth cutoff frequency to selected keys.
cmds.filterButterworthCtx( ctx, e=True, sk=True, cof=3.0 )

Apply the current settings to the selected curves.
cmds.filterButterworthCtx( ctx, e=True, apply=True )

---
Return:
---


    string: Context name

Flags:
---


---
apply(a): boolean
    properties: edit
    When specified, finalizes the current context state
and records the command for the operation. This is equivalent
to completing the tool action without exiting the current
tool context.

---
cutoffFrequency(cof): float
    properties: query, edit
    Specifies the cutoff frequency setting of the Butterworth filter.
Default is 7.0.

---
endTime(e): time
    properties: query, edit
    Specifies the end time portion of the time range for this filter.
This time range is used when selectedKeys is false.

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
keepKeysOnFrame(kof): boolean
    properties: query, edit
    When true, the Butterworth filter will reposition output keys to
whole frames for the specified sampling rate.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
samplingRate(sr): float
    properties: query, edit
    Specifies the sampling rate setting of the Butterworth filter.
Default is 30.0.

---
selectedKeys(sk): boolean
    properties: query, edit
    If true, sets the filter to apply to the selected keys. Otherwise,
the filter applies to the specified time range. Default is on.

---
startTime(s): time
    properties: query, edit
    Specifies the start time portion of the time range for this filter.
This time range is used when selectedKeys is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filterButterworthCtx.html 
    """


def filterCurve(flagcutoffFrequency: float, flagendTime: time, flagfilter: string, flagkeepKeysOnFrame: boolean, flagkernel: string, flagkeySync: boolean, flagmaxTimeStep: float, flagminTimeStep: float, flagperiod: float, flagprecision: float, flagprecisionMode: int, flagpreserveKeyTangent: string, flagsampleCount: int, flagsamplingRate: float, flagselectedKeys: boolean, flagstartTime: time, flagtimeTolerance: float, flagtolerance: float, flaguseQuaternion: boolean, flagwidth: time) -> int:
    """Synopsis:
---
---
 filterCurve([cutoffFrequency=float], [endTime=time], [filter=string], [keepKeysOnFrame=boolean], [kernel=string], [keySync=boolean], [maxTimeStep=float], [minTimeStep=float], [period=float], [precision=float], [precisionMode=int], [preserveKeyTangent=string], [sampleCount=int], [samplingRate=float], [selectedKeys=boolean], [startTime=time], [timeTolerance=float], [tolerance=float], [useQuaternion=boolean], [width=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filterCurve is undoable, NOT queryable, and NOT editable.butterwortheulergaussiankeyReducerpeakRemoverkeySyncresamplesimplify


Example:
---
import maya.cmds as cmds


cmds.filterCurve( 'nurbsCone1_rotateX', 'nurbsCone1_rotateY', 'nurbsCone1_rotateZ' )

---
Return:
---


    int: The number of filtered curves

Flags:
---


---
cutoffFrequency(cof): float
    properties: create
    Defines the cutoff frequency (in Hz) for the Butterworth filter.

---
endTime(e): time
    properties: create
    Specify the end time of the section to filter. If not specified, the last
key of the animation curve is used to define the end time.

---
filter(f): string
    properties: create
    Specifies the filter type to use. The avalible filters are:
butterworth
euler (default)
gaussian
keyReducer
peakRemover
keySync
resample
simplify

---
keepKeysOnFrame(kof): boolean
    properties: create
    When specified, a secondary filter pass is applied to position keys on whole
frames. This flag is only supported by the Butterworth filter.

---
kernel(ker): string
    properties: create
    The resample kernel is a decimation resampling filter used to resample
dense data. It works on the keyframes and may not produce the desired results
when used with sparse data.

The resample filter converts from either uniform or non-uniform
timestep input data samples to the specified uniform timeStep. Various
time domain filters are available and are specified with the kernel
flag which selects the resampling kernel applied to the keyframes
on the animation curves.


Kernel Values
closest
 Closest sample to output timestamp
lirp
 Linear interpolation between closest samples
box
 Box filter: moving average
triangle
 Triangle filter: (1 - |x|)  weighted moving average
gaussian2
 Gaussian2 Filter: (2^(-2x*x))  weighted moving average
gaussian4
 Gaussian4 Filter: (2^(-4x*x))  weighted moving average


This filter is only targeted at decimation resampling
-- interpolation resampling is basically unsupported.  If your
output framerate is much higher than your input frame rate
(approximate, as the input timestep is not assumed to be regular)
the lirp and triangle will interpolate (usually) and the rest will
either average, or use the closest sample (depending on the
phase and frequency of the input).  However this mode of operation
may not give the expected result.

---
keySync(ks): boolean
    properties: create
    When specified, a secondary filter pass is applied that adds a key to sibling
curves (X,Y,Z) for each key that is encountered. This flag is only supported by the
Key Reducer filter.

---
maxTimeStep(mxs): float
    properties: create
    Simplify filter.

---
minTimeStep(mns): float
    properties: create
    Simplify filter.

---
period(per): float
    properties: create
    Resample filter

---
precision(pre): float
    properties: create
    Defines the precision parameter.
For the Key Reducer filter, this parameter specifies the error limit between the
source and output curves. Greater values reduce precision. Lower values increase
precision.

---
precisionMode(pm): int
    properties: create
    Defines whether the precision value should be treated as:
0: An absolute value
1: A percentage.

---
preserveKeyTangent(pkt): string
    properties: create, multiuse
    When specified, keys whose in or out tangent type match the
specified type are preserved.
Supported tangent types:
fixed
linear
flat
smooth
step
clamped
plateau
stepnext
auto
This flag is only supported by the Key Reducer filter.

---
sampleCount(sc): int
    properties: create
    Defines the Gaussian filter kernel dimension.

---
samplingRate(sr): float
    properties: create
    Defines the rate at which keys are added to the Butterworth filtered curve in
frames per second (FPS).

---
selectedKeys(sk): boolean
    properties: create
    When specified, the filter is only applied to selected keys. This flag
supercedes the startTime/endTime specification.

---
startTime(s): time
    properties: create
    Specify the start time to filter. If not specified, then the first key in the
animation curve is used to get the start time.

---
timeTolerance(tto): float
    properties: create
    Simplify filter.

---
tolerance(tol): float
    properties: create
    Simplify filter.

---
useQuaternion(uq): boolean
    properties: create
    Enable to use quaternion instead of euler.

---
width(w): time
    properties: create
    Defines the width of the Gaussian filter.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filterCurve.html 
    """


def filterExpand(flagexpand: boolean, flagfullPath: boolean, flagselectionMask: int, flagsymActive: boolean, flagsymNegative: boolean, flagsymPositive: boolean, flagsymSeam: boolean) -> list[string]:
    """Synopsis:
---
---
 filterExpand([expand=boolean], [fullPath=boolean], [selectionMask=int], [symActive=boolean], [symNegative=boolean], [symPositive=boolean], [symSeam=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filterExpand is undoable, NOT queryable, and NOT editable.

Object Type Mask 
 Handle                         0            
 Nurbs Curves                     9            
 Nurbs Surfaces                 10        
 Nurbs Curves    On Surface          11        
 Polygon                          12        
 Locator XYZ                     22        
 Orientation Locator             23        
 Locator UV                     24        
 Control Vertices (CVs)         28        
 Edit Points                     30        
 Polygon Vertices              31        
 Polygon Edges                 32        
 Polygon Face                     34        
 Polygon UVs                      35        
 Subdivision Mesh Points         36        
 Subdivision Mesh Edges         37        
 Subdivision Mesh Faces         38        
 Curve Parameter Points         39        
 Curve Knot                     40        
 Surface Parameter Points          41        
 Surface Knot                     42        
 Surface Range                 43        
 Trim Surface Edge             44        
 Surface Isoparms              45        
 Lattice Points                 46        
 Particles                     47        
 Scale Pivots                     49        
 Rotate Pivots                 50        
 Select Handles                 51        
 Subdivision Surface             68        
 Polygon Vertex Face              70        
 NURBS Surface Face              72        
 Subdivision Mesh UVs             73        





Example:
---
import maya.cmds as cmds

Returns any selected isoparms (mask 45) as individual items
(because of "ex=True").
cmds.filterExpand( ex=True, sm=45 )

Returns any selected CVs (mask 28) as compact items.  For example,
  if curve.cv[0:3] is selected, then "curve.cv[0:3]" is returned.
  If "ex=True", then four items are returned, one for each CV.
cmds.filterExpand( ex=False, sm=28 )

Returns any selected CVs (mask 28) and edit points (mask 30).
cmds.filterExpand( sm=(28,30) )

Returns any selected nurbs curves.
cmds.filterExpand( sm=9 )

Returns any selected nurbs curves-on-surface.
cmds.filterExpand( sm=11 )

return the poly faces (mask 34) from the specified arguments
cmds.filterExpand(["pCube1.f[1]","pCube1.f[4]","pCube1.vtx[0:3]"], sm=34)

---
Return:
---


    list[string]: Command result

Flags:
---


---
expand(ex): boolean
    properties: create
    Each item is a single entity if this is true.  Default is true.

---
fullPath(fp): boolean
    properties: create
    If this is true and the selection item is a DAG object, return its
full selection path, instead of the name of the object only when
this value is false.  Default is false.

---
selectionMask(sm): int
    properties: create, multiuse
    Specify the selection mask

---
symActive(sma): boolean
    properties: create
    If symmetry is enabled only return the components on the active symmetry
side of the object. This flag has no effect if symmetry is not active.

---
symNegative(smn): boolean
    properties: create
    If symmetry is enabled only return the components on the negative
side of the object relative to the current symmetry plane. This flag has
no effect if symmetry is not active.

---
symPositive(smp): boolean
    properties: create
    If symmetry is enabled only return the components on the positive
side of the object relative to the current symmetry plane. This flag has
no effect if symmetry is not active.

---
symSeam(sms): boolean
    properties: create
    If symmetry is enabled only return the components that lie equally on both sides
of the object relative to the current symmetry plane. This flag has
no effect if symmetry is not active.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filterExpand.html 
    """


def filterGaussianCtx(flagapply: boolean, flagendTime: time, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagsampleCount: int, flagselectedKeys: boolean, flagstartTime: time, flaguseQuaternion: boolean, flagwidth: time) -> string:
    """Synopsis:
---
---
 filterGaussianCtx(
contextName
    , [apply=boolean], [endTime=time], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [sampleCount=int], [selectedKeys=boolean], [startTime=time], [useQuaternion=boolean], [width=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filterGaussianCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Create a context
ctx = cmds.filterGaussianCtx()

Set the context to the new context just created
cmds.setToolTo(ctx)

Adjust the width and sample count to selected curves.
cmds.filterGaussianCtx(ctx, e=True, width=3, sampleCount=8)

Apply current settings to the real curves.
cmds.filterGaussianCtx(ctx, e=True, a=True)

---
Return:
---


    string: Context name

Flags:
---


---
apply(a): boolean
    properties: edit
    When specified, finalizes the current context state
and records the command for the operation. This is equivalent
to completing the tool action without exiting the current
tool context.

---
endTime(e): time
    properties: query, edit
    Specifies the end time portion of the time range for this filter.
This time range is used when selectedKeys is false.

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
sampleCount(sc): int
    properties: query, edit
    This parameter specifies the number of neighbor will be sampled.

---
selectedKeys(sk): boolean
    properties: query, edit
    If true, sets the filter to apply to the selected keys. Otherwise,
the filter applies to the specified time range. Default is on.

---
startTime(s): time
    properties: query, edit
    Specifies the start time portion of the time range for this filter.
This time range is used when selectedKeys is false.

---
useQuaternion(uq): boolean
    properties: query, edit
    When this is enabled, the filter will first convert the curves
(rotation channel curves, 3 sibling requires at the same time)
from Euler space to quaternions. Then apply the gaussian filter
on it. Convert it back from Quaternions back to Euler space eventually.

---
width(w): time
    properties: query, edit
    This parameter specifies the width of the gaussian kernel shape.
Wider width will

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filterGaussianCtx.html 
    """


def filterInstances(flagshapes: boolean) -> list[string]:
    """Synopsis:
---
---
 filterInstances([shapes=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filterInstances is undoable, queryable, and NOT editable.
Returns a string array containing all matching selection items or
true/false if the query flag is used.




Example:
---
import maya.cmds as cmds

Returns true if any selected object(s) are instances of another selected object.
cmds.filterInstances( q=True )

Returns a new selection list with duplicate instances removed.
cmds.filterInstances()

---
Return:
---


    list[string]: Command result

Flags:
---


---
shapes(s): boolean
    properties: create
    If this is true then the command will check for an instanced shapes
below the selected transform(s) and use them to decide whether the
parent transforms should be considered instances. Default is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filterInstances.html 
    """


def filterKeyReducerCtx(flagapply: boolean, flagendTime: time, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagkeySync: boolean, flagname: string, flagprecision: float, flagprecisionMode: int, flagpreserveKeyTangent: string, flagselectedKeys: boolean, flagstartTime: time) -> string:
    """Synopsis:
---
---
 filterKeyReducerCtx(
contextName
    , [apply=boolean], [endTime=time], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [keySync=boolean], [name=string], [precision=float], [precisionMode=int], [preserveKeyTangent=string], [selectedKeys=boolean], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filterKeyReducerCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Create a context
ctx = cmds.filterKeyReducerCtx()

Activate the tool context
cmds.setToolTo( ctx )

Adjust the KeyReducer cutoff frequency to selected keys.
cmds.filterKeyReducerCtx( ctx, e=True, sk=True, pm=1, pre=0.5 )

Apply the current settings to the selected curves.
cmds.filterKeyReducerCtx( ctx, e=True, apply=True )

---
Return:
---


    string: Context name

Flags:
---


---
apply(a): boolean
    properties: edit
    When specified, finalizes the current context state
and records the command for the operation. This is equivalent
to completing the tool action without exiting the current
tool context.

---
endTime(e): time
    properties: query, edit
    Specifies the end time portion of the time range for this filter.
This time range is used when selectedKeys is false.

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
keySync(ks): boolean
    properties: query, edit
    When true, a secondary filter pass is applied that adds a key to sibling
curves (X,Y,Z) for each key that is encountered.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
precision(pre): float
    properties: query, edit
    Defines the precision parameter.

For the Key Reducer filter, this parameter specifies the error limit between the
source and output curves. Greater values reduce precision. Lower values increase
precision.

---
precisionMode(pm): int
    properties: query, edit
    Specifies the precision mode for the Key Reducer filter. Avaiable
modes are:

0: Absolute value.
1: Percentage

Default is 1 (percentage mode).

---
preserveKeyTangent(pkt): string
    properties: query, edit, multiuse
    When specified, keys whose in or out tangent type match the
specified type are preserved.

Supported tangent types:

fixed
linear
flat
smooth
step
clamped
plateau
stepnext
auto

---
selectedKeys(sk): boolean
    properties: query, edit
    If true, sets the filter to apply to the selected keys. Otherwise,
the filter applies to the specified time range. Default is on.

---
startTime(s): time
    properties: query, edit
    Specifies the start time portion of the time range for this filter.
This time range is used when selectedKeys is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filterKeyReducerCtx.html 
    """


def filterStudioImport(flagconvertShellToPoly: boolean, flagincludeCameras: boolean, flagincludeLights: boolean, flagtransferDirectoryName: string) -> None:
    """Synopsis:
---
---
 filterStudioImport([convertShellToPoly=boolean], [includeCameras=boolean], [includeLights=boolean], [transferDirectoryName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

filterStudioImport is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.filterStudioImport( includeCameras=False )

---


Flags:
---


---
convertShellToPoly(sp): boolean
    properties: create
    If true, shells in the input will be converted to triangular meshes.
    If false, any/all shells encountered will be groups of surfaces.

---
includeCameras(ic): boolean
    properties: create
    If true, cameras in the input to "studioImport" will be translated.
    If false, any/all cameras encountered by "studioImport" will be ignored.

---
includeLights(il): boolean
    properties: create
    If true, lights in the input to "studioImport" will be translated.
    If false, any/all lights encountered by "studioImport" will be ignored.

---
transferDirectoryName(td): string
    properties: create
    If set (non-empty), use as directory for storing imbedded binary files,
    else use the directory given by "theTempDirectory->fullName()".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/filterStudioImport.html 
    """


def findDeformers() -> None:
    """Synopsis:
---
---
 findDeformers(
[objects...]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

findDeformers is undoable, NOT queryable, and NOT editable.
If no shapes are specified on the command then the curently selected
shapes are used.




Example:
---
import maya.cmds as cmds

cmds.findDeformers('ball')

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/findDeformers.html 
    """


def findKeyframe(flaganimation: string, flagattribute: string, flagcontrolPoints: boolean, flagcurve: boolean, flagfloat: floatrange, flaghierarchy: string, flagincludeUpperBound: boolean, flagindex: uint, flagshape: boolean, flagtime: timerange, flagtimeSlider: boolean, flagwhich: string) -> time:
    """Synopsis:
---
---
 findKeyframe(
[animatedObject]
    , [animation=string], [attribute=string], [controlPoints=boolean], [curve=boolean], [float=floatrange], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [shape=boolean], [time=timerange], [timeSlider=boolean], [which=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

findKeyframe is undoable, NOT queryable, and NOT editable.
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

This command will return the time (in current units) of the requested
key. For the relative direction methods (next, previous) if
-time is NOT specified they will use current time.
If the specified object is not animated the command will return
the current time.




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

Find the next key from the current time, based upon the ticks
displayed within the time slider
---

cmds.findKeyframe( timeSlider=True, which="next" )

Find the next key for nurbsCone1 after time 25
---

cmds.findKeyframe( 'nurbsCone1', time=(25,25), which="next" )

Find the curves driving the nurbsCone1's rotateX attribute
---

cmds.findKeyframe( 'nurbsCone1', curve=True, at='rotateX' )

---
Return:
---


    time: Command result

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
curve(c): boolean
    properties: create
    Return a list of the existing curves driving the selected object
or attributes. The which, index, floatRange, timeRange, and
includeUpperBound flags are ignored when this flag is used.

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
timeSlider(ts): boolean
    properties: create
    Get the next key time from the ticks displayed in the
time slider. If this flag is set, then the -an/animation flag
is ignored.

---
which(w): string
    properties: create
    next | previous | first | last
How to find the key

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/findKeyframe.html 
    """


def findType(flagdeep: boolean, flagexact: boolean, flagforward: boolean, flagtype: string) -> list[string]:
    """Synopsis:
---
---
 findType([deep=boolean], [exact=boolean], [forward=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

findType is NOT undoable, NOT queryable, and NOT editable.findType


Example:
---
import maya.cmds as cmds


cmds.createNode( 'transform', name='silly' )
cmds.createNode( 'transform', name='putty' )
cmds.connectAttr( 'putty.tx', 'silly.tx' )

Find transform nodes connected to node "silly"
---

cmds.findType( 'silly', deep=True, type='transform' )
Result: [u'silly', u'putty'] ---


Look forward from a selected item
---

cmds.select( 'silly' )
cmds.findType( deep=True, forward=True, type='transform' )
Result: [u'silly'] ---


---

Find all time nodes
---

cmds.setKeyframe( t=10 )
cmds.findType( type='time', deep=True, exact=True )
Result: [u'time1'] ---


---

Find all anim curve nodes
---

cmds.findType( type="animCurve", deep=True )
Result: [u'pairBlend1_inTranslateX1', u'silly_translateY', u'silly_translateZ', u'silly_visibility', u'silly_rotateX', u'silly_rotateY', u'silly_rotateZ', u'silly_scaleX', u'silly_scaleY', u'silly_scaleZ'] ---


---
Return:
---


    list[string]: The list of node(s) of the requested type connected to the given node(s)

Flags:
---


---
deep(d): boolean
    properties: create
    Find all nodes of the given type instead of just the first.

---
exact(e): boolean
    properties: create
    Match node types exactly instead of any in a node hierarchy.

---
forward(f): boolean
    properties: create
    Look forwards (downstream) through the graph rather than backwards
(upstream) for matching nodes.

---
type(t): string
    properties: create
    Type of node to look for (e.g. "transform"). This flag is mandatory.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/findType.html 
    """


def fitBspline(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagtolerance: linear) -> list[string]:
    """Synopsis:
---
---
 fitBspline([caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fitBspline is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.curve( d=1, p=((0.2662494, 0, 10.640916), (-4.71138, 0, 7.070603), (-7.849212, 0, 1.051444), (-6.646792, 0, -3.475301), (-2.499369, 0, -3.770414), (2.041102, 0, -1.381914), (5.408074, 0, 3.095469)), k=(0, 1, 2, 3, 4, 5, 6) )

cmds.fitBspline( ch=1, tol=0.01 )

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
tolerance(tol): linear
    properties: create, query, edit
    Tolerance for the fit.  The resulting curve will be kept
within tolerance of the given points.
Default: 0.1

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fitBspline.html 
    """


def flexor(flagatBones: boolean, flagatJoints: boolean, flagdeformerCommand: string, flaglist: boolean, flagname: string, flagnoScale: boolean, flagtoSkeleton: boolean, flagtype: string) -> list[string]:
    """Synopsis:
---
---
 flexor(
[objects]
    , [atBones=boolean], [atJoints=boolean], [deformerCommand=string], [list=boolean], [name=string], [noScale=boolean], [toSkeleton=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

flexor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a sculpt object with a max displacement of 4.0 at the
selected joint
cmds.flexor( typ='sculpt', dc="sculpt -mxd 4.0", aj=True )

Create a lattice flexor at all joints on the skeleton:
cmds.flexor( type='jointLattice', aj=True, ts=True )

Create a lattice flexor of dimensions 4 6 4 on the selected joint
cmds.flexor( type='jointLattice', dc="lattice -dv 4 6 4 -cp -dualBase true", aj=True)

---
Return:
---


    list[string]: (the names of the new flexor nodes)

Flags:
---


---
atBones(ab): boolean
    properties: create
    Add a flexor at bones. Flexor will be added at each of the
selected bones, or at all bones in the selected skeleton if
the -ts flag is also specified.

---
atJoints(aj): boolean
    properties: create
    Add a flexor at joints. Flexor will be added at each of the
selected joints, or at all joints in the selected skeleton if
the -ts flag is specified.

---
deformerCommand(dc): string
    properties: create
    String representing underlying deformer command string.

---
list(l): boolean
    properties: query
    List all possible types of flexors. Query mode only.

---
name(n): string
    properties: create
    This flag is obsolete.

---
noScale(ns): boolean
    properties: create
    Do not auto-scale the flexor to the size of the nearby geometry.

---
toSkeleton(ts): boolean
    properties: create
    Specifies that flexors will be added to the entire skeleton
rather than just to the selected joints/bones.
This flag is used in conjunction with the -ab and -aj flags.

---
type(typ): string
    properties: create
    Specifies which type of flexor. To see list of valid types,
use the "flexor -query -list" command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/flexor.html 
    """


def floatField(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagenterCommand: script, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmaxValue: float, flagminValue: float, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagreceiveFocusCommand: script, flagshowTrailingZeros: boolean, flagstatusBarMessage: string, flagstep: float, flaguseTemplate: string, flagvalue: float, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 floatField(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [receiveFocusCommand=script], [showTrailingZeros=boolean], [statusBarMessage=string], [step=float], [useTemplate=string], [value=float], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

floatField is undoable, queryable, and editable.-s/step



Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
cmds.floatField()
cmds.floatField( editable=False )
cmds.floatField( minValue=-10, maxValue=10, value=0 )
cmds.floatField( minValue=0, maxValue=1, precision=2 )
cmds.floatField( minValue=-1, maxValue=1, precision=4, step=.01 )
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
false then the field can not be changed interactively.  However,
you can change the field text with the -v/value flag
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
maxValue(max): float
    properties: create, query, edit
    Upper limit of the field.

---
minValue(min): float
    properties: create, query, edit
    Lower limit of the field.

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
showTrailingZeros(tze): boolean
    properties: create, query, edit
    Show trailing zeros or not

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): float
    properties: create, query, edit
    Increment for the invisible slider.   The field value
will change by this amount when the invisible slider is dragged.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): float
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/floatField.html 
    """


def floatFieldGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenable1: boolean, flagenable2: boolean, flagenable3: boolean, flagenable4: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagextraLabel: string, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfFields: int, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagshowTrailingZeros: boolean, flagstatusBarMessage: string, flagstep: float, flaguseTemplate: string, flagvalue: tuple[float, float, float, float], flagvalue1: float, flagvalue2: float, flagvalue3: float, flagvalue4: float, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 floatFieldGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean], [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfFields=int], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]], [showTrailingZeros=boolean], [statusBarMessage=string], [step=float], [useTemplate=string], [value=[float, float, float, float]], [value1=float], [value2=float], [value3=float], [value4=float], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

floatFieldGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label text and
editable float fields.  The label text is optional and one to four
float fields can be created.




Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
cmds.floatFieldGrp( numberOfFields=3, label='Scale', extraLabel='cm', value1=0.3, value2=0.5, value3=0.1 )
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
showTrailingZeros(tze): boolean
    properties: create, edit
    Show trailing zeros or not

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): float
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
value(v): [float, float, float, float]
    properties: create, query, edit
    Values for all fields.

---
value4(v4): float
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/floatFieldGrp.html 
    """


def floatScrollBar(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontal: boolean, flagisObscured: boolean, flaglargeStep: float, flagmanage: boolean, flagmaxValue: float, flagminValue: float, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flagstep: float, flaguseTemplate: string, flagvalue: float, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 floatScrollBar(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean], [largeStep=float], [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [step=float], [useTemplate=string], [value=float], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

floatScrollBar is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( adjustableColumn=True )
cmds.floatScrollBar()
cmds.floatScrollBar( min=-100, max=100, value=0, step=1, largeStep=10 )
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
    Command executed when the value changes.  This command is
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
    Command executed when the value changes by dragging the
scroll bar's value marker.

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
    properties: create, query
    Orientation of the slider.  This flag is true by default,
which corresponds to a horizontally oriented slider.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
largeStep(ls): float
    properties: create, query, edit
    Larger increment for the scroll bar, ie. the increment
used when the press is between the arrow button and the thumb.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxValue(max): float
    properties: create, query, edit
    Upper limit of the scroll bar.

---
minValue(min): float
    properties: create, query, edit
    Lower limit of the scroll bar.

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
step(s): float
    properties: create, query, edit
    Smaller increment for the scroll bar, ie. the increment
used when the arrow buttons are pressed.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): float
    properties: create, query, edit
    Value of the scroll bar.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/floatScrollBar.html 
    """


def floatSlider(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontal: boolean, flagisObscured: boolean, flagmanage: boolean, flagmaxValue: float, flagminValue: float, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flagstep: float, flaguseTemplate: string, flagvalue: float, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 floatSlider(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean], [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [step=float], [useTemplate=string], [value=float], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

floatSlider is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( adjustableColumn=True )
cmds.floatSlider()
cmds.floatSlider( min=-100, max=100, value=0, step=1 )
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
    Command executed when the value changes.  This command is
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
    Command executed when the value changes by dragging the
slider's value marker.

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
    properties: create, query
    Orientation of the slider.  This flag is true by default,
which corresponds to a horizontally oriented slider.

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
maxValue(max): float
    properties: create, query, edit
    Upper limit of the slider.

---
minValue(min): float
    properties: create, query, edit
    Lower limit of the slider.

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
step(s): float
    properties: create, query, edit
    The step value represents the amount the
value will increase or decrease when you click either side of the
slider.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): float
    properties: create, query, edit
    Value of the slider.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/floatSlider.html 
    """


def floatSlider2(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand1: string, flagchangeCommand2: string, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmaximum: float, flagminimum: float, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpolarity: int, flagpopupMenuArray: boolean, flagpositionControl1: string, flagpositionControl2: string, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvalue1: float, flagvalue2: float, flagvalues: tuple[float, float], flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 floatSlider2(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand1=string], [changeCommand2=string], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [maximum=float], [minimum=float], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [polarity=int], [popupMenuArray=boolean], [positionControl1=string], [positionControl2=string], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [value1=float], [value2=float], [values=[float, float]], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

floatSlider2 is undoable, queryable, and editable.
Note: the floatSlider2 widget currently only supports vertical
(columnLayout) orientation.




Example:
---
import maya.cmds as cmds

---
---
---
---
---
---
---
---
---
---
---
floatSlider2 example ---
---
---
---
---
---
---
---
---
---
---
---
---

---

First, create one object to control with the slider. We will use one
slider handle to control the startSweep and the other the endSweep so
that the sphere can be made to open and close via the handles.
---

cmds.sphere()

Create a window containing a floatSlider2 (two handled float slider).
The window also contains two floating-point textfields.
   - Moving the handle updates the associated textfield.
   - Typing a value into a textfield moves the associated handle.
---

cmds.window()
cmds.columnLayout()

ff1    = cmds.floatField()
slider = cmds.floatSlider2()
ff2    = cmds.floatField()

Hook the slider handles up to drive the textfields. When you move the
slider handles, the textfields will update to display the
position of the handle.
---

cmds.floatSlider2( slider, edit=True, positionControl1=ff1, positionControl2=ff2 )

Set the slider direction (polarity) and upper limit.
---

cmds.floatSlider2( slider, edit=True, polarity=1, max=360 )

Connect the slider so that the handles drive the sweep angles of
the NURBS sphere.
---

cmds.floatSlider2(slider, edit=True, cc1='setAttr makeNurbSphere1.endSweep', cc2='setAttr makeNurbSphere1.startSweep' )

Display the window.
---

cmds.showWindow()

---
Return:
---


    string: The name of the port created or modified

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
changeCommand1(cc1): string
    properties: create, edit
    Command to be associated with handle 1 and issued
whenever the value of the handle is changed (except when values
are changed via the -hv/handleValue flag). An example command might be
"setAttr nurbsSphere1.tx" and if handle 1 were to move to
value 0.23 the slider would issue the command
"setAttr nurbsSphere1.tx 0.23;".

---
changeCommand2(cc2): string
    properties: create, edit
    Command to be associated with handle 2 and issued
whenever the value of the handle is changed (except when values
are changed via the -hv/handleValue flag). An example command might be
"setAttr nurbsSphere1.tx" and if handle 2 were to move to
value 0.23 the slider would issue the command
"setAttr nurbsSphere1.tx 0.23;".

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
maximum(max): float
    properties: create, query, edit
    Maximum limit of the slider. The default value is 10.0.
The maximum value occurs at the top(right) end of the slider
unless -polarity was specified. Note: you cannot set the
maximum value greater than or equal to the current minimum.

---
minimum(min): float
    properties: create, query, edit
    Minimum limit of the slider. The default value is 0.0.
The minimum value occurs at the bottom end of the slider
unless -polarity was specified. Note: you cannot set the
minimum value greater than or equal to the current maximum.

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
polarity(pol): int
    properties: create, query, edit
    Specifies the polarity of the slider. If 0 (the default), the minimum
value (specified by the -minimum flag) occurs at the bottom end of
the slider and maximum at the top(right), with values increasing as the slider
handles are moved towards the upper end of the slider. If the polarity
is specified as 1, the reverse behaviour occurs, with the maximum
occurring at the bottom end, the mimimum occuring at the top(right) end
and values decreasing as the handles are moved towards the upper end.

---
popupMenuArray(pma): boolean
    properties: query
    Return the names of all the popup menus attached to this
control.

---
positionControl1(pc1): string
    properties: create, edit
    Set the name of the control (if any) which is associated with
handle 1 of this slider. The control must be a "floatField". The
control always displays the value of the handle, and is updated as
the handle moves.

---
positionControl2(pc2): string
    properties: create, edit
    Set the name of the control (if any) which is associated with
handle 2 of this slider. The control must be a "floatField". The
control always displays the value of the handle, and is updated as
the handle moves.

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
value1(v1): float
    properties: create, query, edit
    Value of handle 1. To ensure that handle 1 stays at
or below handle 2, an error will occur if the value specified
is too large. If you wish to set both handles simultaneously,
use the -values flag.

---
value2(v2): float
    properties: create, query, edit
    Value of handle 2. To ensure that handle 2 stays at
or above handle 2, an error will occur if the value specified
is too large. If you wish to set both handles simultaneously,
use the -values flag.

---
values(vs): [float, float]
    properties: create, edit
    Sets the value for handles 1 and 2 simulteneously. The
first argument is applied to handle 1 and must be less than
or equal to the second (handle 2) argument or an error will
be issued.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/floatSlider2.html 
    """


def floatSliderButtonGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagbuttonCommand: script, flagbuttonLabel: string, flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagextraLabel: string, flagfield: boolean, flagfieldMaxValue: float, flagfieldMinValue: float, flagfieldStep: float, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagimage: string, flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagmaxValue: float, flagminValue: float, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagsliderStep: float, flagstatusBarMessage: string, flagstep: float, flagsymbolButtonCommand: script, flagsymbolButtonDisplay: boolean, flaguseTemplate: string, flagvalue: float, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 floatSliderButtonGrp(
[name]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [buttonCommand=script], [buttonLabel=string], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [field=boolean], [fieldMaxValue=float], [fieldMinValue=float], [fieldStep=float], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image=string], [isObscured=boolean], [label=string], [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]], [sliderStep=float], [statusBarMessage=string], [step=float], [symbolButtonCommand=script], [symbolButtonDisplay=boolean], [useTemplate=string], [value=float], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

floatSliderButtonGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a float slider component with optional button
and symbol buttons.

TelfFloatSliderGrpCmd.cpp




Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
cmds.floatSliderButtonGrp( label='Label', field=True, buttonLabel='Button', symbolButtonDisplay=True, columnWidth=(5, 23), image='cmdWndIcon.xpm' )
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
    Command string to be executed when the button is pressed.

---
buttonLabel(bl): string
    properties: create, query, edit
    The button text.

---
changeCommand(cc): script
    properties: create, edit
    Command string executed when the value of the
slider changes.  It will be executed only once after a drag
of the slider.

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
    Command string executed repeatedly during a drag
of the slider.

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
extraLabel(el): string
    properties: create, query, edit
    If present on creation this specifies that there will be
an extra label appearing after the slider.  Sets the string to be
the text for the extra label.

---
field(f): boolean
    properties: create
    Indicates whether the group will have an editable float field
present that reflects the value of the slider.

---
fieldMaxValue(fmx): float
    properties: create, query, edit
    Maximum value that may be entered in the field.  This
value may be set to any value greater than
the -max/maxValue flag.  By default, it is equal to
the -max/maxValue flag.

---
fieldMinValue(fmn): float
    properties: create, query, edit
    Minimum value that may be entered in the field.  This
value may be set to any value less than
the -min/minValue flag.  By default, it is equal to
the -min/minValue flag.

---
fieldStep(fs): float
    properties: create, query, edit
    Increment for the field.

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
    Image displayed on the symbol button.

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
    If present on creation the group will have static text.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxValue(max): float
    properties: create, query, edit
    Maximum value for both the slider and the field.

---
minValue(min): float
    properties: create, query, edit
    Minimum value for both the slider and the field.

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
    properties: create, edit
    Number of digits to the right of the decimal.

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
sliderStep(ss): float
    properties: create, query, edit
    The slider step value represents the
amount the value will increase or decrease when you click either
side of the slider.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): float
    properties: create, query, edit
    Increment for both the slider and field.

---
symbolButtonCommand(sbc): script
    properties: create, edit
    Command string executed when the symbol button is pressed.

---
symbolButtonDisplay(sbd): boolean
    properties: create, query, edit
    Visibility of the symbol button.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): float
    properties: create, query, edit
    Value of the group.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/floatSliderButtonGrp.html 
    """


def floatSliderGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagextraLabel: string, flagfield: boolean, flagfieldMaxValue: float, flagfieldMinValue: float, flagfieldStep: float, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagmaxValue: float, flagminValue: float, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagsliderStep: float, flagstatusBarMessage: string, flagstep: float, flaguseTemplate: string, flagvalue: float, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 floatSliderGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [field=boolean], [fieldMaxValue=float], [fieldMinValue=float], [fieldStep=float], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]], [sliderStep=float], [statusBarMessage=string], [step=float], [useTemplate=string], [value=float], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

floatSliderGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of controls containing a
label text, an float field and a float slider. The text and field
controls are optional.  Editing or querying the field range values has
no effect if the -f/field flag was not specified when the group was
created.

This group also allows you to enter values into the field outside of the
slider range which is limited by the -min/minValue
and -max/maxValue flags.  To do this, use
the -fmn/fieldMinValue and -fmx/fieldMaxValue flags to
specify a greater range of values.

Note that the command will not allow you to specify
a -fmn/fieldMinValue greater than the -min/minValue value nor
a -fmx/fieldMaxValue less than the -max/maxValue value.

If you do supply a larger field range with the -fmn/fieldMinValue
and -fmx/fieldMaxValue flags then you will notice that entering a
value in the field that is outside of the slider range will result in
extending the slider range as well.  For example, if you create a slider
group with the following command:

floatSliderGrp -min -10 -max 10 -fieldMinValue -100 -fieldMaxValue 100;

Then you will be able to use the slider to select any value from -10 to 10.
At the same time you will be able to enter into the field any value
from -100 to 100.  If you enter a value, say 20, then the new slider
range will grow such that this value is now accessible through the slider
as well.  In fact, the new slider limit will become double of that what you
entered.  Note that the slider limits will never grow beyond the field
limits, in other words if you entered the value 80 then the slider will be
clipped to the field limit of 100 and not doubled to 160.




Example:
---
import maya.cmds as cmds

   Create a window with a couple float slider groups.  The first will
   use default limit values, and the second will set up a group that has
   a field range greater than the slider range.  Try entering values
   greater than the slider limits in both groups.
---

window = cmds.window(title='floatSliderGrp Example')
cmds.columnLayout()
cmds.floatSliderGrp( label='Group 1', field=True )
cmds.floatSliderGrp( label='Group 2', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )
cmds.showWindow( window )

---
Return:
---


    string: Full path name of the control.

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
    Command string executed when the value of the
slider changes.  It will be executed only once after a drag
of the slider.

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
    Command string executed repeatedly during a drag
of the slider.

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
extraLabel(el): string
    properties: create, query, edit
    If present on creation this specifies that there will be
an extra label appearing after the slider.  Sets the string to be
the text for the extra label.

---
field(f): boolean
    properties: create
    Indicates whether the group will have an editable float field
present that reflects the value of the slider.

---
fieldMaxValue(fmx): float
    properties: create, query, edit
    Maximum value that may be entered in the field.  This
value may be set to any value greater than
the -max/maxValue flag.  By default, it is equal to
the -max/maxValue flag.

---
fieldMinValue(fmn): float
    properties: create, query, edit
    Minimum value that may be entered in the field.  This
value may be set to any value less than
the -min/minValue flag.  By default, it is equal to
the -min/minValue flag.

---
fieldStep(fs): float
    properties: create, query, edit
    Increment for the field.

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
    If present on creation the group will have static text.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxValue(max): float
    properties: create, query, edit
    Maximum value for both the slider and the field.

---
minValue(min): float
    properties: create, query, edit
    Minimum value for both the slider and the field.

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
    properties: create, edit
    Number of digits to the right of the decimal.

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
sliderStep(ss): float
    properties: create, query, edit
    The slider step value represents the
amount the value will increase or decrease when you click either
side of the slider.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): float
    properties: create, query, edit
    Increment for both the slider and field.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): float
    properties: create, query, edit
    Value of the group.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/floatSliderGrp.html 
    """


def flow(flagdivisions: tuple[uint, uint, uint], flaglocalCompute: boolean, flaglocalDivisions: tuple[uint, uint, uint], flagobjectCentered: boolean) -> list[string]:
    """Synopsis:
---
---
 flow(
objects
    , [divisions=[uint, uint, uint]], [localCompute=boolean], [localDivisions=[uint, uint, uint]], [objectCentered=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

flow is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a simple motion path animation

create a path, e,g, a curve
path = cmds.curve(d=3,p=[(-10, 0, 0),(-6, 0, 10),(-3, 0, -10),(10, 0, 0)],k=[0, 0, 0, 1, 1, 1])

create an object, e.g. a sphere
object = cmds.sphere()
cmds.scale( 0.5, 2.0, 0.2 )

animate the object using a motion path with follow on for 30 frames
cmds.pathAnimation( object[0], f=1, stu=0, etu=30, c=path )

select only the animated object
cmds.select( object[0], r=True )

Create flow deformation on the selected object with default values:
cmds.flow()

Create flow deformation on the selected object with
the lattice around the path, and lattice division of 3,20,2:
cmds.flow( oc=False, dv=(3, 20, 2) )

Create flow deformation on the selected object with
lattice subdivisions 4, 7, and 3:

cmds.flow( dv=(4, 7, 3) )

When the object is not currently selected, the name of the object
has to be specified in the command line (note: $object[0] has to
have a motion path animation):

cmds.flow( object[0], dv=(4, 7, 3) )

---
Return:
---


    list[string]: The names of the created flow node and associated
lattice nodes.

Flags:
---


---
divisions(dv): [uint, uint, uint]
    properties: query
    This flag specifies the number of lattice slices
in x,y,z.
The default values are 2 5 2.
When queried, it returns the uint32_t uint32_t uint32_t

---
localCompute(lc): boolean
    properties: query
    This flag specifies whether or not to have local
control over the object deformation.
Default value:
is on when the lattice is around the curve, and
is off when the lattice is around the object. 
When queried, it returns a boolean

---
localDivisions(ld): [uint, uint, uint]
    properties: query
    This flag specifies the extent of the region of effect.
Default values are 2 2 2.
When queried, it returns the uint32_t uint32_t uint32_t

---
objectCentered(oc): boolean
    properties: query
    This flag specifies whether to create the lattice around
the selected object at its center, or to create the lattice
around the curve.
Default value is true.
When queried, it returns a boolean

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/flow.html 
    """


def flowLayout(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchildArray: boolean, flagcolumnSpacing: int, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghorizontal: boolean, flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvertical: boolean, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int, flagwrap: boolean) -> string:
    """Synopsis:
---
---
 flowLayout(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [childArray=boolean], [columnSpacing=int], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [vertical=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int], [wrap=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

flowLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.flowLayout( columnSpacing=10 )
cmds.button()
cmds.button()
cmds.button()
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
childArray(ca): boolean
    properties: query
    Returns a string array of the names of the layout's
immediate children.

---
columnSpacing(cs): int
    properties: create, query, edit
    Sets the space between children.

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
    Orientation of the layout. This flag is true by default, which corresponds to a horizontally laid out control.

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
vertical(v): boolean
    properties: create, query
    This flag is obsolete. Please use the -hr/-horizontal flag instead.

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
wrap(wr): boolean
    properties: create, query, edit
    When set to true, if the layout's parent cannot fit all the children in a single
line, the children will wrap onto the next line(s). Default setting is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/flowLayout.html 
    """


def fluidCacheInfo(flagattribute: string, flagcacheTime: time, flagendFrame: boolean, flaghasCache: boolean, flaghasData: boolean, flaginitialConditions: boolean, flagplayback: boolean, flagresolution: boolean, flagstartFrame: boolean) -> None:
    """Synopsis:
---
---
 fluidCacheInfo([attribute=string], [cacheTime=time], [endFrame=boolean], [hasCache=boolean], [hasData=boolean], [initialConditions=boolean], [playback=boolean], [resolution=boolean], [startFrame=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fluidCacheInfo is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

get start frame for Initial Conditions Cache
cmds.fluidCacheInfo( ic=True, sf=True )

get resolution for Initial Conditions Cache
cmds.fluidCacheInfo( ic=True, re=True )

get end frame for Playback Cache
cmds.fluidCacheInfo( pb=True, ef=True )

get resolution for Playback Cache
cmds.fluidCacheInfo( pb=True, re=True )

Is there data for any of the valid properties
in the playback cache?
cmds.fluidCacheInfo( pb=True, hd=True )

Is there density data in the playback cache?
cmds.fluidCacheInfo( at='density', pb=True, hd=True )

---


Flags:
---


---
attribute(at): string
    properties: create, query, edit
    Modifier to the "hasData" flag, used to query whether a
cache has data (at the current time)
for a specific fluid attribute.  Valid attribute
values are "density", "velocity", "temperature", "fuel", "color",
"coordinates" (for texture coordinates), "falloff".

---
cacheTime(t): time
    properties: create, query, edit
    Only valid with the -hasData flag.  The time the -hasData flag
uses when it queries the cache to see if there is data.

---
endFrame(ef): boolean
    properties: create, query, edit
    Returns end time of cache as float.

---
hasCache(hc): boolean
    properties: create, query, edit
    Returns true if fluid has specified cache, false if not.

---
hasData(hd): boolean
    properties: create, query, edit
    Queries whether a given cache has data in it at the time specified
by the -time flag.  (If not -time flag is present, -hasData assumes
the current time.)
When used with
the "attribute" flag, indicates if data for the specified attribute
exists in the cache.  When used without the "attribute" flag, "hasData"
indicates whether there is data in the cache for any of the valid
fluid attributes.

---
initialConditions(ic): boolean
    properties: create, query, edit
    Specifies the cache to be queried is the "Initial Conditions" cache.

---
playback(pb): boolean
    properties: create, query, edit
    Specifies the cache to be queried is the "Playback" cache.

---
resolution(re): boolean
    properties: create, query, edit
    Returns cache resolution as float[].

---
startFrame(sf): boolean
    properties: create, query, edit
    Returns start time for cache as float.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fluidCacheInfo.html 
    """


def fluidEmitter(flagcycleEmission: string, flagcycleInterval: int, flagdensityEmissionRate: float, flagfluidDropoff: float, flagfuelEmissionRate: float, flagheatEmissionRate: float, flagmaxDistance: linear, flagminDistance: linear, flagname: string, flagposition: tuple[linear, linear, linear], flagrate: float, flagtorusSectionRadius: linear, flagtype: string, flagvolumeOffset: tuple[linear, linear, linear], flagvolumeShape: string, flagvolumeSweep: angle) -> string:
    """Synopsis:
---
---
 fluidEmitter(
selectionList
    , [cycleEmission=string], [cycleInterval=int], [densityEmissionRate=float], [fluidDropoff=float], [fuelEmissionRate=float], [heatEmissionRate=float], [maxDistance=linear], [minDistance=linear], [name=string], [position=[linear, linear, linear]], [rate=float], [torusSectionRadius=linear], [type=string], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fluidEmitter is undoable, queryable, and editable.
If an emitter was created, the command returns the name of the object
owning the emitter, and the name of emitter shape. If an emitter was
queried, the command returns the results of the query.




Example:
---
import maya.cmds as cmds

cmds.fluidEmitter( pos=(0, 0, 0), type='omni', der=1, her=2, fer=3, fdr=1.5, r=100.0, cye='none', cyi=1, mxd=0, mnd=0 )
cmds.connectDynamic( 'fluidShape1', em='emitter1' )

Creates an omni emitter that's emitting density, heat and fuel
into fluidShape1

---
Return:
---


    string: Command result

Flags:
---


---
cycleEmission(cye): string
    properties: query, edit
    Possible values are "none" and "frame."
Cycling emission restarts the random number stream after
a specified interval.  This can either be a number of frames
or a number of emitted particles.  In each case the number
is specified by the cycleInterval attribute. Setting cycleEmission to
"frame" and cycleInterval to 1 will then re-start the random stream every
frame. Setting cycleInterval to values greater than 1 can be used
to generate cycles for games work.

---
cycleInterval(cyi): int
    properties: query, edit
    Specifies the number of frames or particles between restarts of
the random number stream.  See cycleEmission.  Has no effect if
cycleEmission is set to None.

---
densityEmissionRate(der): float
    properties: query, edit
    Rate at which density is emitted.

---
fluidDropoff(fdr): float
    properties: query, edit
    Fluid Emission Dropoff in volume

---
fuelEmissionRate(fer): float
    properties: query, edit
    Rate at which  is emitted.

---
heatEmissionRate(her): float
    properties: query, edit
    Rate at which density is emitted.

---
maxDistance(mxd): linear
    properties: query, edit
    Maximum distance at which emission ends.

---
minDistance(mnd): linear
    properties: query, edit
    Minimum distance at which emission starts.

---
name(n): string
    properties: create, query, edit
    Object name

---
position(pos): [linear, linear, linear]
    properties: create, query, edit, multiuse
    world-space position

---
rate(r): float
    properties: query, edit
    Rate at which particles emitted (can be non-integer).
For point emission this is rate per point per unit time.
For surface emission it is rate per square unit of area per unit time.

---
torusSectionRadius(tsr): linear
    properties: query, edit
    Section radius for a torus volume.  Applies only to torus.
Similar to the section radius in the torus modelling primitive.

---
type(typ): string
    properties: query, edit
    Type of emitter. The choices are omni | dir | direction | surf |
surface | curve | curv. The default is omni.
The full definition of these types are: omnidirectional point emitter,
directional point emitter, surface emitter, or curve emitter.

---
volumeOffset(vof): [linear, linear, linear]
    properties: query, edit
    Volume offset of the emitter.  Volume offset translates
the emission volume by the specified amount from the actual
emitter location.  This is in the emitter's local space.

---
volumeShape(vsh): string
    properties: query, edit
    Volume shape of the emitter.  Sets/edits/queries the
field's volume shape attribute.  If set to any value other
than "none", determines a 3-D volume within which
particles are generated.
Values are: "cube," "sphere," "cylinder," "cone," "torus."

---
volumeSweep(vsw): angle
    properties: query, edit
    Volume sweep of the emitter.  Applies only to sphere, cone,
cylinder, and torus.  Similar effect to the sweep attribute
in modelling.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fluidEmitter.html 
    """


def fluidVoxelInfo(flagcheckBounds: boolean, flaginBounds: tuple[int, int, int], flagobjectSpace: boolean, flagradius: float, flagvoxel: tuple[float, float, float], flagvoxelCenter: boolean, flagxIndex: int, flagyIndex: int, flagzIndex: int) -> None:
    """Synopsis:
---
---
 fluidVoxelInfo([checkBounds=boolean], [inBounds=[int, int, int]], [objectSpace=boolean], [radius=float], [voxel=[float, float, float]], [voxelCenter=boolean], [xIndex=int], [yIndex=int], [zIndex=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fluidVoxelInfo is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

fluid3D is a 10x10x5 three-dimensional fluid.
fluid2D is a 9x9 two-dimensional fluid.
---

Are the given indices within the bounds of the fluids?
---

cmds.fluidVoxelInfo( 'fluid2D', inBounds=( 9, 9, 0) )
Result: false
cmds.fluidVoxelInfo( 'fluid2D', inBounds=( 8, 8, 0) )
Result: true
cmds.fluidVoxelInfo( 'fluid3D', inBounds=( 2, 3, 4 ) )
Result: true
cmds.fluidVoxelInfo( 'fluid3D', inBounds=( 12, 9, 2) )
Result: false

---


Flags:
---


---
checkBounds(cb): boolean
    properties: create
    If this flag is on, and the voxel index of a point that is out of bounds is requested,
then we return nothing.

---
inBounds(ib): [int, int, int]
    properties: create
    Are the three ints representing the x, y, z indices of a voxel within the bounds of the fluid's voxel grid?  True if yes, false if not.  (For 2D fluids, pass in z=0 for the third argument.  See examples.)

---
objectSpace(os): boolean
    properties: create
    Whether the queried value should be returned in object space (TRUE),
or world space (FALSE, the default).

---
radius(r): float
    properties: create
    Modifier for the -voxel flag.  Returns a list of
index triples identifying voxels that fall within
the given radius of the point specified by the
-voxel flag.

---
voxel(v): [float, float, float]
    properties: create
    Returns array of three ints representing the x, y, z indices of the voxel within which the given point position is contained.
If the checkBounds flag is on, and the point is out of bounds, we return nothing. Otherwise, even if the point is out of bounds, index values are returned.
When combined with the -radius flag, returns an array of index triples
representing a list of voxels within a given radius of the given point position.

---
voxelCenter(vc): boolean
    properties: create
    The center position of the specified voxels.  Returns an array of floats (three for each of the indices in the query).  (Valid only with the -xIndex, -yIndex, and -zIndex flags.)

---
xIndex(xi): int
    properties: create
    Only return values for cells with this X index

---
yIndex(yi): int
    properties: create
    Only return values for cells with this Y index

---
zIndex(zi): int
    properties: create
    Only return values for cells with this Z index

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fluidVoxelInfo.html 
    """


def flushUndo() -> None:
    """Synopsis:
---
---
 flushUndo()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

flushUndo is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.flushUndo()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/flushUndo.html 
    """


def fontDialog(flagFontList: boolean, flagscalable: boolean) -> string:
    """Synopsis:
---
---
 fontDialog([FontList=boolean], [scalable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

fontDialog is undoable, NOT queryable, and NOT editable.
When the FontList flag is used, no dialog is displayed. Instead
the command returns an array of the available fonts.




Example:
---
import maya.cmds as cmds

Display a selection dialog containing all available fonts and save
the one selected by the user.
font = cmds.fontDialog()

Get an array of all available fonts.
fonts = cmds.fontDialog(FontList=True)

Get an array of scalable fonts.
scalableFonts = cmds.fontDialog(FontList=True, scalable=True)

---
Return:
---


    string: Dialog name

Flags:
---


---
FontList(fl): boolean
    properties: create
    Returns an array of all available font names. No dialog is displayed.

---
scalable(sc): boolean
    properties: create
    Limits the fonts returned or displayed to just those that are scalable.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/fontDialog.html 
    """


def formLayout(flagannotation: string, flagattachControl: tuple[string, string, int, string], flagattachForm: tuple[string, string, int], flagattachNone: tuple[string, string], flagattachOppositeControl: tuple[string, string, int, string], flagattachOppositeForm: tuple[string, string, int], flagattachPosition: tuple[string, string, int, int], flagbackgroundColor: tuple[float, float, float], flagchildArray: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfDivisions: int, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 formLayout(
[string]
    , [annotation=string], [attachControl=[string, string, int, string]], [attachForm=[string, string, int]], [attachNone=[string, string]], [attachOppositeControl=[string, string, int, string]], [attachOppositeForm=[string, string, int]], [attachPosition=[string, string, int, int]], [backgroundColor=[float, float, float]], [childArray=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfDivisions=int], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

formLayout is undoable, queryable, and editable.
Controls have four edges: top, left, bottom and right.
There are only two directions that children can be positioned in,
right-left and up-down. The attach flags take the direction of
an attachment from the argument that names the edge to attach
(the second argument). Any or all edges of a child may be
attached. There are six ways to attach them:


Attach to Form - Attaches an edge to the relevant side
of the form layout. Thus -attachForm button3 "left" will
attach the left edge of the button to the left edge of the form.

Attach to Opposite Side of Form - Attaches an edge relative to
the furthest side of the form layout.

Attach to Another Control - Attaches an edge to the closest
edge of the other control named.

Attach to Opposite Side of Another Control - Attaches an edge
relative to the furthest side of another control.

Attach to Position - Attaches an edge to a position
on the form layout.  The position is given as a fixed fraction
of the -nd/numDivisions value and as this value defaults to 100
it is easiest to think of it as a percentage of the form's
size.

Attach to Nothing - Attaches an edge to nothing.
The size of the child control will determine this edge's
position.


Each edge attachment may have an offset that acts to separate
controls visually.

There is no default positioning relationship so to have children
appear in the form they must have at least one edge attached in
each direction.

Note: In the flag definitions the arguments follow these
rules:

 control must
be the name of an immediate child of the form layout.

 edge must be one of "top", "left", "bottom", or
"right".

 position may range from 0 to the number of
divisions as specified with the -nd/numberOfDivisions flag
and gives the fraction of the width of the form as a measurement.
This normally means 0-100 so  position may be thought
of as a percentage.

 offset is an integer value in pixels.


These are multi-use flags so any number of attachments
may be made in a single command.

Note: Avoid making control attachments that form a loop in
control dependencies. For example:


window;
string $form = `formLayout`;
string $btn1 = `button`;
string $btn2 = `button`;
string $btn3 = `button`;
formLayout -edit    -attachControl $btn2 "top"   2 $btn1    -attachControl $btn3 "top"   2 $btn2    -attachControl $btn1 "right" 2 $btn3
$form;
showWindow;


$btn2 is attached to $btn1, $btn3 is attached to $btn2, and $btn1 is
attached to $btn3. Thus, the placement of $btn1 is dependent on the
placement of $btn3, which is dependent on the placement of $btn2, which
is dependent on the placement of $btn1. The last control attachment will
have created a loop in the dependencies.

To prevent runtime errors, Maya will ignore this attachment and instead
issue a warning that a cyclical control attachment has been detected in
the script.





Example:
---
import maya.cmds as cmds

window = cmds.window()
form = cmds.formLayout(numberOfDivisions=100)
b1 = cmds.button()
b2 = cmds.button()
column = cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()

cmds.formLayout( form, edit=True, attachForm=[(b1, 'top', 5), (b1, 'left', 5), (b2, 'left', 5), (b2, 'bottom', 5), (b2, 'right', 5), (column, 'top', 5), (column, 'right', 5) ], attachControl=[(b1, 'bottom', 5, b2), (column, 'bottom', 5, b2)], attachPosition=[(b1, 'right', 5, 75), (column, 'left', 0, 75)], attachNone=(b2, 'top') )

cmds.showWindow( window )

---
Return:
---


    string: The full name of the control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
attachControl(ac): [string, string, int, string]
    properties: create, edit, multiuse
    Arguments are: control, edge, offset, control
Valid edge values are: "top" | "bottom" | "left" | "right".
Attach a control to another control.

---
attachForm(af): [string, string, int]
    properties: create, edit, multiuse
    Arguments are: control, edge, offset.
Valid edge values are: "top" | "bottom" | "left" | "right".
Attach the specified control to the form, offset by the specified
amount.

---
attachNone(an): [string, string]
    properties: create, edit, multiuse
    Arguments are: control, edge
Valid edge values are: "top" | "bottom" | "left" | "right".
Attach a control to nothing.

---
attachOppositeControl(aoc): [string, string, int, string]
    properties: create, edit, multiuse
    Arguments are: control, edge, offset, control
Valid edge values are: "top" | "bottom" | "left" | "right".
Attach a control to the opposite side of another control.

---
attachOppositeForm(aof): [string, string, int]
    properties: create, edit, multiuse
    Arguments are: control, edge, offset.
Valid edge values are: "top" | "bottom" | "left" | "right".
Attach a control to the opposite side of the form.

---
attachPosition(ap): [string, string, int, int]
    properties: create, edit, multiuse
    Arguments are: control, edge, offset, position
Valid edge values are: "top" | "bottom" | "left" | "right".
Attach a control to a position in the form.

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
numberOfDivisions(nd): int
    properties: create, query, edit
    Specify the number of horizontal and vertical divisions
across the form. Value must be greater than 0.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/formLayout.html 
    """


def format(flagstringArg: string) -> string:
    """Synopsis:
---
---
 format([stringArg=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

format is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

The mel script below returns the sentence
    "Display all lambert and blinn nodes."
---

cmds.format( 'Display all ^1s and ^2s nodes.', stringArg=('lambert', 'blinn') )

---
Return:
---


    string: Command result

Flags:
---


---
stringArg(s): string
    properties: create, multiuse
    Specify the arguments for the format string.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/format.html 
    """


def frameBufferName(flagautoTruncate: boolean, flagcamera: string, flagrenderLayer: string, flagrenderPass: string) -> string:
    """Synopsis:
---
---
 frameBufferName([autoTruncate=boolean], [camera=string], [renderLayer=string], [renderPass=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

frameBufferName is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.frameBufferName(renderLayer='layer1', renderPass='renderPass1', camera='camera1')

---
Return:
---


    string: Command result

Flags:
---


---
autoTruncate(a): boolean
    properties: create
    use this flag to apply a name truncation algorithm so that the frameBuffer
name will respect the maximum length imposed by the destination file format,
if applicable.

---
camera(c): string
    properties: create
    Specify a camera

---
renderLayer(l): string
    properties: create
    Specify a renderer layer

---
renderPass(p): string
    properties: create
    Specify a renderer pass

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/frameBufferName.html 
    """


def frameLayout(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagbackgroundShade: boolean, flagborderStyle: string, flagborderVisible: boolean, flagchildArray: boolean, flagcollapsable: boolean, flagcollapse: boolean, flagcollapseCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagexpandCommand: script, flagfont: string, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flaglabelAlign: string, flaglabelIndent: int, flaglabelVisible: boolean, flaglabelWidth: int, flagmanage: boolean, flagmarginHeight: int, flagmarginWidth: int, flagmargins: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreCollapseCommand: script, flagpreExpandCommand: script, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 frameLayout(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [backgroundShade=boolean], [borderStyle=string], [borderVisible=boolean], [childArray=boolean], [collapsable=boolean], [collapse=boolean], [collapseCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [expandCommand=script], [font=string], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [labelAlign=string], [labelIndent=int], [labelVisible=boolean], [labelWidth=int], [manage=boolean], [marginHeight=int], [marginWidth=int], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preCollapseCommand=script], [preExpandCommand=script], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

frameLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.scrollLayout( 'scrollLayout' )
cmds.columnLayout( adjustableColumn=True )
cmds.frameLayout( label='Buttons' )
cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.frameLayout( label='Scroll Bars' )
cmds.columnLayout()
cmds.intSlider()
cmds.intSlider()
cmds.intSlider()
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.frameLayout( label='Fields' )
cmds.columnLayout()
cmds.intField()
cmds.intField()
cmds.intField()
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.frameLayout( label='Check Boxes' )
cmds.columnLayout()
cmds.checkBox()
cmds.checkBox()
cmds.checkBox()
cmds.setParent( '..' )
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
backgroundShade(bgs): boolean
    properties: create, query, edit
    Controls whether the background of the frame layout draws with a shaded effect. It is turned off by default.

---
borderStyle(bs): string
    properties: create, query, edit
    This flag is obsolete. The border style is no longer supported.
Using this flag will return a warning.

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
collapsable(cll): boolean
    properties: create, query, edit
    Collapsibility of the frame layout.

---
collapse(cl): boolean
    properties: create, query, edit
    Collapse state of the frame layout.

---
collapseCommand(cc): script
    properties: create, edit
    Command executed after the frame is collapsed.

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
expandCommand(ec): script
    properties: create, edit
    Command executed after the frame is expanded.

---
font(fn): string
    properties: create, query, edit
    The font for the frame label.  Valid values are
"boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",
"plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",
"smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".

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
    Label string for the frame layout.

---
labelAlign(la): string
    properties: create, query, edit
    How to align the label. Default is "top".

---
labelIndent(li): int
    properties: create, query, edit
    Indentation for the frame label.

---
labelVisible(lv): boolean
    properties: create, query, edit
    Visibility of the frame label.

---
labelWidth(lw): int
    properties: create, query, edit
    Width of the label.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
marginHeight(mh): int
    properties: create, query, edit
    Vertical distance between the frame and its children.

---
marginWidth(mw): int
    properties: create, query, edit
    Horizontal distance between the frame and its children.

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
preCollapseCommand(pcc): script
    properties: create, edit
    Command executed just before the frame is collapsed.

---
preExpandCommand(pec): script
    properties: create, edit
    Command executed just before the frame is expanded.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/frameLayout.html 
    """


def framelessDialog(flagbutton: string, flagmessage: string, flagparent: string, flagpath: string, flagprimary: string, flagtitle: string) -> string:
    """Synopsis:
---
---
 framelessDialog([button=string], [message=string], [parent=string], [path=string], [primary=string], [title=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

framelessDialog is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.framelessDialog( title='Confirm', message='File not found',
        path='c:/path/of/file/not/found.txt', button=['OK'], primary=['OK'])

---
Return:
---


    string: Indicates how the dialog was dismissed. If a button is
pressed then the label of the button is returned.

Flags:
---


---
button(b): string
    properties: create, multiuse
    Create a button with the given string as it's text.

---
message(m): string
    properties: create
    The message text appearing in the dialog.

---
parent(p): string
    properties: create
    Specify the parent window for the dialog.  The dialog will
be centered on this window and raise and lower with it's parent.
By default, the dialog is not parented to a particular window and
is simply centered on the screen.

---
path(pat): string
    properties: create
    An optional path appearing after the message.

---
primary(pr): string
    properties: create, multiuse
    Set given buttons as primary.

---
title(t): string
    properties: create
    The dialog title.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/framelessDialog.html 
    """


def freeFormFillet(flagbias: float, flagcaching: boolean, flagconstructionHistory: boolean, flagdepth: float, flagname: string, flagnodeState: int, flagobject: boolean, flagpolygon: int, flagpositionTolerance: float, flagrange: boolean, flagtangentTolerance: float) -> list[string]:
    """Synopsis:
---
---
 freeFormFillet(
[surfaceIsoparm] [surfaceIsoparm]
    , [bias=float], [caching=boolean], [constructionHistory=boolean], [depth=float], [name=string], [nodeState=int], [object=boolean], [polygon=int], [positionTolerance=float], [range=boolean], [tangentTolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

freeFormFillet is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create the fillet across a curve on surface and surface isoparm.
cmds.nurbsPlane( ch=True, o=True, po=0, ax=(0, 1, 0), w=11, lr=1 )
cmds.circle( ch=True, o=True, nr=(0, 1, 0), r=3.79518 )
cmds.projectCurve( 'nurbsCircle1', 'nurbsPlane1', ch=False, rn=False, un=False, tol=0.01 )
Result: [u'nurbsPlane1->projectionCurve1'] ---

cmds.nurbsPlane( p=(0, 6, 0), ax=(0, 1, 0), w=11, lr=1 )
Result: [u'nurbsPlane2', u'makeNurbPlane2'] ---

cmds.freeFormFillet( 'nurbsPlaneShape1->projectionCurve1_1', 'nurbsPlane2.v[1.0]', ch=True, bias=0.0, depth=0.5, po=True )
Result: [u'freeformFilletSurface1', u'ffFilletSrf1'] ---


cmds.trim( 'nurbsPlaneShape1', 'projectionCurve1_Shape1', ch=True, o=True, rpo=True, lu=0.2, lv=0.2 )
Result: [u'nurbsPlaneShape1', u'trim1'] ---

Fillet across a surface trim edge boundary and surface isoparm.
cmds.freeFormFillet( 'nurbsPlane1.edge[1][1][4]', 'nurbsPlane2.v[0][0.0:0.6]', ch=False )
Result: [u'freeformFilletSurface2'] ---


---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
bias(b): float
    properties: create, query, edit
    Bias value for fillet
Default: 0.5

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
depth(d): float
    properties: create, query, edit
    Depth value for fillet
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
positionTolerance(pt): float
    properties: create, query, edit
    C(0) Tolerance For Filleted Surface creation
Default: 0.1

---
tangentTolerance(tt): float
    properties: create, query, edit
    G(1) continuity Tolerance For Filleted Surface creation
Default: 0.1

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

---
range(rn): boolean
    properties: create
    Force a curve range on complete input curve.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/freeFormFillet.html 
    """


def freeze(flagallNodes: boolean, flagdisplayLayers: boolean, flagdownstream: boolean, flagforceDownstream: boolean, flagfrozen: boolean, flaginvisible: boolean, flagnoFreeze: boolean, flagunfreeze: boolean, flagupstream: boolean) -> list[string]:
    """Synopsis:
---
---
 freeze([allNodes=boolean], [displayLayers=boolean], [downstream=boolean], [forceDownstream=boolean], [frozen=boolean], [invisible=boolean], [noFreeze=boolean], [unfreeze=boolean], [upstream=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

freeze is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Set all selected nodes to be frozen
cmds.freeze()
Result: ['node1', 'node2', 'node3']

Set all nodes in the scene to be unfrozen
cmds.freeze( all=True, unfreeze=True )
Result: ['node1', 'node2', 'node3', 'nodeAlreadyFrozen']

---
Return:
---


    list[string]: In query mode the list of currently frozen or unfrozen nodes. The list is in three parts separated by an empty string; nodes with frozen state (un)set, nodes with frozenAffected state (un)set, and the rest of the selected nodes
    list[string]: the list of nodes whose frozen state was set by the command. The list is in two parts separated by an empty string; nodes with frozen state set, and nodes with frozenAffected state set

Flags:
---


---
allNodes(all): boolean
    properties: create, query
    Select which nodes are to be used for the operation.
If it is not set then the selection list will be used. If nothing is selected
all nodes in the scene will be used.
This flag can be used in query mode to find the set of frozen nodes in the scene.
It can also be used in create mode with filters (displayLayers, invisible,
or frozen) to target a specific subset of nodes in the scene.

---
displayLayers(dl): boolean
    properties: create, query
    If this flag is enabled then the display layers on the list to be processed
will be walked. Any nodes they control will be added to the processing list,
providing the display layer visibility control is off and not connected.
Note: Animated visibility or enabled states will be treated as matches to
be thorough. No attempt is made to check for static animation.

---
downstream(dn): boolean
    properties: create, query
    If this flag is enabled then the frozen state will attempt to propagate
downstream from the selected nodes. e.g. the mesh shape deformations being
controlled by a skeleton rig.

---
forceDownstream(fd): boolean
    properties: create, query
    If this flag is enabled then the frozen state will attempt to propagate
downstream from the selected nodes. e.g. the mesh shape deformations being
controlled by a skeleton rig. Unlike the downstream flag though this one
will freeze downstream nodes even if they have other, unfrozen, inputs.

---
frozen(f): boolean
    properties: create, query
    If this flag is enabled then the list of nodes to be processed will be
filtered out so that only nodes with the frozen attribute already set are
included. Otherwise all nodes being processed will first have their frozen
attribute set before propagating the frozen state.
This flag would only be used if nodes were previously frozen and the command
is used to propagate the frozen state through the graph.

---
invisible(i): boolean
    properties: create, query
    If this flag is enabled then the invisible nodes on the list to be processed
will be walked. Any nodes below them in the DAG hierarchy will be added to
the processing list, providing the visibility attribute is not connected.
Note: Animated visibility states will be treated as a match to
be thorough. No attempt is made to check for static animation.

---
noFreeze(n): boolean
    properties: create, query
    This flag previews the nodes that will be frozen without actually freezing them.

---
unfreeze(uf): boolean
    properties: create, query
    If this flag is enabled then the nodes being processed will have their frozen
state turned off instead of on. All of the same filtering and propagating will
be done when deciding which nodes to modify.
In query mode this flag switches from returning the already-frozen nodes to
returning the unfrozen nodes.

---
upstream(up): boolean
    properties: create, query
    If this flag is enabled then the frozen state will attempt to propagate
upstream through the selected nodes. e.g. the param curves feeding into
a frozen transform.
Heuristics are applied to this propagation to ensure that upstream nodes
that are still used by unfrozen nodes will stay unfrozen themselves.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/freeze.html 
    """


def freezeOptions(flagdisplayLayers: boolean, flagdownstream: string, flagexplicitPropagation: boolean, flaginvisible: boolean, flagreferencedNodes: boolean, flagruntimePropagation: boolean, flagupstream: string) -> boolean | string:
    """Synopsis:
---
---
 freezeOptions([displayLayers=boolean], [downstream=string], [explicitPropagation=boolean], [invisible=boolean], [referencedNodes=boolean], [runtimePropagation=boolean], [upstream=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

freezeOptions is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Print the current display layer freeze option
print 'Display layer freeze option is {}'.format( cmds.freezeOptions( query=True, displayLayers=True ) )

Toggle the display layer freeze option on
cmds.freezeOptions( displayLayers=True )
Return: True ---


Set downstream propagation to safe mode
cmds.freezeOptions( downstream='safe' )
Return: True ---


---
Return:
---


    string: Current value of the option if querying the downstream or upstream flags
    boolean: Current value of the option if querying the displayLayers, invisible, referencedNodes, explicitPropagation, or runtimePropagaton flags
    boolean: In creation mode returns true if all options were successfully set

Flags:
---


---
displayLayers(dl): boolean
    properties: create, query
    If this option is enabled then any nodes that are in an enabled, invisible display
layer will be considered to be frozen, and the frozen state will propagate accordingly.

---
downstream(dn): string
    properties: create, query
    Controls how frozen state is propagated downstream from currently frozen nodes.
Valid values are "none" for no propagation, "safe" for propagation downstream
only when all upstream nodes are frozen, and "force" for propagation downstream
when any upstream node is frozen.

---
explicitPropagation(ep): boolean
    properties: create, query
    When turned on this will perform an extra pass when the evaluation graph is
constructed to perform intelligent propagation of the frozen state to related
nodes as specified by the currently enabled options of the evaluation graph.
See also "runtimePropagation".
This option performs more thorough propagation of the frozen state, but requires
extra time for recalculating the evaluation graph.

---
invisible(inv): boolean
    properties: create, query
    If this option is enabled then any nodes that are invisible, either directly or
via an invisible parent node, will be considered to be frozen, and the frozen state
will propagate accordingly.

---
referencedNodes(rn): boolean
    properties: create, query
    If this option is enabled then any nodes that are referenced in from a frozen referenced node
will also be considered to be frozen, and the frozen state will propagate accordingly.

---
runtimePropagation(rt): boolean
    properties: create, query
    When turned on this will allow the frozen state to propagate during execution
of the evaluation graph. See also "explicitPropagation".
This option allows frozen nodes to be scheduled for evaluation, but once it
discovers a node that is frozen it will prune the evaluation based on the
current set of enabled options. It only works in the downstream direction.

---
upstream(up): string
    properties: create, query
    Controls how frozen state is propagated upstream from currently frozen nodes.
Valid values are "none" for no propagation, "safe" for propagation upstream
only when all downstream nodes are frozen, and "force" for propagation upstream
when any downstream node is frozen.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/freezeOptions.html 
    """
