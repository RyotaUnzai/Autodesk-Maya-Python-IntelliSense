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


def geomBind(flagbindMethod: uint, flagfalloff: float, flaggeodesicVoxelParams: tuple[uint, boolean], flagmaxInfluences: int) -> None:
    """Synopsis:
---
---
 geomBind([bindMethod=uint], [falloff=float], [geodesicVoxelParams=[uint, boolean]], [maxInfluences=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

geomBind is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


Compute geodesic voxel weights for skinCluster1 and skinCluster2. This
command will create a geomBind node connected to the two skinClusters
and their common bind pose. The geomBind node will maintain the
geodesic voxel binding parameters used (ie: falloff, resolution, etc.)
---

cmds.select( 'skinCluster1', r=True )
cmds.select( 'skinCluster2', add=True )
cmds.geomBind( bm=3, fo=0, mi=5 )

Create a simple scene that use geodesic voxel weights for skin binding.
cmds.file( f=True, new=True )
cmds.polyCylinder( r=1, h=10, sx=20, sy=20, sz=5 )
cmds.select( d=True )
cmds.joint( p=[0, -4, 0] )
cmds.joint( p=[0, 0, 0] )
cmds.joint( p=[0, 4, 0] )
cmds.select( 'joint1', 'joint2', 'joint3', 'pCylinder1' )
cmds.skinCluster( bindMethod=3 )
cmds.geomBind( 'skinCluster1', bindMethod=3 )

---


Flags:
---


---
bindMethod(bm): uint
    properties: create
    Specifies which bind algorithm to use. By default, Geodesic Voxel will be used.
Available algorithms are:
3 - Geodesic Voxel

---
falloff(fo): float
    properties: create, query, edit
    Falloff controlling the bind stiffness. Valid values range from [0..1].

---
geodesicVoxelParams(gvp): [uint, boolean]
    properties: create, query, edit
    Specifies the geodesic voxel binding parameters. This flag is composed of three
parameters:
0 - Maximum voxel grid resolution which must be a power of two. (ie. 64, 128, 256, etc. )
1 - Performs a post voxel state validation when enabled.
Default values are 256 true.

---
maxInfluences(mi): int
    properties: create, query, edit
    Specifies the maximum influences a vertex can have. By default, all influences
are used (-1).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/geomBind.html 
    """


def geomToBBox(flagbakeAnimation: boolean, flagcombineMesh: boolean, flagendTime: time, flagkeepOriginal: boolean, flagname: string, flagnameSuffix: string, flagsampleBy: time, flagshaderColor: tuple[float, float, float], flagsingle: boolean, flagstartTime: time) -> None:
    """Synopsis:
---
---
 geomToBBox([bakeAnimation=boolean], [combineMesh=boolean], [endTime=time], [keepOriginal=boolean], [name=string], [nameSuffix=string], [sampleBy=time], [shaderColor=[float, float, float]], [single=boolean], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

geomToBBox is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


Create two poly spheres and parent them together
---

cmds.polySphere()
cmds.move(-1, 0, 3)
cmds.polySphere()
cmds.move(3, 0, -1)
cmds.parent( 'pSphere2', 'pSphere1' )

Select the parent sphere
---

cmds.select( 'pSphere1', replace=True )

Create a bounding box per shape in the object hierarchy selected,
add a name and suffix for that bounding box and add a RGB color for the
shader color.
---

cmds.geomToBBox(name='MyBBox', nameSuffix='_perShape', shaderColor=[0,1,0.043])

Create two poly spheres and parent them together
---

cmds.polySphere()
cmds.move(-1, 5, 3)
cmds.polySphere()
cmds.move(3, 5, -1)
cmds.parent( 'pSphere2', 'pSphere1' )

Select the parent sphere
---

cmds.select( 'pSphere1', replace=True )

Create one bounding box for the entire hierarchy selected,
add a name and suffix for that bounding box and add a RGB color for the
shader color.
---

cmds.geomToBBox(single=True, name='MyBBox', nameSuffix='_hierarchy', shaderColor=[0.928,0.460,1])

Create and simple animation and bake the animation on the bounding box for
a specific time frame and incremental evaluation time.
cmds.polySphere(name="BouncingBall")
cmds.currentTime(1)
cmds.setKeyframe()
cmds.currentTime(5)
cmds.move( 0, 10, 0)
cmds.setKeyframe()
cmds.currentTime(9)
cmds.move( 0, 0, 0)
cmds.setKeyframe()

cmds.geomToBBox(keepOriginal=True, name="BakedAnimBBox", bakeAnimation=True, startTime=3, endTime=7, sampleBy=0.5)
cmds.currentTime(1)

---


Flags:
---


---
bakeAnimation(ba): boolean
    properties: create
    Bake the animation. Can be used with startTime, endTime and sampleBy flags.
If used alone, the time slider will be used to specify the startTime and endTime.

---
combineMesh(cm): boolean
    properties: create
    Combine resulting bounding boxes.
Mutually exclusive with -s/single option.

---
endTime(et): time
    properties: create
    Used with bakeAnimation flag. Specifies the end time of the baking process.

---
keepOriginal(ko): boolean
    properties: create
    Do not remove the selected nodes used to create the bounding boxes.

---
name(n): string
    properties: create
    Specifies the bounding box name.

---
nameSuffix(ns): string
    properties: create
    Specifies the bounding box name suffix.

---
sampleBy(sb): time
    properties: create
    Used with bakeAnimation flag. Specifies the animation evaluation time increment.

---
shaderColor(sc): [float, float, float]
    properties: create
    Set the color attribute of the Lambert material associate with the bounding box.
The RGB values should be defined between 0 to 1.0.
Default value is 0.5 0.5 0.5.

---
single(s): boolean
    properties: create
    Create a single bounding box per hierarchy selected.

---
startTime(st): time
    properties: create
    Used with bakeAnimation flag. Specifies the start time of the baking process.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/geomToBBox.html 
    """


def geometryAttrInfo(flagboundingBox: boolean, flagcastToEdges: boolean, flagcastToFaces: boolean, flagcastToVerts: boolean, flagcomponentTagCategory: boolean, flagcomponentTagExpression: string, flagcomponentTagHash: boolean, flagcomponentTagHistory: boolean, flagcomponentTagHistoryHash: boolean, flagcomponentTagNames: boolean, flagcomponents: boolean, flagdeformerChain: boolean, flagelementCount: boolean, flaggroupId: int, flagmatrix: boolean, flagnodeChain: boolean, flagoriginalGeometry: boolean, flagoutputPlugChain: boolean, flagplugChain: boolean, flagpointCount: boolean, flagpointIndices: boolean, flagpoints: boolean, flagsubsetState: boolean) -> Any:
    """Synopsis:
---
---
 geometryAttrInfo(
attribute
    , [boundingBox=boolean], [castToEdges=boolean], [castToFaces=boolean], [castToVerts=boolean], [componentTagCategory=boolean], [componentTagExpression=string], [componentTagHash=boolean], [componentTagHistory=boolean], [componentTagHistoryHash=boolean], [componentTagNames=boolean], [components=boolean], [deformerChain=boolean], [elementCount=boolean], [groupId=int], [matrix=boolean], [nodeChain=boolean], [originalGeometry=boolean], [outputPlugChain=boolean], [plugChain=boolean], [pointCount=boolean], [pointIndices=boolean], [points=boolean], [subsetState=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

geometryAttrInfo is undoable, NOT queryable, and NOT editable.
The requests can be made on a subset of the geometry, either limited by a
specific groupId or by a componentTag expression. For example, when a componentTag
expression is used, the requested indices will be the indices that match the
subset as defined by that expression.




Example:
---
import maya.cmds as cmds

    import maya.cmds as cmds

    cmds.polyCylinder(n="myGeo", r=1, h=6, sx=4, sy=5, sz=1)[0]
    cmds.select(['myGeo.vtx[12:23]', 'myGeo.vtx[25]'])

    clusterNode, clusterHandle = cmds.cluster()
    cmds.move(1.0, 0, 0, clusterHandle, absolute=True)

    Find the groupId for the cluster node to test our queries
    gid = cmds.getAttr('{0}.input[0].groupId'.format(clusterNode))

    Get the number of points
    n0 = cmds.geometryAttrInfo('myGeo.outMesh', pc=True)
    n1 = cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pc=True)
    print "Deforming {0} out of {1} points".format(n1, n0)
    Deforming 13 out of 26 points

    Get the indices that are being deformed
    cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, pi=True)
    Result: [12L, 13L, 14L, 15L, 16L, 17L, 18L, 19L, 20L, 21L, 22L, 23L, 25L] ---


    Get the components that are being deformed
    cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, cmp=True)
    Result: [u'vtx[12:23]', u'vtx[25]'] ---


    Get the bounding box of the total geometry
    cmds.geometryAttrInfo('myGeo.outMesh', bb=True)
    Result: [-1.0, 2.0, -3.0, 3.0, -1.0, 1.0] ---


    Get the bounding box of what is being deformed
    cmds.geometryAttrInfo('myGeo.outMesh', gid=gid, bb=True)
    Result: [0.0, 2.0, 0.6000001430511475, 3.0, -1.0, 1.0] ---


    Get the node chain leading up to the cluster]
    cmds.geometryAttrInfo('cluster1.outputGeometry[0]', nch=True)
    Result: [u'polyCylinder1', u'myGeoShapeOrig', u'groupParts2', u'tweak1', u'cluster1GroupParts', u'cluster1'] ---


    Get the deformer chain leading up to the cluster
    cmds.geometryAttrInfo('cluster1.outputGeometry[0]', dch=True)
    Result: [u'tweak1', u'cluster1'] ---


    Get the plug chain leading up to the cluster
    cmds.geometryAttrInfo('cluster1.outputGeometry[0]', pch=True)
    Result: [u'polyCylinder1.output', u'myGeoShapeOrig.inMesh', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.inputGeometry', u'groupParts2.outputGeometry', u'tweak1.input[0].inputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.inputGeometry', u'cluster1GroupParts.outputGeometry', u'cluster1.input[0].inputGeometry', u'cluster1.outputGeometry[0]'] ---


    Get the output plug chain leading up to the cluster
    cmds.geometryAttrInfo('cluster1.outputGeometry[0]', och=True)
    Result: [u'polyCylinder1.output', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.outputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.outputGeometry', u'cluster1.outputGeometry[0]'] ---


---
Return:
---


    Any: Information about the geometry in the attribute. The number and type
of values returned depends on the information request.

Flags:
---


---
boundingBox(bb): boolean
    properties: create
    Returns the bounding box of the geometry

---
castToEdges(cte): boolean
    properties: create
    Ensures the componentTag expression will be resolved to edge components

---
castToFaces(ctf): boolean
    properties: create
    Ensures the componentTag expression will be resolved to face components

---
castToVerts(ctv): boolean
    properties: create
    Ensures the componentTag expression will be resolved to vert components

---
componentTagCategory(ccy): boolean
    properties: create
    This flag will return the component tag category of the resulting components.
Verts are "v", edges are "e", faces are "f". In case the the category can not
be determined "unknown" is returned

---
componentTagExpression(cex): string
    properties: create
    Specifies the componentTagExpression we want to query. When specified all answers to
the information requests will be limited to the subset of the geometry as is
contained in the combination of these componentTags

---
componentTagHash(hsh): boolean
    properties: create
    This flag will return a unique hash value for the state of all the componentTags
contained in the geometry. If a hash is different from before it means that
something has changed, either tags have been added/removed/renamed and/or their
component contents have been altered.

---
componentTagHistory(cth): boolean
    properties: create
    This flag will return a description of the componentTags and the nodes in the chain
where they were added to the geometry.

---
componentTagHistoryHash(chh): boolean
    properties: create
    This flag will return a unique hash value for the componentTag history of the
geometry in the plug. If a hash is different from before it means that
something has changed, either different nodes have created the tags or the
contents of the tags have been altered.

---
componentTagNames(cnm): boolean
    properties: create
    Returns the names of the componentTags on the geometry

---
components(cmp): boolean
    properties: create
    Returns the components of the geometry

---
deformerChain(dch): boolean
    properties: create
    This flag will return the list of deformer nodes through which the geometry passes to the specified plug

---
elementCount(ec): boolean
    properties: create
    Returns the element count of the components

---
groupId(gid): int
    properties: create
    Specifies the groupId we want to query. When specified all answers to the
information requests will be limited to the subset of the geometry as is
contained in this groupId

---
matrix(mtx): boolean
    properties: create
    Returns the matrix associated with the geometry

---
nodeChain(nch): boolean
    properties: create
    This flag will return the list of nodes through which the geometry passes to the specified plug

---
originalGeometry(og): boolean
    properties: create
    This flag will return the name of a plug on a node upstream (likely at the front end)
that is the best candidate to be used as the originalGeometry. This can return an
empty plug when none exists.

---
outputPlugChain(och): boolean
    properties: create
    This flag will return the chain of plugs upstream of the specified plug (including only output plugs)

---
plugChain(pch): boolean
    properties: create
    This flag will return the chain of plugs upstream of the specified plug (including both input and output plugs)

---
pointCount(pc): boolean
    properties: create
    Returns the point count of the geometry

---
pointIndices(pi): boolean
    properties: create
    Returns the indices of the geometry

---
points(pnt): boolean
    properties: create
    Returns a list of points of the geometry

---
subsetState(sbs): boolean
    properties: create
    Returns the state of the specified subset
-1 means the subset was invalid
0 means the subset contains none of the points of the geometry
1 means the subset contains some (but not all) of the points of the geometry
2 means the subset contains all the points of the geometry

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/geometryAttrInfo.html 
    """


