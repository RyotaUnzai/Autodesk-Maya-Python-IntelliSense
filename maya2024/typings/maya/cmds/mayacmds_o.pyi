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


def objExists() -> boolean:
    """Synopsis:
---
---
 objExists(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

objExists is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Select an object if and only if it exists.
Print a warning if it does not exist.
if cmds.objExists('surface1'):
  cmds.select('surface1')
else:
  print("Warning: no surface exists.")

---
Return:
---


    boolean: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/objExists.html 
    """


def objectCenter(gl: boolean, local: boolean, x: boolean, y: boolean, z: boolean) -> float | float[]:
    """Synopsis:
---
---
 objectCenter(
object
    , [gl=boolean], [local=boolean], [x=boolean], [y=boolean], [z=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

objectCenter is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

create a simple hierarchy
cmds.polyCube( name='a' )
cmds.polyCube( name='b' )
cmds.parent( 'b', 'a' )
cmds.move( 3, 0, 0, 'a', localSpace=True )
cmds.move( 2, 2, 2, 'b', localSpace=True )

X_COORD = cmds.objectCenter('b',x=True)
Result: 5 ---


Get the center of the bounding box of b in local space
XYZ = cmds.objectCenter('b', l=True)
Result: 2 2 2 ---


Get the center of the bounding box of b in world space
XYZ = cmds.objectCenter('b', gl=True)
Result: 5 2 2 ---


Get the center of the bounding box of a in world space
XYZ = cmds.objectCenter('a', gl=True)

---
Return:
---


    float[]: When the asking for the center (default).
    float: When asking for one coordinate only.

Flags:
---


---
gl(gl): boolean
    properties: create
    Return positional values in global coordinates (default).

---
local(l): boolean
    properties: create
    Return positional values in local coordinates.

---
x(x): boolean
    properties: create
    Return X value only

---
y(y): boolean
    properties: create
    Return Y value only

---
z(z): boolean
    properties: create
    Return Z value only

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/objectCenter.html 
    """


def objectType(isAType: string, isType: string, tagFromType: string, typeFromTag: int, typeTag: boolean) -> boolean | string:
    """Synopsis:
---
---
 objectType(
object
    , [isAType=string], [isType=string], [tagFromType=string], [typeFromTag=int], [typeTag=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

objectType is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

create an object to query type of
cmds.sphere( n='sphere1' )

To query the type of an object:
cmds.objectType( 'sphere1Shape' )
Result: nurbsSurface ---


To confirm that sphere1Shape really is a nurbs surface:
cmds.objectType( 'sphere1Shape', isType='nurbsSurface' )
Result: 1 ---


---
Return:
---


    string: The type of the specified object
    boolean: For "isType": was the object of the specified type?

Flags:
---


---
isAType(isa): string
    properties: create
    Returns true if the object is the specified type or derives
from an object that is of the specified type. This flag will
only work with dependency nodes.

---
isType(i): string
    properties: create
    Returns true if the object is exactly of the specified type.
False otherwise.

---
tagFromType(tgt): string
    properties: create
    Returns the type tag given a type name.

---
typeFromTag(tpt): int
    properties: create
    Returns the type name given an integer type tag.

---
typeTag(tt): boolean
    properties: create
    Returns an integer tag that is unique for that object type.  Not all
object types will have tags.  This is the unique 4-byte value that is
used to identify nodes of a given type in the binary file format.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/objectType.html 
    """


def objectTypeUI(isType: string, listAll: boolean, superClasses: boolean) -> string:
    """Synopsis:
---
---
 objectTypeUI(
string
    , [isType=string], [listAll=boolean], [superClasses=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

objectTypeUI is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

print(cmds.objectTypeUI( 'viewPanes' ))

show all commands as their types
import sys
for c,e in enumerate(cmds.objectTypeUI(listAll=True)):
    c += 1
    sys.stdout.write(e + " ")
    if c % 3 == 0:
        sys.stdout.write('\n')

show Qt inheritence hierachy for buttons
cmds.window()
cmds.rowColumnLayout()
b = cmds.button()
cmds.showWindow()
print(cmds.objectTypeUI(b,sc=True))

---
Return:
---


    string: The type of the specified object.

Flags:
---


---
isType(i): string
    properties: create
    Returns true|false if the object is of the specified type.

---
listAll(la): boolean
    properties: create
    Returns a list of all known UI commands and their respective types.
Each entry contains three strings which are the command name, ui type and class name.
Note that the class name is internal and is subject to change.

---
superClasses(sc): boolean
    properties: create
    Returns a list of the names of all super classes for the given object.
Note that all class names are internal and are subject to change.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/objectTypeUI.html 
    """


def offsetCurve(caching: boolean, connectBreaks: int, constructionHistory: boolean, cutLoop: boolean, cutRadius: linear, distance: linear, name: string, nodeState: int, normal: tuple[linear, linear, linear], object: boolean, range: boolean, reparameterize: boolean, stitch: boolean, subdivisionDensity: int, tolerance: linear, useGivenNormal: boolean) -> list[string]:
    """Synopsis:
---
---
 offsetCurve(
[curve]
    , [caching=boolean], [connectBreaks=int], [constructionHistory=boolean], [cutLoop=boolean], [cutRadius=linear], [distance=linear], [name=string], [nodeState=int], [normal=[linear, linear, linear]], [object=boolean], [range=boolean], [reparameterize=boolean], [stitch=boolean], [subdivisionDensity=int], [tolerance=linear], [useGivenNormal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

offsetCurve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

offset all active curves to the specified distance:
cmds.offsetCurve( d=4.0 )

create offsets for the specified curve and turn loop cutting off:
cmds.offsetCurve( 'curve1', cl=False)

create offsets with circular arcs at the breaks in the curve and use
a cutting radius of 2.0 if there are any loops in the offsets:
cmds.offsetCurve( 'curve1', cb=1, cl=True, cr=2.0 )

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
connectBreaks(cb): int
    properties: create, query, edit
    Connect breaks method (between gaps):
0 - off,
1 - circular,
2 - linear
Default: 2

---
cutLoop(cl): boolean
    properties: create, query, edit
    Do loop cutting.
Default: false

---
cutRadius(cr): linear
    properties: create, query, edit
    Loop cut radius. Only used if cutLoop attribute is set true.
Default: 0.0

---
distance(d): linear
    properties: create, query, edit
    Offset distance
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
normal(nr): [linear, linear, linear]
    properties: create, query, edit
    Offset plane normal

---
reparameterize(rp): boolean
    properties: create, query, edit
    Do reparameterization. It is not advisable to change this value.
Default: false

---
stitch(st): boolean
    properties: create, query, edit
    Stitch curve segments together. It is not advisable to change this value.
Default: true

---
subdivisionDensity(sd): int
    properties: create, query, edit
    Maximum subdivision density per span
Default: 5

---
tolerance(tol): linear
    properties: create, query, edit
    Tolerance
Default: 0.01

---
useGivenNormal(ugn): boolean
    properties: create, query, edit
    Use the given normal (or, alternativelly, geometry normal)
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
range(rn): boolean
    properties: create
    Force a curve range on complete input curve.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/offsetCurve.html 
    """


def offsetCurveOnSurface(caching: boolean, checkPoints: int, connectBreaks: int, constructionHistory: boolean, cutLoop: boolean, distance: linear, name: string, nodeState: int, object: boolean, range: boolean, stitch: boolean, subdivisionDensity: int, tolerance: linear) -> list[string]:
    """Synopsis:
---
---
 offsetCurveOnSurface(
[curve]
    , [caching=boolean], [checkPoints=int], [connectBreaks=int], [constructionHistory=boolean], [cutLoop=boolean], [distance=linear], [name=string], [nodeState=int], [object=boolean], [range=boolean], [stitch=boolean], [subdivisionDensity=int], [tolerance=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

offsetCurveOnSurface is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.nurbsPlane( ch=True, o=True, po=0, ax=(0, 1, 0), w=10, lr=2 )
cmds.circle( ch=True, o=True, nr=(0, 1, 0), r=3 )
cmds.projectCurve( 'nurbsCircle1', 'nurbsPlane1', ch=0, rn=False, un=False, tol=0.01 )

Offset given curve to the specified distance at the specified tolerance:
cmds.offsetCurveOnSurface( 'nurbsPlaneShape1->projectionCurve1_1', d=0.12, tol=0.02 )

Create offsets for the specified curve and turn loop cutting off:
cmds.offsetCurveOnSurface( 'nurbsPlaneShape1->projectionCurve1_1', cl=False )

Create offsets with circular arcs at the breaks in the curves and trim
away any loops in the offset curve:
cmds.offsetCurveOnSurface( 'nurbsPlaneShape1->projectionCurve1_1', cb=1, cl=False )

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
checkPoints(cp): int
    properties: create, query, edit
    Checkpoints for fit quality per span. Not advisable to change this value.
Default: 3

---
connectBreaks(cb): int
    properties: create, query, edit
    Connect breaks method (between gaps):
0 - off,
1 - circular,
2 - linear
Default: 2

---
cutLoop(cl): boolean
    properties: create, query, edit
    Do loop cutting.
Default: false

---
distance(d): linear
    properties: create, query, edit
    Offset distance
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
stitch(st): boolean
    properties: create, query, edit
    Stitch curve segments together. Not advisable to change this value.
Default: true

---
subdivisionDensity(sd): int
    properties: create, query, edit
    Maximum subdivision density per span
Default: 5

---
tolerance(tol): linear
    properties: create, query, edit
    Tolerance
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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/offsetCurveOnSurface.html 
    """


