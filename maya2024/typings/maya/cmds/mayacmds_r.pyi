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


def radial(attenuation: float, magnitude: float, maxDistance: linear, name: string, perVertex: boolean, position: tuple[linear, linear, linear], torusSectionRadius: linear, type: float, volumeExclusion: boolean, volumeOffset: tuple[linear, linear, linear], volumeShape: string, volumeSweep: angle) -> string:
    """Synopsis:
---
---
 radial(
selectionList
    , [attenuation=float], [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear], [type=float], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

radial is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
A radial field pushes objects directly towards or directly away from it,
like a magnet.

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

cmds.radial( 'particle1', m=5.0, mxd=2.0 )
Creates a radial field with magnitude 5.0 and maximum distance 2.0,
and adds it to the list of fields particle1 owns.

cmds.radial( pos=(2, 0, 4 ))
Creates a radial field at position (0,2,4) in world coordinates,
with default magnitude(1.0), attentuation (1.0),
and max distance (5.0).

cmds.radial( 'radialField1', e=True, att=0.98 )
Edits the attenuation value of the field named radialField1

cmds.radial( 'radialField1', q=True, m=True )
Queries radialField1 for its magnitude.

cmds.radial( 'radialField1', e=True, mxd=10.0 )
Changes the maximum distance of the field called
"radialField1" to 10.0.

cmds.radial( m=2.0 )
Creates a radial field with magnitude 2.0 for every active selection.
If no there are active
selections, creates such a field at world position (0,0,0).

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
type(typ): float
    properties: query, edit
    Type of radial field (0 - 1).  This controls the algorithm by
which the field is attenuated. Type 1, provided for backward
compatibility, specifies the same algorithm as Alias |
Wavefront Dynamation. A value between 0 and 1 yields a linear blend.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/radial.html 
    """