def geometryConstraint(flaglayer: string, flagname: string, flagremove: boolean, flagtargetList: boolean, flagweight: float, flagweightAliasList: boolean) -> list[string]:
    """Synopsis:
---
---
 geometryConstraint(
[target...] object
    , [layer=string], [name=string], [remove=boolean], [targetList=boolean], [weight=float], [weightAliasList=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

geometryConstraint is undoable, queryable, and editable.
A geometryConstraint takes as input one or more surface shapes (the
targets) and a DAG transform node (the object).  The
geometryConstraint position constrained object such object lies on
the surface of the target with the greatest weight value.  If two
targets have the same weight value then the one with the lowest index
is chosen.




Example:
---
import maya.cmds as cmds

Constrain cube1 to surf1 at the closest point to  cube1.
cmds.geometryConstraint( 'surf1', 'cube1' )

Will prefer surf1 though the weights are equal
cmds.geometryConstraint( 'surf1', 'surf2', 'cube2', w=.1 )

Now constraints cube2 to lie on surf2 as it's weight is greater
cmds.geometryConstraint( 'surf2', 'cube2', e=True, w=10. )

Removes surf2 from cube2's geometryConstraint.
cmds.geometryConstraint( 'surf2', 'cube2', e=True, rm=True )

Adds surf3 to cube2's geometryConstraint with the default weight.
cmds.geometryConstraint( 'surf3', 'cube2' )

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/geometryConstraint.html 
    """


def getAttr(flagasString: boolean, flagcaching: boolean, flagchannelBox: boolean, flagexpandEnvironmentVariables: boolean, flagkeyable: boolean, flaglock: boolean, flagmultiIndices: boolean, flagsettable: boolean, flagsilent: boolean, flagsize: boolean, flagtime: time, flagtype: boolean) -> Any:
    """Synopsis:
---
---
 getAttr(
attribute
    , [asString=boolean], [caching=boolean], [channelBox=boolean], [expandEnvironmentVariables=boolean], [keyable=boolean], [lock=boolean], [multiIndices=boolean], [settable=boolean], [silent=boolean], [size=boolean], [time=time], [type=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getAttr is NOT undoable, NOT queryable, and NOT editable.
For Ufe attributes, the input attribute string should be
"<ufe_path_string>.<ufe_attribute_name>".

UI units are used where applicable.

Currently, the types of attributes that can be displayed are:


 numeric attributes
 string attributes
 matrix attributes
 numeric compound attributes (whose children are all numeric)
 vector array attributes
 double array attributes
 int32 array attributes
 point array attributes
 data component list attributes
 Ufe attributes


Other data types cannot be retrieved. No result is returned if the
attribute contains no data.




Example:
---
import maya.cmds as cmds

cmds.createNode( 'revolve', n='gravityWell' )
cmds.sphere( n='loxTank' )
cmds.cone( n='noseCone' )
cmds.cone( n='fin' )
cmds.pointConstraint( 'fin', 'noseCone', n='weld' )

angle = cmds.getAttr('gravityWell.esw')
Result: 360 ---

type = cmds.getAttr('loxTank.translate',type=True)
Result: double3 ---

lock = cmds.getAttr('noseCone.translateX',lock=True)
Result: 0 ---

finZ = cmds.getAttr('fin.translateZ',time=12)
Result: 0.0 ---

size = cmds.getAttr('weld.target',size=True)
Result: 1 ---

size = cmds.getAttr('weld.target',settable=True)
Result: 0 ---

matrix = cmds.getAttr('loxTank.matrix')
Result: 1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 ---

cmds.createNode('file',n='file1')
cmds.setAttr( 'file1.ftn', '$TMPDIR/smile.gif',type='string' )
s = cmds.getAttr('file1.ftn')
Result: $TMPDIR/smile.gif ---

s = cmds.getAttr('file1.ftn',x=True)
Result: /var/tmp/smile.gif ---


Get the list of all used indices on a multi attribute
cmds.getAttr('initialShadingGroup.dagSetMembers', multiIndices=True)
Result: [0, 1, 2] ---


---
Return:
---


    Any: Value or state of the attribute. The number and type
of values returned is dependent on the attribute type.

Flags:
---


---
asString(asString): boolean
    properties: create
    This flag is only valid for enum attributes. It allows you to
get the attribute values as strings instead of integer values.
Note that the returned string value is dependent on the
UI language Maya is running in (about -uiLanguage).
Not supported for Ufe attributes.

---
caching(ca): boolean
    properties: create
    Returns whether the attribute is set to be cached internally
Not supported for Ufe attributes.

---
channelBox(cb): boolean
    properties: create
    Returns whether the attribute is set to show in the Channel Box.
Keyable attributes also show in the Channel Box.
Not supported for Ufe attributes. The display of Ufe attributes in
the Channel Box is controlled using the channelBox command flag
-ual/ufeFixedAttrList.

---
expandEnvironmentVariables(x): boolean
    properties: create
    Expand any environment variable and (tilde characters on UNIX)
found in string attributes which are returned.
Not supported for Ufe attributes.

---
keyable(k): boolean
    properties: create
    Returns the keyable state of the attribute.
Not supported for Ufe attributes.

---
lock(l): boolean
    properties: create
    Returns the lock state of the attribute.

---
multiIndices(mi): boolean
    properties: create
    If the attribute is a multi, this will return a list containing
all of the valid indices for the attribute.
Not supported for Ufe attributes.

---
settable(se): boolean
    properties: create
    Returns 1 if this attribute is currently settable by setAttr,
0 otherwise. An attribute is settable if it's not locked
and either not connected, or has only keyframed animation.
For Ufe attributes an attribute is settable if it's not locked.

---
silent(sl): boolean
    properties: create
    When evaluating an attribute that is not a numeric or string
value, suppress the error message saying that the data cannot be
displayed. The attribute will be evaluated even though its data
cannot be displayed. This flag does not suppress all error messages,
only those that are benign.
Not supported for Ufe attributes.

---
size(s): boolean
    properties: create
    Returns the size of a multi-attribute array.  Returns 1 if non-multi.
Not supported for Ufe attributes.

---
time(t): time
    properties: create
    Evaluate the attribute at the given time instead of the current time.
Not supported for Ufe attributes.

---
type(typ): boolean
    properties: create
    Returns the type of data currently in the attribute.

Attributes of simple types such as strings and numerics always contain
data, but attributes of complex types (arrays, meshes, etc) may contain no data
if none has ever been assigned to them. When this happens the command will
return with no result: not an empty string, but no result at all.
Attempting to directly compare this non-result to another value or use it
in an expression will result in an error, but you can assign it to a
variable in which case the variable will be set to the default value for
its type (e.g. an empty string for a string variable, zero for an integer
variable, an empty array for an array variable). So to be safe when using this
flag, always assign its result to a string variable, never try to use it
directly.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getAttr.html 
    """


def getClassification(flagsatisfies: string) -> list[string]:
    """Synopsis:
---
---
 getClassification(
string
    , [satisfies=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getClassification is undoable, NOT queryable, and NOT editable.
Classification strings look like file pathnames ("shader/reflective" or "texture/2D", for
example).  Multiple classifications can be combined into a single compound
classification string by joining the individual classifications with ':'.
For example, the classification string "shader/reflective:texture/2D" means
that the node is both a reflective shader and a 2D texture.

The classification string is used to determine how rendering nodes
are categorized in various UI, such as the Create Render Node and HyperShade
windows:


CategoryClassification String
2D Textures"texture/2d"
3D Textures"texture/3d"
Env Textures"texture/environment"
Surface Materials"shader/surface"
Volumetric Materials"shader/volume"
Displacement Materials"shader/displacement"
Lights"light"
General Utilities"utility/general"
Color Utilities"utility/color
Particle Utilities"utility/particle"
Image Planes"imageplane"
Glow"postprocess/opticalFX"


The classification string is also used to determine how Viewport 2.0
will interpret the node.


CategoryClassification String
Geometry"drawdb/geometry"
Transform"drawdb/geometry/transform"
Sub-Scene Object"drawdb/subscene"
Shader"drawdb/shader"
Surface Shader"drawdb/shader/surface"




Example:
---
import maya.cmds as cmds

Get the classification string for the "lambert" node type
---

classifications = cmds.getClassification('lambert')
for c in classifications[:]:
    print '\tClassified as ' + c + '\n'

isShader = cmds.getClassification("lambert",satisfies="shader")

---
Return:
---


    list[string]: Returns the classification strings for the given node type, or
an empty array if the node type is not classified.

Flags:
---


---
satisfies(sat): string
    properties: create
    Returns true if the given node type's classification satisfies the classification
string which is passed with the flag.

A non-compound classification string A is said to satisfy a non-compound
classification string B if A is a subclassification of B (for example,
"shaders/reflective" satisfies "shaders").

A compound classification string A satisfies a compound classification
string B iff:


every component of A satisfies at least one component of B and 
every component of B is satisfied by at least one component of A


Hence, "shader/reflective/phong:texture" satisfies "shader:texture", but
"shader/reflective/phong" does not satisfy "shader:texture".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getClassification.html 
    """