def offsetSurface(caching: boolean, constructionHistory: boolean, distance: linear, method: int, name: string, nodeState: int, object: boolean) -> list[string]:
    """Synopsis:
---
---
 offsetSurface(
[surface]
    , [caching=boolean], [constructionHistory=boolean], [distance=linear], [method=int], [name=string], [nodeState=int], [object=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

offsetSurface is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To offset the active surface to the specified distance:
cmds.offsetSurface( d=4.0 )

To create an offset using the surface fit offset method:
cmds.offsetSurface( 'surface1', m=0, d=2.0 )

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
distance(d): linear
    properties: create, query, edit
    Offset distance
Default: 1.0

---
method(m): int
    properties: create, query, edit
    Offset method
0 - Surface Fit
1 - CV Fit
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/offsetSurface.html 
    """


def ogs(deviceInformation: boolean, disposeReleasableTextures: boolean, dumpTexture: string, enableHardwareInstancing: boolean, fragmentEditor: string, fragmentXML: string, gpuMemoryTotal: int, gpuMemoryUsed: boolean, isLegacyViewportEnabled: boolean, isRemoteGLSessionEnabled: boolean, isWinRemoteSession: boolean, pause: boolean, rebakeTextures: boolean, regenerateUVTilePreview: string, reloadTextures: boolean, reset: boolean, shaderSource: string, toggleTexturePaging: boolean, traceRenderPipeline: boolean) -> string:
    """Synopsis:
---
---
 ogs([deviceInformation=boolean], [disposeReleasableTextures=boolean], [dumpTexture=string], [enableHardwareInstancing=boolean], [fragmentEditor=string], [fragmentXML=string], [gpuMemoryTotal=int], [gpuMemoryUsed=boolean], [isLegacyViewportEnabled=boolean], [isRemoteGLSessionEnabled=boolean], [isWinRemoteSession=boolean], [pause=boolean], [rebakeTextures=boolean], [regenerateUVTilePreview=string], [reloadTextures=boolean], [reset=boolean], [shaderSource=string], [toggleTexturePaging=boolean], [traceRenderPipeline=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ogs is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

// Reset the database for all panels running the OGS renderer.
// Returns the number of panels affected.
cmds.ogs( reset=True )
// Result: [modelPanel1] //

// Set the gpu memory limit to 2048 MB.  Memory management systems
// will attempt to avoid going over this limit.  Can be used to reserve
// memory for other applications.
cmds.ogs( gpuMemoryTotal=2048 )

// Output the current gpu memory limit in MB.
cmds.ogs( query=True, gpuMemoryTotal=True )

// Output an estimate of the amount of currently allocated gpu memory by
// Maya in MB.
cmds.ogs( gpu=True )

---
Return:
---


    string: Result of the operation

Flags:
---


---
deviceInformation(di): boolean
    properties: create
    If used then output the current device information.

---
disposeReleasableTextures(drt): boolean
    properties: create
    Clear up all the releasable file textures in GPU memory that are not required for rendering.

---
dumpTexture(dt): string
    properties: create
    If used then dump GPU texture memory usage info (in MB), must be used with FLAG gpuMemoryUsed.
The final info detail is specified by the string parameter. Current available values are: "full" , "total".

---
enableHardwareInstancing(hwi): boolean
    properties: create
    Enables/disables new gpu instancing of instanceable render items in OGS.

---
fragmentEditor(fe): string
    properties: create
    If used then launch the fragment editor UI.

---
fragmentXML(xml): string
    properties: create
    Get the fragment XML associated with a shading node.

---
gpuMemoryTotal(gmt): int
    properties: create, query
    Get or set the total amount of GPU memory which Maya is allowed to use (in MB).

---
gpuMemoryUsed(gpu): boolean
    properties: create
    If used then output the estimated amount of GPU memory in use (in MB).

---
isLegacyViewportEnabled(lve): boolean
    properties: query
    To query if the legacy viewport is enabled.

---
isRemoteGLSessionEnabled(rgl): boolean
    properties: query
    Query if remote gl is allowed

---
isWinRemoteSession(irs): boolean
    properties: query
    Query if this is a remote session.

---
pause(p): boolean
    properties: create, query
    Toggle pausing VP2 display update

---
rebakeTextures(rbt): boolean
    properties: create
    If used then re-bake all baked textures for OGS.

---
regenerateUVTilePreview(rup): string
    properties: create
    If used then regenerate all UV tiles preview textures for OGS.

---
reloadTextures(rlt): boolean
    properties: create
    If used then reload all textures for OGS.

---
reset(r): boolean
    properties: create, query
    If used then reset the entire OGS database for all viewports using it.
In query mode the number of viewports that would be affected is returned
but the reset is not actually done.  If no viewport is using OGS then
OGS will stop listening to DG changes.

---
shaderSource(ss): string
    properties: query
    Get the shader source for the specified material.

---
toggleTexturePaging(ttp): boolean
    properties: create
    If used then toggle the default OGS Texture paging mechanism.

---
traceRenderPipeline(trp): boolean
    properties: create
    Enable debug tracing of the renderer pipeline.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ogs.html 
    """


def ogsRender(activeMultisampleType: string, activeRenderOverride: string, activeRenderTargetFormat: string, availableFloatingPointTargetFormat: boolean, availableMultisampleType: boolean, availableRenderOverrides: boolean, camera: string, currentFrame: boolean, currentView: boolean, enableFloatingPointRenderTarget: boolean, enableMultisample: boolean, frame: float, height: uint, layer: name, noRenderView: boolean, width: uint) -> boolean:
    """Synopsis:
---
---
 ogsRender([activeMultisampleType=string], [activeRenderOverride=string], [activeRenderTargetFormat=string], [availableFloatingPointTargetFormat=boolean], [availableMultisampleType=boolean], [availableRenderOverrides=boolean], [camera=string], [currentFrame=boolean], [currentView=boolean], [enableFloatingPointRenderTarget=boolean], [enableMultisample=boolean], [frame=float], [height=uint], [layer=name], [noRenderView=boolean], [width=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ogsRender is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a poly sphere.
cmds.polySphere()

Render it
It will try to save the image with format according
to the file name saved in render globals.
cmds.ogsRender(w=480,h=270)
cmds.ogsRender(w=480,h=270)

---
Return:
---


    boolean: Query result

Flags:
---


---
activeMultisampleType(mst): string
    properties: query, edit
    Query the current active multisample type.

---
activeRenderOverride(cro): string
    properties: query, edit
    Set or query the current active render override.

---
activeRenderTargetFormat(fpt): string
    properties: query, edit
    Query the current active floating point target format.

---
availableFloatingPointTargetFormat(afp): boolean
    properties: query
    Returns the names of available floating point render target format.

---
availableMultisampleType(amt): boolean
    properties: query
    Returns the names of available multisample type.

---
availableRenderOverrides(aro): boolean
    properties: query
    Returns the names of available render overrides.

---
camera(cam): string
    properties: create, query, edit
    Specify the camera to use.  Use the first available camera if the camera
given is not found.

---
currentFrame(cf): boolean
    properties: create, query, edit
    Render the current frame.

---
currentView(cv): boolean
    properties: create, query, edit
    When turned on, only the current view will be rendered.

---
enableFloatingPointRenderTarget(efp): boolean
    properties: query, edit
    Enable/disable floating point render target.

---
enableMultisample(ems): boolean
    properties: query, edit
    Enable/disable multisample.

---
frame(f): float
    properties: create, edit
    Specify the frame to render.

---
height(h): uint
    properties: create, query, edit
    The height flag pass the height to the ogsRender command. If not used,
the height is taken from the render globals settings.

---
layer(l): name
    properties: create, query, edit
    Render the specified legacy render layer.
Only this render layer will be rendered,
regardless of the renderable attribute value of the render layer.
The layer name will be appended to the output image file name.
The specified render layer becomes the current render layer before rendering,
and remains as current render layer after the rendering.
This argument uses legacy render layers as this command does not recognize the newer
renderSetup render layer system introduced in Maya 2016.

---
noRenderView(nrv): boolean
    properties: create, query, edit
    When turned on, the render view is not updated after image computation

---
width(w): uint
    properties: create, query, edit
    The width flag pass the width to the ogsRender command. If not used,
the width is taken from the render globals settings.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ogsRender.html 
    """


