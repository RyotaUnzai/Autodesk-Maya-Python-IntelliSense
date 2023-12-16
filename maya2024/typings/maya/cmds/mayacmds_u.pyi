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


def ubercam() -> string:
    """Synopsis:
---
---
 ubercam([string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ubercam is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

camera = cmds.shot('myUbercam');

---
Return:
---


    string: Ubercam name

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ubercam.html 
    """


def uiTemplate(defineTemplate: string, exists: boolean, useTemplate: string) -> string:
    """Synopsis:
---
---
 uiTemplate(
[string]
    , [defineTemplate=string], [exists=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

uiTemplate is undoable, queryable, and editable.setUITemplate



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


    string: The name of the uiTemplate created.

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
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/uiTemplate.html 
    """


def unassignInputDevice(clutch: string, device: string) -> None:
    """Synopsis:
---
---
 unassignInputDevice([clutch=string], [device=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

unassignInputDevice is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

This deletes all command strings associated with the spaceball.
cmds.unassignInputDevice( d='spaceball' )

---


Flags:
---


---
clutch(c): string
    properties: create
    Only delete command attachments with this clutch.

---
device(d): string
    properties: create
    Specifies the device to work on.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/unassignInputDevice.html 
    """


def undo() -> None:
    """Synopsis:
---
---
 undo()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

undo is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

In this particular example, each line needs to be executed
separately one after the other. Executing lines separately
guaranties that commands are properly registered in the undo
stack.

cmds.polyCube()
Result: [u'pCube1', u'polyCube1'] ---


cmds.polySphere()
Result: [u'pSphere1', u'polySphere1'] ---


cmds.undo()
Undo: cmds.polySphere()
 ---


cmds.undo()
Undo: cmds.polyCube()
 ---


---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/undo.html 
    """


def undoInfo(chunkName: string, closeChunk: boolean, infinity: boolean, length: uint, openChunk: boolean, printQueue: boolean, printRedoQueue: boolean, redoName: string, redoQueueEmpty: boolean, state: boolean, stateWithoutFlush: boolean, undoName: string, undoQueueEmpty: boolean) -> int | string:
    """Synopsis:
---
---
 undoInfo([chunkName=string], [closeChunk=boolean], [infinity=boolean], [length=uint], [openChunk=boolean], [printQueue=boolean], [printRedoQueue=boolean], [redoName=string], [redoQueueEmpty=boolean], [state=boolean], [stateWithoutFlush=boolean], [undoName=string], [undoQueueEmpty=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

undoInfo is undoable, queryable, and NOT editable.
In query mode, if invoked without flags (other than the query flag), this
command will return the number of items currently on the undo queue.




Example:
---
import maya.cmds as cmds

Turn undo on, with an infinite queue length
cmds.undoInfo( state=True, infinity=True )
Turn undo on, with a queue length of 200
cmds.undoInfo( state=True, infinity=False, length=200 )
Turn undo off
cmds.undoInfo( state=False )
Query the queue length
cmds.undoInfo( q=True, length=True )
Query the number of items currently on the queue.
cmds.undoInfo( q=True )

---
Return:
---


    string: If querying undoName or redoName
    int: If querying state, infinity, or length

Flags:
---


---
chunkName(cn): string
    properties: create, query
    Sets the name used to identify a chunk for undo/redo
purposes when opening a chunk.

---
closeChunk(cck): boolean
    properties: create
    Closes the chunk that was opened earlier by openChunk.
Once close chunk is called, all undoable operations in the chunk
will undo as a single undo operation.
Use with CAUTION!! Improper use of this command can leave the
undo queue in a bad state.

---
infinity(infinity): boolean
    properties: create, query
    Set the queue length to infinity.

---
length(l): uint
    properties: create, query
    Specifies the maximum number of items in the undo queue.
The infinity flag overrides this one.

---
openChunk(ock): boolean
    properties: create
    Opens a chunk so that all undoable operations after this call
will fall into the newly opened chunk, until close chunk is called.
Once close chunk is called, all undoable operations in the chunk
will undo as a single undo operation.
Use with CAUTION!! Improper use of this command can leave the
undo queue in a bad state.

---
printQueue(pq): boolean
    properties: query
    Prints to the Script Editor the contents of the undo queue.

---
printRedoQueue(prq): boolean
    properties: query
    Prints to the Script Editor the contents of the redo queue.

---
redoName(rn): string
    properties: query
    Returns what will be redone (if anything)

---
redoQueueEmpty(rqe): boolean
    properties: query
    Return true if the redo queue is empty. Return false if
there is at least one command in the queue to be redone.

---
state(st): boolean
    properties: create, query
    Turns undo/redo on or off.

---
stateWithoutFlush(swf): boolean
    properties: create, query
    Turns undo/redo on or off without flushing the queue. Use with CAUTION!!
Note that if you  perform destructive operations while stateWithoutFlush is
disabled, and you then enable it again, subsequent undo operations that try
to go past the  destructive operations may be unstable since undo will
not be able to properly reconstruct the former state of the scene.

---
undoName(un): string
    properties: query
    Returns what will be undone (if anything)

---
undoQueueEmpty(uqe): boolean
    properties: query
    Return true if the undo queue is empty. Return false if
there is at least one command in the queue to be undone.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/undoInfo.html 
    """