def getDefaultBrush() -> string:
    """Synopsis:
---
---
 getDefaultBrush()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getDefaultBrush is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

get the name of the current brush
---

brush = cmds.getDefaultBrush()

---
Return:
---


    string: Name of the default brush node

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getDefaultBrush.html 
    """


def getFileList(flagfilespec: string, flagfolder: string) -> list[string]:
    """Synopsis:
---
---
 getFileList([filespec=string], [folder=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getFileList is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

List the contents of the user's projects directory
---

cmds.getFileList( folder=cmds.internalVar(userWorkspaceDir=True) )

List all MEL files in the user's script directory
---

cmds.getFileList( folder=cmds.internalVar(userScriptDir=True), filespec='*.mel' )

---
Return:
---


    list[string]: an array of file names

Flags:
---


---
filespec(fs): string
    properties: create
    wildcard specifier for search.

---
folder(fld): string
    properties: create
    return a directory listing

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getFileList.html 
    """


def getFluidAttr(flagattribute: string, flaglowerFace: boolean, flagxIndex: int, flagxvalue: boolean, flagyIndex: int, flagyvalue: boolean, flagzIndex: int, flagzvalue: boolean) -> None:
    """Synopsis:
---
---
 getFluidAttr([attribute=string], [lowerFace=boolean], [xIndex=int], [xvalue=boolean], [yIndex=int], [yvalue=boolean], [zIndex=int], [zvalue=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getFluidAttr is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

get density for entire fluid
cmds.getFluidAttr( at='density' )

get density at the cell x=1, y=2, z=3
cmds.getFluidAttr( at='density', xi=1, yi=2, zi=3 )

get the velocity at the cell  x=1, y=2, z=3
cmds.getFluidAttr( at='velocity', xi=1, yi=2, zi=3 )

get the x-component of the velocity at cell x=1,
y=2, z=3
cmds.getFluidAttr( xvalue=True, at='velocity', xi=1, yi=2, zi=3 )

get the first component (red) of the rgb vector-valued
attribute "color" at the cell x=1, y=2, z=3
cmds.getFluidAttr( xvalue=True, at='color', xi=1, yi=2, zi=3 )

get the velocity x component the plane x=5
cmds.getFluidAttr( at='velocity', x=True, xi=5 )

---


Flags:
---


---
attribute(at): string
    properties: create
    Specifies the fluid attribute for which to display values.  Valid
attributes are "force", "velocity", "density", "falloff",
"fuel", "color", and "temperature".  (Note that getting force values is an
alternate way of getting velocity values at one time step.)

---
lowerFace(lf): boolean
    properties: create
    Only valid with "-at velocity".  Since velocity values are stored on the edges
of each voxel and not at the center, using voxel based indices to set velocity
necessarily affects neighboring voxels.  Use this flag to only set velocity
components on the lower left three faces of a voxel, rather than all six.

---
xIndex(xi): int
    properties: create
    Only return values for cells with this X index

---
xvalue(x): boolean
    properties: 
    Only get the first component of the vector-valued attribute specified by
the "-at/attribute" flag.

---
yIndex(yi): int
    properties: create
    Only return values for cells with this Y index

---
yvalue(y): boolean
    properties: 
    Only get the second component of the vector-valued attribute specified by
the "-at/attribute" flag.

---
zIndex(zi): int
    properties: create
    Only return values for cells with this Z index

---
zvalue(z): boolean
    properties: 
    Only get the third component of the vector-valued attribute specified by
the "-at/attribute" flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getFluidAttr.html 
    """


def getInputDeviceRange(flagmaxValue: boolean, flagminValue: boolean) -> float[]:
    """Synopsis:
---
---
 getInputDeviceRange([maxValue=boolean], [minValue=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getInputDeviceRange is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

This will return a single value which is the minimum value
the spaceball translate:X axis can return.
cmds.getInputDeviceRange( 'spaceball', 'translate:X', min=True )

This will return an array containing the maximum values for
all of the spaceball axes.
cmds.getInputDeviceRange( 'spaceball', max=True )

Warning:
    Maya is dependent on the device driver or plugin to supply it with
    the correct value.  Some device drivers don't return correct
    information.

---
Return:
---


    float[]: Command result

Flags:
---


---
maxValue(max): boolean
    properties: create
    list only the maximum value of the axis

---
minValue(min): boolean
    properties: create
    list only the minimum value of the axis

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getInputDeviceRange.html 
    """


def getMetadata(flagchannelName: string, flagchannelType: string, flagdataType: boolean, flagendIndex: string, flagindex: string, flagindexType: string, flaglistChannelNames: boolean, flaglistMemberNames: boolean, flaglistStreamNames: boolean, flagmemberName: string, flagscene: boolean, flagstartIndex: string, flagstreamName: string) -> float[] | list[int] | list[string]:
    """Synopsis:
---
---
 getMetadata([channelName=string], [channelType=string], [dataType=boolean], [endIndex=string], [index=string], [indexType=string], [listChannelNames=boolean], [listMemberNames=boolean], [listStreamNames=boolean], [memberName=string], [scene=boolean], [startIndex=string], [streamName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getMetadata is NOT undoable, NOT queryable, and NOT editable.
This command is used to retrieve the values of metadata elements from a node or scene.
It is restricted to returning a single structure member at a time. For convenience
the detail required is only enough to find a single Member of a single Structure
on a single metadata Channel.


In the simplest case if there is a single Stream on one metadata Channel
which uses a Structure with only one Member then all that is required is the
name of the object containing the metadata. In the most complex case the
'channelName', 'streamName', and 'memberName' are all required to narrow down
the metadata to a single unique Member.


In general for scripting it's a good idea to use all flags anyway since there
could be metadata added anywhere. The shortcuts are mainly for quick entry when
entering commands directly in the script editor or command line.


When an Index is specified where data is not present the command fails with a
message telling you which Index or Indices didn't have values. Use the
hasMetadata command first to determine where metadata exists if you
need to know in advance where to find valid metadata.

Filter Flags
channelName - Only look for metadata on one particular Channel type
streamName - Only look for metadata on one particular named Stream. When
used in conjunction with channelName then ignore Streams with a matching
name but a different Channel type
index - Only look for metadata on one or more specific Index values of
a Stream. Requires use of the streamName flag. Does not require the
indexType flag as that will be inferred by the streamName.
startIndex/endIndex - Same as index but using an entire range of
Index values rather than a single one. Not valid for index types not supporting
ranges (e.g. strings)
indexType - Only look for metadata using a particular Index type. Can
have its scope narrowed by other filter flags as well.
memberName - The particular Member in the metadata in a Structure to
retrieve. If this is not specified the Structure can only have a single Member.


Metadata on meshes is special in that the Channel types "vertex",
"edge", "face", and "vertexFace" are directly connected to the
components of the same name. To make getting these metadata
Channels easier you can simply select or specify on the command
line the corresponding components rather than using the channelName
and index/startIndex/endIndex flags. For
example the selection "myMesh.vtx[8:10]" corresponds to
channelName = vertex and either index = 8, 9, 10
as a multi-use flag or setIndex = 8, endIndex=10.


Only a single node or scene and unique metadata Structure Member are
allowed in a single command. This keeps the data simple at the possible
cost of requiring multiple calls to the command to get more than one
Structure Member's value.


When the data is returned it will be in Index order with an entire Member
appearing together. For example if you were retrieving float[3] metadata on
three components you would get the nine values back in the order:
index[0]-float[0], index[0]-float[1], index[0]-float[2],
index[1]-float[0], index[1]-float[1], index[1]-float[2],
index[2]-float[0], index[2]-float[1], index[2]-float[2]. In the Python
implementation the float[3] values will be an array each so you would
get back three float[3] arrays.




Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.polyPlane( name='smcPlane', constructionHistory=False )
Result: smcPlane ---

cmds.pickWalk( d='down' )
Result: [u'smcPlaneShape'] ---


Create structures
cmds.dataStructure( format='raw', asString='name=idStructure:int32=ID' )
Result: idStructure ---

cmds.dataStructure( format='raw', asString='name=keyValueStructure:string=value' )
Result: keyValueStructure ---


Apply structures to plane
cmds.addMetadata( structure='idStructure', streamName='idStream', channelName='vertex' )
cmds.addMetadata( structure='keyValueStructure', streamName='keyValueStream', channelName='key', indexType='string' )

Set the metadata values on three of the components by selection
cmds.select( 'smcPlaneShape.vtx[8:10]', replace=True )
cmds.editMetadata( streamName='idStream', memberName='ID', value=7 )
Result: 1 ---


Retrieve the three newly set metadata values
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( streamName='idStream', memberName='ID', channelName='vertex', index=['8','9','10'] )
Result: [[7], [7], [7]] ---


List stream names of the shape
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( listStreamNames=True )
Result: [u'keyValueStream', u'idStream'] ---


List stream names which is in the specified channel
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( channelName='vertex', listStreamNames=True )
Result: [u'idStream'] ---


List stream names of the shape which has the specified member
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( memberName='ID', listStreamNames=True )
Result: [u'idStream'] ---


List channel names which is used by the specified stream
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( streamName='idStream', listChannelNames=True )
Result: [u'vertex'] ---


List channel names which has the specified member
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( memberName='ID', listChannelNames=True )
Result: [u'vertex'] ---


List member names which is used by the specified stream
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( streamName='idStream', listMemberNames=True )
Result: [u'ID'] ---


Query data type of the listed member
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( streamName='idStream', listMemberNames=True, dataType=True )
Result: [u'ID', u'int32'] ---


Query data type of the specified member
cmds.select( 'smcPlaneShape', replace=True )
cmds.getMetadata( streamName='idStream', memberName='ID', dataType=True )
Result: [u'int32'] ---


Get metadata from a larger group of indices all at once.
Note that unassigned metadata values assume the default (0 for numbers).
cmds.select( 'smcPlaneShape.vtx[7:10]', replace=True )
cmds.getMetadata( streamName='idStream', memberName='ID' )
Result: [[0], [7], [7], [7]] ---


Set metadata values using the complex index type stream
cmds.editMetadata( streamName='keyValueStream', memberName='value', stringValue='Starry Night', index='Title' )
Result: True ---

cmds.editMetadata( streamName='keyValueStream', memberName='value', stringValue='Vincent Van Gogh', index='Artist' )
Result: True ---


Retrieve the complex index data (note return is in alphabetical order of index)
cmds.getMetadata( streamName='keyValueStream', memberName='value', channelName='key', index=['Title', 'Artist'], indexType='string' )
Result: [['Vincent Van Gogh'], ['Starry Night']] ---


---
Return:
---


    list[int]: List of integer values from the metadata member
    float[]: List of real values from the metadata member
    list[string]: List of string values from the metadata member

Flags:
---


---
dataType(dt): boolean
    properties: create
    Used with the flag 'streamName' and 'memberName' to query the dataType
of the specfied member.

---
listChannelNames(lcn): boolean
    properties: create
    Query the channel names on the shape.
This flag can be used with some flags to filter the results.
It can be used with the flag 'streamName' to get the channel
with the specfied stream and the flag 'memberName' to get the channel
in which the stream contains the specified member.
It cannot be used with the flag 'channelName'.

---
listMemberNames(lmn): boolean
    properties: create
    Query the member names on the shape.
This flag can be used with some flags to filter the results. It can be used with
'streamName' to get the member which is in the specified stream and the flag
'channelName' to get the member which is used in the specfied channel.
It cannot be used with the flag 'memberName'.

---
listStreamNames(lsn): boolean
    properties: create
    Query the stream names on the shape.
This flag can be used with some flags to filter the results. It can be
used with the flag 'channelName' to get the stream names on the specified channel
and the flag 'memberName' to get the stream names which has the specified member.
It cannot be used with the flag 'streamName'.

---
memberName(mn): string
    properties: create
    Name of the Structure member being retrieved. The names of the members are
set up in the Structure definition, either through the description passed
in through the "dataStructure" command or via the API used to create that
Structure. This flag is only necessary when selected Structures have more
than one member.

---
channelName(cn): string
    properties: create, query
    Filter the metadata selection to only recognize metadata belonging to
the specified named Channel (e.g. "vertex"). This flag is ignored if the
components on the selection list are being used to specify the metadata
of interest.
                        In query mode, this flag can accept a value.

---
channelType(cht): string
    properties: create, query
    Obsolete - use the 'channelName' flag instead.
                        In query mode, this flag can accept a value.

---
endIndex(eix): string
    properties: create
    The metadata is stored in a Stream, which is an indexed list. If you have
mesh components selected then the metadata indices are implicit in the list
of selected components. If you select only the node or scene then this flag
may be used in conjunction with the startIndex flag to specify a range
of indices from which to retrieve the metadata. It is an error to have the
value of startIndex be greater than that of endIndex.


See also the index flag for an alternate way to specify multiple
indices. This flag can only be used on index types that support a range
(e.g. integer values - it makes no sense to request a range between two
strings)

                        In query mode, this flag can accept a value.

---
index(idx): string
    properties: create, query, multiuse
    In the typical case metadata is indexed using a simple integer value.
Certain types of data may use other index types. e.g. a "vertexFace"
component will use a "pair" index type, which is two integer values; one
for the face ID of the component and the second for the vertex ID.


The index flag takes a string, formatted in the way the
specified indexType requires. All uses of the
index flag have the same indexType. If the type was
not specified it is assumed to be a simple integer value.

                        In query mode, this flag can accept a value.

---
indexType(idt): string
    properties: create, query
    Name of the index type the new Channel should be using. If not specified this
defaults to a simple integer index. Of the native types only a mesh
"vertexFace" channel is different, using a "pair" index type.
                        In query mode, this flag can accept a value.

---
scene(scn): boolean
    properties: create, query
    Use this flag when you want to add metadata to the scene as a whole rather than to
any individual nodes. If you use this flag and have nodes selected the nodes will
be ignored and a warning will be displayed.

---
startIndex(six): string
    properties: create
    The metadata is stored in a Stream, which is an indexed list. If you have
mesh components selected then the metadata indices are implicit in the list
of selected components. If you select only the node or scene then this flag
may be used in conjunction with the endIndex flag to specify a range of
indices from which to retrieve the metadata. It is an error to have the value
of startIndex be greater than that of endIndex.


See also the index flag for an alternate way to specify multiple
indices. This flag can only be used on index types that support a range
(e.g. integer values - it makes no sense to request a range between two
strings)

                        In query mode, this flag can accept a value.

---
streamName(stn): string
    properties: create, query
    Name of the metadata Stream. Depending on context it could be the name of a
Stream to be created, or the name of the Stream to pass through the filter.
                        In query mode, this flag can accept a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getMetadata.html 
    """


