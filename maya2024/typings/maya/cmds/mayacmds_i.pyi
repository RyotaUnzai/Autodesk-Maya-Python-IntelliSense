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


def iconTextButton(align: string, annotation: string, backgroundColor: tuple[float, float, float], command: script, commandRepeatable: boolean, defineTemplate: string, disabledImage: string, docTag: string, doubleClickCommand: script, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, flat: boolean, flipX: boolean, flipY: boolean, font: string, fullPathName: boolean, handleNodeDropCallback: script, height: int, highlightColor: tuple[float, float, float], highlightImage: string, image: string, image1: string, image2: string, image3: string, imageOverlayLabel: string, isObscured: boolean, label: string, labelEditingCallback: script, labelOffset: int, manage: boolean, marginHeight: uint, marginWidth: uint, noBackground: boolean, numberOfPopupMenus: boolean, overlayLabelBackColor: tuple[float, float, float, float], overlayLabelColor: tuple[float, float, float], parent: string, popupMenuArray: boolean, preventOverride: boolean, rotation: float, scaleIcon: boolean, selectionImage: string, sourceType: string, statusBarMessage: string, style: string, useAlpha: boolean, useTemplate: string, version: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 iconTextButton(
[string]
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [command=script], [commandRepeatable=boolean], [defineTemplate=string], [disabledImage=string], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [flat=boolean], [flipX=boolean], [flipY=boolean], [font=string], [fullPathName=boolean], [handleNodeDropCallback=script], [height=int], [highlightColor=[float, float, float]], [highlightImage=string], [image=string], [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string], [labelEditingCallback=script], [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint], [noBackground=boolean], [numberOfPopupMenus=boolean], [overlayLabelBackColor=[float, float, float, float]], [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rotation=float], [scaleIcon=boolean], [selectionImage=string], [sourceType=string], [statusBarMessage=string], [style=string], [useAlpha=boolean], [useTemplate=string], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

iconTextButton is undoable, queryable, and editable.
This command creates an iconTextButton that can be displayed with different
icons, with or without accompanying text label. When an argument is
passed, it is used to give a name to the iconTextButton.




Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout( adjustableColumn=True )
cmds.iconTextButton( style='textOnly', image1='sphere.png', label='sphere' )
cmds.iconTextButton( style='iconOnly', image1='spotlight.png', label='spotlight' )
cmds.iconTextButton( style='iconAndTextHorizontal', image1='cone.png', label='cone' )
cmds.iconTextButton( style='iconAndTextVertical', image1='cube.png', label='cube' )
cmds.showWindow( window )

---
Return:
---


    string: The name of the iconTextButton.

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
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/iconTextButton.html 
    """


def iconTextCheckBox(align: string, annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, defineTemplate: string, disabledImage: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, flat: boolean, flipX: boolean, flipY: boolean, font: string, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], highlightImage: string, image: string, image1: string, image2: string, image3: string, imageOverlayLabel: string, isObscured: boolean, label: string, labelOffset: int, manage: boolean, marginHeight: uint, marginWidth: uint, noBackground: boolean, numberOfPopupMenus: boolean, offCommand: script, onCommand: script, overlayLabelBackColor: tuple[float, float, float, float], overlayLabelColor: tuple[float, float, float], parent: string, popupMenuArray: boolean, preventOverride: boolean, rotation: float, selectionHighlightImage: string, selectionImage: string, statusBarMessage: string, style: string, useAlpha: boolean, useTemplate: string, value: boolean, version: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 iconTextCheckBox(
[string]
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [disabledImage=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [flat=boolean], [flipX=boolean], [flipY=boolean], [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [highlightImage=string], [image=string], [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string], [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint], [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script], [overlayLabelBackColor=[float, float, float, float]], [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rotation=float], [selectionHighlightImage=string], [selectionImage=string], [statusBarMessage=string], [style=string], [useAlpha=boolean], [useTemplate=string], [value=boolean], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

iconTextCheckBox is undoable, queryable, and editable.
This command creates an iconTextCheckBox.




Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout( adjustableColumn=True )
cmds.iconTextCheckBox( style='textOnly', image1='sphere.png', label='sphere' )
cmds.iconTextCheckBox( style='iconOnly', image1='spotlight.png', label='spotlight' )
cmds.iconTextCheckBox( style='iconAndTextHorizontal', image1='cone.png', label='cone' )
cmds.iconTextCheckBox( style='iconAndTextVertical', image1='cube.png', label='cube' )
cmds.showWindow( window )

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
changeCommand(cc): script
    properties: create, query, edit
    Command executed when the control's state is changed.
Note that this flag should not be used in conjunction with
onCommand and offCommand. That is, one should either use
changeCommand and test the state of the control from inside
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
flat(fla): boolean
    properties: create, query, edit
    Sets whether the control will be a flat button (0 false, 1 true).

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
    properties: create, query, edit
    Command executed when the control is turned off.

---
onCommand(onc): script
    properties: create, query, edit
    Command executed when the control is turned on.

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
selectionHighlightImage(shi): string
    properties: create, query, edit
    Image displayed while the control is selected and the cursor
is over the control. Image size
must be the same as the image specified with the -i/image
flag. This is a Windows only flag.

---
selectionImage(si): string
    properties: create, query, edit
    Image displayed while the control is selected. Image size
must be the same as the image specified with the -i/image
flag. This is a Windows only flag.

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
value(v): boolean
    properties: create, query, edit
    Sets or returns the state of the control.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/iconTextCheckBox.html 
    """


def iconTextRadioButton(align: string, annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, collection: string, defineTemplate: string, disabledImage: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, flat: boolean, flipX: boolean, flipY: boolean, font: string, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], highlightImage: string, image: string, image1: string, image2: string, image3: string, imageOverlayLabel: string, isObscured: boolean, label: string, labelOffset: int, manage: boolean, marginHeight: uint, marginWidth: uint, noBackground: boolean, numberOfPopupMenus: boolean, offCommand: script, onCommand: script, overlayLabelBackColor: tuple[float, float, float, float], overlayLabelColor: tuple[float, float, float], parent: string, popupMenuArray: boolean, preventOverride: boolean, rotation: float, select: boolean, selectionHighlightImage: string, selectionImage: string, statusBarMessage: string, style: string, useAlpha: boolean, useTemplate: string, version: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 iconTextRadioButton(
string
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [collection=string], [defineTemplate=string], [disabledImage=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [flat=boolean], [flipX=boolean], [flipY=boolean], [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [highlightImage=string], [image=string], [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string], [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint], [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script], [overlayLabelBackColor=[float, float, float, float]], [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rotation=float], [select=boolean], [selectionHighlightImage=string], [selectionImage=string], [statusBarMessage=string], [style=string], [useAlpha=boolean], [useTemplate=string], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

iconTextRadioButton is undoable, queryable, and editable.
This command creates a iconTextRadioButton that is added to the most
recently created iconTextRadioCollection unless the -cl/cluster flag is
used.




Example:
---
import maya.cmds as cmds

cmds.window( tlc=(100, 400) )
cmds.columnLayout( adj=True )
cmds.iconTextRadioCollection( 'itRadCollection' )
cmds.iconTextRadioButton( st='textOnly', i1='sphere.png', l='sphere' )
cmds.iconTextRadioButton( st='iconOnly', i1='spotlight.png', l='spotlight' )
cmds.iconTextRadioButton( st='iconAndTextHorizontal', i1='cone.png', l='cone' )
cmds.iconTextRadioButton( st='iconAndTextVertical', i1='cube.png', l='cube' )
cmds.showWindow()

---
Return:
---


    string: The name of the iconTextRadioButton created.

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
changeCommand(cc): script
    properties: create, query, edit
    Command executed when the control's state is changed.
Note that this flag should not be used in conjunction with
onCommand and offCommand. That is, one should either use
changeCommand and test the state of the control from inside
the callback, or use onCommand and offCommand as separate
callbacks.

---
collection(cl): string
    properties: create
    To explicitly add the control to the specified collection.

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
flat(fla): boolean
    properties: create, query, edit
    Sets whether the control will be a flat button (0 false, 1 true).

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
    properties: create, query, edit
    Command executed when the control is turned off.

---
onCommand(onc): script
    properties: create, query, edit
    Command executed when the control is turned on.

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
select(sl): boolean
    properties: create, query, edit
    Will set this button as the selected one.

---
selectionHighlightImage(shi): string
    properties: create, query, edit
    Image displayed while the control is selected and the cursor
is over the control. Image size
must be the same as the image specified with the -i/image
flag. This is a Windows only flag.

---
selectionImage(si): string
    properties: create, query, edit
    Image displayed while the control is selected. Image size
must be the same as the image specified with the -i/image
flag. This is a Windows only flag.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/iconTextRadioButton.html 
    """


def iconTextRadioCollection(collectionItemArray: boolean, defineTemplate: string, disableCommands: boolean, exists: boolean, gl: boolean, numberOfCollectionItems: boolean, parent: string, select: string, useTemplate: string) -> string:
    """Synopsis:
---
---
 iconTextRadioCollection(
[string]
    , [collectionItemArray=boolean], [defineTemplate=string], [disableCommands=boolean], [exists=boolean], [gl=boolean], [numberOfCollectionItems=boolean], [parent=string], [select=string], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

iconTextRadioCollection is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window( tlc=(100, 400) )
cmds.columnLayout( adj=True )
cmds.iconTextRadioCollection( 'itRadCollection' )
cmds.iconTextRadioButton( st='textOnly', i1='sphere.png', l='sphere' )
cmds.iconTextRadioButton( st='iconOnly', i1='spotlight.png', l='spotlight' )
cmds.iconTextRadioButton( st='iconAndTextHorizontal', i1='cone.png', l='cone' )
cmds.iconTextRadioButton( st='iconAndTextVertical', i1='cube.png', l='cube' )
cmds.showWindow()

---
Return:
---


    string: The name of the iconTextRadioCollection created.

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
disableCommands(dcm): boolean
    properties: edit
    Allows a particular iconTextRadioButton in the collection to
be selected without invoking the commands attached to
the -cc/changeCommand, -onc/onCommand, or -ofc/offCommand flags.
This flag is only meaningful when used in conjuction with
the -edit and -select flags.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
gl(gl): boolean
    properties: create, query
    Set the collection to have no parent layout.  If the collection has
a parent layout then it will be deleted with that layout, otherwise
if it is specified to be global it must be explicitly deleted.

---
numberOfCollectionItems(nci): boolean
    properties: query
    Returns the number of items that are in this collection.

---
parent(p): string
    properties: create
    Set the specified layout to be the parent layout of the cluster.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/iconTextRadioCollection.html 
    """


def iconTextScrollList(allowMultiSelection: boolean, annotation: string, append: string, backgroundColor: tuple[float, float, float], changeCommand: script, defineTemplate: string, deselectAll: boolean, docTag: string, doubleClickCommand: script, dragCallback: script, dragFeedbackVisible: boolean, dropCallback: script, dropRectCallback: script, editIndexed: uint, editable: boolean, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, itemAt: tuple[int, int], itemTextColor: tuple[int, float, float, float], manage: boolean, noBackground: boolean, numberOfIcons: uint, numberOfPopupMenus: boolean, numberOfRows: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, removeAll: boolean, selectCommand: script, selectIndexedItem: int, selectItem: string, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, visualRectAt: tuple[int, int], width: int) -> string:
    """Synopsis:
---
---
 iconTextScrollList(
[string]
    , [allowMultiSelection=boolean], [annotation=string], [append=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [deselectAll=boolean], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dragFeedbackVisible=boolean], [dropCallback=script], [dropRectCallback=script], [editIndexed=uint], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [itemAt=[int, int]], [itemTextColor=[int, float, float, float]], [manage=boolean], [noBackground=boolean], [numberOfIcons=uint], [numberOfPopupMenus=boolean], [numberOfRows=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [removeAll=boolean], [selectCommand=script], [selectIndexedItem=int], [selectItem=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [visualRectAt=[int, int]], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

iconTextScrollList is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.paneLayout()
cmds.iconTextScrollList(allowMultiSelection=True, append=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'), selectItem='six' )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


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
    Script to run when the list changes

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deselectAll(da): boolean
    properties: create, edit
    Deselect all items.

---
docTag(dtg): string
    properties: create, query, edit
    Add a documentation flag to the control.  The documentation flag
has a directory structure.
(e.g., -dt render/multiLister/createNode/material)

---
doubleClickCommand(dcc): script
    properties: create, edit
    Specify the command to be executed when an item is double clicked.

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
dragFeedbackVisible(dfv): boolean
    properties: create, edit
    Should the drag feedback be shown in the scrollbar?

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
editIndexed(ei): uint
    properties: create, edit
    Index of the edited field

---
editable(ed): boolean
    properties: create, edit
    Set the field to be editable or not

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
itemAt(ia): [int, int]
    properties: query
    Return the name of the item, if any, located at given point
      In query mode, this flag needs a value.

---
itemTextColor(itc): [int, float, float, float]
    properties: create, edit, multiuse
    Set the text color of the item at the given index. Arguments are:
index, red, green, and blue. Indices are 1-based. Each color
component ranges in value from 0.0 to 1.0.

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
numberOfIcons(nic): uint
    properties: query
    Number of icons.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
numberOfRows(nr): boolean
    properties: query
    Number of visible rows.

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
visualRectAt(vra): [int, int]
    properties: query
    Return the visual rectangle of the item, if any, located at given point. The
result is a an array of 4 integers, in local coordinates, describing the
rectangle, in the following order: left, top, width, height.
      In query mode, this flag needs a value.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/iconTextScrollList.html 
    """


def iconTextStaticLabel(align: string, annotation: string, backgroundColor: tuple[float, float, float], defineTemplate: string, disabledImage: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, flipX: boolean, flipY: boolean, font: string, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], image: string, image1: string, image2: string, image3: string, imageOverlayLabel: string, isObscured: boolean, label: string, labelOffset: int, manage: boolean, marginHeight: uint, marginWidth: uint, noBackground: boolean, numberOfPopupMenus: boolean, overlayLabelBackColor: tuple[float, float, float, float], overlayLabelColor: tuple[float, float, float], parent: string, popupMenuArray: boolean, preventOverride: boolean, rotation: float, statusBarMessage: string, style: string, useAlpha: boolean, useTemplate: string, version: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 iconTextStaticLabel(
string
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [disabledImage=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [flipX=boolean], [flipY=boolean], [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image=string], [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string], [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint], [noBackground=boolean], [numberOfPopupMenus=boolean], [overlayLabelBackColor=[float, float, float, float]], [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rotation=float], [statusBarMessage=string], [style=string], [useAlpha=boolean], [useTemplate=string], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

iconTextStaticLabel is undoable, queryable, and editable.
This command creates an iconTextStaticLabel.




Example:
---
import maya.cmds as cmds

cmds.window( tlc=(100, 400) )
cmds.columnLayout()
cmds.iconTextStaticLabel( st='textOnly', i1='sphere.png', l='sphere' )
cmds.iconTextStaticLabel( st='iconOnly', i1='spotlight.png', l='spotlight' )
cmds.iconTextStaticLabel( st='iconAndTextHorizontal', i1='cone.png', l='cone' )
cmds.iconTextStaticLabel( st='iconAndTextVertical', i1='cube.png', l='cube' )
cmds.showWindow()

---
Return:
---


    string: The name of the iconTextStaticLabel created.

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
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/iconTextStaticLabel.html 
    """


def ikHandle(autoPriority: boolean, connectEffector: boolean, createCurve: boolean, createRootAxis: boolean, curve: name, disableHandles: boolean, enableHandles: boolean, endEffector: string, exists: string, forceSolver: boolean, freezeJoints: boolean, jointList: boolean, name: string, numSpans: int, parentCurve: boolean, positionWeight: float, priority: int, rootOnCurve: boolean, rootTwistMode: boolean, setupForRPsolver: boolean, simplifyCurve: boolean, snapCurve: boolean, snapHandleFlagToggle: boolean, snapHandleToEffector: boolean, solver: string, startJoint: string, sticky: string, twistType: string, weight: float) -> string:
    """Synopsis:
---
---
 ikHandle(
object
    , [autoPriority=boolean], [connectEffector=boolean], [createCurve=boolean], [createRootAxis=boolean], [curve=name], [disableHandles=boolean], [enableHandles=boolean], [endEffector=string], [exists=string], [forceSolver=boolean], [freezeJoints=boolean], [jointList=boolean], [name=string], [numSpans=int], [parentCurve=boolean], [positionWeight=float], [priority=int], [rootOnCurve=boolean], [rootTwistMode=boolean], [setupForRPsolver=boolean], [simplifyCurve=boolean], [snapCurve=boolean], [snapHandleFlagToggle=boolean], [snapHandleToEffector=boolean], [solver=string], [startJoint=string], [sticky=string], [twistType=string], [weight=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikHandle is undoable, queryable, and editable.
If there are 2 joints selected and neither -startJoint nor
-endEffector flags are not specified, then the handle will be
created from the selected joints.

If a single joint is selected and neither -startJoint nor
-endEffector flags are specified, then the handle will be
created with the selected joint as the end-effector and the
start joint will be the top of the joint chain containing the
end effector.

The default values of the flags are:

-name "ikHandle#"
-priority 1
-weight 1.0
-positionWeight 1.0
-solver "ikRPsolver"
-forceSolver on
-snapHandleFlagToggle on
-sticky off
-createCurve true
-simplifyCurve true
-rootOnCurve true
-twistType linear
-createRootAxis false
-parentCurve true
-snapCurve false
-numSpans 1
-rootTwistMode false.

These attributes can be specified in creation mode, edited in
edit mode (-e) or queried in query mode (-q).




Example:
---
import maya.cmds as cmds

Will create a handle from Joint-1 to an end-effector at
the location of Joint-5 with a priority of 2 and a
weight of 0.5
---

cmds.ikHandle( sj='joint1', ee='joint5', p=2, w=.5 )

Create a handle called leg from the start joint
named hip to the end-effector named Ankle.
---

cmds.ikHandle( n='Leg', sj='Hip', ee='Ankle' )

---
Return:
---


    string: Command result

Flags:
---


---
autoPriority(ap): boolean
    properties: edit
    Specifies that this handle's priority is assigned
automatically.  The assigned priority will be based on
the hierarchy distance from the root of the skeletal
chain to the start joint of the handle.

---
connectEffector(ce): boolean
    properties: create, edit
    This option is set to true as default, meaning that
end-effector translate is connected with the endJoint translate.

---
createCurve(ccv): boolean
    properties: create
    Specifies if a curve should automatically be created for
the ikSplineHandle.

---
createRootAxis(cra): boolean
    properties: create
    Specifies if a root transform should automatically
be created above the joints affected by the ikSplineHandle.
This option is used to prevent the root flipping singularity
on a motion path.

---
curve(c): name
    properties: create, query, edit
    Specifies the curve to be used by the ikSplineHandle. Joints
will be moved to align with this curve. This flag is mandatory if you use
the -freezeJoints option.

---
disableHandles(dh): boolean
    properties: edit
    set given handles to full fk (ikBlend attribute = 0.0)

---
enableHandles(eh): boolean
    properties: edit
    set given handles to full ik (ikBlend attribute = 1.0)

---
endEffector(ee): string
    properties: create, query, edit
    Specifies the end-effector of the handle's joint chain.
The end effector may be specified with a joint or an
end-effector.  If a joint is specified, an end-effector will
be created at the same position as the joint and this
new end-effector will be used as the end-effector.

---
exists(ex): string
    properties: edit
    Indicates if the specified handle exists or not.

---
forceSolver(fs): boolean
    properties: create, query, edit
    Forces the solver to be used everytime.
It could also be known as animSticky. So, after you set
the first key the handle is sticky.

---
freezeJoints(fj): boolean
    properties: create, edit
    Forces the curve, specfied by -curve option, to align itself along the existing joint chain.
When false, or unspecified, the joints will be moved to positions along the specified curve.

---
jointList(jl): boolean
    properties: edit
    Returns the list of joints that the handle is manipulating.

---
name(n): string
    properties: create, query, edit
    Specifies the name of the handle.

---
numSpans(ns): int
    properties: create
    Specifies the number of spans in the
automatically generated curve of the ikSplineHandle.

---
parentCurve(pcv): boolean
    properties: create
    Specifies if the curve should automatically
be parented to the parent of the first joint affected
by the ikSplineHandle.

---
positionWeight(pw): float
    properties: create, query, edit
    Specifies the position/orientation weight of a handle.
This is used to compute the "distance" between the goal
position and the end-effector position.  A positionWeight of
1.0 computes the distance as the distance between
positions only and ignores the orientations.  A positionWeight
of 0.0 computes the distance as the distance between the
orientations only and ignores the positions.  A positionWeight
of 0.5 attempts to weight the distances equally but
cannot actually compute this due to unit differences.
Because there is no way to add linear units and angular units.

---
priority(p): int
    properties: create, query, edit
    Sets the priority of the handle.  Logically, all handles
with a lower number priority are solved before any
handles with a higher numbered priority.  (All handles
of priority 1 are solved before any handles of priority
2 and so on.)  Handle priorities must be ] 0.

---
rootOnCurve(roc): boolean
    properties: create, query, edit
    Specifies if the root is
locked onto the curve of the ikSplineHandle.

---
rootTwistMode(rtm): boolean
    properties: create, query, edit
    Specifies whether the start joint is allowed to
twist or not. If not, then the required twist is distributed over the
remaining joints. This applies to all the twist types.

---
setupForRPsolver(srp): boolean
    properties: edit
    If the flag is set and ikSolver is ikRPsolver, call
RPRotateSetup for the new ikHandle. It is for ikRPsolver only.

---
simplifyCurve(scv): boolean
    properties: create
    Specifies if the ikSplineHandle curve should be simplified.

---
snapCurve(snc): boolean
    properties: create
    Specifies if the curve should automatically
snap to the first joint affected by the ikSplineHandle.

---
snapHandleFlagToggle(shf): boolean
    properties: create, query, edit
    Specifies that the handle position should be snapped to
the end-effector position if the end-effector is moved
by the user.  Setting this flag on allows you to use
forward kinematics to pose or adjust your skeleton and
then to animate it with inverse kinematics.

---
snapHandleToEffector(see): boolean
    properties: edit
    All handles are immediately moved so that the handle
position and orientation matches the end-effector
position and orientation.

---
solver(sol): string
    properties: create, query, edit
    Specifies the solver.  The complete list of
available solvers may not be known until run-time
because some of the solvers may be implemented as
plug-ins.  Currently the only valid solver are
ikRPsolver, ikSCsolver and ikSplineSolver.

---
startJoint(sj): string
    properties: create, query, edit
    Specifies the start joint of the handle's joint chain.

---
sticky(s): string
    properties: create, query, edit
    Specifies that this handle is "sticky". Valid values are "off",
"sticky", "superSticky". Sticky handles
are solved when the skeleton is being manipulated
interactively.  If a character has sticky feet, the
solver will attempt to keep them in the same position as
the user moves the character's root.  If they were not
sticky, they would move along with the root.

---
twistType(tws): string
    properties: create, query, edit
    Specifies the type of interpolation to
be used by the ikSplineHandle.  The interpolation options are
"linear", "easeIn", "easeOut", and "easeInOut".

---
weight(w): float
    properties: create, query, edit
    Specifies the handles weight in error calculations.  The
weight only applies when handle goals are in conflict
and cannot be solved simultaneously.  When this happens,
a solution is computed that weights the "distance" from
each goal to the solution by the handle's weight and
attempts to minimize this value.  The weight must be ]= 0.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikHandle.html 
    """


def ikHandleCtx(autoPriorityH: boolean, createCurve: boolean, createRootAxis: boolean, exists: boolean, forceSolverH: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, numSpans: int, parentCurve: boolean, poWeightH: float, priorityH: int, rootOnCurve: boolean, rootTwistMode: boolean, simplifyCurve: boolean, snapCurve: boolean, snapHandleH: boolean, solverTypeH: string, stickyH: string, twistType: string, weightH: float) -> string:
    """Synopsis:
---
---
 ikHandleCtx(
object
    , [autoPriorityH=boolean], [createCurve=boolean], [createRootAxis=boolean], [exists=boolean], [forceSolverH=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [numSpans=int], [parentCurve=boolean], [poWeightH=float], [priorityH=int], [rootOnCurve=boolean], [rootTwistMode=boolean], [simplifyCurve=boolean], [snapCurve=boolean], [snapHandleH=boolean], [solverTypeH=string], [stickyH=string], [twistType=string], [weightH=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikHandleCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Edit an existing context to create an ikHandle with snapping on.
---

if cmds.ikHandleCtx( 'ikHandleCtx', q=True, ex=True ):
  cmds.ikHandleCtx('ikHandleCtx', e=True, snapHandleH=True)

---
Return:
---


    string: Context name

Flags:
---


---
autoPriorityH(apH): boolean
    properties: create, query, edit
    Specifies that this handle's priority is assigned
automatically.
C: The default is off.
Q: When queried, this flag returns an int.

---
createCurve(ccv): boolean
    properties: create, query, edit
    Specifies if a curve should be automatically created
for the ikSplineHandle. The flag is ignored in the ikHandleCtx.
C: The default is on. 
Q: When queried, this flag returns an int.

---
createRootAxis(cra): boolean
    properties: edit
    Specifies if a root transform should automatically
be created above the joints affected by the ikSplineHandle.
This option is used to prevent the
root flipping singularity on a motion path. This flag is ignored in
the ikHandleCtx.
C: The default is off. 
Q: When queried, this flag returns an int.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
forceSolverH(fsH): boolean
    properties: create, query, edit
    Specifies if the ikSolver is enabled for the ikHandle.
C: The default is on. 
Q: When queried, this flag returns an int.

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
numSpans(ns): int
    properties: edit
    Specifies the number of spans in the automatically generated
curve of the ikSplineHandle. This flag is ignored in the
ikHandleCtx.
C: The default is 1. 
Q: When queried, this flag returns an int.

---
parentCurve(pcv): boolean
    properties: edit
    Specifies if the curve should automatically be parented to the
parent of the first joint affected by the ikSplineHandle. The
flag is ignored in the ikHandleCtx.
C: The default is on. 
Q: When queried, this flag returns an int.

---
poWeightH(pwH): float
    properties: create, query, edit
    Specifies the position/orientation weight of the
ikHandle.
C: The default is 1.
Q: When queried, this flag returns a float.

---
priorityH(pH): int
    properties: create, query, edit
    Specifies the priority of the ikHandle.
C: The default is 1.
Q: When queried, this flag returns an int.

---
rootOnCurve(roc): boolean
    properties: edit
    Specifies if the root is locked onto the curve
of the ikSplineHandle. This flag is ignored in the ikHandleCtx. 
C: The default is on. 
Q: When queried, this flag returns an int.

---
rootTwistMode(rtm): boolean
    properties: edit
    Specifies whether the start joint is allowed to twist or not.
If not, then the required twist is distributed over the
remaining joints. This applies to all the twist types.
This flag is ignored in the ikHandleCtx. 
C: The default is off. 
Q: When queried, this flag returns an int.

---
simplifyCurve(scv): boolean
    properties: edit
    Specifies if the ikSplineHandle curve should be simplified.
This flag is ignored in the ikHandleCtx.
C: The default is on. 
Q: When queried, this returns an int.

---
snapCurve(snc): boolean
    properties: edit
    Specifies if the curve should automatically snap
to the first joint affected by the ikSplineHandle. This flag is
ignored in the ikHandleCtx.
C: The default is off. 
Q: When queried, this flag returns an int.

---
snapHandleH(snH): boolean
    properties: create, query, edit
    Specifies if the ikHandle snapping is on.
C: The default is on.
Q: When queried, this flag returns an int.

---
solverTypeH(stH): string
    properties: create, query, edit
    Lists what ikSolver is being used. The
ikSplineSolver may not be selected. To use an ikSplineSolver
use the ikSplineHandleCtx command. 
C: The default solver is the default set by the user preferences.
Q: When queried, this flag returns a string.

---
stickyH(sH): string
    properties: create, query, edit
    Specifies if the ikHandle is sticky or not. Valid strings
are "sticky" and "off".
C: The default is "off".
Q: When queried, this flag returns a string.

---
twistType(tws): string
    properties: edit
    Specifies the type of interpolation to be used by the
ikSplineHandle. This flag is ignored in the ikHandleCtx.
The interpolation options are "linear", "easeIn", "easeOut", and
"easeInOut". 
C: The default is "linear". 
Q: When queried, this flag returns a string.

---
weightH(wH): float
    properties: create, query, edit
    Specifies the weight of the ikHandle.
C: The default is 1.
Q: When queried, this flag returns a float.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikHandleCtx.html 
    """


def ikHandleDisplayScale() -> float:
    """Synopsis:
---
---
 ikHandleDisplayScale(
float
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikHandleDisplayScale is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Half the display size with respect to the default size.
cmds.ikHandleDisplayScale( 0.5 )

---
Return:
---


    float: Returns current display size of ikHandle.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikHandleDisplayScale.html 
    """


def ikSolver(epsilon: float, maxIterations: int, name: string, solverType: string) -> string:
    """Synopsis:
---
---
 ikSolver(
[object]
    , [epsilon=float], [maxIterations=int], [name=string], [solverType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikSolver is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

creates fooSolver of type ikSCsolver with max error of 0.5
---

cmds.ikSolver( st='ikSCsolver', ep=0.5, n='fooSolver' )

---
Return:
---


    string: Command result

Flags:
---


---
epsilon(ep): float
    properties: create, query, edit
    max error

---
maxIterations(mxi): int
    properties: create, query, edit
    Sets the max iterations for a solution

---
name(n): string
    properties: create, query, edit
    Name of solver

---
solverType(st): string
    properties: create, query, edit
    valid solverType (only ikSystem knows what is valid) for
creation of a new solver (required)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikSolver.html 
    """


def ikSplineHandleCtx(autoPriorityH: boolean, createCurve: boolean, createRootAxis: boolean, exists: boolean, forceSolverH: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, numSpans: int, parentCurve: boolean, poWeightH: float, priorityH: int, rootOnCurve: boolean, rootTwistMode: boolean, simplifyCurve: boolean, snapCurve: boolean, snapHandleH: boolean, solverTypeH: string, stickyH: string, twistType: string, weightH: float) -> string:
    """Synopsis:
---
---
 ikSplineHandleCtx(
object
    , [autoPriorityH=boolean], [createCurve=boolean], [createRootAxis=boolean], [exists=boolean], [forceSolverH=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [numSpans=int], [parentCurve=boolean], [poWeightH=float], [priorityH=int], [rootOnCurve=boolean], [rootTwistMode=boolean], [simplifyCurve=boolean], [snapCurve=boolean], [snapHandleH=boolean], [solverTypeH=string], [stickyH=string], [twistType=string], [weightH=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikSplineHandleCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Edit an existing context to create an ikSplineHandle with
   the curve parented to the corresponding joint.
---

if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
  cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)

---
Return:
---


    string: The name of the context.

Flags:
---


---
autoPriorityH(apH): boolean
    properties: create, query, edit
    Specifies that this handle's priority is assigned
automatically.
C: The default is off.
Q: When queried, this flag returns an int.

---
createCurve(ccv): boolean
    properties: create, query, edit
    Specifies if a curve should be automatically created
for the ikSplineHandle. 
C: The default is on. 
Q: When queried, this flag returns an int.

---
createRootAxis(cra): boolean
    properties: edit
    Specifies if a root transform should automatically
be created above the joints affected by the ikSplineHandle.
This option is used to prevent the
root flipping singularity on a motion path. 
C: The default is off. 
Q: When queried, this flag returns an int.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
forceSolverH(fsH): boolean
    properties: create, query, edit
    Specifies if the ikSolver is enabled for the ikHandle.
C: The default is on. 
Q: When queried, this flag returns an int.

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
numSpans(ns): int
    properties: edit
    Specifies the number of spans in the automatically generated
curve of the ikSplineHandle. 
C: The default is 1. 
Q: When queried, this flag returns an int.

---
parentCurve(pcv): boolean
    properties: edit
    Specifies if the curve should automatically be parented to the
parent of the first joint affected by the ikSplineHandle. 
C: The default is on. 
Q: When queried, this flag returns an int.

---
poWeightH(pwH): float
    properties: create, query, edit
    Specifies the position/orientation weight of the
ikHandle.
C: The default is 1.
Q: When queried, this flag returns a float.

---
priorityH(pH): int
    properties: create, query, edit
    Specifies the priority of the ikHandle.
C: The default is 1.
Q: When queried, this flag returns an int.

---
rootOnCurve(roc): boolean
    properties: edit
    Specifies if the root is locked onto the curve
of the ikSplineHandle. 
C: The default is on. 
Q: When queried, this flag returns an int.

---
rootTwistMode(rtm): boolean
    properties: edit
    Specifies whether the start joint is allowed to twist or not.
If not, then the required twist is distributed over the
remaining joints. This applies to all the twist types.
C: The default is off. 
Q: When queried, this flag returns an int.

---
simplifyCurve(scv): boolean
    properties: edit
    Specifies if the ikSplineHandle curve should be simplified. 
C: The default is on. 
Q: When queried, this returns an int.

---
snapCurve(snc): boolean
    properties: edit
    Specifies if the curve should automatically snap
to the first joint affected by the ikSplineHandle. 
C: The default is off. 
Q: When queried, this flag returns an int.

---
snapHandleH(snH): boolean
    properties: create, query, edit
    Specifies if the ikHandle snapping is on. This flag
is ignored for the ikSplineSolver.
C: The default is on.
Q: When queried, this flag returns an int.

---
solverTypeH(stH): string
    properties: create, query, edit
    Lists what ikSolver is being used. For the
ikSplineContext the solver can only be the ikSplineSolver
and this flag is ignored. 
C: The default solver is the ikSplineSolver.
Q: When queried, this flag returns a string.

---
stickyH(sH): string
    properties: create, query, edit
    Specifies if the ikHandle is sticky or not. Valid strings
are "sticky" and "off". This flag is ignored for the ikSplineSolver.
C: The default is "off".
Q: When queried, this flag returns a string.

---
twistType(tws): string
    properties: edit
    Specifies the type of interpolation to be used by the
ikSplineHandle. 
The interpolation options are "linear", "easeIn", "easeOut", and
"easeInOut".
C: The default is "linear". 
Q: When queried, this flag returns a string.

---
weightH(wH): float
    properties: create, query, edit
    Specifies the weight of the ikHandle. This flag is
ignored in the ikSplineHandleCtx.
C: The default is 1.
Q: When queried, this flag returns a float.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikSplineHandleCtx.html 
    """


def ikSystem(allowRotation: boolean, autoPriority: boolean, autoPriorityMC: boolean, autoPrioritySC: boolean, list: tuple[int, int], snap: boolean, solve: boolean, solverTypes: boolean) -> string:
    """Synopsis:
---
---
 ikSystem(
[object]
    , [allowRotation=boolean], [autoPriority=boolean], [autoPriorityMC=boolean], [autoPrioritySC=boolean], [list=[int, int]], [snap=boolean], [solve=boolean], [solverTypes=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikSystem is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Prints out the solver execution order
---

cmds.ikSystem( q=True, ls=True )

Moves solver on position 2 to position 1 in
the execution order list ( zero based index )
---

cmds.ikSystem( e=True, ls=(1, 0) )

---
Return:
---


    string: Command result

Flags:
---


---
allowRotation(ar): boolean
    properties: query, edit
    Set true to allow rotation of an ik handle with keys set on
translation.

---
autoPriority(ap): boolean
    properties: edit
    set autoPriority for all ikHandles

---
autoPriorityMC(apm): boolean
    properties: edit
    set autoPriority for all multiChain handles

---
autoPrioritySC(aps): boolean
    properties: edit
    set autoPriority for all singleChain handles

---
list(ls): [int, int]
    properties: query, edit
    returns the solver execution order when in query
mode(list of strings) changes execution order when in edit mode
(int old position, int new position)

---
snap(sn): boolean
    properties: query, edit
    Set global snapping

---
solve(sol): boolean
    properties: query, edit
    Set global solve

---
solverTypes(st): boolean
    properties: query
    returns a list of valid solverTypes ( query only )

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikSystem.html 
    """


def ikSystemInfo(globalSnapHandle: boolean) -> None:
    """Synopsis:
---
---
 ikSystemInfo(
boolean
    , [globalSnapHandle=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikSystemInfo is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Enable global handle snapping
---

cmds.ikSystemInfo( gsh=True )

---


Flags:
---


---
globalSnapHandle(gsh): boolean
    properties: create, query
    If this flag is off, all ikHandles will not be snapped.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikSystemInfo.html 
    """


def ikfkDisplayMethod(display: string) -> None:
    """Synopsis:
---
---
 ikfkDisplayMethod([display=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ikfkDisplayMethod is NOT undoable, queryable, and NOT editable.ikfkDisplayMethod


Example:
---
import maya.cmds as cmds

Just display ik.
---

cmds.ikfkDisplayMethod( display='ik' )

Display ik and fk when the handle is selected
---

cmds.ikfkDisplayMethod( display='ikfk' )

---


Flags:
---


---
display(d): string
    properties: create, query
    Specify how ik/fk blending should be shown when the handle is selected.
Possible choices are "none" (do not display any blending), "ik" (only
show ik),"fk" (only show fk), and "ikfk" (show both ik and fk).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ikfkDisplayMethod.html 
    """


def illustratorCurves(caching: boolean, constructionHistory: boolean, illustratorFilename: string, nodeState: int, object: boolean, tolerance: float) -> list[string]:
    """Synopsis:
---
---
 illustratorCurves(
[string]
    , [caching=boolean], [constructionHistory=boolean], [illustratorFilename=string], [nodeState=int], [object=boolean], [tolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

illustratorCurves is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create curves from an input Adobe(R) Illustrator(R) file d:/sample.ai
and scale factor 2.54
cmds.illustratorCurves( ifn='d:/sample.ai', sf=2.54 )

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
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
illustratorFilename(ifn): string
    properties: create
    Input Adobe(R) Illustrator(R) file name.

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
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
tolerance(tl): float
    properties: create, query, edit
    CVs on the output curve get snapped if the distance
between two contiguous CVs are lesser than this tolerance value.
Default: 0.001f

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/illustratorCurves.html 
    """


def image(annotation: string, backgroundColor: tuple[float, float, float], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], image: string, isObscured: boolean, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 image(
[imageName]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

image is undoable, queryable, and editable.



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

---
Return:
---


    string: The name of the image created.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/image.html 
    """


def imagePlane(camera: string, counter: boolean, detach: boolean, dropFrame: boolean, fileName: string, frameDuration: int, height: float, imageSize: tuple[int, int], lookThrough: string, maintainRatio: boolean, name: string, negTimesOK: boolean, numFrames: int, quickTime: boolean, showInAllViews: boolean, timeCode: int, timeCodeTrack: boolean, timeScale: int, twentyFourHourMax: boolean, width: float) -> boolean:
    """Synopsis:
---
---
 imagePlane([camera=string], [counter=boolean], [detach=boolean], [dropFrame=boolean], [fileName=string], [frameDuration=int], [height=float], [imageSize=[int, int]], [lookThrough=string], [maintainRatio=boolean], [name=string], [negTimesOK=boolean], [numFrames=int], [quickTime=boolean], [showInAllViews=boolean], [timeCode=int], [timeCodeTrack=boolean], [timeScale=int], [twentyFourHourMax=boolean], [width=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

imagePlane is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

        import maya.cmds as cmds

        // create image plane with width and height example
        myImagePlane = cmds.imagePlane( width=100, height=50 )

        // create image plane with width and maintainRatio off
        myImagePlane = cmds.imagePlane( width=100, maintainRatio=False )

        // create free image plane with look through camera specified.
        myImagePlane =  cmds.imagePlane( lookThrough="persp")

        // create free image plane with look through camera specified let it only show when looking through this specified camera.
        myImagePlane =  cmds.imagePlane( lookThrough="persp", showInAllViews=false)

        // edit image plane example
        cmds.imagePlane( myImagePlane[1], e=True, w=100, h=200, mr=False ) ;

        // edit free image plane with look through camera specified.
        myImagePlane =  cmds.imagePlane( myImagePlane[1], e=True, lookThrough="side")

        // query image width height example
        cmds.imagePlane( myImagePlane[1], q=True, w=True, h=True ) ;

        // Create image plane with name
        cmds.imagePlane( name="Foo") ;
        cmds.imagePlane( width=100, height=50, name="Foo") ;

        // query loaded image ratio
        cmds.imagePlane( myImagePlane[1], q=True, iz=True );

        // Create image plane under a specified camera
        camera = cmds.camera()
        cmds.imagePlane(camera=camera[1])

---
Return:
---


    boolean: Command result

Flags:
---


---
camera(c): string
    properties: create, query, edit
    When creating, it will try to attach the created image plane to the specified camera.
If the given camera is invalid, creating will fail.
When querying, it will query which camera current image plane is attaching to.
If it has no camera attached to (free image plane), it will return an empty string.
When edit, it will make the image plane attach to the new specified camera.
If the camera given is invalid, it will do nothing.
When the image plane is attached to a camera, the image plane's transform node will be set identity.
The detach command will not restore the original position of the image plane.
but the undo command will restore the original position of the image plane.

---
counter(cn): boolean
    properties: 
    Query the 'counter' flag of the movie's timecode format.
If this is true, the timecode returned by the -timeCode flag will be a simple counter.
If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).

---
detach(d): boolean
    properties: edit
    This flag can only be used in the edit mode, when this flag is used in edit, it will
detach current image plane from any camera it attaches to and make it a free image plane.

---
dropFrame(df): boolean
    properties: query
    Query the 'drop frame' flag of the movie's timecode format.

---
fileName(fn): string
    properties: create, edit
    Set the image name for image plane to read.

---
frameDuration(fd): int
    properties: query
    Query the frame duration of the movie's timecode format.

---
height(h): float
    properties: create, query, edit
    Height of the image plane. When creating, if this flag is not specified,
it will use 10.0 as default height.

---
imageSize(iz): [int, int]
    properties: query
    Get size of the loaded image.

---
lookThrough(lt): string
    properties: create, query, edit
    The camera currently used for image plane to look through.

---
maintainRatio(mr): boolean
    properties: create, query, edit
    Let the image plane respect the picture aspect ratio. When creating,
if this flag is not specified, it will use true as default value.

---
name(n): string
    properties: create, query
    Set the image plane node name when creating or return the image plane name when querying.

---
negTimesOK(nt): boolean
    properties: query
    Query the 'neg times OK' flag of the movie's timecode format.

---
numFrames(nf): int
    properties: query
    Query the whole number of frames per second of the movie's timecode format.

---
quickTime(qt): boolean
    properties: query
    Query whether the image plane is using a QuickTime movie.

---
showInAllViews(sia): boolean
    properties: create, query, edit
    The flag is used to show the current image plane in all views or not.

---
timeCode(tc): int
    properties: query
    Query the whole number of frames per second of the movie's timecode format.

---
timeCodeTrack(tt): boolean
    properties: query
    Query whether the movie on the image plane has a timecode track.

---
timeScale(ts): int
    properties: query
    Query the timescale of the movie's timecode format.

---
twentyFourHourMax(tf): boolean
    properties: query
    Query the '24 hour max' flag of the movie's timecode format.

---
width(w): float
    properties: create, query, edit
    Width of the image plane. When creating, if this flag is not specified,
it will use 10.0 as default width.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/imagePlane.html 
    """


def imfPlugins(extension: string, keyword: string, multiFrameSupport: string, pluginName: string, readSupport: string, writeSupport: string) -> list[string]:
    """Synopsis:
---
---
 imfPlugins([string], [extension=string], [keyword=string], [multiFrameSupport=string], [pluginName=string], [readSupport=string], [writeSupport=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

imfPlugins is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.imfPlugins( query=True )
returns a list of all imf plugin names
cmds.imfPlugins( 'pluginName', query=True, ext=True )
returns image file extension of the plugin
cmds.imfPlugins( 'pluginName', query=True, key=True )
returns IMF keyword of the plugin
cmds.imfPlugins( 'imfKeyWord', query=True, pn=True )
returns plugin name corresponding to imf keyword
cmds.imfPlugins( 'imfKeyWord', query=True, ws=True )
returns true if this plugin key supports write operations
cmds.imfPlugins( 'imfKeyWord', query=True, rs=True )
returns true if this plugin key supports read operations
cmds.imfPlugins( 'imfKeyWord', query=True, mfs=True )
returns true if this plugin key supports multiframe input/output

---
Return:
---


    list[string]: Command result

Flags:
---


---
extension(ext): string
    properties: create, query
    image file extension

---
keyword(key): string
    properties: create, query
    imf keyword

---
multiFrameSupport(mfs): string
    properties: create, query
    multi frame IO is supported

---
pluginName(pn): string
    properties: create, query
    imf plugin name

---
readSupport(rs): string
    properties: create, query
    read operation is supported

---
writeSupport(ws): string
    properties: create, query
    write operation is supported

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/imfPlugins.html 
    """


def inViewEditor(visible: boolean) -> None:
    """Synopsis:
---
---
 inViewEditor([visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

inViewEditor is NOT undoable, queryable, and NOT editable.




Example:
---
import maya.cmds as cmds

---
Show the In-View Editor outside the Show Manips context
cmds.inViewEditor(visible=1)

---


Flags:
---


---
visible(v): boolean
    properties: create, query
    Shows/hides the In-View Editor outside the Show Manips context.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/inViewEditor.html 
    """


def inViewMessage(alpha: float, assistMessage: string, backColor: uint, clear: string, clickKill: boolean, dragKill: boolean, fade: boolean, fadeInTime: uint, fadeOutTime: uint, fadeStayTime: uint, font: string, fontSize: uint, frameOffset: uint, hide: boolean, message: string, minimize: boolean, position: string, restore: boolean, show: boolean, statusMessage: string, textAlpha: float, textOffset: uint, uvEditor: boolean) -> None:
    """Synopsis:
---
---
 inViewMessage([alpha=float], [assistMessage=string], [backColor=uint], [clear=string], [clickKill=boolean], [dragKill=boolean], [fade=boolean], [fadeInTime=uint], [fadeOutTime=uint], [fadeStayTime=uint], [font=string], [fontSize=uint], [frameOffset=uint], [hide=boolean], [message=string], [minimize=boolean], [position=string], [restore=boolean], [show=boolean], [statusMessage=string], [textAlpha=float], [textOffset=uint], [uvEditor=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

inViewMessage is undoable, NOT queryable, and NOT editable.
Note: On Linux, the alpha and textAlpha flags for inViewMessage are
only supported when running a window manager that supports compositing (transparency
and opacity).  Otherwise, they are ignored.  In addition, the flags for message
fading: -fade, -fadeInTime, -fadeStay and -fadeOutTime are supported,
but the message will display without a fade effect if the window manager
doesn't support compositing.




Example:
---
import maya.cmds as cmds

Create a user assist message in the center of the viewport with some of the text highlighted in yellow.
The message will fade out after the default time.
cmds.inViewMessage( amg='In-view message <hl>test</hl>.', pos='midCenter', fade=True )

---


Flags:
---


---
alpha(a): float
    properties: create
    Sets the maximum alpha transparency for the message box.

---
assistMessage(amg): string
    properties: create
    The user assistance message to be displayed, can be html format.

---
backColor(bkc): uint
    properties: create
    Sets the background color for the message using the format 0xAARRGGBB, alpha is not taken into account.

---
clear(cl): string
    properties: create
    Use this flag to clear the message at a specified position.
The supported positions are the same as for the -pos/position flag.

---
clickKill(ck): boolean
    properties: create
    Use this flag if the message needs to be deleted on mouse click.

---
dragKill(dk): boolean
    properties: create
    Use this flag if the message needs to be deleted on mouse drag.

---
fade(f): boolean
    properties: create
    Whether the message will fade after a time interval or not.

---
fadeInTime(fit): uint
    properties: create
    Sets how long it takes for the image to fade in (milliseconds).

---
fadeOutTime(fot): uint
    properties: create
    Sets how long it takes for the image to fade out (milliseconds).

---
fadeStayTime(fst): uint
    properties: create
    Sets how long the image stays at max opacity  (milliseconds).

---
font(ft): string
    properties: create
    Sets the message to a font (eg. "Arial").

---
fontSize(fts): uint
    properties: create
    Sets the message font size.

---
frameOffset(fof): uint
    properties: create
    Sets how far the message appears from the edge of the viewport in pixels.

---
hide(hd): boolean
    properties: create
    Hides all messages.

---
message(msg): string
    properties: create
    The message to be displayed, can be html format.
General message, inherited by -amg/assistMessage and -smg/statusMessage.

---
minimize(min): boolean
    properties: create
    Minimize all messages.

---
position(pos): string
    properties: create
    The position that the message will appear at relative to the active viewport.
The supported positions are:

"topLeft"
"topCenter"
"topRight"
"midLeft"
"midCenter"
"midCenterTop"
"midCenterBot"
"midRight"
"botLeft"
"botCenter"
"botRight"

---
restore(res): boolean
    properties: create
    Restore all messages.

---
show(sh): boolean
    properties: create
    Shows all messages.

---
statusMessage(smg): string
    properties: create
    The status info message to be displayed, can be html format.

---
textAlpha(ta): float
    properties: create
    Sets the maximum alpha transparency for the message text.

---
textOffset(tof): uint
    properties: create
    Sets how far the text appears from the edge of the message box in pixels.

---
uvEditor(uv): boolean
    properties: create
    Show the message in the active UV editor view.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/inViewMessage.html 
    """


def inheritTransform(off: boolean, on: boolean, preserve: boolean, toggle: boolean) -> None:
    """Synopsis:
---
---
 inheritTransform(
[objects...]
    , [off=boolean], [on=boolean], [preserve=boolean], [toggle=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

inheritTransform is undoable, queryable, and NOT editable.
If the -p flag is specified then the object's transformation will
be modified to compensate when changing the inherit flag so the
object will not change its world-space location.




Example:
---
import maya.cmds as cmds

create an circle, move it off center, group it
and move the group so that the circle is back in center
cmds.circle( nr=(0, 1, 0), n='circle1' )
cmds.move( 2, 0, 0 )
cmds.group()
cmds.move( -2, 0, 0 )

turn off inherits transform flag of circle1.
The circle will now appear at (2, 0, 0)
cmds.inheritTransform( 'circle1', off=True )

turn off inherits transform flag of circle1 but preserve the
position of the circle. The circle will stay centered at (0, 0, 0)
cmds.inheritTransform( 'circle1', on=True )
cmds.inheritTransform( 'circle1', off=True, preserve=True )

query state of inherits transform flag
cmds.inheritTransform( 'circle1', q=True )

---


Flags:
---


---
off(off): boolean
    properties: create, query
    turn off inherit state for the given object(s)

---
on(on): boolean
    properties: create, query
    turn on inherit state for the given object(s)

---
preserve(p): boolean
    properties: create, query
    preserve the objects world-space position
by modifying the object(s) transformation
matrix.

---
toggle(tgl): boolean
    properties: create, query
    toggle the inherit state for the given object(s)
(default if no flags are given)
-on
turn on inherit state for the given object(s)
-off
turn off inherit state for the given object(s)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/inheritTransform.html 
    """


def insertJoint() -> string:
    """Synopsis:
---
---
 insertJoint(
[object]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

insertJoint is undoable, NOT queryable, and NOT editable.
The given joint(or selected joint) should not have skin attached.
The command works on the selected joint. No options or flags are necessary.




Example:
---
import maya.cmds as cmds

Will insert a new joint under joint2. Child joints of joint2 will be
under the new inserted joint.
cmds.insertJoint( 'joint2' )

---
Return:
---


    string: The name of the new inserted joint

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/insertJoint.html 
    """


def insertJointCtx(exists: boolean, image1: string, image2: string, image3: string) -> string:
    """Synopsis:
---
---
 insertJointCtx([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

insertJointCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.insertJointCtx()

---
Return:
---


    string: The name of the context.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/insertJointCtx.html 
    """


def insertKeyCtx(breakdown: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, preserveTangent: boolean) -> string:
    """Synopsis:
---
---
 insertKeyCtx(
contextName
    , [breakdown=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [preserveTangent=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

insertKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a insert key context for the graph editor
---

cmds.insertKeyCtx( 'insertKeyContext' )

---
Return:
---


    string: Context name

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/insertKeyCtx.html 
    """


def insertKnotCurve(addKnots: boolean, caching: boolean, constructionHistory: boolean, curveOnSurface: boolean, insertBetween: boolean, name: string, nodeState: int, numberOfKnots: int, object: boolean, parameter: float, replaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 insertKnotCurve(
curve
    , [addKnots=boolean], [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [insertBetween=boolean], [name=string], [nodeState=int], [numberOfKnots=int], [object=boolean], [parameter=float], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

insertKnotCurve is undoable, queryable, and editable.
An edit point will appear where you insert the knot. Also, the
number of spans and CVs in the curve will increase in the area where
the knot is inserted.

You can insert up to "degree" knots at a
curve parameter that isn't already an edit point. eg. for a
degree three curve, you can insert up to 3 knots.

Use this operation if you need more CVs in a local area of the curve.
Use this operation (or "hardenPoint") if you want to create a corner
in a curve.




Example:
---
import maya.cmds as cmds

cmds.insertKnotCurve( 'curve1', ch=True, p=0.3, nk=2 )
cmds.insertKnotCurve( 'curve1.u[0.3]', ch=True, nk=2 )
Both commands will insert two knots into curve1 at parameter value 0.3.
Because the ch flag is used, a dependency node is created.

cmds.insertKnotCurve( 'curve1', ch=True, add=False, p=0.5, nk=3 )
Inserts enough knots into curve1 at parameter value 0.5 to
achieve a knot multiplicity of 3.  Because the ch flag is used,
a dependency node is created.

cmds.insertKnotCurve( 'curve1', ch=True, p=(0.3, 0.5, 0.8) )
Inserts a default of one knot at each parameter value: 0.3, 0.5 and 0.8.

cmds.insertKnotCurve( 'curve1', ch=True, p=(0.3, 0.5, 0.8), nk=2 )
Inserts two knots at each parameter value: 0.3, 0.5 and 0.8.

cmds.insertKnotCurve( 'curve1', ch=True, p=(0.1, 0.3, 0.5, 0.8), nk=(1, 2) )
RuntimeError: Number of knot flags must match number of parameter flags.

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
addKnots(add): boolean
    properties: create, query, edit
    Whether to add knots or complement.  Complement means knots will be added to reach the specified number of knots.
Default: true

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
insertBetween(ib): boolean
    properties: create, query, edit
    If set to true, and there is more than one parameter value specified,
the knots will get inserted at equally spaced intervals between
the given parameter values, rather than at the parameter values
themselves.
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
numberOfKnots(nk): int
    properties: create, query, edit, multiuse
    How many knots to insert.  At any point on the curve, there can
be a maximum of "degree" knots.
Default: 1

---
parameter(p): float
    properties: create, query, edit, multiuse
    Parameter value(s) where knots are added
Default: 0.0

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
curveOnSurface(cos): boolean
    properties: create
    If possible, create 2D curve as a result.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/insertKnotCurve.html 
    """


def insertKnotSurface(addKnots: boolean, caching: boolean, constructionHistory: boolean, direction: int, insertBetween: boolean, name: string, nodeState: int, numberOfKnots: int, object: boolean, parameter: float, replaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 insertKnotSurface(
surface
    , [addKnots=boolean], [caching=boolean], [constructionHistory=boolean], [direction=int], [insertBetween=boolean], [name=string], [nodeState=int], [numberOfKnots=int], [object=boolean], [parameter=float], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

insertKnotSurface is undoable, queryable, and editable.
You must specify one, none or all number of knots with the "-nk" flag.
eg. if you specify none, then the default (one) knot will be added
at each specified parameter value.  If you specify one "-nk" value
then that number of knots will be added at each parameter value.
Otherwise, you must specify the same number of "-nk" flags as "-p" flags,
defining the number of knots to be added at each specified parameter value.

You can insert up to "degree" knots at a
parameter value that isn't already an isoparm.  eg. for a degree 3
surface, you can insert up to 3 knots.

Use this operation if you need more CVs in a local area of the surface.
Use this operation if you want to create a corner in the surface.

Note: A single insertKnotSurface command cannot insert in both directions
at once; you must use two separate commands to do this.




Example:
---
import maya.cmds as cmds

cmds.insertKnotSurface( 'surface1', ch=True, p=0.3, d=0 )
cmds.insertKnotSurface( 'surface1.v[0.3]', ch=True )
Inserts one knot (which is the default) into surface1 at
parameter value v = 0.3.  When an isoparm is specified, the direction
and parameter value is implied and the "p" and "d" flags can be omitted.

cmds.insertKnotSurface( 'surface1', ch=True, p=0.3, nk=2, d=0 )
Inserts two knots into surface1 at parameter value v = 0.3.

cmds.insertKnotSurface( 'surface1', ch=True, p=0.3, p=0.5, p=0.8, nk=2, d=0 )
Inserts two knots at each parameter value v = 0.3, 0.5 and 0.8.

cmds.insertKnotSurface( 'surface1', ch=True, p=0.5, add=False, nk=3, d=1 )
Inserts enough knots into surface1 at parameter value u = 0.5 to
achieve a knot multiplicity of 3.

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
addKnots(add): boolean
    properties: create, query, edit
    Whether to add knots or complement.  Complement means knots will be added to reach the specified number of knots.
Default: true

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
direction(d): int
    properties: create, query, edit
    Direction in which to insert knot:
0 - V direction,
1 - U direction
Default: 1

---
insertBetween(ib): boolean
    properties: create, query, edit
    If set to true, and there is more than one parameter value specified,
the knots will get inserted at equally spaced intervals between
the given parameter values, rather than at the parameter values
themselves.
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
numberOfKnots(nk): int
    properties: create, query, edit, multiuse
    How many knots to insert
Default: 1

---
parameter(p): float
    properties: create, query, edit, multiuse
    Parameter value(s) where knots are added
Default: 0.0

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/insertKnotSurface.html 
    """


def instance(leaf: boolean, name: string, smartTransform: boolean) -> string:
    """Synopsis:
---
---
 instance(
[objects]
    , [leaf=boolean], [name=string], [smartTransform=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

instance is undoable, NOT queryable, and NOT editable.
If no objects are given, then the selected list is instanced.
When an object is instanced a  new transform node is created
that points to the selected object.

The smart transform feature allows instance to transform newly
instanced objects based on previous transformations between instances.

Example: Instance an object and move it to a new location.  Instance
it again with the smart transform flag.  It should have moved once
again the distance you had previously moved it.

Note: changing the selected list between smart instances will cause
the transform information to be deleted.

It returns a list of the new objects created by the instance operation.

See also: duplicate




Example:
---
import maya.cmds as cmds

Create a hierarchy
cmds.sphere( n='sphere1' )
cmds.move( 3, 0, 0 )
cmds.sphere( n='sphere2' )
cmds.move( -3, 0, 0 )
cmds.group( 'sphere1', 'sphere2', n='group1' )
cmds.group( 'group1', n='group2' )

Create an instance of one of the spheres
cmds.instance( 'sphere1' )

Duplicate the hierarchy except for the shapes which are
instanced.instances of all leaf level shapes
cmds.instance( 'group1', leaf=True )

Create a row of 4 instanced circles which are equally spaced
cmds.circle( n='circle1' )
cmds.instance()
cmds.move( 3, 0, 0 )
cmds.instance( smartTransform=True )
cmds.instance( smartTransform=True )

---
Return:
---


    string: - the name of the new transform node is returned.

Flags:
---


---
leaf(lf): boolean
    properties: create
    Instances leaf-level objects. Acts like duplicate
except leaf-level objects are instanced.

---
name(n): string
    properties: create
    Name to give new instance

---
smartTransform(st): boolean
    properties: create
    Transforms instances item based on movements between
transforms

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/instance.html 
    """


def instanceable(allow: boolean, recursive: boolean, shape: boolean) -> boolean[]:
    """Synopsis:
---
---
 instanceable([allow=boolean], [recursive=boolean], [shape=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

instanceable is undoable, queryable, and NOT editable.
Flags one or more DAG nodes so that they can (or cannot) be instanced.
This command sets an internal state on the specified DAG nodes which is
checked whenever Maya attempts an instancing operation.
If no node names are provided on the command line then the current selection list is used.


Sets are automatically expanded to their constituent objects. Nodes which are already
instanced (or have children which are already instanced) cannot be marked as non-instancable.




Example:
---
import maya.cmds as cmds

create a sphere.
flag the transform and its shape as non-instanceable, then try to instance the sphere.
you get an error because the shape is non-instanceable.
cmds.sphere()
cmds.instanceable( allow=0, shape=True )
cmds.instance()
Error: '|nurbsSphere1' has non-instanceable children thus it cannot be instanced.

Flag the sphere and its shape as instanceable. Then it can be instanced.
cmds.instanceable( allow=1, shape=True )
cmds.instance()
Result: nurbsSphere2 ---


---
Return:
---


    boolean[]: For query execution.

Flags:
---


---
allow(a): boolean
    properties: create, query
    Specifies the new instanceable state for the node. Specify true to allow the node
to be instanceable, and false to prevent it from being instanced. The default is true
(i.e. nodes can be instanced by default).

---
recursive(r): boolean
    properties: create
    Can be specified with the -allow flag in create or edit mode to recursively apply the
-allow setting to all non-shape children of the selected node(s). To also affect
shapes, also specify the -shape flag along with -recursive.

---
shape(s): boolean
    properties: create
    Can be specified with the -allow flag in create or edit mode to apply the
-allow setting to all shape children of the selected node(s). This flag can be
specified in conjunction with the -recursive flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/instanceable.html 
    """


def instancer(addObject: boolean, cycle: string, cycleStep: float, cycleStepUnits: string, index: int, levelOfDetail: string, name: string, object: string, objectPosition: string, objectRotation: string, objectScale: string, pointDataSource: boolean, removeObject: boolean, rotationOrder: string, rotationUnits: string, valueName: string) -> string:
    """Synopsis:
---
---
 instancer([addObject=boolean], [cycle=string], [cycleStep=float], [cycleStepUnits=string], [index=int], [levelOfDetail=string], [name=string], [object=string], [objectPosition=string], [objectRotation=string], [objectScale=string], [pointDataSource=boolean], [removeObject=boolean], [rotationOrder=string], [rotationUnits=string], [valueName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

instancer is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.polySphere(n='myShape')
cmds.instancer( name='myInstancerNode', a=True, object='myShape' )

---
Return:
---


    string: Command result

Flags:
---


---
addObject(a): boolean
    properties: create, edit
    This flag indicates that objects specified by the -object flag will be added to
the instancer node as instanced objects.

---
cycle(c): string
    properties: create, query, edit
    This flag sets or queries the cycle attribute for the instancer node.
The options are "none" or "sequential".  The default is "none".

---
cycleStep(cs): float
    properties: create, query, edit
    This flag sets or queries the cycle step attribute for the instancer node.  This attribute
indicates the size of the step in frames or seconds (see cycleStepUnit).

---
cycleStepUnits(csu): string
    properties: create, query, edit
    This flag sets or queries the cycle step unit attribute for the instancer
node.  The options are "frames" or "seconds".  The default is "frames".

---
index(i): int
    properties: query
    This flag is used to query the name of the ith instanced object.

---
levelOfDetail(lod): string
    properties: create, query, edit
    This flag sets or queries the level of detail of the instanced objects.  The
options are "geometry", "boundingBox", "boundingBoxes".  The default is
"geometry".

---
name(n): string
    properties: create, query
    This flag sets or queries the name of the instancer node.

---
object(obj): string
    properties: create, query, edit, multiuse
    This flag indicates which objects will be add/removed from the list of instanced
objects.  The flag is used in conjuction with the -add and -remove flags.  If
neither of these flags is specified on the command line then -add is assumed.

---
objectPosition(op): string
    properties: query
    This flag queries the given objects position.  This object can be any instanced object or
sub-object.

---
objectRotation(objectRotation): string
    properties: query
    This flag queries the given objects rotation.  This object can be any instanced object or
sub-object.

---
objectScale(os): string
    properties: query
    This flag queries the given objects scale.  This object can be any instanced object or
sub-object.

---
pointDataSource(pds): boolean
    properties: query
    This flag is used to query the source node supply the data for the input points.

---
removeObject(rm): boolean
    properties: edit
    This flag indicates that objects specified by the -object flag will be
removed from the instancer node as instanced objects.

---
rotationOrder(ro): string
    properties: create, query, edit
    This flag specifies the rotation order associated with the rotation flag.  The
options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.

---
rotationUnits(ru): string
    properties: create, query, edit
    This flag specifies the rotation units associated with the rotation flag.  The
options are degrees or radians.  By default the attribute is degrees.

---
valueName(vn): string
    properties: query
    This flag is used to query the value(s) of the array associated with the given
name.  If the -index flag is used in conjuction with this flag then the ith
value will be returned.  Otherwise, the entire array will be returned.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/instancer.html 
    """


def intField(annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, defineTemplate: string, docTag: string, dragCallback: script, dragCommand: script, dropCallback: script, editable: boolean, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, enterCommand: script, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, maxValue: int, minValue: int, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, receiveFocusCommand: script, statusBarMessage: string, step: int, useTemplate: string, value: int, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 intField(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [maxValue=int], [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [receiveFocusCommand=script], [statusBarMessage=string], [step=int], [useTemplate=string], [value=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

intField is undoable, queryable, and editable.-s/step



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.intField()
cmds.intField( editable=False )
cmds.intField( minValue=-10, maxValue=10, value=0 )
cmds.intField( minValue=-1000, maxValue=1000, step=10 )
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
invisible slider.

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
The value of the field can always be changed with
the -v/value flag regardless of the state of
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
maxValue(max): int
    properties: create, query, edit
    Upper limit of the field.

---
minValue(min): int
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
step(s): int
    properties: create, query, edit
    Increment for the invisible slider.  The field value
will change by this amount when the invisible slider is dragged.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): int
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/intField.html 
    """


def intFieldGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dragCommand: script, dropCallback: script, enable: boolean, enable1: boolean, enable2: boolean, enable3: boolean, enable4: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, extraLabel: string, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, noBackground: boolean, numberOfFields: int, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, rowAttach: tuple[int, string, int], statusBarMessage: string, useTemplate: string, value: tuple[int, int, int, int], value1: int, value2: int, value3: int, value4: int, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 intFieldGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean], [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfFields=int], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [useTemplate=string], [value=[int, int, int, int]], [value1=int], [value2=int], [value3=int], [value4=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

intFieldGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label text and
editable integer fields. The label text is optional and one to
four fields can be created.




Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
cmds.intFieldGrp( numberOfFields=3, label='Scale', extraLabel='cm', value1=3, value2=5, value3=1 )
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
    Set the number of fields on creation.  One to four fields
are available.  The default is one field.

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
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): [int, int, int, int]
    properties: create, query, edit
    Values for all fields.

---
value4(v4): int
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/intFieldGrp.html 
    """


def intScrollBar(annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, defineTemplate: string, docTag: string, dragCallback: script, dragCommand: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], horizontal: boolean, isObscured: boolean, largeStep: int, manage: boolean, maxValue: int, minValue: int, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, statusBarMessage: string, step: int, useTemplate: string, value: int, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 intScrollBar(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean], [largeStep=int], [manage=boolean], [maxValue=int], [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [step=int], [useTemplate=string], [value=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

intScrollBar is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( adjustableColumn=True )
cmds.intScrollBar()
cmds.intScrollBar( min=-100, max=100, value=0, step=1, largeStep=10 )
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
    Orientation of the scroll bar.  This flag is true by default,
which corresponds to a horizontally oriented scroll bar.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
largeStep(ls): int
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
maxValue(max): int
    properties: create, query, edit
    Upper limit of the scroll bar.

---
minValue(min): int
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
step(s): int
    properties: create, query, edit
    Smaller increment for the scroll bar, ie. the increment
used when the arrow buttons are pressed.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): int
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/intScrollBar.html 
    """


def intSlider(annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, defineTemplate: string, docTag: string, dragCallback: script, dragCommand: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], horizontal: boolean, isObscured: boolean, manage: boolean, maxValue: int, minValue: int, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, statusBarMessage: string, step: int, useTemplate: string, value: int, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 intSlider(
string
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean], [manage=boolean], [maxValue=int], [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [step=int], [useTemplate=string], [value=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

intSlider is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( adjustableColumn=True )
cmds.intSlider()
cmds.intSlider( min=-100, max=100, value=0, step=1 )
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
maxValue(max): int
    properties: create, query, edit
    Upper limit of the slider.

---
minValue(min): int
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
step(s): int
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
value(v): int
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/intSlider.html 
    """


def intSliderGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dragCommand: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, extraLabel: string, field: boolean, fieldMaxValue: int, fieldMinValue: int, fieldStep: int, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, maxValue: int, minValue: int, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, rowAttach: tuple[int, string, int], sliderStep: int, statusBarMessage: string, step: int, useTemplate: string, value: int, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 intSliderGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [field=boolean], [fieldMaxValue=int], [fieldMinValue=int], [fieldStep=int], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [maxValue=int], [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [sliderStep=int], [statusBarMessage=string], [step=int], [useTemplate=string], [value=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

intSliderGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of controls containing a
label text, an integer field and an integer slider. The text and field
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

intSliderGrp -min -10 -max 10 -fieldMinValue -100 -fieldMaxValue 100;

Then you will be able to use the slider to select any value from -10 to 10.
At the same time you will be able to enter into the field any value
from -100 to 100.  If you enter a value, say 20, then the new slider
range will grow such that this value is now accessible through the slider
as well.  In fact, the new slider limit will become double of that what you
entered.  Note that the slider limits will never grow beyond the field
limits, in other words if you entered the value 80 then the slider will be
clipped to the field limit of 100 and not doubled to 160.

TelfBaseGrpCmd.cpp




Example:
---
import maya.cmds as cmds

   Create a window with a couple integer slider groups.  The first will
   use default limit values, and the second will set up a group that has
   a field range greater than the slider range.  Try entering values
   greater than the slider limits in both groups.
---

window = cmds.window( title='intSliderGrp Example' )
cmds.columnLayout()
cmds.intSliderGrp( field=True, label='Group 1' )
cmds.intSliderGrp( field=True, label='Group 2', minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0 )
cmds.showWindow( window )

---
Return:
---


    string: Full path name of the control on creation.

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
    The command string executed when the value of the
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
    The command string executed repeatedly during a drag
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
    If true on creation the group will have an editable int field
present that reflects the value of the slider.

---
fieldMaxValue(fmx): int
    properties: create, query, edit
    Maximum value that may be entered in the field.  This
value may be set to any value greater than
the -max/maxValue flag.  By default, it is equal to
the -max/maxValue flag.

---
fieldMinValue(fmn): int
    properties: create, query, edit
    Minimum value that may be entered in the field.  This
value may be set to any value less than
the -min/minValue flag.  By default, it is equal to
the -min/minValue flag.

---
fieldStep(fs): int
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
Returns a string on query.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxValue(max): int
    properties: create, query, edit
    Sets the maximum value for both the slider and the field.

---
minValue(min): int
    properties: create, query, edit
    Sets the minimum value for both the slider and the field.

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
rowAttach(rat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column, attachment type, offset.
Possible attachments are: top | bottom | both.
Specifies attachment types and offsets for the entire row.

---
sliderStep(ss): int
    properties: create, query, edit
    On Linux the slider step value represents the
amount the value will increase or decrease when you click either
side of the slider.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): int
    properties: create, query, edit
    Increment for both the slider and field.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): int
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/intSliderGrp.html 
    """


def internalVar(mayaInstallDir: boolean, userAppDir: boolean, userBitmapsDir: boolean, userHotkeyDir: boolean, userMarkingMenuDir: boolean, userPrefDir: boolean, userPresetsDir: boolean, userScriptDir: boolean, userShelfDir: boolean, userTmpDir: boolean, userWorkspaceDir: boolean) -> string:
    """Synopsis:
---
---
 internalVar([mayaInstallDir=boolean], [userAppDir=boolean], [userBitmapsDir=boolean], [userHotkeyDir=boolean], [userMarkingMenuDir=boolean], [userPrefDir=boolean], [userPresetsDir=boolean], [userScriptDir=boolean], [userShelfDir=boolean], [userTmpDir=boolean], [userWorkspaceDir=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

internalVar is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

myScriptDir = cmds.internalVar(userScriptDir=True)

---
Return:
---


    string: The value of the variable specified by the flag use.

Flags:
---


---
mayaInstallDir(mid): boolean
    properties: create
    Return the Maya installation directory.

---
userAppDir(uad): boolean
    properties: create
    Return the user application directory.

---
userBitmapsDir(ubd): boolean
    properties: create
    Return the user bitmaps prefs directory.

---
userHotkeyDir(uhk): boolean
    properties: create
    Return the user hotkey directory.

---
userMarkingMenuDir(umm): boolean
    properties: create
    Return the user marking menu directory.

---
userPrefDir(upd): boolean
    properties: create
    Return the user preference directory.

---
userPresetsDir(ups): boolean
    properties: create
    Return the user presets directory.

---
userScriptDir(usd): boolean
    properties: create
    Return the user script directory.

---
userShelfDir(ush): boolean
    properties: create
    Return the user shelves directory.

---
userTmpDir(utd): boolean
    properties: create
    Return a temp directory.  Will check for TMPDIR environment variable,
otherwise will return the current directory.

---
userWorkspaceDir(uwd): boolean
    properties: create
    Return the user workspace directory
(also known as the projects directory).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/internalVar.html 
    """


def intersect(caching: boolean, constructionHistory: boolean, curveOnSurface: boolean, firstSurface: boolean, name: string, nodeState: int, object: boolean, tolerance: linear) -> list[string]:
    """Synopsis:
---
---
 intersect(
[surface] [surface]
    , [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [firstSurface=boolean], [name=string], [nodeState=int], [object=boolean], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

intersect is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Intersect the two active surfaces and create the resulting curve on
surface as a 3D curve (note: only one 3D curve is created for each
pair of intersecting surfaces):
cmds.intersect( cos=True )

Intersect the nurbs sphere and nurbs plane, creating a curve-on-surface
on each surface:
cmds.intersect( 'nurbsSphere1', 'nurbsPlane1', fs=True )

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
firstSurface(fs): boolean
    properties: query, edit
    Creates a curve-on-surface on the first surface only or
on all surfaces (default).

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
    Tolerance to fit to.
Default: 0.01

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
curveOnSurface(cos): boolean
    properties: create
    If possible, create 2D curve as a result.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/intersect.html 
    """


def iprEngine(copy: string, defineTemplate: string, diagnostics: boolean, estimatedMemory: boolean, exists: boolean, iprImage: string, motionVectorFile: boolean, object: name, region: tuple[int, int, int, int], relatedFiles: boolean, releaseIprImage: boolean, resolution: boolean, scanlineIncrement: string, showProgressBar: boolean, startTuning: boolean, stopTuning: boolean, underPixel: tuple[int, int], update: boolean, updateDepthOfField: boolean, updateLightGlow: boolean, updateMotionBlur: boolean, updatePort: string, updateShaderGlow: boolean, updateShading: boolean, updateShadowMaps: boolean, useTemplate: string) -> string:
    """Synopsis:
---
---
 iprEngine([copy=string], [defineTemplate=string], [diagnostics=boolean], [estimatedMemory=boolean], [exists=boolean], [iprImage=string], [motionVectorFile=boolean], [object=name], [region=[int, int, int, int]], [relatedFiles=boolean], [releaseIprImage=boolean], [resolution=boolean], [scanlineIncrement=string], [showProgressBar=boolean], [startTuning=boolean], [stopTuning=boolean], [underPixel=[int, int]], [update=boolean], [updateDepthOfField=boolean], [updateLightGlow=boolean], [updateMotionBlur=boolean], [updatePort=string], [updateShaderGlow=boolean], [updateShading=boolean], [updateShadowMaps=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

iprEngine is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a iprEngine and tell it about an already created ipr image.
cmds.iprEngine(ipr='iprImages/persp_scene1_ipr.iff')

Tell the iprEngine about the region to update.
cmds.iprEngine( 'iprEngine1', e=True, region=(10, 10, 100, 100))

Tell the iprEngine to watch changes and update pixels.
cmds.iprEngine( 'iprEngine1', e=True, startTuning=True )

---
Return:
---


    string: - the name of the ipr engine created or modified

Flags:
---


---
copy(cp): string
    properties: edit
    Copies the deep raster file, as well as its related files, to the
new location.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
diagnostics(dig): boolean
    properties: edit
    The diagnostics should be shown

---
estimatedMemory(mem): boolean
    properties: query
    Displays the estimated memory being used by IPR.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
iprImage(ipr): string
    properties: create, query, edit
    Specify the ipr image to use.

---
motionVectorFile(mvf): boolean
    properties: query
    Returns the name of the motion vector file used by IPR.

---
object(obj): name
    properties: create, query, edit
    The objects to be tuned.

---
region(r): [int, int, int, int]
    properties: create, query, edit
    The coordinates of the region to be tuned.
The integers are in the sequence left bottom right top
or x1,y2  x2,y2

---
relatedFiles(rel): boolean
    properties: query
    Returns the names for the related files, e.g, the non-glow-non-blur image,
the motion vector file, and the depth-map files.

---
releaseIprImage(rii): boolean
    properties: edit
    The ipr image should be released and
memory should    be freed.

---
resolution(res): boolean
    properties: query
    The width and height of the ipr file.

---
scanlineIncrement(sli): string
    properties: create, query, edit
    Set the scanline increment percentage.  If the height of
the region being update is 240 pixels, and the scanlineIncrement
is 10% then the image will refresh blocks of 24 scanlines.

---
showProgressBar(spb): boolean
    properties: create, query, edit
    Show progress bar during tuning.

---
startTuning(st): boolean
    properties: create, query, edit
    An ipr image has been specified and now changes
to shading    networks should force an image to be
produced.

---
stopTuning(spt): boolean
    properties: create, query, edit
    Tuning should cease but ipr image should not be closed.

---
underPixel(un): [int, int]
    properties: edit
    Get list of objects under the pixel sprcified.

---
update(u): boolean
    properties: create, edit
    Force an update.

---
updateDepthOfField(udf): boolean
    properties: create, edit
    Force a refresh of depth-of-field.

---
updateLightGlow(ulg): boolean
    properties: create, query, edit
    Automatically update when light glow changes.

---
updateMotionBlur(umb): boolean
    properties: create, query, edit
    Automatically update when 2.5D motion blur changes.

---
updatePort(up): string
    properties: create, query, edit
    The name of the port that is to be updated when
pixel values are recomputed.  (not currently supported)

---
updateShaderGlow(usg): boolean
    properties: create, query, edit
    Automatically update when shader glow changes.

---
updateShading(us): boolean
    properties: create, query, edit
    Automatically update shading.

---
updateShadowMaps(usm): boolean
    properties: create, edit
    Force the shadow maps to be generated and an update to occur.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/iprEngine.html 
    """


def isConnected(ignoreUnitConversion: boolean) -> boolean:
    """Synopsis:
---
---
 isConnected(
string string
    , [ignoreUnitConversion=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

isConnected is undoable, NOT queryable, and NOT editable.isConnectedfalsetrue
The first string specifies the source plug to check for connection.
The second one specifies the destination plug to check for connection.




Example:
---
import maya.cmds as cmds

cmds.sphere( n='jupiter' )
cmds.sphere( n='io' )
cmds.connectAttr( 'jupiter.ty', 'io.ty' )

Are the two "tx" attributes on transform1 and transform2 connected?
cmds.isConnected( 'jupiter.tx', 'io.tx' )
Result: 0 ---


Are the two "ty" attributes on transform1 and transform2 connected?
cmds.isConnected( 'jupiter.ty', 'io.ty' )
Result: 1 ---


---
Return:
---


    boolean: Are the two plugs connected?

Flags:
---


---
ignoreUnitConversion(iuc): boolean
    properties: create
    In looking for connections, skip past unit conversion nodes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/isConnected.html 
    """


def isDirty(connection: boolean, datablock: boolean) -> boolean:
    """Synopsis:
---
---
 isDirty(
string...
    , [connection=boolean], [datablock=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

isDirty is undoable, NOT queryable, and NOT editable.isDirty



Example:
---
import maya.cmds as cmds

Create a plusMinusAverage node and a transform. We set the 'skipSelect'
flag so that they are not displayed in the Attribute Editor because
that would force an evaluation and cause the plugs to become clean.
import maya.cmds as cmds
cmds.createNode('plusMinusAverage', n='pma', skipSelect=True)
cmds.createNode('transform', n='t', skipSelect=True)

Hide the transform so that Maya's draw won't force an evaluation which
would clean its plugs.
cmds.hide('t')

Connect the transform's 'tx' to one of the plusMinusAverage node's
inputs.
cmds.connectAttr('t.tx', 'pma.input1D[0]')

Set the value of the transform's 'tx' and check that the
target of the connection has become dirty.
cmds.setAttr('t.tx', 13)
cmds.isDirty('pma.input1D[0]')
Result: 1 ---


If we retrieve the value of the destination attribute
then the connection becomes clean.
cmds.getAttr('pma.input1D[0]')
Result: 13.0 ---

cmds.isDirty('pma.input1D[0]')
Result: 0 ---


A plusMinusAverage node's 'output1D' attribute depends
upon the values in its 'input1D' array. Since we haven't
retrieved its value yet, it should still be dirty. However,
it seems to be clean:
cmds.isDirty('pma.output1D')
Result: 0 ---


The reason for this is that the 'isDirty' command
by default only checks connections and 'output1D' has
no connection to be dirty. If we instead check its
value in the datablock, we get the expected result:
cmds.isDirty('pma.output1D', d=True)
Result: 1 ---


The output value will remain dirty until we
force its evaluation by retrieving it.
cmds.getAttr('pma.output1D')
Result: 13.0 ---

cmds.isDirty('pma.output1D', d=True)
Result: 0 ---


---
Return:
---


    boolean: Is the plug dirty? If more than one plug is given then it returns the
logical "and" of all dirty states.

Flags:
---


---
connection(c): boolean
    properties: create
    Check the connection of the plug (default).

---
datablock(d): boolean
    properties: create
    Check the datablock entry for the plug.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/isDirty.html 
    """


def isTrue() -> None:
    """Synopsis:
---
---
 isTrue(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

isTrue is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.isTrue( 'SomethingSelected' )
Result: 1 ---


---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/isTrue.html 
    """


def isolateSelect(addDagObject: name, addSelected: boolean, addSelectedObjects: boolean, loadSelected: boolean, removeDagObject: name, removeSelected: boolean, state: boolean, update: boolean, viewObjects: boolean) -> boolean:
    """Synopsis:
---
---
 isolateSelect(
string
    , [addDagObject=name], [addSelected=boolean], [addSelectedObjects=boolean], [loadSelected=boolean], [removeDagObject=name], [removeSelected=boolean], [state=boolean], [update=boolean], [viewObjects=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

isolateSelect is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

create some primitives and go into component selection mode
cmds.sphere( n='sphere1' )
cmds.cone( n='cone1' )
cmds.selectMode( component=True )

Use the current modelPanel for isolation
isolated_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)

turn on isolate select mode for a particular 3d view. Only
the sphere and the selected CVs will be displayed.
cmds.select( 'sphere1.cv[0:2][*]' )
Connect the selected objects with editor and
locks the current list of objects within the mainConnection
cmds.editor( isolated_panel, edit=True, lockMainConnection=True, mainListConnection='activeList' )
cmds.isolateSelect( isolated_panel, state=1 )

add the cone to the list of objects to be viewed
cmds.select( 'cone1' )
cmds.isolateSelect( isolated_panel, addSelected=True )

make just the sphere the object to be viewed
cmds.select( 'sphere1' )
Unlock the current list of objects within the editor
cmds.editor( isolated_panel, edit=True, mainListConnection='activeList' )
cmds.isolateSelect( isolated_panel, loadSelected=True )

---
Return:
---


    boolean: When used with query

Flags:
---


---
addDagObject(ado): name
    properties: 
    Add the specified object to the set of objects to be
displayed in the view.

---
addSelected(addSelected): boolean
    properties: 
    Add the currently active objects to the set of
objects to be displayed in the view.

---
addSelectedObjects(aso): boolean
    properties: 
    Add selected objects to the set of objects to be displayed in the view.
This flag differs from addSelected in that it will ignore selected components
and add the entire object.

---
loadSelected(ls): boolean
    properties: 
    Replace the objects being displayed with the currently
active objects.

---
removeDagObject(rdo): name
    properties: 
    Remove the specified object from the set of objects to be
displayed in the view.

---
removeSelected(rs): boolean
    properties: 
    Remove the currently active objects to the set of
objects to be displayed in the view.

---
state(s): boolean
    properties: query
    Turns isolate select mode on/off.

---
update(u): boolean
    properties: 
    Update the view's list of objects due to a change
to the set of objects to be displayed.

---
viewObjects(vo): boolean
    properties: query
    Returns the name (if any) of the objectSet which contains
the list of objects visible in the view if isolate select mode
is on. If isolate select mode is off, an empty string is
returned.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/isolateSelect.html 
    """


def itemFilter(byBin: string, byName: string, byScript: string, byType: string, category: string, classification: string, clearByBin: boolean, clearByType: boolean, difference: tuple[string, string], exists: boolean, intersect: tuple[string, string], listBuiltInFilters: boolean, listOtherFilters: boolean, listUserFilters: boolean, negate: boolean, parent: string, pythonModule: string, secondScript: string, text: string, union: tuple[string, string], uniqueNodeNames: boolean) -> list[string] | string:
    """Synopsis:
---
---
 itemFilter(
[string]
    , [byBin=string], [byName=string], [byScript=string], [byType=string], [category=string], [classification=string], [clearByBin=boolean], [clearByType=boolean], [difference=[string, string]], [exists=boolean], [intersect=[string, string]], [listBuiltInFilters=boolean], [listOtherFilters=boolean], [listUserFilters=boolean], [negate=boolean], [parent=string], [pythonModule=string], [secondScript=string], [text=string], [union=[string, string]], [uniqueNodeNames=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

itemFilter is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a filter that will pass all transforms.
---

transforms = cmds.itemFilter(byType='transform')

   Create a filter that will pass all spot lights.
---

spotLights = cmds.itemFilter(byType='spotLight')

   There are two ways to create a filter that passes both
   spot lights and transforms.  You can create a filter
   that is a union of the previous two or just specify
   both object types on one filter.
---

unionFilter = cmds.itemFilter(union=(transforms, spotLights))
spotLightsAndTransforms = cmds.itemFilter(byType=('transform','spotLight'))

   Create a filter that lists all objects beginning with the
   letter "a".
---

aFilter = cmds.itemFilter(byName='a*')

   Create a filter that lists only transforms and spot lights
   that begin with the letter "a".
---

intersectionFilter = cmds.itemFilter( intersect=(spotLightsAndTransforms, aFilter) )

   Delete the filters when done with them.
---

cmds.delete( transforms, spotLights, aFilter )
cmds.delete( unionFilter, intersectionFilter )

---
Return:
---


    string: Single command result
    list[string]: Multiple command result

Flags:
---


---
byBin(bk): string
    properties: create, query, edit, multiuse
    The filter will only pass items whose bin list
contains the given string as a bin name.
This is a multi-use flag.
If more than one occurance of this flag is used in a single
command, the filter will accept a node if it matches at least
one of the given bins (in other words, a union or logical or
of all given bins.

---
byName(bn): string
    properties: create, query, edit
    The filter will only pass items whose names match the given regular
expression string.  This string can contain the special
characters * and ?.  '?' matches any one character, and '*'
matches any substring.

---
byScript(bs): string
    properties: create, query, edit
    The filter will run a MEL script named by the given string on each item name.  Items
will pass the filter if the script returns a non-zero value.
The script name string must be the name of a proc whose signature
is:
global proc int procName( string $name ) or
def procName(*args, **keywordArgs) if -pym/pythonModule is specified.
Note that if -secondScript is also used, it will always take precedence.

---
byType(bt): string
    properties: create, query, edit, multiuse
    The filter will only pass items whose typeName matches the
given string.  The typeName of an object can be found using
the nodeType command.  This is a multi-use flag.
If more than one occurance of this flag is used in a single
command, the filter will accept a node if it matches at least
one of the given types (in other words, a union or logical or
of all given types.

---
category(cat): string
    properties: create, query, edit, multiuse
    A string for categorizing the filter.

---
classification(cls): string
    properties: create, query, edit
    Indicates whether the filter is a built-in or user filter.
The string argument must be either "builtIn" or "user".
The "other" classification is deprecated. Use "user" instead.

Filters will not be deleted by a file new, and filter nodes will
be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and
will not be accessible from the command-line.

---
clearByBin(cbk): boolean
    properties: create, edit
    This flag will clear any existing bins associated with this filter.

---
clearByType(cbt): boolean
    properties: create, edit
    This flag will clear any existing typeNames associated with this filter.

---
difference(di): [string, string]
    properties: create, query, edit
    The filter will consist of the set difference of two other filters,
whose names are the given strings.
Items will pass this filter if and only if they pass the first filter but
not the second filter.

---
exists(ex): boolean
    properties: create
    Returns true|false depending upon whether the
specified object exists. Other flags are ignored.

---
intersect(intersect): [string, string]
    properties: create, query, edit
    The filter will consist of the intersection of two other filters,
whose names are the given strings.
Items will pass this filter if and only if they pass both of
the contained filters.

---
listBuiltInFilters(lbf): boolean
    properties: query
    Returns an array of all item filters with classification "builtIn".

---
listOtherFilters(lof): boolean
    properties: query
    The "other" classification is deprecated. Use "user" instead.
Returns an array of all item filters with classification "other".

---
listUserFilters(luf): boolean
    properties: query
    Returns an array of all item filters with classification "user".

---
negate(neg): boolean
    properties: create, query, edit
    This flag can be used to cause the filter to invert itself,
and reverse what passes and what fails.

---
parent(p): string
    properties: create, query, edit
    Optional.  If specified, the filter's life-span is linked to
that of the parent.  When the parent goes out of scope, so
does the filter.  If not specified, the filter will exist
until explicitly deleted.

---
pythonModule(pym): string
    properties: create, query, edit
    Treat -bs/byScript and -ss/secondScript as Python functions located in the specified module.

---
secondScript(ss): string
    properties: create, query, edit
    Cannot be used in conjunction with the -bs flag.  The second
script is for filtering whole lists at once, rather than
individually.  Its signature must be:
global proc string[] procName( string[] $name ) or
def procName(*args, **keywordArgs) if -pym/pythonModule is specified.
It should take in a list of items, and return a filtered list
of items.

---
text(t): string
    properties: create, query, edit
    Defines an annotation string to be stored with the filter

---
union(un): [string, string]
    properties: create, query, edit
    The filter will consist of the union of two other filters, whose
names are the given strings.
Items will pass this filter if they pass at least one of the
contained filters.

---
uniqueNodeNames(unn): boolean
    properties: create, query, edit
    Returns unique node names to script filters so there are no naming
conflicts.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/itemFilter.html 
    """


def itemFilterAttr(byName: string, byNameString: string, byScript: string, classification: string, dynamic: boolean, exists: boolean, hasCurve: boolean, hasDrivenKey: boolean, hasExpression: boolean, hidden: boolean, intersect: tuple[string, string], keyable: boolean, listBuiltInFilters: boolean, listOtherFilters: boolean, listUserFilters: boolean, negate: boolean, parent: string, published: boolean, readable: boolean, scaleRotateTranslate: boolean, secondScript: string, text: string, union: tuple[string, string], writable: boolean) -> list[string] | string:
    """Synopsis:
---
---
 itemFilterAttr(
[string]
    , [byName=string], [byNameString=string], [byScript=string], [classification=string], [dynamic=boolean], [exists=boolean], [hasCurve=boolean], [hasDrivenKey=boolean], [hasExpression=boolean], [hidden=boolean], [intersect=[string, string]], [keyable=boolean], [listBuiltInFilters=boolean], [listOtherFilters=boolean], [listUserFilters=boolean], [negate=boolean], [parent=string], [published=boolean], [readable=boolean], [scaleRotateTranslate=boolean], [secondScript=string], [text=string], [union=[string, string]], [writable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

itemFilterAttr is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a filter that will pass all the SRT (scale-rotate-translate)
   attributes.
---

srtFilter = cmds.itemFilterAttr('itemFilterAttr', scaleRotateTranslate=True)

   Create a filter that will pass all the attributes driven by an
   expression.
---

exprFilter = cmds.itemFilterAttr(hasExpression=True)

   Create a filter that will pass all the SRT attributes driven by an
   expression (intersect two previous ones).
---

srtExprFilter = cmds.itemFilterAttr(intersect=(srtFilter, exprFilter))

   Delete the filters when done with them.
---

cmds.delete( srtFilter, exprFilter, srtExprFilter )

---
Return:
---


    string: Single command result
    list[string]: Multiple command result

Flags:
---


---
byName(bn): string
    properties: create, query, edit
    The filter will only pass items whose names match the given regular
expression string.  This string can contain the special
characters * and ?.  '?' matches any one character, and '*'
matches any substring.
This flag cannot be used in conjunction with the -byScript or -secondScript flags.

---
byNameString(bns): string
    properties: create, query, edit, multiuse
    The filter will only pass items whose names match the given string.
This is a multi-use flag which allows the user to specify several strings.
The filter will pass items that match any of the strings.
This flag cannot be used in conjunction with the -byScript or -secondScript flags.

---
byScript(bs): string
    properties: create, query, edit
    The filter will run a MEL script named by the given string on each
attribute name.  Attributes will pass the filter if the script
returns a non-zero value.
The script name string must be the name of a proc whose signature
is:
global proc int procName( string $nodeName string $attrName )
This flag cannot be used in conjunction with the -byName or -byNameString flags.

---
classification(cls): string
    properties: create, query, edit
    Indicates whether the filter is a built-in or user filter.
The string argument must be either "builtIn" or "user".
The "other" filter classification is deprecated. Use "user"
instead.

Filters created by Maya should be classified as "builtIn".
Filters created by plugins or user scripts should be classified
as "user".

Filters will not be deleted by a file new. Filter nodes will
be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and
will not be accessible from the command-line.

---
dynamic(dy): boolean
    properties: create, query, edit
    The filter will only pass dynamic attributes

---
exists(ex): boolean
    properties: create, query, edit
    The filter will only pass attributs that exist

---
hasCurve(hc): boolean
    properties: create, query, edit
    The filter will only pass attributes that are driven by animation
curves.

---
hasDrivenKey(hdk): boolean
    properties: create, query, edit
    The filter will only pass attributes that are driven by driven keys

---
hasExpression(he): boolean
    properties: create, query, edit
    The filter will only pass attributes that are driven by expressions

---
hidden(h): boolean
    properties: create, query, edit
    The filter will only pass attributes that are hidden to the user

---
intersect(intersect): [string, string]
    properties: create, query, edit
    The filter will consist of the intersection of two other filters,
whose names are the given strings.
Attributes will pass this filter if and only if they pass both of
the contained filters.

---
keyable(k): boolean
    properties: create, query, edit
    The filter will only pass attributes that are keyable

---
listBuiltInFilters(lbf): boolean
    properties: query
    Returns an array of all attribute filters with classification "builtIn".

---
listOtherFilters(lof): boolean
    properties: query
    The "other" classification has been deprecated. Use "user" instead.
Returns an array of all attribute filters with classification "other".

---
listUserFilters(luf): boolean
    properties: query
    Returns an array of all attribute filters with classification "user".

---
negate(neg): boolean
    properties: create, query, edit
    This flag can be used to cause the filter to invert itself,
and reverse what passes and what fails.

---
parent(p): string
    properties: 
    This flag is no longer supported.

---
published(pub): boolean
    properties: create, query, edit
    The filter will only pass attributes that are published on the container.

---
readable(r): boolean
    properties: create, query, edit
    The filter will only pass attributes that are readable (outputs)

---
scaleRotateTranslate(srt): boolean
    properties: create, query, edit
    The filter will show only SRT attributes: scale, rotate, translate and
their children

---
secondScript(ss): string
    properties: create, query, edit
    Can be used in conjunction with the -bs flag.  The second
script is for filtering whole lists at once, rather than
individually.  Its signature must be:
global proc string[] procName( string[] $nodeName string[] $attrName )
It should take in a list of attributes, and return a filtered list
of attributes.
This flag cannot be used in conjunction with the -byName or -byNameString flags.

---
text(t): string
    properties: create, query, edit
    Defines an annotation string to be stored with the filter

---
union(un): [string, string]
    properties: create, query, edit
    The filter will consist of the union of two other filters, whose
names are the given strings.
Attributes will pass this filter if they pass at least one of the
contained filters.

---
writable(w): boolean
    properties: create, query, edit
    The filter will only pass attributes that are writable (inputs)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/itemFilterAttr.html 
    """


def itemFilterType(text: string, type: boolean) -> list[string] | string:
    """Synopsis:
---
---
 itemFilterType(
string
    , [text=string], [type=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

itemFilterType is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a filter that will pass all spot lights and transforms.
---

filter = cmds.itemFilter(byType=('transform', 'spotLight'))

   Now query the type of the filter.
---

type = cmds.itemFilterType(filter, q=True, type=True)
print( 'Filter type: ' + type + '\n' )

   Delete the filter.
---

cmds.delete( filter )

---
Return:
---


    string: Single command result
    list[string]: Multiple command result

Flags:
---


---
text(t): string
    properties: query, edit
    Defines an annotation string to be stored with the filter

---
type(typ): boolean
    properties: query
    Query the type of the filter object. Possible return values are:
itemFilter, attributeFilter, renderFilter, or unknownFilter.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/itemFilterType.html 
    """