def unfold(applyToShell: boolean, areaWeight: float, globalBlend: float, globalMethodBlend: float, iterations: int, optimizeAxis: int, pinSelected: boolean, pinUvBorder: boolean, scale: float, stoppingThreshold: float, useScale: boolean) -> int:
    """Synopsis:
---
---
 unfold([applyToShell=boolean], [areaWeight=float], [globalBlend=float], [globalMethodBlend=float], [iterations=int], [optimizeAxis=int], [pinSelected=boolean], [pinUvBorder=boolean], [scale=float], [stoppingThreshold=float], [useScale=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

unfold is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Create a sphere and select it.
cmds.polySphere()

Optimise the position of some Uvs
cmds.unfold( 'pSphere1.map[189:398]' )

---
Return:
---


    int: the number of relaxation iterations carried out

Flags:
---


---
applyToShell(applyToShell): boolean
    properties: create
    Specifies that the selected components should be only work on shells that
have something have been selected or pinned.

---
areaWeight(aw): float
    properties: create
    Surface driven importance. 0 treat all faces equal. 1 gives more importance to large ones.

---
globalBlend(gb): float
    properties: create
    This allows the user to blend between a local optimization method
(globalBlend = 0.0) and a global optimization method
(globalBlend = 1.0). The local optimization method looks at the
ratio between the triangles on the object and the triangles in UV
space.  It has a side affect that it can sometimes introduce tapering
problems.  The global optimization is much slower, but takes into
consideration the entire object when optimizing uv placement.

---
globalMethodBlend(gmb): float
    properties: create
    The global optimization method uses two functions to compute
a minimization.  The first function controls edge
stretch by using edges lengths between xyz and uv.  The second
function penalizes the first function by preventing
configurations where triangles would overlap.  For every surface
there is a mix between these two functions that will give the
appropriate response. Values closer to 1.0 give more weight to
the edge length function. Values closer to 0.0 give more weight to
surface area.  The default value of '0.5' is a even mix
between these two values.

---
iterations(i): int
    properties: create
    Maximum number of iterations for each connected UV piece.

---
optimizeAxis(oa): int
    properties: create
    Degree of freedom for optimization
0=Optimize freely, 1=Move vertically only, 2=Move horzontally only

---
pinSelected(ps): boolean
    properties: create
    Specifies that the selected components should be pinned instead
the unselected components.

---
pinUvBorder(pub): boolean
    properties: create
    Specifies that the UV border should be pinned when doing the solve.
By default only unselected components are pinned.

---
scale(s): float
    properties: create
    Ratio between 2d and 3d space.

---
stoppingThreshold(ss): float
    properties: create
    Minimum distorsion improvement between two steps in %.

---
useScale(us): boolean
    properties: create
    Adjust the scale or not.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/unfold.html 
    """