def getModifiers() -> int:
    """Synopsis:
---
---
 getModifiers()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getModifiers is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

def PrintModifiers(*args):
    mods = cmds.getModifiers()
    print 'Modifiers are:'
    if (mods & 1) > 0: print ' Shift'
    if (mods & 4) > 0: print ' Ctrl'
    if (mods & 8) > 0: print ' Alt'
    if (mods & 16): print ' Command/Windows'

cmds.window()
cmds.columnLayout()
cmds.button( label='Press Me', command=PrintModifiers )
cmds.showWindow()

---
Return:
---


    int: indicating which modifier keys are pressed.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getModifiers.html 
    """


def getModulePath(flagmoduleName: string) -> string:
    """Synopsis:
---
---
 getModulePath([moduleName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getModulePath is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.getModulePath(moduleName='myModule')

---
Return:
---


    string: Command result

Flags:
---


---
moduleName(mn): string
    properties: create
    The name of the module whose path you want to retrieve.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getModulePath.html 
    """


def getPanel(flagallConfigs: boolean, flagallPanels: boolean, flagallScriptedTypes: boolean, flagallTypes: boolean, flagatPosition: tuple[int, int], flagconfigWithLabel: string, flagcontaining: string, flaginvisiblePanels: boolean, flagscriptType: string, flagtype: string, flagtypeOf: string, flagunderPointer: boolean, flagvisiblePanels: boolean, flagwithFocus: boolean, flagwithLabel: string) -> list[string]:
    """Synopsis:
---
---
 getPanel([allConfigs=boolean], [allPanels=boolean], [allScriptedTypes=boolean], [allTypes=boolean], [atPosition=[int, int]], [configWithLabel=string], [containing=string], [invisiblePanels=boolean], [scriptType=string], [type=string], [typeOf=string], [underPointer=boolean], [visiblePanels=boolean], [withFocus=boolean], [withLabel=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getPanel is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.getPanel( all=True )
cmds.getPanel( type='modelPanel' )
cmds.getPanel( containing='button0' )
cmds.getPanel( underPointer=True )
cmds.getPanel( withFocus=True )

Whenever the hotBox's 'noClickCommand' is invoked, have it switch the
main Maya view to a single pane configuration, displaying the panel
which was under the mouse pointer at the time the 'hotBox' command was
executed.
def panePopAt(x, y):
        panel = cmds.getPanel(atPosition=(x, y))
        if panel != '':
                mel.eval('doSwitchPanes(1, { "single", "' + panel + '" })')

cmds.hotBox(noClickCommand=panePopAt, noClickPosition=True)

---
Return:
---


    list[string]: An array of panel names

Flags:
---


---
allConfigs(ac): boolean
    properties: create
    Return the names of the all panel configuration in a string array.

---
allPanels(all): boolean
    properties: create
    Return the names of all the panels in a string array.

---
allScriptedTypes(ast): boolean
    properties: create
    Return the names of all types of scripted panels in a string array.

---
allTypes(at): boolean
    properties: create
    Return the names of all types of panels, except scripted types in
a string array.

---
atPosition(ap): [int, int]
    properties: create
    Return the name of the panel which contains the specified screen coordinates.
An empty string is returned if there is no panel at those coordinates.

---
configWithLabel(cwl): string
    properties: create
    Return the name of the panel configuration with the specified label text.

---
containing(c): string
    properties: create
    Return the name of the panel containing the specified control.
An empty string is returned if the specified control is not in
any panel.

---
invisiblePanels(inv): boolean
    properties: create
    Return the names of all the invisible panels in a string array.

---
scriptType(sty): string
    properties: create
    Return the names of all scripted panels of the specified type in a
string array.

---
type(typ): string
    properties: create
    Return the names of all panels of the specified type in a string array.

---
typeOf(to): string
    properties: create
    Return the type of the specified panel.

---
underPointer(up): boolean
    properties: create
    Return the name of the panel that the pointer is currently over.
An empty string is returned if the pointer is not over any panel.

---
visiblePanels(vis): boolean
    properties: create
    Return the names of all the visible panels in a string array.

---
withFocus(wf): boolean
    properties: create
    Return the name of the panel that currently has focus.  If no
panel has focus then the last panel that had focus is returned.

---
withLabel(wl): string
    properties: create
    Return the name of the panel with the specified label text.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getPanel.html 
    """


def getParticleAttr(flagarray: boolean, flagattribute: string, flagobject: string) -> float[]:
    """Synopsis:
---
---
 getParticleAttr(
selectionItem
    , [array=boolean], [attribute=string], [object=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getParticleAttr is undoable, NOT queryable, and NOT editable.
If you list components, they must all be from the same particle
object; the action ignores all objects after the first.  Likewise if
you list more than one object, the actiion will return values only for
the first one.




Example:
---
import maya.cmds as cmds

cmds.getParticleAttr( 'particle1', at='velocity' )

This will return the average velocity for the entire particle
object as well as the maximum offset from the average.

cmds.getParticleAttr( 'particleShape1.pt[0:7]', 'particleShape1.pt[11]', at='velocity' )

This will return the average velocity for particles 0-7 and 11
as well as the maximum offset from the average.

cmds.getParticleAttr( 'particleShape1.pt[0:7]', 'particleShape1.pt[11]', at='position', array=1 )
This will return an array of 27 floats containing the position
values for the nine specified particles.

---
Return:
---


    float[]: Command result

Flags:
---


---
array(a): boolean
    properties: create
    Tells the action whether you want a full array of data. If set true,
the action returns an array of floats containing the values for all
the specified particles.  If set false (the default), the action
returns the average value and the maximum offset from the average over
the component.  If the attribute is a vector attribute, the action
returns six values: Average X, Average Y, Average Z, Maximum offset in X, Y, and Z of component.

---
attribute(at): string
    properties: create
    Tells the action which attribute you want the value of.
Must be a per-particle attribute.

---
object(o): string
    properties: create
    This flag is obsolete.  Instead of using it, please pass the
name of the object and/or components you want on the command line.
See the examples.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getParticleAttr.html 
    """


def getRenderDependencies() -> string:
    """Synopsis:
---
---
 getRenderDependencies(string)  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getRenderDependencies is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Return the dependencies of render target myRenderTarget.
---

import maya.cmds as cmds
dependencies = cmds.getRenderDependencies(myRenderTarget)

---
Return:
---


    string: Dependencies for argument image source

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getRenderDependencies.html 
    """


def getRenderTasks(flagcamera: string, flagrenderLayer: string) -> list[string]:
    """Synopsis:
---
---
 getRenderTasks(string, [camera=string], [renderLayer=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

getRenderTasks is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Return render tasks for myImageSource.
---

import maya.cmds as cmds
tasks = cmds.getRenderTasks('myImageSource', c='myCamera', rl='myRenderLayer')

---
Return:
---


    list[string]: Render tasks (one per string) for argument render target.

Flags:
---


---
camera(c): string
    properties: create
    Camera node to use in the render context for the image source render task.

---
renderLayer(rl): string
    properties: create
    Render layer to use in the render context for the image source render task.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/getRenderTasks.html 
    """