def radioButton(align: string, annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, collection: string, data: int, defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, editable: boolean, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, offCommand: script, onCommand: script, parent: string, popupMenuArray: boolean, preventOverride: boolean, recomputeSize: boolean, select: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 radioButton(
[string]
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [collection=string], [data=int], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [recomputeSize=boolean], [select=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

radioButton is undoable, queryable, and editable.-cl/collection



Example:
---
import maya.cmds as cmds

cmds.window( width=150 )
cmds.columnLayout( adjustableColumn=True )
cmds.radioCollection()
cmds.radioButton( label='One' )
cmds.radioButton( label='Two' )
cmds.radioButton( label='Three' )
cmds.radioButton( label='Four' )
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
    This flag is obsolete and should no longer be used.
The radio button label will always be left-aligned.

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
    Command executed when the radio button's state is changed.
Note that this flag should not be used in conjunction with
onCommand and offCommand. That is, one should either use
changeCommand and test the state of the radio button from inside
the callback, or use onCommand and offCommand as separate
callbacks.

---
collection(cl): string
    properties: create
    To explicitly add a radio button to a collection of radio
buttons specify the name of the radio collection.

---
data(da): int
    properties: create, query, edit
    Internal data associated with the radio button.

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
    The edit state of the radio button.  By default, this flag
is set to true and the radio button value may be changed by
clicking on it.  If false then the radio button is 'read only' and
can not be clicked on. The value of the radio button can always be
changed with the -sl/select flag regardless of the state of
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
offCommand(ofc): script
    properties: create, edit
    Command executed when the radio button is turned off.

---
onCommand(onc): script
    properties: create, edit
    Command executed when the radio button is turned on.

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
select(sl): boolean
    properties: create, query, edit
    Select the radio button.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/radioButton.html 
    """


def radioButtonGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, annotation1: string, annotation2: string, annotation3: string, annotation4: string, backgroundColor: tuple[float, float, float], changeCommand: script, changeCommand1: script, changeCommand2: script, changeCommand3: script, changeCommand4: script, columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], data1: int, data2: int, data3: int, data4: int, defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, editable: boolean, enable: boolean, enable1: boolean, enable2: boolean, enable3: boolean, enable4: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, label1: string, label2: string, label3: string, label4: string, labelAnnotation: string, labelArray2: tuple[string, string], labelArray3: tuple[string, string, string], labelArray4: tuple[string, string, string, string], manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, numberOfRadioButtons: int, offCommand: script, offCommand1: script, offCommand2: script, offCommand3: script, offCommand4: script, onCommand: script, onCommand1: script, onCommand2: script, onCommand3: script, onCommand4: script, parent: string, popupMenuArray: boolean, preventOverride: boolean, rowAttach: tuple[int, string, int], select: int, shareCollection: string, statusBarMessage: string, useTemplate: string, vertical: boolean, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 radioButtonGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [annotation1=string], [annotation2=string], [annotation3=string], [annotation4=string], [backgroundColor=[float, float, float]], [changeCommand=script], [changeCommand1=script], [changeCommand2=script], [changeCommand3=script], [changeCommand4=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [data1=int], [data2=int], [data3=int], [data4=int], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean], [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [label1=string], [label2=string], [label3=string], [label4=string], [labelAnnotation=string], [labelArray2=[string, string]], [labelArray3=[string, string, string]], [labelArray4=[string, string, string, string]], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [numberOfRadioButtons=int], [offCommand=script], [offCommand1=script], [offCommand2=script], [offCommand3=script], [offCommand4=script], [onCommand=script], [onCommand1=script], [onCommand2=script], [onCommand3=script], [onCommand4=script], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [select=int], [shareCollection=string], [statusBarMessage=string], [useTemplate=string], [vertical=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

radioButtonGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates from one to four radio buttons in a single row.
By default the radio buttons will share a single collection, but they
can also share the collection of another radio button group.  The buttons
can also have an optional text label.




Example:
---
import maya.cmds as cmds

   Create a window with two separate radio button groups.
---

window = cmds.window()
cmds.columnLayout()
cmds.radioButtonGrp( label='Three Buttons', labelArray3=['One', 'Two', 'Three'], numberOfRadioButtons=3 )
cmds.radioButtonGrp( label='Four Buttons', labelArray4=['I', 'II', 'III', 'IV'], numberOfRadioButtons=4 )
cmds.showWindow( window )

   Create a window with two radio button groups that are
   linked together.
---

window = cmds.window()
cmds.columnLayout()
group1 = cmds.radioButtonGrp( numberOfRadioButtons=3, label='Colors', labelArray3=['Red', 'Blue', 'Green'] )
cmds.radioButtonGrp( numberOfRadioButtons=3, shareCollection=group1, label='', labelArray3=['Yellow', 'Orange', 'Purple'] )
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
annotation1(an1): string
    properties: create, query, edit
    specifies the tooptip of the first radiobutton

---
annotation2(an2): string
    properties: create, query, edit
    specifies the tooptip of the second radiobutton

---
annotation3(an3): string
    properties: create, query, edit
    specifies the tooptip of the third radiobutton

---
annotation4(an4): string
    properties: create, query, edit
    specifies the tooptip of the fourth radiobutton

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
    Command executed when the group changes state.
Note that this flag should not be used in conjunction with
onCommand and offCommand. That is, one should either use
changeCommand and test the state of a radio button from inside
the callback, or use onCommand and offCommand as separate
callbacks.

---
changeCommand4(cc4): script
    properties: create, edit
    Specify a changed state command for each respective radio
button.

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
data4(da4): int
    properties: create, query, edit
    Internal data associated with each radio button.

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
    The edit state of the group.  By default, this flag
is set to true and the radio button values may be changed by
clicking on them.  If false then the radio buttons are 'read only'
and can not be clicked on. The value of the radio button can
always be changed with the sl/select flags regardless of
the state of the ed/editable flag.

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enable4(en4): boolean
    properties: create, query, edit
    Enable state of the individual radio buttons.

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
    When present on creation an optional text label will be
built with the group.  The string specifies the label text.

---
label4(l4): string
    properties: create, query, edit
    Specify label strings for the respective radio buttons in
the group.

---
labelAnnotation(la): string
    properties: create, query, edit
    when present on creation an optional text label will be
built with the group . The string specifies the label tooltip

---
labelArray4(la4): [string, string, string, string]
    properties: create, query, edit
    Specify multiple labels in a single flag.  These flags
are ignored if the number of radio buttons doesn't match.

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
numberOfRadioButtons(nrb): int
    properties: create
    Number of radio buttons in the group (1 - 4).

---
offCommand(ofc): script
    properties: create, edit
    Command executed when any radio button turns off.

---
offCommand4(of4): script
    properties: create, edit
    Off command for each respective radio button.

---
onCommand(onc): script
    properties: create, edit
    Command executed when any radio button turns on.

---
onCommand4(on4): script
    properties: create, edit
    On command for each respective radio button.

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
select(sl): int
    properties: create, query, edit
    Selected radio button.  The argument is a 1 based integer.

---
shareCollection(scl): string
    properties: create
    Specify the radioButtonGrp that this radio group is to be
associated with.  By default the radio group will be a separate
collection.

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
vertical(vr): boolean
    properties: create, query
    Whether the orientation of the radio buttons in this group
are horizontal (default) or vertical.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/radioButtonGrp.html 
    """


def radioCollection(collectionItemArray: boolean, defineTemplate: string, exists: boolean, gl: boolean, numberOfCollectionItems: boolean, parent: string, select: string, useTemplate: string) -> string:
    """Synopsis:
---
---
 radioCollection(
[string]
    , [collectionItemArray=boolean], [defineTemplate=string], [exists=boolean], [gl=boolean], [numberOfCollectionItems=boolean], [parent=string], [select=string], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

radioCollection is undoable, queryable, and editable.-p/parent-gl/globaldeleteUI



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( adjustableColumn=True, rowSpacing=10 )
cmds.frameLayout( label='Colors' )
cmds.columnLayout()
collection1 = cmds.radioCollection()
rb1 = cmds.radioButton( label='Red' )
rb2 = cmds.radioButton( label='Blue' )
rb3 = cmds.radioButton( label='Green' )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.frameLayout( label='Position' )
cmds.columnLayout()
collection2 = cmds.radioCollection()
rb4 = cmds.radioButton( label='Top' )
rb5 = cmds.radioButton( label='Middle' )
rb6 = cmds.radioButton( label='Bottom' )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.radioCollection( collection1, edit=True, select=rb2 )
cmds.radioCollection( collection2, edit=True, select=rb6 )
cmds.showWindow()

---
Return:
---


    string: Full path name to the collection.

Flags:
---


---
collectionItemArray(cia): boolean
    properties: query
    Return a string list giving the long names of all the items
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
    Set the collection to have no parent layout.  Global
collections must be explicitly deleted.

---
numberOfCollectionItems(nci): boolean
    properties: query
    Return the number of items in this collection.

---
parent(p): string
    properties: create
    The parent of the collection.  The collection will be deleted
along with the parent.

---
select(sl): string
    properties: create, query, edit
    Select the specified collection item.  If queried will
return the name of the currently selected collection item.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/radioCollection.html 
    """


def radioMenuItemCollection(defineTemplate: string, exists: boolean, gl: boolean, parent: string, useTemplate: string) -> string:
    """Synopsis:
---
---
 radioMenuItemCollection(
[string]
    , [defineTemplate=string], [exists=boolean], [gl=boolean], [parent=string], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

radioMenuItemCollection is undoable, queryable, and editable.-p/parent-g/globaldeleteUI



Example:
---
import maya.cmds as cmds

cmds.window( menuBar=True )
cmds.menu( label='Position' )
cmds.radioMenuItemCollection()
cmds.menuItem( label='Top', radioButton=False )
cmds.menuItem( label='Middle', radioButton=False )
cmds.menuItem( label='Bottom', radioButton=True )
cmds.menu( label='Number' )
cmds.radioMenuItemCollection()
cmds.menuItem( label='One', radioButton=True )
cmds.menuItem( label='Two', radioButton=False )
cmds.menuItem( label='Three', radioButton=False )
cmds.showWindow()

---
Return:
---


    string: Full path name to the collection.

Flags:
---


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
    Set the collection to have no parent menu.  Global
collections must be explicitly deleted.

---
parent(p): string
    properties: create
    The parent of the collection.  The collection will be deleted
along with the parent.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/radioMenuItemCollection.html 
    """


def rampColorPort(annotation: string, backgroundColor: tuple[float, float, float], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, noBackground: boolean, node: name, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, selectedColorControl: string, selectedInterpControl: string, selectedPositionControl: string, statusBarMessage: string, useTemplate: string, verticalLayout: boolean, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 rampColorPort(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [node=name], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [selectedColorControl=string], [selectedInterpControl=string], [selectedPositionControl=string], [statusBarMessage=string], [useTemplate=string], [verticalLayout=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rampColorPort is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

ramp = cmds.createNode('ramp')
cmds.window()
cmds.columnLayout()
cmds.rampColorPort( node=ramp )
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
node(n): name
    properties: create
    Specifies the name of the newRamp texture node
this port will represent.

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
selectedColorControl(sc): string
    properties: create, edit
    Set the name of the control (if any) which is to be used to show
the color of the currently selected entry in the ramp. This control
will automatically update as the user selects different entries in
the ramp, and will modify the selected entry if edited. The type of
control must be an attrColorSliderGrp.

---
selectedInterpControl(si): string
    properties: create, edit
    Set the name of the control (if any) which is to be used to show
the interpolation of the currently selected entry in the ramp. This control
will automatically update as the user selects different entries in
the ramp, and will modify the selected entry if edited. The type of
control must be an attrEnumOptionMenuGrp.

---
selectedPositionControl(sp): string
    properties: create, edit
    Set the name of the control (if any) which is to be used to show
the position of the currently selected entry in the ramp. This control
will automatically update as the user selects different entries in
the ramp, and will modify the selected entry if edited. The type of
control must be an attrFieldSliderGrp.

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
verticalLayout(vl): boolean
    properties: create, query, edit
    Set the preview's layout.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rampColorPort.html 
    """


def rangeControl(annotation: string, backgroundColor: tuple[float, float, float], changedCommand: script, defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, maxRange: time, minRange: time, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int, widthHeight: tuple[int, int]) -> string:
    """Synopsis:
---
---
 rangeControl(
name
    , [annotation=string], [backgroundColor=[float, float, float]], [changedCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [maxRange=time], [minRange=time], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int], [widthHeight=[int, int]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rangeControl is undoable, queryable, and editable.Note



Example:
---
import maya.cmds as cmds

This will create a window with a scrollable playback range control. The initial
range is set up to be from 0 to 30, and the maximum values the
slider can access are 0 to 60.  Dragging the control's slider sets the
30-frame-long playback range within the bounded values of
0 to 60.
---

cmds.window()
cmds.frameLayout( lv=False )
cmds.playbackOptions( minTime=0, maxTime=30 )
cmds.rangeControl( 'myRangeSlider', minRange=0, maxRange=60 )
cmds.showWindow()

---
Return:
---


    string: Name of newly created rangeControl.

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
changedCommand(cc): script
    properties: create, edit
    script to be executed when the range changes

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
maxRange(max): time
    properties: create, query, edit
    Controls the max range displayable in the control

---
minRange(min): time
    properties: create, query, edit
    Controls the max range displayable in the control

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

---
widthHeight(wh): [int, int]
    properties: create, edit
    Controls the dimensions of the control

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rangeControl.html 
    """


def readTake(angle: string, device: string, frequency: float, linear: string, noTime: boolean, take: string) -> None:
    """Synopsis:
---
---
 readTake([angle=string], [device=string], [frequency=float], [linear=string], [noTime=boolean], [take=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

readTake is undoable, NOT queryable, and NOT editable.
See also: writeTake, applyTake




Example:
---
import maya.cmds as cmds

   Read data info the clock device and apply.
cmds.readTake( device='clock', take='clock.mov' )
cmds.applyTake( device='clock' )

---


Flags:
---


---
angle(a): string
    properties: create
    Sets the angular unit used in the take. Valid strings are
"deg", "degree", "rad", and "radian". 
C: The default is the current user angular unit.

---
device(d): string
    properties: create
    Specifies the device into which the take data is read. This is a
required argument.

---
frequency(f): float
    properties: create
    The timestamp is ignored and the specified frequency is used. If
timeStamp data is not in the .mov file, the -noTimestamp flag
should also be used. This flag resample, instead
the data is assumed to be at the specified frequency. 
C: If the take file does not use time stamps, the default frequency
is 60Hz.

---
linear(l): string
    properties: create
    Sets the linear unit used in the take. Valid strings are
"mm", "millimeter", "cm", "centimeter", "m", "meter", "km",
"kilometer", "in", "inch", "ft", "foot", "yd", "yard", "mi",
and "mile". 
C: The default is the current user linear unit.

---
noTime(nt): boolean
    properties: create
    Specifies if the take (.mov) file contains time stamps. 
C: The default is to assume time stamps are part of the take file.

---
take(t): string
    properties: create
    Reads the specified take file. It is safest to pass the full
path to the flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/readTake.html 
    """


def rebuildCurve(caching: boolean, constructionHistory: boolean, degree: int, endKnots: int, fitRebuild: boolean, keepControlPoints: boolean, keepEndPoints: boolean, keepRange: int, keepTangents: boolean, name: string, nodeState: int, object: boolean, range: boolean, rebuildType: int, replaceOriginal: boolean, smartSurfaceCurveRebuild: boolean, spans: int, tolerance: linear) -> list[string]:
    """Synopsis:
---
---
 rebuildCurve(
curve [curve]
    , [caching=boolean], [constructionHistory=boolean], [degree=int], [endKnots=int], [fitRebuild=boolean], [keepControlPoints=boolean], [keepEndPoints=boolean], [keepRange=int], [keepTangents=boolean], [name=string], [nodeState=int], [object=boolean], [range=boolean], [rebuildType=int], [replaceOriginal=boolean], [smartSurfaceCurveRebuild=boolean], [spans=int], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rebuildCurve is undoable, queryable, and editable.
The optional second curve can be used to specify a reference
parameterization.




Example:
---
import maya.cmds as cmds

rebuild curve to 5 uniform spans
cmds.rebuildCurve( rt=0, s=5 )

rebuild curve by reducing redundant spans
cmds.rebuildCurve( rt=1 )

rebuild curve by matching the parameterization of another curve
curve1 is the curve to rebuild
curve2 is the reference curve
cmds.rebuildCurve( 'curve1', 'curve2', rt=2 )

rebuild curve by removing all multiple interior knots
cmds.rebuildCurve( rt=3 )

rebuild curve using the curvature of the curve
to create more spans where curvature is higher
cmds.rebuildCurve( rt=4 )

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
degree(d): int
    properties: create, query, edit
    The degree of the resulting curve
1 - linear,
2 - quadratic,
3 - cubic,
5 - quintic,
7 - heptic
Default: 3

---
endKnots(end): int
    properties: create, query, edit
    End conditions for the curve
0 - uniform end knots,
1 - multiple end knots,
Default: 0

---
fitRebuild(fr): boolean
    properties: create, query, edit
    If true use the least squares fit rebuild.
Otherwise use the convert method.
Default: true

---
keepControlPoints(kcp): boolean
    properties: create, query, edit
    If true, the CVs will remain the same.
This forces uniform parameterization unless rebuildType is matchKnots.
Default: false

---
keepEndPoints(kep): boolean
    properties: create, query, edit
    If true, keep the endpoints the same.
Default: true

---
keepRange(kr): int
    properties: create, query, edit
    Determine the parameterization for the resulting curve.
0 - reparameterize the resulting curve from 0 to 1,
1 - keep the original curve parameterization,
2 - reparameterize the result from 0 to number of spans
Default: 1

---
keepTangents(kt): boolean
    properties: create, query, edit
    If true, keep the end tangents the same.
Default: true

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
rebuildType(rt): int
    properties: create, query, edit
    How to rebuild the input curve.
0 - uniform,
1 - reduce spans,
2 - match knots,
3 - remove multiple knots,
4 - curvature
5 - rebuild ends
6 - clean
Default: 0

---
smartSurfaceCurveRebuild(scr): boolean
    properties: create, query, edit
    If true, curve on surface is rebuild in 3D and 2D info is kept
Default: false

---
spans(s): int
    properties: create, query, edit
    The number of spans in resulting curve
Used only if rebuildType is uniform.
Default: 4

---
tolerance(tol): linear
    properties: create, query, edit
    The tolerance with which to rebuild.
Default: 0.01

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
range(rn): boolean
    properties: create
    Force a curve range on complete input curve.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rebuildCurve.html 
    """


def rebuildSurface(caching: boolean, constructionHistory: boolean, degreeU: int, degreeV: int, direction: int, endKnots: int, fitRebuild: int, keepControlPoints: boolean, keepCorners: boolean, keepRange: int, name: string, nodeState: int, object: boolean, polygon: int, rebuildType: int, replaceOriginal: boolean, spansU: int, spansV: int, tolerance: linear) -> list[string]:
    """Synopsis:
---
---
 rebuildSurface(
surface [surface]
    , [caching=boolean], [constructionHistory=boolean], [degreeU=int], [degreeV=int], [direction=int], [endKnots=int], [fitRebuild=int], [keepControlPoints=boolean], [keepCorners=boolean], [keepRange=int], [name=string], [nodeState=int], [object=boolean], [polygon=int], [rebuildType=int], [replaceOriginal=boolean], [spansU=int], [spansV=int], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rebuildSurface is undoable, queryable, and editable.
The optional second surface can be used to specify a reference
parameterization.




Example:
---
import maya.cmds as cmds

rebuild the surface using uniform parameterization
The rebuilt surface will have 5 spans in u and
10 spans in v
cmds.rebuildSurface( rt=0, dir=2, su=5, sv=10 )

rebuild the surface by removing its redundant spans
cmds.rebuildSurface( rt=1 )

rebuild the surface by matching the u parameterization
of another surface. surface1 is the surface to rebuild
surface2 is the reference surface
cmds.rebuildSurface( 'surface1', 'surface2', rt=2, dir=0 )

rebuild the surface by removing all multiple interior knots
cmds.rebuildSurface( rt=3 )

rebuild the surface using uniform parameterization
cmds.rebuildSurface( rt=4 )

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
degreeU(du): int
    properties: create, query, edit
    The degree of the resulting surface in the u direction
0 - maintain current,
1 - linear,
2 - quadratic,
3 - cubic,
5 - quintic,
7 - heptic
Default: 3

---
degreeV(dv): int
    properties: create, query, edit
    The degree of the resulting surface in the v direction
0 - maintain current,
1 - linear,
2 - quadratic,
3 - cubic,
5 - quintic,
7 - heptic
Default: 3

---
direction(dir): int
    properties: create, query, edit
    The direction in which to rebuild:
0 - U,
1 - V,
2 - Both U and V
Default: 2

---
endKnots(end): int
    properties: create, query, edit
    End conditions for the surface
0 - uniform end knots,
1 - multiple end knots,
Default: 0

---
fitRebuild(fr): int
    properties: create, query, edit
    Specify the type of rebuild method to be used:
0 - Convert Classic, the default and original convert method.
1 - Fit using the least squares fit method.
2 - Convert Match, alternate matching convert method.
3 - Convert Grid, uses a grid-based fit algorithm.
Default: 0

---
keepControlPoints(kcp): boolean
    properties: create, query, edit
    Use the control points of the input surface.
This forces uniform parameterization unless rebuildType is 2 (match knots)
Default: false

---
keepCorners(kc): boolean
    properties: create, query, edit
    The corners of the resulting surface will not change from the corners of the input surface.
Default: true

---
keepRange(kr): int
    properties: create, query, edit
    Determine the parameterization for the resulting surface.
0 - reparameterize the resulting surface from 0 to 1;
1 - keep the original surface parameterization;
2 - reparameterize the result from 0 to number of spans
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
rebuildType(rt): int
    properties: create, query, edit
    The rebuild type:
0 - uniform,
1 - reduce spans,
2 - match knots,
3 - remove multiple knots,
4 - force non rational
5 - rebuild ends
6 - trim convert (uniform)
7 - into Bezier mesh
Default: 0

---
spansU(su): int
    properties: create, query, edit
    The number of spans in the u direction in resulting surface. Used only when rebuildType is 0 - uniform. If 0, keep the same number of spans as the original surface.
Default: 4

---
spansV(sv): int
    properties: create, query, edit
    The number of spans in the v direction in resulting surface. Used only when rebuildType is 0 - uniform. If 0, keep the same number of spans as the original surface.
Default: 4

---
tolerance(tol): linear
    properties: create, query, edit
    The tolerance with which to rebuild
Default: 0.01

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
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rebuildSurface.html 
    """


def recordAttr(attribute: string, delete: boolean) -> None:
    """Synopsis:
---
---
 recordAttr([attribute=string], [delete=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

recordAttr is undoable, queryable, and NOT editable.
If no attributes are specified all attributes of the node
are recorded.

When the query flag is used, a list of the attributes being recorded will be returned.




Example:
---
import maya.cmds as cmds

This command will setup the translateX and translateY
attributes for recording.
cmds.recordAttr( at=['translateX', 'translateZ'] )

---


Flags:
---


---
attribute(at): string
    properties: create, multiuse
    specify the attribute to record

---
delete(d): boolean
    properties: create
    Do not record the specified attributes

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/recordAttr.html 
    """


def recordDevice(cleanup: boolean, data: boolean, device: string, duration: int, playback: boolean, state: boolean, wait: boolean) -> None:
    """Synopsis:
---
---
 recordDevice([cleanup=boolean], [data=boolean], [device=string], [duration=int], [playback=boolean], [state=boolean], [wait=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

recordDevice is undoable, queryable, and NOT editable.
See also: enableDevice, applyTake, readTake, writeTake




Example:
---
import maya.cmds as cmds

   Record the clock device for 30 seconds and apply the data.
---

import time
cmds.recordDevice( device='clock', duration=30 )
time.sleep( 30 )
cmds.recordDevice( device='clock', state=False )
cmds.applyTake( device='clock' )

---


Flags:
---


---
cleanup(c): boolean
    properties: create
    Removes the recorded data from the device.

---
data(da): boolean
    properties: query
    Specifies if the device has recorded data. If the device is
recording at the time of query, the flag will return false. 
Q: When queried, this flag returns an int.

---
device(d): string
    properties: create, multiuse
    Specifies which device(s) to start record recording.
The listed device(s) will start recording regardless of their record
enable state. 
C: The default is to start recording all devices that are
record enabled.

---
duration(dr): int
    properties: create, query
    Duration (in seconds) of the recording. When the duration
expires, the device will still be in a recording state and must
be told to stop recording. 
C: The default is 60. 
Q: When queried, this flag returns an int.

---
playback(p): boolean
    properties: create, query
    If any attribute is connected to an animation curve, the
animation curve will play back while recording the device(s)
including any animation curves attached to attributes being
recorded. 
C: The default is false. 
Q: When queried, this flag returns an int.

---
state(st): boolean
    properties: create, query
    Start or stop device recording. 
C: The default is true. 
Q: When queried, this flag returns an int.

---
wait(w): boolean
    properties: create
    If -p/playback specified, wait until playback completion before
returning control to the user. This flag is ignored if -p is not used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/recordDevice.html 
    """


def redo() -> None:
    """Synopsis:
---
---
 redo()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

redo is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

In this particular example, each line needs to be executed
separately one after the other. Executing lines separately
guaranties that commands are properly registered in the undo
stack.

cmds.polyCube()
Result: [u'pCube1', u'polyCube1'] ---


cmds.undo()
Undo: cmds.polyCube()
 ---


cmds.redo()
Redo: cmds.polyCube()
 ---

Result: [u'pCube1', u'polyCube1'] ---


---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/redo.html 
    """


def referenceEdit(applyFailedEdits: boolean, changeEditTarget: tuple[string, string], editCommand: string, failedEdits: boolean, onReferenceNode: string, removeEdits: boolean, successfulEdits: boolean) -> None:
    """Synopsis:
---
---
 referenceEdit([applyFailedEdits=boolean], [changeEditTarget=[string, string]], [editCommand=string], [failedEdits=boolean], [onReferenceNode=string], [removeEdits=boolean], [successfulEdits=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

referenceEdit is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

---

EXAMPLE FOR -removeEdits
---

Assume:
main.ma contains a reference to mid.ma.
mid.ma contains a reference to bot.ma.

NOTE: The target reference must be unloaded for the
following commands to work.

Remove all the edits which apply to mid.ma.
This can be done by specifying either the reference
node or the reference file.
cmds.referenceEdit( 'midRN', removeEdits=True )
cmds.referenceEdit( 'mid.ma', removeEdits=True )

Remove all "setAttr" edits which apply to mid.ma.
This can be done by specifying either the reference
node or the reference file.
cmds.referenceEdit( 'midRN', editCommand='setAttr', removeEdits=True )
cmds.referenceEdit( 'mid.ma', editCommand='setAttr', removeEdits=True )

Remove all the "parent" edits which apply to mid:pSphere1.
cmds.referenceEdit( 'mid:pSphere1', editCommand='parent', removeEdits=True )

Remove all the "connectAttr" edits which apply to mid:pSphere1.translateX.
cmds.referenceEdit( 'mid:pSphere1.translateX', editCommand='connectAttr', removeEdits=True )

---
Remove the "connectAttr" edit having mid:pSphere1.translateX as a source and mid:pSphere2.translateX as a destination.
cmds.referenceEdit( ["|mid:pSphere1.translateX", "|mid:pSphere2.translateX"], failedEdits = True, successfulEdits = True, editCommand = 'connectAttr', removeEdits = True )

Remove all the edits which apply to bot.ma and are stored on midRN.
The referenceEdit command is only capable of removing edits which
are stored on a top level reference node. The only edits which
are stored on a top level reference node are those which were made
from the main scene. If the file mid.ma was previously opened and
modifications were made to bot.ma, those edits can only be removed
by opening mid.ma and issuing a referenceEdit command.
---

cmds.referenceEdit( 'mid:botRN', removeEdits=True )
cmds.referenceEdit( 'bot.ma', removeEdits=True )

---

EXAMPLE FOR -changeEditTarget
---

tempDir = cmds.internalVar(utd=True)

Create a reference containing pSphere1.
---

cmds.file( f=True, new=True )
cmds.polySphere( ch=1, r=1, sx=20, sy=20, ax=(0, 1, 0) )
newFileName = '%sref.ma' % tempDir
cmds.file( rename=newFileName )
cmds.file( f=True, s=True, type='mayaAscii')

Reference the file in and position pSphere1
---

cmds.file( f=True, new=True )
cmds.file( newFileName, r=True, ns='ref' )
cmds.select( 'ref:pSphere1', r=True )
cmds.move( 5, 5, 5 )
topFileName = '%stop.ma' % tempDir
cmds.file( rename=topFileName )
cmds.file( f=True, s=True, type='mayaAscii')

Later on its determined that pSphere1 is actually
BobMrozowski.
---

cmds.file( newFileName, f=True, o=True )
cmds.rename( 'pSphere1', 'BobMrozowski' )
cmds.file( f=True, s=True, type='mayaAscii')

Now go to open your main scene again...
---

cmds.file( topFileName, f=True, o=True )
... and notice that BobMrozowski is back at
the origin.
---

So remap all edits so that anything that used to
affect ref:pSphere1 now affects ref:BobMrozowski...
---

cmds.referenceEdit( 'refRN', changeEditTarget=('ref:pSphere1','ref:BobMrozowski') )
... and then force all previously failing edits affecting
refRN to be re-applied.
---

cmds.referenceEdit( 'refRN', applyFailedEdits=True )
BobMrozowski should now be back at 5 5 5.
---


---


Flags:
---


---
applyFailedEdits(afe): boolean
    properties: create
    Attempts to apply any unapplied edits. This flag is useful if previously
failing edits have been fixed using the -changeEditTarget flag. This flag
can only be used on loaded references. If the command target is a referenced
node, the associated reference is used instead.

---
changeEditTarget(cet): [string, string]
    properties: create
    Used to change a target of the specified edits.
This flag takes two parameters: the old target of the edits, and the
new target to change it to. The target can either be a node name ("node"), a
node and attribute name ("node.attr"), or just an attribute name (".attr").
If an edit currently affects the old target, it will be changed to affect
the new target.
Flag 'referenceQuery' should be used to determine the format of the edit targets.
As an example most edits store the long name of the attribute
(e.g. "translateX"), so when specifying the old target, a long name must also
be used. If the short name is specified (e.g. "tx"), chances are the edit
won't be retargeted.

---
failedEdits(fld): boolean
    properties: create
    This is a secondary flag used to indicate whether or not failed
edits should be acted on (e.g. queried, removed, etc...). A failed
edit is an edit which could not be successfully applied the last
time its reference was loaded.
An edit can fail for a variety of reasons (e.g. the referenced
node to which it applies was removed from the referenced file).
By default failed edits will be acted on.

---
removeEdits(r): boolean
    properties: create
    Remove edits which affect the specified unloaded commandTarget.

---
successfulEdits(scs): boolean
    properties: create
    This is a secondary flag used to indicate whether or not successful
edits should be acted on (e.g. queried, removed, etc...). A successful
edit is any edit which was successfully applied the last time its
reference was loaded. This flag will have no affect if the
commandTarget is loaded.
By default successful edits will not be acted on.

---
editCommand(ec): string
    properties: create, query, multiuse
    This is a secondary flag used to indicate which type of reference edits should
be considered by the command.
If this flag is not specified all edit types will be included.
This flag requires a string parameter. Valid values are: "addAttr",
"connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr",
"lock" and "unlock". In some contexts, this flag may be specified
more than once to specify multiple edit types to consider.

---
onReferenceNode(orn): string
    properties: create, query, multiuse
    This is a secondary flag used to indicate that only those edits which are stored
on the indicated reference node should be considered. This flag only supports
multiple uses when specified with the "exportEdits" command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/referenceEdit.html 
    """


def referenceQuery(child: boolean, dagPath: boolean, editAttrs: boolean, editCommand: string, editNodes: boolean, editStrings: boolean, failedEdits: boolean, filename: boolean, isExportEdits: boolean, isLoaded: boolean, isNodeReferenced: boolean, isPreviewOnly: boolean, liveEdits: boolean, namespace: boolean, nodes: boolean, onReferenceNode: string, parent: boolean, parentNamespace: boolean, referenceNode: boolean, shortName: boolean, showDagPath: boolean, showFullPath: boolean, showNamespace: boolean, successfulEdits: boolean, topReference: boolean, unresolvedName: boolean, withoutCopyNumber: boolean) -> list[string]:
    """Synopsis:
---
---
 referenceQuery([child=boolean], [dagPath=boolean], [editAttrs=boolean], [editCommand=string], [editNodes=boolean], [editStrings=boolean], [failedEdits=boolean], [filename=boolean], [isExportEdits=boolean], [isLoaded=boolean], [isNodeReferenced=boolean], [isPreviewOnly=boolean], [liveEdits=boolean], [namespace=boolean], [nodes=boolean], [onReferenceNode=string], [parent=boolean], [parentNamespace=boolean], [referenceNode=boolean], [shortName=boolean], [showDagPath=boolean], [showFullPath=boolean], [showNamespace=boolean], [successfulEdits=boolean], [topReference=boolean], [unresolvedName=boolean], [withoutCopyNumber=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

referenceQuery is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Build a sample scene:
main scene contains a reference to mid.ma.
mid.ma contains a reference to bot.ma.

Create bot.ma with a poly sphere.
---

cmds.polySphere()
cmds.file( rename='bot.ma' )
cmds.file( f=True, s=True, type='mayaAscii')

Create mid.ma with a poly cone.
Reference bot.ma into mid.ma and group
the sphere in bot.ma
---

cmds.file( f=True, new=True )
cmds.file( 'bot.ma', r=True,ns='bot' )
cmds.polyCone()
cmds.group( 'bot:pSphere1' )
cmds.file( rename='mid.ma' )
cmds.file( f=True, s=True, type='mayaAscii')

Create a poly plane.
Reference mid.ma into the main scene,
move the cone in mid.ma, and connect
the plane to the sphere in bot.ma.
---

cmds.file( f=True, new=True )
cmds.file( 'mid.ma', r=True, ns='mid' )
cmds.select( 'mid:pCone1', r=True )
cmds.move( 5, 5, 5, r=True )
cmds.polyPlane()
cmds.connectAttr( 'pPlane1.ty', 'mid:bot:polySphere1.radius' )

Now perform some queries:
---

cmds.referenceQuery( 'midRN',filename=True )
Result: C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/mid.ma
cmds.referenceQuery( 'mid:pCone1', filename=True, shortName=True )
Result: mid.ma
cmds.referenceQuery( 'mid:botRN', filename=True, parent=True )
Result: C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/mid.ma

cmds.referenceQuery( 'mid.ma', referenceNode=True )
Result: midRN
cmds.referenceQuery( 'C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/bot.ma', referenceNode=True)
Result: mid:botRN
cmds.referenceQuery( 'bot.ma', referenceNode=True, parent=True )
Result: midRN
cmds.referenceQuery( 'bot.ma', referenceNode=True, topReference=True )
Result: midRN

cmds.referenceQuery( 'mid:botRN',nodes=True )
Result:[u'mid:bot:pPlane1', u'mid:bot:pPlaneShape1', u'mid:bot:outputCloth1', u'mid:bot:nCloth1', u'mid:bot:nClothShape1', u'mid:bot:dynamicConstraint1', u'mid:bot:dynamicConstraintShape1', u'mid:bot:nurbsSphere1', u'mid:bot:nurbsSphereShape1', u'mid:bot:pSphere1', u'mid:bot:pSphereShape1', u'mid:bot:lightLinker1', u'mid:bot:layerManager', u'mid:bot:defaultLayer', u'mid:bot:renderLayerManager', u'mid:bot:defaultRenderLayer', u'mid:bot:polyPlane1', u'mid:bot:nucleus1', u'mid:bot:nComponent1', u'mid:bot:uiConfigurationScriptNode', u'mid:bot:sceneConfigurationScriptNode', u'mid:bot:nClothShape1Cache1Start', u'mid:bot:cacheBlend1', u'mid:bot:nClothShape1Cache2', u'mid:bot:nClothShape1Cache1End', u'mid:bot:makeNurbSphere1', u'mid:bot:polySphere1'] ---


cmds.referenceQuery( 'pPlane1', isNodeReferenced=True )
Result: 0
cmds.referenceQuery( 'mid:pCone1', isNodeReferenced=True )
Result: 1

cmds.referenceQuery( 'mid:botRN', parentNamespace=True )
Result: mid

cmds.referenceQuery( 'mid:bot:pSphere1', parentNamespace=True )
Result: mid

cmds.referenceQuery( 'C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/bot.ma', parentNamespace=True )
Result: mid

print cmds.referenceQuery( 'bot.ma', namespace=True )
Result: :mid:bot

print cmds.referenceQuery( 'mid:botRN', namespace=True )
Result: :mid:bot

print cmds.referenceQuery( 'bot.ma', namespace=True, shortName=True )
Result: bot

print cmds.referenceQuery( 'mid.ma', namespace=True )
Result: :mid

print cmds.referenceQuery( 'mid.ma', namespace=True, shortName=True )
Result: mid

---
Return:
---


    list[string]: For query execution.

Flags:
---


---
child(ch): boolean
    properties: create
    This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags
to indicate the the children of the target reference will be returned.
Returns a string array.

---
isExportEdits(iee): boolean
    properties: create
    Returns a boolean indicating whether the specified reference node or file
name is an edits file (created with the Export Edits feature)

---
isLoaded(il): boolean
    properties: create
    Returns a boolean indicating whether the specified reference node or
file name refers to a loaded or unloaded reference.

---
liveEdits(le): boolean
    properties: create
    Specifies that the edits should be returned based on the live edits
database. Only valid when used in conjunction with the editStrings flag.

---
dagPath(dp): boolean
    properties: create
    This flag modifies the '-n/-nodes' flag to indicate that the names of
any dag objects returned will include as much of the dag path as is
necessary to make the names unique. If this flag is not present, the
names returned will not include any dag paths.

---
editAttrs(ea): boolean
    properties: create
    Returns string array.
A main flag used to query the edits that have
been applied to the target. Only the names of
the attributes involved in the reference edit will be
returned. If an edit involves multiple attributes (e.g. "connectAttr"
edits) the nodes will be returned as separate,
consecutive entries in the string array. A valid target is either
a reference node, a reference file, or a referenced node.
If a referenced node is specified, only those edits which
affect that node will be returned. If a reference file
or reference node is specified any edit which affects
a node in that reference will be returned. If no target is
specified all edits are returned. This command can
be used on both loaded and unloaded references. By default
it will return all the edits, formatted as MEL commands,
which apply to the target.
This flag can be used in combination with the
'-ea/-editAttrs' flag to indicate that the names
of both the involved nodes and attributes will be
returned in the format 'node.attribute'.

---
editNodes(en): boolean
    properties: create
    Returns string array.
A main flag used to query the edits that have
been applied to the target. Only the names of
the nodes involved in the reference edit will be
returned. If an edit involves multiple nodes (e.g. "connectAttr"
edits) the nodes will be returned as separate,
consecutive entries in the string array. A valid target is either
a reference node, a reference file, or a referenced node.
If a referenced node is specified, only those edits which
affect that node will be returned. If a reference file
or reference node is specified any edit which affects
a node in that reference will be returned. If no target is
specified all edits are returned. This command can
be used on both loaded and unloaded references. By default
it will return all the edits, formatted as MEL commands,
which apply to the target.
This flag can be used in combination with the
'-ea/-editAttrs' flag to indicate that the names
of both the involved nodes and attributes will be
returned in the format 'node.attribute'.

---
editStrings(es): boolean
    properties: create
    Returns string array.
A main flag used to query the edits that have
been applied to the target. The edit will be returned
as a valid MEL command. A valid target is either
a reference node, a reference file, or a referenced node.
If a referenced node is specified, only those edits which
affect that node will be returned. If a reference file
or reference node is specified any edit which affects
a node in that reference will be returned. If no target is
specified all edits are returned. This command can be used
on both loaded and unloaded references. By default it will
return all the edits, formatted as MEL commands,
which apply to the target.
This flag cannot be used with either the '-en/-editNodes'
or '-ea/-editAttrs' flags.

---
failedEdits(fld): boolean
    properties: create
    This is a secondary flag used to indicate whether or not failed
edits should be acted on (e.g. queried, removed, etc...). A failed
edit is an edit which could not be successfully applied the last
time its reference was loaded.
An edit can fail for a variety of reasons (e.g. the referenced
node to which it applies was removed from the referenced file).
By default failed edits will not be acted on.

---
filename(f): boolean
    properties: create
    Returns string.
A main flag used to query the filename associated with the target reference.

---
isNodeReferenced(inr): boolean
    properties: create
    Returns boolean.
A main flag used to determine whether or not the target node comes
from a referenced file.
true if the target node comes from a referenced file, false if not.

---
isPreviewOnly(ipo): boolean
    properties: create
    Returns boolean.
This flag is used to determine whether or not the target reference node is
only a preview reference node.

---
namespace(ns): boolean
    properties: create
    Returns string.
This flag returns the full namespace path of the target reference, starting from the root namespace ":".
It can be combined with the shortName flag to return just the base name of the namespace.

---
nodes(n): boolean
    properties: create
    Returns string array.
A main flag used to query the contents of the target reference.

---
parent(p): boolean
    properties: create
    This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags
to indicate the the parent of the target reference will be returned.

---
parentNamespace(pns): boolean
    properties: create
    A main flag used to query and return the parent namespace of the target reference.

---
referenceNode(rfn): boolean
    properties: create
    Returns string.
A main flag used to query the reference node associated with the target
reference.

---
shortName(shn): boolean
    properties: create
    This flag modifies the '-f/-filename' and '-ns/-namespace' flags.
Used with the '-f/-filename' flag indicates that the file name returned will be the short name
(i.e. just a file name without any directory paths). If this flag is not present, the full name
and directory path will be returned.
Used with the '-ns/-namespace' flag indicates that the namespace returned will be the base name of the namespace.
(i.e. the base name of the full namespace path ":AAA:BBB:CCC" is "CCC"  )

---
showDagPath(sdp): boolean
    properties: create
    Shows/hides the full dag path for edits. If false only displays the
node-name of reference edits. Must be used with the -editNodes,
-editStrings or -editAttrs flag.

---
showFullPath(sfp): boolean
    properties: create
    Return the full path from the root namespace for reference edits.
Must be used with the -editNodes, -editStrings or -editAttrs flags.

---
showNamespace(sns): boolean
    properties: create
    Shows/hides the namespaces on nodes in the reference edits.
Must be used with the -editNodes, -editStrings or -editAttrs flag

---
successfulEdits(scs): boolean
    properties: create
    This is a secondary flag used to indicate whether or not successful
edits should be acted on (e.g. queried, removed, etc...). A successful
edit is any edit which was successfully applied the last time its
reference was loaded.
By default successful edits will be acted on.

---
topReference(tr): boolean
    properties: create
    This flag modifies the '-rfn/-referenceNode' flag
to indicate the top level ancestral reference of the target reference will be
returned.

---
unresolvedName(un): boolean
    properties: create
    This flag modifies the '-f/-filename' flag to indicate that the file name
returned will be unresolved (i.e. it will be the path originally
specified when the file was loaded into Maya; this path may
contain environment variables and may not exist on disk). If this
flag is not present, the resolved name will     be returned.

---
withoutCopyNumber(wcn): boolean
    properties: create
    This flag modifies the '-f/-filename' flag to indicate that the file name
returned will not have a copy number (e.g. '{1}') appended to the end. If this
flag is not present, the file name returned may have a copy number
appended to the end.

---
editCommand(ec): string
    properties: create, query, multiuse
    This is a secondary flag used to indicate which type of reference edits should
be considered by the command.
If this flag is not specified all edit types will be included.
This flag requires a string parameter. Valid values are: "addAttr",
"connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr",
"lock" and "unlock". In some contexts, this flag may be specified
more than once to specify multiple edit types to consider.

---
onReferenceNode(orn): string
    properties: create, query, multiuse
    This is a secondary flag used to indicate that only those edits which are stored
on the indicated reference node should be considered. This flag only supports
multiple uses when specified with the "exportEdits" command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/referenceQuery.html 
    """


def refineSubdivSelectionList() -> boolean:
    """Synopsis:
---
---
 refineSubdivSelectionList()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

refineSubdivSelectionList is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

after selecting components of a subdivision surface
cmds.refineSubdivSelectionList()

---
Return:
---


    boolean: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/refineSubdivSelectionList.html 
    """


def refresh(currentView: boolean, fileExtension: string, filename: string, force: boolean, suspend: boolean) -> None:
    """Synopsis:
---
---
 refresh([currentView=boolean], [fileExtension=string], [filename=string], [force=boolean], [suspend=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

refresh is undoable, NOT queryable, and NOT editable.
If the -cv flag is specified, then only the current active view
is redrawn.





Example:
---
import maya.cmds as cmds

cmds.refresh()


The refresh command can also be used to take a snapshot of the current scene view and
save it as an image file. See example below.

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


Flags:
---


---
currentView(cv): boolean
    properties: create
    Redraw only the current view (default redraws all views).

---
fileExtension(fe): string
    properties: create
    Specify the type of file to save using the filename flag.

---
filename(fn): string
    properties: create
    Specify the name of a file in which to save a snapshot of the
viewports, or just the current one if the currentView flag is set.

---
force(f): boolean
    properties: create
    Force the refresh regardless of the state of the model.

---
suspend(su): boolean
    properties: create
    Suspends or resumes Maya's handling of refresh events. Specify "on" to
suspend refreshing, and "off" to resume refreshing. Note that
resuming refresh does not itself cause a refresh -- the next natural refresh
event in Maya after "refresh -suspend off" is issued will cause the refresh
to occur. Use this flag with caution: although it provides opportunities
to enhance performance, much of Maya's dependency graph evaluation in
interactive mode is refresh driven, thus use of this flag may lead to
slight solve differences when you have a complex dependency graph with
interrelations.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/refresh.html 
    """


def refreshEditorTemplates() -> None:
    """Synopsis:
---
---
 refreshEditorTemplates()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

refreshEditorTemplates is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

The following command will cause the currently
selected AE tab and all copied AE tab windows
to be refreshed.
---

cmds.refreshEditorTemplates

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/refreshEditorTemplates.html 
    """


def regionSelectKeyCtx(bottomManip: float, exists: boolean, history: boolean, image1: string, image2: string, image3: string, leftManip: float, name: string, rightManip: float, topManip: float) -> float:
    """Synopsis:
---
---
 regionSelectKeyCtx(
contextName
    , [bottomManip=float], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [leftManip=float], [name=string], [rightManip=float], [topManip=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

regionSelectKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a manipulator style scale key context for the graph editor
---

cmds.regionSelectKeyCtx( 'regionSelectKeyContext' )

---
Return:
---


    float: Manip values, when queried

Flags:
---


---
bottomManip(bot): float
    properties: query
    Get a point located inside the bottom manipulator of the region box, in screen space.

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
leftManip(lft): float
    properties: query
    Get a point located inside the left manipulator of the region box, in screen space.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
rightManip(rgt): float
    properties: query
    Get a point located inside the right manipulator of the region box, in screen space.

---
topManip(top): float
    properties: query
    Get a point located inside the top manipulator of the region box, in screen space.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/regionSelectKeyCtx.html 
    """


def relationship(b: boolean, relationshipData: string) -> None:
    """Synopsis:
---
---
 relationship([b=boolean], [relationshipData=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

relationship is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


cmds.relationship('ignore', 'lightLinker1', 'pCube1', 'pointLight1')

---


Flags:
---


---
b(b): boolean
    properties: create, query, edit
    Break the specified relationship instead of creating it

---
relationshipData(rd): string
    properties: create, query, edit, multiuse
    Provide relationship data to be used when creating the relationship.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/relationship.html 
    """


def reloadImage() -> boolean:
    """Synopsis:
---
---
 reloadImage(
string string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

reloadImage is undoable, NOT queryable, and NOT editable.
The first string argument is the file name of the .xpm file. The
second string argument is the name of a control using the specified
pixmap.




Example:
---
import maya.cmds as cmds

cmds.reloadImage( 'image.xpm', 'iconTextButtonName' )
cmds.reloadImage( 'image', 'shelfButtonName' )
cmds.reloadImage( '~/bitmaps/maya/image.xpm', 'toolButtonName' )

---
Return:
---


    boolean: True if image is successfully loaded, false otherwise.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/reloadImage.html 
    """


def rememberCtxSettings() -> None:
    """Synopsis:
---
---
 rememberCtxSettings(
[string]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rememberCtxSettings is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.rememberCtxSettings('Move')

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rememberCtxSettings.html 
    """


def removeJoint() -> None:
    """Synopsis:
---
---
 removeJoint(
[object]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

removeJoint is undoable, NOT queryable, and NOT editable.
The given (or selected) joint should not be the root joint of the skeleton,
and not have skin attached. The command works on the given (or selected)
joint. No options or flags are necessary.




Example:
---
import maya.cmds as cmds

joint5 will be removed. Child joints of joint5 will be reparented under
joint5's parent joint.
cmds.removeJoint( 'joint5' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/removeJoint.html 
    """


def removeMultiInstance(allChildren: boolean, b: boolean) -> boolean:
    """Synopsis:
---
---
 removeMultiInstance(
attribute
    , [allChildren=boolean], [b=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

removeMultiInstance is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.createNode('choice',n='choice')
cmds.setAttr('choice.input[0]',2.0)
cmds.setAttr('choice.input[4]',4.0)
cmds.connectAttr('choice.input[8]','choice.input[100]')

This will remove the element with index 4 from the input of
the choice node as long as there are no incoming or outgoing
connections to the attribute.
---

cmds.removeMultiInstance( 'choice.input[4]' )

This will remove the element with index 100 from the input of
the choice node, breaking any existing connections first.
---

cmds.removeMultiInstance( 'choice.input[100]', b=True )

---
Return:
---


    boolean: (true if the instance was removed, false if something went wrong,
like the attribute is connected but -b true was not specified)

Flags:
---


---
allChildren(all): boolean
    properties: create
    If the argument is true, remove all children of the multi parent.

---
b(b): boolean
    properties: create
    If the argument is true, all connections to the attribute
will be broken before the element is removed. If false, then
the command will fail if the element is connected.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/removeMultiInstance.html 
    """


def rename(ignoreShape: boolean, uuid: boolean) -> string:
    """Synopsis:
---
---
 rename(
[object] string
    , [ignoreShape=boolean], [uuid=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rename is undoable, NOT queryable, and NOT editable.
When a transform is renamed then any shape nodes beneath the
transform that have the same prefix as the old transform name
are renamed. For example, "rename nurbsSphere1 ball" would
rename "nurbsSphere1|nurbsSphereShape1" to "ball|ballShape".

If the new name ends in a single '#' then the rename command
will replace the  trailing '#' with a number that ensures
the new name is unique.




Example:
---
import maya.cmds as cmds

create two namespaces under the root namespace and create
a sphere under the root namespace and a sphere under one
of the new namespaces.
cmds.namespace( set=':' )
cmds.sphere( n='sphere1' )
cmds.namespace( add='nsA' )
cmds.namespace( add='nsB' )
cmds.namespace( set='nsA' )
cmds.sphere( n='sphere2' )
cmds.namespace( set=':' )
change name of sphere1
cmds.rename('sphere1', 'spinning_ball')

change name of spinning_ball back to sphere1
cmds.select( 'spinning_ball', r=True )
cmds.rename( 'sphere1' )

move sphere2 to namespace nsB
cmds.rename( 'nsA:sphere2', 'nsB:sphere2' )
Result: nsB:sphere2 ---


move sphere2 back to namespace nsA when not in the root namespace
Note the ":" appearing in front of the new name to indicate
we want to move the object to namespace nsA under the root namespace.
cmds.namespace( set='nsB' )
cmds.rename( 'nsB:sphere2', ':nsA:sphere2' )
Result: nsA:sphere2 ---


Let's try this without the leading ":" in the new name.
Since we are namespace nsA, in affect, what we are trying to do
is rename :nsB:sphere2 to :nsA:nsB:sphere3. Since there isn't a
nsB namespace under the namespace nsA, the namespace specification
on new name is ignored and a warning is issued.
cmds.namespace( set=':nsA' )
cmds.rename( 'nsA:sphere2', 'nsB:sphere3' )
Warning: Removing invalid characters from name. ---

Result: nsA:sphere3 ---


rename an object when not in the root namespace
and move the object to current namespace
cmds.namespace( set=':nsB' )
cmds.rename( 'nsA:sphere3', 'sphere4' )
Result: nsB:sphere4 ---


rename an object with an absolute name to move it into a new namespace.
The namespace does not exist so will be created.
cmds.namespace( set=':nsB' )
cmds.rename( 'nsA:sphere3', ':nsC:sphere4' )
Result: nsC:sphere4 ---


---
Return:
---


    string: The new name. When undone returns original name.

Flags:
---


---
ignoreShape(ignoreShape): boolean
    properties: create
    Indicates that renaming of shape nodes below
transform nodes should be prevented.

---
uuid(uid): boolean
    properties: create
    Indicates that the new name is actually a UUID,
and that the command should change the node's UUID.
(In which case its name remains unchanged.)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rename.html 
    """


def renameAttr() -> string:
    """Synopsis:
---
---
 renameAttr()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renameAttr is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.sphere( n='sph' )
cmds.addAttr( sn='ms', ln='mass', dv=1.0, min=0.001, max=10000 )
Rename the long and short names separately
cmds.renameAttr( 'sph.mass', 'length' )
cmds.renameAttr( 'sph.ms', 'ln' )

---
Return:
---


    string: The new name. When undone returns the original name.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renameAttr.html 
    """


def renameUI() -> string:
    """Synopsis:
---
---
 renameUI(
string string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renameUI is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

   Create a window with a single button.
---

window = cmds.window()
cmds.columnLayout()
cmds.button( 'exampleButton', label='Example' )
cmds.showWindow( window )

   Edit the button label.
---

cmds.button( 'exampleButton', edit=True, label='New Label' )

   Rename the button.
---

cmds.renameUI( 'exampleButton', 'newButton' )

   Query the button label using the new object name.
---

cmds.button( 'newButton', query=True, label=True )

---
Return:
---


    string: The new name, or the old name if re-naming fails.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renameUI.html 
    """


def render(abortMissingTexture: boolean, batch: boolean, keepPreImage: boolean, layer: string, nglowpass: boolean, nshadows: boolean, replace: boolean, xresolution: int, yresolution: int) -> string:
    """Synopsis:
---
---
 render(
[camera]
    , [abortMissingTexture=boolean], [batch=boolean], [keepPreImage=boolean], [layer=string], [nglowpass=boolean], [nshadows=boolean], [replace=boolean], [xresolution=int], [yresolution=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

render is NOT undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.render()

cam = cmds.camera()
cmds.render( cam[0], x=768, y=576 )

---
Return:
---


    string: The name of the rendered image.

Flags:
---


---
abortMissingTexture(amt): boolean
    properties: create
    Abort renderer when encountered missing texture. Only
available when -batch is set

---
batch(b): boolean
    properties: create
    Run in batch mode. Compute the images for all renderable
cameras. This is the mel equivalent of running maya in batch
mode with the -render flag set. All other flags are ignored
when -batch is used.

---
keepPreImage(kpi): boolean
    properties: create
    Keep the renderings prior to post-process around. Only
available when -batch is set

---
layer(l): string
    properties: create
    Render the specified render layer.
Only this render layer will be rendered,
regardless of the renderable attribute value of the render layer.
The layer name will be appended to the output image file name.
The specified render layer becomes the current render layer before rendering,
and remains as current render layer after the rendering.

---
nglowpass(ngl): boolean
    properties: create
    Overwrite glow pass capabilities (can turn off glow pass globally
by setting this value to false)

---
nshadows(nsh): boolean
    properties: create
    Shadowing capabilities (can turn off shadow globally
by setting this value to false)

---
replace(rep): boolean
    properties: create
    Replace the rendered image if it already exists. Only
available when -batch is set

---
xresolution(x): int
    properties: create
    Overwrite x resolution

---
yresolution(y): int
    properties: create
    Overwrite y resolution

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/render.html 
    """


def renderGlobalsNode(name: string, parent: string, renderQuality: string, renderResolution: string, shared: boolean, skipSelect: boolean) -> string:
    """Synopsis:
---
---
 renderGlobalsNode(
string
    , [name=string], [parent=string], [renderQuality=string], [renderResolution=string], [shared=boolean], [skipSelect=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderGlobalsNode is undoable, NOT queryable, and NOT editable.
The renderGlobalsNode creates a render globals node and registers it
with the model. The createNode command will not register nodes of this
type correctly.




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

cmds.renderGlobalsNode('bob')

this one will use defaults for resolution and quality
cmds.renderGlobalsNode('bob', name='bob' )

cmds.renderGlobalsNode('bob', rq='myTestQuality1', name='abekasTestGlobals' )

---
Return:
---


    string: The name of the new node.
    string: The name of the render globals node

Flags:
---


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
renderQuality(rq): string
    properties: create
    Set the quality to be the renderQuality node with the given name.

---
renderResolution(rr): string
    properties: create
    Set the resolution to be the resolution node with the given name.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderGlobalsNode.html 
    """


def renderInfo(castShadows: boolean, chordHeight: float, chordHeightRatio: float, doubleSided: boolean, edgeSwap: boolean, minScreen: float, name: string, opposite: boolean, smoothShading: boolean, unum: int, useChordHeight: boolean, useChordHeightRatio: boolean, useDefaultLights: boolean, useMinScreen: boolean, utype: int, vnum: int, vtype: int) -> None:
    """Synopsis:
---
---
 renderInfo([castShadows=boolean], [chordHeight=float], [chordHeightRatio=float], [doubleSided=boolean], [edgeSwap=boolean], [minScreen=float], [name=string], [opposite=boolean], [smoothShading=boolean], [unum=int], [useChordHeight=boolean], [useChordHeightRatio=boolean], [useDefaultLights=boolean], [useMinScreen=boolean], [utype=int], [vnum=int], [vtype=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderInfo is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.renderInfo( doubleSided=False, opposite=True )

---


Flags:
---


---
castShadows(cs): boolean
    properties: create
    Determines if object casts shadow or not.

---
chordHeight(ch): float
    properties: create
    Tessellation subdivision criteria.

---
chordHeightRatio(chr): float
    properties: create
    Tessellation subdivision criteria.

---
doubleSided(ds): boolean
    properties: create
    Determines if object double or single sided.

---
edgeSwap(es): boolean
    properties: create
    Tessellation subdivision criteria.

---
minScreen(ms): float
    properties: create
    Tessellation subdivision criteria.

---
name(n): string
    properties: create
    Namespace to use.

---
opposite(o): boolean
    properties: create
    Determines if the normals of the object is to be reversed.

---
smoothShading(ss): boolean
    properties: create
    Determines if smooth shaded, or flat shaded - applies only to polysets.

---
unum(un): int
    properties: create
    Tessellation subdivision criteria.

---
useChordHeight(uch): boolean
    properties: create
    Tessellation subdivision criteria.

---
useChordHeightRatio(ucr): boolean
    properties: create
    Tessellation subdivision criteria.

---
useDefaultLights(udl): boolean
    properties: create
    Obsolete flag.

---
useMinScreen(ums): boolean
    properties: create
    Tessellation subdivision criteria.

---
utype(ut): int
    properties: create
    Tessellation subdivision criteria.

---
vnum(vn): int
    properties: create
    Tessellation subdivision criteria.

---
vtype(vt): int
    properties: create
    Tessellation subdivision criteria.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderInfo.html 
    """


def renderLayerPostProcess(keepImages: boolean, sceneName: string) -> None:
    """Synopsis:
---
---
 renderLayerPostProcess([keepImages=boolean], [sceneName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderLayerPostProcess is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.renderLayerPostProcess()

---


Flags:
---


---
keepImages(ki): boolean
    properties: create, query
    When set to on, the original iff images are kept after the conversion to PSD.
Default is to remove them.

---
sceneName(sn): string
    properties: create, query
    Specifies the scene name for interactive batch rendering.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderLayerPostProcess.html 
    """


def renderManip(camera: tuple[boolean, boolean, boolean, boolean, boolean], light: tuple[boolean, boolean, boolean], spotLight: tuple[boolean, boolean, boolean, boolean, boolean, boolean, boolean], state: boolean) -> None:
    """Synopsis:
---
---
 renderManip(
object
    , [camera=[boolean, boolean, boolean, boolean, boolean]], [light=[boolean, boolean, boolean]], [spotLight=[boolean, boolean, boolean, boolean, boolean, boolean, boolean]], [state=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderManip is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.camera()

cmds.renderManip( 'cameraShape1' )

cmds.renderManip( 'cameraShape1', e=True, st=True )

cmds.renderManip( 'cameraShape1', q=True, st=True )

---


Flags:
---


---
camera(cam): [boolean, boolean, boolean, boolean, boolean]
    properties: query, edit
    Query or edit the visiblity status of the component camera
manipulators. The order of components are: cycling index,
center of interest, pivot, clipping planes, and unused.

---
light(lt): [boolean, boolean, boolean]
    properties: query, edit
    Query or edit the visiblity status of the component light
manipulators. The order of components are: cycling index,
center of interest, and pivot.

---
spotLight(slt): [boolean, boolean, boolean, boolean, boolean, boolean, boolean]
    properties: query, edit
    Query or edit the visiblity status of the component spot light
manipulators. The order of components are: cycling index,
center of interest, pivot, cone angle, penumbra, look through
barn doors, and decay regions.

---
state(st): boolean
    properties: query, edit
    Query or edit the state of manipulators on an camera, ambient
light, directional light, point light, or spot light. This
flag's default value is on.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderManip.html 
    """


def renderPartition() -> string:
    """Synopsis:
---
---
 renderPartition(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderPartition is undoable, queryable, and NOT editable.q



Example:
---
import maya.cmds as cmds

Query the current render partition
cmds.renderPartition( q=True )

Set the current render partition to "foofoo"
cmds.renderPartition( 'foofoo' )

---
Return:
---


    string: The render partition

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderPartition.html 
    """


def renderPassRegistry(channels: int, isPassSupported: boolean, passID: string, passName: boolean, renderer: string, supportedChannelCounts: boolean, supportedDataTypes: boolean, supportedPassSemantics: boolean, supportedRenderPassNames: boolean, supportedRenderPasses: boolean) -> list[string]:
    """Synopsis:
---
---
 renderPassRegistry([channels=int], [isPassSupported=boolean], [passID=string], [passName=boolean], [renderer=string], [supportedChannelCounts=boolean], [supportedDataTypes=boolean], [supportedPassSemantics=boolean], [supportedRenderPassNames=boolean], [supportedRenderPasses=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderPassRegistry is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


Get supported channel counts supported by your renderer and the passID "DIFF".

cmds.renderPassRegistry(passID='DIFF',renderer='yourRenderer', supportedChannelCounts=True)
---

Get supported data types supported by your renderer, the passID "DIFF" and the channels "3".

cmds.renderPassRegistry(passID='DIFF', renderer='yourRenderer', channels=3, supportedDataTypes=True)

---
Return:
---


    list[string]: Command result

Flags:
---


---
channels(ch): int
    properties: create
    Specify the number of channels for query.

---
isPassSupported(ips): boolean
    properties: create
    Return whether the pass is supported by the renderer
This flag must be specified by the flag -passID firstly. The renderer whose default
value is the current renderer is specified by the flag renderer.

---
passID(pi): string
    properties: create
    Specify the render pass ID for query.

---
passName(pn): boolean
    properties: create
    Get the pass name for the passID.
This flag must be specified by the flag -passID firstly.

---
renderer(r): string
    properties: create
    Specify a renderer when using this command.
By default the current renderer is specified.

---
supportedChannelCounts(scc): boolean
    properties: create
    List channel counts supported by the renderer(specified by the flag -renderer) and
the specified pass ID.
This flag must be specified by the flag -passID firstly.

---
supportedDataTypes(sdt): boolean
    properties: create
    List frame buffer types supported by the renderer(specified by the flag -renderer),
the specified passID and channels.
This flag must be specified by the flag -passID and -channels firstly.

---
supportedPassSemantics(ps): boolean
    properties: create
    List pass semantics supported by the specified passID.
This flag must be specified by the flag -passId firstly.

---
supportedRenderPassNames(spn): boolean
    properties: create
    List render pass names supported by the renderer(specified by the flag -renderer).

---
supportedRenderPasses(srp): boolean
    properties: create
    List render passes supported by the renderer(specified by the flag -renderer).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderPassRegistry.html 
    """


def renderQualityNode(name: string, parent: string, shared: boolean, skipSelect: boolean) -> string:
    """Synopsis:
---
---
 renderQualityNode(
string
    , [name=string], [parent=string], [shared=boolean], [skipSelect=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderQualityNode is undoable, NOT queryable, and NOT editable.
The renderQualityNode creates a render quality node
and registers it with the model.  The createNode
command will not register nodes of this type correctly.




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

cmds.renderQualityNode()
cmds.renderQualityNode( name='loResTestQuality' )

---
Return:
---


    string: The name of the new node.
    string: The Name of the render quality node

Flags:
---


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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderQualityNode.html 
    """


def renderSettings(camera: string, customTokenString: string, firstImageName: boolean, fullPath: boolean, fullPathTemp: boolean, genericFrameImageName: string, imageGenericName: boolean, lastImageName: boolean, layer: string, leaveUnmatchedTokens: boolean) -> list[string]:
    """Synopsis:
---
---
 renderSettings([camera=string], [customTokenString=string], [firstImageName=boolean], [fullPath=boolean], [fullPathTemp=boolean], [genericFrameImageName=string], [imageGenericName=boolean], [lastImageName=boolean], [layer=string], [leaveUnmatchedTokens=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderSettings is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Get the name of the first and last image for the current layer
fl = cmds.renderSettings(firstImageName=True, lastImageName=True)

print( 'First image is '+fl[0] )

This is the empty string if the scene is not set for animation
if fl[1] == '':
    print('Not rendering animation');
else:
    print( 'Last image is '+fl[1] )

---
Return:
---


    list[string]: Command result

Flags:
---


---
camera(cam): string
    properties: create
    Specify a camera that you want to replace the current renderable camera

---
customTokenString(cts): string
    properties: create
    Specify a custom key-value string to use to replace custom tokens in
the file name. Use with firstImageName or lastImageName. Basic tokens
(Scene, Layer, RenderLayer, Camera, Version, Extension) will be
automatically expanded. Any other tokens must be specified here to
be expanded.
The format of the string is a space separated list of tokens-value pairs.
For example, if the file name string is "myFile_<myToken>_<myOtherToken>_v"
then the argument to this flag string should take the form
"myToken=myTokenValue myOtherToken=myOtherTokenValue".

---
firstImageName(fin): boolean
    properties: create
    Returns the first image name

---
fullPath(fp): boolean
    properties: create
    Returns the full path for the image using the current project. Use with
firstImageName, lastImageName, or genericFrameImageName.

---
fullPathTemp(fpt): boolean
    properties: create
    Returns the full path for the preview render of the image using the current
project. Use with firstImageName, lastImageName, or genericFrameImageName.

---
genericFrameImageName(gin): string
    properties: create
    Returns the generic frame image name with the custom specified frame
index token

---
imageGenericName(ign): boolean
    properties: create
    Returns the image generic name

---
lastImageName(lin): boolean
    properties: create
    Returns the last image name

---
layer(lyr): string
    properties: create
    Specify a render layer name that you want to replace the current render layer

---
leaveUnmatchedTokens(lut): boolean
    properties: create
    Do not remove unmatched tokens from the name string. Use with
firstImageName or lastImageName.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderSettings.html 
    """


def renderThumbnailUpdate(forceUpdate: string) -> None:
    """Synopsis:
---
---
 renderThumbnailUpdate(
boolean
    , [forceUpdate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderThumbnailUpdate is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Turns on thumbnail updates.
cmds.renderThumbnailUpdate(True)

Turns off thumbnail updates.
cmds.renderThumbnailUpdate(False)

Force update of a thumbnail
cmds.renderThumbnailUpdate(fu = "lambert1")

---


Flags:
---


---
forceUpdate(fu): string
    properties: create
    Force the thumbnail to update.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderThumbnailUpdate.html 
    """


def renderWindowEditor(autoResize: boolean, blendMode: int, caption: string, changeCommand: tuple[string, string, string, string], clear: tuple[int, int, float, float, float], cmEnabled: boolean, colorManage: boolean, compDisplay: int, compImageFile: string, control: boolean, currentCamera: string, currentCameraRig: string, defineTemplate: string, displayImage: int, displayImageViewCount: int, displayStyle: string, docTag: string, doubleBuffer: boolean, drawAxis: boolean, editorName: boolean, exists: boolean, exposure: float, filter: string, forceMainConnection: string, frameImage: boolean, frameRegion: boolean, gamma: float, highlightConnection: string, loadImage: string, lockMainConnection: boolean, mainListConnection: string, marquee: tuple[float, float, float, float], nbImages: boolean, nextViewImage: boolean, outputColorManage: boolean, panel: string, parent: string, pcaption: string, realSize: boolean, refresh: boolean, removeAllImages: boolean, removeImage: boolean, resetRegion: boolean, resetViewImage: boolean, saveImage: boolean, scaleBlue: float, scaleGreen: float, scaleRed: float, selectionConnection: string, showRegion: tuple[int, int], singleBuffer: boolean, snapshot: tuple[string, int, int], snapshotMode: boolean, stateString: boolean, stereo: int, stereoImageOrientation: tuple[string, string], stereoMode: string, toggle: boolean, unParent: boolean, unlockMainConnection: boolean, updateMainConnection: boolean, useTemplate: string, viewImageCount: int, viewTransformName: string, writeImage: string) -> string:
    """Synopsis:
---
---
 renderWindowEditor(
editorName
    , [autoResize=boolean], [blendMode=int], [caption=string], [changeCommand=[string, string, string, string]], [clear=[int, int, float, float, float]], [cmEnabled=boolean], [colorManage=boolean], [compDisplay=int], [compImageFile=string], [control=boolean], [currentCamera=string], [currentCameraRig=string], [defineTemplate=string], [displayImage=int], [displayImageViewCount=int], [displayStyle=string], [docTag=string], [doubleBuffer=boolean], [drawAxis=boolean], [editorName=boolean], [exists=boolean], [exposure=float], [filter=string], [forceMainConnection=string], [frameImage=boolean], [frameRegion=boolean], [gamma=float], [highlightConnection=string], [loadImage=string], [lockMainConnection=boolean], [mainListConnection=string], [marquee=[float, float, float, float]], [nbImages=boolean], [nextViewImage=boolean], [outputColorManage=boolean], [panel=string], [parent=string], [pcaption=string], [realSize=boolean], [refresh=boolean], [removeAllImages=boolean], [removeImage=boolean], [resetRegion=boolean], [resetViewImage=boolean], [saveImage=boolean], [scaleBlue=float], [scaleGreen=float], [scaleRed=float], [selectionConnection=string], [showRegion=[int, int]], [singleBuffer=boolean], [snapshot=[string, int, int]], [snapshotMode=boolean], [stateString=boolean], [stereo=int], [stereoImageOrientation=[string, string]], [stereoMode=string], [toggle=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string], [viewImageCount=int], [viewTransformName=string], [writeImage=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderWindowEditor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

There can only be one renderWindowEditor.
Check if it already exists or create it otherwise.
---

editor = cmds.renderWindowEditor(q=True, editorName=True )
if( len(editor) == 0  ):
        editor = cmds.renderWindowEditor( "renderView" )

cmds.renderWindowEditor( editor, e=True, mq=(0.7, 0.3, 0.3, 0.5) )

cmds.renderWindowEditor( editor, e=True, ar=True )

cmds.renderWindowEditor( editor, e=True, snapshot=('persp', 256, 256) )

cmds.renderWindowEditor( editor, e=True, crc='persp' )
cmds.renderWindowEditor( editor, q=True, crc=True )

---
Return:
---


    string: The name of the editor

Flags:
---


---
autoResize(ar): boolean
    properties: create, query, edit
    Lets the render view editor automatically resize the viewport or not.

---
blendMode(blm): int
    properties: create, query, edit
    Sets the blend mode for the render view.
New image sent to the render view will be blended
with the previous image in the render view,
and the composited image will appear.

---
caption(cap): string
    properties: create, query, edit
    Sets the caption which appears at the bottom of the render view.

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
clear(cl): [int, int, float, float, float]
    properties: create, query, edit
    Clear the image with the given color at the given resolution.
Arguments are respectively: width height red green blue.

---
cmEnabled(cme): boolean
    properties: query, edit
    Turn on or off applying color management in the View.  If set, the color
management configuration set in the current view is used.

---
colorManage(com): boolean
    properties: edit
    When used with the writeImage flag, causes the written image to
be color-managed using the settings from the view color manager
attached to the view.

---
compDisplay(cd): int
    properties: create, query, edit
    0 : disable compositing.
1 : displays the composited image immediately.
For example, when foreground layer tile is sent to the render
view window,
the composited tile is displayed in the render view window,
and the original foreground layer tile is not displayed.
2 : display the un-composited image, and keep the
composited image for the future command.
For example, when foreground layer tile is sent to the
render view window,
the original foreground layer tile is not displayed,
and the composited tile is stored in a buffer.
3 : show the current composited image.
If there is a composited image in the buffer, display it.

---
compImageFile(cif): string
    properties: create, query, edit
    Open the given image file
and blend with the buffer
as if the image was just rendered.

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
currentCamera(crc): string
    properties: create, query, edit
    Get or set the current camera. (used when redoing last render)

---
currentCameraRig(crg): string
    properties: create, query, edit
    Get or set the current camera rig name. If a camera rig is
specified, it will be used when redoing the last render as
opposed to the currentCamera value, as the currentCamera
value will hold the child camera last used for rendering
the camera rig.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
displayImage(di): int
    properties: query, edit
    Set a particular image in the Editor Image Stack as the current Editor Image.
Images are added to the Editor Image Stack using the "si/saveImage" flag.

---
displayImageViewCount(dvc): int
    properties: query
    Query the number of views stored for a given image in the Editor Image Stack. This is not the same
as querying using "viewImageCount" which returns the number of views for the current rendered image.

---
displayStyle(dst): string
    properties: create, query, edit
    Set the mode to display the image. Valid values are:

"color" to display the basic RGB image
"mask" to display the mask channel
"lum" to display the luminance of the image

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
editorName(en): boolean
    properties: query
    Returns the name of the editor, or an empty string if the editor has not been created yet.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
exposure(exp): float
    properties: query, edit
    The exposure value used by the color management of the current view.

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
frameImage(fi): boolean
    properties: create, query, edit
    Frames the image inside the window.

---
frameRegion(fr): boolean
    properties: create, query, edit
    Frames the region inside the window.

---
gamma(ga): float
    properties: query, edit
    The gamma value used by the color management of the current view.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

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
marquee(mq): [float, float, float, float]
    properties: create, query, edit
    The arguments define the four corners of a rectangle: top left bottom right.
The rectangle defines a marquee for the render computation.

---
nbImages(nim): boolean
    properties: query
    returns the number of images

---
nextViewImage(nvi): boolean
    properties: create, edit
    The render editor has the capability to render multiple cameras within a
single view. This is different from image binning where an image is saved. Multiple image views
are useful for comparing two different camera renders side-by-side. The nextViewImage flag tells
the editor that it should prepare its internal image storage mechanism to store to the next
view location.

---
outputColorManage(ocm): boolean
    properties: edit
    When used with the writeImage flag, causes the written image to
be color-managed using the outpute color space in the color preferences
attached to the view.

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
pcaption(pca): string
    properties: create, query, edit
    Get or set the permanent caption which appears under
the image that is currently showing in the render editor.

---
realSize(rs): boolean
    properties: create, query, edit
    Display the image with a one to one pixel match.

---
refresh(ref): boolean
    properties: edit
    requests a refresh of the current Editor Image.

---
removeAllImages(ra): boolean
    properties: edit
    remove all the Editor Images from the Editor Image Stack

---
removeImage(ri): boolean
    properties: edit
    remove the current Editor Image from the Editor Image Stack

---
resetRegion(rr): boolean
    properties: create, query, edit
    Forces a reset of any marquee/region.

---
resetViewImage(rvi): boolean
    properties: create, edit
    The render editor has the capability to render multiple cameras within a
single view. This is different from image binning where an image is saved. Multiple image views
are useful for comparing two different camera renders side-by-side. The resetViewImage flag tells
the editor that it should reset its internal image storage mechanism to the first image.
This would happen at the very start of a render view render.

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
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
showRegion(srg): [int, int]
    properties: create, query, edit
    Shows the current region at the given resolution. The two parameters
define the width and height.

---
singleBuffer(sbf): boolean
    properties: create, query, edit
    Set the display in single buffer mode

---
snapshot(snp): [string, int, int]
    properties: create, query, edit
    Makes a copy of the camera of the model editor at the
given size.
First argument is the editor name, second is the width, third is the height.

---
snapshotMode(snm): boolean
    properties: create, query, edit
    Get or set the window's snapshot mode.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
stereo(s): int
    properties: create, query, edit
    Puts the editor into stereo image mode.  The effective resolution of the
output image is twice the size of the horizontal size. The orientation of the
images can be set using the stereoOrientation flag.

---
stereoImageOrientation(sio): [string, string]
    properties: create, query, edit
    Specifies the orientation of stereo camera renders.  The first argument specifies the orientation
value for the firstleft image and the second argument specifies the orientation value for the right
image. The orientation values are 'normal', the image appears as seen throught he camera, or
'mirrored', the image is mirrored horizontally.

---
stereoMode(sm): string
    properties: create, query, edit
    Specifies how the image is displayed in the view.  By default the stereo is rendered with a
side by side image.  The rendered image is a single image that is twice the size of a normal image,
'both'. Users can also choose to display as 'redcyan', 'redcyanlum', 'leftonly', 'rightonly', or 'stereo'.

both - displays both the left and right
redcyan - displays the images as a red/cyan pair.
redcyanlum - displays the luminance of the images as a red/cyan pair.
leftonly - displays the left side only
rightonly - displays the right side only
stereo - mode that supports Crystal Eyes(tm) or Zscreen (tm) renders

---
toggle(tgl): boolean
    properties: create, query, edit
    Turns the ground plane display on/off.

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
viewImageCount(vic): int
    properties: create, query, edit
    The render editor has the capability to render multiple cameras within a
single view. This is different from image binning where an image is saved. Multiple image views
are useful for comparing two different camera renders side-by-side. The viewImageCount flag tells
the editor that it should prepare its internal image storage mechanism for a given number of views.

---
viewTransformName(vtn): string
    properties: query, edit
    Sets/gets the view transform to be applied if color management is enabled in the
current view.

---
writeImage(wi): string
    properties: edit
    write the current Editor Image to disk

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderWindowEditor.html 
    """


def renderWindowSelectContext(exists: boolean, image1: string, image2: string, image3: string) -> string:
    """Synopsis:
---
---
 renderWindowSelectContext([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderWindowSelectContext is undoable, queryable, and editable.


Return:
---


    string: Context name

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderWindowSelectContext.html 
    """


def renderer(addGlobalsNode: string, addGlobalsTab: tuple[string, string, string], batchRenderOptionsProcedure: string, batchRenderOptionsStringProcedure: string, batchRenderProcedure: string, cancelBatchRenderProcedure: string, changeIprRegionProcedure: string, commandRenderProcedure: string, exists: boolean, globalsNodes: boolean, globalsTabCreateProcNames: boolean, globalsTabLabels: boolean, globalsTabUpdateProcNames: boolean, iprOptionsMenuLabel: string, iprOptionsProcedure: string, iprOptionsSubMenuProcedure: string, iprRenderProcedure: string, iprRenderSubMenuProcedure: string, isRunningIprProcedure: string, logoCallbackProcedure: string, logoImageName: string, materialViewRendererList: boolean, materialViewRendererPause: boolean, materialViewRendererSuspend: boolean, namesOfAvailableRenderers: boolean, pauseIprRenderProcedure: string, polyPrelightProcedure: string, refreshIprRenderProcedure: string, renderDiagnosticsProcedure: string, renderGlobalsProcedure: string, renderMenuProcedure: string, renderOptionsProcedure: string, renderProcedure: string, renderRegionProcedure: string, renderSequenceProcedure: string, rendererUIName: string, renderingEditorsSubMenuProcedure: string, showBatchRenderLogProcedure: string, showBatchRenderProcedure: string, showRenderLogProcedure: string, startIprRenderProcedure: string, stopIprRenderProcedure: string, supportColorManagement: boolean, textureBakingProcedure: string, unregisterRenderer: boolean) -> None:
    """Synopsis:
---
---
 renderer([string], [addGlobalsNode=string], [addGlobalsTab=[string, string, string]], [batchRenderOptionsProcedure=string], [batchRenderOptionsStringProcedure=string], [batchRenderProcedure=string], [cancelBatchRenderProcedure=string], [changeIprRegionProcedure=string], [commandRenderProcedure=string], [exists=boolean], [globalsNodes=boolean], [globalsTabCreateProcNames=boolean], [globalsTabLabels=boolean], [globalsTabUpdateProcNames=boolean], [iprOptionsMenuLabel=string], [iprOptionsProcedure=string], [iprOptionsSubMenuProcedure=string], [iprRenderProcedure=string], [iprRenderSubMenuProcedure=string], [isRunningIprProcedure=string], [logoCallbackProcedure=string], [logoImageName=string], [materialViewRendererList=boolean], [materialViewRendererPause=boolean], [materialViewRendererSuspend=boolean], [namesOfAvailableRenderers=boolean], [pauseIprRenderProcedure=string], [polyPrelightProcedure=string], [refreshIprRenderProcedure=string], [renderDiagnosticsProcedure=string], [renderGlobalsProcedure=string], [renderMenuProcedure=string], [renderOptionsProcedure=string], [renderProcedure=string], [renderRegionProcedure=string], [renderSequenceProcedure=string], [rendererUIName=string], [renderingEditorsSubMenuProcedure=string], [showBatchRenderLogProcedure=string], [showBatchRenderProcedure=string], [showRenderLogProcedure=string], [startIprRenderProcedure=string], [stopIprRenderProcedure=string], [supportColorManagement=boolean], [textureBakingProcedure=string], [unregisterRenderer=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

renderer is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To register a renderer called "myRenderer":
---

cmds.renderer( 'myRenderer' )

To edit a renderer called "myRenderer" with its rendererUIName
being "My Renderer":
---

cmds.renderer( 'myRenderer', edit=True, rendererUIName='My Renderer' )

To register a renderer called "anotherRenderer" with all
its parameters specified.
---

cmds.renderer( 'anotherRenderer', rendererUIName='Another Renderer', iprRenderProcedure='mayaSoftwareIprRender', -iprOptionsProcedure='', isRunningIprProcedure='mayaSoftwareIsRunningIpr', startIprRenderProcedure='mayaSoftwareStartIprRender', stopIprRenderProcedure='mayaSoftwareStopIprRender', refreshIprRenderProcedure='mayaSoftwareRefreshIprImage', pauseIprRenderProcedure='mayaSoftwarePauseIprRender', changeIprRegionProcedure='mayaSoftwareChangeIprRegion', iprOptionsMenuLabel='IPR Tuning Options', iprOptionsSubMenuProcedure='mayaSoftwareIprUpdateOptionsSubMenu', iprRenderSubMenuProcedure='mayaSoftwareIprUpdateRenderSubMenu', renderProcedure='mayaSoftwareRender', renderOptionsProcedure='RenderOptions', renderDiagnosticsProcedure='RenderDiagnostics', commandRenderProcedure='render -batch', batchRenderProcedure='BatchRender', batchRenderOptionsProcedure='BatchRenderOptions', batchRenderOptionsStringProcedure="mayaSoftwareBatchRenderOptionsString", cancelBatchRenderProcedure='CancelBatchRender', showBatchRenderProcedure='ShowBatchRender', showRenderLogProcedure='', showBatchRenderLogProcedure='', renderRegionProcedure='mayaRenderRegion', textureBakingProcedure='performConvertSolidTx', polyPrelightProcedure='performPrelight', renderingEditorsSubMenuProcedure='', logoImageName='', logoCallbackProcedure='' )

To add a render globals node the renderer uses:
---

cmds.renderer( 'anotherRenderer', edit=True, addGlobalsNode='defaultRenderGlobals' )

To add the tabs associated with the specified renderer
for the unified render globals window, use the syntax
---

     renderer -edit
              -addGlobalsTab globalsTabLabel
                             globalsTabCreateProcName
                             globalsTabUpdateProcName
              renderer;
---

where "globalsTabLabel" is the label of the tab,
"globalsTabCreatedProcName" is the name of the mel procedure
which is used to create the content in the tab.
and "globalsTabCreatedProcName" is the name of the mel procedure
which is used to update the content in the tab.
---

Note that if you want to add a number of tabs, you need to repeat
this renderer command for each tab you wish to add, as shown below.
---

cmds.renderer( 'anotherRenderer', edit=True, addGlobalsTab=('Maya Software', 'createMayaSoftwareGlobalsTab', 'updateMayaSoftwareGlobalsTab') )


To get a list of unified render globals window tab labels associated
with the specified renderer.
---

cmds.renderer( 'anotherRenderer', query=True, globalsTabLabels=True )

To get a list of names of mel procedures that are used to
create the unified render globals window tabs associated with
the specified renderer.
---

cmds.renderer( 'anotherRenderer', query=True, globalsTabCreateProcNames=True )

To get a list of names of mel procedures that are used to
update the unified render globals window tabs associated with
the specified renderer.
---

cmds.renderer( 'anotherRenderer', query=True, globalsTabUpdateProcNames=True )

To view a list of registered renderers.
---

cmds.renderer( query=True, namesOfAvailableRenderers=True )

To check if anotherRenderer exists.
---

cmds.renderer( 'anotherRenderer', exists=True )

To view a list of render globals nodes used by the specified
renderer:
---

cmds.renderer( 'anotherRenderer', query=True, globalsNodes=True )

---


Flags:
---


---
addGlobalsNode(agn): string
    properties: create, query, edit
    This flag allows the user to add a globals node the specified
renderer uses.

---
addGlobalsTab(agt): [string, string, string]
    properties: create, edit
    Add a tab associated with the specified renderer for the
unified render globals window.

---
batchRenderOptionsProcedure(bro): string
    properties: create, query, edit
    Set or query the batch render options procedure associated with the
specified renderer.

---
batchRenderOptionsStringProcedure(bso): string
    properties: create, query, edit
    Set or query the argument string that will be used with the command
line utility 'Render' when doing a batch render

---
batchRenderProcedure(br): string
    properties: create, query, edit
    Set or query the batch render procedure associated with the
specified renderer.

---
cancelBatchRenderProcedure(cbr): string
    properties: create, query, edit
    Set or query returns the cancel batch render procedure associated
with the specified renderer.

---
changeIprRegionProcedure(cir): string
    properties: create, query, edit
    Set or query the change IPR region procedure associated with the
specified renderer.

---
commandRenderProcedure(cr): string
    properties: create, query, edit
    Set or query the command line rendering procedure associated with the
specified renderer.

---
exists(ex): boolean
    properties: query, edit
    The flag returns true if the specified renderer is registered
in the registry, and it returns false otherwise.

---
globalsNodes(gn): boolean
    properties: create, query, edit
    This flag returns the list of render globals nodes the
specified renderer uses.

---
globalsTabCreateProcNames(gtc): boolean
    properties: create, query, edit
    This flag returns the names of procedures that are used to
create the unified render globals window tabs
that are associated with the specified renderer.

---
globalsTabLabels(gtl): boolean
    properties: create, query, edit
    This flag returns the labels of unified render globals window tabs
that are associated with the specified renderer.

---
globalsTabUpdateProcNames(gtu): boolean
    properties: create, query, edit
    This flag returns the names of procedures that are used to
update the unified render globals window tabs
that are associated with the specified renderer.

---
iprOptionsMenuLabel(ipm): string
    properties: create, query, edit
    Set or query the label for the IPR update options menu which is under
the render view's IPR menu.

---
iprOptionsProcedure(io): string
    properties: create, query, edit
    Set or query the IPR render options procedure associated with the
specified renderer.

---
iprOptionsSubMenuProcedure(ips): string
    properties: create, query, edit
    Set or query the procedure for creating the sub menu for the IPR
update options menu which is under the render view's IPR menu.

---
iprRenderProcedure(ipr): string
    properties: create, query, edit
    Set or query the IPR render command associated with the
specified renderer.

---
iprRenderSubMenuProcedure(irs): string
    properties: create, query, edit
    Set or query the procedure for creating the sub menu for the IPR
render menu which is under the render view's IPR menu.

---
isRunningIprProcedure(isr): string
    properties: create, query, edit
    Set or query the isRunningIpr command associated with the
specified renderer.

---
logoCallbackProcedure(lgc): string
    properties: create, query, edit
    Set or query the procedure which is a callback associated to the
logo for the specified renderer.   For example, the logo and the
callback can be used in the unified render globals window beside
the "Render Using" optionMenu.

---
logoImageName(log): string
    properties: create, query, edit
    Set or query the logo image name for the specified renderer.
The logo is a image representing the renderer.

---
materialViewRendererList(mvl): boolean
    properties: query, edit
    Returns the names of material view renderers that are currently registered.

---
materialViewRendererPause(mvp): boolean
    properties: query, edit
    Specifies whether to pause the material viewer.
Useful for globally halting updates to the material viewer.
The material view renderer will remain suspended while the viewer is paused.

---
materialViewRendererSuspend(mvs): boolean
    properties: query, edit
    Specifies whether to suspend or resume the material view renderer.
Useful for temporarily stopping the material view renderer while another
rendering task is running.

---
namesOfAvailableRenderers(ava): boolean
    properties: query, edit
    Returns the names of renderers that are currently registered.

---
pauseIprRenderProcedure(psi): string
    properties: create, query, edit
    Set or query the pause IPR render procedure associated with the
specified renderer.

---
polyPrelightProcedure(pp): string
    properties: create, query, edit
    Set or query the polygon prelight procedure associated with
the specified renderer.

---
refreshIprRenderProcedure(rfi): string
    properties: create, query, edit
    Set or query the refresh IPR render procedure associated with the
specified renderer.

---
renderDiagnosticsProcedure(rd): string
    properties: create, query, edit
    Set or query the render diagnostics procedure associated with the
specified renderer.

---
renderGlobalsProcedure(rg): string
    properties: create, query, edit
    This flag is obsolete.  It will be removed in the next release.

---
renderMenuProcedure(rm): string
    properties: create, query, edit
    This flag is obsolete. It will be removed in the next release.

---
renderOptionsProcedure(ro): string
    properties: create, query, edit
    Set or query the render options procedure associated with the
specified renderer.

---
renderProcedure(r): string
    properties: create, query, edit
    Set or query the render command associated with the specified renderer.

---
renderRegionProcedure(rr): string
    properties: create, query, edit
    Set or query the render region procedure associated with the specified
renderer.

---
renderSequenceProcedure(rs): string
    properties: create, query, edit
    Set or query the sequence rendering procedure associated with the
specified renderer.

---
rendererUIName(ui): string
    properties: create, query, edit
    Set or query the rendererUIName for the specified renderer.
The rendererUIName is the name of the renderer as it would appear
in menus.

---
renderingEditorsSubMenuProcedure(res): string
    properties: create, query, edit
    Set or query the procedure reponsible for creating renderer
specific editors submenu under the "Rendering Editors" menu
for the specified renderer.

---
showBatchRenderLogProcedure(brl): string
    properties: create, query, edit
    Set or query the log file batch procedure associated with the
specified renderer.

---
showBatchRenderProcedure(sbr): string
    properties: create, query, edit
    Set or query the show batch render procedure associated with
the specified renderer.

---
showRenderLogProcedure(srl): string
    properties: create, query, edit
    Set or query the log file render procedure associated with
the specified renderer.

---
startIprRenderProcedure(sti): string
    properties: create, query, edit
    Set or query the start IPR render procedure associated with the
specified renderer.

---
stopIprRenderProcedure(spi): string
    properties: create, query, edit
    Set or query the stop IPR render procedure associated with the
specified renderer.

---
supportColorManagement(scm): boolean
    properties: query, edit
    Specifies whether the renderer supports color management.

---
textureBakingProcedure(tb): string
    properties: create, query, edit
    Set or query the texture baking procedure associated with
the specified renderer.

---
unregisterRenderer(unr): boolean
    properties: query, edit
    Unregister the specified renderer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/renderer.html 
    """


def reorder(back: boolean, front: boolean, relative: int) -> None:
    """Synopsis:
---
---
 reorder(
[objects...]
    , [back=boolean], [front=boolean], [relative=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

reorder is undoable, NOT queryable, and NOT editable.
For relative moves, both positive and negative numbers may be
specified.  Positive numbers move the object forward and
negative numbers move the object backward amoung its
siblings. When an object is at the end (beginning) of the list
of siblings, a relative move of 1 (-1) will put the object at
the beginning (end) of the list of siblings.  That is,
relative moves will wrap if necessary.

If a shape is specified and it is the only child then its parent
will be reordered.




Example:
---
import maya.cmds as cmds

create a hierarchy
cmds.sphere( n='sphere1' )
cmds.sphere( n='sphere2' )
cmds.sphere( n='sphere3' )
cmds.sphere( n='sphere4' )
cmds.group( 'sphere1', 'sphere2', 'sphere3', 'sphere4', n='group1' )

The hierarchy group1 contains sphere1, sphere2, sphere3 and sphere4.
The command below moves sphere2 before sphere1.
cmds.reorder( 'sphere2', r=-1 )

make sphere1 the first sibling
cmds.reorder( 'sphere1', front=True )

move sphere3 forward 2 siblings. Moving it forward one
sibling would put it at the end. Moving it forward again
puts it at the beginning.
cmds.reorder( 'sphere3', r=2 )

---


Flags:
---


---
back(b): boolean
    properties: create
    Move object(s) to back of sibling list.

---
front(f): boolean
    properties: create
    Move object(s) to front of sibling list.

---
relative(r): int
    properties: create
    Move object(s) relative to other siblings.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/reorder.html 
    """


def reorderContainer(back: boolean, front: boolean, relative: int) -> None:
    """Synopsis:
---
---
 reorderContainer([back=boolean], [front=boolean], [relative=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

reorderContainer is undoable, queryable, and editable.
For relative moves, both positive and negative numbers may be
specified.  Positive numbers move the object forward and
negative numbers move the object backward amoung its
siblings. When an object is at the end (beginning) of the list
of siblings, a relative move of 1 (-1) will put the object at
the beginning (end) of the list of siblings.  That is,
relative moves will wrap if necessary.

Only nodes within one container can be moved at a time.
Note: The container command's -nodeList flag will return a sorted list of
contained nodes. To see the effects of reordering, use the -unsortedOrder flag
in conjunction with the -nodeList flag.




Example:
---
import maya.cmds as cmds


create a container
cmds.sphere( n='sphere1' )
cmds.sphere( n='sphere2' )
cmds.sphere( n='sphere3' )
cmds.sphere( n='sphere4' )
cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )

The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
The command below moves sphere2 before sphere1.
cmds.reorderContainer( 'sphere2', r=-1 )

make sphere1 the first sibling
cmds.reorderContainer( 'sphere1', front=True )

move sphere3 forward 2 siblings. Moving it forward one
sibling would put it at the end. Moving it forward again
puts it at the beginning.
cmds.reorderContainer( 'sphere3', r=2 )

---


Flags:
---


---
back(b): boolean
    properties: create, query, edit
    Move object(s) to back of container contents list

---
front(f): boolean
    properties: create, query, edit
    Move object(s) to front of container contents list

---
relative(r): int
    properties: create, query, edit
    Move object(s) relative to other container contents

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/reorderContainer.html 
    """


def reorderDeformers(name: string) -> None:
    """Synopsis:
---
---
 reorderDeformers(
string string selectionList
    , [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

reorderDeformers is undoable, NOT queryable, and NOT editable.
It inserts deformer2 before deformer1. Currently supported deformer
nodes include: sculpt, cluster, jointCluster, lattice, wire,
jointLattice, boneLattice, blendShape.




Example:
---
import maya.cmds as cmds

Create some geometry to deform
cmds.sphere( name='sphere1' )
cmds.sphere( name='sphere2' )

Create a couple of deformers
cmds.select( 'sphere1Shape', 'sphere2Shape' )
cmds.sculpt( name='sculpt1' )
cmds.select( 'sphere1Shape', 'sphere2Shape' )
cmds.cluster( name='cluster1' )

Change their order
cmds.reorderDeformers( 'sculpt1', 'cluster1', 'sphere1Shape', 'sphere2Shape' )

---


Flags:
---


---
name(n): string
    properties: create
    This flag is obsolete and is not used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/reorderDeformers.html 
    """


def requires(dataType: string, nodeType: string) -> None:
    """Synopsis:
---
---
 requires(
string string
    , [dataType=string], [nodeType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

requires is undoable, NOT queryable, and NOT editable.
The first string names a product (either "maya", or a plug-in name)

The second string gives the version. This command is only useful during
file I/O, so users should not have any need to use this command themselves.

The flags "-nodeType" and "-dataType" specify the node types
and data types defined by the plug-in. When Maya open a scene file, it
runs "requires" command in the file and load required plug-ins. But some
plug-ins may be not loaded because they are missing. The flags "-nodeType"
and "-dataType" are used by the missing plug-ins. If one plug-in is missing,
nodes and data created by this plug-in are created as unknown nodes and
unknown data. Maya records their original types for these unknown nodes
and data. When these nodes and data are saved back to file, it will be
possible to determine the associated missing plug-ins. And when export
selected nodes, Maya can write out the exact required plug-ins.
The flags "-nodeType" and "-dataType" is optional. In this command, if these
flags are not given for one plug-in and the plug-in is missing, the "requires"
command of this plug-in will always be saved back.




Example:
---
import maya.cmds as cmds

cmds.requires( 'maya', '7.0' )
cmds.requires( 'simpleLoftNode.so', '1.0' )
cmds.requires( 'gpuCache', '1.0', nodeType='gpuCache')

---


Flags:
---


---
dataType(dt): string
    properties: create, multiuse
    Specify a data type defined by this plug-in.
The data type is specified by MFnPlugin::registerData() when register
the plug-in.

---
nodeType(nt): string
    properties: create, multiuse
    Specify a node type defined by this plug-in.
The node type is specified by MFnPlugin::registerNode() when register
the plug-in.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/requires.html 
    """


def reroot() -> None:
    """Synopsis:
---
---
 reroot(
[object]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

reroot is undoable, NOT queryable, and NOT editable.
The given(or selected) joint should not have skin attached. The    command
works on the given or selected joint. No options or flags are necessary.




Example:
---
import maya.cmds as cmds

joint5 will be a new root joint of the skeleton.
cmds.reroot( 'joint5' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/reroot.html 
    """


def resampleFluid(resampleDepth: int, resampleHeight: int, resampleWidth: int) -> None:
    """Synopsis:
---
---
 resampleFluid([resampleDepth=int], [resampleHeight=int], [resampleWidth=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

resampleFluid is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

set width resolution to 3
cmds.resampleFluid( rw=3 )

set height resolution to 12
cmds.resampleFluid( rh=12 )

set all  resolutions to 20
cmds.resampleFluid( rw=20, rh=20, rd=20 )

---


Flags:
---


---
resampleDepth(rd): int
    properties: create, query, edit
    Change depth resolution to this value

---
resampleHeight(rh): int
    properties: create, query, edit
    Change height resolution to this value

---
resampleWidth(rw): int
    properties: create, query, edit
    Change width resolution to this value

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/resampleFluid.html 
    """


def resetTool() -> None:
    """Synopsis:
---
---
 resetTool(
[string]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

resetTool is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.resetTool( 'moveSuperContext' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/resetTool.html 
    """


def resolutionNode(name: string, parent: string, shared: boolean, skipSelect: boolean) -> string:
    """Synopsis:
---
---
 resolutionNode(
string
    , [name=string], [parent=string], [shared=boolean], [skipSelect=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

resolutionNode is undoable, NOT queryable, and NOT editable.
The resolutionNode creates a render resolution node
and registers it with the model.  The createNode
command will not register nodes of this type correctly.




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

cmds.resolutionNode( 'customRes' )
cmds.resolutionNode( 'customRes', name='customRes' )

---
Return:
---


    string: The name of the new node.
    string: The name of the render resolution node

Flags:
---


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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/resolutionNode.html 
    """


def resourceManager(nameFilter: string, saveAs: tuple[string, string]) -> None:
    """Synopsis:
---
---
 resourceManager([nameFilter=string], [saveAs=[string, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

resourceManager is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

List all resources starting with an "a"
cmds.resourceManager(nameFilter="a*")

---


Flags:
---


---
nameFilter(nf): string
    properties: create
    List only resources matching the name. Argument may contain ? and *
characters.

---
saveAs(s): [string, string]
    properties: create
    Saves a copy of the resource (first parameter) as a separate file (second parameter).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/resourceManager.html 
    """


def retimeKeyCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, moveByFrame: int, name: string, snapOnFrame: boolean) -> boolean:
    """Synopsis:
---
---
 retimeKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [moveByFrame=int], [name=string], [snapOnFrame=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

retimeKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a manipulator style scale key context for the graph editor
---

cmds.retimeKeyCtx( 'retimeKeyContext' )

---
Return:
---


    boolean: Query value from the snapOnFame setting.

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
moveByFrame(mbf): int
    properties: edit
    Move the selected retime bar by the specified number of frames

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
snapOnFrame(sof): boolean
    properties: query, edit
    When set, the retime markers will snap on frames as they are moved.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/retimeKeyCtx.html 
    """


def reverseCurve(caching: boolean, constructionHistory: boolean, curveOnSurface: boolean, name: string, nodeState: int, object: boolean, range: boolean, replaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 reverseCurve(
curve
    , [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [name=string], [nodeState=int], [object=boolean], [range=boolean], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

reverseCurve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.reverseCurve( 'curve1', constructionHistory=True )
Reverses curve1 with construction history on.  The result will
be a string array, where the first string is the name of the new
reversed curve and the second string is the name of the new
dependency node.

cmds.reverseCurve( 'curve1', ch=False, replaceOriginal=True )
Reverses curve1 without construction history, replacing the original.
The result will be a string array, where the first string
is the name of the curve (curve1).  Because history is off,
no dependency node will be created.  The reversed curve will
replace the original curve.

cmds.reverseCurve( 'curve1', ch=True, rpo=True )
Reverses curve1 with history, trying to replace the original.
If curve1 was not a result of construction history, then this command
will simply replace curve1 with the reversed curve.  No dependency
node will be created.

If curve1 was a result of construction history, then this command
will insert a reverse dependency node before the curve.  eg.
Before reverseCurve cmd:   curve0 ---> closeCurve DN ---> curve1
After cmd:  curve0 ---> closeCurve DN ---> reverseCurve DN ---> curve1

The result will be a string array , where the first string
is the name of the curve (curve1) and the second name is the
new dependency node.

---
Return:
---


    list[string]: (object name and node name)

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
range(rn): boolean
    properties: create
    Force a curve range on complete input curve.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/reverseCurve.html 
    """


def reverseSurface(caching: boolean, constructionHistory: boolean, direction: int, name: string, nodeState: int, object: boolean, replaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 reverseSurface(
surface
    , [caching=boolean], [constructionHistory=boolean], [direction=int], [name=string], [nodeState=int], [object=boolean], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

reverseSurface is undoable, queryable, and editable.
This command also handles selected surface isoparms. For a selected
isoparm, imagine that the isoparm curve is reversed after the
operation. E.g. reverseSurface surface.v[0.1] will reverse in the U
direction.




Example:
---
import maya.cmds as cmds

cmds.reverseSurface( 'surface1', ch=True, d=0 )
cmds.reverseSurface( 'surface1.v[0.1]', ch=True )
Reverses surface1 with construction history in the U direction.
The name of the new surface and the name of the new dependency node
are returned.

cmds.reverseSurface( 'surface1', ch=False, rpo=True, d=1 )
cmds.reverseSurface( 'surface1.u[0.1]', ch=True )
Reverses surface1 without history, with replace original on,
in the V direction.  Because the "-rpo" flag is on, the name of
the original surface is returned as well as the new dependency node.
The reversed surface will <em>replace</em> the original surface.

cmds.reverseSurface( 'surface1', ch=False, rpo=True, d=2 )
Reverses surface1 without history, with replace original on,
in both the U and V directions.

cmds.reverseSurface( 'surface1', ch=False, rpo=True, d=3 )
Swaps the U and V directions of surface1 with history, with replace
original on.  This has the effect of reversing the surface normal.

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
    The direction to reverse the surface in:
0 - U,
1 - V,
2 - Both U and V,
3 - Swap
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

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/reverseSurface.html 
    """


def revolve(autoCorrectNormal: boolean, axis: tuple[linear, linear, linear], axisChoice: int, axisX: linear, axisY: linear, axisZ: linear, bridge: boolean, caching: boolean, computePivotAndAxis: int, constructionHistory: boolean, degree: int, endSweep: angle, name: string, nodeState: int, object: boolean, pivot: tuple[linear, linear, linear], pivotX: linear, pivotY: linear, pivotZ: linear, polygon: int, radius: linear, radiusAnchor: float, range: boolean, rebuild: boolean, sections: int, startSweep: angle, tolerance: linear, useLocalPivot: boolean, useTolerance: boolean) -> list[string]:
    """Synopsis:
---
---
 revolve(
curve
    , [autoCorrectNormal=boolean], [axis=[linear, linear, linear]], [axisChoice=int], [axisX=linear], [axisY=linear], [axisZ=linear], [bridge=boolean], [caching=boolean], [computePivotAndAxis=int], [constructionHistory=boolean], [degree=int], [endSweep=angle], [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]], [pivotX=linear], [pivotY=linear], [pivotZ=linear], [polygon=int], [radius=linear], [radiusAnchor=float], [range=boolean], [rebuild=boolean], [sections=int], [startSweep=angle], [tolerance=linear], [useLocalPivot=boolean], [useTolerance=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

revolve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To revolve a curve about the X axis at the origin. The profile curve is
revolved by 360 degrees by default.
cmds.revolve( 'curve1', ax=(1, 0, 0), p=(0, 0, 0) )

To revolve a curve about the Y axis at 1,0,1:
cmds.revolve( 'curve1', ax=(0, 1, 0), p=(1, 0, 1) )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
autoCorrectNormal(acn): boolean
    properties: create, query, edit
    If this is set to true we will attempt to reverse the direction of the axis in case it is necessary to do so for the surface normals to end up pointing to the outside of the object.
Default: false

---
axis(ax): [linear, linear, linear]
    properties: create, query, edit
    Revolve axis

---
axisChoice(aco): int
    properties: create, query, edit
    Only used for computed axis/pivot case.  As we are computing the axis for a planar curve, we have two choices for the major axis based axis.  We will choose the axis corresponding to the longer dimension of the object (0), or explicitly choose one or the other (choices 1 and 2).
Default: 0

---
axisX(axx): linear
    properties: create, query, edit
    X of the axis
Default: 1

---
axisY(axy): linear
    properties: create, query, edit
    Y of the axis
Default: 0

---
axisZ(axz): linear
    properties: create, query, edit
    Z of the axis
Default: 0

---
bridge(br): boolean
    properties: create, query, edit
    If true, we will close a partial revolve to get a pie shaped surface.  The surface will be closed, but not periodic the way it is in the full revolve case.
Default: false

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
computePivotAndAxis(cpa): int
    properties: create, query, edit
    If this is set to 2, we will compute the axis, use the curve position and radius to compute the pivot for the revolve internally.  The value of the pivot and axis attributes are ignored.  If this is set to 1, we will take the supplied axis, but compute the pivot.  If this is set to 0, we will take both the supplied axis and pivot.
Default: 0

---
degree(d): int
    properties: create, query, edit
    The degree of the resulting surface.
Default: 3

---
endSweep(esw): angle
    properties: create, query, edit
    The value for the end sweep angle, in the current units.  This must be no more than the maximum, 360 degrees, or 2 Pi radians.
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
    Revolve pivot point

---
pivotX(px): linear
    properties: create, query, edit
    X of the pivot
Default: 0

---
pivotY(py): linear
    properties: create, query, edit
    Y of the pivot
Default: 0

---
pivotZ(pz): linear
    properties: create, query, edit
    Z of the pivot
Default: 0

---
radius(r): linear
    properties: create, query, edit
    The pivot point will be this distance away from the bounding box of the curve, if computedPivot is set to true.  The value of the pivot attribute is ignored.
Default: 1

---
radiusAnchor(ra): float
    properties: create, query, edit
    The position on the curve for the anchor point so that we can compute the pivot using the radius value.  If in 0 - 1 range, its on the curve, normalized parameter range.  If < 0 or > 1, its computed based on the bounding box.
Default: -1

---
sections(s): int
    properties: create, query, edit
    Number of sections of the resulting surface (if tolerance is not used).
Default: 8

---
startSweep(ssw): angle
    properties: create, query, edit
    The value for the start sweep angle, in the current units.  This must be no more than the maximum, 360 degrees, or 2 Pi radians.
Default: 0

---
tolerance(tol): linear
    properties: create, query, edit
    Tolerance to build to (if useTolerance attribute is set)
Default: 0.01

---
useTolerance(ut): boolean
    properties: create, query, edit
    Use the tolerance, or the number of sections to control the sections.
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

---
range(rn): boolean
    properties: create
    Force a curve range on complete input curve.

---
rebuild(rb): boolean
    properties: create
    Rebuild the input curve(s) before using them in the operation.  Use nurbsCurveRebuildPref to set the parameters for the conversion.

---
useLocalPivot(ulp): boolean
    properties: create, query, edit
    If true, then the pivot of the profile curve is used
as the start point of the axis of revolution.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/revolve.html 
    """


def rigidBody(active: boolean, angularVelocity: boolean, applyForceAt: string, bounciness: float, cache: boolean, centerOfMass: tuple[float, float, float], collisions: boolean, contactCount: boolean, contactName: boolean, contactPosition: boolean, damping: float, deleteCache: boolean, dynamicFriction: float, force: boolean, ignore: boolean, impulse: tuple[float, float, float], impulsePosition: tuple[float, float, float], initialAngularVelocity: tuple[float, float, float], initialVelocity: tuple[float, float, float], layer: int, lockCenterOfMass: boolean, mass: float, name: string, orientation: tuple[float, float, float], particleCollision: boolean, passive: boolean, position: tuple[float, float, float], removeShape: string, solver: string, spinImpulse: tuple[float, float, float], standInObject: string, staticFriction: float, tesselationFactor: int, velocity: boolean) -> string:
    """Synopsis:
---
---
 rigidBody([active=boolean], [angularVelocity=boolean], [applyForceAt=string], [bounciness=float], [cache=boolean], [centerOfMass=[float, float, float]], [collisions=boolean], [contactCount=boolean], [contactName=boolean], [contactPosition=boolean], [damping=float], [deleteCache=boolean], [dynamicFriction=float], [force=boolean], [ignore=boolean], [impulse=[float, float, float]], [impulsePosition=[float, float, float]], [initialAngularVelocity=[float, float, float]], [initialVelocity=[float, float, float]], [layer=int], [lockCenterOfMass=boolean], [mass=float], [name=string], [orientation=[float, float, float]], [particleCollision=boolean], [passive=boolean], [position=[float, float, float]], [removeShape=string], [solver=string], [spinImpulse=[float, float, float]], [standInObject=string], [staticFriction=float], [tesselationFactor=int], [velocity=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rigidBody is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Creates a rigid body with a initial velocity of 10 in the x
direction, a bounciness of 0.5 and a static friction coefficent
of 0.4.
---

cmds.rigidBody( n='myRigidBody', active=True, iv=(10, 0, 0), b=0.5, sf=0.4 )

---
Return:
---


    string: New rigid body name.

Flags:
---


---
active(act): boolean
    properties: create, query, edit
    Creates a rigid body that is active.  An active rigid body accepts and
causes collisions and is effected by dynamic fields.  This is the
default.

---
angularVelocity(av): boolean
    properties: query
    Current angular velocity of rigid body.

---
applyForceAt(afa): string
    properties: create, query, edit
    Determines how forces are applied to the rigid body.
The choices are centerOfMass | boundingBox | verticesOrCVs.
Default: boundingBox

---
bounciness(b): float
    properties: create, query, edit
    Sets the restitution (or bounciness) of the rigid body.
Range:   0.0 - 2.0
Default: 0.6

---
cache(c): boolean
    properties: create, query, edit
    Turns caching on (1) or off (0) for the rigid body.
Default: off

---
centerOfMass(com): [float, float, float]
    properties: create, query, edit
    Sets the center of mass (x,y,z) of the rigid body.
Default: actual center of mass.

---
collisions(cl): boolean
    properties: create, query, edit
    Truns collisions on/off for the rigid body.  If the collisions
are turned of the rigid body will not collide with any other rigid body.
Default: on.

---
contactCount(cc): boolean
    properties: query
    returns the current contact count for the rigid body.

---
contactName(cn): boolean
    properties: query
    returns all the rigid body names which are in contact with this shape.  One name
for each contact will be returned.

---
contactPosition(cp): boolean
    properties: query
    returns all the contact position.  One position for each contact
will be returned.

---
damping(dp): float
    properties: create, query, edit
    Sets the damping value of the rigid body.
Range:   -2.0 - 2.0
Default: 0.0

---
deleteCache(dc): boolean
    properties: edit
    Deletes the cache (if one exists) of the rigid body.

---
dynamicFriction(df): float
    properties: create, query, edit
    Sets the dynamic friction for the rigid body.
Range:   0.0 - 1.0
Default: 0.2

---
force(f): boolean
    properties: query
    Current force on the rigid body.

---
ignore(ig): boolean
    properties: create, query, edit
    Causes the rigid body to be ignored in the rigid solver.
Default: off

---
impulse(i): [float, float, float]
    properties: create, edit
    Applies an impulse (instantaneous) force on a rigid body.
Default: 0.0 0.0 0.0

---
impulsePosition(imp): [float, float, float]
    properties: create, edit
    The position at which the impulse is applied.
Default: the bodies center of mass.

---
initialAngularVelocity(iav): [float, float, float]
    properties: create, query, edit
    Sets the initial angular velocity of the rigid body.
Default: 0.0 0.0 0.0

---
initialVelocity(iv): [float, float, float]
    properties: create, query, edit
    Sets the initial velocity of the rigid body.
Default: 0.0 0.0 0.0

---
layer(l): int
    properties: create, query, edit
    Sets the collision layer of the rigid body.  Only rigid bodies in the
same collision layer can collide with each other.
Range:   >= 0
Default: 0.

---
lockCenterOfMass(lcm): boolean
    properties: create, query, edit
    Locks the center of mass for the rigid body.
Default: off

---
mass(m): float
    properties: create, query, edit
    Sets the mass of the rigid body.
Range:   > 0
Default: 1.0

---
name(n): string
    properties: create, query, edit
    Assigns the rigid body the given name.

---
orientation(o): [float, float, float]
    properties: create, query, edit
    Sets the initial orientation (x,y,z) of the rigid body.
Default: current orientation.

---
particleCollision(pc): boolean
    properties: create, query, edit
    Turns the ability for a rigid body to collide with particles
on and off.  The particles will exert a force on the rigid body.
Default: off

---
passive(pas): boolean
    properties: create, query, edit
    Creates a rigid body that is passive.  A passive rigid body does not
react to collisions but active rigid bodies can collide with it.
Dynamic Fields will not effect a passive rigid body.  Only passive
rigid bodies can be keyframed.

---
position(p): [float, float, float]
    properties: create, query, edit
    Sets the initial position (x,y,z) of the rigid body.
Default: current position.

---
removeShape(rs): string
    properties: create, query, edit
    Remove the named shape.

---
solver(slv): string
    properties: create, query, edit
    The name of the solver which this rigid node is to resided.  If the
solver does not exists then the rigid body will not be created.  If the
edit flag is thrown add the solver exists, the rigid body will be moved
to that solver.

---
spinImpulse(si): [float, float, float]
    properties: create, edit
    Applies an spin impulse (instantaneous rotational) force on a rigid body.
Default: 0.0 0.0 0.0

---
standInObject(sio): string
    properties: create, query, edit
    Causes the simulator to use a stand in object for the simulation.
The choices are none | cube | sphere. The default is none.
Default: none

---
staticFriction(sf): float
    properties: create, query, edit
    Sets the static friction for the rigid body.
Range:   0.0 - 1.0
Default: 0.2

---
tesselationFactor(tf): int
    properties: create, query
    Sets the tesselation factor for a rigid body surface.
Range:   >= 10
Default: 200.

---
velocity(vel): boolean
    properties: query
    Current velocity of rigid body.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rigidBody.html 
    """


def rigidSolver(autoTolerances: boolean, bounciness: boolean, cacheData: boolean, collide: boolean, collisionTolerance: float, contactData: boolean, create: boolean, current: boolean, deleteCache: boolean, displayCenterOfMass: boolean, displayConstraint: boolean, displayVelocity: boolean, dynamics: boolean, friction: boolean, interpenetrate: boolean, interpenetrationCheck: boolean, name: string, rigidBodies: boolean, rigidBodyCount: boolean, showCollision: boolean, showInterpenetration: boolean, solverMethod: int, startTime: float, state: boolean, statistics: boolean, stepSize: float, velocityVectorScale: float) -> None:
    """Synopsis:
---
---
 rigidSolver([autoTolerances=boolean], [bounciness=boolean], [cacheData=boolean], [collide=boolean], [collisionTolerance=float], [contactData=boolean], [create=boolean], [current=boolean], [deleteCache=boolean], [displayCenterOfMass=boolean], [displayConstraint=boolean], [displayVelocity=boolean], [dynamics=boolean], [friction=boolean], [interpenetrate=boolean], [interpenetrationCheck=boolean], [name=string], [rigidBodies=boolean], [rigidBodyCount=boolean], [showCollision=boolean], [showInterpenetration=boolean], [solverMethod=int], [startTime=float], [state=boolean], [statistics=boolean], [stepSize=float], [velocityVectorScale=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rigidSolver is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Set the playback time range to [1, 100]
cmds.playbackOptions(min=1, max=100)
Create a poly cube named "floor"
cmds.polyCube(w=10, h=0.10, d=10, sx=10, sy=1, sz=10, ax=(0, 1, 0), name='floor')
Create a poly sphere named "ball", then move it to 0 9 0
cmds.polySphere(r=1, sx=20, sy=20, ax=(0, 1, 0), name='ball')
cmds.move(0, 9.0, 0, r=True)
Create a new rigid body solver
cmds.rigidSolver(create=True, name='rigidSolver1')
Set the floor to passive rigid body
cmds.select('floor')
cmds.rigidBody(passive=True, solver='rigidSolver1', name='passiveRigidBody')
Set the ball to active rigid body
cmds.select('ball')
cmds.rigidBody(active=True, solver='rigidSolver1', name='activeRigidBody')
Add a gravity field, and connect it to ball
cmds.gravity(pos=(0, 0, 0), m=9.8, dx=0, dy=-1, dz=0, name='gravityField')
cmds.connectDynamic('activeRigidBody', f='gravityField')
Play
cmds.play(w=True)

Set the rigid solver to allow the ball to interpenetrate the floor, then replay
cmds.currentTime(1, e=True)
cmds.rigidSolver('passiveRigidBody', 'activeRigidBody', 'rigidSolver1', e=True, interpenetrate=True)
cmds.play(w=True)

Set the rigid solver to disallow the ball to interpenetrate the floor, replay
cmds.currentTime(1, e=True)
cmds.rigidSolver('passiveRigidBody', 'activeRigidBody', 'rigidSolver1', e=True, collide=True)
cmds.play(w=True)

Set the rigid solver to turn off the bounciness, replay
cmds.currentTime(1, e=True)
cmds.rigidSolver('rigidSolver1', e=True, bounciness=False)
cmds.play(w=True)

---


Flags:
---


---
autoTolerances(at): boolean
    properties: query, edit
    Turns the auto tolerance calculation on and off.  The auto tolerances
calculation will override the default or user defined values of the
step size and collision tolerance value that is calculated based
on the objects in the scene.
Default: 0 (off)

---
bounciness(b): boolean
    properties: query, edit
    Turns bounciness on and off for the an the objects in the
simulation.
Default value: on

---
cacheData(cd): boolean
    properties: query, edit
    Turns the cache on fall all rigid bodies in the system.
Default value: off

---
collide(c): boolean
    properties: query, edit
    Disallows the interpenetration of the two rigid bodies listed.
Default: Collide is on for all bodies.

---
collisionTolerance(ct): float
    properties: query, edit
    Sets the collision tolerance.  This is the error at which two objects
are considered to have collided.
Range:   0.0005 - 1.000
Default: 0.02

---
contactData(ctd): boolean
    properties: query, edit
    Turns the contact data information on/off for all rigid bodies.
Default value: off

---
create(cr): boolean
    properties: create
    Creates a new rigid solver.

---
current(cu): boolean
    properties: create
    Sets rigid solver as the current solver.

---
deleteCache(deleteCache): boolean
    properties: query, edit
    Deletes the cache for all rigid bodies in the system.

---
displayCenterOfMass(dcm): boolean
    properties: query, edit
    Displays the center of mass icon.
Default value: on

---
displayConstraint(dc): boolean
    properties: query, edit
    Displays the constraint vectors.
Default value: on

---
displayVelocity(dv): boolean
    properties: query, edit
    Displays the velocity vectors.
Default value: off

---
dynamics(d): boolean
    properties: query, edit
    Turns dynamics on and off for the an the objects in the simulation.
Default value: on

---
friction(f): boolean
    properties: query, edit
    Turns friction on and off for the an the objects in the simulation.
Default value: on

---
interpenetrate(i): boolean
    properties: query, edit
    Allows the two rigid bodies listed to interpenetrate.
Default: interpenetration is off for all bodies.

---
interpenetrationCheck(ic): boolean
    properties: edit
    Checks for interpenetrating rigid bodies in the scene.

---
name(n): string
    properties: create, query, edit
    Name of the new object

---
rigidBodies(rb): boolean
    properties: query
    Returns a list of rigid bodies in the solver.

---
rigidBodyCount(rbc): boolean
    properties: query
    Returns the number of rigid bodies in the solver.

---
showCollision(sc): boolean
    properties: query, edit
    Displays the colliding objects in a different color.

---
showInterpenetration(si): boolean
    properties: query, edit
    Displays the interpenetrating objects in a different color.

---
solverMethod(sm): int
    properties: query, edit
    Sets the solver method.  The choices are 0 | 1 | 2.
0 = Euler (fastest/least acurate),
1 = Runge-Kutta ( slower/more acurate),
2 = adaptive Runge-Kutta
(slowest/most acurate).
The default is 2 (adaptive Runge-Kutta)

---
startTime(stt): float
    properties: create, query, edit
    Sets the start time for the solver.

---
state(st): boolean
    properties: query, edit
    Turns the rigid solver on or off.

---
statistics(sta): boolean
    properties: query, edit
    Turns the statistic information on/off for all rigid bodies.
Default value: off

---
stepSize(s): float
    properties: query, edit
    Sets the solvers step size.  This is the maximum size of a single step
the
solver will take at one time.
Range:   0.0004 - 0.100
Default: 0.0333

---
velocityVectorScale(vs): float
    properties: query, edit
    scales the velocity vector display.
Default value: 1.0

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rigidSolver.html 
    """


def roll(absolute: boolean, degree: angle, relative: boolean) -> None:
    """Synopsis:
---
---
 roll(
[camera]
    , [absolute=boolean], [degree=angle], [relative=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

roll is undoable, NOT queryable, and NOT editable.
The default mode is relative and the rotation is applied with
respect to the current orientation of the camera. When mode is set
to absolute, the rotation is applied with respect to the plane
constructed from the following three vectors in the world space:
the world up vector, the camera view vector, and the camera up
vector.

The rotation angle is specified in degrees.

The roll command can be applied to either a perspective or an
orthographic camera.

This command may be applied to more than one camera; objects that
are not cameras are ignored. When no camera name supplied, this command
is applied to all currently active cameras.




Example:
---
import maya.cmds as cmds

cmds.camera()

Align the horizontal direction with the world horizon
cmds.roll( 'cameraShape1', abs=True, d=0 )

Roll the camera 15 degrees clockwise
cmds.roll( 'cameraShape1', d=15 )

cmds.roll( d=15 )

---


Flags:
---


---
absolute(abs): boolean
    properties: create
    Set to absolute mode.

---
degree(d): angle
    properties: create
    Set the amount of the rotation angle.

---
relative(rel): boolean
    properties: create
    Set to relative mode.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/roll.html 
    """


def rollCtx(alternateContext: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, rollScale: float, toolName: string) -> string:
    """Synopsis:
---
---
 rollCtx(
[context]
    , [alternateContext=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [rollScale=float], [toolName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rollCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.rollCtx( 'rollContext', rs=30.0 )

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
rollScale(rs): float
    properties: create, query, edit
    In degrees of rotation per 100 pixels of cursor drag.

---
toolName(tn): string
    properties: create, query
    Name of the specific tool to which this command refers.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rollCtx.html 
    """


def rotate(absolute: boolean, centerPivot: boolean, componentSpace: boolean, constrainAlongNormal: boolean, deletePriorHistory: boolean, euler: boolean, forceOrderXYZ: boolean, objectCenterPivot: boolean, objectSpace: boolean, orientAxes: tuple[angle, angle, angle], pivot: tuple[linear, linear, linear], preserveChildPosition: boolean, preserveGeometryPosition: boolean, preserveUV: boolean, reflection: boolean, reflectionAboutBBox: boolean, reflectionAboutOrigin: boolean, reflectionAboutX: boolean, reflectionAboutY: boolean, reflectionAboutZ: boolean, reflectionTolerance: float, relative: boolean, rotateX: boolean, rotateXY: boolean, rotateXYZ: boolean, rotateXZ: boolean, rotateY: boolean, rotateYZ: boolean, rotateZ: boolean, symNegative: boolean, translate: boolean, worldSpace: boolean, xformConstraint: string) -> None:
    """Synopsis:
---
---
 rotate(
float float float [objects]
    , [absolute=boolean], [centerPivot=boolean], [componentSpace=boolean], [constrainAlongNormal=boolean], [deletePriorHistory=boolean], [euler=boolean], [forceOrderXYZ=boolean], [objectCenterPivot=boolean], [objectSpace=boolean], [orientAxes=[angle, angle, angle]], [pivot=[linear, linear, linear]], [preserveChildPosition=boolean], [preserveGeometryPosition=boolean], [preserveUV=boolean], [reflection=boolean], [reflectionAboutBBox=boolean], [reflectionAboutOrigin=boolean], [reflectionAboutX=boolean], [reflectionAboutY=boolean], [reflectionAboutZ=boolean], [reflectionTolerance=float], [relative=boolean], [rotateX=boolean], [rotateXY=boolean], [rotateXYZ=boolean], [rotateXZ=boolean], [rotateY=boolean], [rotateYZ=boolean], [rotateZ=boolean], [symNegative=boolean], [translate=boolean], [worldSpace=boolean], [xformConstraint=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rotate is undoable, NOT queryable, and NOT editable.
The default behaviour, when no objects or flags are passed,
is to do a absolute rotate on each currently selected object
in the world space.




Example:
---
import maya.cmds as cmds

create a circle and grouped cone to rotate;
cmds.circle( n='circle1' )
cmds.cone( ax=(0, 1, 0), n='cone1' )
cmds.group( 'cone1', n='group1' )

rotate the active objects 45 degrees about the world space X axis
centered at each object's rotate pivot point.
cmds.select( 'cone1' )
cmds.rotate( '45deg', 0, 0, r=True )

Set the rotation values for group1 to (90, 0, 0). This is
equivalent to:
  cmds.setAttr('group1.rx',90)
  cmds.setAttr('group1.ry',0)
  cmds.setAttr('group1.rz',0)
cmds.rotate( '90deg', 0, 0, 'group1' )

rotate the circle 180 degrees about its local space Y axis
centered at the rotate pivot point 1 0 0.
cmds.rotate( 0, '180deg', 0, 'circle1', pivot=(1, 0, 0) )

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
    Rotate in local component space

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
euler(eu): boolean
    properties: create
    Modifer for -relative flag that specifies rotation
values should be added to current XYZ rotation values.

---
forceOrderXYZ(fo): boolean
    properties: create
    When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.

---
objectCenterPivot(ocp): boolean
    properties: create
    Let the pivot be the center of the bounding box of each object

---
objectSpace(os): boolean
    properties: create
    Perform rotation about object-space axis.

---
orientAxes(oa): [angle, angle, angle]
    properties: create
    Euler axis for orientation.

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
    When true, UV values on rotated components are projected across the rotation
in 3d space. For small edits, this will freeze the world space texture mapping
on the object.
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
rotateX(x): boolean
    properties: create
    Rotate in X direction

---
rotateXY(xy): boolean
    properties: create
    Rotate in X and Y direction

---
rotateXYZ(xyz): boolean
    properties: create
    Rotate in all directions (default)

---
rotateXZ(xz): boolean
    properties: create
    Rotate in X and Z direction

---
rotateY(y): boolean
    properties: create
    Rotate in Y direction

---
rotateYZ(yz): boolean
    properties: create
    Rotate in Y and Z direction

---
rotateZ(z): boolean
    properties: create
    Rotate in Z direction

---
symNegative(smn): boolean
    properties: create
    When set the component transformation is flipped so it is relative to the
negative side of the symmetry plane. The default (no flag) is to transform
components relative to the positive side of the symmetry plane.

---
translate(t): boolean
    properties: create
    When true, the command will modify the node's translate attribute instead of its
rotateTranslate attribute, when rotating around a pivot other than the object's
own rotate pivot.

---
worldSpace(ws): boolean
    properties: create
    Perform rotation about global world-space axis.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rotate.html 
    """


def rotationInterpolation(convert: string) -> None:
    """Synopsis:
---
---
 rotationInterpolation([convert=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rotationInterpolation is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


Converts "nurbsCone1_rotateX" and its sibling curves to quaternion tangent dependent format.
cmds.rotationInterpolation( 'nurbsCone1_rotateX', convert='quaternion' )

---


Flags:
---


---
convert(c): string
    properties: create, query
    Specifies the rotation interpolation mode for the curves after converting.
Possible choices are "none" (unsynchronized Euler-angled curves which are
compatible with pre-4.0 Maya curves), "euler" (Euler-angled curves with
keyframes kept synchronized), "quaternion" (quaternion curves with
keyframes kept synchronized, but the exact interpolation depends on
individual tangents),  "quaternionSlerp" (applies quaternion slerp interpolation
to the curve, ignoring tangent settings), "quaternionSquad" (applied cubic interpolation
to the curve in quaternion space, ignoring tangent settings)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rotationInterpolation.html 
    """


def roundConstantRadius(append: boolean, constructionHistory: boolean, name: string, object: boolean, radiuss: linear, side: tuple[string, int], sidea: int, sideb: int) -> list[string]:
    """Synopsis:
---
---
 roundConstantRadius(
string string [string string]
    , [append=boolean], [constructionHistory=boolean], [name=string], [object=boolean], [radiuss=linear], [side=[string, int]], [sidea=int], [sideb=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

roundConstantRadius is undoable, queryable, and editable.compound
The results from this command are three surface var groups plus the
name of the new roundConstantRadius dependency node, if history was on.
The 1st var group contains trimmed copies of the original surfaces.  The 2nd
var group contains the new NURBS fillet surfaces.  The 3rd var group
contains the new NURBS corners (if any).

A simple example of an edge pair is an edge of a NURBS cube,
where two faces of the cube meet.  This command generates a NURBS
fillet at the edge and trims back the faces.

Another example is a NURBS cylinder with a planar trim surface cap.
This command will create a NURBS fillet where the cap meets the
the cylinder and will trim back the cap and the cylinder.

Another example involves all 12 edges of a NURBS cube.  NURBS fillets
are created where any face meets another face.  NURBS corners are
created whenever 3 edges meet at a corner.




Example:
---
import maya.cmds as cmds

This rounds four edges of a cube with radius 0.9.  Because a single
radius is specified, it is used for all edges.  The edges must
be specified in matching pairs if no "sidea" or "sideb" flags
are used.
---

cube = cmds.nurbsCube(w=5, lr=1, hr=1, d=3, ch=0)
sides = cmds.listRelatives( cube[0], c=True )
rnd = cmds.roundConstantRadius(
    (sides[0] + ".v[0]"), (sides[2] + ".v[1]"),
    (sides[0] + ".u[1]"), (sides[4] + ".v[1]"),
    (sides[0] + ".v[1]"), (sides[3] + ".u[1]"),
    (sides[0] + ".u[0]"), (sides[5] + ".u[1]"),
    rad=0.9 )

This adds a pair of isoparms to an existing round operation,
named $rnd[3] (from previous example)
---

cmds.roundConstantRadius( (sides[3] + '.v[0]'), (sides[5] + '.v[1]'),
                          rnd[3], append=True, rad=0.8 )

This rounds 6 edges of a cube with different radius values.
The first four edges have radius 0.9 and the others have radius 1.1.
In this case the edges are specified in matching pairs
since no "sidea" or "sideb" flags are used.
---

cube = cmds.nurbsCube( w=5, lr=1, hr=1, d=3, ch=0 )
sides = cmds.listRelatives( cube[0], c=True )
cmds.roundConstantRadius( (sides[0]+".v[0]"), (sides[2]+".v[1]"),
                          (sides[0]+".u[1]"), (sides[4]+".v[1]"),
                          (sides[0]+".v[1]"), (sides[3]+".u[1]"),
                          (sides[0]+".u[0]"), (sides[5]+".u[1]"),
                          (sides[3]+".v[0]"), (sides[5]+".v[1]"),
                          (sides[2]+".u[1]"), (sides[4]+".u[0]"),
                          rad=[0.9, 0.9, 0.9, 0.9, 1.1, 1.1] )

This rounds a 2-to-1 compound edge.  The sidea flag indicates
that there two edges on side A, and one on side B.
The edges must be specified in the corresponding order.
---

pln1 = cmds.nurbsPlane(w=5, ch=0, ax=(0, 1, 0))
pln2 = cmds.nurbsPlane( p=(2.5, 2.5, 1.25), ax=(1, 0, 0), w=2.5, lr=2, d=3, u=1, v=1, ch=0 )
pln3 = cmds.nurbsPlane( p=(2.5, 2.5, -1.25), ax=(1, 0, 0), w=2.5, lr=2, d=3, u=1, v=1, ch=0 )
pln4 = cmds.nurbsPlane( p=(0, 2.5, -2.5), ax=(0, 0, 1), w=5, lr=1, d=3, u=1, v=1, ch=0 )
cmds.roundConstantRadius( (pln2[0]+'.v[0]'), (pln3[0]+'.v[0]'),
                          (pln1[0]+'.u[1]'), (pln3[0]+'.u[1]'),
                          (pln4[0]+'.u[1]'), rad=0.9,
                          side=[('a',2), ('b', 1), ('a', 1), ('b', 1)] )

---
Return:
---


    list[string]: (resulting NURBS surfaces' names and node name)

Flags:
---


---
append(a): boolean
    properties: create
    If true, then an edge pair is being added to an existing
round dependency node.  Default is false.
When this flag is true, an existing round dependency node
must be specified. See example below.

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
radiuss(rad): linear
    properties: create, multiuse
    Use this flag to specify radius.  This overrides the
"r/radius" flag.  If only one "rad" flag is used,
then it is applied to all edge pairs.  If more than one "rad" flag is used,
then the number of "-rad" flags must equal the number
of edge pairs.  For example, for four edge pairs,
zero, one or four "rad" flags must be specified.

---
side(s): [string, int]
    properties: create, multiuse
    Use this flag for compound edges.  It replaces the sidea/sideb flags and is
compatible with Python.

The first argument must be either "a" or "b".

The same number of "a" values as "b" values must be specified.
If no sides are specified with the "side" flag (or sidea/sideb flags), then
the edges are assumed to be in pairs.
See also examples below.
For example, two faces of a cube meet at an edge pair.
Suppose one of the faces is then split in two pieces
at the middle of the edge, so that there is one
face on side "A", and two pieces on side "B".  In this case
the flag combination: -side "a" 1 -side "b" 2 would be used.
The edges must be specified in the corresponding order:
// MEL
roundConstantRadius -side "a" 1 -side "b" 2 isoA isoB1 isoB2;
# Python
maya.cmds.roundConstantRadius( 'isoA', 'isoB1', 'isoB2', side=[("a",1), ("b",2)] )

---
sidea(sa): int
    properties: create, multiuse
    Use this flag for compound edges in conjunction with the
following "-sb" flag.

This flag is not intended for use from Python.  Please see "side" flag instead.

The same number of "-sa" flags as "-sb" flags must be specified.
If no "-sa" nor "-sb" flags are specified, then the edges
are assumed to be in pairs.
See also examples below.
For example, two faces of a cube meet at an edge pair.
Suppose one of the faces is then split in two pieces
at the middle of the edge, so that there is one
face on side "A", and two pieces on side "B".  In this case,
the flag combination: -sidea 1 -sideb 2 would be used.
The edges must be specified in the corresponding order:
roundConstantRadius -sidea 1 -sideb 2 isoA isoB1 isoB2;

---
sideb(sb): int
    properties: create, multiuse
    Use this flag for compound edges in conjunction with the
"-sa" flag.  See description for the "-sa" flag.

This flag is not intended for use from Python.  Please see "side" flag instead.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/roundConstantRadius.html 
    """


def rowColumnLayout(adjustableColumn: int, annotation: string, backgroundColor: tuple[float, float, float], childArray: boolean, columnAlign: tuple[int, string], columnAttach: tuple[int, string, int], columnOffset: tuple[int, string, int], columnSpacing: tuple[int, int], columnWidth: tuple[int, int], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, generalSpacing: int, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, margins: int, noBackground: boolean, numberOfChildren: boolean, numberOfColumns: int, numberOfPopupMenus: boolean, numberOfRows: int, parent: string, popupMenuArray: boolean, preventOverride: boolean, rowAlign: tuple[int, string], rowAttach: tuple[int, string, int], rowHeight: tuple[int, int], rowOffset: tuple[int, string, int], rowSpacing: tuple[int, int], statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 rowColumnLayout(
[string]
    , [adjustableColumn=int], [annotation=string], [backgroundColor=[float, float, float]], [childArray=boolean], [columnAlign=[int, string]], [columnAttach=[int, string, int]], [columnOffset=[int, string, int]], [columnSpacing=[int, int]], [columnWidth=[int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfColumns=int], [numberOfPopupMenus=boolean], [numberOfRows=int], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAlign=[int, string]], [rowAttach=[int, string, int]], [rowHeight=[int, int]], [rowOffset=[int, string, int]], [rowSpacing=[int, int]], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rowColumnLayout is undoable, queryable, and editable.-nc/numberOfColumns-nr/numberOfRows
Some flags only make sense for one of either the row format or the
column format.  For example the -rh/rowHeight flag can only be
specified in row format. In column format the row height is
determined by the tallest child in the row, plus offsets.




Example:
---
import maya.cmds as cmds

   The following script will position the buttons in a single column.
---

   +----+
   | b1 |
   +----+
   +----+
   | b2 |
   +----+
   +----+
   | b3 |
   +----+
---

cmds.window()
cmds.rowColumnLayout( numberOfColumns=1 )
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow()

   The following script will position the buttons in a single row.
---

   +----++----++----+
   | b1 || b2 || b3 |
   +----++----++----+
---

cmds.window()
cmds.rowColumnLayout( numberOfRows=1 )
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow()

   The following script will position the buttons in 3 columns, each
   column a different width.
---

   +----++--------++------------+
   | b1 ||   b2   ||     b3     |
   +----++--------++------------+
   +----++--------++------------+
   | b4 ||   b5   ||     b6     |
   +----++--------++------------+
   +----+
   | b7 |
   +----+
---

cmds.window()
cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 60), (2, 80), (3, 100)] )
cmds.button()
cmds.button()
cmds.button()
cmds.button()
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow()

   The following script will position the buttons in 2 rows, each
   row a different height.
---

   +----++----++----++----+
   | b1 || b3 || b5 || b7 |
   +----++----++----++----+
   +----++----++----+
   |    ||    ||    |
   | b2 || b4 || b6 |
   |    ||    ||    |
   +----++----++----+
---

cmds.window()
cmds.rowColumnLayout( numberOfRows=2, rowHeight=[(1, 30), (2, 60)] )
cmds.button()
cmds.button()
cmds.button()
cmds.button()
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
adjustableColumn(adj): int
    properties: create, edit
    Specifies which column has an adjustable size that changes
with the sizing of the layout.

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
columnAlign(cal): [int, string]
    properties: create, edit, multiuse
    Alignment for text and pixmaps in the specified
column.  Values are: "left", "right" and "center".  Only valid
for column format, ie. number of columns specified
with -nc/numberOfColumns flag.

---
columnAttach(cat): [int, string, int]
    properties: create, edit, multiuse
    The attachments and offsets for the children in
the specified column.  The first argument is the 1-based column
index.  The second argument is the attachment, valid values are
"left", "right" and "both".  The third argument must be greater
than 0 and specifies the offset.

---
columnOffset(co): [int, string, int]
    properties: create, edit, multiuse
    The attachment offset for the specified column.  The first
argument is the 1-based column index.  The second argument is the
attachment, valid values are "left", "right" and "both".  The
third argument must be greater than 0 and specifies the offset.

---
columnSpacing(cs): [int, int]
    properties: create, edit, multiuse
    The space between columns in pixels.  In column format
this flag specifies that the space be to the left of the
given column.  In row format it specifies the space between all
columns, however a valid column index is still required.  The
first argument is the 1-based column index.  The second argument
must be greater than 0 and specifies the spacing.

---
columnWidth(cw): [int, int]
    properties: create, edit, multiuse
    Width of a column. This flag is valid only in column
format.  The column width must be greater than 0.  The first
argument is the 1-based column index.  The second argument must
be greater than 0 and specifies the column width.

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
numberOfColumns(nc): int
    properties: create, query
    Number of columns. This flag is mutually exclusive to
the -nr/numRows flag.  Either one or the other can be
specified.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
numberOfRows(nr): int
    properties: create, query
    Number of rows. This flag is mutually exclusive to
the -nc/numColumns flag. Either one or the other can be
specified.

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
rowAlign(ral): [int, string]
    properties: create, edit, multiuse
    Alignment for text and pixmaps in the specified row.
Values are: "left", "right" and "center".  Only valid for
row format, ie. number of rows specified
with -nr/numberOfRows flag.

---
rowAttach(rat): [int, string, int]
    properties: create, edit, multiuse
    The attachments and offsets for the children in
the specified row.  The first argument is the 1-based row
index.  The second argument is the attachment, valid values are
"top", "bottom" and "both".  The third argument must be greater
than 0 and specifies the offset.

---
rowHeight(rh): [int, int]
    properties: create, edit, multiuse
    Height of a row. This flag is only valid in row format.
The row height must be greater than 0. The first
argument is the 1-based row index.  The second argument must
be greater than 0 and specifies the row height.

---
rowOffset(ro): [int, string, int]
    properties: create, edit, multiuse
    The attachment offset for the specified row.  The first
argument is the 1-based row index.  The second argument is the
attachment, valid values are "top", "bottom" and "both".  The
third argument must be greater than 0 and specifies the offset.

---
rowSpacing(rs): [int, int]
    properties: create, edit, multiuse
    The space between rows, in pixels.  In row format this
specifies the space above the specified row.  In
column format it specifies the space between all rows, however
a valid row index is still required.  The first argument is the
1-based row index.  The second argument must be greater than 0 and
specifies the spacing.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rowColumnLayout.html 
    """


def rowLayout(adjustableColumn: int, adjustableColumn1: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, backgroundColor: tuple[float, float, float], childArray: boolean, columnAlign: tuple[int, string], columnAlign1: string, columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach1: string, columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset1: int, columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, generalSpacing: int, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, margins: int, noBackground: boolean, numberOfChildren: boolean, numberOfColumns: int, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, rowAttach: tuple[int, string, int], statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 rowLayout(
[string]
    , [adjustableColumn=int], [adjustableColumn1=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [childArray=boolean], [columnAlign=[int, string]], [columnAlign1=string], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach1=string], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset1=int], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfColumns=int], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

rowLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Layout a label, field and slider such that the label is right
   justified and the field adjusts in size as the window is resized.
---

cmds.window()
cmds.rowLayout( numberOfColumns=3, columnWidth3=(80, 75, 150), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
cmds.text()
cmds.intField()
cmds.intSlider()
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
adjustableColumn(adj): int
    properties: create, edit, multiuse
    Specifies which column has an adjustable size that changes
with the sizing of the layout.

---
adjustableColumn1(ad1): int
    properties: create
    Specifies that the first column has an adjustable size that
changes with the size of the parent layout.
Ignored if there isn't exactly one column.

---
adjustableColumn2(ad2): int
    properties: create
    Specifies which of the two columns has an adjustable size
that changes with the size of the parent layout.
Ignored if there isn't exactly two columns.

---
adjustableColumn3(ad3): int
    properties: create
    Specifies which of the three columns has an adjustable size
that changes with the size of the parent layout.
Ignored if there isn't exactly three columns.

---
adjustableColumn4(ad4): int
    properties: create
    Specifies which of the four columns has an adjustable size
that changes with the size of the parent layout.
Ignored if there isn't exactly four columns.

---
adjustableColumn5(ad5): int
    properties: create
    Specifies which of the five columns has an adjustable size
that changes with the size of the parent layout.
Ignored if there isn't exactly five columns.

---
adjustableColumn6(ad6): int
    properties: create
    Specifies which of the six columns has an adjustable size
that changes with the size of the parent layout.
Ignored if there isn't exactly six columns.

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
columnAlign(cal): [int, string]
    properties: create, edit, multiuse
    Text alignment for the specified column.
Valid values are "left", "right", and "center"

---
columnAlign1(cl1): string
    properties: create
    Text alignment for the first column.
Valid values are "left", "right", and "center".
Ignored if there isn't exactly one column.

---
columnAlign2(cl2): [string, string]
    properties: create
    Text alignment for both columns.
Valid values are "left", "right", and "center".
Ignored if there isn't exactly two columns.

---
columnAlign3(cl3): [string, string, string]
    properties: create
    Text alignment for all three columns.
Valid values are "left", "right", and "center".
Ignored if there isn't exactly three columns.

---
columnAlign4(cl4): [string, string, string, string]
    properties: create
    Text alignment for all four columns.
Valid values are "left", "right", and "center".
Ignored if there isn't exactly four columns.

---
columnAlign5(cl5): [string, string, string, string, string]
    properties: create
    Text alignment for all five columns.
Valid values are "left", "right", and "center".
Ignored if there isn't exactly five columns.

---
columnAlign6(cl6): [string, string, string, string, string, string]
    properties: create
    Text alignment for all six columns.
Valid values are "left", "right", and "center".
Ignored if there isn't exactly six columns.

---
columnAttach(cat): [int, string, int]
    properties: create, edit, multiuse
    Horizontally attach a particular column.  The first
argument is a 1-based index specifying the column.  The second
argument is the attachment, valid values are "left", "right",
and "both".  The third argument is the offset value.

---
columnAttach1(ct1): string
    properties: create
    Attachment type for the first column.  Ignored if there isn't
exactly one column. Valid values are "left", "right", and "both".

---
columnAttach2(ct2): [string, string]
    properties: create
    Attachment type for both columns.  Ignored if there isn't
exactly two columns. Valid values are "left", "right", and "both".

---
columnAttach3(ct3): [string, string, string]
    properties: create
    Attachment type for all three columns.  Ignored if there
isn't exactly three columns. Valid values are "left", "right",
and "both".

---
columnAttach4(ct4): [string, string, string, string]
    properties: create
    Attachment type for all four columns.  Ignored if there isn't
exactly four columns. Valid values are "left", "right", and "both".

---
columnAttach5(ct5): [string, string, string, string, string]
    properties: create
    Attachment type for all five columns.  Ignored if there isn't
exactly five columns. Valid values are "left", "right", and "both".

---
columnAttach6(ct6): [string, string, string, string, string, string]
    properties: create
    Attachment type for all six columns.  Ignored if there isn't
exactly six columns. Valid values are "left", "right", and "both".

---
columnOffset1(co1): int
    properties: create
    Used in conjunction with the -columnAttach1 flag.  If that
flag is not used then this flag will be ignored.  Sets the offset
for the first column.  The offsets applied are based on the
attachments specified with the -columnAttach1 flag.
Ignored if there isn't exactly one column.

---
columnOffset2(co2): [int, int]
    properties: create
    Used in conjunction with the -columnAttach2 flag.  If that
flag is not used then this flag will be ignored.  Sets the offset
for both columns.  The offsets applied are based on the
attachments specified with the -columnAttach2 flag.
Ignored if there isn't exactly two columns.

---
columnOffset3(co3): [int, int, int]
    properties: create
    Used in conjunction with the -columnAttach3 flag.  If that
flag is not used then this flag will be ignored.  Sets the offset
for all three columns.  The offsets applied are based on the
attachments specified with the -columnAttach3 flag.
Ignored if there isn't exactly three columns.

---
columnOffset4(co4): [int, int, int, int]
    properties: create
    Used in conjunction with the -columnAttach4 flag.  If that
flag is not used then this flag will be ignored.  Sets the offset
for all four columns.  The offsets applied are based on the
attachments specified with the -columnAttach4 flag.
Ignored if there isn't exactly four columns.

---
columnOffset5(co5): [int, int, int, int, int]
    properties: create
    Used in conjunction with the -columnAttach5 flag.  If that
flag is not used then this flag will be ignored.  Sets the offset
for all five columns.  The offsets applied are based on the
attachments specified with the -columnAttach5 flag.
Ignored if there isn't exactly five columns.

---
columnOffset6(co6): [int, int, int, int, int, int]
    properties: create
    Used in conjunction with the -columnAttach6 flag.  If that
flag is not used then this flag will be ignored.  Sets the offset
for all six columns.  The offsets applied are based on the
attachments specified with the -columnAttach6 flag.
Ignored if there isn't exactly six columns.

---
columnWidth(cw): [int, int]
    properties: create, edit, multiuse
    Width of a particular column.  The first argument is a
1-based index specifying the column.  The second argument is the
width value.

---
columnWidth1(cw1): int
    properties: create
    Width for the first column.  Ignored if there isn't exactly
one column.

---
columnWidth2(cw2): [int, int]
    properties: create
    Widths for both columns.  Ignored if there isn't
exactly two columns.

---
columnWidth3(cw3): [int, int, int]
    properties: create
    Widths for all three columns.  Ignored if there isn't
exactly three columns.

---
columnWidth4(cw4): [int, int, int, int]
    properties: create
    Widths for all four columns.  Ignored if there isn't
exactly four columns.

---
columnWidth5(cw5): [int, int, int, int, int]
    properties: create
    Widths for all five columns.  Ignored if there isn't
exactly five columns.

---
columnWidth6(cw6): [int, int, int, int, int, int]
    properties: create
    Widths for all six columns.  Ignored if there isn't
exactly six columns.

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
numberOfColumns(nc): int
    properties: create, query
    Number of columns in the row.  The specified number of
columns must be a value greater than 0.

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
    Vertically attach a particular column.  The first argument
is a 1-based index specifying the column.  The second argument is
the attachment, valid values are "top", "bottom", and "both".  The
third argument is the offset value.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/rowLayout.html 
    """


def runTimeCommand(addKeyword: string, addTag: string, annotation: string, category: string, categoryArray: boolean, command: script, commandArray: boolean, commandLanguage: string, default: boolean, defaultCommandArray: boolean, delete: boolean, exists: boolean, helpUrl: string, hotkeyCtx: string, image: string, keywords: string, label: string, longAnnotation: string, numberOfCommands: boolean, numberOfDefaultCommands: boolean, numberOfUserCommands: boolean, plugin: string, save: boolean, showInHotkeyEditor: boolean, tags: string, userCommandArray: boolean) -> string:
    """Synopsis:
---
---
 runTimeCommand(
name
    , [addKeyword=string], [addTag=string], [annotation=string], [category=string], [categoryArray=boolean], [command=script], [commandArray=boolean], [commandLanguage=string], [default=boolean], [defaultCommandArray=boolean], [delete=boolean], [exists=boolean], [helpUrl=string], [hotkeyCtx=string], [image=string], [keywords=string], [label=string], [longAnnotation=string], [numberOfCommands=boolean], [numberOfDefaultCommands=boolean], [numberOfUserCommands=boolean], [plugin=string], [save=boolean], [showInHotkeyEditor=boolean], [tags=string], [userCommandArray=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

runTimeCommand is undoable, queryable, and editable.command
Note that the resulting command takes no arguments, has no flags and
may not be queried or edited.

The command name you provide must be unique. The name itself must
begin with an alphabetic character or underscore followed by
alphanumeric characters or underscores.

If you create your run time commands in a script which is automatically
sourced at startup then set the default flag to true.  This
will prevent the application from attempting to save these commands.




Example:
---
import maya.cmds as cmds

   Create a command that simply prints a message.  After executing
   the following lines enter the command name <i>MyHelloCommand</i>
   in the Command Line.
---

if maya.cmds.runTimeCommand( 'MyHelloCommand', exists=True ):
    cmds.runTimeCommand( annotation='Print the word "Hello"', command='print "Hello\\n"', MyHelloCommand )

   Create a window with a button that invokes the <i>MyHelloCommand</i>
   command.
---

cmds.window()
cmds.paneLayout()
Some commands support different language source types. Since the button command does not, it
assumes Python and the command has to be explicitly forwarded to MEL, which is what the runTimeCommand creates.
cmds.button( command='import maya.mel; mel.eval("MyHelloCommand")' )
cmds.showWindow();

---
Return:
---


    string: The name of the command on.

Flags:
---


---
addKeyword(ak): string
    properties: create, edit, multiuse
    Append one keyword to the keyboard list, which is used by the Search user interface

---
addTag(at): string
    properties: create, edit, multiuse
    Append one keyword to the tag list, which is used by the Search user interface

---
annotation(ann): string
    properties: create, query, edit
    Description of the command.

---
category(cat): string
    properties: create, query, edit
    Category for the command.

---
categoryArray(caa): boolean
    properties: query
    Return all the run time command categories.

---
command(c): script
    properties: create, query, edit
    Command to be executed when runTimeCommand is invoked.

---
commandArray(ca): boolean
    properties: query
    Returns an string array containing the names of all the run
time commands.

---
commandLanguage(cl): string
    properties: create, query, edit
    In edit or create mode, this flag allows the caller to choose a scripting
language for a command passed to the "-command" flag.  If this flag is not
specified, then the callback will be assumed to be in the language from which
the runTimeCommand command was called.  In query mode, the language for this
runTimeCommand is returned.  The possible values are "mel" or "python".

---
default(d): boolean
    properties: create, query
    Indicate that this run time command is a default command.
Default run time commands will not be saved to preferences.

---
defaultCommandArray(dca): boolean
    properties: query
    Returns an string array containing the names of all the
default run time commands.

---
delete(delete): boolean
    properties: edit
    Delete the specified user run time command.

---
exists(ex): boolean
    properties: create
    Returns true|false depending upon whether the specified object
exists. Other flags are ignored.

---
helpUrl(url): string
    properties: create, query, edit
    Custom URL for the online documentation of this command. Used in the Search user interface.

---
hotkeyCtx(hc): string
    properties: create, query, edit
    hotkey Context for the command.

---
image(i): string
    properties: create, query, edit
    Image filename for the command.

---
keywords(k): string
    properties: create, query, edit
    Keywords for the command. Used for searching for commands in the Search user interface.
When multiple keywords, use ; as a separator. (Example: "keyword1;keyword2")

---
label(l): string
    properties: create, query, edit
    Label for the command.

---
longAnnotation(la): string
    properties: create, query, edit
    Extensive, multi-line description of the command.
This will show up in the Search user interface's 'more info' page in addition to the annotation.

---
numberOfCommands(nc): boolean
    properties: query
    Return the number of run time commands.

---
numberOfDefaultCommands(ndc): boolean
    properties: query
    Return the number of default run time commands.

---
numberOfUserCommands(nuc): boolean
    properties: query
    Return the number of user run time commands.

---
plugin(p): string
    properties: create, query, edit
    Name of the plugin this command requires to be loaded.
This flag wraps the script provided into a safety check and automatically loads the
plugin referenced on execution if it hasn't been loaded.
If the plugin fails to load, the command won't be executed.

---
save(s): boolean
    properties: edit
    Save all the user run time commands.

---
showInHotkeyEditor(she): boolean
    properties: create, query, edit
    Indicate that this run time command should be shown in the Hotkey Editor.
Default value is true.

---
tags(t): string
    properties: create, query, edit
    Tags for the command. Used for grouping commands in the Search user interface.
When more than one tag, use ; as a separator. (Example: "tag1;tag2")

---
userCommandArray(uca): boolean
    properties: query
    Returns an string array containing the names of all the
user run time commands.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/runTimeCommand.html 
    """


def runup(cache: boolean, fromPreviousFrame: boolean, fromStartFrame: boolean, maxFrame: time, state: boolean) -> string:
    """Synopsis:
---
---
 runup([cache=boolean], [fromPreviousFrame=boolean], [fromStartFrame=boolean], [maxFrame=time], [state=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

runup is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.runup( mxf=10, cache=True )

Starts at the minimum start frame of all dynamic objects
and plays through to frame 10.  This guarantees that the system
is in the same state it would be as if you had rewound and played
forward from frame 0.  The state of the dynamic object(s) will be
cached after the runup.

---
Return:
---


    string: Command result

Flags:
---


---
cache(cch): boolean
    properties: create
    Cache the state after the runup.

---
fromPreviousFrame(fpf): boolean
    properties: create
    Run up the animation from the previously evaluated frame.
If no flag is supplied this is the default.

---
fromStartFrame(fsf): boolean
    properties: create
    Run up the animation from the start frame.
If no flag is supplied -fromPreviousFrame is the default.

---
maxFrame(mxf): time
    properties: create
    Ending time for runup, in current user time units.
The runup will always start at the
minimum start frame for all dynamic objects.

---
state(st): boolean
    properties: create
    Turns runup and cache on/off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/runup.html 
    """