def ungroup(absolute: boolean, parent: string, relative: boolean, world: boolean) -> None:
    """Synopsis:
---
---
 ungroup(
[objects...]
    , [absolute=boolean], [parent=string], [relative=boolean], [world=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ungroup is undoable, NOT queryable, and NOT editable.
The objects will be placed at the same level in the hierarchy the
group node occupied unless the -w flag is specified, in which case
they will be placed under the world.

If an object is ungrouped and there is an object in the new group
with the same name then this command will rename the ungrouped
object.

See also: group, parent, instance, duplicate




Example:
---
import maya.cmds as cmds

Create a simple hierarchy
cmds.sphere( n='sphere1' )
cmds.move( 2, 0, 0 )
cmds.sphere( n='sphere2' )
cmds.move( -2, 0, 0 )
cmds.group( 'sphere1', 'sphere2', n='group1' )
cmds.move( 0, 2, 0 )
cmds.sphere( n='sphere3' )
cmds.move( 0, 0, 2 )
cmds.group( 'group1', 'sphere3', n='group2' )
cmds.group( em=True, n='group3' )

Remove group1 from the hierarchy. What should remain
is group2 with sphere3, sphere1, and sphere2 as children.
Note that the objects don't move since the absolute flag
is implied.
---

cmds.ungroup( 'group1' )

Try the same ungroup with the -relative flag.
Now sphere1 and sphere2 will move down 2 units in Y.
---

cmds.undo()
cmds.ungroup( 'group1', relative=True )

Now try the same ungroup operation with the -parent flag.
This will move the children of group1 under group3.
cmds.undo()
cmds.ungroup( 'group1', parent='group3' )

---


Flags:
---


---
absolute(a): boolean
    properties: create
    preserve existing world object transformations
(overall object transformation is preserved
by modifying the objects local transformation)
[default]

---
parent(p): string
    properties: create
    put the ungrouped objects under the given parent

---
relative(r): boolean
    properties: create
    preserve existing local object transformations
(don't modify local transformation)

---
world(w): boolean
    properties: create
    put the ungrouped objects under the world

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ungroup.html 
    """


def uniform(attenuation: float, directionX: float, directionY: float, directionZ: float, magnitude: float, maxDistance: linear, name: string, perVertex: boolean, position: tuple[linear, linear, linear], torusSectionRadius: linear, volumeExclusion: boolean, volumeOffset: tuple[linear, linear, linear], volumeShape: string, volumeSweep: angle) -> string:
    """Synopsis:
---
---
 uniform(
selectionList
    , [attenuation=float], [directionX=float], [directionY=float], [directionZ=float], [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

uniform is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
A uniform field pushes objects in a fixed direction.  The field
strength, but not the field direction, depends on the distance
from the object to the field location.

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

cmds.uniform( dx=0, dy=1.0, dz=0.5 )
Creates a uniform field pushing in direction (0,1,0.5) for every
active selection. If there is no active selection, it creates this
field at world position (0,0,0).

cmds.uniform( 'uniformF', e=True, att=0.98 )
edits the acceleration value of the field uniformF
cmds.uniform( 'uniformF', q=True, att=1 )
queries uniformF for its acceleration value

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
directionX(dx): float
    properties: query, edit
    X-component of direction.

---
directionY(dy): float
    properties: query, edit
    Y-component of direction.

---
directionZ(dz): float
    properties: query, edit
    Z-component of direction

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/uniform.html 
    """


