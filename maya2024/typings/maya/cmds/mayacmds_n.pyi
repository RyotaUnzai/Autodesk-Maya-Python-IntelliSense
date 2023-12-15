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


def nBase(flagclearCachedTextureMap: string, flagclearStart: boolean, flagstuffStart: boolean, flagtextureToVertex: string) -> boolean:
    """Synopsis:
---
---
 nBase([clearCachedTextureMap=string], [clearStart=boolean], [stuffStart=boolean], [textureToVertex=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nBase is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Stuff the current positions and velocities into nCloth1's startPositions and
startVelocities.
---

cmds.nBase( 'nCloth1', e=True, stuffStart=True )

Clear nCloth1's startPositions and startVelocities.
---

cmds.nBase( 'nCloth1', e=True, clearStart=True )

Transfer the texture map data for the thicknessMap attribute into the
thicknessPerVertex attribute.
---

cmds.nBase( 'nCloth1', e=True, textureToVertex='thicknessMap' )

---
Return:
---


    boolean: Command result

Flags:
---


---
clearCachedTextureMap(cct): string
    properties: create, edit
    Clear the cached texture map for the specified attribute from
the nBase.

---
clearStart(cs): boolean
    properties: create, edit
    Indicates that start state should be cleared

---
stuffStart(ss): boolean
    properties: create, edit
    Indicates that current state should be stuffed into the start state

---
textureToVertex(ttv): string
    properties: create, edit
    Transfer the texture map data for the specified attribute into
the related per-vertex attribute.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nBase.html 
    """


def nParticle(flagattribute: string, flagcache: boolean, flagconserve: float, flagcount: boolean, flagdeleteCache: boolean, flagdynamicAttrList: boolean, flagfloatValue: float, flaggridSpacing: linear, flaginherit: float, flagjitterBasePoint: tuple[linear, linear, linear], flagjitterRadius: linear, flaglowerLeft: tuple[linear, linear, linear], flagname: string, flagnumJitters: uint, flagorder: int, flagparticleId: int, flagperParticleDouble: boolean, flagperParticleVector: boolean, flagposition: tuple[linear, linear, linear], flagshapeName: string, flagupperRight: tuple[linear, linear, linear], flagvectorValue: tuple[float, float, float]) -> string:
    """Synopsis:
---
---
 nParticle(
selectionItem
    , [attribute=string], [cache=boolean], [conserve=float], [count=boolean], [deleteCache=boolean], [dynamicAttrList=boolean], [floatValue=float], [gridSpacing=linear], [inherit=float], [jitterBasePoint=[linear, linear, linear]], [jitterRadius=linear], [lowerLeft=[linear, linear, linear]], [name=string], [numJitters=uint], [order=int], [particleId=int], [perParticleDouble=boolean], [perParticleVector=boolean], [position=[linear, linear, linear]], [shapeName=string], [upperRight=[linear, linear, linear]], [vectorValue=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nParticle is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Creates a particle object with four particles
cmds.nParticle( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)] )

Returns the age of the particle with id 2 in object particle1
cmds.nParticle( 'particle1', q=True, attribute='age', id=2 )

Returns the velocity of the 3rd particle in the currently selected
particle object
cmds.nParticle( attribute='velocity', q=True, order=3  )

Edits the velocity of the 7th particle in the currently selected
particle object to be 0.0, 1.0, 0.0
cmds.nParticle( e=True, attribute='velocity', order=3, vectorValue=(0.0, 1.0, 0.0) )

Edits the mass of the particle in "particle1" with id 3 to be 0.7
cmds.nParticle( 'nParticle1', e=True, attribute='mass', id=3, fv=0.7 )

---
Return:
---


    string: The name of the nParticle object created

Flags:
---


---
attribute(at): string
    properties: query, edit
    Used in per particle attribute query and edit. Specifies the
name of the attribute being queried or edited.
      In query mode, this flag needs a value.

---
cache(ch): boolean
    properties: create, query, edit
    Turns caching on/off for the particle shape.

---
conserve(c): float
    properties: query, edit
    Conservation of momentum control (between 0 and 1).  Specifies
the fraction of the particle shape's existing momentum which is
conserved from frame to frame.
A value of 1 (the default) corresponds to true Newtonian physics,
in which momentum is conserved.

---
count(ct): boolean
    properties: query
    Returns the number of particles in the object.

---
deleteCache(dc): boolean
    properties: create
    Deletes the particle shapes cache. This command is not undoable.

---
dynamicAttrList(dal): boolean
    properties: query
    Returns a list of the dynamic attributes in the object.

---
floatValue(fv): float
    properties: edit
    Used only in per particle attribute edit.  Specifies that the edit is
of a float attribute and must be followed by the new float value.

---
gridSpacing(grs): linear
    properties: create, query, multiuse
    Spacing between particles in the grid.

---
inherit(i): float
    properties: query, edit
    Inherit this fraction (0-1) of emitting object's velocity.

---
jitterBasePoint(jbp): [linear, linear, linear]
    properties: create, query, multiuse
    Base point (center point) for jitters.  The command will create
one swatch of jitters for each base point.  It will pair up
other flags with base points in the order they are given in the
command line.  If not enough instances of the other flags are
availble, the last one on the line with be used for all other
instances of -jpb.

---
jitterRadius(jr): linear
    properties: create, query, multiuse
    Max radius from the center to place the particle instances.

---
lowerLeft(ll): [linear, linear, linear]
    properties: create, query, multiuse
    Lower left point of grid.

---
name(n): string
    properties: query, edit
    name of particle object

---
numJitters(nj): uint
    properties: create, query, multiuse
    Number of jitters (instances) per particle.

---
order(order): int
    properties: query, edit
    Used in per particle attribute query and edit. Specifies the
zero-based order (index) of the particle whose attribute is being
queried  or edited in the
particle array. Querying the value of a per particle attribute
requires the -attribute and -id or -order flags and their arguments
to precede the -q flag.
      In query mode, this flag needs a value.

---
particleId(id): int
    properties: query, edit
    Used in per particle attribute query and edit. Specifies the
id of the particle whose attribute is being queried or edited.
Querying the value of a per particle attribute
requires the -attribute and -id or -order flags and their arguments
to precede the -q flag.
      In query mode, this flag needs a value.

---
perParticleDouble(ppd): boolean
    properties: query
    Returns a list of the per-particle double attributes,
excluding initial-state, cache, and information-only attributes.

---
perParticleVector(ppv): boolean
    properties: query
    Returns a list of the per-particle vector attributes,
excluding initial-state, cache, and information-only attributes.

---
position(p): [linear, linear, linear]
    properties: multiuse
    World-space position of each particle.

---
shapeName(sn): string
    properties: query, edit
    Specify the shape name used for geometry instancing.
DO not confuse this with the -n flag which names the particle object.

---
upperRight(ur): [linear, linear, linear]
    properties: create, query, multiuse
    Upper right point of grid.

---
vectorValue(vv): [float, float, float]
    properties: edit
    Used only in per particle attribute edit.  Specifies that the edit is
of a vector attribute and must be followed by all three float values
for the vector.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nParticle.html 
    """


def nSoft(flagconvert: boolean, flagduplicate: boolean, flagduplicateHistory: boolean, flaggoal: float, flaghideOriginal: boolean) -> string:
    """Synopsis:
---
---
 nSoft(
selectionList
    , [convert=boolean], [duplicate=boolean], [duplicateHistory=boolean], [goal=float], [hideOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nSoft is undoable, queryable, and NOT editable.

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
them, then reparent the structure outside the hierarchy.

When duplicating, the nSoft portion (the duplicate) is given the name
"copyOf" + "original object name".  The particle portion is always
given the name "original object name" + "Particles."

None of the flags of the nSoft command can be queried.  The nSoft -q
command is used only to identify when an object is a nSoft body,
or when two objects are part of the same nSoft body.
See the examples.




Example:
---
import maya.cmds as cmds

cmds.sphere()
cmds.nSoft( 'nurbsSphere1', c=True )

Creates a sphere named nurbsSphere1 and converts nurbSphere1 into
a nSoft object. The particle portion of the nSoft object will
be parented (with its own transform) under nurbsSphere1.

cmds.sphere()
cmds.nSoft( 'nurbsSphere1', d=True )

Same as the previous example, except that the nSoft command will make
a duplicate of nurbsSphereShape1. The resulting nSoft body will be
completely independent of nurbSphere1 and its children. Input connections
to nurbsSphereShape1 will be duplicated, but not any upstream history
(in other words, just plain "duplicate").

cmds.sphere()
cmds.nSoft( 'nurbsSphere1', dh=True )

Same as the previous example, except that upstream history on
nurbsSphereShape1 will be duplicated as well (equivalent to
"duplicate history").

cmds.sphere()
cmds.nSoft( 'nurbSphere1', g=0.3 )

This will make a duplicate of the shape under nurbSphere1 (as for -d),
and use it as the shape for the newly created nSoft object.
The original nurbsSphereShape1 will be made a goal for the particles of
softy, with a goal weight of 0.3. This will make those particles try to
follow nurbSphere1 loosely as it moves around.

cmds.nSoft( 'foobar', q=True )
Returns true if foobar is a nSoft object.

cmds.nSoft( 'foobar', 'foobarParticles', q=True )

Returns true if foobar and foobarParticles are parts of the same
nSoft object. This is useful because when you select a nSoft body,
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
nSoft body will be inserted in the same hierarchy as the original,
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
also have a copy of it that was a nSoft body.
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
you want the resulting nSoft body to try to
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
whichever of the two objects is NOT the nSoft object will be hidden.
In other words, with -d -h true, the original object will be hidden;
with -d -c -h 1 the duplicate object will be hidden.
You would typically do this if you want to use the non-dynamic object as
a goal for the nSoft one (see -g) but you do not want it visible in the scene.
The flags -h 1 and -c are mutually exclusive.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nSoft.html 
    """


def nameCommand(flagannotation: string, flagcommand: script, flagdata1: string, flagdata2: string, flagdata3: string, flagdefault: boolean, flagsourceType: string) -> string:
    """Synopsis:
---
---
 nameCommand(
[string]
    , [annotation=string], [command=script], [data1=string], [data2=string], [data3=string], [default=boolean], [sourceType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nameCommand is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a nameCommand object.
---

cmds.nameCommand( 'circleToolNameCommand', ann='The Circle Tool', c='cmds.setToolTo("circleContext")' )

Now map the nameCommand to a hotkey.
---

cmds.hotkey( keyShortcut='F5', altModifier=True, name='circleToolNameCommand' )

---
Return:
---


    string: The name of the nameCommand object created

Flags:
---


---
annotation(ann): string
    properties: create
    A description of the command.

---
command(c): script
    properties: create
    The command that is executed
when the nameCommand is invoked.

---
data3(da3): string
    properties: create
    These are optional, user-defined data strings that
are attached to the nameCommand object.  They can be
edited or queried using the assignCommand command.

---
default(d): boolean
    properties: create
    Indicate that this name command is a default command.
Default name commands will not be saved to preferences.

---
sourceType(stp): string
    properties: create
    Sets the language type for the command script. Can only be used in conjunction with the -command flag.
Valid values are "mel" (enabled by default), and "python".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nameCommand.html 
    """


