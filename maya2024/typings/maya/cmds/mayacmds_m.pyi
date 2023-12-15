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


def makeIdentity(flagapply: boolean, flagjointOrient: boolean, flagnormal: uint, flagpreserveNormals: boolean, flagrotate: boolean, flagscale: boolean, flagtranslate: boolean) -> None:
    """Synopsis:
---
---
 makeIdentity(
[dagObject]
    , [apply=boolean], [jointOrient=boolean], [normal=uint], [preserveNormals=boolean], [rotate=boolean], [scale=boolean], [translate=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

makeIdentity is undoable, NOT queryable, and NOT editable.
translate = 0, 0, 0
rotate = 0, 0, 0
scale = 1, 1, 1
shear = 1, 1, 1

If a transform is a joint, then the "translate" attribute may not be 0,
but will be used to position the joints so that they preserve their
world space positions.  The translate flag doesn't apply to joints,
since joints must preserve their world space positions.  Only the rotate
and scale flags are meaningful when applied to joints.

If the -a/apply flag is true, then the transforms that are reset
are accumulated and applied to the all shapes below the modified
transforms, so that the shapes will not move. The pivot positions are
recalculated so that they also will not move in world space.
If this flag is false, then the transformations are reset to identity,
without any changes to preserve position.




Example:
---
import maya.cmds as cmds

Example 1:  Create a hierarchical object, for example a
car. Scale the tires, translate the doors into place, rotate the
steering wheel, then select the group node above the car, and type:

cmds.makeIdentity( apply=True )
The car should not move.

cmds.move( 3, 0, 0 )
The car should move exactly 3 units to (3, 0, 0), since
the previous makeIdentity command set its translation to (0, 0, 0).

cmds.makeIdentity()
The car should return to the same position as before the move.

Example 2:  Create a curve and translate, rotate and scale it.
Then group it and translate, rotate and scale the group.

cmds.makeIdentity( 'group1', apply=True, translate=True )
The curve will not move, but both the curve transform's and group
transform's translation will be set to 0, 0, 0. The rotation and
scale will remain the same.

cmds.makeIdentity( 'group1', apply=True, rotate=True )
The curve will not move, but both the curve transform's and group
transform's rotation will be set to 0, 0, 0. The translation and
scale will remain the same.

cmds.makeIdentity( 'group1', apply=True, scale=True )
The curve will not move, but both the curve transform's and group
transform's scale will be set to 1, 1, 1. The translation and rotation
will remain the same.

cmds.makeIdentity( 'group1', apply=True, translate=True, rotate=True )
The curve will not move, but both the curve transform's and group
transform's translation and rotation will be set to 0, 0, 0.
The scale will remain the same.

cmds.makeIdentity( 'group1', apply=False, translate=True )
The curve transform and group transform will have their translation
set to 0, 0, 0. The curve will probably move, since the apply
flag is false.

cmds.makeIdentity( apply=True, translate=True, rotate=True, scale=True )
This is the same as "makeIdentity -apply true".

Example 3:  Create a polyCube and translate, rotate and scale it.
And then freeze the normals.

cmds.polyCube()
cmds.rotate( 30, 45, 0 )
cmds.move( 2, 0, 2, r=True )
cmds.scale( 2, 1, 2, r=True )
cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )

---


Flags:
---


---
apply(a): boolean
    properties: create
    If this flag is true, the accumulated transforms are applied to
the shape after the transforms are made identity, such that the
world space positions of the transforms pivots are preserved,
and the shapes do not move. The default is false.

---
jointOrient(jo): boolean
    properties: create
    If this flag is set, the joint orient on joints will be reset
to align with worldspace.

---
normal(n): uint
    properties: create
    If this flag is set to 1, the normals on polygonal objects
will be frozen.  This flag is valid only when the -apply flag is on.
If this flag is set to 2, the normals on polygonal objects will
be frozen only if its a non-rigid transformation matrix.
ie, a transformation that does not contain shear, skew or
non-proportional scaling.
The default behaviour is not to freeze normals.

---
preserveNormals(pn): boolean
    properties: create
    If this flag is true, the normals on polygonal objects will be
reversed if the objects are negatively scaled (reflection).
This flag is valid only when the -apply flag is on.

---
rotate(r): boolean
    properties: create
    If this flag is true, only the rotation is applied to the shape.
The rotation will be changed to 0, 0, 0.
If neither translate nor rotate nor scale flags are specified,
then all (t, r, s) are applied.

---
scale(s): boolean
    properties: create
    If this flag is true, only the scale is applied to the shape.
The scale factor will be changed to 1, 1, 1.
If neither translate nor rotate nor scale flags are specified,
then all (t, r, s) are applied.

---
translate(t): boolean
    properties: create
    If this flag is true, only the translation is applied to the shape.
The translation will be changed to 0, 0, 0.
If neither translate nor rotate nor scale flags are specified,
then all (t, r, s)  are applied.  (Note: the translate flag is not
meaningful when applied to joints, since joints are made to preserve
their world space position.  This flag will have no effect on joints.)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/makeIdentity.html 
    """


def makeLive(flagaddObjects: boolean, flagnone: boolean, flagregistry: int, flagregistryCount: boolean, flagregistryReset: boolean, flagregistrySize: int, flagremoveObjects: boolean) -> None:
    """Synopsis:
---
---
 makeLive(
[surface...]
    , [addObjects=boolean], [none=boolean], [registry=int], [registryCount=boolean], [registryReset=boolean], [registrySize=int], [removeObjects=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

makeLive is undoable, queryable, and editable.
The makeLive command expects one of these types of objects as an explicit
argument.  If no argument is explicitly specified, then there are a number
of default behaviours based on what is currently active.  The command will
fail if the active object(s) is/are not one of the valid types of objects.
If there is nothing active, the current live object(s) will become dormant.
Otherwise, the active object(s) will become the live object(s).

The command allows for a limited number of objects collections to be saved
in a registry entry. These collections can be queried and/or made live.




Example:
---
import maya.cmds as cmds

cmds.makeLive( 'surface1' )
cmds.makeLive( none=True )

---


Flags:
---


---
addObjects(ao): boolean
    properties: edit
    Add the listed object(s) to the current live list.
If an object is already in the live list, it is ignored.

---
none(n): boolean
    properties: create
    If the -n/none flag, the live object(s) will become dormant.
Use of this flag causes any arguments to be ignored.

---
registry(r): int
    properties: create, query
    Make live the objects defined in the specified registry entry.
In Query mode, return the list of objects defined in the specified registry entry.

---
registryCount(rc): boolean
    properties: query
    Return the actual number of registry entries.
This number ranges from 0 to 'registrySize' - 1.

---
registryReset(rr): boolean
    properties: create
    Reset the maximum number of registry entries to the default value and clear all stored data.

---
registrySize(rs): int
    properties: create, query
    Defines the maximum number of registry entries that are remembered by the command.
In Query mode, returns the maximum number currently set.

---
removeObjects(ro): boolean
    properties: edit
    Remove the listed object(s) from the current live list.
If an object is not in the list, it is ignored.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/makeLive.html 
    """


def makePaintable(flagactivate: boolean, flagactivateAll: boolean, flagaltAttribute: string, flagattrType: string, flagclearAll: boolean, flagremove: boolean, flagshapeMode: string, flaguiName: string) -> None:
    """Synopsis:
---
---
 makePaintable([string][string], [activate=boolean], [activateAll=boolean], [altAttribute=string], [attrType=string], [clearAll=boolean], [remove=boolean], [shapeMode=string], [uiName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

makePaintable is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Make particle.mass paintable.
cmds.makePaintable( 'particle', 'mass', attrType='doubleArray' )

Make particle.goalPP paintable, with a ui name myGoalPP.
Also make the goalPP0 attribute painted simultaneously
cmds.makePaintable( 'particle', 'goalPP', attrType='doubleArray', ui='myGoalPP', altAttribute='goalPP0' )

Make weightGeometryFilter.weights paintable. Define
weightGeometryFilter as a deformer node.
cmds.makePaintable( 'weightGeometryFilter', 'weights', attrType='multiFloat', sm='deformer' )

Make all the attributes paintable on the artAttrPaintTest node.
cmds.makePaintable( 'artAttrPaintTest', 'intArray', attrType='intArray' )
cmds.makePaintable( 'artAttrPaintTest', 'dblArray', attrType='doubleArray' )
cmds.makePaintable( 'artAttrPaintTest', 'vecArray', attrType='vectorArray' )
cmds.makePaintable( 'artAttrPaintTest', 'intMulti', attrType='multiInteger' )
cmds.makePaintable( 'artAttrPaintTest', 'fltMulti', attrType='multiFloat' )
cmds.makePaintable( 'artAttrPaintTest', 'dblMulti', attrType='multiDouble' )
cmds.makePaintable( 'artAttrPaintTest', 'flt3Multi', attrType='multiVector' )
cmds.makePaintable( 'artAttrPaintTest', 'dbl3Multi', attrType='multiVector' )

---


Flags:
---


---
activate(ac): boolean
    properties: create, query
    Activate / deactivate the given paintable attribute. Used
to filter out some nodes in the attribute paint tool.

---
activateAll(aca): boolean
    properties: create, query
    Activate / deactivate all the registered paintable attributes. Used
to filter out some nodes in the attribute paint tool.

---
altAttribute(aa): string
    properties: create, query, multiuse
    Define an alternate attribute which will also receive the same
values. There can be multiple such flags.

---
attrType(at): string
    properties: create, query
    Paintable attribute type.
   Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.

---
clearAll(ca): boolean
    properties: create, query
    Removes all paintable attribute definitions.

---
remove(rm): boolean
    properties: create, query
    Make the attribute not paintable any more.

---
shapeMode(sm): string
    properties: create, query
    This flag controls how Artisan correlates the paintable node to a
corresponding shape node.  It is used for attributes of type multi
of multi, where the first multi dimension corresponds to the shape
index (i.e. cluster nodes). At present, only one value of this flag
is supported: "deformer". By default this flag is an empty string,
which means that there is a direct indexing (no special mapping
required) of the attribute with respect to vertices on the shape.

---
uiName(ui): string
    properties: create, query
    UI name. Default is the attribute name.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/makePaintable.html 
    """


def makeSingleSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagstitchTolerance: float) -> list[string]:
    """Synopsis:
---
---
 makeSingleSurface(
surface
    , [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean], [stitchTolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

makeSingleSurface is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To make a single poly surface from a bunch of surfaces
cmds.makeSingleSurface( 'nurbsPlane1', 'nurbsPlane2', 'nurbsPlane3' )

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

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
stitchTolerance(st): float
    properties: edit
    Stitch tolerance.
Default: 0.1

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/makeSingleSurface.html 
    """


def makebot(flagcheckdepends: boolean, flagcheckres: uint, flaginput: string, flagnooverwrite: boolean, flagoutput: string, flagverbose: boolean) -> None:
    """Synopsis:
---
---
 makebot([checkdepends=boolean], [checkres=uint], [input=string], [nooverwrite=boolean], [output=string], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

makebot is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.makebot( i='in_image', o='/usr/tmp/out_bot_file' )

---


Flags:
---


---
checkdepends(c): boolean
    properties: create
    the BOT file should only be generated if it doesn't already exists,
or if it is older than the source file

---
checkres(r): uint
    properties: create
    the BOT file should only be generated if its resolution (maximum of
width and height) is larger than the minimum value specified by the
argument

---
input(i): string
    properties: create
    input image file

---
nooverwrite(nov): boolean
    properties: create
    If -c and/or -r indicate that the BOT file should be generated but
if already exists, then this flag will prevent the file from being
overwritten

---
output(o): string
    properties: create
    output BOT file

---
verbose(v): boolean
    properties: create
    Makebot will provide feedback if this flag is specified

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/makebot.html 
    """