def unknownNode(plugin: boolean, realClassName: boolean, realClassTag: boolean) -> list[string]:
    """Synopsis:
---
---
 unknownNode([plugin=boolean], [realClassName=boolean], [realClassTag=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

unknownNode is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

query the unknown node's real class name
---

cmds.unknownNode( 'testIterator1', q=True, rcn=True )
Result: testIterator ---


query the unknown node's class IFF tag
if the node was loaded from a Maya ASCII file
---

cmds.unknownNode( 'testIterator1', q=True, rct=True )
Warning: line 1: No class tag available for node 'testIterator1'. ---

Result: 0 ---


if the node was loaded from a Maya Binary file
---

cmds.unknownNode( 'testIterator1', q=True, rct=True )
Result: 10 ---


query the plug-in that defined the unknown node
---

cmds.unknownNode( 'testIterator1', q=True, p=True )
Result: testIteratorNode ---


---
Return:
---


    list[string]: in query mode

Flags:
---


---
plugin(p): boolean
    properties: query
    In query mode return the name of the plug-in from which the unknown node originated.
If no plug-in then the empty string is returned.

---
realClassName(rcn): boolean
    properties: query
    Return the real class name of the node.

---
realClassTag(rct): boolean
    properties: query
    Return the real class IFF tag of the node.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/unknownNode.html 
    """


def unknownPlugin(dataTypes: boolean, list: boolean, nodeTypes: boolean, remove: boolean, version: boolean) -> list[string]:
    """Synopsis:
---
---
 unknownPlugin([dataTypes=boolean], [list=boolean], [nodeTypes=boolean], [remove=boolean], [version=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

unknownPlugin is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

list the unknown plug-ins
---

cmds.unknownPlugin( q=True, l=True )
Result: foo ---


query the version of the unknown plug-in
---

cmds.unknownPlugin( "foo", q=True, v=True )
Result: 1.0 ---


attempt to remove the unknown plug-in
---

cmds.unknownPlugin( "foo", r=True )

---
Return:
---


    list[string]: in query mode

Flags:
---


---
dataTypes(dt): boolean
    properties: query
    Returns the data types associated with the given unknown plug-in.
This will always be empty for pre-Maya 2014 files.

---
list(l): boolean
    properties: query
    Lists the unknown plug-ins in the scene.

---
nodeTypes(nt): boolean
    properties: query
    Returns the node types associated with the given unknown plug-in.
This will always be empty for pre-Maya 2014 files.

---
remove(r): boolean
    properties: create
    Removes the given unknown plug-in from the scene.
For Maya 2014 files and onwards, this will fail if node
or data types defined by the plug-in are still in use.

---
version(v): boolean
    properties: query
    Returns the version string of the given unknown plug-in.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/unknownPlugin.html 
    """


def unloadPlugin(addCallback: script, force: boolean, removeCallback: script) -> list[string]:
    """Synopsis:
---
---
 unloadPlugin(
string [string...]
    , [addCallback=script], [force=boolean], [removeCallback=script])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

unloadPlugin is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Unload the plugin that has the internal name "newNode"
---

cmds.unloadPlugin( 'newNode.py' )

---
Return:
---


    list[string]: the internal names of the successfully unloaded plug-ins

Flags:
---


---
addCallback(ac): script
    properties: create
    Add a procedure to be called just before a plugin is
unloaded. The procedure should have one string argument, which
will be the plugin's name.

---
force(f): boolean
    properties: create
    Unload the plugin even if it is providing services.  This
is not recommended.  If you unload a plug-in that implements
a node or data type in the scene, those instances will be
converted to unknown nodes or data and the scene will no
longer behave properly. Maya may become unstable or even
crash. If you use this flag you are advised to save your scene
in MayaAscii format and restart Maya as soon as possible.

---
removeCallback(rc): script
    properties: create
    Remove a procedure which was previously added
with -addCallback.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/unloadPlugin.html 
    """