def ghosting(flagaction: string, flagallGhostedObjects: boolean, flagallInRange: boolean, flagcustomFrames: int, flagenable: boolean, flagfarOpacity: float, flagframes: boolean, flaggeometryFilter: boolean, flagghostedObjects: boolean, flagghostsStep: int, flaghierarchy: boolean, flagjointFilter: boolean, flaglocatorFilter: boolean, flagmode: string, flagnearOpacity: float, flagpostColor: tuple[float, float, float], flagpostFrames: int, flagpreColor: tuple[float, float, float], flagpreFrames: int, flagpreset: string, flagresetAll: boolean, flaguseDriver: boolean) -> boolean | float | float[] | list[int] | list[string] | string:
    """Synopsis:
---
---
 ghosting([action=string], [allGhostedObjects=boolean], [allInRange=boolean], [customFrames=int], [enable=boolean], [farOpacity=float], [frames=boolean], [geometryFilter=boolean], [ghostedObjects=boolean], [ghostsStep=int], [hierarchy=boolean], [jointFilter=boolean], [locatorFilter=boolean], [mode=string], [nearOpacity=float], [postColor=[float, float, float]], [postFrames=int], [preColor=[float, float, float]], [preFrames=int], [preset=string], [resetAll=boolean], [useDriver=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ghosting is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Turn off all ghost drawing
cmds.ghosting( enable=False )

Change the default actions to prevent walking down the DAG hierarchies when finding objects to ghost/unghost
cmds.ghosting( hierarchy=False )

Ghost the selected objects
cmds.ghosting( action='ghost' )
Result: "OBJECT1" ---


Unghost the selected objects
cmds.ghosting( action='unghost' )
Result: "OBJECT1" ---


Unghost all objects
cmds.ghosting( action='unghostAll' )
Result: "OBJECT1" ---


Set the mode to use only keyframes as specified, rather than every one in the playback range for ghosts
cmds.ghosting( mode='keyframes' )
cmds.ghosting( allInRange=False )

Set three custom ghost frames
cmds.ghosting( mode='custom' )
cmds.ghosting( customFrames=-9999999 )
cmds.ghosting( query=True, customFrames=True )
Return: [] ---

cmds.ghosting( customFrames=[1,2,50] )

Set the opacity of the ghost farthest from the current frame
cmds.ghosting( farOpacity=0.01 )

Query the current list of ghost frames using the ghost parameters on OBJECT1
cmds.ghosting( OBJECT1, query=True, frames=True )
Return: [1.0, 2.0, 50.0] ---


Make future ghosting actions skip geometry objects (e.g. meshes)
cmds.ghosting( geometryFilter=True )

Get the list of currently ghosted objects
cmds.ghosting( query=True, ghostedObjects=True )
Return: OBJECT1 ---


Change the number of ghosted frames after the current time to 2
cmds.ghosting( postFrames=2 )

Change the number of ghosted frames before the current time to 5
cmds.ghosting( preFrames=5 )

Change the step between ghosts to be 2
cmds.ghosting( ghostsStep=2 )

Make future ghosting actions skip joints
cmds.ghosting( jointFilter=True )

Make future ghosting actions skip locators
cmds.ghosting( locatorFilter=True )

Change the ghosting mode to only have ghosts before the current frame
cmds.ghosting( mode='pre' )

Set the opacity of the ghost closest to the current frame
cmds.ghosting( nearOpacity=0.1 )

Set the color of ghosts after the current time to be green
cmds.ghosting( postColor=[0.0, 1.0, 0.0] )

Set the color of ghosts before the current frame to red and modify all existing ghosts to use that color
cmds.ghosting( edit=True, allGhostedObjects=True, preColor=[1.0, 0.0, 0.0] )
Return: OBJECT1 ---


Set the preset to show every other ghost
cmds.ghosting( preset='2s' )

Set the preset to show 5 pre frames, 2 post frames, at every 5th frame
cmds.ghosting( preset='Custom' )
cmds.ghosting( preFrames=5 )
cmds.ghosting( postFrames=2 )
cmds.ghosting( ghostsStep=5 )
cmds.ghosting( mode='preAndPost' )

Reset all cmds.ghosting(  parameters to their default values
cmds.ghosting( resetAll=True )
Return: True ---


Set the use-driver default for the ghosts
cmds.ghosting( useDriver=True )

---
Return:
---


    boolean: the previous global state of ghost visibility (after setting 'enable' flag)
    boolean: the global state of ghost visibility (query 'enabled' flag)
    boolean: the global state of the default ghost all-in-range value (query 'allInRange' flag)
    boolean: the global state of the default ghost hierarchy (query 'hierarchy' flag)
    boolean: the global state of the default ghost geometry filter (query 'geometryFilter' flag)
    boolean: the global state of the default ghost joint filter (query 'jointFilter' flag)
    boolean: the global state of the default ghost locator filter (query 'locatorFilter' flag)
    boolean: the global state of the default post frame count (query 'postFrames' flag)
    boolean: the global state of the default pre frame count (query 'preFrames' flag)
    boolean: the global state of the default ghost frames step count (query 'ghostsStep' flag)
    list[string]: List of all objects for which ghosting was enabled ('action="ghost"' in create mode)
    list[string]: List of all objects for which ghosting was disabled ('action="unghost"' or 'action="unghostAll"' in create mode)
    list[string]: List of all objects for which ghosting is currently enabled (query 'ghostedObjects' flag)
    list[string]: List of affected objects (any flag in edit mode)
    float[]: List of (frame1, frame2, ...) that is the union of ghosted frames on all selected objects (query 'frames' flag)
    float: Current opacity value for ghosts farthest from the current time (query 'farOpacity' flag)
    float: Current opacity value for ghosts closest to the current time (query 'nearOpacity' flag)
    float: The previous opacity value for ghosts farthest from the current time (set 'farOpacity' flag)
    float: The previous opacity value for ghosts closest to the current time (set 'nearOpacity' flag)
    string: Current ghosting mode (query 'mode' flag)
    string: The previous ghosting mode (set 'mode' flag)
    float[]: Color as [red, green, blue] used for ghosts after the current time (query 'postColor' flag)
    float[]: Previous color as [red, green, blue] used for ghosts after the current time (set 'postColor' flag)
    float[]: Color as [red, green, blue] used for ghosts before the current time (query 'preColor' flag)
    float[]: Previous color as [red, green, blue] used for ghosts before the current time (set 'preColor' flag)
    list[int]: Custom frame list for the 'frames' mode (query 'customFrames' flag)
    list[int]: Previous custom frame list (set 'customFrames' flag)

Flags:
---


---
action(act): string
    properties: create
    Define the actions to be performed by the command. Legal values are
"ghost", "unghost", and "unghostAll".
The "ghost" will try to enable ghosting on all _visible_ DAG objects in the selection list.
Imtermediate transform nodes will only be ghosted if axis display are active.

---
allGhostedObjects(ago): boolean
    properties: edit
    Only works in edit mode, specifying that the edits are to be applied to all ghosted objects instead of just the selected ones.

---
allInRange(a): boolean
    properties: create, query, edit
    In create mode, define the default value for whether keyframe mode should use every keyframe in the playback range or use the specified values.
In edit mode, modify the all-in-range value for all ghosts.
In create mode with the "ghost" action, also set the custom ghost all-in-range value for the selected objects.

---
customFrames(cf): int
    properties: create, query, edit, multiuse
    In create mode, define the default value for the list of custom ghost frames.
In edit mode, modify the custom ghost frames for all ghosts. The special frame number "-9999999" is used
to remove all custom frames, circumventing a quirk in the command engine that does not allow passing an empty list.
In create mode with the "ghost" action, also set the custom ghost frames for the selected objects.

---
enable(en): boolean
    properties: create, query
    Enables or disables ghost visibility on the entire scene. This does not modify
any of the node ghosting attributes, it only globally enables or disables the
drawing of any ghosts that have been defined on nodes.
This is a preference-based flag so its value will persist between sessions,
even if you load a new file with different ghost attribute settings.

---
farOpacity(fo): float
    properties: create, query, edit
    In create mode, define the default value for the opacity value for ghosts farthest away from the current time.
In edit mode, modify the opacity value of ghosts farthest away from the current time for all ghosts.
In create mode with the "ghost" action, also set the opacity value of ghosts farthest away from the current time for the selected objects.

---
frames(f): boolean
    properties: query
    Queries the current set of ghost frames on the selected objects based on the ghosting
mode, parameters set on the object, and the current time when relevant. Ignores the state
of the ghosting enabled flag.

---
geometryFilter(gf): boolean
    properties: create, query, edit
    In create mode, enable or disable the default ghost geometry filter.
In create mode with the "ghost" action set, also filter the selection to omit geometry nodes if this flag is false.

---
ghostedObjects(go): boolean
    properties: query
    Only works in query mode to find the names of all currently ghosted DAG nodes.

---
ghostsStep(gs): int
    properties: create, query, edit
    In create mode, define the default value for the number of steps (keyframes or frames) between ghosts.
In edit mode, modify the number of steps (keyframes or frames) between ghosts.
In create mode with the "ghost" action, also set the default number of steps (keyframes or frames) between ghosts for the selected objects.

---
hierarchy(h): boolean
    properties: create, query, edit
    Enables or disables the ghost hierarchy default value. When no ghosting action is set it does
not modify any of the node ghosting attributes, it only sets the preference for how
future commands will filter the list of affected nodes.
When used in conjunction with a ghosting action it will fist set the preference value and
then use that new value as a filter on the ghosting action. If a ghosting action is specified
without this flag then the current value of the preference is used in its place.
This is a preference-based flag so its value will persist between sessions,
even if you load a new file with different ghost attribute settings.

---
jointFilter(jf): boolean
    properties: create, query, edit
    In create mode, enable or disable the default ghost joint filter.
In create mode with the "ghost" action set, also filter the selection to omit joint nodes if this flag is false.

---
locatorFilter(lf): boolean
    properties: create, query, edit
    In create mode, enable or disable the default ghost locator filter.
In create mode with the "ghost" action set, also filter the selection to omit locator nodes if this flag is false.

---
mode(m): string
    properties: create, query, edit
    Define the default mode for ghosting actions. Legal values are "preAndPost",
"pre", "post", "custom", and "keyframes".

---
nearOpacity(no): float
    properties: create, query, edit
    In create mode, define the default value for the opacity value for ghosts nearest to the current time.
In edit mode, modify the opacity value of ghosts nearest to the current time for all ghosts.
In create mode with the "ghost" action, also set the opacity value of ghosts nearest to the current time for the selected objects.

---
postColor(poc): [float, float, float]
    properties: create, query, edit
    In create mode, define the default value for the color of ghosts after the current time.
In edit mode, modify the color of ghosts after the current time for all ghosts.
In create mode with the "ghost" action, also set the color of ghosts after the current time for the selected objects.

---
postFrames(pof): int
    properties: create, query, edit
    In create mode, define the default value for the number of ghosted frames after the current time.
In edit mode, modify the number of ghosted frames after the current time for all ghosts.
In create mode with the "ghost" action, also set the default number of ghosted frames after the current time for the selected objects.

---
preColor(prc): [float, float, float]
    properties: create, query, edit
    In create mode, define the default value for the color of ghosts before the current time.
In edit mode, modify the color of ghosts before the current time for all ghosts.
In create mode with the "ghost" action, also set the color of ghosts before the current time for the selected objects.

---
preFrames(prf): int
    properties: create, query, edit
    In create mode, define the default value for the number of ghosted frames before the current time.
In edit mode, modify the number of ghosted frames before the current time for all ghosts.
In create mode with the "ghost" action, also set the default number of ghosted frames before the current time for the selected objects.

---
preset(p): string
    properties: create, query, edit
    Define the default mode for ghosting presets. Legal values are "1s", "2s", "4s", "5s", "10s", and "Custom".
Setting anything other than "Custom" fixes ghosts at 3 pre frames, 3 post frames, with a step value of the preset
(e.g. "2s" means show ghosts at every second frame or keyframe)

---
resetAll(r): boolean
    properties: create, edit
    Reset all ghosting options to their default values. Use with caution!

---
useDriver(ud): boolean
    properties: create, query, edit
    In create mode, enable or disable the default ghost use driver value.
In edit mode, modify the use driver value of all existing ghosts.
In create mode with the "ghost" action, also set the use driver value for the selected objects.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ghosting.html 
    """