def manipMoveContext(flagactiveHandle: int, flagactiveHandleNormal: int, flagalignAlong: tuple[float, float, float], flagbakePivotOri: boolean, flagconstrainAlongNormal: boolean, flagcurrentActiveHandle: int, flageditPivotMode: boolean, flageditPivotPosition: boolean, flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaginteractiveUpdate: boolean, flaglastMode: int, flagmanipVisible: boolean, flagmode: int, flagorientAxes: tuple[float, float, float], flagorientJoint: string, flagorientJointEnabled: boolean, flagorientObject: string, flagorientTowards: tuple[float, float, float], flagpinPivot: boolean, flagpivotOriHandle: boolean, flagposition: boolean, flagpostCommand: script, flagpostDragCommand: tuple[script, string], flagpreCommand: script, flagpreDragCommand: tuple[script, string], flagpreserveChildPosition: boolean, flagpreserveUV: boolean, flagreflection: boolean, flagreflectionAbout: int, flagreflectionAxis: int, flagreflectionTolerance: float, flagresetPivotMode: int, flagsecondaryAxisOrient: string, flagsnap: boolean, flagsnapComponentsRelative: boolean, flagsnapLiveFaceCenter: boolean, flagsnapLivePoint: boolean, flagsnapPivotOri: boolean, flagsnapPivotPos: boolean, flagsnapRelative: boolean, flagsnapValue: float, flagtranslate: tuple[float, float, float], flagtweakMode: boolean, flagxformConstraint: string) -> string:
    """Synopsis:
---
---
 manipMoveContext(
[object]
    , [activeHandle=int], [activeHandleNormal=int], [alignAlong=[float, float, float]], [bakePivotOri=boolean], [constrainAlongNormal=boolean], [currentActiveHandle=int], [editPivotMode=boolean], [editPivotPosition=boolean], [exists=boolean], [image1=string], [image2=string], [image3=string], [interactiveUpdate=boolean], [lastMode=int], [manipVisible=boolean], [mode=int], [orientAxes=[float, float, float]], [orientJoint=string], [orientJointEnabled=boolean], [orientObject=string], [orientTowards=[float, float, float]], [pinPivot=boolean], [pivotOriHandle=boolean], [position=boolean], [postCommand=script], [postDragCommand=[script, string]], [preCommand=script], [preDragCommand=[script, string]], [preserveChildPosition=boolean], [preserveUV=boolean], [reflection=boolean], [reflectionAbout=int], [reflectionAxis=int], [reflectionTolerance=float], [resetPivotMode=int], [secondaryAxisOrient=string], [snap=boolean], [snapComponentsRelative=boolean], [snapLiveFaceCenter=boolean], [snapLivePoint=boolean], [snapPivotOri=boolean], [snapPivotPos=boolean], [snapRelative=boolean], [snapValue=float], [translate=[float, float, float]], [tweakMode=boolean], [xformConstraint=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipMoveContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new move context:
cmds.manipMoveContext()

To query the mode of an existing context:
cmds.manipMoveContext( 'manipMoveContext1', q=True, mode=True )

To edit an existing context to come up with the X axis handle
active by default:
cmds.manipMoveContext( 'manipMoveContext1', e=True, ah=0 )

cmds.spaceLocator( p=(0, 0, 0), name='locatorA' )

cmds.manipMoveContext( 'manipMoveContext1', e=True, m=2 ) WorldSpace
cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=0.4 )
Now, dragging any of the move handles will
move the object in steps of 0.4 units.

cmds.move( 0.8, 0, 0, 'locatorA', a=True )
cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=False )
Now, dragging X-axis handle will
move the object in steps of 2 units, and will
place the object anywhere in (0,0,0) (2,0,0) (4,0,0) ...etc
NOTE: If in objectSpace Mode, the snapRelative should be ON.
Absolute discrete move is not supported in objectSpace mode.

cmds.move( 0.8, 0, 0, 'locatorA', a=True )
cmds.manipMoveContext( 'manipMoveContext1', e=True, snap=True )
cmds.manipMoveContext( 'manipMoveContext1', e=True, snapValue=2 )
cmds.manipMoveContext( 'manipMoveContext1', e=True, snapRelative=True )
Now, dragging X-axis handle will
move the object in steps of 2 units, and will
place the object anywhere in (2.8,0,0) (4.8,0,0) (6.8,0,0) ...etc

---
Return:
---


    string: The name of the new context

Flags:
---


---
activeHandle(ah): int
    properties: query, edit
    Sets the default active handle for the manip.  That is, the handle
which should be initially active when the tool is activated.
Values can be:

0 - X axis handle is active
1 - Y axis handle is active
2 - Z axis handle is active
3 - Center handle (all 3 axes) is active (default)

---
activeHandleNormal(ahn): int
    properties: query, edit
    0 - U axis handle is active
1 - V axis handle is active
2 - N axis handle is active ( default )
3 - Center handle (all 3 axes) is active

applicable only when the manip mode is 3.

---
alignAlong(aa): [float, float, float]
    properties: create, edit
    Aligns active handle along vector.

---
bakePivotOri(bpo): boolean
    properties: query, edit
    Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.

---
constrainAlongNormal(xn): boolean
    properties: query, edit
    When true, transform constraints are applied along the vertex normal first
and only use the closest point when no intersection is found along the normal.

---
currentActiveHandle(cah): int
    properties: query, edit
    Sets the active handle for the manip.
Values can be:

0 - X axis handle is active
1 - Y axis handle is active
2 - Z axis handle is active
3 - Center handle (all 3 axes) is active
4 - XY plane handle is active
5 - YZ plane handle is active
6 - XZ plane handle is active

---
editPivotMode(epm): boolean
    properties: query
    Returns true manipulator is in edit pivot mode

---
editPivotPosition(epp): boolean
    properties: query
    Returns the current position of the edit pivot manipulator.

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
interactiveUpdate(iu): boolean
    properties: query, edit
    Value can be : true or false.
This flag value is valid only if the mode is 3 i.e. move vertex normal.

---
lastMode(lm): int
    properties: query
    Returns the previous translation mode.

---
manipVisible(vis): boolean
    properties: query
    Returns true if the main translate manipulator is visible.

---
mode(m): int
    properties: query, edit
    Translate mode:

0 - Object Space
1 - Local Space
2 - World Space (default)
3 - Move Along Vertex Normal
4 - Move Along Rotation Axis
5 - Move Along Live Object Axis
6 - Custom Axis Orientation
10 - Component Space

---
orientAxes(oa): [float, float, float]
    properties: query, edit
    Orients manipulator rotating around axes by specified angles

---
orientJoint(oj): string
    properties: query, edit
    Specifies the type of orientation for joint orientation. Valid options are:
none, xyz, xzy, yxz, yzx, zxy, zyx.

---
orientJointEnabled(oje): boolean
    properties: query, edit
    Specifies if joints should be reoriented when moved.

---
orientObject(oo): string
    properties: create, edit
    Orients manipulator to the passed in object/component

---
orientTowards(ot): [float, float, float]
    properties: create, edit
    Orients active handle towards world point

---
pinPivot(pin): boolean
    properties: query, edit
    Pin component pivot. When the component pivot is set and pinned selection
changes will not reset the pivot position and orientation.

---
pivotOriHandle(poh): boolean
    properties: query, edit
    When true, the pivot manipulator will show the orientation handle during editing.
Default is true.

---
position(p): boolean
    properties: query
    Returns the current position of the manipulator

---
postCommand(psc): script
    properties: create, edit
    Specifies a command to be executed when the tool is exited.

---
postDragCommand(pod): [script, string]
    properties: create, edit
    Specifies a command and a node type. The command will be executed at
the end of a drag when a node of the specified type is in the selection.

---
preCommand(prc): script
    properties: create, edit
    Specifies a command to be executed when the tool is entered.

---
preDragCommand(prd): [script, string]
    properties: create, edit
    Specifies a command and a node type. The command will be executed at
the start of a drag when a node of the specified type is in the selection.

---
preserveChildPosition(pcp): boolean
    properties: query, edit
    When false, the children objects move when their parent is moved.
When true, the worldspace position of the children will be maintained as
the parent is moved. Default is false.

---
preserveUV(puv): boolean
    properties: query, edit
    When false, the uvs are not changes to match the vertex edit.
When true, the uvs are edited to project to new values to stop texture
swimming as vertices are moved.

---
reflection(rfl): boolean
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionAbout(rab): int
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionAxis(rfa): int
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionTolerance(rft): float
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
resetPivotMode(rpm) 2024.2: int
    properties: query, edit
    Specifies the mode used when resetting the pivot position. Available modes are:

0: Center pivot (on bounding box)
1: Zero pivot (object-space origin)

---
secondaryAxisOrient(sao): string
    properties: query, edit
    Specifies the global axis (in world coordinates) that should be used
to should be used to align the second axis of the orientJointType triple.
Valid options are xup, yup, zup, xdown, ydown, zdown, none.

---
snap(s): boolean
    properties: query, edit
    Value can be : true or false.
Enable/Disable the discrete move.
If set to true, the move manipulator of all the
move contexts would snap at discrete points
along the active handle during mouse drag.  The
interval between the points can be controlled
using the 'snapValue' flag.

---
snapComponentsRelative(scr): boolean
    properties: query, edit
    Value can be : true or false.
If true, while snapping a group of CVs/Vertices, the
relative spacing between them will be preserved.
If false, all the CVs/Vertices will be snapped to the
target point
(is used during grid snap(hotkey 'x'), and
point snap(hotkey 'v'))
Depress the 'x' key before click-dragging the manip handle
and check to see the behaviour of moving a bunch of CVs,
with this flag ON and OFF.

---
snapLiveFaceCenter(slf): boolean
    properties: query, edit
    Value can be : true or false.
If true, while moving on the live polygon object, the
move manipulator will snap to the face centers of the object.

---
snapLivePoint(slp): boolean
    properties: query, edit
    Value can be : true or false.
If true, while moving on the live polygon object, the
move manipulator will snap to the vertices of the object.

---
snapPivotOri(spo): boolean
    properties: query, edit
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

---
snapPivotPos(spp): boolean
    properties: query, edit
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

---
snapRelative(sr): boolean
    properties: query, edit
    Value can be : true or false.
Applicable only when the snap is enabled.
If true, the snapValue is treated relative to the
original position before moving.
If false, the snapValue is treated relative to the
world origin.
NOTE:    If in local/object Space Mode,
the snapRelative should be ON.
Absolute discrete move is not supported
in local/object mode.

---
snapValue(sv): float
    properties: query, edit
    Applicable only when the snap is enabled.
The manipulator of all move contexts would move in
steps of 'snapValue'

---
translate(tr): [float, float, float]
    properties: query, edit
    Returns the translation of the manipulator for its current orientation/mode.

---
tweakMode(twk): boolean
    properties: query, edit
    When true, the manipulator is hidden and highlighted components can be selected
and moved in one step using a click-drag interaction.

---
xformConstraint(xc): string
    properties: query, edit
    none - no transform constraint
edge - edge transform constraint
surface - surface transform constraint

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipMoveContext.html 
    """


def manipMoveLimitsCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 manipMoveLimitsCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipMoveLimitsCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.manipMoveLimitsCtx()

---
Return:
---


    string: Name of newly created context

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipMoveLimitsCtx.html 
    """


def manipOptions(flagenableSmartDuplicate: boolean, flagenableSmartExtrude: boolean, flagforceRefresh: boolean, flaghandleSize: float, flaghideManipOnCtrl: boolean, flaghideManipOnShift: boolean, flaghideManipOnShiftCtrl: boolean, flaglinePick: float, flaglineSize: float, flagmiddleMouseRepositioning: boolean, flagpivotRotateHandleOffset: int, flagplaneHandleOffset: int, flagpointSize: float, flagpreselectHighlight: boolean, flagrefreshMode: int, flagrelative: boolean, flagrememberActiveHandle: boolean, flagrememberActiveHandleAfterToolSwitch: boolean, flagscale: float, flagshowExtrudeSliders: boolean, flagshowPivotRotateHandle: boolean, flagshowPlaneHandles: boolean, flagsmartDuplicateType: int) -> None:
    """Synopsis:
---
---
 manipOptions([enableSmartDuplicate=boolean], [enableSmartExtrude=boolean], [forceRefresh=boolean], [handleSize=float], [hideManipOnCtrl=boolean], [hideManipOnShift=boolean], [hideManipOnShiftCtrl=boolean], [linePick=float], [lineSize=float], [middleMouseRepositioning=boolean], [pivotRotateHandleOffset=int], [planeHandleOffset=int], [pointSize=float], [preselectHighlight=boolean], [refreshMode=int], [relative=boolean], [rememberActiveHandle=boolean], [rememberActiveHandleAfterToolSwitch=boolean], [scale=float], [showExtrudeSliders=boolean], [showPivotRotateHandle=boolean], [showPlaneHandles=boolean], [smartDuplicateType=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipOptions is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Scales all handles by a 1.5 factor
cmds.manipOptions( r=True, hs=1.5, ls=1.5 )

All manips are scaled by 2
cmds.manipOptions( s=2 )

---


Flags:
---


---
enableSmartDuplicate(esd): boolean
    properties: create, query
    Enables Shift-Duplicate option on t/r/s manips.

---
enableSmartExtrude(ese): boolean
    properties: create, query
    Enables Shift-Extrude option on t/r/s manips.

---
forceRefresh(fr): boolean
    properties: create
    Force a refresh if there is any deferred evaluation.

---
handleSize(hs): float
    properties: create, query
    Sets the maximum handles size in pixels, for small handles

---
hideManipOnCtrl(hmc): boolean
    properties: create, query
    Hide transform manip when the Ctrl key is pressed.

---
hideManipOnShift(hms): boolean
    properties: create, query
    Hide transform manip when the Shift key is pressed.

---
hideManipOnShiftCtrl(hsc): boolean
    properties: create, query
    Hide transform manip when the Shift and Ctrl keys are both pressed.

---
linePick(lp): float
    properties: create, query
    Set the width of picking zone for long handles

---
lineSize(ls): float
    properties: create, query
    Set the width of long handles (drawn as lines)

---
middleMouseRepositioning(mm): boolean
    properties: create, query
    Specify if the middle mouse should reposition

---
pivotRotateHandleOffset(pro): int
    properties: create, query
    Set the offset of the pivot rotation handle.

---
planeHandleOffset(pho): int
    properties: create, query
    Set the offset of the planar drag handles.

---
pointSize(ps): float
    properties: create, query
    Set the size of points (used to display previous states)

---
preselectHighlight(psh): boolean
    properties: create, query
    Set whether manip handles should be highlighted when moving mouse.

---
refreshMode(rm): int
    properties: create, query
    Set the global refresh mode.

---
relative(r): boolean
    properties: create
    All values are interpreted as multiplication factors instead
of final values.

---
rememberActiveHandle(rah): boolean
    properties: create, query
    Set whether manip handles should be remembered after selection change.

---
rememberActiveHandleAfterToolSwitch(rhs): boolean
    properties: create, query
    Set whether manip handles should be remembered after manipulator change.

---
scale(s): float
    properties: create, query
    Global scaling factor of all manipulators

---
showExtrudeSliders(ses): boolean
    properties: create, query
    Specify if the extrude sliders are to be shown on the manip

---
showPivotRotateHandle(spr): boolean
    properties: create, query
    Toggles the visibility of the pivot rotation handle.

---
showPlaneHandles(sph): boolean
    properties: create, query
    Toggles the visibility of the planar drag handles.

---
smartDuplicateType(sdt): int
    properties: create, query
    Change Shift-Duplicate or Shift-Extrude between Copy and Instance on t/r/s manips.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipOptions.html 
    """


def manipPivot(flagbakeOri: boolean, flagmoveToolOri: int, flagori: tuple[float, float, float], flagoriValid: boolean, flagpinPivot: boolean, flagpos: tuple[float, float, float], flagposValid: boolean, flagreset: boolean, flagresetMode: int, flagresetOri: boolean, flagresetPos: boolean, flagrotateToolOri: int, flagscaleToolOri: int, flagsnapOri: boolean, flagsnapPos: boolean, flagvalid: boolean) -> None:
    """Synopsis:
---
---
 manipPivot([bakeOri=boolean], [moveToolOri=int], [ori=[float, float, float]], [oriValid=boolean], [pinPivot=boolean], [pos=[float, float, float]], [posValid=boolean], [reset=boolean], [resetMode=int], [resetOri=boolean], [resetPos=boolean], [rotateToolOri=int], [scaleToolOri=int], [snapOri=boolean], [snapPos=boolean], [valid=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipPivot is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

// Set tool component pivot to <1,0,0>
cmds.manipPivot( p=(1, 0, 0) )

---


Flags:
---


---
bakeOri(bo): boolean
    properties: create, query
    Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.

---
moveToolOri(mto): int
    properties: create
    Change move tool's axis orientation to the specified mode. This flag is the same
as using "manipMoveContext -e -mode" on the Move tool except that this command
is undoable.

---
ori(o): [float, float, float]
    properties: create, query
    Component pivot orientation in world-space.

---
oriValid(ov): boolean
    properties: query
    Returns true if component pivot orientation is valid.

---
pinPivot(pin): boolean
    properties: create, query
    Pin component pivot. Selection changes will not reset the pivot position/orientation
when a custom pivot is set and pinning is on.

---
pos(p): [float, float, float]
    properties: create, query
    Component pivot position in world-space.

---
posValid(pv): boolean
    properties: query
    Returns true if component pivot position is valid.

---
reset(r): boolean
    properties: create
    Clear the saved component pivot position and orientation.

---
resetMode(rm) 2024.2: int
    properties: query
    Specifies the mode used when resetting the pivot position. Available modes are:

0: Center pivot (on bounding box)
1: Zero pivot (object-space origin)

---
resetOri(ro): boolean
    properties: create
    Clear the saved component pivot orientation.

---
resetPos(rp): boolean
    properties: create
    Clear the saved component pivot position.

---
rotateToolOri(rto): int
    properties: create
    Change rotate tool's axis orientation to the specified mode. This flag is the same
as using "manipRotateContext -e -mode" on the Rotate tool except that this command
is undoable.

---
scaleToolOri(sto): int
    properties: create
    Change scale tool's axis orientation to the specified mode. This flag is the same
as using "manipScaleContext -e -mode" on the Scale tool except that this command
is undoable.

---
snapOri(so): boolean
    properties: create, query
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

---
snapPos(sp): boolean
    properties: create, query
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

---
valid(v): boolean
    properties: query
    Returns true if component pivot position or orientation is valid.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipPivot.html 
    """


def manipRotateContext(flagactiveHandle: int, flagalignAlong: tuple[float, float, float], flagbakePivotOri: boolean, flagcenterTrackball: boolean, flagconstrainAlongNormal: boolean, flagcurrentActiveHandle: int, flageditPivotMode: boolean, flageditPivotPosition: boolean, flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglastMode: int, flagmanipVisible: boolean, flagmode: int, flagmodifyTranslation: boolean, flagorientAxes: tuple[float, float, float], flagorientObject: string, flagorientTowards: tuple[float, float, float], flagpinPivot: boolean, flagpivotOriHandle: boolean, flagposition: boolean, flagpostCommand: script, flagpostDragCommand: tuple[script, string], flagpreCommand: script, flagpreDragCommand: tuple[script, string], flagpreserveChildPosition: boolean, flagpreserveUV: boolean, flagreflection: boolean, flagreflectionAbout: int, flagreflectionAxis: int, flagreflectionTolerance: float, flagresetPivotMode: int, flagrotate: tuple[float, float, float], flagsnap: boolean, flagsnapPivotOri: boolean, flagsnapPivotPos: boolean, flagsnapRelative: boolean, flagsnapValue: float, flagtweakMode: boolean, flaguseCenterPivot: boolean, flaguseManipPivot: boolean, flaguseObjectPivot: boolean, flagxformConstraint: string) -> string:
    """Synopsis:
---
---
 manipRotateContext(
[object]
    , [activeHandle=int], [alignAlong=[float, float, float]], [bakePivotOri=boolean], [centerTrackball=boolean], [constrainAlongNormal=boolean], [currentActiveHandle=int], [editPivotMode=boolean], [editPivotPosition=boolean], [exists=boolean], [image1=string], [image2=string], [image3=string], [lastMode=int], [manipVisible=boolean], [mode=int], [modifyTranslation=boolean], [orientAxes=[float, float, float]], [orientObject=string], [orientTowards=[float, float, float]], [pinPivot=boolean], [pivotOriHandle=boolean], [position=boolean], [postCommand=script], [postDragCommand=[script, string]], [preCommand=script], [preDragCommand=[script, string]], [preserveChildPosition=boolean], [preserveUV=boolean], [reflection=boolean], [reflectionAbout=int], [reflectionAxis=int], [reflectionTolerance=float], [resetPivotMode=int], [rotate=[float, float, float]], [snap=boolean], [snapPivotOri=boolean], [snapPivotPos=boolean], [snapRelative=boolean], [snapValue=float], [tweakMode=boolean], [useCenterPivot=boolean], [useManipPivot=boolean], [useObjectPivot=boolean], [xformConstraint=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipRotateContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To create a new rotate context:
cmds.manipRotateContext()

To query the mode of an existing context:
cmds.manipRotateContext( 'manipRotateContext1', q=True, mode=True )

To edit an existing context to come up with the X axis
handle active by default:
cmds.manipRotateContext( 'manipRotateContext1', e=True, ah=0 )

---
Return:
---


    string: (name of the new context)

Flags:
---


---
activeHandle(ah): int
    properties: query, edit
    Sets the default active handle for the manip.  That is, the handle
which should be initially active when the tool is activated.
Values can be:

0 - X axis handle is active
1 - Y axis handle is active
2 - Z axis handle is active
3 - View rotation handle (outer ring) is active (default)

---
alignAlong(aa): [float, float, float]
    properties: create, edit
    Aligns active handle along vector.

---
bakePivotOri(bpo): boolean
    properties: query, edit
    Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.

---
centerTrackball(ctb): boolean
    properties: create, query, edit
    Specify if the center is to be handled like a trackball

---
constrainAlongNormal(xn): boolean
    properties: query, edit
    When true, transform constraints are applied along the vertex normal first
and only use the closest point when no intersection is found along the normal.

---
currentActiveHandle(cah): int
    properties: query, edit
    Sets the active handle for the manip.
Values can be:

0 - X axis handle is active
1 - Y axis handle is active
2 - Z axis handle is active
3 - View rotation handle (outer ring) is active
4 - Arc Ball is active

---
editPivotMode(epm): boolean
    properties: query
    Returns true manipulator is in edit pivot mode

---
editPivotPosition(epp): boolean
    properties: query
    Returns the current position of the edit pivot manipulator.

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
lastMode(lm): int
    properties: query
    Returns the previous rotation mode.

---
manipVisible(vis): boolean
    properties: query
    Returns true if the rotate manipulator is visible.

---
mode(m): int
    properties: query, edit
    Rotate mode:

0 - Object Space (default)
1 - World Space
2 - Gimbal Mode
3 - Custom Axis Orientation
10 - Component Space

---
modifyTranslation(mt): boolean
    properties: query, edit
    When false, and an object is rotated about a point other than its rotate pivot,
its rotateTranslate attribute is modified to put the object at the
correct position. When true, its translate attribute is used instead.
Default is false.

---
orientAxes(oa): [float, float, float]
    properties: query, edit
    Orients manipulator rotating around axes by specified angles

---
orientObject(oo): string
    properties: create, edit
    Orients manipulator to the passed in object/component

---
orientTowards(ot): [float, float, float]
    properties: create, edit
    Orients active handle towards world point

---
pinPivot(pin): boolean
    properties: query, edit
    Pin component pivot. When the component pivot is set and pinned selection
changes will not reset the pivot position and orientation.

---
pivotOriHandle(poh): boolean
    properties: query, edit
    When true, the pivot manipulator will show the orientation handle during editing.
Default is true.

---
position(p): boolean
    properties: query
    Returns the current position of the manipulator.

---
postCommand(psc): script
    properties: create, edit
    Specifies a command to be executed when the tool is exited.

---
postDragCommand(pod): [script, string]
    properties: create, edit
    Specifies a command and a node type. The command will be executed at
the end of a drag when a node of the specified type is in the selection.

---
preCommand(prc): script
    properties: create, edit
    Specifies a command to be executed when the tool is entered.

---
preDragCommand(prd): [script, string]
    properties: create, edit
    Specifies a command and a node type. The command will be executed at
the start of a drag when a node of the specified type is in the selection.

---
preserveChildPosition(pcp): boolean
    properties: query, edit
    When false, the children objects move when their parent is rotated.
When true, the worldspace position of the children will be maintained as
the parent is moved. Default is false.

---
preserveUV(puv): boolean
    properties: query, edit
    When false, the uvs are not changes to match the vertex edit.
When true, the uvs are edited to project to new values to stop texture
swimming as vertices are moved.

---
reflection(rfl): boolean
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionAbout(rab): int
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionAxis(rfa): int
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionTolerance(rft): float
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
resetPivotMode(rpm) 2024.2: int
    properties: query, edit
    Specifies the mode used when resetting the pivot position. Available modes are:

0: Center pivot (on bounding box)
1: Zero pivot (object-space origin)

---
rotate(ro): [float, float, float]
    properties: query, edit
    Returns the rotation of the manipulator for its current orientation/mode.

---
snap(s): boolean
    properties: create, query, edit
    Specify that the manipulation is to use absolute snap

---
snapPivotOri(spo): boolean
    properties: query, edit
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

---
snapPivotPos(spp): boolean
    properties: query, edit
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

---
snapRelative(sr): boolean
    properties: create, query, edit
    Specify that the manipulation is to use relative snap

---
snapValue(sv): float
    properties: create, query, edit
    Specify the snapping value

---
tweakMode(twk): boolean
    properties: query, edit
    When true, the manipulator is hidden and highlighted components can be selected
and rotated in one step using a click-drag interaction.

---
useCenterPivot(ucp): boolean
    properties: query, edit
    When true, use the center of the selection's bounding box as the center of the rotation
(for all objects).

---
useManipPivot(ump): boolean
    properties: query, edit
    When true, use the manipulator's center as the center of the rotation
(for all objects).

---
useObjectPivot(uop): boolean
    properties: query, edit
    When true, use each object's pivot as the center of its rotation.

---
xformConstraint(xc): string
    properties: query, edit
    none - no transform constraint
edge - edge transform constraint
surface - surface transform constraint

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipRotateContext.html 
    """


def manipRotateLimitsCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 manipRotateLimitsCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipRotateLimitsCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.manipRotateLimitsCtx()

---
Return:
---


    string: Name of newly created context

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipRotateLimitsCtx.html 
    """


def manipScaleContext(flagactiveHandle: int, flagalignAlong: tuple[float, float, float], flagbakePivotOri: boolean, flagconstrainAlongNormal: boolean, flagcurrentActiveHandle: int, flageditPivotMode: boolean, flageditPivotPosition: boolean, flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglastMode: int, flagmanipVisible: boolean, flagmode: int, flagorientAxes: tuple[float, float, float], flagorientObject: string, flagorientTowards: tuple[float, float, float], flagpinPivot: boolean, flagpivotOriHandle: boolean, flagposition: boolean, flagpostCommand: script, flagpostDragCommand: tuple[script, string], flagpreCommand: script, flagpreDragCommand: tuple[script, string], flagpreserveChildPosition: boolean, flagpreserveUV: boolean, flagpreventNegativeScale: boolean, flagreflection: boolean, flagreflectionAbout: int, flagreflectionAxis: int, flagreflectionTolerance: float, flagresetPivotMode: int, flagscale: tuple[float, float, float], flagsnap: boolean, flagsnapPivotOri: boolean, flagsnapPivotPos: boolean, flagsnapRelative: boolean, flagsnapValue: float, flagtweakMode: boolean, flaguseManipPivot: boolean, flaguseObjectPivot: boolean, flagxformConstraint: string) -> string:
    """Synopsis:
---
---
 manipScaleContext(
[object]
    , [activeHandle=int], [alignAlong=[float, float, float]], [bakePivotOri=boolean], [constrainAlongNormal=boolean], [currentActiveHandle=int], [editPivotMode=boolean], [editPivotPosition=boolean], [exists=boolean], [image1=string], [image2=string], [image3=string], [lastMode=int], [manipVisible=boolean], [mode=int], [orientAxes=[float, float, float]], [orientObject=string], [orientTowards=[float, float, float]], [pinPivot=boolean], [pivotOriHandle=boolean], [position=boolean], [postCommand=script], [postDragCommand=[script, string]], [preCommand=script], [preDragCommand=[script, string]], [preserveChildPosition=boolean], [preserveUV=boolean], [preventNegativeScale=boolean], [reflection=boolean], [reflectionAbout=int], [reflectionAxis=int], [reflectionTolerance=float], [resetPivotMode=int], [scale=[float, float, float]], [snap=boolean], [snapPivotOri=boolean], [snapPivotPos=boolean], [snapRelative=boolean], [snapValue=float], [tweakMode=boolean], [useManipPivot=boolean], [useObjectPivot=boolean], [xformConstraint=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipScaleContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To create a new scale context:
cmds.manipScaleContext()

To query the active handle of an existing scale context:
cmds.manipScaleContext( 'manipScaleContext1', q=True, ah=True )

To edit an exiting scale context so that it comes up with the X axis
handle active by default:
cmds.manipScaleContext( 'manipScaleContext1', e=True, ah=0 )

---
Return:
---


    string: (name of the new context)

Flags:
---


---
activeHandle(ah): int
    properties: query, edit
    Sets the default active handle for the manip.  That is, the handle
which should be initially active when the tool is activated.
Values can be:

0 - X axis handle is active
1 - Y axis handle is active
2 - Z axis handle is active
3 - Center handle (all axes) is active (default)

---
alignAlong(aa): [float, float, float]
    properties: create, edit
    Aligns active handle along vector.

---
bakePivotOri(bpo): boolean
    properties: query, edit
    Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.

---
constrainAlongNormal(xn): boolean
    properties: query, edit
    When true, transform constraints are applied along the vertex normal first
and only use the closest point when no intersection is found along the normal.

---
currentActiveHandle(cah): int
    properties: query, edit
    Sets the active handle for the manip.
Values can be:

0 - X axis handle is active
1 - Y axis handle is active
2 - Z axis handle is active
3 - Center handle (all axes) is active
4 - XY plane handle is active
5 - YZ plane handle is active
6 - XZ plane handle is active

---
editPivotMode(epm): boolean
    properties: query
    Returns true manipulator is in edit pivot mode

---
editPivotPosition(epp): boolean
    properties: query
    Returns the current position of the edit pivot manipulator.

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
lastMode(lm): int
    properties: query
    Returns the previous scaling mode.

---
manipVisible(vis): boolean
    properties: query
    Returns true if the scale manipulator is visible.

---
mode(m): int
    properties: query, edit
    Scale mode:

0 - Object Space
1 - Local Space
2 - World Space (default)
3 - Scale Along Vertex Normal
4 - Scale Along Rotation Axis
5 - Scale Along Live Object Axis
6 - Custom Axis Orientation
10 - Component Space

---
orientAxes(oa): [float, float, float]
    properties: query, edit
    Orients manipulator rotating around axes by specified angles

---
orientObject(oo): string
    properties: create, edit
    Orients manipulator to the passed in object/component

---
orientTowards(ot): [float, float, float]
    properties: create, edit
    Orients active handle towards world point

---
pinPivot(pin): boolean
    properties: query, edit
    Pin component pivot. When the component pivot is set and pinned selection
changes will not reset the pivot position and orientation.

---
pivotOriHandle(poh): boolean
    properties: query, edit
    When true, the pivot manipulator will show the orientation handle during editing.
Default is true.

---
position(p): boolean
    properties: query
    Returns the current position of the manipulator.

---
postCommand(psc): script
    properties: create, edit
    Specifies a command to be executed when the tool is exited.

---
postDragCommand(pod): [script, string]
    properties: create, edit
    Specifies a command and a node type. The command will be executed at
the end of a drag when a node of the specified type is in the selection.

---
preCommand(prc): script
    properties: create, edit
    Specifies a command to be executed when the tool is entered.

---
preDragCommand(prd): [script, string]
    properties: create, edit
    Specifies a command and a node type. The command will be executed at
the start of a drag when a node of the specified type is in the selection.

---
preserveChildPosition(pcp): boolean
    properties: query, edit
    When false, the children objects move when their parent is rotated.
When true, the worldspace position of the children will be maintained as
the parent is moved. Default is false.

---
preserveUV(puv): boolean
    properties: query, edit
    When false, the uvs are not changes to match the vertex edit.
When true, the uvs are edited to project to new values to stop texture
swimming as vertices are moved.

---
preventNegativeScale(pns): boolean
    properties: query
    When this is true, negative scale is not allowed.

---
reflection(rfl): boolean
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionAbout(rab): int
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionAxis(rfa): int
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
reflectionTolerance(rft): float
    properties: 
    This flag is obsolete. Reflection is now managed as part of selection itself
using the symmetricModeling command.

---
resetPivotMode(rpm) 2024.2: int
    properties: query, edit
    Specifies the mode used when resetting the pivot position. Available modes are:

0: Center pivot (on bounding box)
1: Zero pivot (object-space origin)

---
scale(sc): [float, float, float]
    properties: query, edit
    Returns the scale of the manipulator for its current orientation/mode.

---
snap(s): boolean
    properties: create, query, edit
    Specify that the manipulation is to use absolute snap

---
snapPivotOri(spo): boolean
    properties: query, edit
    Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.

---
snapPivotPos(spp): boolean
    properties: query, edit
    Snap pivot position. Modify pivot position when snapping the pivot to a component.

---
snapRelative(sr): boolean
    properties: create, query, edit
    Specify that the manipulation is to use relative snap

---
snapValue(sv): float
    properties: create, query, edit
    Specify the snapping value

---
tweakMode(twk): boolean
    properties: query, edit
    When true, the manipulator is hidden and highlighted components can be selected
and scaled in one step using a click-drag interaction.

---
useManipPivot(ump): boolean
    properties: create, query, edit
    Specify whether to pivot on the manip

---
useObjectPivot(uop): boolean
    properties: create, query, edit
    Specify whether to pivot on the object

---
xformConstraint(xc): string
    properties: query, edit
    none - no transform constraint
edge - edge transform constraint
surface - surface transform constraint

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipScaleContext.html 
    """


def manipScaleLimitsCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 manipScaleLimitsCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

manipScaleLimitsCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.manipScaleLimitsCtx()

---
Return:
---


    string: Name of newly created context.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/manipScaleLimitsCtx.html 
    """


def marker(flagattach: boolean, flagdetach: boolean, flagfrontTwist: angle, flagorientationMarker: boolean, flagpositionMarker: boolean, flagsideTwist: angle, flagtime: time, flagupTwist: angle, flagvalueU: float) -> list[string]:
    """Synopsis:
---
---
 marker(
[string]
    , [attach=boolean], [detach=boolean], [frontTwist=angle], [orientationMarker=boolean], [positionMarker=boolean], [sideTwist=angle], [time=time], [upTwist=angle], [valueU=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

marker is undoable, queryable, and editable.
One can specify "-pm -om" option to create both, a position marker
and an orientation marker.

Since there is only one keyframe for each marker of the same type,
no more than one marker of the same type with the same time value
can exist.

The default marker type is the position marker. The default time is
the current time.




Example:
---
import maya.cmds as cmds

Create a simple motion path animation:

create a path, e,g, a curve
path = cmds.curve(d=3,p=[(-10, 0, 0),(-6, 0, 10),(-3, 0, -10),(10, 0, 0)],k=[0, 0, 0, 1, 1, 1])

Create an object, e.g. a sphere
object = cmds.sphere()
cmds.scale( 0.5, 2.0, 0.2 )

animate the object using a motion path with follow on
cmds.pathAnimation( object[0], f=1, stu=0, etu=30, c=path )

change the current time to be frame 20
cmds.currentTime( 20, edit=True )

Create a position marker on the path, at curve parameter value
0.75 and at current time:
cmds.marker( path, u=0.75 )

Create an orientation marker on the path, at time 15:
cmds.marker( path, om=True, t=15 )

Create a position marker and an orientation marker on the path,
at curve parameter value .35 and at time 10:
cmds.marker( path, pm=True, om=True, t=10, u=0.35 )

---
Return:
---


    list[string]: (name of the created markers)

Flags:
---


---
attach(a): boolean
    properties: create
    This flag specifies to attach the selected 3D position markers
to their parent geometry.

---
detach(d): boolean
    properties: create
    This flag specifies to detach the selected position markers from
their parent geometry to the 3D space.

---
frontTwist(ft): angle
    properties: query
    This flag specifies the amount of twist angle about
the front vector for the marker.
Default is 0.
When queried, this flag returns a angle.

---
orientationMarker(om): boolean
    properties: query
    This flag specifies creation of an orientation marker.
Default is not set..
When queried, this flag returns a boolean.

---
positionMarker(pm): boolean
    properties: query
    This flag specifies creation of a position marker.
Default is set.
When queried, this flag returns a boolean.

---
sideTwist(st): angle
    properties: query
    This flag specifies  the amount of twist angle about
the side vector for the marker.
Default is 0.
When queried, this flag returns a angle.

---
time(t): time
    properties: query
    This flag specifies the time for the marker.
Default is the current time.
When queried, this flag returns a time.

---
upTwist(ut): angle
    properties: query
    This flag specifies the amount of twist angle about
the up vector for the marker.
Default is 0.
When queried, this flag returns a angle.

---
valueU(u): float
    properties: query
    This flag specifies the location of the position marker
w.r.t. the parent geometry u parameterization.
Default is the value at current time.
When queried, this flag returns a linear.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/marker.html 
    """


def matchTransform(flagpivots: boolean, flagposition: boolean, flagpositionX: boolean, flagpositionY: boolean, flagpositionZ: boolean, flagrotatePivot: boolean, flagrotation: boolean, flagrotationX: boolean, flagrotationY: boolean, flagrotationZ: boolean, flagscale: boolean, flagscaleBox: boolean, flagscalePivot: boolean, flagscaleX: boolean, flagscaleY: boolean, flagscaleZ: boolean) -> None:
    """Synopsis:
---
---
 matchTransform(
[objects...]
    , [pivots=boolean], [position=boolean], [positionX=boolean], [positionY=boolean], [positionZ=boolean], [rotatePivot=boolean], [rotation=boolean], [rotationX=boolean], [rotationY=boolean], [rotationZ=boolean], [scale=boolean], [scaleBox=boolean], [scalePivot=boolean], [scaleX=boolean], [scaleY=boolean], [scaleZ=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

matchTransform is undoable, NOT queryable, and NOT editable.
If no flags are specified then the command will match position,
rotation and scaling.




Example:
---
import maya.cmds as cmds

create a cone and randomly transform it
cmds.polyCone(n='cone1')
cmds.scale(0.2, 2.0, 0.2);
cmds.rotate(20, 45, 70)
cmds.move(-2, 0, 2)

create a cylinder
cmds.polyCylinder(n='cylinder1')

modify the cylinder's transform to match the cone
cmds.matchTransform('cylinder1','cone1')

---


Flags:
---


---
pivots(piv): boolean
    properties: create
    Match the source object(s) scale/rotate pivot positions to the target transform's pivot.

---
position(pos): boolean
    properties: create
    Match the source object(s) position to the target object.

---
positionX(px): boolean
    properties: create
    Match the source object(s) X position to the target object.

---
positionY(py): boolean
    properties: create
    Match the source object(s) Y position to the target object.

---
positionZ(pz): boolean
    properties: create
    Match the source object(s) Z position to the target object.

---
rotatePivot(rp): boolean
    properties: create
    Match the source object(s) rotate pivot position to the target transform's pivot.

---
rotation(rot): boolean
    properties: create
    Match the source object(s) rotation to the target object.

---
rotationX(rx): boolean
    properties: create
    Match the source object(s) X rotation to the target object.

---
rotationY(ry): boolean
    properties: create
    Match the source object(s) Y rotation to the target object.

---
rotationZ(rz): boolean
    properties: create
    Match the source object(s) Z rotation to the target object.

---
scale(scl): boolean
    properties: create
    Match the source object(s) scale to the target transform.

---
scaleBox(box): boolean
    properties: create
    Use the source/target object's child bounding box size when matching scaling.

---
scalePivot(sp): boolean
    properties: create
    Match the source object(s) scale pivot position to the target transform's pivot.

---
scaleX(sx): boolean
    properties: create
    Match the source object(s) X scale to the target object.

---
scaleY(sy): boolean
    properties: create
    Match the source object(s) Y scale to the target object.

---
scaleZ(sz): boolean
    properties: create
    Match the source object(s) Z scale to the target object.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/matchTransform.html 
    """


def matrixUtil(flaginverse: boolean, flagquaternion: tuple[float, float, float, float], flagrelative: boolean, flagrotation: tuple[float, float, float], flagscale: tuple[float, float, float], flagshear: tuple[float, float, float], flagtranslation: tuple[float, float, float], flagtranspose: boolean) -> string:
    """Synopsis:
---
---
 matrixUtil([inverse=boolean], [quaternion=[float, float, float, float]], [relative=boolean], [rotation=[float, float, float]], [scale=[float, float, float]], [shear=[float, float, float]], [translation=[float, float, float]], [transpose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

matrixUtil is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

---
compose a matrix from translation, rotation, scale and shear
cmds.matrixUtil(t=[10, 20, 30], r=[90, 0, 90], s=[2, 3, 4], sh=[1, 0, 0])
---
query translation
cmds.matrixUtil([1, 0, 0, 0,  0, 1, 0, 0,  0, 0, 1, 0,  0, 0, 0, 1], q=True, t=True)
---
query rotation
cmds.matrixUtil([1, 0, 0, 0,  0, 1, 0, 0,  0, 0, 1, 0,  0, 0, 0, 1], q=True, r=True)
---
query scale
cmds.matrixUtil([1, 0, 0, 0,  0, 1, 0, 0,  0, 0, 1, 0,  0, 0, 0, 1], q=True, s=True)
---
edit translation
cmds.matrixUtil([2, 0, 0, 0,  0, 2, 0, 0,  0, 0, 2, 0,  0, 0, 0, 1], e=True, t=[3,4,5])

---
Return:
---


    string: Command result

Flags:
---


---
inverse(iv): boolean
    properties: create, query, edit
    Compose or query will return the inversed matrix.

---
quaternion(qt): [float, float, float, float]
    properties: create, query, edit
    Compose, edit or query a matrix using specified quaternion values as rotation components.

---
relative(rt): boolean
    properties: create, query, edit
    Add translation, rotation, scale or shear, instead of seting it as absolute.

---
rotation(r): [float, float, float]
    properties: create, query, edit
    Compose, edit or query a matrix using specified values as rotation components.

---
scale(s): [float, float, float]
    properties: create, query, edit
    Compose, edit or query a matrix using specified values as scale components.

---
shear(sh): [float, float, float]
    properties: create, query, edit
    Compose, edit or query a matrix using specified values as shear components.

---
translation(t): [float, float, float]
    properties: create, query, edit
    Compose a matrix using specified values as translation components.

---
transpose(tp): boolean
    properties: create, query, edit
    Compose or query will return the transposed matrix.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/matrixUtil.html 
    """


def mayaDpiSetting(flagmode: uint, flagrealScaleValue: boolean, flagscaleValue: float, flagsystemDpi: boolean) -> float | int:
    """Synopsis:
---
---
 mayaDpiSetting([mode=uint], [realScaleValue=boolean], [scaleValue=float], [systemDpi=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

mayaDpiSetting is NOT undoable, queryable, and NOT editable.
Provide Maya interface scaling based on system DPI or custom scale setting or no scaling. Please note that the change will only take effect after relaunching Maya.


The mayaDpiSetting command is not available on macOS. System scaling should be used to change Maya UI scaling.




Example:
---
import maya.cmds as cmds


Set the scale mode to system dpi based scaling.
cmds.mayaDpiSetting( mode=0 )

Set the interface scaling to 150% custom scaling.
cmds.mayaDpiSetting( mode=1, scaleValue=1.5 )

Disable the interface scaling.
cmds.mayaDpiSetting( mode=2 )

Query the current scaling mode.
cmds.mayaDpiSetting( query=True, mode=True )

Query the current scale value.
cmds.mayaDpiSetting( query=True, scaleValue=True )

Query the system dpi value.
cmds.mayaDpiSetting( query=True, systemDpi=True )

Query the current real scale value.
cmds.mayaDpiSetting( query=True, realScaleValue=True )

---
Return:
---


    int: Scale mode or system DPI value, as queried
    float: Defined scale or real scale, as queried

Flags:
---


---
mode(m): uint
    properties: create, query
    Specifies the interface scaling mode:

0 - System Dpi Based Scaling
1 - Custom Scaling (Must provide the custom scale value with flag "-scaleValue")
2 - No Scaling

---
realScaleValue(rsv): boolean
    properties: query
    This is a query mode only flag which returns the real scale value depending on current scaling mode and defined scale value:

mode 0 - Return the current real scale value which is the ratio of current system dpi to default system dpi
mode 1 - Return the current real scale value which is the product of the defined scale value and the ratio of current system dpi to default system dpi
mode 2 - Always return 1.0 which indicates real scale is 100% when the scaling mode is no scaling.

---
scaleValue(sv): float
    properties: create, query
    Specifies the custom scale of the interface if scaling mode is 1. The allowed values are [1.0, 1.25, 1.5, 2.0].
In query mode, return the scale value depend on current scaling mode:

mode 0 - Always return 1.0 which indicates 100% scaling
mode 1 - Return the custom scale value used
mode 2 - Always return 1.0 which indicates no custom scaling

---
systemDpi(sd): boolean
    properties: query
    This is a query mode only flag which returns the current system dpi value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/mayaDpiSetting.html 
    """


def mayaHasRenderSetup(flagenableCurrentSession: boolean, flagenableDuringTests: boolean) -> None:
    """Synopsis:
---
---
 mayaHasRenderSetup([enableCurrentSession=boolean], [enableDuringTests=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

mayaHasRenderSetup is NOT undoable, queryable, and editable.
This command controls and queries render setup states.




Example:
---
import maya.cmds as cmds


---
Returns whether render setup mode is enabled or disabled
cmds.mayaHasRenderSetup()

---
Query the state renderSetupEnableDuringTests
cmds.mayaHasRenderSetup(query = True, enableCurrentSession = True)

---
Query the state renderSetupEnableDuringTests
cmds.mayaHasRenderSetup(query = True, enableDuringTests = True)

---
Enable renderSetupEnableCurrentSession
cmds.mayaHasRenderSetup(edit = True, enableCurrentSession = True)

---
Disable renderSetupEnableCurrentSession
cmds.mayaHasRenderSetup(edit = True, enableCurrentSession = False)

---
Enable enableDuringTests
cmds.mayaHasRenderSetup(edit = True, enableDuringTests = True)

---
Disable enableDuringTests
cmds.mayaHasRenderSetup(edit = True, enableDuringTests = False)

---


Flags:
---


---
enableCurrentSession(ecs): boolean
    properties: query, edit
    Enables or disables render setup for this Maya session only.
This flag should only be called during Maya intialization. This flag is for internal use only, may change at any time and is unsupported.

---
enableDuringTests(edt): boolean
    properties: query, edit
    Switches render setup for this Maya session only, as legacy render layer mode is assumed during testing.
This flag is for internal use only, may change at any time and is unsupported.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/mayaHasRenderSetup.html 
    """


def melInfo() -> list[string]:
    """Synopsis:
---
---
 melInfo()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

melInfo is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Query the names of all the global MEL procedures currently defined.
---

procs = cmds.melInfo()

---
Return:
---


    list[string]: procedure names

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/melInfo.html 
    """


def melOptions(flagduplicateVariableWarnings: boolean) -> None:
    """Synopsis:
---
---
 melOptions([duplicateVariableWarnings=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

melOptions is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

---
        To find out if there are any duplicate variable declarations in
---
        a script:

---
        Save the current setting of the duplicateVariableWarnings option.
optionVal = cmds.melOptions(q=True, duplicateVariableWarnings=True)

---
        Turn the option on.
cmds.melOptions(duplicateVariableWarnings=True)

---
        Source the script and see all the warnings generated.
import maya.mel as mm
mm.eval('source "myScript.mel"')

// Warning: 	int $i; //
// Warning: "myScript.mel" line 5.8 : Redeclaration of variable "$i" shadows previous declaration at line 3. Previous value will be retained. //

---
        Restore the option to its original value.
cmds.melOptions(duplicateVariableWarnings=optionVal)

---


Flags:
---


---
duplicateVariableWarnings(dvw): boolean
    properties: create, query
    When turned on, this option will cause a warning to be generated whenever a
MEL variable is declared within the same scope as another variable with
the same name.
The warnings will be generated when the script is sourced, not when it
is executed. Usually these warnings indicate an error in the script.

On query the current setting of the option will be returned.

The corresponding preference optionVar is melDuplicateVariableWarnings.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/melOptions.html 
    """


def memory(flagadjustedVirtualMemory: boolean, flagasFloat: boolean, flagdebug: boolean, flagfreeMemory: boolean, flaggigaByte: boolean, flagheapMemory: boolean, flagkiloByte: boolean, flagmegaByte: boolean, flagpageFaults: boolean, flagpageReclaims: boolean, flagphysicalMemory: boolean, flagprocessVirtualMemory: boolean, flagsummary: boolean, flagswapFree: boolean, flagswapLogical: boolean, flagswapMax: boolean, flagswapPhysical: boolean, flagswapReserved: boolean, flagswapVirtual: boolean, flagswaps: boolean) -> None:
    """Synopsis:
---
---
 memory([adjustedVirtualMemory=boolean], [asFloat=boolean], [debug=boolean], [freeMemory=boolean], [gigaByte=boolean], [heapMemory=boolean], [kiloByte=boolean], [megaByte=boolean], [pageFaults=boolean], [pageReclaims=boolean], [physicalMemory=boolean], [processVirtualMemory=boolean], [summary=boolean], [swapFree=boolean], [swapLogical=boolean], [swapMax=boolean], [swapPhysical=boolean], [swapReserved=boolean], [swapVirtual=boolean], [swaps=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

memory is undoable, NOT queryable, and NOT editable.
By default memory sizes are returned in bytes. Since Maya's command engine
only supports 32-bit signed integers, any returned value which cannot fit
into 31 bits will be truncated to 2,147,483,647 and a warning message displayed.
To avoid having memory sizes truncated use one of the memory size flags to
return the value in larger units (e.g. megabytes) or use the asFloat flag to
return the value as a float.




Example:
---
import maya.cmds as cmds

cmds.memory(freeMemory=True)
Result: 525451264 ---


cmds.memory(freeMemory=True megaByte=True)
Result: 521 ---


cmds.memory(freeMemory=True megaByte=True asFloat=True)
Result: 521.33203125 ---


---


Flags:
---


---
adjustedVirtualMemory(av): boolean
    properties: create
    Returns size of adjusted virtual memory allocated by the process.
The adjustment is done by computing an offset when the application is launched
that will be subtracted from the process virtual memory in order to give the
adjusted value.  The returned size is an approximation of the memory used by the
process that can be more reliable in some cases, for instance on platforms where
display drivers can reserve large ranges of memory addresses, therefore increasing
the size of the process virtual memory, even though those addresses are actually
not used.

---
asFloat(af): boolean
    properties: create
    Causes numeric values to be returned as floats rather than ints. This can
be useful if you wish to retain some of the significant digits lost when
using the unit size flags.

---
debug(dbg): boolean
    properties: create
    Print debugging statistics on arena memory (if it exists)

---
freeMemory(fr): boolean
    properties: create
    Returns size of free memory

---
gigaByte(gb): boolean
    properties: create
    Return memory sizes in gigabytes (1024*1024*1024 bytes)

---
heapMemory(he): boolean
    properties: create
    Returns size of memory heap

---
kiloByte(kb): boolean
    properties: create
    Return memory sizes in kilobytes (1024 bytes)

---
megaByte(mb): boolean
    properties: create
    Return memory sizes in megabytes (1024*1024 bytes)

---
pageFaults(pf): boolean
    properties: create
    Returns number of page faults

---
pageReclaims(pr): boolean
    properties: create
    Returns number of page reclaims

---
physicalMemory(phy): boolean
    properties: create
    Returns size of physical memory

---
processVirtualMemory(pv): boolean
    properties: create
    Returns size of virtual memory allocated by the process

---
summary(sum): boolean
    properties: create
    Returns a summary of memory usage. The size flags are ignored and all
memory sizes are given in megabytes.

---
swapFree(swf): boolean
    properties: create
    Returns size of free swap

---
swapLogical(swl): boolean
    properties: create
    Returns size of logical swap

---
swapMax(swm): boolean
    properties: create
    Returns maximum swap size

---
swapPhysical(swp): boolean
    properties: create
    Returns size of physical swap

---
swapReserved(swr): boolean
    properties: create
    Returns size of reserved swap

---
swapVirtual(swv): boolean
    properties: create
    Returns size of virtual swap

---
swaps(sw): boolean
    properties: create
    Returns number of swaps

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/memory.html 
    """


def menu(flagallowOptionBoxes: boolean, flagdefineTemplate: string, flagdeleteAllItems: boolean, flagdocTag: string, flagenable: boolean, flagexists: boolean, flagfamilyImage: string, flaghelpMenu: boolean, flagitemArray: boolean, flaglabel: string, flagmnemonic: string, flagnumberOfItems: boolean, flagparent: string, flagpostMenuCommand: script, flagpostMenuCommandOnce: boolean, flagscrollable: boolean, flagtearOff: boolean, flaguseTemplate: string, flagversion: string, flagvisible: boolean) -> string:
    """Synopsis:
---
---
 menu(
[string]
    , [allowOptionBoxes=boolean], [defineTemplate=string], [deleteAllItems=boolean], [docTag=string], [enable=boolean], [exists=boolean], [familyImage=string], [helpMenu=boolean], [itemArray=boolean], [label=string], [mnemonic=string], [numberOfItems=boolean], [parent=string], [postMenuCommand=script], [postMenuCommandOnce=boolean], [scrollable=boolean], [tearOff=boolean], [useTemplate=string], [version=string], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

menu is undoable, queryable, and editable.menuItem -sm/subMenu true



Example:
---
import maya.cmds as cmds

cmds.window( menuBar=True, width=200 )
cmds.menu( label='File', tearOff=True )
cmds.menuItem( label='New' )
cmds.menuItem( label='Open' )
cmds.menuItem( label='Save' )
cmds.menuItem( divider=True )
cmds.menuItem( label='Quit' )
cmds.menu( label='Help', helpMenu=True )
cmds.menuItem( 'Application..."', label='"About' )
cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow()

---
Return:
---


    string: Full path name to the menu.

Flags:
---


---
allowOptionBoxes(aob): boolean
    properties: create, query
    Deprecated. All menus now always allow option boxes.
Indicate whether the menu will be able to support option box
menu items.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deleteAllItems(dai): boolean
    properties: create, edit
    Delete all the items in this menu.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the menu.

---
enable(en): boolean
    properties: create, query, edit
    Enables/disables the menu.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
familyImage(fi): string
    properties: create, query, edit
    The filename of the icon associated with the menu. This
icon will be used if a menu item does not have an icon image
defined.

---
helpMenu(hm): boolean
    properties: create, query, edit
    Indicates that this menu is the help menu and will be the
right most menu in the menu bar. On Unix systems the help menu
is also right justified in the menu bar.

---
itemArray(ia): boolean
    properties: query
    Return string array of the menu item names.

---
label(l): string
    properties: create, query, edit
    The text that is displayed for the menu.  If no label is
supplied then the menuName will be used.

---
mnemonic(mn): string
    properties: create, query, edit
    Set the Alt key to post that menu.  The character
specified must match the case of its corresponding character in
the menu item text, but selection from the keyboard is case
insensitive.

---
numberOfItems(ni): boolean
    properties: query
    Return number of items in the menu.

---
parent(p): string
    properties: create
    Specify the window that the menu will appear in.

---
postMenuCommand(pmc): script
    properties: create, edit
    Specify a script to be executed when the menu is about to be
shown.

---
postMenuCommandOnce(pmo): boolean
    properties: create, query, edit
    Indicate the -pmc/postMenuCommand should only be
invoked once.  Default value is false, ie.
the -pmc/postMenuCommand is invoked every time the menu is
shown.

---
scrollable(srb): boolean
    properties: create, query, edit
    Make the popup menus support scrolling. Default value is false.

---
tearOff(to): boolean
    properties: create
    Makes the menu tear-off-able.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
version(ver): string
    properties: create, query, edit
    Specify the version that this menu feature was introduced.
The argument should be given as a string of the version number
(e.g. "2014", "2015"). Currently only accepts major version
numbers (e.g. 2014.5 should be given as "2014").

---
visible(vis): boolean
    properties: create, query, edit
    Shows/hides the menu.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/menu.html 
    """


def menuBarLayout(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchildArray: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagmenuArray: boolean, flagmenuBarVisible: boolean, flagmenuIndex: tuple[string, uint], flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfMenus: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 menuBarLayout(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [childArray=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [margins=int], [menuArray=boolean], [menuBarVisible=boolean], [menuIndex=[string, uint]], [noBackground=boolean], [numberOfChildren=boolean], [numberOfMenus=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

menuBarLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a window with two menu bar layouts.
---

window = cmds.window()
cmds.columnLayout( adjustableColumn=True )

   Create first menu bar layout.
---

menuBarLayout = cmds.menuBarLayout()
cmds.menu( label='File' )
cmds.menuItem( label='New' )
cmds.menuItem( label='Open' )
cmds.menuItem( label='Close' )

cmds.menu( label='Help', helpMenu=True )
cmds.menuItem( label='About...' )

cmds.columnLayout()
cmds.button( label='Add Menu', command=('cmds.menu(parent=\"' + menuBarLayout + '\"); cmds.menuItem()') )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.separator( height=10, style='none' )

   Create a second menu bar layout.
---

cmds.menuBarLayout()
cmds.menu( label='Edit' )
cmds.menuItem( label='Cut' )
cmds.menuItem( label='Copy' )
cmds.menuItem( label='Paste' )

cmds.menu( label='View' )
cmds.menuItem( label='Fonts...' )
cmds.menuItem( label='Colors...' )

cmds.columnLayout()
cmds.text( label='Add some controls here.' )
cmds.setParent( '..' )
cmds.setParent( '..' )

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
menuArray(ma): boolean
    properties: query
    Return a string array containing the names of the menus in
the layout's menu bar.

---
menuBarVisible(mbv): boolean
    properties: create, query, edit
    Visibility of the menu bar.

---
menuIndex(mi): [string, uint]
    properties: edit
    Sets the index of a specified menu.

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
numberOfMenus(nm): boolean
    properties: query
    Return the number of menus attached to the layout's menu bar.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/menuBarLayout.html 
    """


def menuEditor(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcellHeight: int, flagcellWidth: int, flagcellWidthHeight: tuple[int, int], flagcheckBoxPresent: tuple[boolean, string, int], flagcheckBoxState: tuple[boolean, string, int], flagcommand: tuple[string, string, int], flagdefineTemplate: string, flagdelete: tuple[string, int], flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagiconMenuCallback: string, flagimage: tuple[string, string, int], flagisObscured: boolean, flaglabel: tuple[string, string, int], flagmanage: boolean, flagmenuItemTypes: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagoptionBoxCommand: tuple[string, string, int], flagoptionBoxPresent: tuple[boolean, string, int], flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagradioButtonPresent: tuple[boolean, string, int], flagradioButtonState: tuple[boolean, string, int], flagseparator: tuple[string, int], flagstatusBarMessage: string, flagstyle: string, flagsubMenuAt: tuple[string, int], flagsubMenuEditorWindow: string, flagsubMenuEditorsOpen: boolean, flagsubMenuOf: tuple[string, string, int], flagtopLevelMenu: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 menuEditor(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [cellHeight=int], [cellWidth=int], [cellWidthHeight=[int, int]], [checkBoxPresent=[boolean, string, int]], [checkBoxState=[boolean, string, int]], [command=[string, string, int]], [defineTemplate=string], [delete=[string, int]], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [iconMenuCallback=string], [image=[string, string, int]], [isObscured=boolean], [label=[string, string, int]], [manage=boolean], [menuItemTypes=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [optionBoxCommand=[string, string, int]], [optionBoxPresent=[boolean, string, int]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [radioButtonPresent=[boolean, string, int]], [radioButtonState=[boolean, string, int]], [separator=[string, int]], [statusBarMessage=string], [style=string], [subMenuAt=[string, int]], [subMenuEditorWindow=string], [subMenuEditorsOpen=boolean], [subMenuOf=[string, string, int]], [topLevelMenu=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

menuEditor is undoable, queryable, and editable.
When editing a Marking Menu, the radial menu items correspond to 8
icons arranged in a circle within the menuEditor.  Overflow items in
the Marking Menu (or linear items in a normal menu) are displayed in
a column below the radial items.

To edit a submenu of a popup menu, a new menuEditor instance must be
created (typically within its own window) and attached to its parent
menuEditor.

Some flags require the position of a menu item to be passed in as an
argument.  For these, positions are specified with a (string,int)
pair, where the string corresponds to a radial position
(possibily "None") and the int corresponds to a linear position
(possibly equal to 0 for none).  Radial positions are specified by
one of ("N",0), ("NE",0), ("E",0), ("SE",0), ("S",0), ("SW",0),
("W",0) or ("NW",0).  Overflow, or linear positions, are specified
with ("None",i), where i is a 1-based index giving the position of
the item within the overflow column.

Note: This command is not meant to be called explicitly. It was
created to support the Marking Menu editor. It is recommended that you
use that editor to modify marking menus.




Example:
---
import maya.cmds as cmds

No example is provided as <b>menuEditor</b> is not intended to be called
independently. It is recommended that you use the Marking Menu editor
to customize marking menus.

---
Return:
---


    string: Full path name to the editor.

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
cellHeight(ch): int
    properties: query, edit
    The height of the icons in the menuEditor.

---
cellWidth(cw): int
    properties: query, edit
    The width of the icons in the menuEditor.

---
cellWidthHeight(cwh): [int, int]
    properties: edit
    The width and height of the icons in the menuEditor.

---
checkBoxPresent(cbp): [boolean, string, int]
    properties: query, edit
    This controls whether a menu item has a check box or not.
The arguments are a flag indicating presence, followed by the position of the menu item.
This flag is ignored if the menu item is a submenu item.
If queried, an array of booleans is returned containing all the flags.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
checkBoxState(cbs): [boolean, string, int]
    properties: query, edit
    The state of the check box associated with a menu item.
The arguments are a flag indicating state, followed by the position of the menu item.
This flag is ignored if the menu item does not have a check box.
If queried, an array of booleans is returned containing all the flags.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
command(c): [string, string, int]
    properties: query, edit
    The command or script executed by a menu item.
The arguments are the command string or script name, followed by the
position of the menu item. This flag is ignored if the menu item is
a submenu item or a separator item.
If queried, an array of strings is returned containing all the commands.
The first 8 entries of the array correspond to radial items (in
order, "N", "NE", ... "NW"), and all later entries correspond to
overflow (or linear) menu items.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
delete(d): [string, int]
    properties: edit
    Deletes the menu item at the given position, removing it from
the menu.  If the menu item has a submenu, and a sub-menuEditor is
open and attached to it, then the sub-menuEditor's window and
all its child menuEditor windows will be closed recursively.

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
iconMenuCallback(imc): string
    properties: create
    This is the name of a MEL callback procedure that is called to
create the popup menus attached to icons in the menuEditor.  The
callback is called once for each newly created icon, and once each
time an icon is moved within the menuEditor.  Popup menus created
by the callback should contain commands for editing the menu item
associated with the icon.  Operations accessible through the menu
should include deletion of the item, editing of the
item's label/command/image/checkbox/optionbox, creation of a submenu,
and popping up a sub-menuEditor.

The arguments to the callback must match this form:

callbackProc(string $menuEditorName, string $parentIconName, string $menuTitle, string $radialPosition, int $overflowRow);

The popup menu's parent should be $parentIconName.

Note that when a sub-menuEditor is created, this flag need not be
re-specified as it adopts a default value equal to the value of
its parent menuEditor's -imc/iconMenuCallback flag.

---
image(i): [string, string, int]
    properties: query, edit
    The filename of the icon associated with a menu item.
This icon is displayed by the menuEditor to represent the menu item.
The arguments are the icon filename, followed by the position of the menu item.
If queried, an array of strings is returned containing all the icon filenames.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
label(l): [string, string, int]
    properties: query, edit
    The label of a menu item.
The arguments are the label text, followed by the position of the
menu item. If queried, an array of strings is returned containing
all the labels. The first 8 entries of the array correspond to radial
items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
menuItemTypes(mit): boolean
    properties: query
    This is a query only flag.  Returns an array of strings indicating the type of contents in
each cell of the menuEditor.  Cells can be "vacant", or may contain a regular menu "item",
or a "separator", or a "submenu" item.  In each case, the corresponding string is returned.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

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
optionBoxCommand(obc): [string, string, int]
    properties: query, edit
    The command or script executed by a menu item's associated option box item.
The arguments are the command string or script name, followed by the position of the menu item.
This flag is ignored if the menu item does not have an associated option box item.
If queried, an array of strings is returned containing all the commands.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
optionBoxPresent(obp): [boolean, string, int]
    properties: query, edit
    This controls whether a menu item has an associated option box item or not.
The arguments are a flag indicating presence, followed by the position of the menu item.
This flag is ignored if the menu item is a submenu item.
If queried, an array of booleans is returned containing all the flags.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

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
radioButtonPresent(rbp): [boolean, string, int]
    properties: query, edit
    This controls whether a menu item has a radio button or not.
The arguments are a flag indicating presence, followed by the position of the menu item.
This flag is ignored if the menu item is a submenu item.
If queried, an array of booleans is returned containing all the flags.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
radioButtonState(rbs): [boolean, string, int]
    properties: query, edit
    The state of the radio button associated with a menu item.
The arguments are a flag indicating state, followed by the position of the menu item.
This flag is ignored if the menu item does not have a radio button.
If queried, an array of booleans is returned containing all the flags.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
separator(sp): [string, int]
    properties: query, edit
    In edit mode this adds a separator to the menuEditor at the
specified position. The parameters are the radialPosition and the
overflowRow. If queried, an array of booleans is returned indicating
if the item is a separator item. The first 8 entries of the array
correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
style(st): string
    properties: query, edit
    This is the style of icons within the menuEditor. Valid styles
are "iconOnly", "textOnly", "iconAndTextHorizontal"
and "iconAndTextVertical".

---
subMenuAt(sma): [string, int]
    properties: edit
    Creates a submenu item at the given position.  A submenu item
created within the radial portion of a menu will overwrite whatever
item (if any) is currently at the given position. A submenu item
created within the overflow (linear) portion of a menu will be
inserted before
the item currently at the given position.

---
subMenuEditorWindow(sew): string
    properties: create
    The name of the window which contains a sub-menuEditor.  Only use
when creatitg a sub-menuEditor. This window will automatically be
closed if a parent menuEditor is closed or if a parent menu item
is deleted.

---
subMenuEditorsOpen(seo): boolean
    properties: query
    This is a query only flag.  Returns an array of booleans, each of which indicates if a
sub-menuEditor is open and attached to the menu item in a particular cell.  One boolean
is returned for each cell in the menuEditor, even if the cell is vacant or contains
a non-submenu item (false will be returned in both these cases).  Only when a cell contains
a submenu item can true possibily be returned.
The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),
and all later entries correspond to overflow (or linear) menu items.

---
subMenuOf(smo): [string, string, int]
    properties: create
    Attaches a sub-menuEditor to its parent menuEditor.  Only use when
creatitg a sub-menuEditor. The arguments are the name
of the parent menuEditor, followed by the position of a submenu item
within the parent. A submenu item must already exist within the parent
at the given position. A submenu item cannot have multiple
sub-menuEditors attached to it.

---
topLevelMenu(tlm): string
    properties: query, edit
    The popup menu to attach to the editor.  All editing operations
performed in the editor (i.e. inserting/deleting/moving an item) will
be immediately reflected in this menu. This flag is ignored if the
editor is a sub-menuEditor.  The editor will update gracefully if the
value of the flag is changed from its initial value.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/menuEditor.html 
    """


def menuItem(flagallowOptionBoxes: boolean, flagannotation: string, flagboldFont: boolean, flagcheckBox: boolean, flagcollection: string, flagcommand: script, flagdata: int, flagdefineTemplate: string, flagdivider: boolean, flagdividerLabel: string, flagdocTag: string, flagdragDoubleClickCommand: script, flagdragMenuCommand: script, flagechoCommand: boolean, flagenable: boolean, flagenableCommandRepeat: boolean, flagexists: boolean, flagfamilyImage: string, flagimage: string, flagimageOverlayLabel: string, flaginsertAfter: string, flagisCheckBox: boolean, flagisOptionBox: boolean, flagisRadioButton: boolean, flagitalicized: boolean, flaglabel: string, flaglongDivider: boolean, flagoptionBox: boolean, flagoptionBoxIcon: string, flagparent: string, flagpostMenuCommand: script, flagpostMenuCommandOnce: boolean, flagradialPosition: string, flagradioButton: boolean, flagrunTimeCommand: string, flagsourceType: string, flagsubMenu: boolean, flagtearOff: boolean, flaguseTemplate: string, flagversion: string, flagvisible: boolean) -> string:
    """Synopsis:
---
---
 menuItem(
[string]
    , [allowOptionBoxes=boolean], [annotation=string], [boldFont=boolean], [checkBox=boolean], [collection=string], [command=script], [data=int], [defineTemplate=string], [divider=boolean], [dividerLabel=string], [docTag=string], [dragDoubleClickCommand=script], [dragMenuCommand=script], [echoCommand=boolean], [enable=boolean], [enableCommandRepeat=boolean], [exists=boolean], [familyImage=string], [image=string], [imageOverlayLabel=string], [insertAfter=string], [isCheckBox=boolean], [isOptionBox=boolean], [isRadioButton=boolean], [italicized=boolean], [label=string], [longDivider=boolean], [optionBox=boolean], [optionBoxIcon=string], [parent=string], [postMenuCommand=script], [postMenuCommandOnce=boolean], [radialPosition=string], [radioButton=boolean], [runTimeCommand=string], [sourceType=string], [subMenu=boolean], [tearOff=boolean], [useTemplate=string], [version=string], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

menuItem is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.window( menuBar=True, width=200 )
cmds.menu( label='Stuff' )
cmds.menuItem( subMenu=True, label='Colors' )
cmds.menuItem( label='Blue' )
cmds.menuItem( label='Green' )
cmds.menuItem( label='Yellow' )
cmds.setParent( '..', menu=True )
cmds.menuItem( divider=True, dividerLabel='Section 1' )
cmds.radioMenuItemCollection()
cmds.menuItem( label='Yes', radioButton=False )
cmds.menuItem( label='Maybe', radioButton=False )
cmds.menuItem( label='No', radioButton=True )
cmds.menuItem( divider=True, dividerLabel='Section 2' )
cmds.menuItem( label='Top', checkBox=True )
cmds.menuItem( label='Middle', checkBox=False )
cmds.menuItem( divider=True, longDivider=False )
cmds.menuItem( label='Bottom', checkBox=True )
cmds.menuItem( divider=True )
cmds.menuItem( label='Option' )
cmds.menuItem( optionBox=True )
cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
cmds.showWindow()

---
Return:
---


    string: Full path name to the menu item.

Flags:
---


---
allowOptionBoxes(aob): boolean
    properties: create, query
    Deprecated. All menus and menu items always allow option boxes.
In the case of submenu items this flag specifies whether the
submenu will be able to support option box menu items.
Always returns true.

---
annotation(ann): string
    properties: create, query, edit
    Annotate the menu item with an extra string value.

---
boldFont(bld): boolean
    properties: create, query
    Specify if text should be bold. Only supported in menus
which use the marking menu implementation.  Default is false
for Windows, and true for all other platforms.

---
checkBox(cb): boolean
    properties: create, query, edit
    Creates a check box menu item.  Argument specifies the
check box value.

---
collection(cl): string
    properties: create, query
    To explicitly add a radio menu item to a radioMenuItemCollection.

---
command(c): script
    properties: create, query, edit
    Attaches a command/script that will be executed when the
item is selected. Note this command is not executed when the
menu item is in an optionMenu control.

---
data(da): int
    properties: create, query, edit
    Attaches a piece of user-defined data to the menu item.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
divider(d): boolean
    properties: create, query
    Creates a divider menu item.

---
dividerLabel(dl): string
    properties: create, query, edit
    Adds a label to a divider menu item.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the menu item.

---
dragDoubleClickCommand(ddc): script
    properties: create, query, edit
    If the menu item is put on the shelf then this command
will be invoked when the corresponding shelf object is double
clicked.

---
dragMenuCommand(dmc): script
    properties: create, query, edit
    If the menu item is put on the shelf then this command
will be invoked when the corresponding shelf object is clicked.

---
echoCommand(ec): boolean
    properties: create, query, edit
    Specify whether the action attached with
the c/command flag should echo to the command output
areas when invoked. This flag is false by default and must be
specified with the c/command flag.

---
enable(en): boolean
    properties: create, query, edit
    Enable state for the menu item.  A disabled menu item is
dimmed and unresponsive.  An enabled menu item is selectable and
has normal appearance.

---
enableCommandRepeat(ecr): boolean
    properties: create, query, edit
    This flag only affects menu items to which a command can be
attached.  Specify true and the command may be repeated by
executing the command repeatLast.  This flag is true by
default for all items except for option box items.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
familyImage(fi): string
    properties: query
    Get the filename of the family icon associated with the menu.
The family icon will be used for the shelf unless an icon is specified with
the image flag.

---
image(i): string
    properties: create, query, edit
    The filename of the icon associated with the menu item.  If
the menu containing the menu item is being edited with a
menuEditor widget, then the menuEditor will use this icon to
represent the menu item. This icon will be displayed on the
shelf when the menu item is placed there.

---
imageOverlayLabel(iol): string
    properties: create, query, edit
    Specify a short (5 character) text string to be overlayed
on top of the icon associated with the menu item. This is primarily
a mechanism for differentiating menu items that are using a Family
icon due to the fact that an icon image had not been explicitly
defined. The image overlay label will not be used if an icon
image is defined for the menu item.

---
insertAfter(ia): string
    properties: create
    Specify After which item the new one will be placed. If
this flag is not specified, item is added at the end of the
menu. Use the empty string "" to insert before the first
item of the menu.

---
isCheckBox(icb): boolean
    properties: query
    Returns true if the item is a check box item.

---
isOptionBox(iob): boolean
    properties: query
    Returns true if the item is an option box item.

---
isRadioButton(irb): boolean
    properties: query
    Returns true if the item is a radio button item.

---
italicized(itl): boolean
    properties: create, query
    Specify if text should be italicized. Only supported in menus
which use the marking menu implementation.  Default is false.

---
label(l): string
    properties: create, query, edit
    The text that appears in the item.

---
longDivider(ld): boolean
    properties: create, query, edit
    Indicate whether the divider is long or short. Has no effect
if divider label is set. Default is true.

---
optionBox(ob): boolean
    properties: create, query
    Indicates that the menu item will be an option box item.  This
item will appear to the right of the preceeding menu item.

---
optionBoxIcon(obi): string
    properties: create, query, edit
    The filename of an icon to be used instead of the usual option box icon.
The icon is searched for in the folder specified by the XBMLANGPATH
environment variable.
The icon can be any size, but will be resized to the standard 16x16 pixels
when drawn.

---
parent(p): string
    properties: create
    Specify the menu that the item will appear in.

---
postMenuCommand(pmc): script
    properties: create, query, edit
    Specify a script to be executed when the submenu is about
to be shown.

---
postMenuCommandOnce(pmo): boolean
    properties: create, query, edit
    Indicate the pmc/postMenuCommand should only be
invoked once.  Default value is false, ie.
the pmc/postMenuCommand is invoked everytime the sub menu
is shown.

---
radialPosition(rp): string
    properties: create, query, edit
    The radial position of the menu item if it is in a Marking
Menu.  Radial positions are given in the form of a cardinal
direction, and may be "N", "NW", "W", "SW", "S", "SE", "E" or "NE".

---
radioButton(rb): boolean
    properties: create, query, edit
    Creates a radio button menu item.  Argument specifies the
radio button value.

---
runTimeCommand(rtc): string
    properties: create, edit
    A shortcut flag to link the menu item with a runTimeCommand.
The value is the name of the runTimeCommand (unique).
It copies the following fields from the runTimeCommand if those
fields have not been provided to this command:
label, annotation, image, command.
Note: command will be set to the runTimeCommand itself.

---
sourceType(stp): string
    properties: create, query, edit
    Set the language type for a command script. Can only be used in
conjunction with a command flag.  Without this flag, commands are
assumed to be the same language of the executing script.  In query
mode, will return the language of the specified command.
Valid values are "mel" and "python".

---
subMenu(sm): boolean
    properties: create, query
    Indicates that the item will have a submenu.
Subsequent menuItems will be added to the submenu
until setParent -menu is called.  Note that a submenu item
creates a menu object and consequently the menu command may
be used on the submenu item.

---
tearOff(to): boolean
    properties: create, query
    For the case where the menu item is a sub menu this flag will
make the sub menu tear-off-able. Note that this flag has no
effect on the other menu item types.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
version(ver): string
    properties: create, query, edit
    Specify the version that this menu item feature was introduced.
The argument should be given as a string of the version number
(e.g. "2013", "2014"). Currently only accepts major version
numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the menu item.  A menu item is created
visible by default.  Note that a menu item's actual appearance is
also dependent on the visible state of its parent layout(s).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/menuItem.html 
    """


def menuSet(flagaddMenu: string, flagallMenuSets: boolean, flagcurrentMenuSet: string, flagexists: string, flaghotBoxVisible: boolean, flaginsertMenu: tuple[string, uint], flaglabel: string, flagmenuArray: list[string], flagmoveMenu: tuple[string, uint], flagmoveMenuSet: tuple[string, uint], flagnumberOfMenuSets: boolean, flagnumberOfMenus: boolean, flagpermanent: boolean, flagremoveMenu: string, flagremoveMenuSet: string) -> string:
    """Synopsis:
---
---
 menuSet(
[object]
    , [addMenu=string], [allMenuSets=boolean], [currentMenuSet=string], [exists=string], [hotBoxVisible=boolean], [insertMenu=[string, uint]], [label=string], [menuArray=string[]], [moveMenu=[string, uint]], [moveMenuSet=[string, uint]], [numberOfMenuSets=boolean], [numberOfMenus=boolean], [permanent=boolean], [removeMenu=string], [removeMenuSet=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

menuSet is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

creating a new menu set;
cmds.menuSet( 'newMenuSetObjName', label='newMenuSet Label' )

using commands on a current menu set
first find the menu set if you don't know the name of it
animMS = maya.mel.eval('findMenuSetFromLabel("Animation")')

menu sets can be queried like normal commands
animMenus = cmds.menuSet(animMS, query=True, menuArray=True)

but editing the set requires either setting the current menu set...
(notice that the menu set comamnds following specify no specific menu set)
cmds.menuSet( currentMenuSet=animMS )
cmds.menuSet( removeMenu=animMenus[0] )
: (other commands which pertain to the animation menu set)

.. or temporarily setting the menu set to work on (does not affect current menu set)
(notice that every command following specifies the specific set to apply operations to)
polyMS = maya.mel.eval('findMenuSetFromLabel("Polygons")')
polyMenus = cmds.menuSet(polyMS, query=True, menuArray=True)
cmds.menuSet( polyMS, removeMenu=polyMenus[0], insertMenu=(polyMenus[1], 0) )

.. where the following commands still affect the animation menu set
animMenus = cmds.menuSet(query=True, menuArray=True)

if you need to find a specific menu...
deformMenu = maya.mel.eval( ('findMenuFromMenuSet(\"' + animMS + '\", "Deform")') )

moving a menu from one spot to another
(ie. moving the Deform Menu to the front of the list)
cmds.menuSet( moveMenu=(deformMenu, 0) )

---
Return:
---


    string: Name of resulting menu set.  (If there are no menu sets left, an empty string is returned)

Flags:
---


---
addMenu(am): string
    properties: create
    Appends a menu onto the end of the current menu set.

---
allMenuSets(ams): boolean
    properties: query
    Returns an array of the all the menu set object names in use.  Query returns string array.

---
currentMenuSet(cms): string
    properties: create, query
    The currently active menu set under which all operations affect (append, insert, remove, etc.).  Query returns string.

---
exists(ex): string
    properties: query
    Returns whether the specified menu set exists.  This query flag supports string arguments.
ie. menuSet -q -exists animationMenuSet;
      In query mode, this flag needs a value.

---
hotBoxVisible(hbv): boolean
    properties: create, query, edit
    Whether this menu set should be displayed in the hotbox as well as in the main menubar.

---
insertMenu(im): [string, uint]
    properties: create
    Inserts a menu into a specified index in the current menu set.

---
label(l): string
    properties: create, query
    The label of the current menu set.  Query returns string.

---
menuArray(ma): string[]
    properties: create, query
    An array of menu names (strings) in the current menu set.  Query returns string array.

---
moveMenu(mm): [string, uint]
    properties: create
    Moves a specified menu from the current menu set to a new position.

---
moveMenuSet(mms): [string, uint]
    properties: create
    Moves a specified menu set to another index.

---
numberOfMenuSets(nms): boolean
    properties: query
    Number of menuSets in total.  Query returns int.

---
numberOfMenus(nm): boolean
    properties: query
    The mumber of menus in the current menu set.  Query returns int.

---
permanent(p): boolean
    properties: create, query, edit
    Whether this menu set can be removed.

---
removeMenu(rm): string
    properties: create
    Removes a specified menu from the current menu set.

---
removeMenuSet(rms): string
    properties: create
    Removes the specified menu set object from the list of all menu sets.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/menuSet.html 
    """


def menuSetPref(flagexists: boolean, flagforce: boolean, flagloadAll: boolean, flagremoveAll: boolean, flagsaveAll: boolean, flagsaveBackup: boolean, flagversion: boolean) -> None:
    """Synopsis:
---
---
 menuSetPref(
[object]
    , [exists=boolean], [force=boolean], [loadAll=boolean], [removeAll=boolean], [saveAll=boolean], [saveBackup=boolean], [version=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

menuSetPref is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

saving the current menuSets
cmds.menuSetPref( saveAll=True )

loading to the current menuSets if they exist
if cmds.menuSetPref(exists=True) :
        cmds.menuSetPref(loadAll=True)

in certain cases, you may wish to remove previous preferences before saving
cmds.menuSetPref( removeAll=True )

---


Flags:
---


---
exists(e): boolean
    properties: query
    Returns whether the menuSet preferences file exists or not.

---
force(f): boolean
    properties: create, edit
    Forces a specified operation to continue even if errors are encountered (such as invalid
preferences).

---
loadAll(la): boolean
    properties: create
    Loads all the menuSets from the preferences file only if the preferences version matches,
or the -force flag is enabled.  On successful load, of a prefs file, an empty string is returned,
otherwise, a description of the problem encountered is returned.

---
removeAll(ra): boolean
    properties: create
    Removes all the menuSets from the preferences file (removes the whole file).

---
saveAll(sa): boolean
    properties: create
    Saves all the current menuSets into the preferences file.

---
saveBackup(sb): boolean
    properties: create
    Saves a backup of the current menu set preferences file if one exists.  This backup will
be saved in the same location as the current preferences file.

---
version(v): boolean
    properties: query
    The base version string which is saved out to file. It is also checked upon loading
in order to indicate changes in the default prefs since the prefs were last saved out.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/menuSetPref.html 
    """


def messageLine(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 messageLine(
[name]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

messageLine is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

window = cmds.window()
form = cmds.formLayout()
frame = cmds.frameLayout(labelVisible=False)
cmds.messageLine()
cmds.formLayout( form, edit=True, attachNone=(frame, 'top'), attachForm=[(frame, 'left', 0), (frame, 'bottom', 0), (frame, 'right', 0)] )
cmds.showWindow( window )

---
Return:
---


    string: : Full path name to the control.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/messageLine.html 
    """


def mimicManipulation(flagmanipulations: string, flagprevalidation: boolean, flagrefresh: boolean) -> boolean[]:
    """Synopsis:
---
---
 mimicManipulation([manipulations=string], [prevalidation=boolean], [refresh=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

mimicManipulation is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.createNode('transform')
cmds.mimicManipulation(manipulations='{ "session": [[{"plug": "transform1.tx", "value": 1.0}]] }')
Result: [False] ---


Build a series of manipulation using Python objects
cmds.setKeyframe('transform1', attribute="translateX", time=1, value=1)
cmds.setKeyframe('transform1', attribute="translateX", time=10, value=10)
manipulations = dict(session=[[{"plug": "transform1.translateX", "value": i}] for i in range(10)])
import json
manips = json.dumps(manipulations)
cmds.mimicManipulation(manipulations=manips)
Result: [True, True, True, True, True, True, True, True, True, True] ---

cmds.mimicManipulation(manipulations=manips, prevalidation=False)
Result: [False, True, True, True, True, True, True, True, True, True] ---


---
Return:
---


    boolean[]: True if the transaction could be evaluated by the Evaluation Manager, false otherwise, for each provided transaction

Flags:
---


---
manipulations(m): string
    properties: create
    JSON string representing the manipulations to be performed.

---
prevalidation(p): boolean
    properties: create
    Flag to control if prevalidation of the manipulated plugs will be
performed.  If it is and the plugs are already properly supported by
the Evaluation Manager, Evaluation Manager manipulation will be used
on the very first frame instead of requiring an initial frame with
dirty propagation and DG evaluation to validate Evaluation Manager
manipulation can be safely performed.

---
refresh(r): boolean
    properties: create
    Flag to control if a refresh is triggered after each manipulation.
Note that refresh is necessary for evaluation to kick in.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/mimicManipulation.html 
    """


def minimizeApp() -> None:
    """Synopsis:
---
---
 minimizeApp()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

minimizeApp is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.minimizeApp()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/minimizeApp.html 
    """


def mirrorJoint(flagmirrorBehavior: boolean, flagmirrorXY: boolean, flagmirrorXZ: boolean, flagmirrorYZ: boolean, flagsearchReplace: tuple[string, string]) -> list[string]:
    """Synopsis:
---
---
 mirrorJoint(
object
    , [mirrorBehavior=boolean], [mirrorXY=boolean], [mirrorXZ=boolean], [mirrorYZ=boolean], [searchReplace=[string, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

mirrorJoint is undoable, NOT queryable, and NOT editable.




Example:
---
import maya.cmds as cmds

Create a mirrored branch of the skeleton starting from the joint "jointName"
about the yz-plane.
Joint orientations on the mirrored side will be identical to the source side.
---

cmds.mirrorJoint( 'jointName' )

Create a mirrored branch of the skeleton starting from the joint "jointName"
about the yz-plane.
Joint orientations on the mirrored side will be mirrored from the source side.
---

cmds.mirrorJoint('jointName',mirrorBehavior=True,myz=True)

Create a mirrored branch of the skeleton starting from the selected joint
about the xy-plane.
Joint orientations on the mirrored side will be mirrored from the source side.
Joint names on the duplicated side will contain the string "right_" if
the corresponding joint on the original side contained the string "left_".
---

cmds.mirrorJoint(mirrorXY=True,mirrorBehavior=True,searchReplace=('left_', 'right_') )

---
Return:
---


    list[string]: Names of the mirrored joints

Flags:
---


---
mirrorBehavior(mb): boolean
    properties: create
    The mirrorBehavior flag is used to specify that when performing the
mirror, the joint orientation axes should be mirrored such that equal
rotations on the original and mirrored joints will place the skeleton
in a mirrored position (symmetric across the mirroring plane). Thus,
animation curves from the original joints can be copied to the mirrored
side to produce a similar (but symmetric) behavior. When mirrorBehavior
is not specified, the joint orientation on the mirrored side will be identical
to the source side.

---
mirrorXY(mxy): boolean
    properties: create
    mirror skeleton from the selected joint about xy-plane in world space.

---
mirrorXZ(mxz): boolean
    properties: create
    mirror skeleton from the selected joint about xz-plane in world space.

---
mirrorYZ(myz): boolean
    properties: create
    mirror skeleton from the selected joint about yz-plane in world space.

---
searchReplace(sr): [string, string]
    properties: create
    After performing the mirror, rename the new joints by searching the name for the
first specified string and replacing it with the second specified string.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/mirrorJoint.html 
    """


def modelCurrentTimeCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagpercent: float) -> string:
    """Synopsis:
---
---
 modelCurrentTimeCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [percent=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

modelCurrentTimeCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.modelCurrentTimeCtx()

---
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
percent(per): float
    properties: query, edit
    Percent of the screen space that represents the full time
slider range (default is 50%)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/modelCurrentTimeCtx.html 
    """


def modelEditor(flagactiveComponentsXray: boolean, flagactiveCustomEnvironment: string, flagactiveCustomGeometry: string, flagactiveCustomLighSet: string, flagactiveCustomOverrideGeometry: string, flagactiveCustomRenderer: string, flagactiveOnly: boolean, flagactiveShadingGraph: string, flagactiveView: boolean, flagaddObjects: string, flagaddSelected: boolean, flagaddSelectedObjects: boolean, flagallObjects: boolean, flagbackfaceCulling: boolean, flagbluePencil: boolean, flagbufferMode: string, flagbumpResolution: tuple[uint, uint], flagcamera: string, flagcameraName: string, flagcameraSet: string, flagcameraSetup: boolean, flagcameras: boolean, flagcapture: string, flagcaptureSequenceNumber: int, flagclipGhosts: boolean, flagcmEnabled: boolean, flagcolorMap: boolean, flagcolorResolution: tuple[uint, uint], flagcontrol: boolean, flagcontrolVertices: boolean, flagcullingOverride: string, flagdefault: boolean, flagdefineTemplate: string, flagdeformers: boolean, flagdimensions: boolean, flagdisplayAppearance: string, flagdisplayLights: string, flagdisplayTextures: boolean, flagdocTag: string, flagdynamicConstraints: boolean, flagdynamics: boolean, flageditorChanged: script, flagexcludeObjectMask: int64, flagexcludeObjectPreset: string, flagexcludePluginList: string, flagexists: boolean, flagexposure: float, flagfilter: string, flagfilteredObjectList: boolean, flagfluids: boolean, flagfogColor: tuple[float, float, float, float], flagfogDensity: float, flagfogEnd: float, flagfogMode: string, flagfogSource: string, flagfogStart: float, flagfogging: boolean, flagfollicles: boolean, flagforceMainConnection: string, flaggamma: float, flaggreasePencils: boolean, flaggrid: boolean, flaghairSystems: boolean, flaghandles: boolean, flagheadsUpDisplay: boolean, flagheight: boolean, flaghighlightConnection: string, flaghulls: boolean, flagignorePanZoom: boolean, flagikHandles: boolean, flagimagePlane: boolean, flaginteractive: boolean, flaginteractiveBackFaceCull: boolean, flaginteractiveDisableShadows: boolean, flagisFiltered: boolean, flagjointXray: boolean, flagjoints: boolean, flaglights: boolean, flaglineWidth: float, flaglocators: boolean, flaglockMainConnection: boolean, flaglowQualityLighting: boolean, flagmainListConnection: string, flagmanipulators: boolean, flagmaxConstantTransparency: float, flagmaximumNumHardwareLights: boolean, flagmodelPanel: string, flagmotionTrails: boolean, flagnCloths: boolean, flagnParticles: boolean, flagnRigids: boolean, flagnoUndo: boolean, flagnurbsCurves: boolean, flagnurbsSurfaces: boolean, flagobjectFilter: script, flagobjectFilterList: script, flagobjectFilterListUI: script, flagobjectFilterShowInHUD: boolean, flagobjectFilterUI: script, flagocclusionCulling: boolean, flagpanel: string, flagparent: string, flagparticleInstancers: boolean, flagpivots: boolean, flagplanes: boolean, flagpluginObjects: tuple[string, boolean], flagpluginShapes: boolean, flagpolymeshes: boolean, flagqueryPluginObjects: string, flagremoveSelected: boolean, flagrendererDeviceName: boolean, flagrendererList: boolean, flagrendererListUI: boolean, flagrendererName: string, flagrendererOverrideList: boolean, flagrendererOverrideListUI: boolean, flagrendererOverrideName: string, flagresetCustomCamera: boolean, flagsceneRenderFilter: string, flagselectionConnection: string, flagselectionHiliteDisplay: boolean, flagsetSelected: boolean, flagshadingModel: int, flagshadows: boolean, flagsmallObjectCulling: boolean, flagsmallObjectThreshold: float, flagsmoothWireframe: boolean, flagsortTransparent: boolean, flagstateString: boolean, flagstereoDrawMode: boolean, flagstrokes: boolean, flagsubdivSurfaces: boolean, flagtextureAnisotropic: boolean, flagtextureCompression: boolean, flagtextureDisplay: string, flagtextureEnvironmentMap: boolean, flagtextureHilight: boolean, flagtextureMaxSize: int, flagtextureMemoryUsed: boolean, flagtextureSampling: int, flagtextures: boolean, flagtoggleExposure: boolean, flagtoggleGamma: boolean, flagtranspInShadows: boolean, flagtransparencyAlgorithm: string, flagtwoSidedLighting: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateColorMode: boolean, flagupdateMainConnection: boolean, flaguseBaseRenderer: boolean, flaguseColorIndex: boolean, flaguseDefaultMaterial: boolean, flaguseInteractiveMode: boolean, flaguseRGBImagePlane: boolean, flaguseReducedRenderer: boolean, flaguseTemplate: string, flaguserNode: string, flagviewObjects: boolean, flagviewSelected: boolean, flagviewTransformName: string, flagviewType: boolean, flagwidth: boolean, flagwireframeBackingStore: boolean, flagwireframeOnShaded: boolean, flagxray: boolean) -> string:
    """Synopsis:
---
---
 modelEditor(
[editorName]
    , [activeComponentsXray=boolean], [activeCustomEnvironment=string], [activeCustomGeometry=string], [activeCustomLighSet=string], [activeCustomOverrideGeometry=string], [activeCustomRenderer=string], [activeOnly=boolean], [activeShadingGraph=string], [activeView=boolean], [addObjects=string], [addSelected=boolean], [addSelectedObjects=boolean], [allObjects=boolean], [backfaceCulling=boolean], [bluePencil=boolean], [bufferMode=string], [bumpResolution=[uint, uint]], [camera=string], [cameraName=string], [cameraSet=string], [cameraSetup=boolean], [cameras=boolean], [capture=string], [captureSequenceNumber=int], [clipGhosts=boolean], [cmEnabled=boolean], [colorMap=boolean], [colorResolution=[uint, uint]], [control=boolean], [controlVertices=boolean], [cullingOverride=string], [default=boolean], [defineTemplate=string], [deformers=boolean], [dimensions=boolean], [displayAppearance=string], [displayLights=string], [displayTextures=boolean], [docTag=string], [dynamicConstraints=boolean], [dynamics=boolean], [editorChanged=script], [excludeObjectMask=int64], [excludeObjectPreset=string], [excludePluginList=string], [exists=boolean], [exposure=float], [filter=string], [filteredObjectList=boolean], [fluids=boolean], [fogColor=[float, float, float, float]], [fogDensity=float], [fogEnd=float], [fogMode=string], [fogSource=string], [fogStart=float], [fogging=boolean], [follicles=boolean], [forceMainConnection=string], [gamma=float], [greasePencils=boolean], [grid=boolean], [hairSystems=boolean], [handles=boolean], [headsUpDisplay=boolean], [height=boolean], [highlightConnection=string], [hulls=boolean], [ignorePanZoom=boolean], [ikHandles=boolean], [imagePlane=boolean], [interactive=boolean], [interactiveBackFaceCull=boolean], [interactiveDisableShadows=boolean], [isFiltered=boolean], [jointXray=boolean], [joints=boolean], [lights=boolean], [lineWidth=float], [locators=boolean], [lockMainConnection=boolean], [lowQualityLighting=boolean], [mainListConnection=string], [manipulators=boolean], [maxConstantTransparency=float], [maximumNumHardwareLights=boolean], [modelPanel=string], [motionTrails=boolean], [nCloths=boolean], [nParticles=boolean], [nRigids=boolean], [noUndo=boolean], [nurbsCurves=boolean], [nurbsSurfaces=boolean], [objectFilter=script], [objectFilterList=script], [objectFilterListUI=script], [objectFilterShowInHUD=boolean], [objectFilterUI=script], [occlusionCulling=boolean], [panel=string], [parent=string], [particleInstancers=boolean], [pivots=boolean], [planes=boolean], [pluginObjects=[string, boolean]], [pluginShapes=boolean], [polymeshes=boolean], [queryPluginObjects=string], [removeSelected=boolean], [rendererDeviceName=boolean], [rendererList=boolean], [rendererListUI=boolean], [rendererName=string], [rendererOverrideList=boolean], [rendererOverrideListUI=boolean], [rendererOverrideName=string], [resetCustomCamera=boolean], [sceneRenderFilter=string], [selectionConnection=string], [selectionHiliteDisplay=boolean], [setSelected=boolean], [shadingModel=int], [shadows=boolean], [smallObjectCulling=boolean], [smallObjectThreshold=float], [smoothWireframe=boolean], [sortTransparent=boolean], [stateString=boolean], [stereoDrawMode=boolean], [strokes=boolean], [subdivSurfaces=boolean], [textureAnisotropic=boolean], [textureCompression=boolean], [textureDisplay=string], [textureEnvironmentMap=boolean], [textureHilight=boolean], [textureMaxSize=int], [textureMemoryUsed=boolean], [textureSampling=int], [textures=boolean], [toggleExposure=boolean], [toggleGamma=boolean], [transpInShadows=boolean], [transparencyAlgorithm=string], [twoSidedLighting=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateColorMode=boolean], [updateMainConnection=boolean], [useBaseRenderer=boolean], [useColorIndex=boolean], [useDefaultMaterial=boolean], [useInteractiveMode=boolean], [useRGBImagePlane=boolean], [useReducedRenderer=boolean], [useTemplate=string], [userNode=string], [viewObjects=boolean], [viewSelected=boolean], [viewTransformName=string], [viewType=boolean], [width=boolean], [wireframeBackingStore=boolean], [wireframeOnShaded=boolean], [xray=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

modelEditor is undoable, queryable, and editable.
Note that some of the flags of this command may have different settings
for normal mode and for interactive/playback mode.  For example, a
modelEditor can be set to use shaded mode normally, but to use wireframe
during playback for greater speed.  Some flags also support having
defaults set so that new model editors will be created with those settings.




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
addSelectedObjects(aso): boolean
    properties: create
    If set then add the selected objects to the editor

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
clipGhosts(cg): boolean
    properties: create, query, edit
    Define whether the clip ghosts should be added or not

---
cmEnabled(cme): boolean
    properties: query, edit
    Turn on or off applying color management in the editor.  If set, the color
management configuration set in the current editor is used.

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
excludeObjectMask(eom) 2024: int64
    properties: create, query, edit
    Set exclude object display settings for all individual objects at once using
a integer mask.

---
excludeObjectPreset(eop) 2024: string
    properties: create, query, edit
    Set exclude object display settings for all individual objects at once using
a named preset.

---
excludePluginList(epl) 2024: string
    properties: create, query, edit, multiuse
    Set exclude object display settings for a plugin object.

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
gamma(ga): float
    properties: query, edit
    The gamma value used by the color management of the current editor.

---
greasePencils(gp): boolean
    properties: create, query, edit
    Define whether the grease pencil marks should be added or not

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
particleInstancers(pi): boolean
    properties: create, query, edit
    Define whether the particle instances should be shown or not

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
toggleExposure(tge): boolean
    properties: edit
    Toggles between the current and the default exposure value of the editor.

---
toggleGamma(tgg): boolean
    properties: edit
    Toggles between the current and the default gamma value of the editor.

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
viewTransformName(vtn): string
    properties: query, edit
    Sets the view pipeline to be applied if color management is enabled in the
current editor.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/modelEditor.html 
    """


def modelPanel(flagbarLayout: boolean, flagcamera: string, flagcontrol: boolean, flagcopy: string, flagcreateString: boolean, flagdefineTemplate: string, flagdocTag: string, flageditString: boolean, flagexists: boolean, flaginit: boolean, flagisUnique: boolean, flaglabel: string, flagmenuBarRepeatLast: boolean, flagmenuBarVisible: boolean, flagmodelEditor: boolean, flagneedsInit: boolean, flagparent: string, flagpopupMenuProcedure: script, flagreplacePanel: string, flagtearOff: boolean, flagtearOffCopy: string, flagtearOffRestore: boolean, flagunParent: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 modelPanel(
panelName
    , [barLayout=boolean], [camera=string], [control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [modelEditor=boolean], [needsInit=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

modelPanel is undoable, queryable, and editable.modelEditor



Example:
---
import maya.cmds as cmds

   Example 1.
---

   Create a model panel in a separate window.
---

window = cmds.window()
cmds.paneLayout()
cmds.modelPanel()
cmds.showWindow( window )

   Example 2.
---

   Set the panel configuration to show all 4 model views.
   Then swap the Perspective View and Front View panels.
---


Since setNamePanelLayout is a MEL procedures, we need to call through MEL
import maya.mel
maya.mel.eval('setNamedPanelLayout("Four View")')
perspPanel = cmds.getPanel( withLabel='Persp View')
frontPanel = cmds.getPanel( withLabel='Front View')
cmds.modelPanel( perspPanel, edit=True, replacePanel=frontPanel )

---
Return:
---


    string: The name of the panel.

Flags:
---


---
barLayout(bl): boolean
    properties: query
    This flag returns the name of the layout which is the parent of
the panels icon bar.

---
camera(cam): string
    properties: query, edit
    Query or edit the camera in a modelPanel.

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
modelEditor(me): boolean
    properties: query
    This flag returns the name of the model editor
contained by the panel.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/modelPanel.html 
    """


def moduleInfo(flagdefinition: boolean, flaglistModules: boolean, flagmoduleName: string, flagpath: boolean, flagversion: boolean) -> list[string]:
    """Synopsis:
---
---
 moduleInfo([definition=boolean], [listModules=boolean], [moduleName=string], [path=boolean], [version=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

moduleInfo is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.moduleInfo(listModules=True)
cmds.moduleInfo(definition=True, moduleName='myModule')
cmds.moduleInfo(path=True, moduleName='myModule')
cmds.moduleInfo(version=True, moduleName='myModule')

---
Return:
---


    list[string]: Command result

Flags:
---


---
definition(d): boolean
    properties: create
    Returns module definition file name for the module specified by the -moduleName parameter.

---
listModules(lm): boolean
    properties: create
    Returns an array containing the names of all currently loaded modules.

---
moduleName(mn): string
    properties: create
    The name of the module whose information you want to retrieve. Has to be used with either -definition / -path / -version flags.

---
path(p): boolean
    properties: create
    Returns the module path for the module specified by the -moduleName parameter.

---
version(v): boolean
    properties: create
    Returns the module version for the module specified by the -moduleName parameter.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/moduleInfo.html 
    """


def mouse(flagenableScrollWheel: boolean, flagmouseButtonTracking: int, flagmouseButtonTrackingStatus: boolean, flagscrollWheelStatus: boolean) -> int:
    """Synopsis:
---
---
 mouse([enableScrollWheel=boolean], [mouseButtonTracking=int], [mouseButtonTrackingStatus=boolean], [scrollWheelStatus=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

mouse is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.mouse( enableScrollWheel=False )

mouseEnabled = cmds.mouse(scrollWheelStatus=True)

cmds.mouse( mouseButtonTracking=1 )

numberOfMouseButtons = cmds.mouse(mouseButtonTrackingStatus=True)

---
Return:
---


    int: When-scrollWheelStatusflag is used, will return 1 if scroll wheel support enabled, otherwise 0.When-mouseButtonTrackingStatusflag is used, will return the number of mouse buttons being tracked.

Flags:
---


---
enableScrollWheel(esw): boolean
    properties: create
    Enable or disable scroll wheel support.

---
mouseButtonTracking(mbt): int
    properties: create
    Set the number (1, 2 or 3) of mouse buttons to track.
Note: this is only supported on Macintosh

---
mouseButtonTrackingStatus(mbs): boolean
    properties: create
    returns the current number of mouse buttons being tracked.

---
scrollWheelStatus(sws): boolean
    properties: create
    returns the current status of scroll wheel support.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/mouse.html 
    """


def movIn(flagfile: string, flagstartTime: time) -> None:
    """Synopsis:
---
---
 movIn(
[attributeList]
    , [file=string], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

movIn is undoable, NOT queryable, and NOT editable.
The starting time used for the .mov file importation is the current time
when the command is executed.

Valid attribute types are numeric attributes; time attributes; linear
attributes; angular attributes; compound attributes made of the types
listed previously; and multi attributes composed of the types listed
previously. If an unsuppoted attribute type is requested, the command
will fail and no data will be imported. It is important that your
user units are set to the same units used in the .mov file, otherwise
linear and angular values will be incorrect.

To export a .mov file, use the movOut command.




Example:
---
import maya.cmds as cmds

cmds.sphere( n='sph' )

   Start importing the data at time 45;
---

cmds.currentTime( 45 )

   Read in rotation, translation, and scale information from the
   test.mov file into the sphere. The order of data in the test.mov
   file must be: rx, ry, rz, tx, ty, tz.
---

cmds.movIn( 'sph.r', 'sph.t', f='sphereMotion.mov' )

   An equivalent way of importing data into the sphere.
---

cmds.movIn( 'sph.rx', 'sph.ry', 'sph.rz', 'sph.tx', 'sph.ty', 'sph.tz', f='sphereMotion.mov' )

---


Flags:
---


---
file(f): string
    properties: create
    The name of the .mov file. If no extension is used, a .mov will be
added.

---
startTime(st): time
    properties: create
    The default start time for importing the .mov file is the
current time. The startTime option sets the starting time for
the .mov data in the current time unit.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/movIn.html 
    """


def movOut(flagcomment: boolean, flagfile: string, flagprecision: uint, flagtime: timerange) -> None:
    """Synopsis:
---
---
 movOut(
[targetList]
    , [comment=boolean], [file=string], [precision=uint], [time=timerange])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

movOut is undoable, NOT queryable, and NOT editable.
Length, angle, and time values will be written to the file in the
user units.

If an unsupported attribute type is requested, the action will fail.
The .mov file may be read back into Maya using the movIn command.




Example:
---
import maya.cmds as cmds

   Create a sphere and set some keyframes.
---

cmds.sphere( n='sph' )
cmds.currentTime( 0 )
cmds.move( 0, 0, 0, 'sph' )
cmds.setKeyframe( 'sph.t' )
cmds.currentTime( 24 )
cmds.move( 8, 9, 10, 'sph' )
cmds.setKeyframe( 'sph.t' )

   Write the keys to a .mov file.
---

cmds.movOut( 'sph.t', f='sphereMotion.mov', t=(0,24) )

   Another way to write the same file.
---

cmds.movOut( 'sph.tx', 'sph.ty', 'sph.tz', f='sphereMotion.mov', t=(0,24) )

---


Flags:
---


---
comment(c): boolean
    properties: create
    If true, the attributes written to the .mov file will be listed
in a commented section at the top of the .mov file. The default is
false.

---
file(f): string
    properties: create
    The name of the .mov file. If no extension is used, a .mov will be
added.

---
precision(pre): uint
    properties: create
    Sets the number of digits to the right of the decimal place in
the .mov file.
C: The default is 6.

---
time(t): timerange
    properties: create
    The time range to save as a .mov file. The default is the current
time range.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/movOut.html 
    """


def move(flagabsolute: boolean, flagcomponentOffset: boolean, flagcomponentSpace: boolean, flagconstrainAlongNormal: boolean, flagdeletePriorHistory: boolean, flaglocalSpace: boolean, flagmoveX: boolean, flagmoveXY: boolean, flagmoveXYZ: boolean, flagmoveXZ: boolean, flagmoveY: boolean, flagmoveYZ: boolean, flagmoveZ: boolean, flagobjectSpace: boolean, flagorientJoint: string, flagparameter: boolean, flagpreserveChildPosition: boolean, flagpreserveGeometryPosition: boolean, flagpreserveUV: boolean, flagreflection: boolean, flagreflectionAboutBBox: boolean, flagreflectionAboutOrigin: boolean, flagreflectionAboutX: boolean, flagreflectionAboutY: boolean, flagreflectionAboutZ: boolean, flagreflectionTolerance: float, flagrelative: boolean, flagrotatePivotRelative: boolean, flagscalePivotRelative: boolean, flagsecondaryAxisOrient: string, flagsymNegative: boolean, flagworldSpace: boolean, flagworldSpaceDistance: boolean, flagxformConstraint: string) -> None:
    """Synopsis:
---
---
 move(
float float float [objects]
    , [absolute=boolean], [componentOffset=boolean], [componentSpace=boolean], [constrainAlongNormal=boolean], [deletePriorHistory=boolean], [localSpace=boolean], [moveX=boolean], [moveXY=boolean], [moveXYZ=boolean], [moveXZ=boolean], [moveY=boolean], [moveYZ=boolean], [moveZ=boolean], [objectSpace=boolean], [orientJoint=string], [parameter=boolean], [preserveChildPosition=boolean], [preserveGeometryPosition=boolean], [preserveUV=boolean], [reflection=boolean], [reflectionAboutBBox=boolean], [reflectionAboutOrigin=boolean], [reflectionAboutX=boolean], [reflectionAboutY=boolean], [reflectionAboutZ=boolean], [reflectionTolerance=float], [relative=boolean], [rotatePivotRelative=boolean], [scalePivotRelative=boolean], [secondaryAxisOrient=string], [symNegative=boolean], [worldSpace=boolean], [worldSpaceDistance=boolean], [xformConstraint=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

move is undoable, NOT queryable, and NOT editable.
The default behaviour, when no objects or flags are passed, is
to do a absolute move on each currently selected object in the
world space. The value of the coordinates are interpreted as
being defined in the current linear unit unless the unit is
explicitly mentioned.

When using -objectSpace there are two ways to use this command.
If numbers are typed without units then the internal values of
the object are set to these values. If, on the other hand a
unit is specified then the internal value is set to the equivalent
internal value that represents that world-space distance.

The -localSpace flag moves the object in its parent space. In this
space the x,y,z values correspond directly to the tx, ty, tz
channels on the object.

The -rotatePivotRelative/-scalePivotRelative flags can be used
with the -absolute flag to translate an object so that its
pivot point ends up at the given absolute position. These
flags will be ignored if components are specified.

The -worldSpaceDistance flag is a modifier flag that may be used
in conjunction with the -objectSpace/-localSpace flags. When this
flag is specified the command treats the x,y,z values as world
space units so the object will move the specified world space
distance but it will move along the axis specified by the
-objectSpace/-localSpace flag. The default behaviour, without
this flag, is to treat the x,y,z values as units in object
space or local space. In other words, the worldspace distance
moved will depend on the transformations applied to the object
unless this flag is specified.




Example:
---
import maya.cmds as cmds

cmds.polySphere()
cmds.move( 1, 1, 1 )
cmds.move( 5, y=True )
cmds.move( '1in', '1in', '1in', relative=True, objectSpace=True, worldSpaceDistance=True )
cmds.move( 0, 0, 0, 'pSphere1', absolute=True )

---


Flags:
---


---
absolute(a): boolean
    properties: create
    Perform an absolute operation.

---
componentOffset(co): boolean
    properties: create
    Move components individually in local space

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
localSpace(ls): boolean
    properties: create
    Move in local space

---
moveX(x): boolean
    properties: create
    Move in X direction

---
moveXY(xy): boolean
    properties: create
    Move in XY direction

---
moveXYZ(xyz): boolean
    properties: create
    Move in all directions (default)

---
moveXZ(xz): boolean
    properties: create
    Move in XZ direction

---
moveY(y): boolean
    properties: create
    Move in Y direction

---
moveYZ(yz): boolean
    properties: create
    Move in YZ direction

---
moveZ(z): boolean
    properties: create
    Move in Z direction

---
objectSpace(os): boolean
    properties: create
    Move in object space

---
orientJoint(oj): string
    properties: create
    Default is xyz.

---
parameter(p): boolean
    properties: create
    Move in parametric space

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
    When true, UV values on translated components are projected along the translation
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
rotatePivotRelative(rpr): boolean
    properties: create
    Move relative to the object's rotate pivot point.

---
scalePivotRelative(spr): boolean
    properties: create
    Move relative to the object's scale pivot point.

---
secondaryAxisOrient(sao): string
    properties: create
    Default is xyz.

---
symNegative(smn): boolean
    properties: create
    When set the component transformation is flipped so it is relative to the
negative side of the symmetry plane. The default (no flag) is to transform
components relative to the positive side of the symmetry plane.

---
worldSpace(ws): boolean
    properties: create
    Move in world space

---
worldSpaceDistance(wd): boolean
    properties: create
    Move is specified in world space units

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/move.html 
    """


def moveKeyCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagmoveFunction: string, flagname: string, flagoption: string) -> string:
    """Synopsis:
---
---
 moveKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [moveFunction=string], [name=string], [option=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

moveKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a move key context which works in insert mode
for the graph editor
---

newCtx = cmds.moveKeyCtx(option='insert')

Edit the context to over mode
---

cmds.moveKeyCtx( newCtx, e=True, option='over' )

---
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
moveFunction(mf): string
    properties: query, edit
    linear | power | constant. Specifies how the keys are
dragged. The default move type is constant where all
keys move the same amount as controlled by user movement.
Power provides a fall-off function where the center of
the drag moves the most and the keys around the drag move
less.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
option(o): string
    properties: create, query, edit
    Valid values are "move," "insert," "over," and
"segmentOver." When you "move" a key, the key will not cross over
(in time) any keys before or after it. When you "insert" a key,
all keys before or after (depending upon the -timeChange value)
will be moved an equivalent amount. When you "over" a key, the key
is allowed to move to any time (as long as a key is not there already).
When you "segmentOver" a set of keys (this option only has a
noticeable effect when more than one key is being moved) the first
key (in time) and last key define a segment (unless you specify a
time range). That segment is then allowed to move over other keys,
and keys will be moved to make room for the segment.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/moveKeyCtx.html 
    """


def moveVertexAlongDirection(flagdirection: tuple[float, float, float], flagmagnitude: linear, flagnormalDirection: linear, flaguDirection: linear, flaguvNormalDirection: tuple[linear, linear, linear], flagvDirection: linear) -> None:
    """Synopsis:
---
---
 moveVertexAlongDirection([direction=[float, float, float]], [magnitude=linear], [normalDirection=linear], [uDirection=linear], [uvNormalDirection=[linear, linear, linear]], [vDirection=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

moveVertexAlongDirection is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.moveVertexAlongDirection( "nurbsSurface1.cv[1][1]", "pPlane1.vtx[120]", d=[(1, 1, 1), (1, 0, 0)], m=[2.0, 1.0] )
Move the control vertex on the surface, mesh in the normalized
directions (1,1,1), (1,0,0) by magnitude 2.0, 1.0 respectively.

cmds.moveVertexAlongDirection( "nurbsSurface1.cv[3][1]", "nurbsSurface2.cv[0][0]", "pPlane1.vtx[10]", n=[1, -1.9, 3] )
Move the control vertex on the NURBS surfaces, mesh along their
respective unit normals by a magnitudes 1.0, -1.9 and 3.0 respectively.

cmds.moveVertexAlongDirection( "nurbsSurface1.cv[4][5]", "nurbsSurface2.cv[0][0]", u=[2.0, 1.0] )
Move the control vertex on the NURBS surfaces in the normalized
tangent along U by a magnitude 2.0 and 1.0 respectively.

cmds.moveVertexAlongDirection( "nurbsSurface1.cv[2][3]", v=-1.0 )
Move the control vertex on the nurbsSurface in the normalized
tangent along V by -1.0

cmds.moveVertexAlongDirection( "nurbsSurface1.cv[1][1]", uvn=(1, 2, -1) )
Move the control vertex on the nurbsSurface in the space defined
by triad [u,v,n] by 1,2,-1 respectively.
If the initial vertex position is o(ox,oy,oz) and u,v and n are
direction vectors then the new position p(px,py,pz) would be:
p = o + 1*u + 2*v + (-1)*n ;

---


Flags:
---


---
direction(d): [float, float, float]
    properties: create, multiuse
    move the vertex along the direction as specified. The direction is
normalized.

---
magnitude(m): linear
    properties: create, multiuse
    move by the specified magnitude in the direction vector.

---
normalDirection(n): linear
    properties: create, multiuse
    move components in the direction of normal by the given magnitude at
the respective components. The normal is 'normalized'.

---
uDirection(u): linear
    properties: create, multiuse
    move components in the direction of tangent along U at the
respective components where appropriate. The flag is ignored
for polygons, NURBS curves. The u direction is normalized.

---
uvNormalDirection(uvn): [linear, linear, linear]
    properties: create, multiuse
    move in the triad space [u,v,n] at the respective components by the
specified displacements. The flag is ignored for polygons, NURBS curves.

---
vDirection(v): linear
    properties: create, multiuse
    move components in the direction of tangent along V at the
respective components where appropriate. The flag is ignored
for polygons, NURBS curves.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/moveVertexAlongDirection.html 
    """


def movieInfo(flagcounter: boolean, flagdropFrame: boolean, flagframeCount: boolean, flagframeDuration: boolean, flagheight: boolean, flagmovieTexture: boolean, flagnegTimesOK: boolean, flagnumFrames: boolean, flagquickTime: boolean, flagtimeCode: boolean, flagtimeCodeTrack: boolean, flagtimeScale: boolean, flagtwentyFourHourMax: boolean, flagwidth: boolean) -> None:
    """Synopsis:
---
---
 movieInfo(string, [counter=boolean], [dropFrame=boolean], [frameCount=boolean], [frameDuration=boolean], [height=boolean], [movieTexture=boolean], [negTimesOK=boolean], [numFrames=boolean], [quickTime=boolean], [timeCode=boolean], [timeCodeTrack=boolean], [timeScale=boolean], [twentyFourHourMax=boolean], [width=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

movieInfo is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.movieInfo("C:/My Documents/myMovie.avi", frameCount=1)
24

---


Flags:
---


---
counter(cn): boolean
    properties: create
    Query the 'counter' flag of the movie's timecode format.
If this is true, the timecode returned by the -timeCode flag will be a simple counter.
If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).

---
dropFrame(df): boolean
    properties: create
    Query the 'drop frame' flag of the movie's timecode format.

---
frameCount(f): boolean
    properties: create
    Query the number of frames in the movie file

---
frameDuration(fd): boolean
    properties: create
    Query the frame duration of the movie's timecode format.

---
height(h): boolean
    properties: create
    Query the height of the movie

---
movieTexture(mt): boolean
    properties: create
    If set, the string argument is interpreted as the name of a movie texture node,
and the command then operates on the movie loaded by that node.

---
negTimesOK(nt): boolean
    properties: create
    Query the 'neg times OK' flag of the movie's timecode format.

---
numFrames(nf): boolean
    properties: create
    Query the whole number of frames per second of the movie's timecode format.

---
quickTime(qt): boolean
    properties: create
    Query whether the movie is a QuickTime movie.

---
timeCode(tc): boolean
    properties: create
    Query the timecode of the current movie frame.

---
timeCodeTrack(tt): boolean
    properties: create
    Query whether the movie has a timecode track.

---
timeScale(ts): boolean
    properties: create
    Query the timescale of the movie's timecode format.

---
twentyFourHourMax(tf): boolean
    properties: create
    Query the '24 hour max' flag of the movie's timecode format.

---
width(w): boolean
    properties: create
    Query the width of the movie

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/movieInfo.html 
    """


def multiProfileBirailSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagpolygon: int, flagtangentContinuityProfile1: boolean, flagtangentContinuityProfile2: boolean, flagtransformMode: int) -> list[string]:
    """Synopsis:
---
---
 multiProfileBirailSurface(
curve curve curve... curve curve
    , [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean], [polygon=int], [tangentContinuityProfile1=boolean], [tangentContinuityProfile2=boolean], [transformMode=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

multiProfileBirailSurface is undoable, queryable, and editable.
In this case, the cmd creates a railed surface by sweeping the profile
"curve1" to profile "curve2", profile "curve2" to profile "curve3"
along the two rail curves "rail1", "rail2". There must be atleast 3
profile curves followed by the two rail curves. The profile curves
must intersect the two rail curves. The constructed may be made
tangent continuous to the first and last profile using the flags -tp1,
-tp2 provided the profiles are surface curves i.e. isoparms, curve on
surface or trimmed edge.




Example:
---
import maya.cmds as cmds

cmds.multiProfileBirailSurface( 'curve1', 'curve2', 'curve3', 'surface1.vn[0.5]', 'surface1.vn[1.0]', ch=True )

tangent continuous surface across the first and last profile.
cmds.multiProfileBirailSurface( 'surface1.vn[0.5]', 'curve1', 'surface1.vn[1.0]', 'curve3', 'curve4', ch=False, tp1=True, tp2=True )

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
    Tangent continuous across the first profile. The profile must be a surface curve.
Default: false

---
tangentContinuityProfile2(tp2): boolean
    properties: create, query, edit
    Tangent continuous across the last profile. The profile must be a surface curve.
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/multiProfileBirailSurface.html 
    """


def multiTouch(flaggestures: boolean, flagtrackpad: uint) -> None:
    """Synopsis:
---
---
 multiTouch([gestures=boolean], [trackpad=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

multiTouch is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Enable multi-touch gestures.
cmds.multiTouch(gestures=True)

To query whether multi-touch gestures are enabled or not:
cmds.multiTouch(q=True, gestures=True)

Set the trackpad mode to 'Cursor and Multi-touch'.
cmds.multiTouch(trackpad=3)

To query the trackpad mode:
cmds.multiTouch(q=True, trackpad=True)

---


Flags:
---


---
gestures(g): boolean
    properties: create, query
    Enables/Disables multi touch gestures.

---
trackpad(t): uint
    properties: create, query
    Sets the trackpad mode.  Values can be:

1 - Cursor Control only
2 - Multi-touch Gestures Only
3 - Cursor and Multi-touch

Note: this is a "Mac" only flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/multiTouch.html 
    """


def mute(flagdisable: boolean, flagforce: boolean) -> list[string]:
    """Synopsis:
---
---
 mute([disable=boolean], [force=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

mute is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Mute playback of the ry channel of ty on the sphere
---

sph = cmds.polySphere()
cmds.setKeyframe( '%s.translate' % sph[0] )
cmds.mute( '%s.translateY' % sph[0] )

Query whether ty is muted
cmds.mute('%s.translateY' % sph[0], q=True )

Disable muting on any muted attributes on the sphere
---

cmds.mute( sph[0], disable=True )

---
Return:
---


    list[string]: Name(s) of the mute node(s)

Flags:
---


---
disable(d): boolean
    properties: create
    Disable muting on the channels

---
force(f): boolean
    properties: create
    Forceable disable of muting on the channels. If there are keys on the mute channel,
the animation and mute node will both be removed.  If this flag is not set, then
mute nodes with animation will only be disabled.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/mute.html 
    """