def untangleUV(mapBorder: string, maxRelaxIterations: int, pinBorder: boolean, pinSelected: boolean, pinUnselected: boolean, relax: string, relaxTolerance: float, shapeDetail: float) -> int:
    """Synopsis:
---
---
 untangleUV([mapBorder=string], [maxRelaxIterations=int], [pinBorder=boolean], [pinSelected=boolean], [pinUnselected=boolean], [relax=string], [relaxTolerance=float], [shapeDetail=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

untangleUV is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.untangleUV( mb='shape_square' )
map the border associated with the selected UV trying to retain the
shape of the object and use a square mapping to iron out crossings

cmds.untangleUV( r='one_over_length', pb=True, ps=False, pu=False, rt=0.1 )
relax the shell associated with the selected UV using edge weights
that are inversely proportional to length of world space lengths
pin the UV on borders and use a tolerance of 0.1

---
Return:
---


    int: the number of relaxation iterations carried out

Flags:
---


---
mapBorder(mb): string
    properties: create
    Map the border containing the selected UV into a variety of shapes that may
be more amenable to UV relaxation operations. There are various types of
mapping available. All the resulting mappings are fit inside the unit square.

Valid values for the STRING are:
circular - a circular mapping with picked UV closest to (0,0)
square - map to unit square with picked UV at (0,0)
shape - a mapping which attempts to reflect the actual shape of the object
        where the picked UV is placed on the line from (0,0) -> (0.5,0.5)
shape_circular - shape mapping which will interpolate to a circular mapping
                 just enough to prevent self-intersections of the mapped border 
shape_square - shape mapping which will interpolate to a square mapping just
               enough to prevent self-intersections of the mapped border

---
maxRelaxIterations(mri): int
    properties: create
    The relaxation process is an iterative algorithm. Using this flag
will put an upper limit on the number of iterations that will be
performed.

---
pinBorder(pb): boolean
    properties: create
    If this is true, then the relevant texture borders are pinned in
place during any relaxation

---
pinSelected(ps): boolean
    properties: create
    If this is true, then then any selected UVs are pinned in
place during any relaxation

---
pinUnselected(pu): boolean
    properties: create
    If this is true, then all unselected UVs in each mesh are pinned in
place during any relaxation

---
relax(r): string
    properties: create
    Relax all UVs in the shell of the selected UV's. The relaxation is done by
simulating a spring system where each UV edge is treated as a spring.
There are a number of different methods characterized by the way the UV
edges are weighted in the spring system. These weightings are determined by
STRING. Valid values for STRING are:
uniform - every edge is weighted the same. This is the fastest method.
inverse_length - every edge weight is inversely proportional to it's world space length.
inverse_sqrt_length - every edge weight is inversely proportional the the square root of it's world space length.
harmonic - this weighting can yield near optimal results in matching the UV's with
the geometry, but can also take a long time.

---
relaxTolerance(rt): float
    properties: create
    This sets the tolerance which is used to determine when the
relaxation process can stop. Smaller tolerances yield better
results but can take much longer.

---
shapeDetail(sd): float
    properties: create
    If the mapBorder flag is set to circular or square, then this flag
will control how much of the border's corresponding surface shape
should be retained in the final mapped border.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/untangleUV.html 
    """


def untrim(caching: boolean, constructionHistory: boolean, curveOnSurface: boolean, name: string, noChanges: boolean, nodeState: int, object: boolean, replaceOriginal: boolean, untrimAll: boolean) -> list[string]:
    """Synopsis:
---
---
 untrim(
surface
    , [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [name=string], [noChanges=boolean], [nodeState=int], [object=boolean], [replaceOriginal=boolean], [untrimAll=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

untrim is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Untrim surface with history.
cmds.untrim( 'surface', ch=True )

Untrims surface without history.
cmds.untrim( 'surface', ch=False )

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
noChanges(nc): boolean
    properties: create, query, edit
    If set then the operation node will be automatically put into pass-through mode.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

---
untrimAll(all): boolean
    properties: query, edit
    if true, untrim all the trims for the surface else untrim
only the last trim

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/untrim.html 
    """