def openCLInfo(limitMinimumVerts: boolean, minVertexBuffer: int, supportsDoublePrecision: boolean, valid: boolean) -> boolean:
    """Synopsis:
---
---
 openCLInfo([limitMinimumVerts=boolean], [minVertexBuffer=int], [supportsDoublePrecision=boolean], [valid=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

openCLInfo is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Query if OpenCL is initialized or not
cmds.openCLInfo(query=True, valid=True)
Result: True ---


Set the minimum vertex buffer size
cmds.openCLInfo(mvb=2000)

Query the minimum vertex buffer size
cmds.openCLInfo(query=True, mvb=True)
Result: 2000 ---


Query whether double precision is supported or not
cmds.openCLInfo(query=True, dbl=True)
Result: True ---


---
Return:
---


    boolean: The state of whether OpenCL is initialized or not (with the 'valid' flag)

Flags:
---


---
limitMinimumVerts(lmv): boolean
    properties: create, query
    Specifies whether the limit on the minimum vert count of the geometry is used or not. The system configuration
determines a certain minimum size for geometries to be allowed on GPU.
When this flag is on this limit is obeyed. When this flag is off this limit is ignored.
This is only used for debugging purposes and is not saved to the file or any preferences.

---
minVertexBuffer(mvb): int
    properties: create, query
    Set the minimum vert count under which the geometry will not be allowed on the GPU (unless in a network
with qualifying geometries).
This is only used for debugging purposes and is not saved to the file or any preferences.

---
supportsDoublePrecision(dbl): boolean
    properties: create, query
    Specifies whether double precision can be used in OpenCL. If the platform can not
allow double precision this can not be set to "on".

---
valid(v): boolean
    properties: query
    Valid in query mode only. Checks if OpenCL is initialized.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/openCLInfo.html 
    """


def openGLExtension(extension: string, renderer: boolean, vendor: boolean, version: boolean) -> string:
    """Synopsis:
---
---
 openGLExtension([extension=string], [renderer=boolean], [vendor=boolean], [version=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

openGLExtension is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Query for the multitexturing extension GL_ARB_multitexture
cmds.openGLExtension( extension='GL_ARB_multitexture' )

Query for all the extensions
cmds.openGLExtension( extension='' )

Query for the renderer name
cmds.openGLExtension( renderer=True )

Query for the vendor
cmds.openGLExtension( vendor=True )

Query for the OpenGL version
cmds.openGLExtension( version=True )

---
Return:
---


    string: The supported string(s)

Flags:
---


---
extension(ext): string
    properties: create
    Specifies the OpenGL extension to query.

---
renderer(rnd): boolean
    properties: create
    Specifies to query the OpenGL renderer.

---
vendor(vnd): boolean
    properties: create
    Specifies to query the company responsible for the OpenGL implementation.

---
version(ver): boolean
    properties: create
    Specifies to query the OpenGL version.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/openGLExtension.html 
    """


def openMayaPref(errlog: boolean, lazyLoad: boolean, oldPluginWarning: boolean) -> int:
    """Synopsis:
---
---
 openMayaPref([errlog=boolean], [lazyLoad=boolean], [oldPluginWarning=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

openMayaPref is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Enable RTLD_LAZY binding when loading plug-ins
cmds.openMayaPref( lz=True )

Force RTLD_NOW binding when loading plug-ins
cmds.openMayaPref( lz=False )

Disable the warning about old plug-ins being loaded
cmds.openMayaPref( ow=False )

Turn on the Error log
cmds.openMayaPref( errlog=True )

Query the Error log
cmds.openMayaPref( q=True, errlog=True )

Turn off the Error log
cmds.openMayaPref( errlog=False )

---
Return:
---


    int: indicates success or failure

Flags:
---


---
errlog(el): boolean
    properties: create, query, edit
    toggles whether or not an error log of failed API method
calls will be created.  When set to true, a file called
"OpenMayaErrorLog" will be created in Maya's current working
directory.  Each time an API method fails, a detailed
description of the error will be written to the file along
with a mini-stack trace that indicates the routine that
called the failing method.
Defaults to false(off).

---
lazyLoad(lz): boolean
    properties: create, query, edit
    toggles whether or not plugins will be loaded with
the RTLD_NOW flag or the RTLD_LAZY flag of dlopen(3C).  If
set to true, RTLD_LAZY will be used.  In this mode references
to functions that cannot be resolved at load time will not be
considered an error.  However, if one of these symbols is
actually dereferenced by the plug-in at run time, Maya will crash.
Defaults to false(off).

---
oldPluginWarning(ow): boolean
    properties: create, query, edit
    toggles whether or not loadPlugin will generate a
warning when plug-ins are loaded that were compiled against
an older, and possibly incompatible Maya release.
Defaults to true(on).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/openMayaPref.html 
    """