def glRender(flagaccumBufferPasses: int, flagalphaSource: string, flagantiAliasMethod: string, flagcameraIcons: boolean, flagclearClr: tuple[float, float, float], flagcollisionIcons: boolean, flagcrossingEffect: boolean, flagcurrentFrame: boolean, flagdrawStyle: string, flagedgeSmoothness: float, flagemitterIcons: boolean, flagfieldIcons: boolean, flagflipbookCallback: string, flagframeEnd: int, flagframeIncrement: int, flagframeStart: int, flagfullResolution: boolean, flaggrid: boolean, flagimageDirectory: string, flagimageName: string, flagimageSize: tuple[int, int, float], flaglightIcons: boolean, flaglightingMode: string, flaglineSmoothing: boolean, flagoffScreen: boolean, flagrenderFrame: string, flagrenderSequence: string, flagsharpness: float, flagshutterAngle: float, flagtextureDisplay: boolean, flagtransformIcons: boolean, flaguseAccumBuffer: boolean, flagviewport: tuple[int, int, float], flagwriteDepthMap: boolean) -> None:
    """Synopsis:
---
---
 glRender([accumBufferPasses=int], [alphaSource=string], [antiAliasMethod=string], [cameraIcons=boolean], [clearClr=[float, float, float]], [collisionIcons=boolean], [crossingEffect=boolean], [currentFrame=boolean], [drawStyle=string], [edgeSmoothness=float], [emitterIcons=boolean], [fieldIcons=boolean], [flipbookCallback=string], [frameEnd=int], [frameIncrement=int], [frameStart=int], [fullResolution=boolean], [grid=boolean], [imageDirectory=string], [imageName=string], [imageSize=[int, int, float]], [lightIcons=boolean], [lightingMode=string], [lineSmoothing=boolean], [offScreen=boolean], [renderFrame=string], [renderSequence=string], [sharpness=float], [shutterAngle=float], [textureDisplay=boolean], [transformIcons=boolean], [useAccumBuffer=boolean], [viewport=[int, int, float]], [writeDepthMap=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

glRender is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Do a hardware render
cmds.glRender(e=1)

---


Flags:
---


---
accumBufferPasses(abp): int
    properties: query, edit
    Set the number of accum buffer render passes.

---
alphaSource(alphaSource): string
    properties: query, edit
    Control the alpha source when writing image files. Valid values
include: off, alpha, red, green, blue, luminance, clamp, invClamp.

---
antiAliasMethod(aam): string
    properties: query, edit
    Set the method used for anti-aliasing polygons: off,
uniform, gaussian.

---
cameraIcons(ci): boolean
    properties: query, edit
    Set display status of camera icons.

---
clearClr(cc): [float, float, float]
    properties: query, edit
    Set the viewport clear color (0 - 1).

---
collisionIcons(coi): boolean
    properties: query, edit
    Set display status of collison model icons.

---
crossingEffect(ce): boolean
    properties: query, edit
    Enable/disable image filtering with a convolution filter.

---
currentFrame(cf): boolean
    properties: query
    Returns the current frame being rendered.

---
drawStyle(ds): string
    properties: query, edit
    Set the object drawing style: boundingBox, points, wireframe,
flatShaded, smoothShaded.

---
edgeSmoothness(es): float
    properties: query, edit
    Controls the amount of edge smoothing. A value of 0.0 gives no
smoothing, 1.0 gives default smoothing, and any other value scales
the amount of default smoothing. Must enable the accumulation buffer.

---
emitterIcons(ei): boolean
    properties: query, edit
    Set display status of emitter icons.

---
fieldIcons(fii): boolean
    properties: query, edit
    Set display status of field icons.

---
flipbookCallback(fc): string
    properties: query, edit
    Register a procedure to be called after the render sequence has
completed. Used to build the flipbook pulldown menu. See the
example section for more details about how to build this procedure.

---
frameEnd(fe): int
    properties: query, edit
    Set the last frame to be rendered.

---
frameIncrement(fi): int
    properties: query, edit
    Set the frame increment during rendering.

---
frameStart(fs): int
    properties: query, edit
    Set the first frame to be rendered.

---
fullResolution(fr): boolean
    properties: query, edit
    Enable/disable rendering to full image output resolution.
Must set a valid image output resolution (-is).

---
grid(gr): boolean
    properties: query, edit
    Set display status of the grid.

---
imageDirectory(id): string
    properties: query, edit
    Set the directory for the image files.

---
imageName(imageName): string
    properties: query, edit
    Set the base name of the image files.

---
imageSize(imageSize): [int, int, float]
    properties: query, edit
    Set the image output size. Takes width, height and aspect ratio.
Pass 0,0,0 to use current port size. The image size must be equal to
or greater then the viewport size. Large images will be tiled if full
resolution rendering has been enabled (-fr/fullResolution).

---
lightIcons(li): boolean
    properties: query, edit
    Set display status of light icons.

---
lightingMode(lm): string
    properties: query, edit
    Set the lighting mode used for rendering: all, selected, default.

---
lineSmoothing(ls): boolean
    properties: query, edit
    Enable/disable anti-aliased lines.

---
offScreen(os): boolean
    properties: query, edit
    When set, this toggle allow HRM to use an offscreen buffer
to render the view. This allows HRM to work when the application
is iconified, or obscured

---
renderFrame(rf): string
    properties: query, edit
    Render the current frame. Requires the name of the view in
which to render.

---
renderSequence(rs): string
    properties: query, edit
    Render the current frame sequence. Requires the name of the
view in which to render.

---
sharpness(sh): float
    properties: query, edit
    Control the sharpness level of the convolution filter.

---
shutterAngle(sa): float
    properties: query, edit
    Set the shutter angle used for motion blur (0 - 1). A value
of 0.0 gives no blurring, 0.5 gives correct blurring, and 1.0
gives continuous blurring. Must enable the accumulation buffer.

---
textureDisplay(txd): boolean
    properties: query, edit
    Enable/disable texture map display.

---
transformIcons(ti): boolean
    properties: query, edit
    Set display status of transform icons.

---
useAccumBuffer(uab): boolean
    properties: query, edit
    Enable/disable the accumulation buffer.

---
viewport(vp): [int, int, float]
    properties: query, edit
    Set the viewport size. Pass in the width, height and aspect ratio.
This size will be used for all test rendering and image output size
unless full resolution (-fr) has been set and a valid image output
size (-is) has been set.

---
writeDepthMap(wdm): boolean
    properties: query, edit
    Enable/disable writing of zdepth to image files.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/glRender.html 
    """


def glRenderEditor(flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaghighlightConnection: string, flaglockMainConnection: boolean, flaglookThru: string, flagmainListConnection: string, flagpanel: string, flagparent: string, flagselectionConnection: string, flagstateString: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string, flagviewCameraName: boolean) -> None:
    """Synopsis:
---
---
 glRenderEditor(
name
    , [control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightConnection=string], [lockMainConnection=boolean], [lookThru=string], [mainListConnection=string], [panel=string], [parent=string], [selectionConnection=string], [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string], [viewCameraName=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

glRenderEditor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a glRender editor, using the top view
window = cmds.window()
cmds.paneLayout()
cmds.glRenderEditor(lookThru='top')
cmds.showWindow( window )

---


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
lookThru(lt): string
    properties: create, query, edit
    Specify which camera the glRender view should be using.

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
viewCameraName(vcn): boolean
    properties: query
    Returns the name of the current camera used by the glRenderPanel. This
is a query only flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/glRenderEditor.html 
    """


def globalStitch(flagcaching: boolean, flagconstructionHistory: boolean, flaglockSurface: boolean, flagmaxSeparation: linear, flagmodificationResistance: float, flagname: string, flagnodeState: int, flagobject: boolean, flagsampling: int, flagstitchCorners: int, flagstitchEdges: int, flagstitchPartialEdges: boolean, flagstitchSmoothness: int) -> list[string]:
    """Synopsis:
---
---
 globalStitch(
surface surface...
    , [caching=boolean], [constructionHistory=boolean], [lockSurface=boolean], [maxSeparation=linear], [modificationResistance=float], [name=string], [nodeState=int], [object=boolean], [sampling=int], [stitchCorners=int], [stitchEdges=int], [stitchPartialEdges=boolean], [stitchSmoothness=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

globalStitch is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

GlobalStitch across three surfaces surface1, surface2, surface3.
cmds.globalStitch( 'surface1', 'surface2', 'surface3', ch=True )

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
lockSurface(lk): boolean
    properties: create, query, edit, multiuse
    Keep the NURBS surface at the specified multi index unchanged by the fitting.
Default: false

---
maxSeparation(ms): linear
    properties: create, query, edit
    Maximum separation that will still be stitched.
Default: 0.1

---
modificationResistance(mr): float
    properties: create, query, edit
    Modification resistance weight for surface CVs.
Default: 1e-1

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
sampling(sam): int
    properties: create, query, edit
    Sampling when stitching edges.
Default: 1

---
stitchCorners(sc): int
    properties: create, query, edit
    Stitch corners of surfaces.
0 - off
1 - closest point
2 - closest knot
Default: 1

---
stitchEdges(se): int
    properties: create, query, edit
    Stitch edges of surfaces.
0 - off
1 - closest point
2 - matching params
Default: 1

---
stitchPartialEdges(spe): boolean
    properties: create, query, edit
    Toggle on (off) partial edge stitching.
Default: false

---
stitchSmoothness(ss): int
    properties: create, query, edit
    Set type of smoothness of edge join.
0 - off
1 - tangent
2 - normal
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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/globalStitch.html 
    """