def upAxis(axis: string, rotateView: boolean) -> None:
    """Synopsis:
---
---
 upAxis([axis=string], [rotateView=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

upAxis is undoable, queryable, and NOT editable.

By default, the ground plane in Maya is on the XY plane.
Hence, the default up-direction is the direction of the positive Z-axis.

The -ax flag is mandatory. In conjunction with the -ax flag,
when the -rv flag is specified, the camera of currently active view is
revolved about the X-axis such that the position of the groundplane in
the view will remain the same as before the the up direction is changed.

The screen update is applied to all cameras of all views.




Example:
---
import maya.cmds as cmds

1. to make the Y-axis of the world to be the up axis:
cmds.upAxis( ax='y' )

2. to make the Z-axis of the world to be the up axis,
and rotate the view:
cmds.upAxis( ax='z', rv=True )

3. to query which axis is the current up axis
(returns a string: a "y" or a "z"):
cmds.upAxis( q=True, axis=True )

---


Flags:
---


---
axis(ax): string
    properties: query
    This flag specifies the axis as the world up direction.
The valid axis are either "y" or "z".
When queried, it returns a string.

---
rotateView(rv): boolean
    properties: create
    This flag specifies to rotate the view as well.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/upAxis.html 
    """


def uvLink(b: boolean, isValid: boolean, make: boolean, queryObject: name, texture: name, uvSet: name) -> string:
    """Synopsis:
---
---
 uvLink(
[objects]
    , [b=boolean], [isValid=boolean], [make=boolean], [queryObject=name], [texture=name], [uvSet=name])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

uvLink is undoable, queryable, and NOT editable.
If no make, break or query flag is specified and both uvSet and
texture flags are present, the make flag is assumed to be specified.

If no make, break or query flag is specified and only one of the
uvSet and texture flags is present, the query flag is assumed to be
specified.

The term "texture" in the context of UV linking is a bit of an
oversimplification. In fact, UV sets can be linked to any node which
takes UV coordinates as input. However in most cases it will be a
texture to which you wish to link a UV set.




Example:
---
import maya.cmds as cmds

cmds.uvLink( uvSet='pSphereShape1.uvSet[2].uvSetName', texture='checker1' )
causes a UV link to be created between uvSet[2] on pSphereShape1
and the checker1 texture.
Note that no make, break or query flag is specified so make is
assumed since both uvSet and texture are specified.

cmds.uvLink( make=True, uvSet='pCubeShape2.uvSet[0].uvSetName', texture='file8' )
causes a UV link to be created between uvSet[0] of pCubeShape2 and
the file8 file texture.

cmds.uvLink( uvSet='pCubeShape2.uvSet[0].uvSetName', texture='file8' )
causes a UV link to be created between uvSet[0] of pCubeShape2 and
the file8 file texture. Note: no make, break or query flag is
specified so the make flag is assumed since both uvSet
and texture are specified.

cmds.uvLink( query=True, uvSet='pCubeShape2.uvSet[0].uvSetName' )
will return a string array of textures which use the UV set
pCubeShape2.uvSet[0].setName. For example, the return value might
be:
file8 file9 checker4 slimeMap

cmds.uvLink( query=True, texture='checker4' )
will return a string array of the UV sets that are used by the
texture. For example, the return value might be
pCubeShape2.uvSet[0].setName pCylinderShape1.uvSet[4].setName
pCylinderShape2.uvSet[3].setName

cmds.uvLink( texture='checker4' )
will return a string array of the UV sets that are used by the
texture. For example, the return value might be
pCubeShape2.uvSet[0].setName pCylinderShape1.uvSet[4].setName
pCylinderShape2.uvSet[3].setName
Note that no make, break or query flag is specified, so query is
assumed since no uvSet was specified.

cmds.uvLink( b=True, uvSet='pCylinderShape2.uvSet[3].uvSetName', texture='checker4' )
causes the checker4 texture to no longer use the UV set
pCylinderShape2.uvSet[3].setName.
The texture will use the default UV set on pCylinderShape2 instead.
If checker4 wasn't using pCylinderShape2.uvSet[3].setName,
nothing changes and a warning is produced.

cmds.uvLink( isValid=True, texture='myTexture' )
Returns true if myTexture is a texture to which a UV set can be
linked, or false otherwise.

myPlug = getSomePlugFromSomewhere()
cmds.uvLink( isValid=True, uvSet=myPlug )
Returns true if $myPlug is a UV set, or false otherwise.

---
Return:
---


    string: or array of strings for query
boolean for isValid

Flags:
---


---
b(b): boolean
    properties: create
    The presence of this flag on the command indicates that the
command is being invoked to break links between UV sets and
textures.

---
isValid(iv): boolean
    properties: create
    This flag is used to verify whether or not a texture or UV set is
valid for the purposes of UV linking. It should be used in
conjunction with either the -texture flag or the -uvSet flag, but
not both at the same time.

---
make(m): boolean
    properties: create
    The presence of this flag on the command indicates that the
command is being invoked to make links between UV sets and
textures.

---
queryObject(qo): name
    properties: create
    This flag should only be used in conjunction with a query of a
texture. This flag is used to indicate that the results of the
query should be limited to UV sets of the object specified by this
flag.

---
texture(t): name
    properties: create
    The argument to the texture flag specifies the texture to be used by
the command in performing the action.

---
uvSet(uvs): name
    properties: create
    The argument to the uvSet flag specifies the UV set to be used by
the command in performing the action.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/uvLink.html 
    """