def nameField(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdrawInactiveFrame: boolean, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnameChangeCommand: script, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagobject: string, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagreceiveFocusCommand: script, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 nameField(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [drawInactiveFrame=boolean], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [nameChangeCommand=script], [noBackground=boolean], [numberOfPopupMenus=boolean], [object=string], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [receiveFocusCommand=script], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nameField is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a window containing a single name field. Associate
   the name field with a sphere.
---

window = cmds.window('window')
cmds.columnLayout( adjustableColumn=True )
sphereName = cmds.sphere()
field = cmds.nameField(object=sphereName[0])
cmds.showWindow( window )

   Rename the sphere and notice that the name field updates.
---

objectName = cmds.nameField(field, query=True, object=True)
cmds.rename( objectName, 'NewName' )

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
    properties: create, query, edit
    This command is executed when the field text is changed by the user.

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
drawInactiveFrame(dif): boolean
    properties: create, query, edit
    Sets whether the name field draws itself with a frame when it is inactive.
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
nameChangeCommand(ncc): script
    properties: create, query, edit
    This command is executed when the name of the node changes.
NOTE: this will be executed when the node name changes, whether
or not the name-change originated with the user typing
into the field. If you want to attach a command to be executed
when the user types into the field, use the -cc/changeCommand flag.

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
object(o): string
    properties: create, query, edit
    Attaches the field to the named dag/ufe object, so that
the field will always display the object's name.

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
    properties: create, query, edit
    Command executed when the field receives focus.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nameField.html 
    """


def namespace(flagabsoluteName: boolean, flagaddNamespace: string, flagcollapseAncestors: string, flagdeleteNamespaceContent: boolean, flagexists: string, flagforce: boolean, flagisRootNamespace: string, flagmergeNamespaceWithOther: string, flagmergeNamespaceWithParent: boolean, flagmergeNamespaceWithRoot: boolean, flagmoveNamespace: tuple[string, string], flagparent: string, flagrecurse: boolean, flagrelativeNames: boolean, flagremoveNamespace: string, flagrename: tuple[string, string], flagsetNamespace: string, flagvalidateName: string) -> string:
    """Synopsis:
---
---
 namespace(
[string]
    , [absoluteName=boolean], [addNamespace=string], [collapseAncestors=string], [deleteNamespaceContent=boolean], [exists=string], [force=boolean], [isRootNamespace=string], [mergeNamespaceWithOther=string], [mergeNamespaceWithParent=boolean], [mergeNamespaceWithRoot=boolean], [moveNamespace=[string, string]], [parent=string], [recurse=boolean], [relativeNames=boolean], [removeNamespace=string], [rename=[string, string]], [setNamespace=string], [validateName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

namespace is undoable, queryable, and NOT editable.
A namespace is a simple grouping of objects under a given name.
Namespaces are primarily used to resolve name-clash issues in Maya,
where a new object has the same name as an existing object (from
importing a file, for example).  Using namespaces, you can have two
objects with the same name, as long as they are contained in
differenct namespaces.

Namespaces are reminiscent of hierarchical structures like file
systems where namespaces are analogous to directories and objects are
analogous to files. The colon (':') character is the separator used to
separate the names of namespaces and nodes instead of the slash ('/')
or backslash ('\') character.  Namespaces can contain other namespaces
as well as objects.  Like objects, the names of namespaces must be
unique within another namespace. Objects and namespaces can be in only
one namespace. Namespace names and object names don't clash so a
namespace and an object contained in another namespace can have the
same name.

There is an unnamed root namespace specified with a leading colon
(':').  Any object not in a named namespace is in the root namespace.
Normally, the leading colon is omitted from the name of an object as
it's presence is implied. The presence of a leading colon is
important when moving objects between namespaces using the 'rename'
command.  For the 'rename' command, the new name is relative to the
current namespace unless the new name is fully qualified with a
leading colon.

Namespaces are created using the 'add/addNamespace' flag. By default they are
created under the current namespace. Changing the current namespace is
done with the 'set/setNamespace' flag. To reset the current namespace to
the root namespace, use 'namespace -set ":";'. Whenever an object is
created, it is added by default to the current namespace.

When creating a new namespace using a qualified name, any intervening namespaces which do
not yet exist will be automatically created. For example, if the name of
the new namespace is specified as "A:B" and the current namespace already
has a child namespace named "A" then a new child namespace named "B" will
be created under "A". But if the current namespace does not yet have a
child named "A" then it will be created automatically. This applies
regardless of the number of levels in the provided name (e.g. "A:B:C:D").

The 'p/parent' flag can be used to explicitly specify the parent namespace
under which the new one should be created, rather than just defaulting to
the current namespace.

If the name given for the new namespace is absolute (i.e. it begins with a
colon, as in ":A:B") then both the current namespace and the 'parent' flag
will be ignored and the new namespace will be created under the root namespace.

The relativeNamespace flag can be used to change the way node names
are displayed in the UI and returned by the 'ls' command. Here are
some specific details on how the return from the 'ls' command works in
relativeNamespace mode:

List all mesh objects in the scene:
ls -type "mesh";
The above command lists all mesh objects in the root and any child namespaces. In relative name lookup mode, all names will be displayed relative to the current namespace. When not in relative name lookup mode (the default behaviour in Maya), results are printed relative to the root namespace.

Using a "*" wildcard:
namespace -set myNS;
ls -type "mesh "*";

In relative name lookup mode, the "*" will match to the current namespace and thus the ls command will list only those meshes defined within the current namespace (i.e. myNs). If relative name lookup is off (the default behaviour in Maya), names are root-relative and thus "*" matches the root namespace, with the net result being that only thoses meshes defined in the root namespace will be listed.

You can force the root namespace to be listed when in relative name lookup mode by specifying ":*" as your search pattern (i.e.
ls -type mesh ":*" which lists those meshes defined in the root namespace only). Note that you can also use ":*" when relative name lookup mode is off to match the root if you want a consistent way to list the root.

Listing child namespace contents:
ls -type mesh "*:*";

For an example to list all meshes in immediate child namespaces, use "*:*". In relative name lookup mode "*:*" lists those meshes in immediate child namespaces of the current namespaces. When not in relative name lookup mode, "*:*" lists meshes in namespaces one level below the root.

Recursive listing of namespace contents:
Example: ls -type mesh -recurse on "*"

The 'recurse' flag is provided on the "ls" command to recursively traverse any child namespaces. In relative name lookup mode, the above example command will list all meshes in the current and any child namespaces of current. When not in relative name lookup mode, the above example command works from the root downwards and is thus equivalent to "ls -type mesh".





Example:
---
import maya.cmds as cmds

Create three namespaces
cmds.namespace( add='FOO' )
cmds.namespace( add='BAR' )
cmds.namespace( add='FRED' )

Create namespace with qualified name
cmds.namespace( add="A:B" )

Create namespace with qualified name
cmds.namespace( add="C:D", parent="A:B" )

Create namespace with qualified name
cmds.namespace( add=":A:B:C:D:E" )

Set the current namespace to FOO
cmds.namespace( set='FOO' )

Create the namespace BAR Under FOO. Note there are
two "BAR" namespaces, :BAR and :FOO:BAR.
cmds.namespace( add='BAR' )

Validate the name
cmds.namespace( validateName="name$space" );
Result: name_space

Check to see that the BAR namespace exists within the current
namespace (FOO)
cmds.namespace( exists='BAR' )
Result: 1 ---


Check to see that the FRED namespace exists under the root namespace
cmds.namespace( exists=':FRED' )
Result: 1 ---


Create two objects. It gets added to the current namespace FOO;
cmds.sphere( n='sphere1' )
cmds.sphere( n='sphere2' )
Result: FOO:sphere2 ---


Move sphere1 from namespace FOO to FOO:BAR. Note that we
need to qualify sphere1 with the namespace FOO because
"sphere1" identifies a non-existent object in the root namespace.
cmds.rename( 'FOO:sphere1', 'BAR:sphere1' )
Result: FOO:BAR:sphere1 ---


Move sphere2 from namespace FOO to BAR.  Note the leading
colon on the new name.
cmds.rename( 'FOO:sphere2', ':BAR:sphere2' )
Result: BAR:sphere2 ---


query the current namespace (using the namespaceInfo command)
cmds.namespaceInfo( currentNamespace=True )
Result: FOO ---


remove the namespace FRED (it must be empty)
cmds.namespace( set=':' )
cmds.namespace( rm='FRED' )

Check to see that the FRED namespace has been removed
cmds.namespace( exists=':FRED' )
Result: 0 ---


Rename namespace BAR to JOE
Note: this is done by creating JOE, moving the contents of
BAR into JOE, and then removing the (now empty) BAR.
cmds.namespace( set=':' )
cmds.namespace( add='JOE' )
cmds.namespace( mv=('BAR', 'JOE') )
cmds.namespace( rm='BAR' )

JOE should now contain a single node: 'sphere2'.
Move the contents of JOE into FRANK, when FRANK already
has a 'sphere2' node. The '-force'
flag is needed.
cmds.namespace( set=':' )
cmds.namespace( add='FRANK' )
cmds.namespace( set='FRANK' )
cmds.sphere( n='sphere2' )
cmds.namespace( force=True, mv=(':JOE', ':FRANK') )
In moving 'sphere2' from JOE to FRANK it will be renamed to
'sphere3' to ensure uniqueness.
The namespace FRANK should now contain 'sphere2', 'sphere2Shape',
and 'sphere3'.

Determine whether the given namespace is root
---

cmds.namespace( query=True, isRootNamespace="FOO" )

---
Set return value to be absolute namespace name
---

print(cmds.namespace(add = "testAbsoluteName", absoluteName = True))

---
Create a sample hierachy that contains only empty namespaces, then collapse it
---

cmds.namespace( set = ":")
cmds.namespace( add = "emptyLevel1")
cmds.namespace( add = "emptyLevel2", parent = "emptyLevel1")
cmds.namespace( add = "leaf", parent = "emptyLevel1:emptyLevel2")
cmds.namespace( collapseAncestors = "emptyLevel1:emptyLevel2:leaf")

Create a sample for removing an existed namespace.
This command can also be used together with these options:
deleteNamespaceContent
mergeNamespaceWithParent
mergeNamespaceWithRoot
mergeNamespaceWithOther
---

The functionality of the three option parameters will also be displayed in the
following sample.
Note: The three option parameters are mutually exclusive.
      Without any option parameters specified, the default way it performances that
      it can only remove a namespace that is empty. If you want to remove any namespace
      with contents, please add option parameter deleteNamespaceContent.
---

cmds.namespace( set = ":")
cmds.namespace( add = ":RM_TEST_ROOT:FOO:BAR:JOE")
cmds.sphere( name = ":RM_TEST_ROOT:FOO:obj1")
cmds.sphere( name = ":RM_TEST_ROOT:FOO:BAR:obj2")

Trying to remove a namespace that is not empty without option parameter,
user will get an error message show that maya cannot remove a namespace that
is not empty.
---

---
cmds.namespace( removeNamespace = ":RM_TEST_ROOT:FOO") Run this command you'll get an error.

Trying to remove an empty namespace.
Namespace :RM_TEST_ROOT:FOO:BAR:JOE has been removed successfully by the command.
---

cmds.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR:JOE")

cmds.undo()

Usage of deleteNamespaceContent option parameter:
Remove all the contents in the target namespace specified in the command and
remove the namespace
---

cmds.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR", deleteNamespaceContent = True)

cmds.undo()

Usage of mergeNamespaceWithParent parameter:
Move the content of the target namespace specified in the command to its parent
namespace and remove the namespace.
---

cmds.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR", mergeNamespaceWithParent = True)

cmds.undo()

Usage of mergeNamespaceWithRoot parameter:
Move the content of the target namespace specified in the command to the root
namespace and remove the namespace.
---

cmds.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR", mergeNamespaceWithRoot = True)

---
Return:
---


    string: Command result

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
addNamespace(add): string
    properties: create
    Create a new namespace with the given name. Both qualified names ("A:B") and unqualified names ("A") are acceptable. If any of the higher-level namespaces in a qualified name do not yet exist, they will be created.
If the supplied name contains invalid characters it will first be modified as per the validateName flag.

---
collapseAncestors(ch): string
    properties: create
    Delete all empty ancestors of the given namespace.
An empty namespace is a a namespace that does not contain any objects
or other nested namespaces

---
deleteNamespaceContent(dnc): boolean
    properties: create
    Used with the 'rm/removeNamespace' flag to indicate that when removing a namespace
the contents of the namespace will also be removed.

---
exists(ex): string
    properties: create
    Returns true if the specified namespace exists, false if not.

---
force(f): boolean
    properties: create
    Used with 'mv/moveNamespace' to force the move operation to ignore
name clashes.

---
isRootNamespace(ir): string
    properties: query
    Returns true if the specified namespace is root, false if not.

---
mergeNamespaceWithOther(mno): string
    properties: create
    Used with the 'rm/removeNamespace' flag.
When removing a namespace, move the rest of the namespace
content to the specified namespace.

---
mergeNamespaceWithParent(mnp): boolean
    properties: create
    Used with the 'rm/removeNamespace' flag.
When removing a namespace, move the rest of the namespace
content to the parent namespace.

---
mergeNamespaceWithRoot(mnr): boolean
    properties: create
    Used with the 'rm/removeNamespace' flag.
When removing a namespace, move the rest of the namespace
content to the root namespace.

---
moveNamespace(mv): [string, string]
    properties: create
    Move the contents of the first namespace into the second namespace.
Child namespaces will also be moved.

Attempting to move a namespace containing referenced nodes will
result in an error; use the 'file' command ('file -edit -namespace')
to change a reference namespace.

If there are objects in the source namespace with the same name as
objects in the destination namespace, an error will be issued. Use
the 'force' flag to override this error - name clashes will be
resolved by renaming the objects to ensure uniqueness.

---
parent(p): string
    properties: create
    Used with the 'addNamespace' or 'rename' flags to specifiy
the parent of the new namespace. The full namespace parent path is required.
When using 'addNamespace' with an absolute name, the 'parent' will be ignored
and the command will display a warning

---
recurse(r): boolean
    properties: query
    Can be used with the 'exists' flag to recursively look for the
specified namespace

---
relativeNames(rel): boolean
    properties: create, query
    Turns on relative name lookup, which causes name lookups within Maya
to be relative to the current namespace. By default this is off, meaning
that name lookups are always relative to the root namespace. Be careful
turning this feature on since commands such as setAttr will behave
differently. It is wise to only turn this feature on while executing
custom procedures that you have written to be namespace independent and
turning relativeNames off when returning control from your custom procedures.
Note that Maya will turn on relative naming during file I/O. Although it
is not recommended to leave relativeNames turned on, if you try to toggle
the value during file I/O you may notice that the value stays "on" because
Maya has already temporarily enabled it internally.

When relativeNames are enabled, the returns provided by the 'ls' command
will be relative to the current namespace. See the main description of this
command for more details.

---
removeNamespace(rm): string
    properties: create
    Deletes the given namespace.  The namespace
must be empty for it to be deleted.

---
rename(ren): [string, string]
    properties: create
    Rename the first namespace to second namespace name. Child namespaces will
also be renamed. Both names are relative to the current namespace. Use the
'parent' flag to specify a parent namespace for the renamed namespace.
An error is issued if the second namespace name already exists.
If the supplied name contains invalid characters it will first be modified
as per the validateName flag.

---
setNamespace(set): string
    properties: create
    Sets the current namespace.

---
validateName(vn): string
    properties: create
    Convert the specified name to a valid name to make it contain no illegal characters.
The leading illegal characters will be removed and other illegal characters will be converted to '_'.
Specially, the leading numeric characters and trailing space characters will be also removed.

Full name path can be validated as well. However, if the namespace of the path does not exist, command will only
return the base name. For example, ":nonExistentNS:name" will be converted to "name".

If the entire name consists solely of illegal characters, e.g. "123" which contains only leading digits, then the returned string will be empty.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/namespace.html 
    """


def namespaceInfo(flagabsoluteName: boolean, flagbaseName: boolean, flagcurrentNamespace: boolean, flagdagPath: boolean, flagfullName: boolean, flaginternal: boolean, flagisRootNamespace: boolean, flaglistNamespace: boolean, flaglistOnlyDependencyNodes: boolean, flaglistOnlyNamespaces: boolean, flagparent: boolean, flagrecurse: boolean, flagshortName: boolean) -> string:
    """Synopsis:
---
---
 namespaceInfo(
string
    , [absoluteName=boolean], [baseName=boolean], [currentNamespace=boolean], [dagPath=boolean], [fullName=boolean], [internal=boolean], [isRootNamespace=boolean], [listNamespace=boolean], [listOnlyDependencyNodes=boolean], [listOnlyNamespaces=boolean], [parent=boolean], [recurse=boolean], [shortName=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

namespaceInfo is undoable, NOT queryable, and NOT editable.

A namespace is a simple grouping of objects under a given name.
Each item in a namespace can then be identified by its own name, along
with what namespace it belongs to.  Namespaces can contain other
namespaces like sets, with the restriction that all namespaces
are disjoint.

Namespaces are primarily used to resolve name-clash issues in Maya,
where a new object has the same name as an existing object
(from importing a file, for example).
Using namespaces, you can have two objects with the same name, as long as
they are contained in different namespaces.

Note that namespaces are a simple grouping of names, so
they do not effect selection, the DAG, the Dependency Graph, or any other
aspect of Maya.  All namespace names are colon-separated.


The namespace format flags are: baseName(shortName), fullName and absoluteName.
The flags are used in conjunction with the main query flags to specify the desired namespace format of the returned result. They can also be used to return the different formats of a specified namespace.
By default, when no format is specified, the result will be returned as a full name.




Example:
---
import maya.cmds as cmds

List the contents of the current namespace
---

cmds.namespaceInfo( listNamespace=True )

List the parent of the current namespace
---

cmds.namespaceInfo( parent=True )

List the parent of the current namespace with short name
---

cmds.namespaceInfo( parent=True, shortName=True )

Determine if the current namespace is root
---

cmds.namespaceInfo( rootNamespace=True )

List the parent of the current namespace with absolute name
---

cmds.namespaceInfo( parent=True, absoluteName=True )

List dependency nodes including internal nodes
---

cmds.namespaceInfo(listOnlyDependencyNodes = True,  internal = True);

samples of query info of specified namespace
cmds.namespace( set =":" )
cmds.namespace( add ="sample" )
cmds.namespace( set =":sample" )
cmds.namespace( add ="sun" )

List the contents of the specified namespace
---

cmds.namespaceInfo( ":sample", listNamespace=True )
Result: sample:sun

List the parent of the specified namespace
---

cmds.namespaceInfo( ":sample:sun", parent=True )
result: sample

List the parent of the specified namespace with baseName name
---

cmds.namespaceInfo( ":sample:sun", parent=True, baseName=True )
result: sample

Determine if the specified namespace is root
---

cmds.namespaceInfo( ":", isRootNamespace=True )
result: True

List the parent of the specified namespace with absolute name
---

cmds.namespaceInfo( ":sample:sun", parent=True, absoluteName=True )
result: :sample

List dependency nodes including internal nodes
---

cmds.namespaceInfo(  ":sample", listOnlyNamespaces = True )
result: sample:sun

Query the namespace name and have it returned in different formats
---

cmds.namespaceInfo( ":sample:sun", baseName = True )
result: "sun"

cmds.namespaceInfo( ":sample:sun", fullName = True )
result: "sample:sun"

cmds.namespaceInfo( "sample:sun", absoluteName = True )
result: ":sample:sun"

---
Return:
---


    string: Command result

Flags:
---


---
absoluteName(an): boolean
    properties: create
    This is a general flag which can be used to specify the desired format for
the namespace(s) returned by the command.
The absolute name of the namespace is a full namespace path, starting from the root namespace ":"
and including all parent namespaces.  For example ":ns:ball" is an absolute namespace
name while "ns:ball" is not.
The absolute namespace name is invariant and is not affected by the current namespace or
relative namespace modes.
See also other format modifiers 'baseName', 'fullName', etc

---
baseName(bn): boolean
    properties: create
    This is a general flag which can be used to specify the desired format for
the namespace(s) returned by the command. The base name of the namespace
contains only the leaf level name and does not contain its parent namespace(s).
For example the base name of an object named "ns:ball" is "ball".
This mode will always return the base name in the same manner, and is not affected by the
current namespace or relative namespace mode.
See also other format modifiers 'absoluteName', 'fullName', etc
The flag 'shortName' is a synonym for 'baseName'.

---
currentNamespace(cur): boolean
    properties: create
    Display the name of the current namespace.

---
dagPath(dp): boolean
    properties: create
    This flag modifies the 'listNamespace' and
'listOnlyDependencyNodes' flags to indicate that the names
of any dag objects returned will include as much of the dag path
as is necessary to make the names unique. If this flag is not
present, the names returned will not include any dag paths.

---
fullName(fn): boolean
    properties: create
    This is a general flag which can be used to specify the desired format for
the namespace(s) returned by the command. The full name of the namespace
contains both the namespace path and the base name, but without the leading colon representing
the root namespace.
For example "ns:ball" is a full name, whereas ":ns:ball" is an absolute name.
This mode is affected by the current namespace and relative namespace modes.
See also other format modifiers 'baseName', 'absoluteName', etc.

---
internal(int): boolean
    properties: create
    This flag is used together with the 'listOnlyDependencyNodes' flag.
When this flag is set, the returned list will
include internal nodes (for example itemFilters) that are not listed by default.

---
isRootNamespace(ir): boolean
    properties: create
    Returns true if the namespace is root(":"), false if not.

---
listNamespace(ls): boolean
    properties: create
    List the contents of the namespace.

---
listOnlyDependencyNodes(lod): boolean
    properties: create
    List all dependency nodes in the namespace.

---
listOnlyNamespaces(lon): boolean
    properties: create
    List all namespaces in the namespace.

---
parent(p): boolean
    properties: create
    Display the parent of the namespace.
By default, the list returned will not include internal nodes (such as itemFilters).
To include the internal nodes, use the 'internal' flag.

---
recurse(r): boolean
    properties: create
    Can be specified with 'listNamespace', 'listOnlyNamespaces'
or 'listOnlyDependencyNode' to cause the listing to recursively
include any child namespaces of the namespaces;

---
shortName(sn): boolean
    properties: create
    This flag is deprecated and may be removed in future releases of Maya.
It is a synonym for the baseName flag. Please use the baseName flag instead.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/namespaceInfo.html 
    """


def newton(flagattenuation: float, flagmagnitude: float, flagmaxDistance: linear, flagminDistance: float, flagname: string, flagperVertex: boolean, flagposition: tuple[linear, linear, linear], flagtorusSectionRadius: linear, flagvolumeExclusion: boolean, flagvolumeOffset: tuple[linear, linear, linear], flagvolumeShape: string, flagvolumeSweep: angle) -> string:
    """Synopsis:
---
---
 newton(
selectionList
    , [attenuation=float], [magnitude=float], [maxDistance=linear], [minDistance=float], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

newton is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
A Newton field pulls an object towards the exerting object with
force dependent on the exerting object's mass, using Newton's
universal law of gravitation.

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

cmds.newton( 'particle1', m=5.0, mxd=2.0 )
Creates a newton field with magnitude 5.0 and maximum distance 2.0,
and adds it to the list of fields particle1 owns.

cmds.newton( pos=(-2, 0, 4) )
Creates a newton field at position (0,2,4) in world coordinates,
with default magnitude(1.0), attentuation (1.0),
and max distance (5.0).

cmds.newton( 'newtonField1', e=1, att=0.98 )
Edits the acceleration value of the field named newtonField1

cmds.newton( 'newtonField1', q=1, m=1 )
Queries newtonF ield1for its magnitude.

cmds.newton( 'newtonField1', e=1, mxd=10.0 )
Changes the maximum distance of the field called
"newtonField1" to 10.0.

cmds.newton( m=2.0 )
Creates a newton field with magnitude 2.0 for every active selection.
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
minDistance(mnd): float
    properties: query, edit
    Minimum distance at which field is exerted.
Distance is in the denominator of the field force equation.
Setting md to a small positive number avoids bizarre behavior
when the distance gets extremely small.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/newton.html 
    """


def nodeCast(flagcopyDynamicAttrs: boolean, flagdisableAPICallbacks: boolean, flagdisableScriptJobCallbacks: boolean, flagdisconnectUnmatchedAttrs: boolean, flagforce: boolean, flagswapNames: boolean, flagswapValues: boolean) -> int:
    """Synopsis:
---
---
 nodeCast(stringstring, [copyDynamicAttrs=boolean], [disableAPICallbacks=boolean], [disableScriptJobCallbacks=boolean], [disconnectUnmatchedAttrs=boolean], [force=boolean], [swapNames=boolean], [swapValues=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nodeCast is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


tr1 = cmds.createNode( 'transform' )
tr2 = cmds.createNode( 'transform' )
cmds.connectAttr( tr1 + ".t", tr2 + ".t" )
cmds.connectAttr( tr2 + ".r", tr1 + ".r" )

theT = tr1
cmds.select( theT, replace=1 )
cmds.addAttr( ln="unmatched", at="long" )
middle_man = cmds.createNode( 'transform' )
cmds.connectAttr( theT + ".unmatched", middle_man + ".tx" )

swapNode = cmds.createNode( 'transform' )
cmds.nodeCast( theT, swapNode, disconnectUnmatchedAttrs=true )

---
Return:
---


    int: 0 for success, 1 for failure.

Flags:
---


---
copyDynamicAttrs(cda): boolean
    properties: create
    If the target node contains any dynamic attributes that are not defined on the
source node, then create identical dynamic attricutes on the source node and copy
the values and connections from the target node into them.

---
disableAPICallbacks(dsa): boolean
    properties: create
    add comment

---
disableScriptJobCallbacks(dsj): boolean
    properties: create
    add comment

---
disconnectUnmatchedAttrs(dua): boolean
    properties: create
    If the node that is being swapped out has any connections that do not exist
on the target node, then indicate if the connection should be disconnected.
By default these connections are not removed because they cannot be restored
if the target node is swapped back with the source node.

---
force(f): boolean
    properties: create
    Forces the command to do the node cast operation even if the nodes do
not share a common base object. When this flag is specified the command
will try to do the best possible attribute matching when swapping the
command.  It is not recommended to use the '-swapValues/sv' flag with
this flag.

---
swapNames(sn): boolean
    properties: create
    Swap the names of the nodes. By default names are not swapped.

---
swapValues(sv): boolean
    properties: create
    Indicates if the commands should exchange attributes on the common attributes
between the two nodes.  For example, if the nodes are the same base type
as a transform node, then rotate, scale, translate values would be copied
over.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nodeCast.html 
    """


def nodeEditor(flagactiveTab: int, flagaddNewNodes: boolean, flagaddNode: string, flagadditiveGraphingMode: boolean, flagallAttributes: boolean, flagallNodes: boolean, flagallowNewTabs: boolean, flagallowTabTearoff: boolean, flagautoSizeNodes: boolean, flagbeginCreateNode: boolean, flagbeginNewConnection: string, flagbreakSelectedConnections: boolean, flagcloseAllTabs: boolean, flagcloseTab: int, flagconnectSelectedNodes: boolean, flagconnectedGraphingMode: boolean, flagconnectionMinSegment: float, flagconnectionOffset: float, flagconnectionRoundness: float, flagconnectionStyle: string, flagconnectionTension: int, flagconsistentNameSize: boolean, flagcontentsChangedCommand: script, flagcontrol: boolean, flagcreateInfo: string, flagcreateNodeCommand: script, flagcreateTab: list[int] | tuple[int, string], flagcrosshairOnEdgeDragging: boolean, flagcustomAttributeListEdit: string | tuple[string, string], flagcycleHUD: boolean, flagdefaultPinnedState: boolean, flagdefineTemplate: string, flagdeleteSelected: boolean, flagdocTag: string, flagdotFormat: string, flagdownstream: boolean, flagduplicateTab: int | tuple[int, int], flagenableOpenGL: boolean, flagexists: boolean, flagextendToShapes: boolean, flagfeedbackConnection: boolean, flagfeedbackNode: boolean, flagfeedbackPlug: boolean, flagfeedbackTabIndex: boolean, flagfeedbackType: boolean, flagfilter: string, flagfilterCreateNodeTypes: script, flagfocusCommand: script, flagforceMainConnection: string, flagframeAll: boolean, flagframeModelSelection: boolean, flagframeSelected: boolean, flaggetNodeList: boolean, flaggraphSelectedConnections: boolean, flaggraphSelection: boolean, flaggridSnap: boolean, flaggridVisibility: boolean, flaghasWatchpoint: boolean, flaghighlightConnection: string, flaghighlightConnections: tuple[string, boolean], flaghudMessage: tuple[string, int, float], flagignoreAssets: boolean, flagisland: boolean, flagkeyPressCommand: script, flagkeyReleaseCommand: script, flaglayout: boolean, flaglayoutCommand: script, flaglockMainConnection: boolean, flagmainListConnection: string, flagnodeSwatchSize: string, flagnodeTitleMode: string, flagnodeViewMode: string, flagoverrideNodeDropPosition: tuple[float, float], flagpanView: tuple[float, float], flagpanel: string, flagparent: string, flagpinSelectedNodes: boolean, flagpopupMenuScript: script, flagprimary: boolean, flagredockTab: boolean, flagremoveDownstream: boolean, flagremoveNode: string, flagremoveUnselected: boolean, flagremoveUpstream: boolean, flagrenameNode: string, flagrenameTab: list[int] | tuple[int, string], flagrestoreInfo: string, flagrestoreLastClosedTab: boolean, flagrootNode: string, flagrootsFromSelection: boolean, flagscaleView: float, flagselectAll: boolean, flagselectConnectionNodes: boolean, flagselectDownstream: boolean, flagselectFeedbackConnection: boolean, flagselectNode: string, flagselectUpstream: boolean, flagselectionConnection: string, flagsetWatchpoint: boolean, flagsettingsChangedCallback: script, flagshaderNetworks: boolean, flagshowAllNodeAttributes: string, flagshowNamespace: boolean, flagshowSGShapes: boolean, flagshowShapes: boolean, flagshowTabs: boolean, flagshowTransforms: boolean, flagshowUnitConversions: boolean, flagstateString: boolean, flagsyncedSelection: boolean, flagtabChangeCommand: script, flagtoggleAttrFilter: boolean, flagtoggleSelectedPins: boolean, flagtoggleSwatchSize: string, flagtoolTipCommand: script, flagtraversalDepthLimit: int, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flagupstream: boolean, flaguseAssets: boolean, flaguseLongName: int, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 nodeEditor(
[string]
    , [activeTab=int], [addNewNodes=boolean], [addNode=string], [additiveGraphingMode=boolean], [allAttributes=boolean], [allNodes=boolean], [allowNewTabs=boolean], [allowTabTearoff=boolean], [autoSizeNodes=boolean], [beginCreateNode=boolean], [beginNewConnection=string], [breakSelectedConnections=boolean], [closeAllTabs=boolean], [closeTab=int], [connectSelectedNodes=boolean], [connectedGraphingMode=boolean], [connectionMinSegment=float], [connectionOffset=float], [connectionRoundness=float], [connectionStyle=string], [connectionTension=int], [consistentNameSize=boolean], [contentsChangedCommand=script], [control=boolean], [createInfo=string], [createNodeCommand=script], [createTab=[int, [, string, ]]], [crosshairOnEdgeDragging=boolean], [customAttributeListEdit=[string, [, string, ]]], [cycleHUD=boolean], [defaultPinnedState=boolean], [defineTemplate=string], [deleteSelected=boolean], [docTag=string], [dotFormat=string], [downstream=boolean], [duplicateTab=[int, [, int, ]]], [enableOpenGL=boolean], [exists=boolean], [extendToShapes=boolean], [feedbackConnection=boolean], [feedbackNode=boolean], [feedbackPlug=boolean], [feedbackTabIndex=boolean], [feedbackType=boolean], [filter=string], [filterCreateNodeTypes=script], [focusCommand=script], [forceMainConnection=string], [frameAll=boolean], [frameModelSelection=boolean], [frameSelected=boolean], [getNodeList=boolean], [graphSelectedConnections=boolean], [graphSelection=boolean], [gridSnap=boolean], [gridVisibility=boolean], [hasWatchpoint=boolean], [highlightConnection=string], [highlightConnections=[string, boolean]], [hudMessage=[string, int, float]], [ignoreAssets=boolean], [island=boolean], [keyPressCommand=script], [keyReleaseCommand=script], [layout=boolean], [layoutCommand=script], [lockMainConnection=boolean], [mainListConnection=string], [nodeSwatchSize=string], [nodeTitleMode=string], [nodeViewMode=string], [overrideNodeDropPosition=[float, float]], [panView=[float, float]], [panel=string], [parent=string], [pinSelectedNodes=boolean], [popupMenuScript=script], [primary=boolean], [redockTab=boolean], [removeDownstream=boolean], [removeNode=string], [removeUnselected=boolean], [removeUpstream=boolean], [renameNode=string], [renameTab=[int, [, string, ]]], [restoreInfo=string], [restoreLastClosedTab=boolean], [rootNode=string], [rootsFromSelection=boolean], [scaleView=float], [selectAll=boolean], [selectConnectionNodes=boolean], [selectDownstream=boolean], [selectFeedbackConnection=boolean], [selectNode=string], [selectUpstream=boolean], [selectionConnection=string], [setWatchpoint=boolean], [settingsChangedCallback=script], [shaderNetworks=boolean], [showAllNodeAttributes=string], [showNamespace=boolean], [showSGShapes=boolean], [showShapes=boolean], [showTabs=boolean], [showTransforms=boolean], [showUnitConversions=boolean], [stateString=boolean], [syncedSelection=boolean], [tabChangeCommand=script], [toggleAttrFilter=boolean], [toggleSelectedPins=boolean], [toggleSwatchSize=string], [toolTipCommand=script], [traversalDepthLimit=int], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [upstream=boolean], [useAssets=boolean], [useLongName=int], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nodeEditor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.window()
form = cmds.formLayout()
p = cmds.scriptedPanel(type="nodeEditorPanel", label="Node Editor")
cmds.formLayout(form, e=True, af=[(p,s,0) for s in ("top","bottom","left","right")])
cmds.showWindow()

---
Return:
---


    string: The name of the created control.

Flags:
---


---
activeTab(at): int
    properties: query, edit
    Gets/sets the index of the tab widget's (active) visible tab. Note: the index is
zero-based.

---
addNewNodes(ann): boolean
    properties: create, query, edit
    New nodes should be added to the graph, default is on.

---
addNode(an): string
    properties: edit, multiuse
    Adds a specified node to the graph. Passing an empty string means the current model
selection will be added to the graph.

---
additiveGraphingMode(agm): boolean
    properties: create, query, edit
    When enabled, the graphing will add node networks to the existing graph instead of replacing it.

---
allAttributes(ala): boolean
    properties: create, query, edit
    Attributes should not be filtered out of the graph, default is off.

---
allNodes(aln): boolean
    properties: create, query, edit
    Nodes should not be filtered out of the graph, default is off.

---
allowNewTabs(ant): boolean
    properties: query
    Query only. Returns whether this Node Editor is allowed to have new tabs added,
either by creating a new tab or duplicating an existing one.

---
allowTabTearoff(att): boolean
    properties: create, edit
    Control whether or not the tabs can be torn off and floated.
Defaults to true.

---
autoSizeNodes(asn): boolean
    properties: create, query, edit
    When enabled, default node widths will be dynamically determined by the node name length, default is on.

---
beginCreateNode(bcn): boolean
    properties: edit
    Begin interactive node-creation at the mouse position. This will create
a control which allows quick creation of a node in the editor.
The actual creation is delegated to the createNodeCommand.

---
beginNewConnection(bnc): string
    properties: edit
    Begin a new interactive connection at the given attribute.

---
breakSelectedConnections(bsc): boolean
    properties: edit
    Break the selected attribute connections.

---
closeAllTabs(cat): boolean
    properties: edit
    Close all tabs on the tab widget.

---
closeTab(clt): int
    properties: edit
    Closes the tab on the tab widget at the specified index. Note: using this flag
on a torn-off tab will close the node editor since there can be only a single tab.
In this case the index argument is ignored.

---
connectSelectedNodes(csn): boolean
    properties: edit
    Creates a connection between all selected nodes in the editor. The default output
port of one node is connected to the default input port of the next node in the
selection order.

---
connectedGraphingMode(cgm): boolean
    properties: create, query, edit
    When enabled, connected nodes will be re-graphed when new nodes are added to the graph.

---
connectionMinSegment(csm): float
    properties: query, edit
    Sets the minimum segment length ratio of the connection leaving an output port.
Applies to "straight", "corner" and "s-shape" connection styles.
Value must be between 0.0 and 1.0.

---
connectionOffset(cso): float
    properties: query, edit
    Sets the offset length for each connection edges.
Applies to "corner" and "s-shape" connection styles.
Value must be between 0.0 and 1.0.

---
connectionRoundness(csr): float
    properties: query, edit
    Sets the roundness factor for each connection edges.
Applies only to "s-shape" connection style.
Value must be between 0.5 and 1.0.

---
connectionStyle(cs): string
    properties: query, edit
    Sets how the connection between nodes are drawn.
Mode values are: "bezier", "straight", "corner" and "s-shape".
In query mode, returns current connection style.

---
connectionTension(cst): int
    properties: query, edit
    Sets where the vertical line should be drawn on connection edge, 0 being in the middle.
Applies to "corner" and "s-shape" connection styles.
Value must be between -100 and 100.

---
consistentNameSize(cns): boolean
    properties: create, query, edit
    When enabled, the size of the node name will consistently match the current zoom
level. When disabled, the node name size will remain the same after zooming out
past a certain level. Default is on.

---
contentsChangedCommand(cc): script
    properties: create, query, edit
    Specifies a function to be called whenever the contents of the node editor changes.

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
createInfo(ci): string
    properties: create, edit
    Creates or modifies a hyperGraphInfo network to save the state of the editor.

---
createNodeCommand(cnc): script
    properties: create, query, edit
    Specifies a function to be used to create nodes through the editor. The function will
be passed the name of the chosen node type. This is used by the tab-create workflow.
By default createNode is used.

---
createTab(ct): [int, [, string, ]]
    properties: create, edit
    Create a new tab inserting it into the tab widget at the specified index. If
index is out of range (such as -1), the tab is simply appended. You can
optionally (Python only) specify a tab label, otherwise it will be set with a
default name. In Mel using an empty string ("") for the tab label will set it
with a default name. The new tab becomes the current (active) tab.
Note: Only certain Node Editors are allowed to create new tabs, which can
be checked by using the -allowNewTabs flag.

---
crosshairOnEdgeDragging(ced): boolean
    properties: create, query, edit
    Toggle crosshair cursor during edge dragging on/off.

---
customAttributeListEdit(cal): [string, [, string, ]]
    properties: query, edit
    Create/Edit the custom attribute list for the given node by entering
a special "Edit Mode" for the node. Note: only one node in the node
editor can be in this edit mode at a time. If another node is selected
the edit mode will end automatically. To end the edit mode use an empty
string for node.
Takes an optional edit mode command which accepts: "hideall" (sets all
the attributes to hidden), "showall" (sets all the attributes to visible),
"preview" (temporarily shows only the visible attributes), "revert"
(restores the visibility settings of the attributes to what they were
before edit mode) and "reset" (the visible attributes are reset so that
only the interesting attributes are displayed).
In query mode returns the name of the node, if any, in edit mode.
Note: the optional string argument is ignored in query mode.

---
cycleHUD(ch): boolean
    properties: create, edit
    Change the HUD to the next state.

---
defaultPinnedState(dps): boolean
    properties: create, query, edit
    Sets default pinned state of all nodes, 1 for pinned, 0 for unpinned. default value 0

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deleteSelected(deleteSelected): boolean
    properties: edit
    Delete the selected nodes and break the selected connections.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
dotFormat(dot): string
    properties: query, edit
    In query mode:
Get the graph information in DOT format. The flag argument specifies a file path to write to.
If "-" is supplied, the data is returned as a string, otherwise the size in bytes of the written
file is returned.
In edit mode:
Sets the positions of nodes in the graph from a Graphviz output file in plain format. Only the
node position, width and height information is used.
If the argument starts with "graph ", it will be treated as the plain data instead of a filename.
      In query mode, this flag needs a value.

---
downstream(ds): boolean
    properties: create, edit
    Include nodes that are downstream of the root nodes.

---
duplicateTab(dpt): [int, [, int, ]]
    properties: create, edit
    Duplicates the tab at the specified index, placing it at the second optional
(Python only) specified index. To place duplicated tab at the end use -1.
The duplicated tab becomes the current (active) tab.
Note: Only certain Node Editors are allowed to duplicate tabs, which can
be checked by using the -allowNewTabs flag.

---
enableOpenGL(egl): boolean
    properties: create, query, edit
    Specifies if OpenGL should be used to render the node editor view.
When enabled this will greatly improve performance but is still a work in progress.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
extendToShapes(ets): boolean
    properties: create, query, edit
    Include child shapes for each selected transform.

---
feedbackConnection(fbc): boolean
    properties: query
    Returns a description of the connection(s) at the current mouse position in the
editor view, if any.
The connection(s) will be returned as a list of strings, which are
pairs of plugs for each connection.

---
feedbackNode(fbn): boolean
    properties: query
    Returns the name of the node at the current mouse position in the editor view,
if any.

---
feedbackPlug(fbp): boolean
    properties: query
    Returns the name of the plug (attribute) at the current mouse position
in the editor view, if any.

---
feedbackTabIndex(fbi): boolean
    properties: query
    Returns the index of the tab at the current mouse position in the editor view,
if any.

---
feedbackType(fbt): boolean
    properties: query
    Returns the most specific type of the feedback item (item at the current mouse
position) in the editor view, if any.
Will be one of "plug", "node", "tab", "connection" or an empty string.
Use the other feedback* flags to query the item description.

---
filter(f): string
    properties: create, query, edit
    Specifies the name of an itemFilter object to be used with this editor.
This filters the information coming onto the main list
of the editor.

---
filterCreateNodeTypes(fcn): script
    properties: create, query, edit
    Specifies a function to be used to filter the list of node types which
appear in the inline-creation menu (tab key). The function should accept
one string array argument and return a string array.

---
focusCommand(fc): script
    properties: create, query, edit
    Specifies a function to be called whenever focus changes for the node editor.

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
frameAll(fa): boolean
    properties: edit
    Frame all the contents of the node editor.

---
frameModelSelection(fms): boolean
    properties: edit
    Frame the current model selection.

---
frameSelected(fs): boolean
    properties: edit
    Frame the selected contents of the node editor.

---
getNodeList(gnl): boolean
    properties: query
    Returns a list of all nodes displayed in the editor.

---
graphSelectedConnections(gsc): boolean
    properties: edit
    Graph the nodes connected by the selected attribute connections.

---
graphSelection(gsl): boolean
    properties: edit
    Graph the nodes that are currently selected.

---
gridSnap(gs): boolean
    properties: create, query, edit
    Toggle grid snapping on/off.

---
gridVisibility(gv): boolean
    properties: create, query, edit
    Toggle grid visiblity on/off.

---
hasWatchpoint(hw): boolean
    properties: query
    Returns if the selected connection has a watchpoint set.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
highlightConnections(hc): [string, boolean]
    properties: create, query, edit, multiuse
    Sets if selecting a node should highlight its connections for the specified editor,
which can be "regular" or "bifrost".

---
hudMessage(hm): [string, int, float]
    properties: edit
    Display the given message on the editor HUD.
The flag arguments are (message, type, duration), where type is:

upper-left corner.
top center.
upper-right corner.
center.

Duration 0 means the message stays until removed. Duration > 0 means it stays for that number of seconds.
An empty message erases whatever is currently displayed for the given type.

---
ignoreAssets(ia): boolean
    properties: create, query, edit
    Deprecated. Do not use in scripts.

---
island(isl): boolean
    properties: query, edit
    Deprecated. Do not use in scripts.

---
keyPressCommand(kpc): script
    properties: create, query, edit
    Specifies a function to be called when a key is pressed and the editor has focus.

The function will be passed the name of the editor and an (uppercase) string representation of the key that was pressed, and should return true if the key was handled, and false if it was not.

Note: `getModifiers` can be used to query the current state of key modifiers.

---
keyReleaseCommand(krc): script
    properties: create, query, edit
    Specifies a function to be called when a key is released and the editor has focus.

The function will be passed the name of the editor and an (uppercase) string representation of the key that was released, and should return true if the key was handled, and false if it was not.

Note: `getModifiers` can be used to query the current state of key modifiers.

---
layout(lay): boolean
    properties: edit
    Perform an automatic layout of the graph.

---
layoutCommand(lc): script
    properties: create, query, edit
    Specifies a function to override the default action when a graph layout is required. The function will
be passed the name of editor. The function should arrange the nodes in the graph.

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
nodeSwatchSize(nss): string
    properties: edit
    Sets the icon swatch size of selected nodes in the active scene (all nodes if none are selected).
Size values are "small" and "large".

---
nodeTitleMode(ntm): string
    properties: create, query, edit
    Gets/sets the node title display mode of the current scene.
Mode values are:
"name" (Display node names),
"type" (Display node types),
"none" (Do not display titles)

---
nodeViewMode(nvm): string
    properties: edit
    Sets the attribute view mode of selected nodes in the active scene (all nodes if none are selected).
Mode values are: "simple" (no attributes displayed), "connected" (connected attributes only), "all"
(all interesting attributes displayed) and "custom" (use custom attribute view).

---
overrideNodeDropPosition(onp): [float, float]
    properties: edit
    Specifies the override position for new node.
Values are respectively the width and height ratio;
0.0, 0.0 corresponds to the top left corner of the view,
1.0, 1.0 corresponds to the bottom right corner of the view,
0.5, 0.5 corresponds to the center of the view.

---
panView(pv): [float, float]
    properties: edit
    Pan the view by the given amount. Arguments of 0 0 will reset the view translation.

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
pinSelectedNodes(psn): boolean
    properties: edit
    Pins or unpins the selected nodes. If no nodes are selected, this will apply to all displayed nodes.

---
popupMenuScript(pms): script
    properties: create, query, edit
    Set the script to be called to register the popup menu with the
control for this editor. The script will be called with a string
argument which gives the name of the editor whose control the popup
menu should be parented to.

---
primary(pr): boolean
    properties: query
    Query only. Returns whether this node editor is the primary one. The
primary editor is the only one that will show and allow tabs.

---
redockTab(rdt): boolean
    properties: query, edit
    If this tab was torn-off from the primary node editor, then the tab and all its
data will be re-docked back into the primary editor and this node editor will
be closed. In query mode returns whether this tab was torn-off and is available
to be re-docked.

---
removeDownstream(rd): boolean
    properties: edit
    Removes all items downstream to the currently active selection.

---
removeNode(rem): string
    properties: edit, multiuse
    Removes a node from the graph. An empty string indicates that currently selected nodes should be removed.

---
removeUnselected(run): boolean
    properties: edit
    Removes unselected nodes from graph.

---
removeUpstream(ru): boolean
    properties: edit
    Removes all items upstream to the currently active selection.

---
renameNode(ren): string
    properties: edit
    Rename a node in the graph. Depending on the zoom level of the view, an edit field
will either appear on the node item or in a popup dialog to allow the new name to be
entered.

---
renameTab(rt): [int, [, string, ]]
    properties: edit
    Renames the tab at the specified index with the (optional) name. If no name is
specified (Python only) or an empty string ("") is used then an inline edit field
is opened to rename the tab.

---
restoreInfo(ri): string
    properties: create, edit
    Restores the editor state corresponding to supplied hyperGraphInfo node.

---
restoreLastClosedTab(rlt): boolean
    properties: query, edit
    If this node editor is the primary one, then restore the last closed tab
(if any). In query mode returns whether there is a tab available to restore.

---
rootNode(rn): string
    properties: create, edit, multiuse
    Add a node name as a root node of the graph.
Passing an empty string clears the current root node list.
When queried, returns the list of current root nodes.

---
rootsFromSelection(rfs): boolean
    properties: create, edit
    Specify that the root nodes for the graph should taken from the currently active selection.

---
scaleView(sv): float
    properties: edit
    Scales the graph view by the given factor. An argument of zero means reset to default.

---
selectAll(sa): boolean
    properties: edit
    Select all items in the graph.

---
selectConnectionNodes(scn): boolean
    properties: edit
    Select the nodes connected by the selected attribute connections.

---
selectDownstream(sd): boolean
    properties: edit
    Select all items downstream to the currently active selection.

---
selectFeedbackConnection(sfc): boolean
    properties: edit
    Select the feedback connection(s) in the editor view, if any.

---
selectNode(sln): string
    properties: query, edit, multiuse
    Select a node in the graph.
Passing an empty string clears the current selection.
When queried, returns the list of currently selected nodes.

---
selectUpstream(su): boolean
    properties: edit
    Select all items upstream to the currently active selection.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
setWatchpoint(sw): boolean
    properties: create, edit
    Adds or removes the watchpoint on the selected connections.

---
settingsChangedCallback(scc): script
    properties: create, query, edit
    Specifies a function to be called whenever settings for the node editor
get changed.

---
shaderNetworks(sns): boolean
    properties: edit
    Graph the shader network for all the objects on the selection list that have shaders.

---
showAllNodeAttributes(saa): string
    properties: edit
    Display all attributes for the given node, not just primary attributes.
Passing an empty string will apply this to all currently selected nodes.
If no nodes are selected, this will be applied to all displayed nodes in the graph.

---
showNamespace(sn): boolean
    properties: create, query, edit
    Specifies whether nodes will have their namespace displayed if they are not in the root namespace.

---
showSGShapes(ssg): boolean
    properties: create, query, edit
    Show shapes that are connected to the network through a shading group.

---
showShapes(ss): boolean
    properties: create, query, edit
    Show shape nodes.

---
showTabs(tab): boolean
    properties: create
    Creation time flag to explicitly control the visibility of the tabs.
If this is set to true or false the tabs visibility will respect that setting.
If this flag is not explicitly set then the tabs will be visible in the primary node editor and tear off tabs,
but will not be visible for other editors that are not the primary editor.

---
showTransforms(st): boolean
    properties: create, query, edit
    Show transforms.

---
showUnitConversions(suc): boolean
    properties: create, query, edit
    Show unit conversion nodes.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
syncedSelection(ssl): boolean
    properties: create, query, edit
    Keep the graph selection in sync with the model selection.

---
tabChangeCommand(tcc): script
    properties: create, edit
    Command executed when the current (active) tab is changed.
Re-selecting the current tab will not invoke this command.
NOTE: This command will also be executed when switching into,
out of, and between compound views.

---
toggleAttrFilter(taf): boolean
    properties: edit
    Toggles the display of the attribute filter field on selected nodes. If any of the selected nodes have the field
displayed, this operation will hide the field for all nodes in the selection. If no nodes are selected, this will
apply to all displayed nodes.

---
toggleSelectedPins(tsp): boolean
    properties: edit
    Toggles pinned state on selected nodes. If any selected nodes are unpinned, this operation will choose to
pin all nodes. If no nodes are selected, this will apply to all displayed nodes.

---
toggleSwatchSize(tss): string
    properties: edit
    Toggles the swatch size of the given node between small and large. If supplied node name was empty, this will be applied to selection,
and if no nodes are selected this is applied to all nodes in editor.
When selection is a combination of small and large swatch sizes, this will set selection to large swatch mode.

---
toolTipCommand(ttc): script
    properties: create, query, edit
    Specifies a function to override the tooltip that is displayed for a node. The function will
be passed the name of the node under the cursor, and should return a text string to be displayed.
A simple HTML 4 subset is supported.

---
traversalDepthLimit(tdl): int
    properties: create, query, edit
    Specify the maximum number of edges which will be followed from any root node
when building the graph. A negative value means unlimited. Default is unlimited.

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
upstream(ups): boolean
    properties: create, edit
    Include nodes that are upstream of the root nodes.

---
useAssets(ua): boolean
    properties: create, query, edit
    Use assets and published attributes instead of contents and actual attributes.

---
useLongName(uln): int
    properties: create, query, edit
    Specifies how attribute names should be displayed.
0 = Display using short attribute names.
1 = Display using nice/UI attribute names.
2 = Display using long attribute names.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nodeEditor.html 
    """


def nodeIconButton(flagalign: string, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcommand: script, flagdefineTemplate: string, flagdisabledImage: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagflipX: boolean, flagflipY: boolean, flagfont: string, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagimage: string, flagimage1: string, flagimage2: string, flagimage3: string, flagimageOverlayLabel: string, flagisObscured: boolean, flaglabel: string, flaglabelOffset: int, flagmanage: boolean, flagmarginHeight: uint, flagmarginWidth: uint, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagoverlayLabelBackColor: tuple[float, float, float, float], flagoverlayLabelColor: tuple[float, float, float], flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrotation: float, flagstatusBarMessage: string, flagstyle: string, flaguseAlpha: boolean, flaguseTemplate: string, flagversion: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 nodeIconButton(
[string]
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [command=script], [defineTemplate=string], [disabledImage=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [flipX=boolean], [flipY=boolean], [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [image=string], [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string], [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint], [noBackground=boolean], [numberOfPopupMenus=boolean], [overlayLabelBackColor=[float, float, float, float]], [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rotation=float], [statusBarMessage=string], [style=string], [useAlpha=boolean], [useTemplate=string], [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nodeIconButton is undoable, queryable, and editable.
This command creates a button that can be displayed with different
icons, with or without a text label. If the button is drag and dropped
onto other controls (e.g., HyperShade), the command will be executed and
the return string will be used as the name of a dropped node.




Example:
---
import maya.cmds as cmds

window = cmds.window( )
cmds.columnLayout( adjustableColumn=True )
cmds.nodeIconButton( style='textOnly', command='cmds.shadingNode("lambert", asShader=True)', label='lambert' )
cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1='sphere.png' )
cmds.nodeIconButton( style='iconAndTextHorizontal', command='cmds.spotLight()', image1='spotlight.png', label='Spot Light' )
cmds.showWindow( window )

---
Return:
---


    string: The name of the button

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
    Command executed when the control is pressed. The command
should return a string which will be used to facilitate node drag
and drop.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nodeIconButton.html 
    """


def nodeOutliner(flagaddCommand: script, flagaddObject: name, flagannotation: string, flagattrAlphaOrder: string, flagbackgroundColor: tuple[float, float, float], flagconnectivity: name, flagcurrentSelection: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfilter: string, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglastClickedNode: boolean, flaglastMenuChoice: string, flaglongNames: boolean, flagmanage: boolean, flagmenuCommand: script, flagmenuMultiOption: boolean, flagmultiSelect: boolean, flagniceNames: boolean, flagnoBackground: boolean, flagnoConnectivity: boolean, flagnodesDisplayed: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpressHighlightsUnconnected: boolean, flagpreventOverride: boolean, flagredraw: boolean, flagredrawRow: boolean, flagremove: string, flagremoveAll: boolean, flagreplace: name, flagselectCommand: script, flagshowConnectedOnly: boolean, flagshowHidden: boolean, flagshowInputs: boolean, flagshowNonConnectable: boolean, flagshowNonKeyable: boolean, flagshowOutputs: boolean, flagshowPublished: boolean, flagshowReadOnly: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> None:
    """Synopsis:
---
---
 nodeOutliner(
[string]
    , [addCommand=script], [addObject=name], [annotation=string], [attrAlphaOrder=string], [backgroundColor=[float, float, float]], [connectivity=name], [currentSelection=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [filter=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [lastClickedNode=boolean], [lastMenuChoice=string], [longNames=boolean], [manage=boolean], [menuCommand=script], [menuMultiOption=boolean], [multiSelect=boolean], [niceNames=boolean], [noBackground=boolean], [noConnectivity=boolean], [nodesDisplayed=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [pressHighlightsUnconnected=boolean], [preventOverride=boolean], [redraw=boolean], [redrawRow=boolean], [remove=string], [removeAll=boolean], [replace=name], [selectCommand=script], [showConnectedOnly=boolean], [showHidden=boolean], [showInputs=boolean], [showNonConnectable=boolean], [showNonKeyable=boolean], [showOutputs=boolean], [showPublished=boolean], [showReadOnly=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nodeOutliner is undoable, queryable, and editable.
In some configurations, dragging a connected attribute of a node will
load the node at the other end of the connection.

There is a right mouse button menu and a flag to attach a command to
it. The menu is used to list the specific connections of a connected
attribute. Clicking over any spot but the row of a connected attribute
will show an empty menu. By default, there is no command attached to
the menu.




Example:
---
import maya.cmds as cmds

mywindow = cmds.window()
myform = cmds.formLayout( numberOfDivisions=100 )

Create an outliner that will print the name of
every object added to it to history pane of the
script editor, then display all available input
plugs on the node.
def onAddNode(name):
    print name
myoutliner = cmds.nodeOutliner( showInputs=True, addCommand=onAddNode )

Attach the nodeOutliner to the layout
cmds.formLayout( myform, edit=True, attachForm=((myoutliner, 'top', 5), (myoutliner, 'left', 5), (myoutliner, 'bottom', 5), (myoutliner, 'right', 5)) )

Display the window with the node Outliner
cmds.showWindow( mywindow )

Create a sphere
objectName = cmds.sphere()

Have the outliner display the sphere
cmds.nodeOutliner( myoutliner, e=True, a='nurbsSphere1' )

---


Flags:
---


---
addCommand(ac): script
    properties: create, query, edit
    Command executed when the node outliner adds something.
String commands use substitution of the term %node for whatever is added, eg,
if you want to print the object added, the command should be
"print(\"%node \\n\")".  Callable python objects are passed the node name.

---
addObject(a): name
    properties: edit
    add the given object to the display

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
attrAlphaOrder(aao): string
    properties: create, query, edit
    Specify how attributes are to be sorted.  Current recognised values
are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and
"descend" to sort from 'z' to 'a'.
Notes: a) this only applies to top level attributes.

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
connectivity(c): name
    properties: query, edit
    Takes an attribute argument ("nodeName.attributeName"), dims any attributes
that can't connect to the given, and highlights any attributes already connected

---
currentSelection(cs): boolean
    properties: query
    Retruns a string array containing what is currently selected

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
filter(f) 2024: string
    properties: query, edit
    filter attributes based on a regular expression

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
lastClickedNode(lcn): boolean
    properties: query
    Returns a string with the last clicked node

---
lastMenuChoice(lmc): string
    properties: query
    Returns the text of the most recent menu selection.

---
longNames(ln): boolean
    properties: query, edit
    Controls whether long or short attribute names will be used
in the interface.  Note that this flag is ignored if the niceNames
flag is set.  Default is short names. Queried, returns a boolean.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
menuCommand(mc): script
    properties: edit
    Attaches the given command to each item in the popup menu.

---
menuMultiOption(mmo): boolean
    properties: query, edit
    Sets whether a menu option labelled "next available" will appear as the first
option on any multi-attribute's right mouse button menu.  Defaults to True.

---
multiSelect(ms): boolean
    properties: query, edit
    Allow multiSelect; more than one thing to be selected at a time

---
niceNames(nn): boolean
    properties: query, edit
    Controls whether the attribute names will be displayed in
a more user-friendly, readable way.  When this is on, the longNames
flag is ignored.  When this is off, attribute names will be displayed
either long or short, according to the longNames flag.
Default is on. Queried, returns a boolean.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
noConnectivity(nc): boolean
    properties: edit
    Reset the node outliner to not show any connectivity, ie, redraw all rows normally.

---
nodesDisplayed(nd): boolean
    properties: query
    Returns a string array containing the list of nodes showing in the node Outliner

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
pressHighlightsUnconnected(phu): boolean
    properties: query, edit
    Sets whether clicking on an unconnected plug will select it or not.  Default is True.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
redraw(r): boolean
    properties: edit
    Redraws the displayed space

---
redrawRow(rr): boolean
    properties: edit
    Redraws the given row

---
remove(rm): string
    properties: edit, multiuse
    remove the given object from the display

---
removeAll(rma): boolean
    properties: edit
    remove all objects from the display

---
replace(rpl): name
    properties: query, edit
    replace what's displayed with the given objects

---
selectCommand(sc): script
    properties: query, edit
    Command issued by selecting.  Different from the c flag in that this
command will only be issued if something is selected.

---
showConnectedOnly(sco): boolean
    properties: query, edit
    show (true) or hide (false) only attributes that are connected matching input/output criteria

---
showHidden(sh): boolean
    properties: query, edit
    show (true) or hide (false) UI invisible attributes that match the input/output criteria

---
showInputs(si): boolean
    properties: query, edit
    show only UI visible attributes that can be connected to

---
showNonConnectable(snc): boolean
    properties: query, edit
    show (true) or hide (false) non connectable attributes that match the input/output criteria

---
showNonKeyable(snk): boolean
    properties: query, edit
    show (true) or hide (false) non keyframeable (animatable) attributes that match the input/output criteria

---
showOutputs(so): boolean
    properties: query, edit
    show only UI visible attributes that can be connected from

---
showPublished(sp): boolean
    properties: query, edit
    Show only published attributes for an asset or a member of an asset.
This flag is ignored on nodes not related to assets.

---
showReadOnly(sro): boolean
    properties: query, edit
    show only read only attributes attributes that can be connected from

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nodeOutliner.html 
    """


def nodePreset(flagattributes: string, flagcustom: string, flagdelete: tuple[name, string], flagexists: tuple[name, string], flagisValidName: string, flaglist: name, flagload: tuple[name, string], flagsave: tuple[name, string]) -> boolean:
    """Synopsis:
---
---
 nodePreset([attributes=string], [custom=string], [delete=[name, string]], [exists=[name, string]], [isValidName=string], [list=name], [load=[name, string]], [save=[name, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nodePreset is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

To determine if "My Special Settings" is a valid name for a preset (it
is not because it contains spaces):
---

cmds.nodePreset(isValidName="My Special Settings" )
Result: 0 ---


To save the settings of nurbsSphereShape1 as a preset called "smithers":
---

cmds.nodePreset( save=("nurbsSphereShape1","smithers") )

To get a list of all presets available that could be applied to
nurbsSphereShape1:
---

cmds.nodePreset( list='nurbsSphereShape1' )
Result: [u'smithers', u'smoothSphere', u'roughSphere', u'atmoSphere'] ---


To load the preset named "smoothSphere" onto nurbsSphereShape1:
---

cmds.nodePreset( load=('nurbsSphereShape1', 'smoothSphere') )

To delete the preset named "smithers" which was formerly available for the
node nurbsSphereShape1 (and other nodes of the same type):
---

cmds.nodePreset( delete=('nurbsSphereShape1', 'smithers') )

To determine if a preset named "smithers" exists for the node
nurbsSphereShape1 (it does not because it has been deleted):
---

cmds.nodePreset( exists=('nurbsSphereShape1', 'smithers') )
Result: 0 ---


Create a preset containing only the color and diffuse attributes:
---

cmds.nodePreset( save=("lambert1","colorAndDiffuse"), attributes='color diffuse' )

Create a preset to map a checker texture to the applied node.
Because the "custom" callback is required to return an array of MEL commands,
each line of python in the array must be wrapped by the MEL "python" command.
---

def customChecker():
    doCheckerCmds = [
                Get the name of the node to apply the checker to.
                "python( \"selection = cmds.ls( selection=True )\" );",
            "python( \"nodeName = selection[0]\" );",
            Create a checker texture.
            "python( \"checkerName = cmds.shadingNode( 'checker', asTexture=True )\" );",
            Connect the checker to the node the preset is applied to.
                "python( \"cmds.connectAttr( (checkerName+\\\".outColor\\\"), (nodeName+\\\".color\\\") )\" );"
                ]
    return doCheckerCmds

        cmds.nodePreset(custom="python( \"customChecker()\" )", save=('lambert1', 'checkered') )

---
Return:
---


    boolean: if isValidName or exists is used.

Flags:
---


---
attributes(atr): string
    properties: create
    A white space separated string of the named attributes to save to the
preset file. If not specified, all attributes will be stored.

---
custom(ctm): string
    properties: create
    Specifies a MEL script for custom handling of node attributes that are not
handled by the general save preset mechanism (ie. multis, dynamic attributes,
or connections). The identifiers #presetName and #nodeName will be expanded
before the script is run. The script must return an array of strings which
will be saved to the preset file and issued as commands when the preset is
applied to another node.
The custom script can query #nodeName in determining what should be saved
to the preset, or issue commands to query the selected node in deciding how
the preset should be applied.

---
delete(delete): [name, string]
    properties: create
    Deletes the existing preset for the node specified by the first argument with
the name specified by the second argument.

---
exists(ex): [name, string]
    properties: create
    Returns true if the node specified by the first argument already has a preset
with a name specified by the second argument. This flag can be used to check if
the user is about to overwrite an existing preset and thereby provide the user
with an opportunity to choose a different name.

---
isValidName(ivn): string
    properties: create
    Returns true if the name consists entirely of valid characters for
a preset name. Returns false if not. Because the preset name will
become part of a file name and part of a MEL procedure name, some
characters must be disallowed. Only alphanumeric characters and underscore
are valid characters for the preset name.

---
list(ls): name
    properties: create
    Lists the names of all presets which can be loaded onto the specified
node.

---
load(ld): [name, string]
    properties: create
    Sets the settings of the node specified by the first argument according to the
preset specified by the second argument. Any attributes on the node which are
the destinations of connections or whose children (multi children or compound
children) are destinations of connections will not be changed by the preset.

---
save(sv): [name, string]
    properties: create
    Saves the current settings of the node specified by the first argument to a
preset of the name specified by the second argument. If a preset for that node
with that name already exists, it will be overwritten with no warning. You can
use the -exists flag to check if the preset already exists. If an attribute of
the node is the destination of a connection, the value of the attribute will
not be written as part of the preset.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nodePreset.html 
    """


def nodeTreeLister(flagaddFavorite: string, flagaddItem: tuple[string, string, script], flagaddVnnItem: tuple[string, string, string, string], flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagclearContents: boolean, flagcollapsePath: string, flagdefineTemplate: string, flagdisplayName: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexecuteItem: string, flagexists: boolean, flagexpandPath: string, flagexpandToDepth: int, flagfavoritesCallback: script, flagfavoritesList: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagitemScript: string, flagmanage: boolean, flagnoBackground: boolean, flagnodeLibrary: string, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrefreshCommand: script, flagremoveFavorite: string, flagremoveItem: string, flagresultsPathUnderCursor: boolean, flagselectPath: string, flagsetDisplayName: tuple[string, string], flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagvnnString: boolean, flagwidth: int) -> string:
    """Synopsis:
---
---
 nodeTreeLister(
[string]
    , [addFavorite=string], [addItem=[string, string, script]], [addVnnItem=[string, string, string, string]], [annotation=string], [backgroundColor=[float, float, float]], [clearContents=boolean], [collapsePath=string], [defineTemplate=string], [displayName=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [executeItem=string], [exists=boolean], [expandPath=string], [expandToDepth=int], [favoritesCallback=script], [favoritesList=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [itemScript=string], [manage=boolean], [noBackground=boolean], [nodeLibrary=string], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [refreshCommand=script], [removeFavorite=string], [removeItem=string], [resultsPathUnderCursor=boolean], [selectPath=string], [setDisplayName=[string, string]], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [vnnString=boolean], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nodeTreeLister is undoable, queryable, and editable.
The optional argument is the name of the control.




Example:
---
import maya.cmds as cmds

cmds.window(width=200)
cmds.formLayout('theForm')
cmds.nodeTreeLister('theTreeLister')
cmds.formLayout('theForm', e=True,
                af=(('theTreeLister', 'top', 0),
                    ('theTreeLister', 'left', 0),
                    ('theTreeLister', 'bottom', 0),
                    ('theTreeLister', 'right', 0)))
cmds.showWindow()

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
nodeLibrary(nl): string
    properties: create, query, edit
    The node library that this tree lister is currently displaying.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nodeTreeLister.html 
    """


def nodeType(flagapiType: boolean, flagderived: boolean, flaginherited: boolean, flagisTypeName: boolean, flagufeRuntimeName: boolean) -> list[string] | string:
    """Synopsis:
---
---
 nodeType(
string
    , [apiType=boolean], [derived=boolean], [inherited=boolean], [isTypeName=boolean], [ufeRuntimeName=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nodeType is undoable, NOT queryable, and NOT editable.
When no flags are used, the unique type name is returned.  This can be
useful for seeing if two nodes are of the same type.

When the api flag is used, the MFn::Type of the node is returned.
This can be useful for seeing if a plug-in node belongs to a given
class. The api flag cannot be used in conjunction with any other
flags.

When the derived flag is used, the command returns a string array
containing the names of all the currently known node types which derive
from the node type of the given object.

When the inherited flag is used, the command returns a string array
containing the names of all the base node types inherited by the
the given node.

If the isTypeName flag is present then the argument provided to the
command is taken to be the name of a node type rather than the name of a
specific node. This makes it possible to query the hierarchy of node types
without needing to have instances of each node type.




Example:
---
import maya.cmds as cmds

cmds.sphere( n='balloon' )

Find the type of node created by the sphere command
cmds.nodeType( 'balloon' )
Result: transform ---


What is the API type of the balloon node?
cmds.nodeType( 'balloon', api=True )
Result: kTransform ---


Which node types derive from camera?
cmds.nodeType( 'camera', derived=True, isTypeName=True )
Result: [u'stereoRigCamera', u'camera'] ---


---
Return:
---


    string: Single command result
    list[string]: Multiple command result

Flags:
---


---
apiType(api): boolean
    properties: create
    Return the MFn::Type value (as a string) corresponding
to the given node.  This is particularly useful when
the given node is defined by a plug-in, since in this
case, the MFn::Type value corresponds to the
underlying proxy class.

This flag cannot be used in combination with any of the other flags.

---
derived(d): boolean
    properties: create
    Return a string array containing the names of all the currently known node
types which derive from the type of the specified node.

---
inherited(i): boolean
    properties: create
    Return a string array containing the names of all the
base node types inherited by the specified node.

---
isTypeName(itn): boolean
    properties: create
    If this flag is present, then the argument provided to the command
is the name of a node type rather than the name of a specific node.

---
ufeRuntimeName(urn): boolean
    properties: create
    Return the UFE Runtime name corresponding to the given node.
This is particularly useful to filter between native Maya objects
and non-native objects exposed to Maya through the UFE interface.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nodeType.html 
    """


def nonLinear(flagafter: boolean, flagafterReference: boolean, flagautoParent: boolean, flagbefore: boolean, flagcommonParent: boolean, flagcomponents: boolean, flagdefaultScale: boolean, flagdeformerTools: boolean, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flagname: string, flagparallel: boolean, flagprune: boolean, flagremove: boolean, flagselectedComponents: boolean, flagsplit: boolean, flagtype: string, flaguseComponentTags: boolean) -> list[string]:
    """Synopsis:
---
---
 nonLinear(
objects
    , [after=boolean], [afterReference=boolean], [autoParent=boolean], [before=boolean], [commonParent=boolean], [components=boolean], [defaultScale=boolean], [deformerTools=boolean], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string], [parallel=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean], [split=boolean], [type=string], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nonLinear is undoable, queryable, and editable.
The nonLinear command has some flags which are specific to the
nonLinear type specified with the -type flag. The flags correspond to
the primary keyable attributes related to the specific type of
nonLinear node. For example, if the type is "bend", then the flags
"-curvature", "-lowBound" and "-highBound" may be used to initialize,
edit or query those attribute values on the bend node. Examples
of this are covered in the example section below.




Example:
---
import maya.cmds as cmds

To create a bend deformer with curvature 0.5
---

cmds.nonLinear( type='bend', curvature=0.5 )

To edit the curvature of the bend deformer
---

cmds.nonLinear( 'bend1', e=True, curvature=0.2 )

To query the curvature of the bend deformer
---

cmds.nonLinear( 'bend1', query=True, curvature=True )

---
Return:
---


    list[string]: Deformer driver name, deformer handle transform name.

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
autoParent(ap): boolean
    properties: create
    Parents the deformer handle under the selected object's
transform. This flag is valid only when a single object
is selected.

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
    Creates a new transform and parents the selected object
and the deformer handle under it.  This flag is valid only
when a single object is selected.

---
components(cmp): boolean
    properties: query
    Returns the components used by the deformer

---
defaultScale(ds): boolean
    properties: create
    Sets the scale of the deformation handle to 1.  By default
the deformation handle is scaled to the match the largest
dimension of the selected objects' bounding box.
[deformerFlags]
The attributes of the deformer handle shape
can be set upon creation, edited and queried as normal flags
using either the long or the short attribute name.  e.g.

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
type(typ): string
    properties: create
    Specifies the type of deformation. The current valid
deformation types are:  bend, twist, squash, flare,
sine and wave

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nonLinear.html 
    """


def normalConstraint(flagaimVector: tuple[float, float, float], flaglayer: string, flagname: string, flagremove: boolean, flagtargetList: boolean, flagupVector: tuple[float, float, float], flagweight: float, flagweightAliasList: boolean, flagworldUpObject: name, flagworldUpType: string, flagworldUpVector: tuple[float, float, float]) -> list[string]:
    """Synopsis:
---
---
 normalConstraint(
[target...] object
    , [aimVector=[float, float, float]], [layer=string], [name=string], [remove=boolean], [targetList=boolean], [upVector=[float, float, float]], [weight=float], [weightAliasList=boolean], [worldUpObject=name], [worldUpType=string], [worldUpVector=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

normalConstraint is undoable, queryable, and editable.
A normalConstraint takes as input one or more surface shapes (the
targets) and a DAG transform node (the object).  The normalConstraint
orients the constrained object such that the aimVector (in the
object's local coordinate system) aligns in world space to combined
normal vector.  The upVector (again the the object's local coordinate
system) is aligned in world space with the worldUpVector.  The
combined normal vector is a weighted average of the normal vector
for each target surface at the point closest to the constrained object.




Example:
---
import maya.cmds as cmds

cmds.normalConstraint( 'surf1', 'cube1' )
orients the aim vector of cube1 in it's local coordinate space,
to the normal vector of surf1 at the closest point to  cube1.

cmds.normalConstraint( 'surf1', 'surf2', 'cube2', w=.1 )
uses the average of the normals from surf1 and surf2.

cmds.normalConstraint( 'surf1', 'cube2', e=True, w=10. )
sets the weight for surf1's effect on cube2 to 10.

cmds.normalConstraint( 'surf2', 'cube2', e=True, rm=True )
removes surf2 from cube2's normalConstraint.

cmds.normalConstraint( 'surf3', 'cube2' )
adds surf3 to cube2's normalConstraint with the default weight.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/normalConstraint.html 
    """


def nurbsBoolean(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagnsrfsInFirstShell: int, flagobject: boolean, flagoperation: int, flagsmartConnection: boolean, flagtolerance: linear) -> list[string]:
    """Synopsis:
---
---
 nurbsBoolean(
surface surface
    , [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [nsrfsInFirstShell=int], [object=boolean], [operation=int], [smartConnection=boolean], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsBoolean is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To do a union between two cubes.
cmds.nurbsBoolean( 'nurbsCube1', 'nurbsCube2', nsf=1, op=0 )

To do a subtract between a cube and a sphere.
i.e cube - sphere
cmds.nurbsBoolean( 'nurbsCube1', 'nurbsSphere1', op=1, nsf=1 )

To do an intersect between two spheres.
cmds.nurbsBoolean( 'nurbsSphere1', 'nurbsSphere2', op=2, nsf=1 )

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
operation(op): int
    properties: create, query, edit
    Type of Boolean operation.
Default: 0

---
tolerance(tlb): linear
    properties: create, query, edit
    fitting tolerance.
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
nsrfsInFirstShell(nsf): int
    properties: create
    The number of selection items comprising the first shell.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
smartConnection(sc): boolean
    properties: create
    Look for any of the selection items having a boolean operation as
history.
Default is true.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsBoolean.html 
    """


def nurbsCopyUVSet() -> boolean:
    """Synopsis:
---
---
 nurbsCopyUVSet()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsCopyUVSet is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.nurbsCopyUVSet()

---
Return:
---


    boolean: Success or Failure.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsCopyUVSet.html 
    """


def nurbsCube(flagaxis: tuple[linear, linear, linear], flagcaching: boolean, flagconstructionHistory: boolean, flagdegree: int, flagheightRatio: float, flaglengthRatio: float, flagname: string, flagnodeState: int, flagobject: boolean, flagpatchesU: int, flagpatchesV: int, flagpivot: tuple[linear, linear, linear], flagpolygon: int, flagwidth: linear) -> list[string]:
    """Synopsis:
---
---
 nurbsCube([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean], [degree=int], [heightRatio=float], [lengthRatio=float], [name=string], [nodeState=int], [object=boolean], [patchesU=int], [patchesV=int], [pivot=[linear, linear, linear]], [polygon=int], [width=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsCube is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.nurbsCube()
cmds.nurbsCube( w=3, hr=5 )
cmds.nurbsCube( w=10, p=(0, 0, 1) )
cmds.nurbsCube( d=1, u=3, v=5, w=5 )

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
    The degree of the resulting surface.
1 - linear,
2 - quadratic,
3 - cubic,
5 - quintic,
7 - heptic
Default: 3

---
heightRatio(hr): float
    properties: create, query, edit
    Ratio of "height" to "width"
Default: 1.0

---
lengthRatio(lr): float
    properties: create, query, edit
    Ratio of "length" to "width"
Default: 1.0

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
patchesU(u): int
    properties: create, query, edit
    Number of sections in U
Default: 1

---
patchesV(v): int
    properties: create, query, edit
    Number of sections in V
Default: 1

---
pivot(p): [linear, linear, linear]
    properties: create, query, edit
    The primitive's pivot point

---
width(w): linear
    properties: create, query, edit
    Width of the object
Default: 1.0

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsCube.html 
    """


def nurbsCurveToBezier() -> list[string]:
    """Synopsis:
---
---
 nurbsCurveToBezier(
curve
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsCurveToBezier is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.nurbsCurveToBezier( )
Converts call selected NURBS curves to Bezier curves.

---
Return:
---


    list[string]: (object name and node name)

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsCurveToBezier.html 
    """


def nurbsEditUV(flagangle: float, flagpivotU: float, flagpivotV: float, flagrelative: boolean, flagrotateRatio: float, flagrotation: boolean, flagscale: boolean, flagscaleU: float, flagscaleV: float, flaguValue: float, flagvValue: float) -> boolean:
    """Synopsis:
---
---
 nurbsEditUV([angle=float], [pivotU=float], [pivotV=float], [relative=boolean], [rotateRatio=float], [rotation=boolean], [scale=boolean], [scaleU=float], [scaleV=float], [uValue=float], [vValue=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsEditUV is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

result = cmds.sphere()
shape = result[0]
cmds.select(shape, r=True)

cmds.nurbsUVSet(create=True)
cmds.nurbsUVSet(useExplicit=True)

cmds.select(shape+".cv[3:5][2:4]", r=True)

Rotate the UVs by 45 degrees
cmds.nurbsEditUV(angle=45)

---
Return:
---


    boolean: Success or Failure.

Flags:
---


---
angle(a): float
    properties: create, query
    Specifies the angle value (in degrees) by which the UV values are to be rotated.

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
    Specifies the ratio value by which the UV values are to be rotated.
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
vValue(v): float
    properties: create, query
    Specifies the value, in the v direction - absolute if relative flag is false..

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsEditUV.html 
    """


def nurbsPlane(flagaxis: tuple[linear, linear, linear], flagcaching: boolean, flagconstructionHistory: boolean, flagdegree: int, flaglengthRatio: float, flagname: string, flagnodeState: int, flagobject: boolean, flagpatchesU: int, flagpatchesV: int, flagpivot: tuple[linear, linear, linear], flagpolygon: int, flagwidth: linear) -> list[string]:
    """Synopsis:
---
---
 nurbsPlane([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean], [degree=int], [lengthRatio=float], [name=string], [nodeState=int], [object=boolean], [patchesU=int], [patchesV=int], [pivot=[linear, linear, linear]], [polygon=int], [width=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsPlane is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create default plane
cmds.nurbsPlane()

Create a degree 3 plane with 4 spans in each direction
cmds.nurbsPlane( d=3, u=4, v=4 )

Create plane that is twice as long as it is wide
cmds.nurbsPlane( w=3, lr=2 )

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
    The degree of the resulting surface
1 - linear,
2 - quadratic,
3 - cubic,
5 - quintic,
7 - heptic
Default: 3

---
lengthRatio(lr): float
    properties: create, query, edit
    The ratio of "length" to "width" of the plane.
Default: 1.0

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
patchesU(u): int
    properties: create, query, edit
    The number of spans in the U direction.
Default: 1

---
patchesV(v): int
    properties: create, query, edit
    The number of spans in the V direction.
Default: 1

---
pivot(p): [linear, linear, linear]
    properties: create, query, edit
    The primitive's pivot point

---
width(w): linear
    properties: create, query, edit
    The width of the plane
Default: 1.0

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsPlane.html 
    """


def nurbsSelect(flagborderSelection: boolean, flagbottomBorder: boolean, flaggrowSelection: int, flagleftBorder: boolean, flagrightBorder: boolean, flagshrinkSelection: int, flagtopBorder: boolean) -> None:
    """Synopsis:
---
---
 nurbsSelect([borderSelection=boolean], [bottomBorder=boolean], [growSelection=int], [leftBorder=boolean], [rightBorder=boolean], [shrinkSelection=int], [topBorder=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsSelect is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Create a Nurbs plane.
cmds.nurbsPlane( u=5, v=7 )

Select it top and bottom CVs.
cmds.nurbsSelect( topBorder=True, bottomBorder=True )

Expand the selection to 3 rows.
cmds.nurbsSelect( growSelection=3 )

Select only the outline of the rows.
cmds.nurbsSelect( borderSelection=True )

---


Flags:
---


---
borderSelection(bs): boolean
    properties: create
    Extract the border of the current CV selection.

---
bottomBorder(bb): boolean
    properties: create
    Selects the bottom border of the surface (V=0).

---
growSelection(gs): int
    properties: create
    Grows the CV selection by the given number of CV

---
leftBorder(lb): boolean
    properties: create
    Selects the left border of the surface (U=0).

---
rightBorder(rb): boolean
    properties: create
    Selects the right border of the surface (U=MAX).

---
shrinkSelection(ss): int
    properties: create
    Shrinks the CV selection by the given number of CV

---
topBorder(tb): boolean
    properties: create
    Selects the top border of the patches (V=MAX).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsSelect.html 
    """


def nurbsSquare(flagcaching: boolean, flagcenter: tuple[linear, linear, linear], flagcenterX: linear, flagcenterY: linear, flagcenterZ: linear, flagconstructionHistory: boolean, flagdegree: int, flagname: string, flagnodeState: int, flagnormal: tuple[linear, linear, linear], flagnormalX: linear, flagnormalY: linear, flagnormalZ: linear, flagobject: boolean, flagsideLength1: linear, flagsideLength2: linear, flagspansPerSide: int) -> list[string]:
    """Synopsis:
---
---
 nurbsSquare([caching=boolean], [center=[linear, linear, linear]], [centerX=linear], [centerY=linear], [centerZ=linear], [constructionHistory=boolean], [degree=int], [name=string], [nodeState=int], [normal=[linear, linear, linear]], [normalX=linear], [normalY=linear], [normalZ=linear], [object=boolean], [sideLength1=linear], [sideLength2=linear], [spansPerSide=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsSquare is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

create degree 1 square with side length 2, center (0,0,0) on the
x-y plane
cmds.nurbsSquare( nr=(0, 0, 1), d=1, c=(0, 0, 0), sl1=2, sl2=2 )

create degree 2 rectangle with length 2,4 at origin on the x-y plane
cmds.nurbsSquare( d=2, nr=(0, 0, 1), c=(0, 0, 0), sl1=2, sl2=4 )

create square of degree 3,side lengths 3, 4 spans per side
cmds.nurbsSquare( nr=(0, 0, 1), c=(0, 0, 0), d=3, sl1=3, sl2=3, sps=4 )

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
center(c): [linear, linear, linear]
    properties: create, query, edit
    The center point of the square.

---
centerX(cx): linear
    properties: create, query, edit
    X of the center point.
Default: 0

---
centerY(cy): linear
    properties: create, query, edit
    Y of the center point.
Default: 0

---
centerZ(cz): linear
    properties: create, query, edit
    Z of the center point.
Default: 0

---
degree(d): int
    properties: create, query, edit
    The degree of the resulting circle:
1 - linear,
2 - quadratic,
3 - cubic,
5 - quintic,
7 - heptic
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
normal(nr): [linear, linear, linear]
    properties: create, query, edit
    The normal of the plane in which the square will lie.

---
normalX(nrx): linear
    properties: create, query, edit
    X of the normal direction.
Default: 0

---
normalY(nry): linear
    properties: create, query, edit
    Y of the normal direction.
Default: 0

---
normalZ(nrz): linear
    properties: create, query, edit
    Z of the normal direction.
Default: 1

---
sideLength1(sl1): linear
    properties: create, query, edit
    The length of a side on the square.
Default: 1.0

---
sideLength2(sl2): linear
    properties: create, query, edit
    The length of an adjacent side on the square.
Default: 1.0

---
spansPerSide(sps): int
    properties: create, query, edit
    The number of spans per side determines the resolution of the square.
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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsSquare.html 
    """


def nurbsToPoly(flagcaching: boolean, flagconstructionHistory: boolean, flagcurvatureTolerance: int, flagexplicitTessellationAttributes: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagsmoothEdge: boolean, flagsmoothEdgeRatio: float, flaguDivisionsFactor: float, flagvDivisionsFactor: float) -> list[string]:
    """Synopsis:
---
---
 nurbsToPoly(
[surface]
    , [caching=boolean], [constructionHistory=boolean], [curvatureTolerance=int], [explicitTessellationAttributes=boolean], [name=string], [nodeState=int], [object=boolean], [smoothEdge=boolean], [smoothEdgeRatio=float], [uDivisionsFactor=float], [vDivisionsFactor=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsToPoly is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new polygonal surface from a NURBS surface:
cmds.nurbsToPoly( 'nurbsSphere1' )

To create a new polygonal surface from a NURBS surface with
history so that the tesselation can be edited afterwards:
cmds.nurbsToPoly( 'nurbsSphere1', ch=True )

---
Return:
---


    list[string]: The polygon and optionally the dependency node name.

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
curvatureTolerance(cvt): int
    properties: create, query, edit
    Presets for level of secondary criteria curvature tolerance:
0 = highest tolerance, 1 = high tolerance, 2 = medium tolerance,
3 = no tolerance
Default: 2

---
explicitTessellationAttributes(eta): boolean
    properties: create, query, edit
    specify advanced or novice mode for tessellation parameters
Default: true

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

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
smoothEdge(ues): boolean
    properties: create, query, edit
    Specifies if the decision to continue tessellation should be
based on the nurbs edge smoothness
Default: false

---
smoothEdgeRatio(esr): float
    properties: create, query, edit
    Specifies the edge smooth ratio.  The higher the value, the
smoother the edge will be.
Default: 0.99

---
uDivisionsFactor(nuf): float
    properties: create, query, edit
    Specifies the tessellation increase factor in U for novice mode
Default: 1.5

---
vDivisionsFactor(nvf): float
    properties: create, query, edit
    Specifies the tessellation increase factor in V for novice mode
Default: 1.5

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsToPoly.html 
    """


def nurbsToPolygonsPref(flagchordHeight: float, flagchordHeightRatio: float, flagdelta3D: float, flagedgeSwap: boolean, flagformat: uint, flagfraction: float, flagmatchRenderTessellation: uint, flagmerge: uint, flagmergeTolerance: float, flagminEdgeLen: float, flagpolyCount: uint, flagpolyType: uint, flaguNumber: uint, flaguType: uint, flaguseChordHeight: boolean, flaguseChordHeightRatio: boolean, flagvNumber: uint, flagvType: uint) -> None:
    """Synopsis:
---
---
 nurbsToPolygonsPref([chordHeight=float], [chordHeightRatio=float], [delta3D=float], [edgeSwap=boolean], [format=uint], [fraction=float], [matchRenderTessellation=uint], [merge=uint], [mergeTolerance=float], [minEdgeLen=float], [polyCount=uint], [polyType=uint], [uNumber=uint], [uType=uint], [useChordHeight=boolean], [useChordHeightRatio=boolean], [vNumber=uint], [vType=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsToPolygonsPref is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

To find out what the current format is:
cmds.nurbsToPolygonsPref( q=True, f=True )

---


Flags:
---


---
format(f): uint
    properties: create, query
    Valid values are 0, 1 and 2.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsToPolygonsPref.html 
    """


def nurbsToSubdiv(flagaddUnderTransform: boolean, flagcaching: boolean, flagcollapsePoles: boolean, flagconstructionHistory: boolean, flagmatchPeriodic: boolean, flagmaxPolyCount: int, flagname: string, flagnodeState: int, flagobject: boolean, flagreverseNormal: boolean) -> list[string]:
    """Synopsis:
---
---
 nurbsToSubdiv(
[surface]
    , [addUnderTransform=boolean], [caching=boolean], [collapsePoles=boolean], [constructionHistory=boolean], [matchPeriodic=boolean], [maxPolyCount=int], [name=string], [nodeState=int], [object=boolean], [reverseNormal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsToSubdiv is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new subd surface from a NURBS surface:
cmds.nurbsToSubdiv( 'nurbsSphere1' )

To create a new subd surface from a NURBS surface with history so that
the tesselation can be edited afterwards:
cmds.nurbsToSubdiv( 'nurbsSphere1', ch=True )

---
Return:
---


    list[string]: The subd surface and optionally the dependency node name

Flags:
---


---
addUnderTransform(aut): boolean
    properties: create, query, edit
    Specify whether the new surface should be added under the old transform or not.

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
collapsePoles(cp): boolean
    properties: create, query, edit
    Collapse poles into a single point
Default: false

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
matchPeriodic(mp): boolean
    properties: create, query, edit
    Match periodic surface texture mapping in the result.
Default: false

---
maxPolyCount(mpc): int
    properties: create, query, edit
    The maximum number of base mesh faces in the resulting subdivision surface.
Default: 1000

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

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
reverseNormal(rn): boolean
    properties: create, query, edit
    Reverse the NURBS surface normal in the conversion.
Default: true

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsToSubdiv.html 
    """


def nurbsToSubdivPref(flagbridge: int, flagcapType: int, flagcollapsePoles: boolean, flagmatchPeriodic: boolean, flagmaxPolyCount: int, flagoffset: linear, flagreverseNormal: boolean, flagsolidType: int, flagtrans00: float, flagtrans01: float, flagtrans02: float, flagtrans10: float, flagtrans11: float, flagtrans12: float, flagtrans20: float, flagtrans21: float, flagtrans22: float, flagtrans30: float, flagtrans31: float, flagtrans32: float) -> None:
    """Synopsis:
---
---
 nurbsToSubdivPref([bridge=int], [capType=int], [collapsePoles=boolean], [matchPeriodic=boolean], [maxPolyCount=int], [offset=linear], [reverseNormal=boolean], [solidType=int], [trans00=float], [trans01=float], [trans02=float], [trans10=float], [trans11=float], [trans12=float], [trans20=float], [trans21=float], [trans22=float], [trans30=float], [trans31=float], [trans32=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsToSubdivPref is undoable, queryable, and NOT editable.
To query any of the flags, use the "-query" flag.

For more information on the flags, see the node documentation for
the "nurbsToSubdivProc" node.




Example:
---
import maya.cmds as cmds

To find out what the current format is:
cmds.nurbsToSubdivPref( q=True, maxPolyCount=True )

---


Flags:
---


---
bridge(br): int
    properties: create, query
    Valid values are 0, 1, 2 or 3.

---
capType(ct): int
    properties: create, query
    Valid values are 0 or 1.

---
solidType(st): int
    properties: create, query
    Valid values are 0, 1 or 2.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsToSubdivPref.html 
    """


def nurbsUVSet(flagcreate: boolean, flaguseExplicit: boolean) -> boolean:
    """Synopsis:
---
---
 nurbsUVSet([create=boolean], [useExplicit=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

nurbsUVSet is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

result = cmds.sphere()
shape = result[0]
cmds.select(shape, r=True)

Create and activate a UV set
cmds.nurbsUVSet(create=True)
cmds.nurbsUVSet(useExplicit=True)

cmds.select(shape+".cv[3:5][2:4]", r=True)

Rotate the UVs by 45 degrees
cmds.nurbsEditUV(angle=45)

---
Return:
---


    boolean: Success or Failure.

Flags:
---


---
create(c): boolean
    properties: create, query, edit
    Creates an explicit UV set on the specified surface. If the surface already has an
explicit UV set this flag will do nothing. Use the -ue/useExplicit flag to set/unset
the explicit UV set as the current UV set.

---
useExplicit(ue): boolean
    properties: create, query, edit
    Toggles the usage of explicit/implicit UVs. When true, explicit UVs will be used,
otherwise the object will use implicit UVs.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/nurbsUVSet.html 
    """