def optionMenu(alwaysCallChangeCommand: boolean, annotation: string, backgroundColor: tuple[float, float, float], beforeShowPopup: script, changeCommand: script, defineTemplate: string, deleteAllItems: boolean, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, itemListLong: boolean, itemListShort: boolean, label: string, manage: boolean, maxVisibleItems: int, noBackground: boolean, numberOfItems: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, postMenuCommand: script, postMenuCommandOnce: boolean, preventOverride: boolean, select: int, statusBarMessage: string, useTemplate: string, value: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 optionMenu(
[string]
    , [alwaysCallChangeCommand=boolean], [annotation=string], [backgroundColor=[float, float, float]], [beforeShowPopup=script], [changeCommand=script], [defineTemplate=string], [deleteAllItems=boolean], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [itemListLong=boolean], [itemListShort=boolean], [label=string], [manage=boolean], [maxVisibleItems=int], [noBackground=boolean], [numberOfItems=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [postMenuCommand=script], [postMenuCommandOnce=boolean], [preventOverride=boolean], [select=int], [statusBarMessage=string], [useTemplate=string], [value=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

optionMenu is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

def printNewMenuItem( item ):
        print item

window = cmds.window()
cmds.columnLayout()
cmds.optionMenu( label='Colors', changeCommand=printNewMenuItem )
cmds.menuItem( label='Yellow' )
cmds.menuItem( label='Purple' )
cmds.menuItem( label='Orange' )
cmds.showWindow( window )

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
alwaysCallChangeCommand(acc): boolean
    properties: create, query
    Toggle whether to always call the change command, regardless of the change.

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
beforeShowPopup(bsp): script
    properties: create, edit
    Callback that is called just before we show the drop down menu.

---
changeCommand(cc): script
    properties: create, edit
    Adds a callback that is called when a new item is selected.

The MEL script will have the newly selected item's value substituted for #1.

For Python, the callback should be a callable object which accepts one argument,
which is the newly selected item's value.

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
    properties: edit
    Delete all the items in this menu.

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
itemListLong(ill): boolean
    properties: query
    The long names of the menu items.

---
itemListShort(ils): boolean
    properties: query
    The short names of the menu items.

---
label(l): string
    properties: create, query, edit
    The optional label text to the left of the popup menu.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxVisibleItems(mvi): int
    properties: create, query, edit
    The maximum number of items that are visible in the popup menu.
If the popup contains more items than this, a scrollbar is added automatically.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfItems(ni): boolean
    properties: query
    The number of menu items.

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
    Specify a script to be executed when the popup menu is about
to be shown.

---
postMenuCommandOnce(pmo): boolean
    properties: create, query, edit
    Indicate the -pmc/postMenuCommand should only be
invoked once.  Default value is false, ie.
the -pmc/postMenuCommand is invoked every time the popup menu is
shown.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
select(sl): int
    properties: create, query, edit
    The current menu item.  The argument and return value
is 1-based.  Note that the current menu item can only be set if it
is enabled.

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
value(v): string
    properties: create, query, edit
    The text of the current menu item.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/optionMenu.html 
    """


def optionMenuGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, backgroundColor: tuple[float, float, float], changeCommand: script, columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, deleteAllItems: boolean, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, extraLabel: string, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, itemListLong: boolean, itemListShort: boolean, label: string, manage: boolean, noBackground: boolean, numberOfItems: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, postMenuCommand: script, postMenuCommandOnce: boolean, preventOverride: boolean, rowAttach: tuple[int, string, int], select: int, statusBarMessage: string, useTemplate: string, value: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 optionMenuGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [deleteAllItems=boolean], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [itemListLong=boolean], [itemListShort=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfItems=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [postMenuCommand=script], [postMenuCommandOnce=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [select=int], [statusBarMessage=string], [useTemplate=string], [value=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

optionMenuGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label text, option
menu and an extra label.  Both the label and extra label are optional.
Subsequent calls to the menuItem command will place them in the option
menu.  When adding menu items to the option menu after the initialization
step, use the name of the options menu itself. See the example below for
more details. Note that commands attached to menu items will not get called.
Use the -cc/changedCommand flag to be notified when the user
changes the value of the option menu.




Example:
---
import maya.cmds as cmds

   Create a window with two option menu groups.
---

window = cmds.window( title='Example 1' )
cmds.columnLayout()

   Create a couple of option menu groups.
---

colors = cmds.optionMenuGrp(label='Colors')
cmds.menuItem( label='Red' )
cmds.menuItem( label='Green' )
cmds.optionMenuGrp( l='Position' )
cmds.menuItem( label='Left' )
cmds.menuItem( label='Center' )
cmds.menuItem( label='Right' )

   Now add an additional item to the first option menu.
---

cmds.menuItem(parent=(colors +'|OptionMenu'), label='Blue' )
cmds.showWindow( window )

   Create another window with an option menu group.
---

window = cmds.window( title='Example 2' )
cmds.columnLayout()
cmds.optionMenuGrp( label='Size', extraLabel='cm', columnWidth=(2, 80) )
cmds.menuItem( label='10' )
cmds.menuItem( label='100' )
cmds.menuItem( label='1000' )
cmds.showWindow( window )

---
Return:
---


    string: The full name of the control on creation.

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
    Command executed when a new item is selected.

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
deleteAllItems(dai): boolean
    properties: edit
    Delete all the items in this menu.

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
extraLabel(el): string
    properties: create, query, edit
    If present on creation this specifies that there will be
an extra label to the right of the option menu.  Sets the string
to be the extra label text.

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
itemListLong(ill): boolean
    properties: query
    Returns the long names of the items.

---
itemListShort(ils): boolean
    properties: query
    Returns the short names of the items.

---
label(l): string
    properties: create, query, edit
    If present on creation this specifies that there will be
a label to the left of the option menu.  Sets the string to be
the label text.

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
    Returns the number of items.

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
    Specify a script to be executed when the popup menu is about
to be shown.

---
postMenuCommandOnce(pmo): boolean
    properties: create, query, edit
    Indicate the -pmc/postMenuCommand should only be
invoked once.  Default value is false, ie.
the -pmc/postMenuCommand is invoked every time the popup menu is
shown.

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
    Selects an item by index.  The first item is 1.

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
value(v): string
    properties: create, query, edit
    Select an item by value.  Also, returns the text of the
currently selected item.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/optionMenuGrp.html 
    """


def optionVar(arraySize: string, category: string, clearArray: string, clearStash: string, default: boolean, exists: string, floatArray: string, floatValue: tuple[string, float], floatValue2: tuple[string, float, float], floatValue3: tuple[string, float, float, float], floatValue4: tuple[string, float, float, float, float], floatValueAppend: tuple[string, float], init: boolean, intArray: string, intValue: tuple[string, int], intValue2: tuple[string, int, int], intValue3: tuple[string, int, int, int], intValue4: tuple[string, int, int, int, int], intValueAppend: tuple[string, int], list: boolean, listCategories: boolean, listModified: boolean, prefFile: string, remove: string, removeFromArray: tuple[string, int], stash: string, stringArray: string, stringValue: tuple[string, string], stringValueAppend: tuple[string, string], transient: boolean, unstash: string, version: int) -> int | list[string]:
    """Synopsis:
---
---
 optionVar([arraySize=string], [category=string], [clearArray=string], [clearStash=string], [default=boolean], [exists=string], [floatArray=string], [floatValue=[string, float]], [floatValue2=[string, float, float]], [floatValue3=[string, float, float, float]], [floatValue4=[string, float, float, float, float]], [floatValueAppend=[string, float]], [init=boolean], [intArray=string], [intValue=[string, int]], [intValue2=[string, int, int]], [intValue3=[string, int, int, int]], [intValue4=[string, int, int, int, int]], [intValueAppend=[string, int]], [list=boolean], [listCategories=boolean], [listModified=boolean], [prefFile=string], [remove=string], [removeFromArray=[string, int]], [stash=string], [stringArray=string], [stringValue=[string, string]], [stringValueAppend=[string, string]], [transient=boolean], [unstash=string], [version=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

optionVar is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.optionVar( iv=('defaultTriangles', 4), sv=('defaultFileName', 'buffalo.maya') )
cmds.optionVar( exists='defaultTriangles' )
Result: 1 ---

cmds.optionVar( q='defaultFileName' )
Result: buffalo.maya ---

cmds.optionVar( list=True )
cmds.optionVar( remove='defaultTriangles' )
cmds.optionVar( exists='defaultTriangles' )
Result: 0 ---


---
Return:
---


    int: 0 or 1 for theexistsoption
    list[string]: When thelistoption is used

Flags:
---


---
arraySize(arraySize): string
    properties: create
    returns the size of the array named "string".  If no such
variable exists, it returns 0.  If the variable is not an
array, it returns 1.

---
category(cat): string
    properties: create
    Set category for the specified variables.

This flag can also be combined with list/listModified flags to get all the
variables in the specified category.

---
clearArray(ca): string
    properties: create, multiuse
    If there is an array named "string", it is set to be empty.
Empty arrays are not saved.

---
clearStash(cs): string
    properties: create, multiuse
    Clear backup copy of a variable.

---
default(d): boolean
    properties: create
    The variable's current and default values will be set to the specified
values.

This flag can also be combined with the query flag to get the default
value or with the exists flag to determine if a default value has been
specified.

It can also be used with list/listModifed flags to
list variables with a default value.

---
exists(ex): string
    properties: create
    Returns 1 if a variable named "string" exists, 0 otherwise.
The default/transient flags can be used to list variables
that have a default value or are transient.
All other flags will be ignored if this is used. (Query has
higher precedence)

---
floatArray(fa): string
    properties: create, multiuse
    Creates a new empty float array variable named "string".
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
floatValue(fv): [string, float]
    properties: create, multiuse
    creates a new variable named "string" with float value "float".
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different)

---
floatValue2(fv2): [string, float, float]
    properties: create, multiuse
    Creates a new variable named "string" with a 2 element float array.
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
floatValue3(fv3): [string, float, float, float]
    properties: create, multiuse
    Creates a new variable named "string" with a 3 element float array.
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
floatValue4(fv4): [string, float, float, float, float]
    properties: create, multiuse
    Creates a new variable named "string" with a 4 element float array.
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
floatValueAppend(fva): [string, float]
    properties: create, multiuse
    adds this value to the end of the array of floats named "string".
If no such array exists, one is created.  If there was a float
value with this name before, it becomes the first element of the
array.  If any other kind of value existed, it is overridden.

---
init(ini): boolean
    properties: create
    Used to initialize or reset variables. If the flag is set to true or the
variable does not exist then the variable's current and default values
will be set to the specified values. If the flag if set to false then
only the default value will be set and the current value will not be
modified.

---
intArray(ia): string
    properties: create, multiuse
    Creates a new empty int array variable named "string".
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
intValue(iv): [string, int]
    properties: create, multiuse
    creates a new variable named "string" with integer value "int".
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
intValue2(iv2): [string, int, int]
    properties: create, multiuse
    Creates a new variable named "string" with a 2 element int array.
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
intValue3(iv3): [string, int, int, int]
    properties: create, multiuse
    Creates a new variable named "string" with a 3 element int array.
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
intValue4(iv4): [string, int, int, int, int]
    properties: create, multiuse
    Creates a new variable named "string" with a 4 element int array.
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
intValueAppend(iva): [string, int]
    properties: create, multiuse
    adds this value to the end of the array of ints named "string".
If no such array exists, one is created.  If there was an int
value with this name before, it becomes the first element of the
array.  If any other kind of value existed, it is overridden.

---
list(l): boolean
    properties: create
    This returns a list of all the defined variable names.

The category flag can be used to list variables in the specified
category and the default/transient flags can be used to list
variables that have a default value or are transient.

All other flags will be ignored if this one is used. (Query and exists
flags have a higher precedence).

---
listCategories(lc): boolean
    properties: create
    This returns a list of all the defined variable categories. All other
flags will be ignored if this one is used. (Query and exists flags
have a higher precedence).

---
listModified(lm): boolean
    properties: create
    This returns a list of all the variables that have been changed from
their default value.

Variables that don't have a default value will also be returned unless
the default flag is used to filter the list to variables that have a
default value. The category flag can also be used to filter the list by
category.

All other flags will be ignored if this one is used. (Query and exists
flags have a higher precedence).

---
prefFile(pf): string
    properties: create, query
    Flag need to be used in conjunction with category
Specify where the optionVars from specified category need to be saved when saving preferences.

---
remove(rm): string
    properties: create, multiuse
    removes the variable named "string", if one exists.
Note: all removals are done before any value
setting, if both the -r and other (-sv, -iv, -fv) flags are
used in the same command.

---
removeFromArray(rfa): [string, int]
    properties: create, multiuse
    removes the element numbered "int" in the array named "string".
Everything beyond it then gets shuffled down.

---
stash(st): string
    properties: create, multiuse
    Make a backup copy of a variable.

---
stringArray(sa): string
    properties: create, multiuse
    Creates a new empty string array variable named "string".
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different).

---
stringValue(sv): [string, string]
    properties: create, multiuse
    creates a new variable named using the first string with value given
by the second string.
If a variable already exists with this name, it is overridden
in favour of the new value (even if the type is different)

---
stringValueAppend(sva): [string, string]
    properties: create, multiuse
    adds the value given by the second string to the end of the array of
strings named by the first string.
If no such array exists, one is created. If there was a string
value with this name before, it becomes the first element of the
array. If any other kind of value existed, it is overridden.

---
transient(t): boolean
    properties: create
    Indicates that specified variables will not be persisted across sessions.
This flag can also be combined with -exists to determine if a variable is
transient.

---
unstash(us): string
    properties: create, multiuse
    Restore a variable from a backup copy.

---
version(v): int
    properties: create
    Preferences version number to warn about incompatbile preference
files

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/optionVar.html 
    """


def orbit(horizontalAngle: angle, pivotPoint: tuple[linear, linear, linear], rotationAngles: tuple[angle, angle], verticalAngle: angle) -> None:
    """Synopsis:
---
---
 orbit(
[camera]
    , [horizontalAngle=angle], [pivotPoint=[linear, linear, linear]], [rotationAngles=[angle, angle]], [verticalAngle=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

orbit is undoable, NOT queryable, and NOT editable.

To revolve horizontally: the rotation axis is the camera up
direction vector. To revolve vertically: the rotation axis is the
camera left direction vector. 

When both the horizontal and the vertical angles are supplied on
the command line, the camera is firstly revolved horizontally,
then revolved vertically. 

This command may be applied to more than one camera; objects that
are not cameras are ignored. When no camera name supplied, this command
is applied to all currently active cameras. 




Example:
---
import maya.cmds as cmds

cmds.camera()
cmds.orbit( 'cameraShape1', ha=-30 )Change the horizontal angle by -30 degrees

cmds.orbit( 'cameraShape1', va=15 )Change the vertical angle by 15 degrees

cmds.orbit( 'cameraShape1', ra=(-30, 15) )Change the horizontal angle by -30 degrees and the vertical angle by 15 degrees

---


Flags:
---


---
horizontalAngle(ha): angle
    properties: create
    Angle to revolve horizontally.

---
pivotPoint(pp): [linear, linear, linear]
    properties: create
    Used as the pivot point in the world space.

---
rotationAngles(ra): [angle, angle]
    properties: create
    Angle to revolve horizontally and vertically.

---
verticalAngle(va): angle
    properties: create
    Angle to revolve vertically.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/orbit.html 
    """


def orbitCtx(alternateContext: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, localOrbit: boolean, name: string, orbitScale: float, toolName: string) -> string:
    """Synopsis:
---
---
 orbitCtx([alternateContext=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [localOrbit=boolean], [name=string], [orbitScale=float], [toolName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

orbitCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.orbitCtx( 'orbitContext', os=30.0, lo=False )

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
localOrbit(lo): boolean
    properties: create, query, edit
    Orbit around the camera's center of interest.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
orbitScale(os): float
    properties: create, query, edit
    In degrees of rotation per 100 pixels of cursor drag.

---
toolName(tn): string
    properties: create, query
    Name of the specific tool to which this command refers.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/orbitCtx.html 
    """


def orientConstraint(createCache: tuple[float, float], deleteCache: boolean, layer: string, maintainOffset: boolean, name: string, offset: tuple[float, float, float], remove: boolean, skip: string, targetList: boolean, weight: float, weightAliasList: boolean) -> string:
    """Synopsis:
---
---
 orientConstraint(
[target ...] [object]
    , [createCache=[float, float]], [deleteCache=boolean], [layer=string], [maintainOffset=boolean], [name=string], [offset=[float, float, float]], [remove=boolean], [skip=string], [targetList=boolean], [weight=float], [weightAliasList=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

orientConstraint is undoable, queryable, and editable.
An orientConstraint takes as input one or more "target" DAG transform
nodes to control the orientation of the single "constraint object"
DAG transform  The orientConstraint orients the constrained object
to match the weighted average of the target world space orientations.




Example:
---
import maya.cmds as cmds

Orients cube1 to match cone1.
cmds.orientConstraint( 'cone1', 'cube1' )

Uses the average of the orientations of cone1 and surf2.
cmds.orientConstraint( 'cone1', 'surf2', 'cube2', w=.1 )

Sets the weight for cone1's effect on cube2 to 10.
cmds.orientConstraint( 'cone1', 'cube2', e=True, w=10. )

Removes surf2 from cube2's orientConstraint
cmds.orientConstraint( 'surf2', 'cube2', e=True, rm=True )

Adds surf3 to cube2's orientConstraint with the default weight
cmds.orientConstraint( 'surf3', 'cube2' )

Constrain the y and z rotation of sph2 to sph1
cmds.orientConstraint( 'sph1', 'sph2', skip="x" )

Modify the constraint so that it constrains all axes of sph2
cmds.orientConstraint( 'sph1', 'sph2', e=True, skip="none" )

Create a cache for the orient constraint controlling cube2
cmds.orientConstraint( 'cube2', e=True, cc=(1, 1000) )

---
Return:
---


    string: [] ( name of the created constraint node)

Flags:
---


---
createCache(cc): [float, float]
    properties: edit
    This flag is used to generate an animation curve that serves as a cache for
the constraint. The two arguments define the start and end frames.

The cache is useful if the constraint has multiple targets and
the constraint's interpolation type is set to "no flip". The "no flip"
mode prevents flipping during playback, but the result is dependent on
the previous frame.  Therefore in order to consistently get the same
result on a specific frame, a cache must be generated. This flag
creates the cache and sets the constraint's interpolation type to
"cache". If a cache exists already, it will be deleted and replaced
with a new cache.

---
deleteCache(dc): boolean
    properties: edit
    Delete an existing interpolation cache.

---
layer(l): string
    properties: create, edit
    Specify the name of the animation layer where the constraint should be added.

---
maintainOffset(mo): boolean
    properties: create
    The offset necessary to preserve the constrained
object's initial orientation will be calculated and used as the
offset.

---
name(n): string
    properties: create, query, edit
    Sets the name of the constraint node to the specified
name.  Default name is constrainedObjectName_constraintType

---
offset(o): [float, float, float]
    properties: create, query, edit
    Sets or queries the value of the offset. Default is 0,0,0.

---
remove(rm): boolean
    properties: edit
    removes the listed target(s) from the constraint.

---
skip(sk): string
    properties: create, edit, multiuse
    Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". The default value in create mode is "none". This flag is multi-use.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/orientConstraint.html 
    """


def outlinerEditor(allowMultiSelection: boolean, alwaysToggleSelect: boolean, animLayerFilterOptions: string, attrAlphaOrder: string, attrFilter: string, autoExpand: boolean, autoExpandAllAnimatedShapes: boolean, autoExpandAnimatedShapes: boolean, autoExpandLayers: boolean, autoSelectNewObjects: boolean, containersIgnoreFilters: boolean, control: boolean, defineTemplate: string, directSelect: boolean, displayMode: string, doNotSelectNewObjects: boolean, docTag: string, dropIsParent: boolean, editAttrName: boolean, exists: boolean, expandAllItems: boolean, expandAllSelectedItems: boolean, expandAttribute: boolean, expandConnections: boolean, expandObjects: boolean, feedbackItemName: boolean, feedbackRowNumber: boolean, filter: string, forceMainConnection: string, getCurrentSetOfItem: int, highlightActive: boolean, highlightConnection: string, highlightSecondary: boolean, ignoreDagHierarchy: boolean, ignoreHiddenAttribute: boolean, ignoreOutlinerColor: boolean, isChildSelected: name, isSet: int, isSetMember: int, isUfeItem: int, lockMainConnection: boolean, longNames: boolean, mainListConnection: string, mapMotionTrails: boolean, masterOutliner: string, niceNames: boolean, object: name, organizeByClip: boolean, organizeByLayer: boolean, panel: string, parent: string, parentObject: boolean, pinPlug: name, refresh: boolean, removeFromCurrentSet: int, renameItem: int, renameSelectedItem: boolean, renderFilterActive: boolean, renderFilterIndex: int, renderFilterVisible: boolean, selectCommand: script, selectionConnection: string, selectionOrder: string, setFilter: string, setsIgnoreFilters: boolean, showAnimCurvesOnly: boolean, showAnimLayerWeight: boolean, showAssets: boolean, showAssignedMaterials: boolean, showAttrValues: boolean, showAttributes: boolean, showCompounds: boolean, showConnected: boolean, showContainedOnly: boolean, showContainerContents: boolean, showDagOnly: boolean, showLeafs: boolean, showMuteInfo: boolean, showNamespace: boolean, showNumericAttrsOnly: boolean, showParentContainers: boolean, showPinIcons: boolean, showPublishedAsConnected: boolean, showReferenceMembers: boolean, showReferenceNodes: boolean, showSelected: boolean, showSetMembers: boolean, showShapes: boolean, showTextureNodesOnly: boolean, showTimeEditor: boolean, showUVAttrsOnly: boolean, showUfeItems: boolean, showUnitlessCurves: boolean, showUpstreamCurves: boolean, sortOrder: string, stateString: boolean, transmitFilters: boolean, ufeFilter: tuple[string, string], ufeFilterValue: boolean, unParent: boolean, unlockMainConnection: boolean, unpinPlug: name, updateMainConnection: boolean, useTemplate: string) -> string:
    """Synopsis:
---
---
 outlinerEditor(
editorName
    , [allowMultiSelection=boolean], [alwaysToggleSelect=boolean], [animLayerFilterOptions=string], [attrAlphaOrder=string], [attrFilter=string], [autoExpand=boolean], [autoExpandAllAnimatedShapes=boolean], [autoExpandAnimatedShapes=boolean], [autoExpandLayers=boolean], [autoSelectNewObjects=boolean], [containersIgnoreFilters=boolean], [control=boolean], [defineTemplate=string], [directSelect=boolean], [displayMode=string], [doNotSelectNewObjects=boolean], [docTag=string], [dropIsParent=boolean], [editAttrName=boolean], [exists=boolean], [expandAllItems=boolean], [expandAllSelectedItems=boolean], [expandAttribute=boolean], [expandConnections=boolean], [expandObjects=boolean], [feedbackItemName=boolean], [feedbackRowNumber=boolean], [filter=string], [forceMainConnection=string], [getCurrentSetOfItem=int], [highlightActive=boolean], [highlightConnection=string], [highlightSecondary=boolean], [ignoreDagHierarchy=boolean], [ignoreHiddenAttribute=boolean], [ignoreOutlinerColor=boolean], [isChildSelected=name], [isSet=int], [isSetMember=int], [isUfeItem=int], [lockMainConnection=boolean], [longNames=boolean], [mainListConnection=string], [mapMotionTrails=boolean], [masterOutliner=string], [niceNames=boolean], [object=name], [organizeByClip=boolean], [organizeByLayer=boolean], [panel=string], [parent=string], [parentObject=boolean], [pinPlug=name], [refresh=boolean], [removeFromCurrentSet=int], [renameItem=int], [renameSelectedItem=boolean], [renderFilterActive=boolean], [renderFilterIndex=int], [renderFilterVisible=boolean], [selectCommand=script], [selectionConnection=string], [selectionOrder=string], [setFilter=string], [setsIgnoreFilters=boolean], [showAnimCurvesOnly=boolean], [showAnimLayerWeight=boolean], [showAssets=boolean], [showAssignedMaterials=boolean], [showAttrValues=boolean], [showAttributes=boolean], [showCompounds=boolean], [showConnected=boolean], [showContainedOnly=boolean], [showContainerContents=boolean], [showDagOnly=boolean], [showLeafs=boolean], [showMuteInfo=boolean], [showNamespace=boolean], [showNumericAttrsOnly=boolean], [showParentContainers=boolean], [showPinIcons=boolean], [showPublishedAsConnected=boolean], [showReferenceMembers=boolean], [showReferenceNodes=boolean], [showSelected=boolean], [showSetMembers=boolean], [showShapes=boolean], [showTextureNodesOnly=boolean], [showTimeEditor=boolean], [showUVAttrsOnly=boolean], [showUfeItems=boolean], [showUnitlessCurves=boolean], [showUpstreamCurves=boolean], [sortOrder=string], [stateString=boolean], [transmitFilters=boolean], [ufeFilter=[string, string]], [ufeFilterValue=boolean], [unParent=boolean], [unlockMainConnection=boolean], [unpinPlug=name], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

outlinerEditor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a new regular outliner in its own window
---

cmds.window()
cmds.frameLayout( labelVisible=False )
panel = cmds.outlinerPanel()
outliner = cmds.outlinerPanel(panel, query=True,outlinerEditor=True)
cmds.outlinerEditor( outliner, edit=True, mainListConnection='worldList', selectionConnection='modelList', showShapes=False, showReferenceNodes=False, showReferenceMembers=False, showAttributes=False, showConnected=False, showAnimCurvesOnly=False, autoExpand=False, showDagOnly=True, ignoreDagHierarchy=False, expandConnections=False, showNamespace=True, showCompounds=True, showNumericAttrsOnly=False, highlightActive=True, autoSelectNewObjects=False, doNotSelectNewObjects=False, transmitFilters=False, showSetMembers=True, setFilter='defaultSetFilter', ignoreHiddenAttribute=False, ignoreOutlinerColor=False )
cmds.showWindow()

---
Return:
---


    string: (the name of the editor)

Flags:
---


---
allowMultiSelection(ams): boolean
    properties: create, edit
    If true then multiple selection will be allowed in the outliner.

---
alwaysToggleSelect(ats): boolean
    properties: create, edit
    If true, then clicking on an item in the outliner will select or
deselect it without affecting the selection of other items (unless
allowMultiSelection is false). If false, clicking on an item in the
outliner will replace the current selection with the selected item.

---
animLayerFilterOptions(alf): string
    properties: create, query, edit
    Specifies whether a filter is to be applied when displaying animation layers.
If so, the options can be "allAffecting" (no filter), "active" (only the active
layers on the object will be displayed) and "animLayerEditor" (the settings will
be taken from the animation layer editor).

---
attrAlphaOrder(aao): string
    properties: create, query, edit
    Specify how attributes are to be sorted. Current recognised values
are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and
"descend" to sort from 'z' to 'a'.
Notes: a) this only applies to top level attributes.

---
attrFilter(af): string
    properties: create, query, edit
    Specifies the name of an itemFilter object to be placed on this editor.
This filters the attributes displayed in the editor.

---
autoExpand(xpd): boolean
    properties: create, query, edit
    This flag specifies whether or not objects that are loaded
in should have their attributes automatically expanded.

---
autoExpandAllAnimatedShapes(xaa) 2024: boolean
    properties: create, query, edit
    This flag controls whether or not all levels in the outliner's
DAG hierachy are expanded when looking for animated shapes.  When
set to false, the outliner expands only the top level of the hieararchy.
This flag is enabled by default and has no effect if autoExpand is
disabled or autoExpandAnimatedShapes is disabled.

---
autoExpandAnimatedShapes(xas): boolean
    properties: create, query, edit
    This flag specifies whether or not DAG objects that have animated
shapes should be automatically expanded to show the shape. This flag
is enabled by default and has no effect if autoExpand is disabled.

---
autoExpandLayers(ael): boolean
    properties: create, query, edit
    If true then when a node with animation layer is displayed, all
the animation layers will show up in expanded form.

---
autoSelectNewObjects(autoSelectNewObjects): boolean
    properties: create, query, edit
    This flag specifies whether or not new objects added to the outliner
should be automatically selected.

---
containersIgnoreFilters(cif): boolean
    properties: create, query, edit
    This flag specifices whether or not filters should be ignored
when displaying container contents.

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
directSelect(ds): boolean
    properties: create, edit
    If true then clicking on an item in the outliner will add or
remove just that item from the selection connection. If false then
clicking on an item in the outliner causes the selection connection
to be reloaded with the currently selected items in the outliner.

---
displayMode(dm): string
    properties: create, query, edit
    Affects how the outliner displays when a filter is applied. List mode
is a non-indented flat list. DAG mode indents to represent the
hierarchical structure of the model.

---
doNotSelectNewObjects(dns): boolean
    properties: create, query, edit
    If true this flag specifies that new objects added to the outliner
will not be selected, even if they are active.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
dropIsParent(dip): boolean
    properties: create, query, edit
    This flag specifies the mode for drag and drop. If the flag is true,
dropping items will do a reparent. If it is false, dropping will
reorder items. By default, the flag is true (parent).

---
editAttrName(ean): boolean
    properties: create, query, edit
    This flag specifies whether or not attribute names can be edited.
By default double-clicking on an attribute will open the expression
editor for that attribute.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
expandAllItems(eai): boolean
    properties: create, edit
    Expand or collapse all items in the outliner.

---
expandAllSelectedItems(eas): boolean
    properties: create, edit
    Expand or collapse all selected items in the outliner.

---
expandAttribute(eat): boolean
    properties: edit
    Force the outliner to fill the selection list with only attributes.

---
expandConnections(xc): boolean
    properties: create, query, edit
    This flag specifies whether or not attributes should be
expanded to show their input connections.
Note: currently the expansion will only show animCurves.

---
expandObjects(eo): boolean
    properties: create, query, edit
    This flag specifies whether or not objects that are loaded
in should be automatically expanded.

---
feedbackItemName(fbn): boolean
    properties: query
    Returns the outliner item name at the current mouse position, if any.

---
feedbackRowNumber(fbr): boolean
    properties: query
    Returns the outliner row number at the current mouse position, if any.

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
getCurrentSetOfItem(gcs): int
    properties: query
    Returns the current set of item at the given row. As an item can belong to number of sets, current set is the set to which the item belongs to currently.

---
highlightActive(ha): boolean
    properties: create, query, edit
    This flag specifies whether or not the outliner should highlight
objects that are active.
Note: if the outliner is driving the contents of another editor,
setting highlightActive to true may produce unexpected behavior.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
highlightSecondary(hs): boolean
    properties: create, query, edit
    This flag specifies whether or not the outliner should highlight objects
that are contained in the highlightConnection.

---
ignoreDagHierarchy(hir): boolean
    properties: create, query, edit
    This flag specifies whether or not DAG objects are displayed
in their DAG hierarchy. Warning: using this flag without
some other form of sensible filtering will lead to a very
confusing outliner.

---
ignoreHiddenAttribute(iha): boolean
    properties: create, query, edit
    Sets whether or not the outliner ignores the 'hidden in outliner' flag on nodes.

---
ignoreOutlinerColor(ioc): boolean
    properties: create, query, edit
    Sets whether or not the outliner ignores the 'use outliner color' flag on nodes.

---
isChildSelected(ics): name
    properties: query
    This flag allows you to query if one or more of the children of the
specified item is selected in the outliner. The item should be
specified using a unique DAG path. Note that if the specified item
appears multiple times in the outliner, the result will be true if one
or more children of any occurrence of the specified item in the
outliner is/are selected.

---
isSet(isSet): int
    properties: query
    Returns true if the item present at the given row is a set.

---
isSetMember(ism): int
    properties: query
    Returns true if the item present at the given row is a set member.

---
isUfeItem(isu): int
    properties: query
    Returns true if the item present at the given row is a UFE item.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
longNames(ln): boolean
    properties: query, edit
    Controls whether long or short attribute names will be used
in the interface.  Note that this flag is ignored if the -niceNames
flag is set.  Default is short names. Queried, returns a boolean.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
mapMotionTrails(mmt): boolean
    properties: create, query, edit
    Sets whether or not we replace the motion trail in the outliner with the object it is trailing.

---
masterOutliner(mst): string
    properties: create, query, edit
    This flag is the name of an outliner that this outliner will share the objects
and state from. When an outliner is shared, all of its state information
comes from, and is applied to, the primary outliner.

---
niceNames(nn): boolean
    properties: query, edit
    Controls whether the attribute names will be displayed in
a more user-friendly, readable way.  When this is on, the longNames
flag is ignored.  When this is off, attribute names will be displayed
either long or short, according to the longNames flag.
Default is on. Queried, returns a boolean.

---
object(obj): name
    properties: query
    This flag is used together with the parentObject flag to get
the name of the parent object for the specified object.

---
organizeByClip(obc): boolean
    properties: create, query, edit
    If true then when a node with Time Editor clips is displayed, attributes
will be displayed according to the clip(s) it belongs to.
eg:

Clip1
Attr1
Attr2
Clip2
Attr1

If it is false then the outliner will be organized primarily by attributes.
eg:

Attr1
Clip1
Clip2
Attr2
Clip1

---
organizeByLayer(obl): boolean
    properties: create, query, edit
    If true then when a node with animation layer is displayed, attributes
will be displayed according to the layer(s) it belongs to.
eg:

Layer1
Attr1
Attr2
Layer2
Attr1

If it is false then the outliner will be organized primarily by attributes.
eg:

Attr1
Layer1
Layer2
Attr2
Layer1

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
pinPlug(pin): name
    properties: create, query, edit
    Pins the named plug, so it always appears in the outliner, irrespective
of the incoming selection connection.
In query mode, returns a list of the pinned plugs.

---
refresh(rfs): boolean
    properties: edit
    Causes the outliner to refresh itself.

---
removeFromCurrentSet(rcs): int
    properties: edit
    Removes selected members of a set from their current set. Current set is the set to which item at the given row belongs to.
If no selected items, the item at the given row is removed from its current set.

---
renameItem(rni): int
    properties: edit
    Renames the item at the given row index in the outliner.

---
renameSelectedItem(rsi): boolean
    properties: edit
    Rename the first selected item in the outliner.

---
renderFilterActive(rfa): boolean
    properties: query
    This is a query only flag which returns true if the render setup filter is Active, i.e one of the four render filters (Inside Selected, Outside Selected, Inside All Layers, Outside All Layers)
is applied on the outliner currently, false otherwise.

---
renderFilterIndex(rfi): int
    properties: create, query, edit
    Sets the Render Setup Filter to the index passed. This only works if the filter is visible in outliner and its selection is not locked.
Valid indices are:

0 - Scene
2 - Inside Selected
3 - Outside Selected
4 - Inside All Layers
5 - Outside All Layers

Default: Scene  0
In query mode returns current index of the filter.

---
renderFilterVisible(rfv): boolean
    properties: create, query, edit
    Show/Hide the Render Setup Filter in outliner. In query mode returns whether the Render Setup Filter is visible or not.

---
selectCommand(sec): script
    properties: create, query, edit
    A command to be executed when an item is selected.
Only valid Mel commands will be saved when the outlinerEditor
will be persisted in a scene or in a JSON layout file.
Python commands are never saved.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
selectionOrder(sod): string
    properties: edit
    Specify how objects are sorted in selection list. Current recognised values
are "chronological" for sorting in selection order and "display" to sort objects in the same order that the outliner does.

---
setFilter(sf): string
    properties: create, query, edit
    Specifies the name of a filter which is used to filter
which (if any) sets to display.

---
setsIgnoreFilters(sif): boolean
    properties: create, query, edit
    This flag specifies whether or not the filter should be ignored
for expanding sets to show set members (default is true).

---
showAnimCurvesOnly(aco): boolean
    properties: create, query, edit
    This flag modifies the showConnected flag.  If showConnected
is set to true then this flag will cause display of only
those attributes that are connected to an animCurve. If
showConnected is set to false then this flag does nothing.

---
showAnimLayerWeight(saw): boolean
    properties: create, query, edit
    If true then when a node with animation layer is displayed, the
weight of the layer will be displayed if it is keyed.

---
showAssets(a): boolean
    properties: create, query, edit
    This flags specifies whether assets should be shown in the outliner.

---
showAssignedMaterials(sam): boolean
    properties: create, query, edit
    Specifies whether to show assigned materials under shapes.

---
showAttrValues(av): boolean
    properties: create, query, edit
    This flag specifies whether attribute values or attribute names should
be displayed.
Note: currently only string attributes can have their values displayed.

---
showAttributes(atr): boolean
    properties: create, query, edit
    Specifies whether to show attributes or not.

---
showCompounds(cmp): boolean
    properties: create, query, edit
    This flag specifies whether or not compound attributes should be
displayed, or just the leaf attributes.
Note: if showConnected is true, and the compound attribute
is connected, it will still be displayed.

---
showConnected(con): boolean
    properties: create, query, edit
    This flag modifies the showAttributes flag.  If showAttributes
is set to true then this flag will cause display of only
those attributes that are connected in the dependency graph.
If showAttributes is set to false then this flag does nothing.

---
showContainedOnly(sco): boolean
    properties: create, query, edit
    This flags specifies whether nodes belonging to containers should be show
under the container node only. Otherwise, it will show up under the world
as well.

---
showContainerContents(scc): boolean
    properties: create, query, edit
    This flags specifies whether the contents of the container should be
shown under the container node in the outliner.

---
showDagOnly(dag): boolean
    properties: create, query, edit
    This flag specifies whether all dependency graph objects will
be displayed, or just DAG objects.

---
showLeafs(laf): boolean
    properties: create, query, edit
    This flag specifies whether or not leaf attributes should be
displayed, or just the compound attributes.
Note: if showConnected is true, and the leaf attribute
is connected, it will still be displayed.

---
showMuteInfo(smi): boolean
    properties: create, query, edit
    This flag specifies whether mute information will be displayed

---
showNamespace(sn): boolean
    properties: create, query, edit
    This flag specifies whether all objects will have their
namespace displayed, if namespace different than root.

---
showNumericAttrsOnly(num): boolean
    properties: create, query, edit
    This flag specifies whether or not all attributes should be
displayed, or just numeric attributes.
Note: if showConnected is true, and the attribute
is connected, it will still be displayed.

---
showParentContainers(spa): boolean
    properties: create, query, edit
    This flags specifies whether nodes belonging to containers/assets should show their
containers/assets as well in its outliner.

---
showPinIcons(spi): boolean
    properties: create, query, edit
    Sets whether pin icons are shown for unpinned plugs.

---
showPublishedAsConnected(spc): boolean
    properties: create, query, edit
    This flags enables attributes that are published to be displayed in italics.
Otherwise, only attributes connected as a destination are shown in italics.

---
showReferenceMembers(rm): boolean
    properties: create, query, edit
    Specifies whether to show reference node members under the reference node in the outliner.

---
showReferenceNodes(rn): boolean
    properties: create, query, edit
    Specifies whether to show reference nodes or not.

---
showSelected(sc): boolean
    properties: create, edit
    If true then the selected items are expanded in the outliner.

---
showSetMembers(ssm): boolean
    properties: create, query, edit
    If true then when a set is expanded, the set members
will be displayed. If false, then only other sets will be
displayed.

---
showShapes(shp): boolean
    properties: create, query, edit
    Specifies whether to show shapes or not.

---
showTextureNodesOnly(tno): boolean
    properties: create, query, edit
    This flag modifies the showConnected flag. If showConnected is set to true then
this flag will cause display of only those attributes that are connected to a
texture node. If showConnected is set to false then this flag does nothing.

---
showTimeEditor(ste): boolean
    properties: create, query, edit
    If true, all nodes related to the Time Editor will be
shown as a hierarchy.

---
showUVAttrsOnly(uv): boolean
    properties: create, query, edit
    This flag specifies whether or not all attributes should be displayed, or
just uv attributes.
Note: currently the only attribute which will be
displayed is Shape.uvSet.uvSetName.

---
showUfeItems(sui) 2024: boolean
    properties: create, query, edit
    Specifies whether to show Ufe (non-Maya) items.

---
showUnitlessCurves(su): boolean
    properties: create, query, edit
    This flag (in combination with -expandConnections) specifies
whether or not connection expansion should show unitless
animCurves.

---
showUpstreamCurves(suc): boolean
    properties: create, query, edit
    Specifies exactly which attributes are displayed when showAttributes
and expandConnections are both true.
If true, the dependency graph is searched upstream for all curves
that drive the selected plugs (showing multiple curves for example
in a typical driven key setup, where first the driven key curve is
encountered, followed by the actual animation curve that drives the
source object). If false, only the first curves encountered
will be shown. Note that, even if false, multiple curves can be shown
if e.g. a blendWeighted node is being used to combine multiple curves.

---
sortOrder(so): string
    properties: create, query, edit
    Specify how objects are to be sorted.  Current recognised values
are "none" for no sorting and "dagName" to sort DAG objects by name.
Notes: a) non-DAG objects are always sorted by nodeType and name.
b) when sortOrder is set to "dagName", objects cannot be reordered
using drag-and-drop, they can however be reparented.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
transmitFilters(tf): boolean
    properties: create, query, edit
    This flag specifies how the selectionConnection is populated
when attribute filters are enabled.  If this flag is set to
true, then all the attributes that pass the filter will be
placed on the selectionConnection.  By default this flag is
false.

---
ufeFilter(uf): [string, string]
    properties: query, edit
    Specifies what UFE filter attributes should be used for display.
This flag must used together with the ufeFilterValue flag to get/set
the value of the UFE filter.
The first string is the UFE run-time name and the second is the child filter name.

---
ufeFilterValue(ufv): boolean
    properties: query, edit
    The value of the UFE filter specified with flag ufeFilter.
This flag must used together with the ufeFilter flag.

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
unpinPlug(unp): name
    properties: create, edit
    Unpins the named plug.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/outlinerEditor.html 
    """


def outlinerPanel(control: boolean, copy: string, createString: boolean, defineTemplate: string, divider: int, docTag: string, editString: boolean, exists: boolean, init: boolean, isUnique: boolean, label: string, menuBarRepeatLast: boolean, menuBarVisible: boolean, needsInit: boolean, outlinerEditor: boolean, parent: string, popupMenuProcedure: script, replacePanel: string, tearOff: boolean, tearOffCopy: string, tearOffRestore: boolean, unParent: boolean, useTemplate: string) -> string:
    """Synopsis:
---
---
 outlinerPanel(
[panelName]
    , [control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [divider=int], [docTag=string], [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean], [outlinerEditor=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

outlinerPanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a new regular outliner in its own window
---

cmds.window()
cmds.frameLayout( labelVisible=False )
panel = cmds.outlinerPanel()
outliner = cmds.outlinerPanel(panel, query=True,outlinerEditor=True)
cmds.outlinerEditor( outliner, edit=True, mainListConnection='worldList', selectionConnection='modelList', showShapes=False, showReferenceNodes=False, showReferenceMembers=False, showAttributes=False, showConnected=False, showAnimCurvesOnly=False, autoExpand=False, showDagOnly=True, ignoreDagHierarchy=False, expandConnections=False, showCompounds=True, showNumericAttrsOnly=False, highlightActive=True, autoSelectNewObjects=False, doNotSelectNewObjects=False, transmitFilters=False, showSetMembers=True, setFilter='defaultSetFilter', ignoreHiddenAttribute=False, ignoreOutlinerColor=False )
cmds.showWindow()

---
Return:
---


    string: (the name of the panel)

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
divider(div): int
    properties: query, edit
    This flag returns the orientation of the divider bar
in the outliner.

0 : horizontal
1 : vertical

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
outlinerEditor(oe): boolean
    properties: query
    This flag returns the name of the outliner editor
contained by the panel.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/outlinerPanel.html 
    """


def outputWindow(show: boolean) -> None:
    """Synopsis:
---
---
 outputWindow([show=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

outputWindow is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.outputWindow()
cmds.outputWindow(show=True)

---


Flags:
---


---
show(s): boolean
    properties: create, query
    Show or hide the output window.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/outputWindow.html 
    """


def overrideModifier(clear: boolean, press: string, release: string) -> None:
    """Synopsis:
---
---
 overrideModifier([clear=boolean], [press=string], [release=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

overrideModifier is undoable, NOT queryable, and NOT editable.
Note that the original modifier key behaviour is not altered in anyway.
For example, if you've assigned "Ctrl" key behaviour to the "c" key
then the "Ctrl" key will still work as you expect, all you've done is
allowed yourself to use the "c" key as an alternative to the "Ctrl" key.




Example:
---
import maya.cmds as cmds

   Example 1.
---

   Map the "a" key such that it behaves just like the "Alt" key.
---

cmds.nameCommand( 'alternateAltPressCommand', annotation='"Alternate Alt-press modifier key"', command='"overrideModifier -press Alt"' )
cmds.nameCommand( 'alternateAltReleaseCommand', annotation='"Alternate Alt-release modifier key"', command='"overrideModifier -release Alt"' )
cmds.hotkey( keyShortcut='a', name='alternateAltPressCommand' )
cmds.hotkey( keyShortcut='a', releaseName='alternateAltPressCommand' )

   Example 2.
---

   The following should restore the "a" hotkey to what it was
   previously.
---

cmds.overrideModifier( clear=True )
cmds.hotkey( factorySettings=True )
cmds.hotkey( sourceUserHotkeys=True )

---


Flags:
---


---
clear(cl): boolean
    properties: create
    Don't force any modifier keys.

---
press(p): string
    properties: create, multiuse
    Force the following modifier to be pressed. Valid values are "Alt",
"Ctrl", "Shift".

---
release(r): string
    properties: create, multiuse
    Force the following modifier to be released. Valid values are "Alt",
"Ctrl", "Shift".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/overrideModifier.html 
    """