def goal(flaggoal: string, flagindex: boolean, flaguseTransformAsGoal: boolean, flagweight: float) -> string:
    """Synopsis:
---
---
 goal(
selectionList
    , [goal=string], [index=boolean], [useTransformAsGoal=boolean], [weight=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

goal is undoable, queryable, and NOT editable.
The goal weight can be keyframed.  It lives on the particle object to
which the goal was added and is a multi-attribute.




Example:
---
import maya.cmds as cmds

cmds.sphere( name='surface1')
cmds.particle( name='Particle')

cmds.goal( 'Particle', g='surface1', w=.75 )

This command assigns surface1 as a goal of Particle with a goal
weight of 0.75.

cmds.goal( 'Particle', g='surface1', w=.75, utr=1 )

This command assigns the transform of surface1 as a goal of Particle
with a goal weight of 0.75.

cmds.goal( 'Particle', g='camera1', w=.75 )

This command assigns the transform of camera1 as a goal of Particle
with a goal weight of 0.75.  The -utr flag is not relevant because
only the transform can be used for any object other than geometry
or particles.

---
Return:
---


    string: Command result

Flags:
---


---
goal(g): string
    properties: create, query, multiuse
    This flag specifies string to be a goal of the particle object on
the command line or the currently selected particle object.  This flag
can be used multiple times to specify multiple goals for a particle
object.  Query is for use by the attribute editor.

---
index(i): boolean
    properties: query
    Returns array of multi-attribute indices for the goals.
Intended for use by the Attribute Editor.

---
useTransformAsGoal(utr): boolean
    properties: create
    Use transform of specified object instead of the shape.
Meaningful only for particle and geometry objects.  Can only be
passed once, applies to all objects passed with -g.

---
weight(w): float
    properties: create
    This specifies the goal weight as a value from 0 to 1.  A value of 0
means that the goal's position will have no effect on the particle
object, while a weight of 1 will make the particle object try to follow
the goal object exactly.  This flag can only be passed once and sets
the weight for every goal passed with the -g/-goal flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/goal.html 
    """


def grabColor(flagalpha: boolean, flaghsvValue: boolean, flagrgbValue: boolean) -> float:
    """Synopsis:
---
---
 grabColor([alpha=boolean], [hsvValue=boolean], [rgbValue=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

grabColor is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.grabColor()
cmds.grabColor( hsv=True, alpha=True )
color = cmds.grabColor()

---
Return:
---


    float: []Three float values representing the color components of the pixel below
the cursor.  If no flags are specified then the default is to return
the red, green and blue color components.

Flags:
---


---
alpha(a): boolean
    properties: create
    Appends the alpha value to the results

---
hsvValue(hsv): boolean
    properties: create
    The 3 returned float values will specify the hue, saturation and
value color components.

---
rgbValue(rgb): boolean
    properties: create
    Default : the 3 returned float values will specify the red, green and blue
color components.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/grabColor.html 
    """