def uvSnapshot(antiAliased: boolean, blueColor: int, entireUVRange: boolean, fileFormat: string, greenColor: int, name: string, overwrite: boolean, redColor: int, uMax: float, uMin: float, uvSetName: string, vMax: float, vMin: float, xResolution: int, yResolution: int) -> None:
    """Synopsis:
---
---
 uvSnapshot([antiAliased=boolean], [blueColor=int], [entireUVRange=boolean], [fileFormat=string], [greenColor=int], [name=string], [overwrite=boolean], [redColor=int], [uMax=float], [uMin=float], [uvSetName=string], [vMax=float], [vMin=float], [xResolution=int], [yResolution=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

uvSnapshot is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Create a polygonal sphere
cmds.polySphere()

Save the UVs in a image
cmds.uvSnapshot( o=True, n='/tmp/uvImage2.iff', xr=256, yr=256 )

---


Flags:
---


---
antiAliased(aa): boolean
    properties: create
    When this flag is set, lines are antialiased.

---
blueColor(b): int
    properties: create
    Blue component of line drawing. Default is 255.

---
entireUVRange(euv): boolean
    properties: create
    When this flag is set, the generated image will contain the entire uv range. Default is UV in 0-1 range.

---
fileFormat(ff): string
    properties: create
    Output file format. Any of those keyword:
                                "iff", "sgi", "pic", "tif", "als", "gif", "rla", "jpg"
        Default is iff.

---
greenColor(g): int
    properties: create
    Green component of line drawing. Default is 255.

---
name(n): string
    properties: create
    Name of the file to be created.

---
overwrite(o): boolean
    properties: create
    When this flag is set, existing file can be ovewritten.

---
redColor(r): int
    properties: create
    Red component of line drawing. Default is 255.

---
uMax(umx): float
    properties: create
    Optional User Specified Max value for U. Default value is 1. This will take precedence over the "entire range" -euv flag.

---
uMin(umn): float
    properties: create
    Optional User Specified Min value for U. Default value is 0. This will take precedence over the "entire range" -euv flag.

---
uvSetName(uvs): string
    properties: create
    Name of the uv set to use. Default is the current one.

---
vMax(vmx): float
    properties: create
    Optional User Specified Max value for V. Default value is 1. This will take precedence over the "entire range" -euv flag.

---
vMin(vmn): float
    properties: create
    Optional User Specified Min value for V. Default value is 0. This will take precedence over the "entire range" -euv flag.

---
xResolution(xr): int
    properties: create
    Horizontal size of the image. Default is 512.

---
yResolution(yr): int
    properties: create
    Vertical size of the image. Default is 512.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/uvSnapshot.html 
    """
