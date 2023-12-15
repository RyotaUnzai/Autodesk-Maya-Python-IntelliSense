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


def lassoContext(flagdrawClosed: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 lassoContext(
string
    , [drawClosed=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lassoContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a new lasso context, then switch to it
cmds.lassoContext('lassoContext1')
cmds.setToolTo('lassoContext1')

---
Return:
---


    string: Name of the context created

Flags:
---


---
drawClosed(dc): boolean
    properties: create, query, edit
    Turns the closed display of the lasso on/off.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lassoContext.html 
    """


def lattice(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcommonParent: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagdivisions: tuple[uint, uint, uint], flagdualBase: boolean, flagexclusive: string, flagfreezeMapping: boolean, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flaglatticeReset: boolean, flagldivisions: tuple[uint, uint, uint], flagminimumSize: float, flagname: string, flagobjectCentered: boolean, flagoutsideFalloffDistance: float, flagoutsideLattice: uint, flagparallel: boolean, flagposition: tuple[linear, linear, linear], flagprune: boolean, flagremove: boolean, flagremoveTweaks: boolean, flagrotation: tuple[angle, angle, angle], flagscale: tuple[linear, linear, linear], flagselectedComponents: boolean, flagsplit: boolean, flaguseComponentTags: boolean) -> list[string]:
    """Synopsis:
---
---
 lattice(
selectionList
    , [after=boolean], [afterReference=boolean], [before=boolean], [commonParent=boolean], [components=boolean], [deformerTools=boolean], [divisions=[uint, uint, uint]], [dualBase=boolean], [exclusive=string], [freezeMapping=boolean], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [latticeReset=boolean], [ldivisions=[uint, uint, uint]], [minimumSize=float], [name=string], [objectCentered=boolean], [outsideFalloffDistance=float], [outsideLattice=uint], [parallel=boolean], [position=[linear, linear, linear]], [prune=boolean], [remove=boolean], [removeTweaks=boolean], [rotation=[angle, angle, angle]], [scale=[linear, linear, linear]], [selectedComponents=boolean], [split=boolean], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lattice is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

to create a 4x5x4 lattice centered around the sphere
---

cmds.sphere();
cmds.lattice( dv=(4, 5, 4), oc=True )

to edit the lattice divisions to be 6x6x6
---

cmds.lattice( 'ffd1', e=True, dv=(6, 6, 6) )

move a point on the lattice
cmds.select('ffd1Lattice.pt[2][2][5]',r=True)
cmds.move(0,0,3,r=True)

to reset the lattice
---

cmds.lattice( 'ffd1', e=True, lr=True )

---
Return:
---


    list[string]: Ffd node name, lattice name, base lattice name.

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
commonParent(cp): boolean
    properties: create
    Group the base lattice and the deformed lattice under
a common transform. This means that you can resize the lattice
without affecting the deformation by resizing the common
transform.

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
divisions(dv): [uint, uint, uint]
    properties: create, query, edit
    Set the number of lattice slices in x, y, z. Default
is 2, 5, 2. When queried, this flag returns float float float.
When you change the number of divisions, any tweaking or
animation of lattice points must be redone.

---
dualBase(db): boolean
    properties: create
    Create a special purpose ffd deformer node which
accepts 2 base lattices. The default is off which results
in the creation of a normal ffd deformer node.
Intended for internal usage only.

---
exclusive(ex): string
    properties: create, query
    Puts the deformation set in a deform partition.

---
freezeMapping(fm): boolean
    properties: create, query, edit
    The base position of the geometries points is fixed
at the time this flag is set.  When mapping is frozen, moving
the geometry with respect to the lattice will not cause the
deformation to be recomputed.

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
latticeReset(lr): boolean
    properties: edit
    Reset the lattice to match its base position. This will
undo any deformations that the lattice is causing. The lattice
will only deform points that are enclosed within the lattice's
reset (base) position.

---
ldivisions(ldv): [uint, uint, uint]
    properties: create, query, edit
    Set the number of local lattice slices in x, y, z.

---
minimumSize(mns): float
    properties: create
    Set the minimum size of a side of the lattice during creation
using the objectCentered flag which causes the lattice size to
be determined from the geometry that is being deformed.
When f.e. the object is a flat plane this can avoid the lattice
to have size 0.0 along one side.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
objectCentered(oc): boolean
    properties: create
    Centers the lattice around the selected object(s) or
components. Default is off which centers the
lattice at the origin.

---
outsideFalloffDistance(ofd): float
    properties: create
    Set the falloff distance used when the setting for
transforming points outside of the base lattice is set to 2.
The distance value is a positive number which specifies the
size of the falloff distance as a multiple of the base lattice
size, thus a value of 1.0 specifies that only points up to
the base lattice width/height/depth away are transformed.
A value of 0.0 is equivalent to an outsideLattice value of
0 (i.e. no points outside the base lattice are transformed).
A huge value is equivalent to transforming an outsideLattice
value of 1 (i.e. all points are transformed).

---
outsideLattice(ol): uint
    properties: create
    Set the mode describing how points outside the base
lattice are transformed. 0 (the default) specifies that no
outside points are transformed. 1 specifies that all outside
points are transformed, and 2 specifies that only those
outside points which fall within the "falloff distance" (see
the -ofd/outsideFalloffDistance flag) are transformed. When
querying, the current setting for the lattice is returned.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
position(pos): [linear, linear, linear]
    properties: create
    Used to specify the position of the newly created lattice.

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
removeTweaks(rt): boolean
    properties: edit
    Remove any lattice deformations caused by moving lattice
points. Translations/rotations and scales on the lattice itself
are not removed.

---
rotation(ro): [angle, angle, angle]
    properties: create
    Used to specify the initial rotation of the newly created lattice.

---
scale(s): [linear, linear, linear]
    properties: create
    Used to specify the initial scale of the newly created lattice.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lattice.html 
    """


def latticeDeformKeyCtx(flagenvelope: float, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglatticeColumns: uint, flaglatticeRows: uint, flagname: string, flagscaleLatticePts: boolean) -> string:
    """Synopsis:
---
---
 latticeDeformKeyCtx(
contextName
    , [envelope=float], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [latticeColumns=uint], [latticeRows=uint], [name=string], [scaleLatticePts=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

latticeDeformKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a lattice manipulator with 4 x 4 lattice.
---

cmds.latticeDeformKeyCtx( 'latticeContex', latticeColumns=4, latticeRows=4 )

---
Return:
---


    string: Context name

Flags:
---


---
envelope(ev): float
    properties: query, edit
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
    properties: query, edit
    Specifies the number column points the lattice contains.

---
latticeRows(lr): uint
    properties: query, edit
    Specifies the number of rows the lattice contains.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
scaleLatticePts(slp): boolean
    properties: query, edit
    Specifies if the selected lattice points should scale
around the pick point. If this value is false the
the default operation is 'move'

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/latticeDeformKeyCtx.html 
    """


def launch(flagdirectory: string, flagmovie: string, flagpdfFile: string, flagwebPage: string) -> None:
    """Synopsis:
---
---
 launch([directory=string], [movie=string], [pdfFile=string], [webPage=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

launch is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

---
launch a web browser to open webpage http://www.autodesk.com
cmds.launch(web="http://www.autodesk.com")

---


Flags:
---


---
directory(dir): string
    properties: create
    A directory.

---
movie(mov): string
    properties: create
    A movie file. The only acceptable movie file formats are MPEG,
Quicktime, and Windows Media file. The file's name must end
with .mpg, .mpeg, .mp4, .wmv, .mov, or .qt.

---
pdfFile(pdf): string
    properties: create
    A PDF (Portable Document Format) document. The file's name must
end with .pdf.

---
webPage(web): string
    properties: create
    A web page.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/launch.html 
    """


def launchImageEditor(flageditImageFile: string, flagviewImageFile: string) -> None:
    """Synopsis:
---
---
 launchImageEditor(
[filename]
    , [editImageFile=string], [viewImageFile=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

launchImageEditor is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a blinn shader with a psd file texture.
cmds.shadingNode('blinn', asShader=True)
cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
cmds.connectAttr('blinn1.outColor', 'blinn1SG.surfaceShader', f=True)
cmds.shadingNode('psdFileTex', asTexture=True)
cmds.connectAttr('psdFileTex1.outColor', 'blinn1.color')
cmds.setAttr('psdFileTex1.fileTextureName', 'C:/test.psd', type='string')

Create a poly plane, and assign the blinn shader to it.
cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
cmds.sets(e=True, forceElement='blinn1SG')

Now you can launch Photoshop to edit this psd texture file
cmds.launchImageEditor(eif=cmds.getAttr('psdFileTex1.fileTextureName'))

---


Flags:
---


---
editImageFile(eif): string
    properties: create
    If the file is a PSD, then the specified verison of Photoshop is launched,
and the file is opened in it. If file is any other image type,
then the preferred image editor is launched, and the file is opened in it.

---
viewImageFile(vif): string
    properties: create
    Opens up an Image editor to view images.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/launchImageEditor.html 
    """


def layerButton(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolor: tuple[float, float, float], flagcommand: script, flagcurrent: boolean, flagdefineTemplate: string, flagdocTag: string, flagdoubleClickCommand: script, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghideOnPlaybackCommand: script, flaghighlightColor: tuple[float, float, float], flagidentification: int, flagisObscured: boolean, flaglabel: string, flaglabelWidth: boolean, flaglayerHideOnPlayback: boolean, flaglayerState: string, flaglayerVisible: boolean, flagmanage: boolean, flagname: string, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrenameCommand: string, flagselect: boolean, flagstatusBarMessage: string, flagtransparent: boolean, flagtypeCommand: script, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagvisibleCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 layerButton([annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [color=[float, float, float]], [command=script], [current=boolean], [defineTemplate=string], [docTag=string], [doubleClickCommand=script], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [hideOnPlaybackCommand=script], [highlightColor=[float, float, float]], [identification=int], [isObscured=boolean], [label=string], [labelWidth=boolean], [layerHideOnPlayback=boolean], [layerState=string], [layerVisible=boolean], [manage=boolean], [name=string], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [renameCommand=string], [select=boolean], [statusBarMessage=string], [transparent=boolean], [typeCommand=script], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [visibleCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

layerButton is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
Create a button for the default layer, colour it red and select it
b = cmds.layerButton(name='defaultLayer', cl=(1.0, 0.0, 0.0), s=True)
cmds.showWindow()

Find out how wide the layer buttons are when created
width = cmds.layerButton(b ,q=True, labelWidth=True )

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
    Set the command to call on a change of any kind.

---
color(cl): [float, float, float]
    properties: create, edit
    Layer color, specified with normalized real numbers in R, G,
B space.

---
command(c): script
    properties: create, edit
    Set the command to call on a single click.

---
current(cr): boolean
    properties: create, edit
    Set this button to display as the current layer.  The current
layer is the one which the user has the option of adding all newly
created objects into.  NB: Setting the layer button to this state
has no effect on the actual current layer.

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
    Set the command to call on a double click.

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
hideOnPlaybackCommand(hpc): script
    properties: create, edit
    Command that is called when the hide on playback indicator of
the layer button is pressed.

---
highlightColor(hlc): [float, float, float]
    properties: create, query, edit
    The highlight color of the control. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
identification(id): int
    properties: create, query, edit
    This is the integer identification number associated with
the layer.

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
    Label text for the button.

---
labelWidth(lw): boolean
    properties: query
    Query the width of the label part so as to determine if
button clicks are in the label part or the colour swatch part.

---
layerHideOnPlayback(hp): boolean
    properties: create, query, edit
    Indicates whether the layer is visible or invisible during the playback.

---
layerState(ls): string
    properties: create, query, edit
    Describes the state of the layer.  This may be one of
normal, template, or reference.

---
layerVisible(lv): boolean
    properties: create, query, edit
    Indicates whether the layer is visible or invisible.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
name(n): string
    properties: create, query
    Name of the layer.

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
renameCommand(rc): string
    properties: create, edit
    Set the command to call when the layer gets renamed. The string
'#1' will be substituted with the control's name and '#2' will be
replaced with the layer's new name.

---
select(s): boolean
    properties: create, query, edit
    Set this button to display as a selected layer.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
transparent(t): boolean
    properties: create, query, edit
    Indicate whether the layer color is visible or transparent.

---
typeCommand(tc): script
    properties: create, edit
    Command that is called when the type indicator of
the layer button is pressed.

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
visibleCommand(vc): script
    properties: create, edit
    Command that is called when the visibility indicator of
the layer button is pressed.

---
width(w): int
    properties: create, query, edit
    The width of the control.  The control will attempt to
be this size if it is not overruled by parent layout conditions.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/layerButton.html 
    """


def layeredShaderPort(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnode: name, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagselectedColorControl: string, flagselectedTransparencyControl: string, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 layeredShaderPort(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [node=name], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [selectedColorControl=string], [selectedTransparencyControl=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

layeredShaderPort is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

layer = cmds.shadingNode('layeredShader', asShader=True)
cmds.window()
cmds.columnLayout('r')
cmds.layeredShaderPort(n=layer)
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
    Specifies the name of the newLayeredShader
node this port will represent.

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
selectedColorControl(scc): string
    properties: create
    Specifies the name of the UI-control that
represents the currently selected layer's color.

---
selectedTransparencyControl(stc): string
    properties: create
    Specifies the name of the UI-control that
represents the currently selected layer's transparency.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/layeredShaderPort.html 
    """


def layeredTexturePort(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnode: name, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagselectedAlphaControl: string, flagselectedBlendModeControl: string, flagselectedColorControl: string, flagselectedIsVisibleControl: string, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 layeredTexturePort(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [node=name], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [selectedAlphaControl=string], [selectedBlendModeControl=string], [selectedColorControl=string], [selectedIsVisibleControl=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

layeredTexturePort is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout('r')
cmds.layeredTexturePort(n='layeredTexture1')
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
    Specifies the name of the newLayeredTexture
node this port will represent.

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
selectedAlphaControl(sac): string
    properties: create
    Specifies the name of the UI-control that
represents the currently selected layer's alpha.

---
selectedBlendModeControl(sbc): string
    properties: create
    Specifies the name of the UI-control that
represents the currently selected layer's blend mode.

---
selectedColorControl(scc): string
    properties: create
    Specifies the name of the UI-control that
represents the currently selected layer's color.

---
selectedIsVisibleControl(svc): string
    properties: create
    Specifies the name of the UI-control that
represents the currently selected layer's visibility.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/layeredTexturePort.html 
    """


def layout(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchildArray: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> None:
    """Synopsis:
---
---
 layout(
string
    , [annotation=string], [backgroundColor=[float, float, float]], [childArray=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

layout is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

   Create a simple window containing a single column layout
   and a few buttons.
---

window = cmds.window(title='Layout Example')
column = cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow( window )

   If you don't know that the layout is actually a 'columnLayout' then
   you may use the 'layout' command to determine certain properties.
---

cmds.layout( column, query=True, numberOfChildren=True )
cmds.layout( column, query=True, childArray=True )
cmds.layout( column, query=True, height=True )

---


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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/layout.html 
    """


def layoutDialog(flagbackgroundColor: tuple[float, float, float], flagdismiss: string, flagparent: string, flagtitle: string, flaguiScript: script) -> string:
    """Synopsis:
---
---
 layoutDialog([backgroundColor=[float, float, float]], [dismiss=string], [parent=string], [title=string], [uiScript=script])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

layoutDialog is undoable, NOT queryable, and NOT editable.
NOTE:
A layoutDialog is not a window and certain UI elements will not function
properly within it. In particular menuBars and panels containing menuBars
should not be used with the layoutDialog.




Example:
---
import maya.cmds as cmds

def checkboxPrompt():
        Get the dialog's formLayout.
        ---

        form = cmds.setParent(q=True)

        layoutDialog's are not resizable, so hard code a size here,
        to make sure all UI elements are visible.
        ---

        cmds.formLayout(form, e=True, width=300)

        t = cmds.text(l='What do you want to do?')

        b1 = cmds.button(l='Abort', c='cmds.layoutDialog( dismiss="Abort" )' )
        b2 = cmds.button(l='Skip', c='cmds.layoutDialog( dismiss="Skip" )' )
        b3 = cmds.button(l='Continue', c='cmds.layoutDialog( dismiss="Continue" )' )

        cb1 = cmds.checkBox(label='Remember my choice')

        spacer = 5
        top = 5
        edge = 5

        cmds.formLayout(form, edit=True,
                                        attachForm=[(t, 'top', top), (t, 'left', edge), (t, 'right', edge), (b1, 'left', edge), (b3, 'right', edge), (cb1, 'left', edge), (cb1, 'bottom', spacer)],
                                        attachNone=[(t, 'bottom'), (b1, 'bottom'), (b2, 'bottom'), (b3, 'bottom'), (cb1, 'right')],
                                        attachControl=[(b1, 'top', spacer, t), (b2, 'top', spacer, t), (b3, 'top', spacer, t), (cb1, 'top', spacer, b1)],
                                        attachPosition=[(b1, 'right', spacer, 33), (b2, 'left', spacer, 33), (b2, 'right', spacer, 66), (b3, 'left', spacer, 66)])

print cmds.layoutDialog(ui=checkboxPrompt)

---
Return:
---


    string: The string specified by the -dismiss flag, or "dismiss" if the dialog
was closed.

Flags:
---


---
backgroundColor(bgc): [float, float, float]
    properties: create
    The background color of the dialog. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0. (Windows only flag)

---
dismiss(dis): string
    properties: create
    Dismiss the current layoutDialog. The specified string will
be set as the result of the initial layoutDialog command.

---
parent(p): string
    properties: create
    Specify the parent window for the dialog.  The dialog will
be centered on this window and raise and lower with it's parent.
By default, the dialog is not parented to a particular window and
is simply centered on the screen.

---
title(t): string
    properties: create
    The dialog title.

---
uiScript(ui): script
    properties: create
    The specified MEL procedure name will be invoked to build the
UI of the layoutDialog. This flag is required when creating
a layoutDialog.
The top-level control of a layoutDialog is a formLayout with
100 divisions. It can be accessed by calling 'setParent -q' at
the beginning of the specified MEL procedure.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/layoutDialog.html 
    """


def license(flagborrow: boolean, flaginfo: boolean, flagisBorrowed: boolean, flagisExported: boolean, flagisTrial: boolean, flaglicenseMethod: boolean, flagproductChoice: boolean, flagr: boolean, flagshowBorrowInfo: boolean, flagshowProductInfoDialog: boolean, flagstatus: boolean, flagusage: boolean) -> string:
    """Synopsis:
---
---
 license([borrow=boolean], [info=boolean], [isBorrowed=boolean], [isExported=boolean], [isTrial=boolean], [licenseMethod=boolean], [productChoice=boolean], [r=boolean], [showBorrowInfo=boolean], [showProductInfoDialog=boolean], [status=boolean], [usage=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

license is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.license(showProductInfoDialog=True)

---
Return:
---


    string: The application's license information.

Flags:
---


---
borrow(b): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
info(i): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
isBorrowed(ib): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
isExported(ie): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
isTrial(it): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
licenseMethod(lm): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
productChoice(pc): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
r(r): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
showBorrowInfo(sbi): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
showProductInfoDialog(spi): boolean
    properties: create
    Show the Product Information Dialog

---
status(s): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
usage(u): boolean
    properties: create
    This flag is obsolete and no longer supported.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/license.html 
    """


def lightList(flagadd: name, flagremove: name) -> None:
    """Synopsis:
---
---
 lightList([add=name], [remove=name])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lightList is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.lightList( add='foo' )

---


Flags:
---


---
add(add): name
    properties: create
    add object(s) to light list.

---
remove(rm): name
    properties: create
    remove object(s) to light list.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lightList.html 
    """


def lightlink(flagb: boolean, flaghierarchy: boolean, flaglight: name, flagmake: boolean, flagobject: name, flagsets: boolean, flagshadow: boolean, flagshapes: boolean, flagtransforms: boolean, flaguseActiveLights: boolean, flaguseActiveObjects: boolean) -> list[string] | string:
    """Synopsis:
---
---
 lightlink(
objects
    , [b=boolean], [hierarchy=boolean], [light=name], [make=boolean], [object=name], [sets=boolean], [shadow=boolean], [shapes=boolean], [transforms=boolean], [useActiveLights=boolean], [useActiveObjects=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lightlink is undoable, queryable, and NOT editable.
If no make, break or query flag is specified and both lights and
objects flags are present, the make flag is assumed to be specified.

If no make, break or query flag is specified and only one of the
lights and objects flags is present, the query flag is assumed to be
specified.

You can specify as many lights and objects as you like, using the
multiuse -light and -object flags.

A better way to perform light linking is to make sets of lights and
sets of geometry. If you create a set which contains lights (such as
the ceiling lights in your scene) and a set which contains geometry
(such as the geometry of your character), you can then link the
set containing lights with the set containing geometry
in order to get those lights to illuminate those pieces of geometry.
In addition, you can add and remove lights and geometry from their
respective sets without having to make and break light links.




Example:
---
import maya.cmds as cmds

cmds.lightlink( light=('spotLight1', 'pointLight2', 'ambientLight4'), object=('apple', 'orange', 'banana') )

causes a light link to be "created between"    each of the lights
spotLight1, pointLight2, ambientLight4 and each of the objects
apple, orange, banana. This creates 9 links. Note that no make,
break or query flag is specified so make is assumed since both
lights and objects are specified.

cmds.lightlink( make=True, light='ceilingLightSet', object='apple' )
causes a light link to be "created between" the ceiling lights and
the apple geometry. If apple is already illuminated by
ceilingLightSet, then nothing changes and a warning is produced.

cmds.lightlink( object='stillLifeSet', light='spotLight1' )
causes a light link to be "created between" spotLight1 and the still
life. If stillLifeSet is already illuminated by spotLight1, then
nothing changes and a warning is produced. Note: no make, break or
query flag is specified so the make flag is assumed since both lights
and objects are specified.

cmds.lightlink( light=('ceilingLightSet', 'floorLightSet'), object='tableAndChairsSet' )
causes a light link to be "created between" each of the light sets
ceilingLightSet, floorLightSet and the object set tableAndChairsSet.

cmds.lightlink( query=True, light='ceilingLightSet' )
will return a string array of objects which are illuminated by the
set ceilingLightSet. For example, the return value might be:
stillLifeSet table chair floor roomWallsSet binky

cmds.lightlink( query=True, object='apple' )
will return a string array of lights which illuminate the object
apple. For example, the return value might be ceilingLightSet
spotLight1 spotLight2 ambientLight1

cmds.lightlink( object='apple' )
will return a string array of lights which illuminate the object
apple. For example, the return value might be ceilingLightSet
spotLight1 spotLight2 ambientLight1. Note that no make, break
or query flag is specified, so query is assumed since no lights
are specified.

cmds.lightlink( b=True, light='ceilingLightSet', object='apple' )
causes the light set ceilingLightSet to no longer illuminate the
object apple. If ceilingLightSet was already not illuminating apple,
nothing changes and a warning is produced.

---
Return:
---


    string: Single element command result
    list[string]: Multi element command result

Flags:
---


---
b(b): boolean
    properties: create
    The presence of this flag on the command indicates that the
command is being invoked to break links between lights and
renderable objects.

---
hierarchy(h): boolean
    properties: create
    When querying, specifies whether the result should include the
hierarchy of transforms above shapes linked to the queried
light/object. The transforms considered part of the hierarchy do
not include the transform immediately above the shape. Default
is true.

---
light(l): name
    properties: create, multiuse
    The argument to the light flag specifies a node to be used by
the command in performing the action as if the node is a light.
This is a multiuse flag -- many light nodes can be specified in
a single invocation of the lightlink command.

---
make(m): boolean
    properties: create
    The presence of this flag on the command indicates that the
command is being invoked to make links between lights and
renderable objects.

---
object(o): name
    properties: create, multiuse
    The argument to the object flag specifies a node to be used by
the command in performing the action as if the node is an object.
This is a multiuse flag -- many object nodes can be specified in
a single invocation of the lightlink command.

---
sets(set): boolean
    properties: create
    When querying, specifies whether the result should include sets
linked to the queried light/object. Default is true.

---
shadow(shd): boolean
    properties: create
    Specify that shadows are to be linked.

---
shapes(shp): boolean
    properties: create
    When querying, specifies whether the result should include shapes
linked to the queried light/object. Default is true.

---
transforms(t): boolean
    properties: create
    When querying, specifies whether the result should include
transforms immediately above shapes linked to the queried
light/object. Default is true.

---
useActiveLights(ual): boolean
    properties: create
    Specify that active lights are to be used.

---
useActiveObjects(uao): boolean
    properties: create
    Specify that active objects are to be used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lightlink.html 
    """


def linearPrecision() -> None:
    """Synopsis:
---
---
 linearPrecision(
int
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

linearPrecision is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.linearPrecision( 3 )
cmds.linearPrecision( 10 ) will be rounded down to 6, the maximum

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/linearPrecision.html 
    """


def listAnimatable(flagactive: boolean, flagmanip: boolean, flagmanipHandle: boolean, flagshape: boolean, flagtype: boolean) -> list[string]:
    """Synopsis:
---
---
 listAnimatable([active=boolean], [manip=boolean], [manipHandle=boolean], [shape=boolean], [type=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listAnimatable is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

List only the attrs driven by the current manip.
---

cmds.listAnimatable( manip=True )

List only the attrs driven by the current manipulator handle.
---

cmds.listAnimatable( manipHandle=True )

List only the types of nodes driven by the current manip.
---

cmds.listAnimatable( manip=True, type=True )

List only the types of the active nodes.
---

cmds.listAnimatable( type=True )

List attributes on active objects (and shapes below them),
or active attrs.
---

cmds.listAnimatable()

List types of active objects and types of any shapes below active
objects.
---

cmds.listAnimatable( type=True )

---
Return:
---


    list[string]: All animatable attributes found

Flags:
---


---
active(act): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
manip(m): boolean
    properties: create
    Return only those attributes affected by the current manip.
If there is no manip active and any other flags are
specified, output is the same as if the "-manip" flag were not present.

---
manipHandle(mh): boolean
    properties: create
    Return only those attributes affected by the current manip handle.
If there is no manip handle active and any other flags are
specified, output is the same as if the "-manipHandle" flag were not present.

---
shape(s): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
type(typ): boolean
    properties: create
    Instead of returning attributes, Return the types of nodes that
are currently animatable.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listAnimatable.html 
    """


def listAttr(flagarray: boolean, flagattributeType: string, flagcaching: boolean, flagcategory: string, flagchangedSinceFileOpen: boolean, flagchannelBox: boolean, flagconnectable: boolean, flagextension: boolean, flagfromPlugin: boolean, flagfullNodeName: boolean, flaghasData: boolean, flaghasNullData: boolean, flaginUse: boolean, flagkeyable: boolean, flagleaf: boolean, flaglocked: boolean, flagmulti: boolean, flagnodeName: boolean, flagoutput: boolean, flagramp: boolean, flagread: boolean, flagreadOnly: boolean, flagscalar: boolean, flagscalarAndArray: boolean, flagsettable: boolean, flagshortNames: boolean, flagstring: string, flagunlocked: boolean, flagusedAsFilename: boolean, flaguserDefined: boolean, flagvisible: boolean, flagwrite: boolean) -> list[string]:
    """Synopsis:
---
---
 listAttr(
[objects]
    , [array=boolean], [attributeType=string], [caching=boolean], [category=string], [changedSinceFileOpen=boolean], [channelBox=boolean], [connectable=boolean], [extension=boolean], [fromPlugin=boolean], [fullNodeName=boolean], [hasData=boolean], [hasNullData=boolean], [inUse=boolean], [keyable=boolean], [leaf=boolean], [locked=boolean], [multi=boolean], [nodeName=boolean], [output=boolean], [ramp=boolean], [read=boolean], [readOnly=boolean], [scalar=boolean], [scalarAndArray=boolean], [settable=boolean], [shortNames=boolean], [string=string], [unlocked=boolean], [usedAsFilename=boolean], [userDefined=boolean], [visible=boolean], [write=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listAttr is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.sphere()
cmds.listAttr( r=True, s=True )
This will list the scalar readable attributes of the
selected nodes.  If more than one node is selected attributes
may be listed several times.

cmds.listAttr( s=True, r=True, w=True, c=True, st=['centerX','centerY'] )
This will list all scalar, readable, writable, and connectable
attributes whose names are "centerX" or "centerY".

cmds.listAttr( r=True, st='center*', ct='a*' )
This will list all readable attributes whose names match
"center*" (e.g. "centerX" or "centerpede") and who belong to
a category starting with the letter "a".

cmds.listAttr( 'nurbsSphere1', s=True, cfo=True )
This will list all scalar attributes of
nurbsSphere1 that have been changed since the
file in which nurbsSphere1 is defined has been
opened.  If nurbsSphere1 comes from a referenced file,
the result will be all the attributes that have changed
since the referenced file was opened.

---
Return:
---


    list[string]: : List of attributes matching criteria

Flags:
---


---
array(a): boolean
    properties: create
    only list array (not multi) attributes

---
attributeType(at) 2024: string
    properties: create, multiuse
    Return attributes of a particular type.

---
caching(ca): boolean
    properties: create
    only show attributes that are cached internally

---
category(ct): string
    properties: create, multiuse
    only show attributes belonging to the given category.
Category string can be a regular expression.

---
changedSinceFileOpen(cfo): boolean
    properties: create
    Only list the attributes that have been changed
since the file they came from was opened. Typically useful
only for objects/attributes coming from referenced files.

---
channelBox(cb): boolean
    properties: create
    only show non-keyable attributes that appear in the channelbox

---
connectable(c): boolean
    properties: create
    only show connectable attributes

---
extension(ex): boolean
    properties: create
    list user-defined attributes for all nodes of this type (extension attributes)

---
fromPlugin(fp): boolean
    properties: create
    only show attributes that were created by a plugin

---
fullNodeName(fnn) 2024: boolean
    properties: create
    Return full node name in result.

---
hasData(hd): boolean
    properties: create
    list only attributes that have data (all attributes
except for message attributes)

---
hasNullData(hnd): boolean
    properties: create
    list only attributes that have null data.
This will list all attributes that have
data (see hasData flag) but the data value
is uninitialized.
A common example where an attribute may have null
data is when a string attribute is
created but not yet assigned an initial value.
Similarly array attribute data is often null until
it is initialized.

---
inUse(iu): boolean
    properties: create
    only show attributes that are currently marked as in use. This flag indicates
that an attribute affects the scene data in some way. For example it has a
non-default value or it is connected to another attribute.  This is the
general concept though the precise implementation is subject to change.

---
keyable(k): boolean
    properties: create
    only show attributes that can be keyframed

---
leaf(lf): boolean
    properties: create
    Only list the leaf-level name of the attribute.
controlPoints[44].xValue would be listed as "xValue".

---
locked(l): boolean
    properties: create
    list only attributes which are locked

---
multi(m): boolean
    properties: create
    list each currently existing element of a multi-attribute

---
nodeName(nn) 2024: boolean
    properties: create
    Return node name in result.

---
output(o): boolean
    properties: create
    List only the attributes which are numeric or which
are compounds of numeric attributes.

---
ramp(ra): boolean
    properties: create
    list only attributes which are ramps

---
read(r): boolean
    properties: create
    list only attributes which are readable

---
readOnly(ro): boolean
    properties: create
    List only the attributes which are readable and not
writable.

---
scalar(s): boolean
    properties: create
    only list scalar numerical attributes

---
scalarAndArray(sa): boolean
    properties: create
    only list scalar and array attributes

---
settable(se): boolean
    properties: create
    list attribute which are settable

---
shortNames(sn): boolean
    properties: create
    list short attribute names (default is to list long names)

---
string(st): string
    properties: create, multiuse
    List only the attributes that match the other
criteria AND match the string(s) passed from this flag.
String can be a regular expression.

---
unlocked(u): boolean
    properties: create
    list only attributes which are unlocked

---
usedAsFilename(uf): boolean
    properties: create
    list only attributes which are designated to be treated as filenames

---
userDefined(ud): boolean
    properties: create
    list user-defined (dynamic) attributes

---
visible(v): boolean
    properties: create
    only show visible or non-hidden attributes

---
write(w): boolean
    properties: create
    list only attributes which are writable

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listAttr.html 
    """


def listAttrPatterns(flagpatternType: boolean, flagverbose: boolean) -> list[string]:
    """Synopsis:
---
---
 listAttrPatterns([patternType=boolean], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listAttrPatterns is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.listAttrPatterns()
// Return: ["approvalAttrs", "sceneAndShotAttrs"] //

cmds.listAttrPatterns( patternType=True )
// Return: "xmlPatternFactory" //

cmds.listAttrPatterns( patternType=True, verbose=True )
// Return: ["xmlPatternFactory", "xmlPatternFactory/approvalAttrs", "xmlPatternFactory/sceneAndShotAttrs"] //

cmds.listAttrPatterns( verbose=True )
Pattern approvalAttrs
    PatternFactory xmlPatternFactory:
    File: "attrPatterns/approvalAttrs.xml"
    Attribute Count: 8
    Attribute Tree:
      fxApproval (compound)
        fxApprover (string)
        fxApprovalDate (int)
        fxApprovalState (enum)
      layoutApproval (compound)
        layoutApprover (string)
        layoutApprovalDate (int)
        layoutApprovalState (enum)
  Pattern sceneAndShotAttrs
    PatternFactory xmlPatternFactory:
    File: "attrPatterns/sceneAndShotAttrs.xml"
    Attribute Count: 4
    Attribute Tree:
      sceneId (int)
      sceneOwner (string)
      shotId (int)
      shotOwner (string)
// Return: ["approvalAttrs", "sceneAndShotAttrs"] //

---
Return:
---


    list[string]: List of patterns or pattern instances available

Flags:
---


---
patternType(pt): boolean
    properties: create
    If turned on then show the list of pattern types rather than actual instantiated patterns.

---
verbose(v): boolean
    properties: create
    If turned on then show detailed information about the patterns or pattern types.
The same list of instance or pattern names is returned as for the non-verbose case.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listAttrPatterns.html 
    """


def listCameras(flagorthographic: boolean, flagperspective: boolean) -> list[string]:
    """Synopsis:
---
---
 listCameras([orthographic=boolean], [perspective=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listCameras is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

List all cameras
cmds.listCameras()

List all persp cameras
perspCameras = cmds.listCameras( p=True )

---
Return:
---


    list[string]: Command result

Flags:
---


---
orthographic(o): boolean
    properties: create
    Display all orthographic cameras.

---
perspective(p): boolean
    properties: create
    Display all perspective cameras.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listCameras.html 
    """


def listConnections(flagconnections: boolean, flagdestination: boolean, flagexactType: boolean, flagfullNodeName: boolean, flagplugs: boolean, flagshapes: boolean, flagskipConversionNodes: boolean, flagsource: boolean, flagtype: string) -> list[string]:
    """Synopsis:
---
---
 listConnections([connections=boolean], [destination=boolean], [exactType=boolean], [fullNodeName=boolean], [plugs=boolean], [shapes=boolean], [skipConversionNodes=boolean], [source=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listConnections is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.sphere( ch=True, n='BALL' )
cmds.setKeyframe()
List all connections to BALL
list = cmds.listConnections('BALL')

List only incoming connections from BALL.tx
cmds.listConnections( 'BALL.tx', d=False, s=True )

List connections from BALL to nodes of type 'transform'
cmds.listConnections( t='transform' )

List connections on BALL, ignoring unit conversion nodes
cmds.listConnections( 'BALL', scn=True )

---
Return:
---


    list[string]: List of connection plugs/nodes

Flags:
---


---
connections(c): boolean
    properties: create
    If true, return both attributes involved in the connection. The one
on the specified object is given first.  Default false.

---
destination(d): boolean
    properties: create
    Give the attributes/objects that are on the "destination" side of
connection to the given object.  Default true.

---
exactType(et): boolean
    properties: create
    When set to true, -t/type only considers node of this exact
type. Otherwise, derived types are also taken into account.

---
fullNodeName(fnn) 2024: boolean
    properties: create
    Return full node name in result.

---
plugs(p): boolean
    properties: create
    If true, return the connected attribute names; if false, return the
connected object names only.  Default false;

---
shapes(sh): boolean
    properties: create
    Actually return the shape name instead of the transform when the
shape is "selected".  Default false.

---
skipConversionNodes(scn): boolean
    properties: create
    If true, skip over unit conversion nodes and return the
node connected to the conversion node on the other side.  Default false.

---
source(s): boolean
    properties: create
    Give the attributes/objects that are on the "source" side of
connection to the given object.  Default true.

---
type(t): string
    properties: create
    If specified, only take objects of a specified type.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listConnections.html 
    """


def listDeviceAttachments(flagattribute: string, flagaxis: string, flagclutch: string, flagdevice: string, flagfile: string, flagselection: boolean, flagwrite: boolean) -> string:
    """Synopsis:
---
---
 listDeviceAttachments([attribute=string], [axis=string], [clutch=string], [device=string], [file=string], [selection=boolean], [write=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listDeviceAttachments is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.listDeviceAttachments()List all attachments

List attachments on the spaceball that are clutched on Button1
cmds.listDeviceAttachments( d='spaceball', c='Button1' )

write out attachments for the spaceball device, since there is
no file name specified, attachments will be written out to
spaceball.mel
cmds.listDeviceAttachments( d='spaceball', w=True )

write out attachments for all devices, since there is not file
name specified, attachments will be written out to devices.mel
cmds.listDeviceAttachments( w=True )

---
Return:
---


    string: Command result

Flags:
---


---
attribute(at): string
    properties: create
    specify the attribute attachments to list

---
axis(ax): string
    properties: create
    specify the axis attachments to list

---
clutch(c): string
    properties: create
    List only attachment clutched with this button

---
device(d): string
    properties: create
    specify which device attachments to list

---
file(f): string
    properties: create
    Specify the name of the file to write out device
attachments.

---
selection(sl): boolean
    properties: create
    This flag list only attachments on selection

---
write(w): boolean
    properties: create
    Write out device attachments to a file specified
by the -f flag, is set.  If -f is not set, it'll
write out to a file named for the device.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listDeviceAttachments.html 
    """


def listHistory(flagallConnections: boolean, flagallFuture: boolean, flagallGraphs: boolean, flagbreadthFirst: boolean, flagfastIteration: boolean, flagfullNodeName: boolean, flagfuture: boolean, flagfutureLocalAttr: boolean, flagfutureWorldAttr: boolean, flaggroupLevels: boolean, flaghistoryAttr: boolean, flaginterestLevel: int, flagleaf: boolean, flaglevels: uint, flagpruneDagObjects: boolean) -> list[string]:
    """Synopsis:
---
---
 listHistory(
objects
    , [allConnections=boolean], [allFuture=boolean], [allGraphs=boolean], [breadthFirst=boolean], [fastIteration=boolean], [fullNodeName=boolean], [future=boolean], [futureLocalAttr=boolean], [futureWorldAttr=boolean], [groupLevels=boolean], [historyAttr=boolean], [interestLevel=int], [leaf=boolean], [levels=uint], [pruneDagObjects=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listHistory is undoable, queryable, and NOT editable.
For information on history connections through specific plugs use
the "listConnections" command first to find where the history begins
then use this command on the resulting node.




Example:
---
import maya.cmds as cmds

cmds.curve( d=3, p=[(-3, 0, 0),(-1, 0, 6),(6, 0, 8),(8, 0, 2)], k=[0,0,0,1,1,1], n="snake" )
cmds.instance( n="rattler" )
cmds.revolve( 'rattler', ch=True, n="charmer" )
cmds.revolve( 'snake', ch=True, n="medusa" )

cmds.listHistory()
Result:[u'medusaShape', u'revolve2', u'snake|curveShape1'] ---


cmds.listHistory( 'charmer' )
Result:[u'charmerShape', u'revolve1', u'rattler|curveShape1'] ---


cmds.listHistory( 'medusa', lv=1 )
Result:[u'medusaShape', u'revolve2'] ---


cmds.listHistory( 'medusa', future=True )
Result:[u'medusaShape', u'initialShadingGroup'] ---


If you just list the curve's future you get both directions
cmds.listHistory( 'curveShape1', future=True )
Result:[u'snake|curveShape1', u'revolve2', u'medusaShape', u'revolve1', u'charmerShape'] ---


To follow only one history you'll need to follow the path you
want first, then add the node you started at if so desired since
it will not be included (here snake|curveShape1 won't list).

List the future of the first curve
hist = cmds.listConnections('curveShape1.ws[0]',c=1)
cmds.listHistory( hist[1], future=True )
Result:[u'revolve2', u'medusaShape'] ---


List the future of the second curve
hist = cmds.listConnections('curveShape1.ws[1]',c=1)
cmds.listHistory( hist[1], future=True )
Result:[u'revolve1', u'charmerShape'] ---


cmds.listHistory( leaf=0 )
Result:[u'medusa'] ---


---
Return:
---


    list[string]: List of history nodes

Flags:
---


---
allConnections(ac): boolean
    properties: create
    If specified, the traversal that searches for the history or future will
not restrict its traversal across nodes to only dependent plugs.
Thus it will reach all upstream nodes (or all downstream nodes for f/future).

---
allFuture(af): boolean
    properties: create
    If listing the future, list all of it. Otherwise if a shape has
an attribute that represents its output geometry data, and that plug
is connected, only list the future history downstream from that
connection.

---
allGraphs(ag): boolean
    properties: create
    This flag is obsolete and has no effect.

---
breadthFirst(bf): boolean
    properties: create
    The breadth first traversal will return the closest nodes in the
traversal first. The depth first traversal will follow a complete
path away from the node, then return to any other paths from the
node. Default is depth first.

---
fastIteration(fi): boolean
    properties: create
    This flag enables a faster iteration mode that offers more scalable performance,
especially when traversing nodes with numerous connections.  However, the results can
be slightly different, especially in cases with transitive dependencies between
attributes (attribute A is affected by B which is affected by C, but A is not
directly affected by C).

---
fullNodeName(fnn) 2024: boolean
    properties: create
    Return full node name in result.

---
future(f): boolean
    properties: create
    List the future instead of the history.

---
futureLocalAttr(fl): boolean
    properties: query
    This flag allows querying of the local-space future-related attribute(s) on shape nodes.

---
futureWorldAttr(fw): boolean
    properties: query
    This flag allows querying of the world-space future-related attribute(s) on shape nodes.

---
groupLevels(gl): boolean
    properties: create
    The node names are grouped depending on the level.  > 1 is
the lead, the rest are grouped with it.

---
historyAttr(ha): boolean
    properties: query
    This flag allows querying of the attribute where history connects on shape nodes.

---
interestLevel(il): int
    properties: create
    If this flag is set, only nodes whose historicallyInteresting
attribute value is not less than the value will be listed.
The historicallyInteresting attribute is 0 on nodes which are
not of interest to non-programmers.  1 for the TDs, 2 for the users.

---
leaf(lf): boolean
    properties: create
    If transform is selected, show history for its leaf
shape. Default is true.

---
levels(lv): uint
    properties: create
    Levels deep to traverse. Setting the number of levels to
0 means do all levels. All levels is the default.

---
pruneDagObjects(pdo): boolean
    properties: create
    If this flag is set, prune at dag objects.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listHistory.html 
    """


def listInputDeviceAxes() -> list[string]:
    """Synopsis:
---
---
 listInputDeviceAxes(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listInputDeviceAxes is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Returns a list of the axes of the spaceball.
cmds.listInputDeviceAxes( 'spaceball' )

---
Return:
---


    list[string]: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listInputDeviceAxes.html 
    """


def listInputDeviceButtons() -> list[string]:
    """Synopsis:
---
---
 listInputDeviceButtons(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listInputDeviceButtons is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Returns a list of the buttons of the spaceball.
cmds.listInputDeviceButtons( 'spaceball' )

---
Return:
---


    list[string]: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listInputDeviceButtons.html 
    """


def listInputDevices(flagfree: boolean, flagprimary: boolean, flagsecondary: boolean) -> list[string]:
    """Synopsis:
---
---
 listInputDevices([free=boolean], [primary=boolean], [secondary=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listInputDevices is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Returns a list of devices.
cmds.listInputDevices()

---
Return:
---


    list[string]: Command result

Flags:
---


---
free(f): boolean
    properties: create
    List the free devices

---
primary(p): boolean
    properties: create
    List the primary devices

---
secondary(s): boolean
    properties: create
    List the secondary devices

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listInputDevices.html 
    """


def listNodeTypes(flagexclude: string) -> list[string]:
    """Synopsis:
---
---
 listNodeTypes(
string
    , [exclude=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listNodeTypes is undoable, NOT queryable, and NOT editable.
See the 'getClassification' command for a list of the standard classification
strings.




Example:
---
import maya.cmds as cmds

List all shader types in the system
cmds.listNodeTypes( 'shader' )

List all 2D textures that are also shaders
cmds.listNodeTypes( 'texture/2D:shader' )

List all volume shading nodes that are neither utility nodes nor particle nodes
cmds.listNodeTypes( 'shader/volume', ex='shader/volume/utility:shader/volume/particle' )

---
Return:
---


    list[string]: The type names of all node types in the system that satisfy the
given classification string.

Flags:
---


---
exclude(ex): string
    properties: create
    Nodes that satisfies this exclude classification will be filtered out.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listNodeTypes.html 
    """


def listNodesWithIncorrectNames() -> None:
    """Synopsis:
---
---
 listNodesWithIncorrectNames()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listNodesWithIncorrectNames is NOT undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.listNodesWithIncorrectNames()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listNodesWithIncorrectNames.html 
    """


def listRelatives(flagallDescendents: boolean, flagallParents: boolean, flagchildren: boolean, flagfullPath: boolean, flagnoIntermediate: boolean, flagparent: boolean, flagpath: boolean, flagshapes: boolean, flagtype: string) -> list[string]:
    """Synopsis:
---
---
 listRelatives(
[objects]
    , [allDescendents=boolean], [allParents=boolean], [children=boolean], [fullPath=boolean], [noIntermediate=boolean], [parent=boolean], [path=boolean], [shapes=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listRelatives is undoable, NOT queryable, and NOT editable.

Unlike ls, this command does not return a unique path but simply returns
the object's name by default. To get a unique path the -path flag must
be used.


When listing parents of objects directly under the world, the command
will return an empty parent list. Listing parents of objects directly
under a shape (underworld objects) will return their containing shape
node in the list of parents. Listing parents of components of objects
will return the object.


When listing children, shape nodes will return their underworld
objects in the list of children. Listing children of components of
objects returns nothing.


The -ni/noIntermediate flag works with the -s/shapes flag.
It causes any intermediate shapes among the descendents to be ignored.




Example:
---
import maya.cmds as cmds

create an object and an instance for queries
cmds.sphere( n='nexus' )
cmds.instance( n='ball' )

List the name of the shape below the transform node.
shapes = cmds.listRelatives('nexus')

list all parents of shape
(The result of the command is shown)
cmds.listRelatives( shapes[0], allParents=True )
Result:[u'nexus', u'ball'] ---


---
Return:
---


    list[string]: Command result

Flags:
---


---
allDescendents(ad): boolean
    properties: create
    Returns all the children, grand-children etc. of
this dag node.  If a descendent is instanced,
it will appear only once on the list returned.
Note that it lists grand-children before children.

---
allParents(ap): boolean
    properties: create
    Returns all the parents of this dag node. Normally, this
command only returns the parent corresponding to the first
instance of the object

---
children(c): boolean
    properties: create
    List all the children of this dag node (default).

---
fullPath(f): boolean
    properties: create
    Return full pathnames instead of object names.

---
noIntermediate(ni): boolean
    properties: create
    No intermediate objects

---
parent(p): boolean
    properties: create
    Returns the parent of this dag node

---
path(pa): boolean
    properties: create
    Return a proper object name that can be passed to other commands.

---
shapes(s): boolean
    properties: create
    List all the children of this dag node that are
shapes (ie, not transforms)

---
type(typ): string
    properties: create, multiuse
    List all relatives of the specified type.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listRelatives.html 
    """


def listSets(flagallSets: boolean, flagextendToShape: boolean, flagobject: name, flagtype: uint) -> list[string]:
    """Synopsis:
---
---
 listSets(
[object]
    , [allSets=boolean], [extendToShape=boolean], [object=name], [type=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

listSets is undoable, NOT queryable, and NOT editable.
To get a list of all sets in the scene then don't use an object
in the command line but use one of the flags instead.




Example:
---
import maya.cmds as cmds

Get a list of all the sets which `nurbsSphere1` belongs to:
cmds.listSets( object='nurbsSphere1' )

Get a list of all the deformer sets in the scene:
cmds.listSets( type=2 )

Get a list of all the rendering sets which `coneShape1` belongs to:
cmds.listSets( type=1, object='coneShape1' )

---
Return:
---


    list[string]: (string array of all sets the object belongs to)

Flags:
---


---
allSets(allSets): boolean
    properties: create
    Returns all sets in the scene.

---
extendToShape(ets): boolean
    properties: create
    When requesting a transform's sets also walk down to the shape
immediately below it for its sets.

---
object(o): name
    properties: create
    Returns all sets which this object is a member of.

---
type(t): uint
    properties: create
    Returns all sets in the scene of the given type:

1 - all rendering sets
2 - all deformer sets

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/listSets.html 
    """


def loadFluid(flagcurrentTime: boolean, flagframe: float, flaginitialConditions: boolean) -> None:
    """Synopsis:
---
---
 loadFluid([currentTime=boolean], [frame=float], [initialConditions=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

loadFluid is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


Load the initial state cache into the fluid
cmds.loadFluid( ic=True )

---


Flags:
---


---
currentTime(ct): boolean
    properties: create, query, edit
    This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.

---
frame(f): float
    properties: create, query, edit
    This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.

---
initialConditions(ic): boolean
    properties: create, query, edit
    load initial conditions cache

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/loadFluid.html 
    """


def loadModule(flagallModules: boolean, flagload: string, flagscan: boolean) -> list[string]:
    """Synopsis:
---
---
 loadModule([allModules=boolean], [load=string], [scan=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

loadModule is NOT undoable, NOT queryable, and NOT editable.
When Maya starts up it loads all of the module files it finds, making the module's plug-ins, scripts and other resources available for use. Note that the plug-ins themselves are not loaded at this time, Maya is simply made aware of them so that they can be loaded if needed.

The loadModule command provides the ability to list and load any new modules which have been added since Maya started up, thereby avoiding the need to restart Maya before being able to use them.




Example:
---
import maya.cmds as cmds

cmds.loadModule(scan=True)
cmds.loadModule(load='myModuleDef')
cmds.loadModule(allModules=True)

---
Return:
---


    list[string]: Command result

Flags:
---


---
allModules(a): boolean
    properties: create
    Load all new modules not yet loaded in Maya. New modules are the one returned by the -scan option.

---
load(ld): string
    properties: create
    Load the module specified by the module definition file.

---
scan(sc): boolean
    properties: create
    Rescan module presence. Returns the list of module definition files found and not yet loaded into Maya. Does not load any of these newly found modules, nor change the Maya state.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/loadModule.html 
    """


def loadPlugin(flagaddCallback: script, flagallPlugins: boolean, flagname: string, flagquiet: boolean, flagremoveCallback: script) -> list[string]:
    """Synopsis:
---
---
 loadPlugin(
string [string...]
    , [addCallback=script], [allPlugins=boolean], [name=string], [quiet=boolean], [removeCallback=script])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

loadPlugin is undoable, NOT queryable, and NOT editable.
If the plugin was specified with a pathname then that is
where the plugin will be searched for. If no pathname was
provided then the current working directory (i.e. the one
returned by Maya's 'pwd' command) will be searched, followed
by the directories in the MAYA_PLUG_IN_PATH environment variable.

When the plug-in is loaded, the name used in Maya's
internal plug-in registry for the plug-in information will
be the file name with the extension removed.  For example,
if you load the plug-in "newNode.mll" the name used in
the Maya's registry will be "newNode".  This value as
well as that value with either a ".so", ".mll" or ".bundle"
extension can be used as valid arguments to either the
unloadPlugin or pluginInfo commands.




Example:
---
import maya.cmds as cmds

Load the plug-in named "newNode" into Maya.
---

cmds.loadPlugin( 'newNode.py' )

Load all the plug-ins found in all the directories that are
included in MAYA_PLUG_IN_PATH.
---

cmds.loadPlugin( allPlugins=True )

---
Return:
---


    list[string]: the internal names of the successfully loaded plug-ins

Flags:
---


---
addCallback(ac): script
    properties: create
    Add a MEL or Python callback script to be called after a plug-in is loaded.

For MEL, the procedure should have the following signature:
global proc procedureName(string $pluginName).

For Python, you may specify either a script as a string, or a Python callable
object such as a function.  If you specify a string, then put the formatting
specifier "%s" where you want the name of the plug-in to be inserted.  If you
specify a callable such as a function, then the name of the plug-in will be
passed as an argument.

---
allPlugins(a): boolean
    properties: create
    Cause all plug-ins in the search path specified
in MAYA_PLUG_IN_PATH to be loaded.

---
name(n): string
    properties: create
    Set a user defined name for the plug-ins
that are loaded.  If the name is already taken, then a number
will be added to the end of the name to make it unique.

---
quiet(qt): boolean
    properties: create
    Don't print a warning if you attempt to load a plug-in that
is already loaded.

---
removeCallback(rc): script
    properties: create
    Removes a procedure which was previously added
with -addCallback.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/loadPlugin.html 
    """


def loadPrefObjects() -> boolean:
    """Synopsis:
---
---
 loadPrefObjects()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

loadPrefObjects is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.loadPrefObjects()

---
Return:
---


    boolean: True if successful.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/loadPrefObjects.html 
    """


def loadUI(flaglistTypes: boolean, flaguiFile: string, flaguiString: string, flagverbose: boolean, flagworkingDirectory: string) -> string:
    """Synopsis:
---
---
 loadUI([listTypes=boolean], [uiFile=string], [uiString=string], [verbose=boolean], [workingDirectory=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

loadUI is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Note: mydialog.ui must already exist
dialog1 = cmds.loadUI(f='/users/username/mydialog.ui')
cmds.showWindow(dialog1)

Load from a string
dialog = ""
counter = 0

Define the button command callback
def onClick():
    global counter
    global dialog
    counter += 1
    control = "{}|verticalLayout|mybutton".format(dialog)
    cmds.button(control,
        edit=True,
        label="Clicked {} times".format(counter))
    print(counter)

Create a dialog with a button from a UI description in string form
def showDialog():
    dialogString = '''<?xml version='1.0' encoding='UTF-8'?>
        <ui version='4.0'>
        <class>Dialog</class>
        <widget class='QDialog' name='Dialog'>
        <layout class='QVBoxLayout' name='verticalLayout'>
            <item>
            <widget class='QPushButton' name='mybutton'>
            <property name='text'>
            <string>Clicked 0 times</string>
            </property>
            <property name='+command'>
            <string>"onClick()"</string>
            </property>
            </widget>
            </item>
        </layout>
        </widget>
        </ui>'''

    global dialog
    dialog = cmds.loadUI(s=dialogString)
    cmds.window(dialog, e=True, w=200, h=50)
    cmds.showWindow(dialog)

showDialog()

---
Return:
---


    string: Full path name to the root control.

Flags:
---


---
listTypes(lt): boolean
    properties: create
    Returns the list of recognized UI types and their associated Maya command.

---
uiFile(f): string
    properties: create
    Full path to a user interface file to load.

---
uiString(s): string
    properties: create
    Load UI from a formated string.

---
verbose(v): boolean
    properties: create
    Extra information about created controls will be printed.

---
workingDirectory(wd): string
    properties: create
    Sets the working directory, the loader looks for resources
such as icons and resouce files in paths relative to this directory.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/loadUI.html 
    """


def lockNode(flagignoreComponents: boolean, flaglock: boolean, flaglockName: boolean, flaglockUnpublished: boolean) -> boolean[]:
    """Synopsis:
---
---
 lockNode([ignoreComponents=boolean], [lock=boolean], [lockName=boolean], [lockUnpublished=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lockNode is undoable, queryable, and NOT editable.
Locks or unlocks one or more dependency nodes. A locked node is restricted
in the following ways:


It may not be deleted.
It may not be renamed.
Its parenting may not be changed.
Attributes may not be added to or removed from it.
Locked attributes may not be unlocked.
Unlocked attributes may not be locked.


Note that an unlocked attribute of a locked node may still have its value
set, or connections to it made or broken. For more information on attribute
locking, see the setAttr command.


If no node names are specified then the current selection list is used.


There are a few special behaviors when locking containers. Containers are
automatically expanded to their constituent objects. When a container is
locked, members of the container may not be unlocked and the container
membership may not be modified. Containers may also be set to lock unpublished
attributes. When in this state, unpublished member attributes may not have
existing connections broken, new connections cannot be made, and values on unconnected
attributes may not be modified. Parenting is allowed to change on members of locked
containers that have been published as parent or child anchors.




Example:
---
import maya.cmds as cmds

create a sphere, lock it, then try to delete it.
cmds.sphere( n='sphere1' )
cmds.lockNode( 'sphere1' )
cmds.delete( 'sphere1' )
Error: Cannot delete locked nodes.

Unlock the sphere, then it can be deleted.
cmds.lockNode( 'sphere1', lock=False )
cmds.delete( 'sphere1' )

---
Return:
---


    boolean[]: For query execution.

Flags:
---


---
ignoreComponents(ic): boolean
    properties: create, query
    Normally, the presence of a component in the list of objects to be locked
will cause the command to fail with an error. But if this flag is supplied
then components will be silently ignored.

---
lock(l): boolean
    properties: create, query
    Specifies the new lock state for the node. The default is true.

---
lockName(ln): boolean
    properties: create, query
    Specifies the new lock state for the node's name.

---
lockUnpublished(lu): boolean
    properties: create, query
    Used in conjunction with the lock flag. On a container, lock or unlock all
unpublished attributes on the members of the container. For non-containers,
lock or unlock unpublished attributes on the specified node.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lockNode.html 
    """


def loft(flagautoReverse: boolean, flagcaching: boolean, flagclose: boolean, flagconstructionHistory: boolean, flagcreateCusp: boolean, flagdegree: int, flagname: string, flagnodeState: int, flagobject: boolean, flagpolygon: int, flagrange: boolean, flagrebuild: boolean, flagreverse: boolean, flagreverseSurfaceNormals: boolean, flagsectionSpans: int, flaguniform: boolean) -> list[string]:
    """Synopsis:
---
---
 loft(
curve curve [curve...]
    , [autoReverse=boolean], [caching=boolean], [close=boolean], [constructionHistory=boolean], [createCusp=boolean], [degree=int], [name=string], [nodeState=int], [object=boolean], [polygon=int], [range=boolean], [rebuild=boolean], [reverse=boolean], [reverseSurfaceNormals=boolean], [sectionSpans=int], [uniform=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

loft is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

A loft across two curves: curve1, curve2. Curve ranges
have been enabled on the curves. The curves will be reversed
internally if needed to avoid a bowtie looking surface.
cmds.curve( d=3, p=( (-11, 0, 0), (-13, 0, -4), (-17, 0, -15), (-4.7, 0, -10), (1, 0, -8 ) ) )
Result: curve1 ---

cmds.curve( d=3, p=( (-2, 0, 5), (-2, 0, 3), (-2, 0, -1), (4, 0, 0), (7, 0, 0 ) ) )
Result: curve2 ---

cmds.loft( 'curve1', 'curve2', ch=True, rn=True, ar=True )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
autoReverse(ar): boolean
    properties: create, query, edit
    If set to true, the direction of the curves for the loft is computed automatically.  If set to false, the values of the multi-use reverse flag are used instead.
Default: true

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
close(c): boolean
    properties: create, query, edit
    If set to true, the resulting surface will be closed (periodic) with the start (end) at the first curve.  If set to false, the surface will remain open.
Default: false

---
createCusp(cc): boolean
    properties: create, query, edit, multiuse
    Multi-use flag; each occurence of the flag refers to the matching curve in the loft operation; if the flag is set the particular profile will have a cusp (tangent break) in the resulting surface.
Default: false

---
degree(d): int
    properties: create, query, edit
    The degree of the resulting surface
Default: 3

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
reverse(r): boolean
    properties: create, query, edit, multiuse
    Multi-use flag; each occurence of the flag refers to the matching curve in the loft operation; if the flag is set the particular curve will be reversed before being used in the loft operation.
Default: false

---
reverseSurfaceNormals(rsn): boolean
    properties: create, query, edit
    If set, the surface normals on the output NURBS surface will be reversed.  This is accomplished by swapping the U and V parametric directions.
Default: false

---
sectionSpans(ss): int
    properties: create, query, edit
    The number of surface spans between consecutive curves in the loft.
Default: 1

---
uniform(u): boolean
    properties: create, query, edit
    If set to true, the resulting surface will have uniform parameterization in the loft direction.  If set to false, the parameterization will be chord length.
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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/loft.html 
    """


def lookThru(flagfarClip: float, flagnearClip: float) -> None:
    """Synopsis:
---
---
 lookThru(
[editorName] [object]
    , [farClip=float], [nearClip=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lookThru is NOT undoable, queryable, and NOT editable.
Note: if there are multiple objects under the transform selected,
cameras and lights take precedence.




Example:
---
import maya.cmds as cmds

cmds.lookThru( 'cameraShape1', 'topView' )

cmds.lookThru( 'perspView', 'cameraShape1', nc=100, fc=200 )

cmds.lookThru( 'camera1' )

cmds.lookThru( 'nurbsSphere1', nc=0.001, fc=5000.0 )

cmds.lookThru( 'perspView', q=True )

cmds.lookThru( q=True )

---


Flags:
---


---
farClip(fc): float
    properties: create
    Used when setting clip far plane for a new look thru camera. Will
not affect the attributes of an existing camera.
Clip values must come before shape or view.

---
nearClip(nc): float
    properties: create
    Used when setting near clip plane for a new look thru camera. Will
not affect the attributes of an existing camera.
Clip values must come before shape or view.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lookThru.html 
    """


def ls(flagabsoluteName: boolean, flagallPaths: boolean, flagassemblies: boolean, flagcameras: boolean, flagcontainerType: string, flagcontainers: boolean, flagdagObjects: boolean, flagdefaultNodes: boolean, flagdependencyNodes: boolean, flagexactType: string, flagexcludeType: string, flagflatten: boolean, flaggeometry: boolean, flagghost: boolean, flaghead: int, flaghilite: boolean, flagintermediateObjects: boolean, flaginvisible: boolean, flagleaf: boolean, flaglights: boolean, flaglive: boolean, flaglockedNodes: boolean, flaglong: boolean, flagmaterials: boolean, flagmodified: boolean, flagnoIntermediate: boolean, flagnodeTypes: boolean, flagobjectsOnly: boolean, flagorderedSelection: boolean, flagpartitions: boolean, flagpersistentNodes: boolean, flagplanes: boolean, flagpreSelectHilite: boolean, flagreadOnly: boolean, flagrecursive: boolean, flagreferencedNodes: boolean, flagreferences: boolean, flagrenderGlobals: boolean, flagrenderQualities: boolean, flagrenderResolutions: boolean, flagrenderSetups: boolean, flagselection: boolean, flagsets: boolean, flagshapes: boolean, flagshortNames: boolean, flagshowNamespace: boolean, flagshowType: boolean, flagtail: int, flagtemplated: boolean, flagtextures: boolean, flagtransforms: boolean, flagtype: string, flagufeObjects: boolean, flagundeletable: boolean, flaguntemplated: boolean, flaguuid: boolean, flagvisible: boolean) -> list[string]:
    """Synopsis:
---
---
 ls(
[object [object...]]
    , [absoluteName=boolean], [allPaths=boolean], [assemblies=boolean], [cameras=boolean], [containerType=string], [containers=boolean], [dagObjects=boolean], [defaultNodes=boolean], [dependencyNodes=boolean], [exactType=string], [excludeType=string], [flatten=boolean], [geometry=boolean], [ghost=boolean], [head=int], [hilite=boolean], [intermediateObjects=boolean], [invisible=boolean], [leaf=boolean], [lights=boolean], [live=boolean], [lockedNodes=boolean], [long=boolean], [materials=boolean], [modified=boolean], [noIntermediate=boolean], [nodeTypes=boolean], [objectsOnly=boolean], [orderedSelection=boolean], [partitions=boolean], [persistentNodes=boolean], [planes=boolean], [preSelectHilite=boolean], [readOnly=boolean], [recursive=boolean], [referencedNodes=boolean], [references=boolean], [renderGlobals=boolean], [renderQualities=boolean], [renderResolutions=boolean], [renderSetups=boolean], [selection=boolean], [sets=boolean], [shapes=boolean], [shortNames=boolean], [showNamespace=boolean], [showType=boolean], [tail=int], [templated=boolean], [textures=boolean], [transforms=boolean], [type=string], [ufeObjects=boolean], [undeletable=boolean], [untemplated=boolean], [uuid=boolean], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ls is undoable, NOT queryable, and NOT editable.ls
The most common use of ls is to filter or
match objects based on their name (using wildcards) or based on their
type.
By default ls will match any object in the
scene but it can also be used to filter or list the selected
objects when used in conjunction with the -selection flag.

If type names are requested, using the showType flag, they
will be interleaved with object names so the result will be
pairs of <object, type> values.

Internal nodes (for example itemFilter nodes) are typically filtered
so that only scene objects are returned. However, using a wildcard
will cause all the nodes matching the wild card to show up, including
internal nodes.  For example, ls * will list all
nodes whether internal or not.

Use the syntax "::" to denote a recursive namespace search when listing nodes.
For example, ls "::pSphere1" would match objects named
"pSphere1" in any namespace, at any depth. ls "ns::*"
would match any node in namespace "ns" or children namespaces.

When Maya is in relativeNames mode, the ls command
will return names relative to the current namespace and
ls * will list from the the current namespace.
For more details, please refer to the -relativeNames
flag of the namespace command.

The command may also be passed node UUIDs instead of names/paths, and
can return UUIDs instead of names via the -uuid flag.




Example:
---
import maya.cmds as cmds

Create some objects to operate on and select them all.
Note that there are two objects named circle1;
cmds.circle( n='circle1' )
cmds.group()
cmds.circle( n='circle1' )
cmds.sphere( n='sphere1' )
cmds.group()
cmds.instance()
cmds.select( ado=True )

list all objects
cmds.ls()

List all selected objects
cmds.ls( selection=True )

List all hilited objects
cmds.ls( hilite=True )

List last selected object
cmds.ls( selection=True, tail=1 )

List all objects named "sphere1". Note that since sphere1 is
instanced, the command below lists only the first instance.
cmds.ls( 'sphere1' )

To list all instances of sphere1, use the -ap/allPaths flag.
cmds.ls( 'sphere1', ap=True )

List all selected objects named "group*"
cmds.ls( 'group*', sl=True )

List all geometry, lights and cameras in the DAG.
cmds.ls( geometry=True, lights=True, cameras=True )

List all shapes in the dag.
cmds.ls( shapes=True )

One thing to note is that it is better to always use the
-l/long flag when listing nodes without any filter. This is
because there may be two nodes with the same name (in this
example, circle1). 'ls' will list the names of all the objects
in the scene. Objects with the same name need a qualified
path name which uniquely identifies the object. A command
to select all objects such as "select `ls`" will fail because
the object lookup can't resolve which "circle1" object is
intended. To select all objects, you need the following:
cmds.select(cmds.ls(sl=True))

When trying to find a list of all objects of a specific
type, one approach might be to list all objects and then
use the nodeType command to then filter the list. As in:
allObjects = cmds.ls(l=True)
for obj in allObjects:
   if cmds.nodeType(obj) == 'surfaceShape':
     print obj

The problem with this is that 'nodeType' returns the
most derived type of the node. In this example, "surfaceShape"
is a base type for nurbsSurface so nothing will be printed.
To do this properly, the -typ/type flag should be used
to list objects of a specific type as in:
allObjects = cmds.ls(type='surfaceShape')
for obj in allObjects:
    print obj

List all geometry shapes and their types
cmds.ls( type='geometryShape', showType=True )

List all paths to all leaf nodes in the DAG
cmds.ls( dag=True, lf=True, ap=True )

List all nodes below the selected node
cmds.ls( dag=True, ap=True, sl=True )

List all ghosting objects
cmds.ls( ghost=True )

List all dag nodes that are read-only (i.e. referenced nodes)
cmds.ls( dag=True, ro=True )

List reference nodes associated with specific files
cmds.ls( references=True )

List all reference nodes, including unknown and shared reference nodes
cmds.ls( type='reference' )

Select some components and then get the list in both selected and numeric order
obj1 = cmds.polySphere( sx=20, sy=20 )
cmds.select( clear=True )

cmds.selectPref( trackSelectionOrder=1 )

cmds.select( obj1[0]+".f[100]" )
cmds.select( (obj1[0]+".f[50:55]"), add=True )
cmds.select( (obj1[0]+".f[0]"), add=True )
cmds.select( (obj1[0]+".f[56:60]"), add=True )

Regular -selection flag returns the components in compacted numeric order.
cmds.ls( selection=True )
Result:_ [u'pSphere1.f[0]', u'pSphere1.f[50:60]', u'pSphere1.f[100]'] ---


-orderedSelection flag returns the components in the order that we selected them.
cmds.ls( orderedSelection=True )
Result:_ [u'pSphere1.f[100]', u'pSphere1.f[50:55]', u'pSphere1.f[0]', u'pSphere1.f[56:60]'] ---


Turn off tracking when we are done
cmds.selectPref( trackSelectionOrder=0 )

Init some namespace
cmds.namespace( add="A:B:C" )

add object into namespace
cmds.namespace( set=":A:B" )
cmds.polySphere( name="obj1" )
cmds.namespace( set=":A:B:C" )
cmds.polySphere( name="obj1" )
cmds.polySphere( name="obj2" )


The current Namespace is ":A:B:C" and relative mode is off
List all objects and their namespace in the scene
If the object is in the root namespace, then return root ":"
Note that the results shown below have been elided (...) for documentation purposes.
cmds.ls( showNamespace=True )
Result: [u'time1', u':', u'sequenceManager1', u':', u'renderPartition', u':', (...), u'A:B:obj1', u'A:B', u'A:B:C:obj1', u'A:B:C', u'A:B:C:obj2', u'A:B:C'] ---


cmds.select( ":A:B:obj1", r=True )
cmds.select( ":A:B:C:obj2", add=True)


List namespace of all objects named "obj1"
cmds.ls( "obj1", showNamespace=True, recursive=True )
Result: [u'A:B:obj1', u'A:B', u'A:B:C:obj1', u'A:B:C'] ---


List both name and namespace of each selected object
cmds.ls( showNamespace=True, selection=True )
Result: [u'A:B:obj1', u'A:B', u'A:B:C:obj2', u'A:B:C'] ---


Set current namespace
cmds.namespace( set=":A:B" )

Enable relative mode
cmds.namespace( relativeNames=True )

Now the current namespace is ":A:B" and relative mode is on
Note that the name of the current namespace is "" in relative mode
List both name and namespace of each selected objects
cmds.ls( showNamespace=True, selection=True )
Result: [u'obj1', u'', u'C:obj2', u'C'] ---


Make a new scene, modify the transform of the camera perspective, play with the timeline and modify the camera's shape
cmds.file(force=True, new=True)
cmds.setAttr('persp.translateX', 10)
cmds.currentTime(8)
cmds.setAttr('perspShape.horizontalFilmAperture', 16)

List all modified objects of type camera and type time
allObjects=cmds.ls(type=['camera','time'], modified=True)
print allObjects
Result: [u'perspShape', u'time1']

cmds.ls(modified=True)
Result: [u'persp', u'perspShape', u'time1']

cmds.ls(modified=True, excludeType='camera')
Result: [u'persp', u'time1']

Return a node's UUID
cmds.ls( 'sphere1', uuid=True )
Result: [u'ECE85CCC-438D-8113-0236-39A6917DE484']

Find a node by UUID
cmds.ls( 'ECE85CCC-438D-8113-0236-39A6917DE484' )
Result: [u'group2|sphere1']

---
Return:
---


    list[string]: Command result

Flags:
---


---
absoluteName(an): boolean
    properties: create
    This flag can be used in conjunction with the showNamespace flag to specify
that the namespace(s) returned by the command be in absolute namespace format.
The absolute name of the namespace is a full namespace path, starting from the root namespace ":"
and including all parent namespaces.  For example ":ns:ball" is an absolute namespace
name while "ns:ball" is not.
The absolute namespace name is invariant and is not affected by the current namespace or
relative namespace modes.

---
allPaths(ap): boolean
    properties: create
    List all paths to nodes in DAG. This flag only works
if -dag is also specified or if an object name is
supplied.

---
assemblies(assemblies): boolean
    properties: create
    List top level transform Dag objects

---
cameras(ca): boolean
    properties: create
    List camera shapes.

---
containerType(ct): string
    properties: create, multiuse
    List containers with the specified user-defined type.
 This flag cannot be used in conjunction with the type or exactType flag.

---
containers(con): boolean
    properties: create
    List containers. Includes both standard containers as well as other types of
containers such as dagContainers.

---
dagObjects(dag): boolean
    properties: create
    List Dag objects of any type. If object name arguments are
passed to the command then this flag will list all Dag objects
below the specified object(s).

---
defaultNodes(dn): boolean
    properties: create
    Returns default nodes.
A default node is one that Maya creates automatically and does not get
saved out with the scene, although some of its attribute values may.

---
dependencyNodes(dep): boolean
    properties: create
    List dependency nodes. (including Dag objects)

---
exactType(et): string
    properties: create, multiuse
    List all objects of the specified type, but not objects that are
descendents of that type. This flag can appear
multiple times on the command line. Note: the type passed to
this flag is the same type name returned from the showType
flag.
 This flag cannot be used in conjunction with the type or excludeType flag.

---
excludeType(ext): string
    properties: create, multiuse
    List all objects that are not of the specified type.
This flag can appear multiple times on the command line. Note: the type passed to
this flag is the same type name returned from the showType flag.
 This flag cannot be used in conjunction with the type or exactType flag.

---
flatten(fl): boolean
    properties: create
    Flattens the returned list of objects so that each component
is identified individually.

---
geometry(g): boolean
    properties: create
    List geometric Dag objects.

---
ghost(gh): boolean
    properties: create
    List ghosting objects.

---
head(hd): int
    properties: create
    This flag  specifies the maximum number of elements to be
returned from the beginning of the list of items.
Note: each type flag will return at most this many items so
if multiple type flags are specified then the number of items
returned can be greater than this amount.

---
hilite(hl): boolean
    properties: create
    List objects that are currently hilited for component selection.

---
intermediateObjects(io): boolean
    properties: create
    List only intermediate dag nodes.

---
invisible(iv): boolean
    properties: create
    List only invisible dag nodes.

---
leaf(lf): boolean
    properties: create
    List all leaf nodes in Dag. This flag is a modifier and must
be used in conjunction with the -dag flag.

---
lights(lt): boolean
    properties: create
    List light shapes.

---
live(lv): boolean
    properties: create
    List objects that are currently live.

---
lockedNodes(ln): boolean
    properties: create
    Returns locked nodes, which cannot be deleted or renamed. However, their status may change.

---
long(l): boolean
    properties: create
    Return full path names for Dag objects. By default the
shortest unique name is returned.

---
materials(mat): boolean
    properties: create
    List materials or shading groups.

---
modified(mod): boolean
    properties: create
    When this flag is set, only nodes modified since the last save will be returned.

---
noIntermediate(ni): boolean
    properties: create
    List only non intermediate dag nodes.

---
nodeTypes(nt): boolean
    properties: create
    Lists all registered node types.

---
objectsOnly(o): boolean
    properties: create
    When this flag is set only object names will be returned and
components/attributes will be ignored.

---
orderedSelection(os): boolean
    properties: create
    List objects and components that are currently selected in their order of selection.  This flag depends
on the value of the -tso/trackSelectionOrder flag of the selectPref command.  If that flag is not
enabled than this flag will return the same thing as the -sl/selection flag would.

---
partitions(pr): boolean
    properties: create
    List partitions.

---
persistentNodes(pn): boolean
    properties: create
    Returns persistent nodes, which are nodes that stay in the Maya session after a file > new.
These are a special class of default nodes that do not get reset on file > new.
Ex: itemFilter and selectionListOperator nodes.

---
planes(pl): boolean
    properties: create
    List construction plane shapes.

---
preSelectHilite(psh): boolean
    properties: create
    List components that are currently hilited for pre-selection.

---
readOnly(ro): boolean
    properties: create
    Returns referenced nodes. Referenced nodes are read only.
NOTE: Obsolete. Please use "-referencedNodes".

---
recursive(r): boolean
    properties: create
    When set to true, this command will look for name matches
in all namespaces. When set to false, this command will only look
for matches in namespaces that are requested (e.g. by specifying
a name containing the ':'... "ns1:pSphere1").

---
referencedNodes(rn): boolean
    properties: create
    Returns referenced nodes. Referenced nodes are read only.

---
references(rf): boolean
    properties: create
    List references associated with files. Excludes special reference
nodes such as the sharedReferenceNode and unknown reference nodes.

---
renderGlobals(rg): boolean
    properties: create
    List render globals.

---
renderQualities(rq): boolean
    properties: create
    List named render qualities.

---
renderResolutions(rr): boolean
    properties: create
    List render resolutions.

---
renderSetups(rs): boolean
    properties: create
    Alias for -renderGlobals.

---
selection(sl): boolean
    properties: create
    List objects that are currently selected.

---
sets(set): boolean
    properties: create
    List sets.

---
shapes(s): boolean
    properties: create
    List shape objects.

---
shortNames(sn): boolean
    properties: create
    Return short attribute names. By default long attribute names
are returned.

---
showNamespace(sns): boolean
    properties: create
    Show the namespace of each object after the object name.
 This flag cannot be used in conjunction with the showType flag.

---
showType(st): boolean
    properties: create
    List the type of each object after its name.

---
tail(tl): int
    properties: create
    This flag specifies the maximum number of elements to be
returned from the end of the list of items.
Note: each    type flag will return at most this many items so
if multiple type flags are specified then the number of items
returned can be greater than this amount

---
templated(tm): boolean
    properties: create
    List only templated dag nodes.

---
textures(tex): boolean
    properties: create
    List textures.

---
transforms(tr): boolean
    properties: create
    List transform objects.

---
type(typ): string
    properties: create, multiuse
    List all objects of the specified type. This flag can appear
multiple times on the command line. Note: the type passed to
this flag is the same type name returned from the showType
flag. Note: some selection items in Maya do not have a specific
object/data type associated with them and will return "untyped"
when listed with this flag.
 This flag cannot be used in conjunction with the exactType or excludeType flag.

---
ufeObjects(ufe): boolean
    properties: create
    When used in conjunction with the -sl/selection flag, will return objects that are
defined through the UFE interface as well as native Maya objects.

---
undeletable(ud): boolean
    properties: create
    Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.

---
untemplated(ut): boolean
    properties: create
    List only un-templated dag nodes.

---
uuid(uid): boolean
    properties: create
    Return node UUIDs instead of names.
Note that there are no "UUID paths" - combining this
flag with e.g. the -long flag will not result in a path
formed of node UUIDs.

---
visible(v): boolean
    properties: create
    List only visible dag nodes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ls.html 
    """


def lsThroughFilter(flagitem: string, flagnodeArray: boolean, flagreverse: boolean, flagselection: boolean, flagsort: string) -> list[string]:
    """Synopsis:
---
---
 lsThroughFilter(
string
    , [item=string], [nodeArray=boolean], [reverse=boolean], [selection=boolean], [sort=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lsThroughFilter is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Return all objects in the model that are named bob.
(See the command "itemFilter" for how to construct these filters.)
cmds.lsThroughFilter( 'texturesNamedBobFilter' )

Return same objects as above, but sorted in reverse
alphabetical order:
cmds.lsThroughFilter( 'texturesNamedBobFilter', na=True, sort='byName', reverse=True )

---
Return:
---


    list[string]: List of nodes passing the filter

Flags:
---


---
item(it): string
    properties: create, multiuse
    Run the filter on specified node(s), using the fast
version of this command.

---
nodeArray(na): boolean
    properties: create
    Fast version that runs an entire array of
nodes through the filter at one time.

---
reverse(rv): boolean
    properties: create
    Only available in conjunction with nodeArray flag.
Reverses the order of nodes in the returned arrays if true.

---
selection(sl): boolean
    properties: create
    Run the filter on selected nodes only, using the fast
version of this command.

---
sort(so): string
    properties: create
    Only available in conjunction with nodeArray flag.
Orders the nodes in the returned array. Current options are:
"byName", "byType", and "byTime".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lsThroughFilter.html 
    """


def lsUI(flagcmdTemplates: boolean, flagcollection: boolean, flagcontexts: boolean, flagcontrolLayouts: boolean, flagcontrols: boolean, flagdumpWidgets: boolean, flageditors: boolean, flaghead: int, flaglong: boolean, flagmenuItems: boolean, flagmenus: boolean, flagnumWidgets: boolean, flagpanels: boolean, flagradioMenuItemCollections: boolean, flagtail: int, flagtype: string, flagwindows: boolean, flagworkspaceControls: boolean) -> list[string]:
    """Synopsis:
---
---
 lsUI(
[objects]
    , [cmdTemplates=boolean], [collection=boolean], [contexts=boolean], [controlLayouts=boolean], [controls=boolean], [dumpWidgets=boolean], [editors=boolean], [head=int], [long=boolean], [menuItems=boolean], [menus=boolean], [numWidgets=boolean], [panels=boolean], [radioMenuItemCollections=boolean], [tail=int], [type=string], [windows=boolean], [workspaceControls=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

lsUI is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

   List all windows.
---

cmds.lsUI( windows=True )

   List all panels and editors.
---

cmds.lsUI( panels=True, editors=True )

   Use the -typ/type flag to list all controls and control layouts.
   Alternatively, you could use the -ctl/controls and -cl/controlLayouts
   flags.
---

cmds.lsUI( type=['control','controlLayout'] )

   Or...
---

cmds.lsUI( controls=True, controlLayouts=True )

---
Return:
---


    list[string]: The names of the object arguments.

Flags:
---


---
cmdTemplates(ct): boolean
    properties: create
    UI command templates created using ELF UI commands.

---
collection(col): boolean
    properties: create
    Control collections created using ELF UI commands.

---
contexts(ctx): boolean
    properties: create
    Tool contexts created using ELF UI commands.

---
controlLayouts(cl): boolean
    properties: create
    Control layouts created using ELF UI commands [e.g. formLayouts, paneLayouts, etc.]

---
controls(ctl): boolean
    properties: create
    Controls created using ELF UI commands. [e.g. buttons, checkboxes, etc]

---
dumpWidgets(dw): boolean
    properties: create
    Dump all QT widgets used by Maya.

---
editors(ed): boolean
    properties: create
    All currently existing editors.

---
head(hd): int
    properties: create
    The parameter specifies the maximum number of elements to be returned
from the beginning of the list of items. (Note: each flag
will return at most this many items so if multiple flags are specified
then the number of items returned will be greater than the value
specified).

---
long(l): boolean
    properties: create
    Use long pathnames instead of short non-path names.

---
menuItems(mi): boolean
    properties: create
    Menu items created using ELF UI commands.

---
menus(m): boolean
    properties: create
    Menus created using ELF UI commands.

---
numWidgets(nw): boolean
    properties: create
    Reports the number of QT widgets used by Maya.

---
panels(p): boolean
    properties: create
    All currently existing panels.

---
radioMenuItemCollections(rmc): boolean
    properties: create
    Menu item collections created using ELF UI commands.

---
tail(tl): int
    properties: create
    The parameter specifies the maximum number of elements to be returned
from the end of the list of items. (Note: each flag
will return at most this many items so if multiple flags are specified
then the number of items returned will be greater than the value
specified).

---
type(typ): string
    properties: create, multiuse
    List all objects of a certain type specified by the string argument.
For example, "window", "menu", "control", or "controlLayout".

---
windows(wnd): boolean
    properties: create
    Windows created using ELF UI commands.

---
workspaceControls(wc): boolean
    properties: create
    Workspace controls created using ELF UI commands.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/lsUI.html 
    """