def gradientControl(flagadaptiveScaling: boolean, flagannotation: string, flagattribute: name, flagbackgroundColor: tuple[float, float, float], flagclearAttribute: boolean, flagdefineTemplate: string, flagdisplayKeyInfo: boolean, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghighlightMode: string, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfControls: uint, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagreadOnly: boolean, flagrefreshOnRelease: uint, flagselectedColorControl: string, flagselectedInterpControl: string, flagselectedPositionControl: string, flagstaticNumberOfControls: boolean, flagstaticPositions: boolean, flagstatusBarMessage: string, flagupperLimitControl: string, flaguseTemplate: string, flagverticalLayout: boolean, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 gradientControl(
[string]
    , [adaptiveScaling=boolean], [annotation=string], [attribute=name], [backgroundColor=[float, float, float]], [clearAttribute=boolean], [defineTemplate=string], [displayKeyInfo=boolean], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [highlightMode=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfControls=uint], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [readOnly=boolean], [refreshOnRelease=uint], [selectedColorControl=string], [selectedInterpControl=string], [selectedPositionControl=string], [staticNumberOfControls=boolean], [staticPositions=boolean], [statusBarMessage=string], [upperLimitControl=string], [useTemplate=string], [verticalLayout=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

gradientControl is undoable, queryable, and editable.
Either a color compound or a float value (the control will
automatically detect which and display a ramp or graph accordingly).
A single float attribute for position.
An enum for the interpolation types.




Example:
---
import maya.cmds as cmds

Create a ramp widget for the profileCurve attribute
---

cmds.window( title='Gradient Control For Attribute' )
objName = cmds.createNode('polySplitRing')
cmds.columnLayout()
cmds.gradientControl( at='%s.profileCurve' % objName )
cmds.showWindow()

To add a ramp widget in the attribute editor, call the
AEaddRampControl mel script.
---


---
Return:
---


    string: The name of the port created or modified

Flags:
---


---
adaptiveScaling(adaptiveScaling): boolean
    properties: create, query, edit
    Allow the ramp widget display to scale vertically to
accommodate values greater than 1.0. True if adaptive scaling is
enabled, false (the default) if not.

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
attribute(at): name
    properties: create, edit
    Specifies the name of the gradient attribute to control.

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
clearAttribute(cla): boolean
    properties: edit
    Removes the gradient attribute that controls the widget.
A new attribute can be set again using the attribute flag

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
displayKeyInfo(dki) 2024: boolean
    properties: create, query, edit
    Specifies if key position should be displayed in a tooltip when the user
hovers over or drags a control point.

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
highlightMode(hlm): string
    properties: create, query, edit
    Specifies when the ramp should be highlighted. Only applies to curves.
Possible values are "off", "hover" and "always". Default is "off".

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
numberOfControls(nc): uint
    properties: query
    Returns the number of controls in the ramp widget

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
readOnly(ro): boolean
    properties: create, query, edit
    Specifies if the ramp is read only or not. If true, the ramp
can't be edited and control points will be hidden.

---
refreshOnRelease(ror): uint
    properties: create, query, edit
    Define how updates are dispatched during interactive
editing of the ramp widget. True causes updates to only dispatch
after releasing the mouse button after editing. False (the default)
causes updates to dispatch interactively during editing (e.g. while
moving ramp curve points). Note that the global update mode, if
set to "on release" can disable the effect of this option.

---
selectedColorControl(scc): string
    properties: create, edit
    Specifies the name of a color control to edit the selected color.

---
selectedInterpControl(sic): string
    properties: create, edit
    Specifies the name of an enum control to edit the selected
interpolation.

---
selectedPositionControl(spc): string
    properties: create, edit
    Specifies the name of a float slider to edit the selected
position.

---
staticNumberOfControls(snc): boolean
    properties: create, query, edit
    When 'true', this flag disables the creation/deletion of
ramp entries (control points) via ramp widget interaction. Default
is false.

---
staticPositions(sp): boolean
    properties: create, query, edit
    When 'true', this flag disables the interactive modification
of ramp entry positions. Default is false.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
upperLimitControl(ulc): string
    properties: create, query, edit
    Specify the name of a text control which is updated with the
current upper display limit for the ramp. This option is only
effective when adaptiveScaling is specified.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
verticalLayout(vl): boolean
    properties: create, query, edit
    When 'true', this makes the control orient vertically rather than
horizontally. The default is `false` or horizontal.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/gradientControl.html 
    """


def gradientControlNoAttr(flagannotation: string, flagasString: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcurrentKey: int, flagcurrentKeyChanged: script, flagcurrentKeyColorValue: tuple[float, float, float], flagcurrentKeyCurveValue: boolean, flagcurrentKeyInterpValue: int, flagdefineTemplate: string, flagdisplayKeyInfo: boolean, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghighlightMode: string, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagoptionVar: string, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrampAsColor: boolean, flagreadOnly: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvalueAtPoint: float, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 gradientControlNoAttr(
[string]
    , [annotation=string], [asString=string], [backgroundColor=[float, float, float]], [changeCommand=script], [currentKey=int], [currentKeyChanged=script], [currentKeyColorValue=[float, float, float]], [currentKeyCurveValue=boolean], [currentKeyInterpValue=int], [defineTemplate=string], [displayKeyInfo=boolean], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [highlightMode=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [optionVar=string], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rampAsColor=boolean], [readOnly=boolean], [statusBarMessage=string], [useTemplate=string], [valueAtPoint=float], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

gradientControlNoAttr is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a window with a gradient control for an optionVar
---

cmds.window( title='Gradient Control For OptionVar' )
cmds.optionVar(stringValueAppend=['falloffCurveOptionVar', '0,1,2'])
cmds.optionVar(stringValueAppend=['falloffCurveOptionVar', '1,0,2'])
cmds.columnLayout()
cmds.gradientControlNoAttr( 'falloffCurve', h=90)
cmds.gradientControlNoAttr( 'falloffCurve', e=True, optionVar='falloffCurveOptionVar' )
cmds.showWindow()

Query for the value on the curve at a given position.
---

cmds.gradientControlNoAttr( 'falloffCurve', q=True, valueAtPoint=0.5 )

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
asString(asString): string
    properties: query, edit
    Used to query and set the value of the ramp as a string of comma
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
    Specifies a command to be executed whenever the value of this ramp
is modified. This option should not be used when specifying an
optionVar.

---
currentKey(ck): int
    properties: create, query, edit
    Returns the index of the currently selected key.

---
currentKeyChanged(ckc): script
    properties: edit
    Specifies a command to be executed whenever the selected key
changes.

---
currentKeyColorValue(clv): [float, float, float]
    properties: query, edit
    Get or set the color of the currently selected key.
Only useful if the ramp is set to be a color ramp.

---
currentKeyCurveValue(cvv): boolean
    properties: query, edit
    Get or set the value of the currently selected key.
Only useful if the ramp is set to be a curve ramp.

---
currentKeyInterpValue(civ): int
    properties: query, edit
    Get or set the interpolation value for the current key.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
displayKeyInfo(dki) 2024: boolean
    properties: create, query, edit
    Specifies if key position should be displayed in a tooltip when the user
hovers over or drags a control point.

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
    properties: edit
    Specifies a command to be executed while the ramp is being modified.

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
highlightMode(hlm): string
    properties: create, query, edit
    Specifies when the ramp should be highlighted. Only applies to curves.
Possible values are "off", "hover" and "always". Default is "off".

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
rampAsColor(rac): boolean
    properties: create, query, edit
    Sets whether the ramp should be viewed as a colour ramp or as
a curve.  Default is as a curve.

---
readOnly(ro): boolean
    properties: create, query, edit
    Specifies if the ramp is read only or not. If true, the ramp
can't be edited and control points will be hidden.

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
valueAtPoint(vap): float
    properties: query
    Used during query to specify the point at which to query the curve.
      In query mode, this flag needs a value.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/gradientControlNoAttr.html 
    """


def graphDollyCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 graphDollyCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

graphDollyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a dolly view context for the graph editor
---

cmds.graphDollyCtx( 'graphDollyContext' )

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/graphDollyCtx.html 
    """


def graphSelectContext(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string) -> string:
    """Synopsis:
---
---
 graphSelectContext([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

graphSelectContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a selection context for the hypergraph editor.
---

cmds.graphSelectContext( 'hyperGraphSelectContext' )

---
Return:
---


    string: Command result

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/graphSelectContext.html 
    """


def graphTrackCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 graphTrackCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

graphTrackCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a track view context for the graph editor
---

cmds.graphTrackCtx( 'graphTrackContext' )

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/graphTrackCtx.html 
    """


def gravity(flagattenuation: float, flagdirectionX: float, flagdirectionY: float, flagdirectionZ: float, flagmagnitude: float, flagmaxDistance: linear, flagname: string, flagperVertex: boolean, flagposition: tuple[linear, linear, linear], flagtorusSectionRadius: linear, flagvolumeExclusion: boolean, flagvolumeOffset: tuple[linear, linear, linear], flagvolumeShape: string, flagvolumeSweep: angle) -> string:
    """Synopsis:
---
---
 gravity(
[objects]
    , [attenuation=float], [directionX=float], [directionY=float], [directionZ=float], [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

gravity is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
A gravity field simulates the Earth's gravitational force.   It pulls
objects in a fixed direction (generally downward) entirely
independent of their position or mass.

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

The default for -dx -dy -dz is always the opposite of the current up
direction. For example, if the current up direction is (0,1,0)
(a standard Maya configuration), then the gravity default is
-dx 0 -dy -1 -dz 0.  The default for -a is 9.8.  9.8 meters per second
squared happens to be standard Earth gravity, but in fact Maya interprets
this value as centimeters per second squared.  If we were to use it as
meters per second squared then with default Maya units, your particles
would vanish almost in the wink of an eye. If you want a different value,
set it in the gravity option box.




Example:
---
import maya.cmds as cmds

cmds.gravity( 'particle1' )
Creates a gravity field and adds it to the list of fields
owned by particle1.

cmds.gravity( pos=(-2, 0, 4) )
Creates a gravity field at position (0,2,4) in world coordinates.

cmds.gravity( 'MyGravity', e=True, att=10.4 )
Changes the gravitational acceleration of the field called
"MyGravity" to 10.4.

cmds.gravity( dx=0, dy=1.0, dz=0.5 )
Creates a gravity field pulling in direction (0,1,0.5) for every
active selection. If there is no active selection, it creates this
field at world position (0,0,0).

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/gravity.html 
    """


def grid(flagdefault: boolean, flagdisplayAxes: boolean, flagdisplayAxesBold: boolean, flagdisplayDivisionLines: boolean, flagdisplayGridLines: boolean, flagdisplayOrthographicLabels: boolean, flagdisplayPerspectiveLabels: boolean, flagdivisions: uint, flagorthographicLabelPosition: string, flagperspectiveLabelPosition: string, flagreset: boolean, flagsize: linear, flagspacing: linear, flagstyle: uint, flagtoggle: boolean) -> None:
    """Synopsis:
---
---
 grid([default=boolean], [displayAxes=boolean], [displayAxesBold=boolean], [displayDivisionLines=boolean], [displayGridLines=boolean], [displayOrthographicLabels=boolean], [displayPerspectiveLabels=boolean], [divisions=uint], [orthographicLabelPosition=string], [perspectiveLabelPosition=string], [reset=boolean], [size=linear], [spacing=linear], [style=uint], [toggle=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

grid is undoable, queryable, and NOT editable.
This command lets you reset the ground plane, change its size
and grid line spacing, grid subdivisions and display options.





Example:
---
import maya.cmds as cmds

---
To toggle the grid display of the grid (in all views):
currState = cmds.grid( toggle=True, q=True )
cmds.grid( toggle=(currState == 0) )

To reset the grid to default values:
cmds.grid( reset=True )

To change the grid spacing and subdivisions:
cmds.grid( spacing=10, d=10 )

To set the defaults for inches
cmds.grid( default=True, spacing='1in', size='1ft', divisions=4 )

To change the size of the grid to 20x20, extending 10 units
in each direction:
cmds.grid( spacing=10 )

To query the current size of the grid:
returns a size in the current linear unit.
cmds.grid( query=True, size=True )

A typical grid would be a grid size of 20x20, with
major grid lines every 10 units, with 10 divisions between
major grid lines. This be done with the following command.
cmds.grid( size='10cm', sp='10.0cm', d=10 )

Turn on numeric grid labels.
---

cmds.grid( displayPerspectiveLabels=True )

Display grid labels along the axes.
---

cmds.grid( perspectiveLabelPosition='axis' )

---


Flags:
---


---
default(df): boolean
    properties: query
    Used to specify/query default values.

---
displayAxes(da): boolean
    properties: query
    Specify true to display the grid axes.

---
displayAxesBold(dab): boolean
    properties: query
    Specify true to accent the grid axes by drawing them with a
thicker line.

---
displayDivisionLines(ddl): boolean
    properties: query
    Specify true to display the subdivision lines between
grid lines.

---
displayGridLines(dgl): boolean
    properties: query
    Specify true to display the grid lines.

---
displayOrthographicLabels(dol): boolean
    properties: query
    Specify true to display the grid line numeric labels in
the orthographic views.

---
displayPerspectiveLabels(dpl): boolean
    properties: query
    Specify true to display the grid line numeric labels in
the perspective view.

---
divisions(d): uint
    properties: query
    Sets the number of subdivisions between major grid lines.
The default is 10. If the spacing is 10 units, setting
divisions to 10 will cause division lines to appear 1 unit
apart.

---
orthographicLabelPosition(olp): string
    properties: query
    The position of the grid's numeric labels in orthographic
views. Valid values are    "axis" and "edge".

---
perspectiveLabelPosition(plp): string
    properties: query
    The position of the grid's numeric labels in perspective
views. Valid values are    "axis" and "edge".

---
reset(r): boolean
    properties: 
    Resets the ground plane to its default values

---
size(s): linear
    properties: query
    Sets the size of the grid in linear units.  The default is
12 units.

---
spacing(sp): linear
    properties: query
    Sets the spacing between major grid lines in linear units.
The default is 10 units.

---
style(st): uint
    properties: query
    This flag is obsolete and should not be used.

---
toggle(tgl): boolean
    properties: query
    Turns the ground plane display off in all windows, including
orthographic windows.  Default is true.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/grid.html 
    """


def gridLayout(flagallowEmptyCells: boolean, flagannotation: string, flagautoGrow: boolean, flagbackgroundColor: tuple[float, float, float], flagcellHeight: int, flagcellWidth: int, flagcellWidthHeight: tuple[int, int], flagchildArray: boolean, flagcolumnsResizable: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flaggridOrder: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfColumns: int, flagnumberOfPopupMenus: boolean, flagnumberOfRows: int, flagnumberOfRowsColumns: tuple[int, int], flagparent: string, flagpopupMenuArray: boolean, flagposition: tuple[string, int], flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 gridLayout(
[string]
    , [allowEmptyCells=boolean], [annotation=string], [autoGrow=boolean], [backgroundColor=[float, float, float]], [cellHeight=int], [cellWidth=int], [cellWidthHeight=[int, int]], [childArray=boolean], [columnsResizable=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [gridOrder=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfColumns=int], [numberOfPopupMenus=boolean], [numberOfRows=int], [numberOfRowsColumns=[int, int]], [parent=string], [popupMenuArray=boolean], [position=[string, int]], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

gridLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(50, 50) )
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
allowEmptyCells(aec): boolean
    properties: create, query
    Specify true if you want free positioning of the children
in the layout and potentially leaving empty cells between children.
Set to false if you want the children to always be packed together.
The default is true.

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
autoGrow(ag): boolean
    properties: create, query
    Specify true if you want the grid layout size to grow as
children are added.  For example, if the grid layout has 2 columns
and 2 rows then adding a fifth child will cause the grid to expand
to 3 rows if this flag is true, otherwise the grid will remain the
same size and the new child will be hidden from view until you
expand the size of the grid using the appropriate flags.  The
default is true.

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
    A positive non-zero integer value indicating the height
of cells in the grid layout.

---
cellWidth(cw): int
    properties: create, query, edit
    A positive non-zero integer value indicating the width
of cells in the grid layout.

---
cellWidthHeight(cwh): [int, int]
    properties: create, edit
    Two positive non-zero integer values for indicating the
width and height, respectively, of the cells in the grid layout.

---
childArray(ca): boolean
    properties: query
    Returns a string array of the names of the layout's
immediate children.

---
columnsResizable(cr): boolean
    properties: create, query
    Specify true if you want the number of columns to adjust
according to the width of the layout.  Set to false if you want
the number of columns to remain fixed when the width of the
layout is changed.  The default is false.

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
gridOrder(go): boolean
    properties: query
    As opposed to the childArray flag, the gridOrder flag
returns the children of the grid Layout in the order they
are diplayed in the window.

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
    properties: create, query, edit
    A positive non-zero integer value indicating the number
of columns in the grid layout.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
numberOfRows(nr): int
    properties: create, query, edit
    A positive non-zero integer value indicating the number
of rows in the grid layout.

---
numberOfRowsColumns(nrc): [int, int]
    properties: create, edit
    Two positive non-zero integer values for the number
of rows and columns, respectively, in the grid layout.

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
    Specify the name of a child control in the grid layout along
with a 1-based integer value indicating the desired
position of the child.  Positions increase from left to right
within a row and then wrap around to the next row increasing from
top to bottom.  For example, a grid layout with 3 columns and 2
rows has 6 visible positions where 1, 2 and 3 occupy the first row
and 4, 5 and 6 occupy the second.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/gridLayout.html 
    """


def group(flagabsolute: boolean, flagempty: boolean, flagname: string, flagparent: string, flagrelative: boolean, flaguseAsGroup: string, flagworld: boolean) -> string:
    """Synopsis:
---
---
 group(
[objects...]
    , [absolute=boolean], [empty=boolean], [name=string], [parent=string], [relative=boolean], [useAsGroup=string], [world=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

group is undoable, NOT queryable, and NOT editable.
If the -em flag is specified, then an empty group (with no
objects) is created.

If the -w flag is specified then the new group is placed under the
world, otherwise if -p is specified it is placed under the
specified node. If neither -w or -p is specified the new group is
placed under the lowest common group they have in common. (or the
world if no such group exists)

If an object is grouped with another object that has the same name
then one of the objects will be renamed by this command.





Example:
---
import maya.cmds as cmds

create an empty group node with no children
cmds.group( em=True, name='null1' )

create some objects and group them
cmds.sphere( n='sphere1' )
cmds.circle( n='circle1' )
cmds.group( 'circle1', 'sphere1', n='group1' )

create a group node under another node and move
the sphere under the new group node.
cmds.group( 'sphere1', parent='null1' )

---
Return:
---


    string: - name of the group node

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
empty(em): boolean
    properties: create
    create an empty group (with no objects in it)

---
name(n): string
    properties: create
    Assign given name to new group node.

---
parent(p): string
    properties: create
    put the new group under the given parent

---
relative(r): boolean
    properties: create
    preserve existing local object transformations
(relative to the new group node)

---
useAsGroup(uag): string
    properties: create
    Use the specified node as the group node. The specified node must be
derived from the transform node and must not have any existing parents
or children.

---
world(w): boolean
    properties: create
    put the new group under the world

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/group.html 
    """
