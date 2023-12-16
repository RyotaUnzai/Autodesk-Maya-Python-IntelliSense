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


def backgroundEvaluationManager(interrupt: boolean, mode: string, pause: boolean, resume: boolean) -> None:
    """Synopsis:
---
---
 backgroundEvaluationManager([interrupt=boolean], [mode=string], [pause=boolean], [resume=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

backgroundEvaluationManager is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Set background evaluation manager to serial mode
cmds.backgroundEvaluationManager( mode="serial" )
Result: True ---


Return the current background evaluation manager mode
cmds.backgroundEvaluationManager( query=True, m=True )
Result: [u'serial'] ---


Pause background evaluation
cmds.backgroundEvaluationManager( pause=True )
Result: True ---


Return the current background evaluation manager mode
cmds.backgroundEvaluationManager( query=True, p=True )
Result: True ---


Resume background evaluation (unless was paused by someone else)
cmds.backgroundEvaluationManager( resume=True )
Result: True ---


Enable fast interrupt of background executions
cmds.backgroundEvaluationManager( interrupt=True )
Result: True ---


---


Flags:
---


---
interrupt(i): boolean
    properties: create, query
    Enable or disable fast interrupt of background execution during interactive workflow.

---
mode(m): string
    properties: create, query
    Changes the current evaluation mode in the evaluation manager. Supported values are
"serial" and "parallel".

---
pause(p): boolean
    properties: create, query
    Pause background evaluation. Will block till background evaluation is fully stopped.
Can be queried to get the current state.

---
resume(r): boolean
    properties: create
    Resume background evaluation. Will start suspended evaluations unless someones else requested it.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/backgroundEvaluationManager.html 
    """


def bakeClip(blend: tuple[uint, uint], clipIndex: uint, keepOriginals: boolean, name: string) -> string:
    """Synopsis:
---
---
 bakeClip([blend=[uint, uint]], [clipIndex=uint], [keepOriginals=boolean], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bakeClip is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

   First create a simple character.
---

cmds.cone( n='bakeCone' )
cmds.character( n='coneCharacter' )

   Create some animation.
---

cmds.select( 'bakeCone', r=True )
cmds.currentTime( 0 )
cmds.setKeyframe( 'bakeCone.tx', v=0 )
cmds.currentTime( 10 )
cmds.setKeyframe( 'bakeCone.tx', v=10 )

    Make a clip.
---

cmds.clip( 'coneCharacter', startTime=0, endTime=10, name='up' )

   Create a second clip.
---

cmds.select( 'bakeCone', r=True )
cmds.currentTime( 15 )
cmds.setKeyframe( 'bakeCone.tx', v=15 )
cmds.currentTime( 25 )
cmds.setKeyframe( 'bakeCone.tx', v=0 )

Make a clip.
---

cmds.clip( 'coneCharacter', startTime=15, endTime=25, name='down' )

Blend the clips, with a linear weighting function.
---

scheduler = cmds.character('coneCharacter', query=True, sc=True)
cmds.clipSchedule( scheduler, b=(0, 1) )
blendNode = cmds.clipSchedule( scheduler, q=True, bn=(0, 1))
cmds.setKeyframe( blendNode[0], at='weight', t=0.0, v=0.0 )
cmds.setKeyframe( blendNode[0], at='weight', t=1.0, v=1.0 )

   Bake out the two clips and the blend.
---

cmds.bakeClip( 'coneCharacter', ci=[0, 1], name='bakedUpAndDown' )

---
Return:
---


    string: clip name

Flags:
---


---
blend(b): [uint, uint]
    properties: create
    Specify the indices of the clips being blended.

---
clipIndex(ci): uint
    properties: create, multiuse
    Specify the index of the clip to bake.

---
keepOriginals(k): boolean
    properties: create
    Keep original clips in the trax editor and place the merged clip into the visor. The default is to schedule the merged clip, and to keep the original clips in the visor.

---
name(n): string
    properties: create
    Specify the name of the new clip to create.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bakeClip.html 
    """


def bakeDeformer(bakeRangeOfMotion: boolean, colorizeSkeleton: boolean, customRangeOfMotion: timerange, dstMeshName: string, dstSkeletonName: string, hierarchy: boolean, influences: list[string], maxInfluences: int, pruneWeights: float, smoothWeights: int, srcMeshName: string, srcSkeletonName: string) -> string:
    """Synopsis:
---
---
 bakeDeformer([bakeRangeOfMotion=boolean], [colorizeSkeleton=boolean], [customRangeOfMotion=timerange], [dstMeshName=string], [dstSkeletonName=string], [hierarchy=boolean], [influences=string[]], [maxInfluences=int], [pruneWeights=float], [smoothWeights=int], [srcMeshName=string], [srcSkeletonName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bakeDeformer is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
import maya.mel as mel

def createJointsAndMesh(offset = (0., 0., 0.)):
    root = cmds.joint()
    for _ in range(0,5):
        cmds.joint()
        cmds.move(0., 2., 0., r=True)

    meshes = cmds.polyCube(sx=3,sy=10,sz=3,h=10)
    cmds.move(0, 5, 0, r=True)
    cmds.select([root, meshes[0]], r=True)
    cmds.move(offset[0], offset[1], offset[2], r=True)
    cmds.select(cl=True)
    return (root, meshes[0])

def bindMesh(object):
    rootJoint, mesh = object
    cmds.select(rootJoint, r=True, hi=True)
    cmds.select(mesh, add=True)
    mel.eval('SmoothBindSkin')
    cmds.select(cl=True)

def randomizeJoints(object):
    from math import degrees
    rootJoint = object[0]
    cmds.select(rootJoint, r=True)
    cmds.pickWalk(d='down')
    for i in range(4):
        rads = mel.eval('sphrand 1.')
        cmds.rotate(degrees(rads[0]), degrees(rads[1]), degrees(rads[2]))
        cmds.pickWalk(d='down')

def matchRotations(src, dst):
    cmds.select(src[0], r=True, hi=True)
    srcChain = cmds.ls(sl=True)

    cmds.select(dst[0], r=True, hi=True)
    dstChain = cmds.ls(sl=True)

    for joints in zip(dstChain, srcChain):
        cmds.select(list(joints), r=True)
        mel.eval('MatchRotation')

Create a new scene
cmds.file(f=True, new=True)

Create two joint chains/meshes
object1 = createJointsAndMesh()
object2 = createJointsAndMesh(offset=(5, 0, 0))

Bind one of the joint chains to the mesh and rotate the weights
bindMesh(object1)
randomizeJoints(object1)

Use bakeDeformer to learn and apply the linear blend skinning weights.
cmds.bakeDeformer(ss=object1[0], sm=object1[1], ds=object2[0], dm=object2[1], mi=3)

Match the rotations of the two chains to show the results are similar
matchRotations(object1, object2)

---
Return:
---


    string: BakeDeformer name

Flags:
---


---
bakeRangeOfMotion(brm) 2024.2: boolean
    properties: create
    When this flag is specified the command will generate a series of poses, one per frame, by rotating each influence 45 degrees.
This is useful for generating a set of key poses that can be modified to adjust the range of motion. (see the -customRangeOfMotion flag for details)
The first pose generated will be the current/rest pose and the total number of poses generated will be returned.

---
colorizeSkeleton(cs): boolean
    properties: create
    The new skin cluster created will have its skeleton colorized. Must be used with the -srcSkeletonName and -dstSkeletonName flags.

---
customRangeOfMotion(rom): timerange
    properties: create
    When this flag is specified with the frames for the range of motion to be used, the tool will step through
each frame as a separate pose. Otherwise the tool will use the existing range of motion in the tool
that rotates each influence 45 degrees.

    Usage examples:

 -rom "10:20" means all frames in the range from 10 to 20, inclusive, in the current time unit. 
 Omitting one end of a range means using either end of the animation range (or both), as in the following examples: 
 -rom "10:" means all frames from time 10 (in the current time unit) onwards to the maximum time in the animation range (on the timeline). 
 -rom ":10" means all frames from the minimum time on the animation range (on the timeline) up to (and including) time 10 (in the current time unit). 
 -rom ":" is a short form to specify all frames, from minimum to maximum time on the current animation range. 


When using this flag, some of the joints in the specified range of motion may not have changed sufficiently.
To improve bakeDeformer results or avoid algorithm errors, the command will return a list of influences that do not move enough in the specified range of motion.
To detect these joints, the local transformation of each joint is compared between subsequent frames.
We consider that a joint has sufficiently changed if any of the below criteria are met:

There is a rotation of at least 5 degrees, as determined by the shortest rotation between transforms.
There is a translation of 1% or greater of the size of the largest bounding box containing all joints for each frame.
There is a scaling change of at least 1%. This percentage represents the smallest scaling value over the largest scaling value (in absolute value).


    If a joint has not met any of the criteria, it will be added to the warning of joints that have not moved enough.



The custom range of motion should be considered experimental.

---
dstMeshName(dm): string
    properties: create
    The destination mesh name.

---
dstSkeletonName(ds): string
    properties: create
    The destination skeleton name.

---
hierarchy(hi): boolean
    properties: create
    All children of the passed joints that are used in the influences flag are used.

---
influences(i): string[]
    properties: create
    A list of joints that are used as the influences to determine new weights.

---
maxInfluences(mi): int
    properties: create
    The maximum number of influences per vertex.

---
pruneWeights(pw): float
    properties: create
    On the newly created skin cluster, set any weight below the given the value to zero (post-processing).
This will call the skinPercent command as follows: "skinPercent -pruneWeights [value] [skinClusterName] [dstMeshName]"
where [value] is the value passed into this flag, [skinClusterName] is the name of the new skinCluster node created
after running this tool, and [dstMeshName] is the mesh provided in the -dstMeshName flag.

---
smoothWeights(sw): int
    properties: create
    The number of smoothing iterations for smoothing weights (post-processing). This also renormalizes the remaining the weights.

---
srcMeshName(sm): string
    properties: create
    The source mesh name.

---
srcSkeletonName(ss): string
    properties: create
    The source skeleton name.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bakeDeformer.html 
    """


def bakePartialHistory(allShapes: boolean, postSmooth: boolean, preCache: boolean, preDeformers: boolean, prePostDeformers: boolean) -> string:
    """Synopsis:
---
---
 bakePartialHistory([allShapes=boolean], [postSmooth=boolean], [preCache=boolean], [preDeformers=boolean], [prePostDeformers=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bakePartialHistory is undoable, queryable, and editable.
Note that not all modeling operations can be baked such that they create exactly the
same effect after baking. For example, imagine the history contains a skinning operation
followed by a smooth. Before baking, the smooth operation is performed each time
the skin deforms, so it will smooth differently depending on the output of the skin.
When the smooth operation is baked into the skinning, the skin will be reweighted
based on the smooth points to attempt to approximate the original behavior. However,
the skin node does not perform the smooth operation, it merely performs skinning with
the newly calculated weights and the result will not be identical to before the bake.

In general, modeling operations that occur before deformers can be baked precisely.
Those which occur after can only be approximated. The -pre and -post flags allow you
to control whether only the operations before or after the deformers are baked.

When the command is used on an object with no deformers, the entire history
will be deleted.




Example:
---
import maya.cmds as cmds

create a cylinder with history to use as an example
---

cyl = cmds.polyCylinder()
cmds.polySmooth()
cmds.cluster()
cmds.select( cyl[0],r=True )
cmds.polyTriangulate()

query what will be baked
---

cmds.bakePartialHistory( cyl[0],query=True,prePostDeformers=True )

perform the bake, baking history from before and after the
deformer
---

cmds.bakePartialHistory( cyl[0],prePostDeformers=True )

Bake the history before the geometry cache on the cylinder.
To actually demo, add a geometry cache before executing the command
below.
---

cmds.select( cyl[0],r=True )
cmds.bakePartialHistory( cyl[0],preCache=True )

---
Return:
---


    string: name of shapes that were baked

Flags:
---


---
allShapes(all): boolean
    properties: create, query
    Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked.
If this option is specified and there are no shapes in the scene, then this command will do nothing and end successfully.

---
postSmooth(nps): boolean
    properties: create, query
    Specifies whether or not a smoothing operation should be done on skin vertices. This
smoothing is only done on vertices that are found to deviate largely from other
vertex values.  The default is false.

---
preCache(pc): boolean
    properties: create, query
    Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.

---
preDeformers(pre): boolean
    properties: create, query
    Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.

---
prePostDeformers(ppt): boolean
    properties: create, query
    Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the default. In query mode, returns a list of the nodes that will be baked.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bakePartialHistory.html 
    """


def bakeResults(animation: string, attribute: string, bakeOnOverrideLayer: boolean, controlPoints: boolean, destinationLayer: string, disableImplicitControl: boolean, float: floatrange, hierarchy: string, includeUpperBound: boolean, index: uint, minimizeRotation: boolean, oversamplingRate: uint, preserveOutsideKeys: boolean, removeBakedAnimFromLayer: boolean, removeBakedAttributeFromLayer: boolean, resolveWithoutLayer: string, sampleBy: time, shape: boolean, simulation: boolean, smart: bool | list[boolean, float], sparseAnimCurveBake: boolean, time: timerange) -> int:
    """Synopsis:
---
---
 bakeResults(
objects
    , [animation=string], [attribute=string], [bakeOnOverrideLayer=boolean], [controlPoints=boolean], [destinationLayer=string], [disableImplicitControl=boolean], [float=floatrange], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [minimizeRotation=boolean], [oversamplingRate=uint], [preserveOutsideKeys=boolean], [removeBakedAnimFromLayer=boolean], [removeBakedAttributeFromLayer=boolean], [resolveWithoutLayer=string], [sampleBy=time], [shape=boolean], [simulation=boolean], [smart=[[, boolean, float, ]]], [sparseAnimCurveBake=boolean], [time=timerange])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bakeResults is undoable, queryable, and editable.
This command operates on a keyset. A keyset is
defined as a group of keys within a specified time range on one or
more animation curves.

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
If there are no active keys or tangents, do not do anything.



objects:
Only act on specified objects. If there are no objects specified, do not
do anything.



Note that the "-animation" flag can be used to override
the curves uniquely identified by the multi-use
"-attribute" flag, which takes an argument of the form
attributeName, such as "translateX".

Keys on animation curves are identified by either
their time values or their indices. Times and indices should
be specified as a range, as shown below.

-time "10:20" means all keys in the range from 10 to 20,
inclusive, in the current time unit.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of
each animation curve.







Example:
---
import maya.cmds as cmds

To replace the set of nodes controlling the animation of
surface1.translateX with a single animation animCurve, between the
time interval 5-44, with a sampling frequency of 2 timeUnits, use the
following command:
cmds.bakeResults( 'surface1.translateX', t=(5,44), sb=2 )

This bakes the joints on a skeleton over the time interval 1-40.
cmds.bakeResults( 'joint*', t=(1,40), simulation=True )

---
Return:
---


    int: - The number of channels baked

Flags:
---


---
animation(an): string
    properties: create
    Where this command should get the animation to act
on. Valid values are "objects," "keys," and
"keysOrObjects" Default: "keysOrObjects." See
command description for details.

---
attribute(at): string
    properties: create, multiuse
    List of attributes to select
      In query mode, this flag needs a value.

---
bakeOnOverrideLayer(bol): boolean
    properties: create
    If true, all layered and baked attribute will be added as a top override layer.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
destinationLayer(dl): string
    properties: create
    This flag can be used to specify an existing layer where the baked results
should be stored. Use this flag with caution. If the destination layer already has animation on it
that contributes to the final result, it will be replaced by the output of the bake. As a result,
it is possible that the combined animation visible in the scene is different before / after the baking
process.

---
disableImplicitControl(dic): boolean
    properties: create
    Whether to disable implicit control after the anim curves
are obtained as the result of this command. An implicit control
to an attribute is some function that affects the attribute
without using an explicit dependency graph connection. The
control of IK, via ik handles, is an example.

---
float(f): floatrange
    properties: create, multiuse
    value uniquely representing a non-time-based
key (or key range) on a time-based animCurve. Valid
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
Default value: true. This flag is only valid when
the argument to the -t/time flag is a time range with
a lower and upper bound. Note: when used with the "pasteKey"
command, this flag refers only to the time range of the
target curve that is replaced, when using options such
as "replace," "fitReplace," or "scaleReplace." This
flag has no effect on the curve pasted from the clipboard.

---
index(index): uint
    properties: create, multiuse
    index of a key on an animCurve
      In query mode, this flag needs a value.

---
minimizeRotation(mr): boolean
    properties: create
    Specify whether to minimize the local Euler component from key to key during baking of rotation channels.

---
oversamplingRate(osr): uint
    properties: create
    Amount of samples per sampleBy period. Default is 1.

---
preserveOutsideKeys(pok): boolean
    properties: create
    Whether to preserve keys that are outside the bake range
when there are directly connected animation curves or a pairBlend node
which has an animation curve as its direct input. The default
(false) is to remove frames outside the bake range. If the channel
that you are baking is not controlled by a single animation curve,
then a new animation curve will be created with keys only in the
bake range. In the case of pairBlend-driven channels, setting pok to
true will retain both the pairBlend and its input animCurve. The
blended values will be baked onto the animCurve and the weight of the
pairBlend weight will be keyed to the animCurve during the baked
range.

---
removeBakedAnimFromLayer(rba): boolean
    properties: create
    If true, all baked animation will be removed from the layer.
Otherwise all layer associated with the baked animation will be muted.

---
removeBakedAttributeFromLayer(ral): boolean
    properties: create
    If true, all baked attribute will be removed from the layer.
Otherwise all layer associated with the baked attribute will be muted.

---
resolveWithoutLayer(rwl): string
    properties: create, multiuse
    This flag can be used to specify a list of layers to be merged together during the bake process. This
is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines
the proper value to key on the destination layer to achieve the same result as the merged layers.

---
sampleBy(sb): time
    properties: create
    Amount to sample by. Default is 1.0 in current timeUnit.

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
simulation(sm): boolean
    properties: create
    Using this flag instructs the command to preform a simulation instead
of just evaluating each attribute separately over the range of time.
The simulation flag is required to bake animation that depends on
the whole scene being evaluated at each time step such as dynamics. The
default is false.

---
smart(sr): [[, boolean, float, ]]
    properties: create
    Specify whether to enable smart bake and the optional smart bake tolerance.

---
sparseAnimCurveBake(sac): boolean
    properties: create
    When this is true and anim curves are being baked, do not insert
any keys into areas of the curve where animation is defined. And, use
as few keys as possible to bake the pre and post infinity behavior.
When this is false, one key will be inserted at each time step. The
default is false.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bakeResults.html 
    """


def bakeSimulation(animation: string, attribute: string, bakeOnOverrideLayer: boolean, controlPoints: boolean, destinationLayer: string, disableImplicitControl: boolean, float: floatrange, hierarchy: string, includeUpperBound: boolean, index: uint, minimizeRotation: boolean, preserveOutsideKeys: boolean, removeBakedAnimFromLayer: boolean, removeBakedAttributeFromLayer: boolean, resolveWithoutLayer: string, sampleBy: time, shape: boolean, simulation: boolean, smart: bool | list[boolean, float], sparseAnimCurveBake: boolean, time: timerange) -> None:
    """Synopsis:
---
---
 bakeSimulation(
objects
    , [animation=string], [attribute=string], [bakeOnOverrideLayer=boolean], [controlPoints=boolean], [destinationLayer=string], [disableImplicitControl=boolean], [float=floatrange], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [minimizeRotation=boolean], [preserveOutsideKeys=boolean], [removeBakedAnimFromLayer=boolean], [removeBakedAttributeFromLayer=boolean], [resolveWithoutLayer=string], [sampleBy=time], [shape=boolean], [simulation=boolean], [smart=[[, boolean, float, ]]], [sparseAnimCurveBake=boolean], [time=timerange])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bakeSimulation is undoable, queryable, and editable.
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

The bakeSimulation command is obsolete.  Instead, "bakeResults
-simulation true" should be used.  The bakeSimulation command has
retained for backwards compatibility.

This command allows the user to replace a chain of dependency
nodes, or implicit relationship, such as those between joints
and IK handles, which define the value of an attribute, with a
single animation curve. Command allows the user to specify the
range and frequency of sampling. Unlike the bakeResults
command, this command will actually set the time of the
current scene to all the times, in sequence, inside the given time
interval before it sets the time back to when it is started.
As a result, it may modify the scene.




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

To replace the animation driven by an ik handle of joints,
starting from joint1, with separate animCurves, within the
time interval 5-44, with a sampling frequency of 2 timeUnits,
use the following command:
---

cmds.bakeSimulation( 'joint1', t=(5,44), sb=2, at=["rx","ry","rz"], hi="below" )

---


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
bakeOnOverrideLayer(bol): boolean
    properties: create
    If true, all layered and baked attributes will be added as a top override layer.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
destinationLayer(dl): string
    properties: create
    This flag can be used to specify an existing layer where the baked results
should be stored.

---
disableImplicitControl(dic): boolean
    properties: create
    Whether to disable implicit control after the anim curves
are obtained as the result of this command. An implicit control
to an attribute is some function that affects the attribute
without using an explicit dependency graph connection. The
control of IK, via ik handles, is an example.

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
minimizeRotation(mr): boolean
    properties: create
    Specify whether to minimize the local euler component from key to key during baking of rotation channels.

---
preserveOutsideKeys(pok): boolean
    properties: create
    Whether to preserve keys that are outside the bake range
when there are directly connected animation curves.  The default
(false) is to remove frames outside the bake range.  If the channel
that you are baking is not controlled by a single animation curve,
then a new animation curve will be created with keys only in the
bake range.

---
removeBakedAnimFromLayer(rba): boolean
    properties: create
    If true, all baked animation will be removed from the layer.

---
removeBakedAttributeFromLayer(ral): boolean
    properties: create
    If true, all baked attributes will be removed from the layer.

---
resolveWithoutLayer(rwl): string
    properties: create, multiuse
    This flag can be used to specify a list of layers to be merged together during the bake process. This
is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines
the proper value to key on the destination layer to achieve the same result as the merged layers.

---
sampleBy(sb): time
    properties: create
    Amount to sample by. Default is 1.0 in current timeUnit

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
simulation(sm): boolean
    properties: create
    Using this flag instructs the command to preform a simulation instead
of just evaluating each attribute separately over the range of time.
The simulation flag is required to bake animation that that depends on
the whole scene being evaluated at each time step such as dynamics. The
default is true.

---
smart(sr): [[, boolean, float, ]]
    properties: create
    Specify whether to enable smart bake and the optional smart bake tolerance.

---
sparseAnimCurveBake(sac): boolean
    properties: create
    When baking anim curves, do not insert any keys into areas
of the curve where animation is defined.  And, use as few keys
as possible to bake the pre and post infinity behaviors.  When
this is false, one key will be inserted at each time step.  The
default is false.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bakeSimulation.html 
    """


def baseTemplate(exists: boolean, fileName: string, force: boolean, load: boolean, matchFile: string, silent: boolean, unload: boolean, viewList: string) -> None:
    """Synopsis:
---
---
 baseTemplate([string], [exists=boolean], [fileName=string], [force=boolean], [load=boolean], [matchFile=string], [silent=boolean], [unload=boolean], [viewList=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

baseTemplate is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


   Determine if template exists
---

cmds.baseTemplate ('foo.xml', exists=True)
---


---


Flags:
---


---
exists(ex): boolean
    properties: query
    Returns true or false depending upon whether the specified template exists.
When used with the matchFile argument, the query will return true if the
template exists and the filename it was loaded from matches the filename
given.

---
fileName(fn): string
    properties: create, query
    Specifies the filename associated with the template.  This argument can be
used in conjunction with load, save or query modes. If no filename is
associated with a template, a default file name based on the template
name will be used.  It is recommended but not required that the
filename and template name correspond.

---
force(f): boolean
    properties: create
    This flag is used with some actions to allow them to proceed with an
overwrite or destructive operation.
When used with load, it will allow an existing template to be reloaded
from a file.  When used in create mode, it will allow an existing template
to be recreated (for example when using fromContainer argument to
regenerate a template).

---
load(l): boolean
    properties: 
    Load an existing template from a file.
If a filename is specified for the template, the entire file
(and all templates in it) will be loaded.
If no file is specified, a default filename will be assumed,
based on the template name.

---
matchFile(mf): string
    properties: query
    Used in query mode in conjunction with other flags this flag specifies
an optional file name that is to be matched as part of the query operation.
                        In query mode, this flag needs a value.

---
silent(si): boolean
    properties: create, query, edit
    Silent mode will suppress any error or warning messages that would normally be
reported from the command execution.  The return values are unaffected.

---
unload(u): boolean
    properties: create
    Unload the specified template.  This action will not delete the
associated template file if one exists, it merely removes the template
definition from the current session.

---
viewList(vl): string
    properties: create, query
    Used in query mode, returns a list of all views defined on the template.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/baseTemplate.html 
    """


def baseView(itemInfo: string, itemList: boolean, viewDescription: boolean, viewLabel: boolean, viewList: boolean, viewName: string) -> None:
    """Synopsis:
---
---
 baseView(string, [itemInfo=string], [itemList=boolean], [viewDescription=boolean], [viewLabel=boolean], [viewList=boolean], [viewName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

baseView is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


Obtain a list of all available views for template1
---

cmds.baseView ( 'AEblinn', query=True, viewList=True);
Result: [u'Animation', u'Rendering'] ---

---


---


Flags:
---


---
itemInfo(ii): string
    properties: query
    Used in query mode in conjunction with the itemList flag.
The command will return a list of information for each item in the view, the
information fields returned for each item are determined by this argument value.
The information fields will be listed in the string array returned.
The order in which the keyword is specified will determine the order in which
the data will be returned by the command.
One or more of the following keywords, separated by colons ':' are used to
specify the argument value.

itemIndex  : sequential item number (0-based)
itemName   : item name (string)
itemLabel  : item display label (string)
itemDescription : item description field (string)
itemLevel  : item hierarchy level (0-n)
itemIsGroup : (boolean 0 or 1) indicates whether or not this item is a group
itemIsAttribute : (boolean 0 or 1) indicates whether or not this item is an attribute
itemNumChildren: number of immediate children (groups or attributes) of this item
itemAttrType : item attribute type (string)
itemCallback : item callback field (string)

In query mode, this flag needs a value.

---
itemList(il): boolean
    properties: query
    Used in query mode, the command will return a list of information for each item in
the view.  The viewName flag is used to select the view to query.
The information returned about each item is determined by the itemInfo argument value.
For efficiency, it is best to query all necessary item information at one time
(to avoid recomputing the view information on each call).

---
viewDescription(vd): boolean
    properties: query
    Used in query mode, returns the description field associated with the
selected view.
If no description was defined for this view, the value will be empty.

---
viewLabel(vb): boolean
    properties: query
    Used in query mode, returns the display label associated with the view.
An appropriate label suitable for the user interface will be
returned based on the selected view.  Use of the view label
is usually more suitable than the view name for display purposes.

---
viewList(vl): boolean
    properties: query
    Used in query mode, command will return a list of all views defined for the
given target (container or template).

---
viewName(vn): string
    properties: query
    Used in query mode, specifies the name of the queried view when used in
conjunction with a template target. When used in conjunction with a container
target, it requires no string argument, and returns the name of the currently
active view associated with the container; this value may be empty if the
current view is not a valid template view or is generated by one of the
built-in views modes. For this reason, the view label is generally more
suitable for display purposes.
                        In query mode, this flag can accept a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/baseView.html 
    """


def batchRender(filename: string, melCommand: string, numProcs: int, preRenderCommand: string, remoteRenderMachine: string, renderCommandOptions: string, showImage: boolean, status: string, useRemoteRender: boolean, useStandalone: boolean, verbosity: int) -> None:
    """Synopsis:
---
---
 batchRender([filename=string], [melCommand=string], [numProcs=int], [preRenderCommand=string], [remoteRenderMachine=string], [renderCommandOptions=string], [showImage=boolean], [status=string], [useRemoteRender=boolean], [useStandalone=boolean], [verbosity=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

batchRender is undoable, NOT queryable, and NOT editable.

The batchRender will spawn a separate maya process in which
commands will be communicated to it through a commandPort. If Maya
is unable to find an available port an error will be
produced. Maya will attempt to use ports 7835 through 7844.




Example:
---
import maya.cmds as cmds

cmds.batchRender()

cmds.batchRender( 'mayafile' )

---


Flags:
---


---
filename(f): string
    properties: create
    Filename to be rendered; if empty, a temporary filename will be created.

---
melCommand(mc): string
    properties: create
    Mel command to execute to run a renderer other than the software renderer.

---
numProcs(n): int
    properties: create
    Number of processors to use (0 means use all available processors).

---
preRenderCommand(prc): string
    properties: create
    Command to be run prior to invoking a batch render.

---
remoteRenderMachine(rm): string
    properties: create
    Name of remote render machine. Not available on Windows.

---
renderCommandOptions(rco): string
    properties: create
    Arguments to the render command for batch rendering.

---
showImage(si): boolean
    properties: create
    Show progress of the current rendering job.

---
status(st): string
    properties: create
    Status string for displaying the batch render status.

---
useRemoteRender(um): boolean
    properties: create
    If remote rendering is desired. Not available on Windows.

---
useStandalone(us): boolean
    properties: create
    Batch rendering is to be done by exporting the scene and rendering with a standalone renderer.

---
verbosity(v): int
    properties: create
    Defines the verbosity level to report the batch rendering
status:
1: display only one start message, then one message when all
frames are rendered.
2: display only start and end frame messages.
3: display all messages (default).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/batchRender.html 
    """


def bevel(bevelShapeType: int, caching: boolean, constructionHistory: boolean, cornerType: int, depth: linear, extrudeDepth: linear, joinSurfaces: boolean, name: string, nodeState: int, numberOfSides: int, object: boolean, polygon: int, range: boolean, tolerance: linear, width: linear) -> list[string]:
    """Synopsis:
---
---
 bevel(
[object]
    , [bevelShapeType=int], [caching=boolean], [constructionHistory=boolean], [cornerType=int], [depth=linear], [extrudeDepth=linear], [joinSurfaces=boolean], [name=string], [nodeState=int], [numberOfSides=int], [object=boolean], [polygon=int], [range=boolean], [tolerance=linear], [width=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bevel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Bevel (one) active curve with a width and depth of 1.5:
cmds.bevel( w=1.5, d=1.5 )

Create a single-sided bevel (at start) surface using the specified
curve (with the default dimensions):
cmds.bevel( 'curve1', ns=2 )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
bevelShapeType(bst): int
    properties: create, query, edit
    Shape type: 1 - straight cut, 2 - curve out, 3 - curve in
Default: 1

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
cornerType(ct): int
    properties: create, query, edit
    Corner type: 1 - linear, 2 - circular
Default: 2

---
depth(d): linear
    properties: create, query, edit
    The depth for bevel
Default: 0.5

---
extrudeDepth(ed): linear
    properties: create, query, edit
    The extrude depth for bevel
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
tolerance(tol): linear
    properties: create, query, edit
    The tolerance for bevel offsets
Default: 0.01

---
width(w): linear
    properties: create, query, edit
    The width for bevel
Default: 0.5

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
joinSurfaces(js): boolean
    properties: create, query, edit
    Attach bevelled surfaces into one surface for each
input curve.
Default:true

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
numberOfSides(ns): int
    properties: create, query, edit
    How to apply the bevel.

1 - no bevels
2 - bevel at start only
3 - bevel at end only
4 - bevel at start and end

Default: 4

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bevel.html 
    """


def bevelPlus(bevelInside: boolean, capSides: int, constructionHistory: boolean, innerStyle: int, joinSurfaces: boolean, name: string, normalsOutwards: boolean, numberOfSides: int, outerStyle: int, polygon: int, range: boolean) -> list[string]:
    """Synopsis:
---
---
 bevelPlus(
curve [curve curve...]
    , [bevelInside=boolean], [capSides=int], [constructionHistory=boolean], [innerStyle=int], [joinSurfaces=boolean], [name=string], [normalsOutwards=boolean], [numberOfSides=int], [outerStyle=int], [polygon=int], [range=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bevelPlus is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.circle()
cmds.scale( 10, 10, 10, r=True )
cmds.circle()
cmds.scale( 5, 5, 5, r=True )
cmds.bevelPlus( 'nurbsCircle1', 'nurbsCircle2', po=1, cap=4, outerStyle=2, innerStyle=4 )

---
Return:
---


    list[string]: Object name(s) and node name

Flags:
---


---
bevelInside(bin): boolean
    properties: create, query, edit
    If true, ensure surface always remains within the original profile curve
Default: false

---
capSides(cap): int
    properties: create, query
    How to cap the bevel.

1 - no caps
2 - cap at start only
3 - cap at end only
4 - cap at start and end

Default:4

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
innerStyle(innerStyle): int
    properties: create, query, edit
    Similar to outerStyle, this style is applied to all
but the first (outer) curve specified.

---
joinSurfaces(js): boolean
    properties: create, query, edit
    Attach bevelled surfaces into one surface for each
input curve.
Default:true

---
name(n): string
    properties: create
    Sets the name of the newly-created node. If it contains
namespace path, the new node will be created under the
specified namespace; if the namespace does not exist, it
will be created.

---
normalsOutwards(no): boolean
    properties: create, query, edit
    If enabled, the normals point outwards on the
resulting NURBS or poly surface.

---
numberOfSides(ns): int
    properties: create, query, edit
    How to apply the bevel.

1 - no bevels
2 - bevel at start only
3 - bevel at end only
4 - bevel at start and end

Default: 4

---
outerStyle(os): int
    properties: create, query, edit
    Choose a style to use for the bevel of the first (outer)
curve.  There are 15 predefined styles (values 0 to 14 can be used
to select them). For those experienced with MEL, you can, after
the fact, specify a custom curve and use it for the style curve.
See the documentation for styleCurve node to see what requirements
a style curve must satisfy.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bevelPlus.html 
    """


def bezierAnchorPreset(preset: int) -> int:
    """Synopsis:
---
---
 bezierAnchorPreset([preset=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bezierAnchorPreset is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Applies the "Bezier" anchor preset to all selected anchors
cmds.bezierAnchorPreset( p=0 )

Applies the "Bezier Corner" anchor preset to all selected anchors
cmds.bezierAnchorPreset( p=1 )

Applies the "Corner" anchor preset to all selected anchors
cmds.bezierAnchorPreset( p=2 )

---
Return:
---


    int: (number of modified anchors)

Flags:
---


---
preset(p): int
    properties: create
    Selects a preset to apply to selected Bezier anchors. Valid arguments are:

0: Bezier
1: Bezier Corner
2: Corner

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bezierAnchorPreset.html 
    """


def bezierAnchorState(even: boolean, smooth: boolean) -> int:
    """Synopsis:
---
---
 bezierAnchorState([even=boolean], [smooth=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bezierAnchorState is undoable, NOT queryable, and NOT editable.
- Smooth/Broken anchor tangents
- Even/Uneven weighted anchor tangents




Example:
---
import maya.cmds as cmds

Sets all selected anchors (or attached tangent handles) to smooth and uneven
cmds.bezierAnchorState( sm=1, ev=0 )

---
Return:
---


    int: (number of modified anchors)

Flags:
---


---
even(ev): boolean
    properties: create
    Sets selected anchors (or attached tangent handles) to even weighting when true, uneven otherwise.

---
smooth(sm): boolean
    properties: create
    Sets selected anchors (or attached tangent handles) to smooth when true, broken otherwise.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bezierAnchorState.html 
    """


def bezierCurveToNurbs() -> list[string]:
    """Synopsis:
---
---
 bezierCurveToNurbs(
curve
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bezierCurveToNurbs is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.bezierCurveToNurbs( )
Converts call selected Bezier curves to NURBS curves.

---
Return:
---


    list[string]: (object name and node name)

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bezierCurveToNurbs.html 
    """


def bezierInfo(anchorFromCV: int, cvFromAnchor: int, isAnchorSelected: boolean, isTangentSelected: boolean, onlyAnchorsSelected: boolean, onlyTangentsSelected: boolean) -> int:
    """Synopsis:
---
---
 bezierInfo([anchorFromCV=int], [cvFromAnchor=int], [isAnchorSelected=boolean], [isTangentSelected=boolean], [onlyAnchorsSelected=boolean], [onlyTangentsSelected=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bezierInfo is undoable, NOT queryable, and NOT editable.




Example:
---
import maya.cmds as cmds

Queries the CV index of the anchor index 1
cmds.bezierInfo( cfa=1 )

Queries the anchor index of a CV index 3
cmds.bezierInfo( afc=3 );

---
Return:
---


    int: Queried value

Flags:
---


---
anchorFromCV(afc): int
    properties: create
    Returns the Bezier anchor index from a given CV index

---
cvFromAnchor(cfa): int
    properties: create
    Returns the CV index for a given Bezier anchor index

---
isAnchorSelected(ias): boolean
    properties: create
    Returns 1 if an anchor CV is currently selected. 0, otherwise.

---
isTangentSelected(its): boolean
    properties: create
    Returns 1 if a tangent CV is currently selected. 0, otherwise.

---
onlyAnchorsSelected(oas): boolean
    properties: create
    Returns 1 if the only CV components selected are anchor CVs. 0, otherwise.

---
onlyTangentsSelected(ots): boolean
    properties: create
    Returns 1 if the only CV components selected are tangent CVs. 0, otherwise.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bezierInfo.html 
    """


def binMembership(addToBin: string, exists: string, inheritBinsFromNodes: name, isValidBinName: string, listBins: boolean, makeExclusive: string, notifyChanged: boolean, removeFromBin: string) -> boolean:
    """Synopsis:
---
---
 binMembership([addToBin=string], [exists=string], [inheritBinsFromNodes=name], [isValidBinName=string], [listBins=boolean], [makeExclusive=string], [notifyChanged=boolean], [removeFromBin=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

binMembership is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Add a given node to a bin.
---

cmds.binMembership( 'lambert1', addToBin='wood' )

Add a selection of nodes to a given bin.
---

newLambertNode = cmds.createNode('lambert')
list = ("lambert1", newLambertNode)
cmds.binMembership( list, addToBin='grass' )

Check if a node exists in a bin.
---

cmds.binMembership( 'lambert1', exists='wood' )

Query and return all the nodes which belong to the bin.
---

newLambertNode = cmds.createNode('lambert')
nodeList = ("lambert1", newLambertNode)
cmds.binMembership( nodeList, query=True, listBins=True )

Make the nodes belong exclusively in bin "wood".
---

newLambertNode = cmds.createNode('lambert')
nodeList = ("lambert1", newLambertNode)
cmds.binMembership( nodeList, makeExclusive='wood' )

Let the dest node inherit bins from nodes in the src node list.
The dest node is specified by the "inheritBinsFromNodes" flag's
argument.
---

cmds.binMembership( 'lambert1', addToBin='wood' )
node = cmds.createNode('lambert')
cmds.binMembership( node, addToBin='grass' )
srcNodeList = ("lambert1", node)
destNode = cmds.createNode('blinn')
cmds.binMembership( srcNodeList, inheritBinsFromNodes=destNode )

Notify that binMembership has been changed.
---

cmds.binMembership( notifyChanged=True )

Check if a bin name is valid or not.  If valid, return true.
Otherwise, return false.
---

cmds.binMembership( isValidBinName='wood' )

---
Return:
---


    boolean: Command result

Flags:
---


---
addToBin(add): string
    properties: create
    Add the nodes in a node list to a bin.

---
exists(ex): string
    properties: create
    Query if a node exists in a bin.  The exists flag can take only one node.

---
inheritBinsFromNodes(ibn): name
    properties: create
    Let the node in the flag's argument inherit bins from nodes
in the specified node list.  The node list is specified as the
object of the command.

---
isValidBinName(ivn): string
    properties: create
    Query if the specified bin name is valid.  If so, return true.
Otherwise, return false.

---
listBins(lb): boolean
    properties: create, query
    Query and return a list of bins a list of nodes belong to.
If a bin contains any of the nodes in the selection list,
then it should be included
in the returned bin list.

---
makeExclusive(mke): string
    properties: create
    Make the specified nodes belong exclusively in the specified bin.

---
notifyChanged(nfc): boolean
    properties: create
    This flag is used to notify that binMembership has been changed.

---
removeFromBin(rm): string
    properties: create
    Remove the nodes in a node list from a bin.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/binMembership.html 
    """


def bindSkin(byClosestPoint: boolean, byPartition: boolean, colorJoints: boolean, delete: boolean, doNotDescend: boolean, enable: boolean, name: string, partition: string, toAll: boolean, toSelectedBones: boolean, toSkeleton: boolean, unbind: boolean, unbindKeepHistory: boolean, unlock: boolean) -> string:
    """Synopsis:
---
---
 bindSkin(
[objects]
    , [byClosestPoint=boolean], [byPartition=boolean], [colorJoints=boolean], [delete=boolean], [doNotDescend=boolean], [enable=boolean], [name=string], [partition=string], [toAll=boolean], [toSelectedBones=boolean], [toSkeleton=boolean], [unbind=boolean], [unbindKeepHistory=boolean], [unlock=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bindSkin is undoable, queryable, and editable.

The skin is bound using the so-called "rigid" bind, in which
the components are rigidly attached to the closest bone in the
skeleton. Flexors can later be added to the skeleton to
smooth out the skinning around joints.

The skin(s) can be bound either to the entire skeleton hierarchy
of the selected joint(s), or to only the selected joints. The
entire hierarchy is the default. The -tsb/-toSelectedBones flag
allows binding to only the selected bones.

This command can also be used to detach the skin from the skeleton.
Detaching the skin is useful in a variety of situations, such as:
inserting additional bones, deleting bones, changing the bind
position of the skeleton or skin, or simply getting rid of the
skinning nodes altogether. The options to use when detaching the
skin depend on how much of the skinning info you want to get rid
of. Namely: (1) -delete or -unbind: remove all skinning nodes, (2) -unbindKeepHistory: remove the skinning sets, but keep the weights, (3) -disable: disable the skinning but keep the skinning sets and the weights.




Example:
---
import maya.cmds as cmds

Create a joint chain and a polygonal plane.
cmds.select(d=True)
cmds.joint(p=(-3.0, 0.0,-12.0))
cmds.joint(p=(-3.0, 0.0, -5.0))
cmds.joint(p=(1.0, 0.0, 5.5))
cmds.joint(p=(6.0, 0.0, 10.0))
cmds.polyPlane(w=20.0,h=20.0,sx=25,sy=25)

cmds.select('joint1',add=True)

to bind the selected objects to the selected skeleton
---

cmds.bindSkin()

to bind nurbsSphere1 and pPlane1 to the skeleton containing joint2
---

cmds.bindSkin( 'nurbsSphere1', 'joint2', 'pPlane1' )

to bind the selected partition to the selected skeleton
---

cmds.bindSkin( bp=True )

to bind the selected objects to the selected bones only,
not the entire skeleton
---

cmds.bindSkin( tsb=True )

to detach the selected objects and delete any unused
bindSkin history
---

cmds.bindSkin( unbind=True )

to detach pPlane1 and delete any unused
bindSkin history
---

cmds.bindSkin( 'pPlane1', unbind=True )

to detach the selected objects and keep the history
---

cmds.bindSkin( unbindKeepHistory=True )

To disable the skin on the selected skeletons. This gives
the effect of detaching the skin without removing the
bindSkin groups on the object. You can then modify the joint
positioning, and enable the binding, keeping your original
groups.
---

cmds.bindSkin( enable=False )

to enable skin on a skeleton which has been disabled
---

cmds.bindSkin( enable=True )

---
Return:
---


    string: Command result

Flags:
---


---
byClosestPoint(bcp): boolean
    properties: create
    bind each point in the object to the segment closest to the point.
The byClosestPoint and byPartition flags are mutually
exclusive.  The byClosestPoint flag is the default.

---
byPartition(bp): boolean
    properties: create
    bind each group in the partition to the segment
closest to the group's centroid. A partition must be specified
with the -p/-partition flag

---
colorJoints(cj): boolean
    properties: create
    In bind mode, this flag assigns colors to the joints based
on the colors assigned to the joint's skin set.
In delete and unlock mode, this flag removes the colors from
joints that are no longer bound as skin.
In disable and unbindKeepHistory mode, this flag does nothing.

---
delete(d): boolean
    properties: create
    Detach the skin on the selected skeletons and remove all bind-
related construction history.

---
doNotDescend(dnd): boolean
    properties: create
    Do not descend to shapes that are parented below the selected
object(s).
Bind only the selected objects.

---
enable(en): boolean
    properties: create
    Enable or disable a bind that has been disabled on the selected
skeletons.
To enable the bind on selected bones only, select the bones and
use the -tsb flag with the -en flag. This flag is used when you
want to temporarily disable the bind without losing the set
information or the weight information of the skinning, for example
if you want to modify the bindPose.

---
name(n): string
    properties: create
    This flag is obsolete.

---
partition(p): string
    properties: create
    Specify a partition to bind by. This is only valid when
used with the -bp/-byPartition flag.

---
toAll(ta): boolean
    properties: create
    objects will be bound to the entire selected skeletons. Even bones with zero influence
will be bound, whereas the toSkeleton will only bind non-zero influences.

---
toSelectedBones(tsb): boolean
    properties: create
    objects will be bound to the selected bones only.

---
toSkeleton(ts): boolean
    properties: create
    objects will be bound to the selected skeletons. The toSkeleton, toAll
and toSelectedBones flags are mutually exclusive. The toSkeleton flag is the default.

---
unbind(ub): boolean
    properties: create
    unbind the selected objects. They will no longer move with
the skeleton. Any bindSkin history that is no longer used
will be deleted.

---
unbindKeepHistory(ubk): boolean
    properties: create
    unbind the selected objects. They will no longer move with
the skeleton. However, existing weights on the skin
will be kept for use the next time the skin is bound. This option
is appropriate if you want to modify the skeleton without losing
the weighting information on the skin.

---
unlock(ul): boolean
    properties: create
    unlock the selected objects. Since bindSkin will no longer give
normal results if bound objects are moved away from the skeleton,
bindSkin locks translate, rotate and scale. This command unlocks
the selected objects translate, rotate and scale.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bindSkin.html 
    """


def blend2(autoAnchor: boolean, autoNormal: boolean, caching: boolean, constructionHistory: boolean, crvsInFirstRail: int, flipLeftNormal: boolean, flipRightNormal: boolean, leftAnchor: float, leftEnd: float, leftStart: float, multipleKnots: boolean, name: string, nodeState: int, object: boolean, polygon: int, positionTolerance: float, reverseLeft: boolean, reverseRight: boolean, rightAnchor: float, rightEnd: float, rightStart: float, tangentTolerance: float) -> list[string]:
    """Synopsis:
---
---
 blend2(
curve curve [curve...]
    , [autoAnchor=boolean], [autoNormal=boolean], [caching=boolean], [constructionHistory=boolean], [crvsInFirstRail=int], [flipLeftNormal=boolean], [flipRightNormal=boolean], [leftAnchor=float], [leftEnd=float], [leftStart=float], [multipleKnots=boolean], [name=string], [nodeState=int], [object=boolean], [polygon=int], [positionTolerance=float], [reverseLeft=boolean], [reverseRight=boolean], [rightAnchor=float], [rightEnd=float], [rightStart=float], [tangentTolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

blend2 is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Do blend with auto normal and with no history:
cmds.blend2( an=True, ch=False )

Do blend without auto normal
cmds.blend2( an=False, fln=True, frn=True )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
autoAnchor(aa): boolean
    properties: create, query, edit
    If true and both paths are closed, automatically determine the value on the right rail so that they match
Default: true

---
autoNormal(an): boolean
    properties: create, query, edit
    If true, the direction of each starting tangent is computed based on given geometry.
Default: true

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
flipLeftNormal(fln): boolean
    properties: create, query, edit
    If true, flip the starting tangent off the left boundary.
Default: false

---
flipRightNormal(frn): boolean
    properties: create, query, edit
    If true, flip the starting tangent off the right boundary.
Default: false

---
leftAnchor(la): float
    properties: create, query, edit
    The reference parameter on the left boundary where the blend surface starts in the case of the closed rail.
Default: 0.0

---
leftEnd(le): float
    properties: create, query, edit
    The reference parameter on the left boundary where the blend surface ends.
Default: 1.0

---
leftStart(ls): float
    properties: create, query, edit
    The reference parameter on the left boundary where the blend surface starts.
Default: 0.0

---
multipleKnots(mk): boolean
    properties: create, query, edit
    If true, use the new blend which produces fully multiple interior knots
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
positionTolerance(pt): float
    properties: create, query, edit
    The positional C(0) tolerance of the blend surface to the adjacent surfaces.
Default: 0.1

---
reverseLeft(rvl): boolean
    properties: create, query, edit
    If true, reverse the direction off the left boundary.  autoDirection must be false for this value to be considered.
Default: false

---
reverseRight(rvr): boolean
    properties: create, query, edit
    If true, reverse the direction of the right boundary.  autoDirection must be false for this value to be considered.
Default: false

---
rightAnchor(ra): float
    properties: create, query, edit
    The reference parameter on the right boundary where the blend surface starts in the case of the closed rail.
Default: 0.0

---
rightEnd(re): float
    properties: create, query, edit
    The reference parameter on the right boundary where the blend surface ends.
Default: 1.0

---
rightStart(rs): float
    properties: create, query, edit
    The reference parameter on the right boundary where the blend surface starts.
Default: 0.0

---
tangentTolerance(tt): float
    properties: create, query, edit
    The tangent G(1) continuity tolerance of the blend surface to the adjacent surfaces.
Default: 0.1

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
crvsInFirstRail(cfr): int
    properties: create, query, edit
    Number of curves in the first rail of the blend.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/blend2.html 
    """


def blendShape(after: boolean, afterReference: boolean, automatic: boolean, before: boolean, components: boolean, copyDelta: tuple[uint, uint, uint], copyInBetweenDelta: tuple[uint, uint, uint, uint], copyWeights: tuple[uint, uint, uint], deformerTools: boolean, editTarget: boolean, envelope: float, exclusive: string, export: string, exportTarget: tuple[int, int], flipTarget: tuple[uint, uint], frontOfChain: boolean, geometry: string, geometryIndices: boolean, ignoreSelected: boolean, inBetween: boolean, inBetweenIndex: uint, inBetweenType: string, includeHiddenSelections: boolean, ip: string, mergeSource: int, mergeTarget: uint, mirrorDirection: uint, mirrorTarget: tuple[uint, uint], name: string, normalizationGroups: boolean, origin: string, parallel: boolean, prune: boolean, remove: boolean, resetTargetDelta: tuple[uint, uint], selectedComponents: boolean, split: boolean, suppressDialog: boolean, symmetryAxis: string, symmetryEdge: string, symmetrySpace: uint, tangentSpace: boolean, target: [string, uint, string, float], topologyCheck: boolean, transform: string, useComponentTags: boolean, weight: tuple[uint, float], weightCount: uint) -> list[string]:
    """Synopsis:
---
---
 blendShape(
[objects]
    , [after=boolean], [afterReference=boolean], [automatic=boolean], [before=boolean], [components=boolean], [copyDelta=[uint, uint, uint]], [copyInBetweenDelta=[uint, uint, uint, uint]], [copyWeights=[uint, uint, uint]], [deformerTools=boolean], [editTarget=boolean], [envelope=float], [exclusive=string], [export=string], [exportTarget=[int, int]], [flipTarget=[uint, uint]], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [inBetween=boolean], [inBetweenIndex=uint], [inBetweenType=string], [includeHiddenSelections=boolean], [ip=string], [mergeSource=int], [mergeTarget=uint], [mirrorDirection=uint], [mirrorTarget=[uint, uint]], [name=string], [normalizationGroups=boolean], [origin=string], [parallel=boolean], [prune=boolean], [remove=boolean], [resetTargetDelta=[uint, uint]], [selectedComponents=boolean], [split=boolean], [suppressDialog=boolean], [symmetryAxis=string], [symmetryEdge=string], [symmetrySpace=uint], [tangentSpace=boolean], [target=[string, uint, string, float]], [topologyCheck=boolean], [transform=string], [useComponentTags=boolean], [weight=[uint, float]], [weightCount=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

blendShape is undoable, queryable, and editable.
In the create mode the first item on the selection list is treated
as the base and the remaining inputs as targets. If the first item
on the list has multiple shapes grouped beneath it, the targets must
have an identical shape hierarchy. Additional base shapes
can be added in edit mode using the deformers -g flag.




Example:
---
import maya.cmds as cmds

---

Perform a blendShape using the currently-selected objects.
The lead (last-selected) object will be the base shape, and each
of the others become targets.
---

cmds.blendShape()

---

Create a blendShape that starts with curve3 as the base, and blends
in curve1 and curve2 as targets.

cmds.blendShape( 'curve1', 'curve2', 'curve3' )

---

Apply 80% of the total blendShape deformation, by setting
the envelope parameter to 0.8
cmds.blendShape( 'blendShape1', edit=True, en=0.8 )


---

Set the weights for the first two target shapes to 0.6
and 0.1 respecxtively
cmds.blendShape( 'blendShape1', edit=True, w=[(0, 0.6), (1, 0.1)] )

---

Add a third target (target3) to the blendShape on curve3
cmds.blendShape( 'blendShape1', edit=True, t=('curve3', 1, 'target3', 1.0) )

---

Add an inbetween (smirk) on target3 for base shape curve3
The inbetween will take effect at a weight of 0.2
cmds.blendShape( 'blendShape2', edit=True, ib=True, t=('curve3', 2, 'smirk', 0.2) )

Edit target 1
---

cmds.sculptTarget( 'blendShape1', e=True, target=1 )

Query the edit target
---

cmds.blendShape( 'blendShape1', q=True, edt=True )

---
Return:
---


    list[string]: (the blendShape node name)

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
automatic(at): boolean
    properties: create, edit
    The -automatic flag is used to specify deformer ordering in a way that
choses between -frontOfChain and -before automatically. If the geometry being
deformed is only affected by invertible deformers, the -frontOfChain mode is used, otherwise
the -before mode is used.

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
copyDelta(cd): [uint, uint, uint]
    properties: edit
    Set the base, source, and destination delta index values.

---
copyInBetweenDelta(cid): [uint, uint, uint, uint]
    properties: edit
    Set the base, target, source, and destination delta index values.

---
copyWeights(cw): [uint, uint, uint]
    properties: edit
    Copy base, source, and destination weight index values.

---
deformerTools(dt): boolean
    properties: query
    Returns the name of the deformer tool objects (if any)
as string string ...

---
editTarget(edt) 2024: boolean
    properties: query
    Returns the name of the edit target of a blendShape, if any, as it appears in
the Shape Editor. If the target being edited is an in-between, it will append
the value of the in-between to the shape name (e.g., pSphere2_0.564).

---
envelope(en): float
    properties: create, query, edit
    Set the envelope value for the deformer, controlling
how much of the total deformation gets applied. Default is 1.0.

---
exclusive(ex): string
    properties: create, query
    Puts the deformation set in a deform partition.

---
export(ep): string
    properties: edit
    Export the shapes to the named file path.

---
exportTarget(et): [int, int]
    properties: edit, multiuse
    Specify the base and target index pairs for the export.

---
flipTarget(ft): [uint, uint]
    properties: edit, multiuse
    Flip the list of base and target pairs.

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
ip(ip): string
    properties: edit
    Import the shapes from the named file path.

---
inBetween(ib): boolean
    properties: create, edit
    Indicate that the specified target should serve as
an inbetween. An inbetween target is one that serves as an
intermediate target between the base shape and another target.

---
inBetweenIndex(ibi): uint
    properties: edit
    Only used with the -rtd/-resetTargetDelta flag to remove delta values
for points in the inbetween target geometry defined by this index.

---
inBetweenType(ibt): string
    properties: create, edit
    Specify if the in-between target to be created is relative to the hero
target or if it is absolute.
If it is relative to hero targets, the in-between target will get any changes made to the hero target.
Valid values are "relative" and "absolute".
This flag should always be used with the -ib/-inBetween and -t/-target flags.

---
includeHiddenSelections(ihs): boolean
    properties: create
    Apply the deformer to any visible and hidden objects in the selection list.
Default is false.

---
mergeSource(mgs): int
    properties: edit, multiuse
    List of source indexes for a merge.

---
mergeTarget(mgt): uint
    properties: edit
    Target index of a merge

---
mirrorDirection(md): uint
    properties: edit
    Mirror direction; 0 = negative, 1 = positive

---
mirrorTarget(mt): [uint, uint]
    properties: edit, multiuse
    Mirror the list of base and target pairs.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
normalizationGroups(ng): boolean
    properties: query
    Returns a list of the used normalization group IDs.

---
origin(o): string
    properties: create
    blendShape will be performed with respect to the
world by default. Valid values are "world" and "local". The local flag will cause the blend
shape to be performed with respect to the shape's local
origin.

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
resetTargetDelta(rtd): [uint, uint]
    properties: edit, multiuse
    Remove all delta values for points in the target geometry,
including all sequential targets defined by target index.
Parameter list:

uint: the base object index
uint: the target index

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
suppressDialog(sd): boolean
    properties: create, edit
    Suppress dialog box and run the command as defined by the user.

---
symmetryAxis(sa): string
    properties: query, edit
    Axis for symmetry. Valid values are "X", "Y", and "Z".

---
symmetryEdge(se): string
    properties: query, edit, multiuse
    One or two symmetry edge names, separated by a ".". See the blendShape node's
symmetryEdge attribute for legal values.

---
symmetrySpace(ss): uint
    properties: query, edit
    Space for symmetry. 0 = Topological, 1 = Object, 2 = UV

---
tangentSpace(ts): boolean
    properties: create, edit
    Indicate that the delta of the specified target should be relative to
the tangent space of the surface.

---
target(t): [string, uint, string, float]
    properties: create, query, edit, multiuse
    Set target object as the index target shape for the base shape base
object. The full influence of target shape takes effect when its shape
weight is targetValue.
Parameter list:

string: the base object
int: index
string: the target object
double: target value

---
topologyCheck(tc): boolean
    properties: create
    Set the state of checking for a topology match between the
shapes being blended. Default is on.

---
transform(tr): string
    properties: query, edit
    Set transform for target, then the deltas will become relative to a post transform. Typically the
best workflow for this option is to choose a joint that is related to the fix you have introduced.
This flag should be used only if the "Deformation order" of blendShape node is "Before".

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

---
weight(w): [uint, float]
    properties: create, query, edit, multiuse
    Set the weight value (second parameter) at index (first parameter).

---
weightCount(wc): uint
    properties: create, query, edit
    Set the number of shape weight values.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/blendShape.html 
    """


def blendShapeEditor(control: boolean, defineTemplate: string, docTag: string, exists: boolean, filter: string, forceMainConnection: string, highlightConnection: string, lockMainConnection: boolean, mainListConnection: string, panel: string, parent: string, selectionConnection: string, stateString: boolean, targetControlList: boolean, targetList: boolean, unParent: boolean, unlockMainConnection: boolean, updateMainConnection: boolean, useTemplate: string, verticalSliders: boolean) -> string:
    """Synopsis:
---
---
 blendShapeEditor(
string
    , [control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightConnection=string], [lockMainConnection=boolean], [mainListConnection=string], [panel=string], [parent=string], [selectionConnection=string], [stateString=boolean], [targetControlList=boolean], [targetList=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string], [verticalSliders=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

blendShapeEditor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.blendShapeEditor( 'libEd' )

---
Return:
---


    string: The name of the editor

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/blendShapeEditor.html 
    """


def blendShapePanel(blendShapeEditor: boolean, control: boolean, copy: string, createString: boolean, defineTemplate: string, docTag: string, editString: boolean, exists: boolean, init: boolean, isUnique: boolean, label: string, menuBarRepeatLast: boolean, menuBarVisible: boolean, needsInit: boolean, parent: string, popupMenuProcedure: script, replacePanel: string, tearOff: boolean, tearOffCopy: string, tearOffRestore: boolean, unParent: boolean, useTemplate: string) -> string:
    """Synopsis:
---
---
 blendShapePanel(
string
    , [blendShapeEditor=boolean], [control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

blendShapePanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.blendShapePanel( 'bsP' )

---
Return:
---


    string: The name of the panel

Flags:
---


---
blendShapeEditor(be): boolean
    properties: query
    Query only flag that returns the name of an editor to be associated with the panel.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/blendShapePanel.html 
    """


def blendTwoAttr(attribute: string, attribute0: name, attribute1: name, blender: name, controlPoints: boolean, driver: int, name: string, shape: boolean, time: timerange) -> list[string]:
    """Synopsis:
---
---
 blendTwoAttr(
[objects]
    , [attribute=string], [attribute0=name], [attribute1=name], [blender=name], [controlPoints=boolean], [driver=int], [name=string], [shape=boolean], [time=timerange])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

blendTwoAttr is undoable, queryable, and editable.     (1 - blendFunction) * input[0]  +  blendFunction * input[1] 
The blendTwoAttr command can be used to blend the animation of an
object to transition smoothly between the animation of two other
objects.

When the blendTwoAttr command is issued, it creates a blendTwoAttr
node on the specified attributes, and reconnects whatever was previously
connected to the attributes to the new blend nodes. You may also
specify which two attributes should be used to blend together.

The driver is used when you want to keyframe an object after it is
being animated by a blend node. The current driver index specifies
which of the two blended attributes should be keyframed.




Example:
---
import maya.cmds as cmds

Assume we have animated a bouncing sphere, sphere1, and we would like
the sphere to smoothly transition into following a second sphere's,
sphere2, animation between time 15 and 20.
---

cmds.select( 'sphere1' )
cmds.blendTwoAttr( at='tx', at1='sphere2.tx', t=(15,20) )
cmds.blendTwoAttr( at='ty', at1='sphere2.ty', t=(15,20) )
cmds.blendTwoAttr( at='tz', at1='sphere2.tz', t=(15,20) )

You can use the "-at" flag to narrow the query. For example, if
you wanted to know the names of the newly created blender curves
for only the tx and tz attributes of sphere1, you could say:
---

cmds.blendTwoAttr( at=['tx','tz'], query=True, blender=True )

You can now keyframe the sphere2's animation by changing the
driver on sphere1.
---

cmds.blendTwoAttr( at='tx', edit=True, driver=1 )
setKeyframe ...

If you already had two objects, sphere1 and sphere2 animated, and
you wanted to blend between their animation abruptly at time 15,
you could do:
---

cmds.blendTwoAttr( 'newObject.tx', t=(15,15), at0='sphere1.tx', at1='sphere2.tx' )

---
Return:
---


    list[string]: The names of the blendTwoAttr dependency nodes that were created.

Flags:
---


---
attribute(at): string
    properties: create, multiuse
    A list of attributes for the selected nodes for which a
blendTwoAttr node will be created.
      In query mode, this flag needs a value.

---
attribute0(at0): name
    properties: create, query, edit
    The attribute that should be connected to the first input
of the new blendTwoAttr node.
When queried, it returns a string.

---
attribute1(at1): name
    properties: create, query, edit
    The attribute that should be connected to the second input
of the new blendTwoAttr node.
When queried, it returns a string.

---
blender(bl): name
    properties: create, query, edit
    The blender attribute. This is the attribute that will be
connected to the newly created blendTwoAttr node(s) blender attribute.
This attribute controls how much of each of the two attributes
to use in the blend. If this flag is not specified, a new
animation curve is created whose value goes from 1 to 0
throughout the time range specified by the -t flag. If -t is not
specified, an abrupt change from the value of the first to the
value of the second attribute will occur at the current time
when this command is issued.

---
controlPoints(cp): boolean
    properties: create
    Explicitly specify whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.

---
driver(d): int
    properties: create, query, edit
    The index of the driver attribute for this blend node (0 or 1)
When queried, it returns an integer.

---
name(n): string
    properties: create, query
    name for the new blend node(s)

---
shape(s): boolean
    properties: create
    Consider all attributes of shapes below transforms as well,
except "controlPoints". Default: true

---
time(t): timerange
    properties: create
    The time range between which the blending between the 2 attributes
should occur. If a single time is specified, then the blend will
cause an abrupt change from the first to the second attribute at
that time.  If a range is specified, a smooth blending will occur
over that time range. The default is to make a sudden transition
at the current time.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/blendTwoAttr.html 
    """


def blindDataType(dataType: string, longDataName: string, longNames: boolean, query: boolean, shortDataName: string, shortNames: boolean, typeId: int, typeNames: boolean) -> string:
    """Synopsis:
---
---
 blindDataType([dataType=string], [longDataName=string], [longNames=boolean], [query=boolean], [shortDataName=string], [shortNames=boolean], [typeId=int], [typeNames=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

blindDataType is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

To create a new blind data typeId with a floating point attribute
cmds.blindDataType( id=9001, dt='float', longDataName='bdFloat', shortDataName='bdf' )

To create a Blind Data type with several attributes
cmds.blindDataType( 'ruf', '-dt', 'float', '-longDataName', 'smoothness', '-shortDataName', 'smo', '-dt', 'int' id=9005, dt='float', longDataName='roughness', shortDataName='', longDataName='count', shortDataName='cnt' )

To query if a type is already used
cmds.blindDataType( 9001
to query the type of a single attribute
 'blindDataType', '-q', '-id', 9001, '-tn', '-ldn', 'smoothness', query=True, id=True )

to get the types and names for all attributes
cmds.blindDataType( 9001, '-tn', query=True, id=True )

---
Return:
---


    string: Name of nodes created

Flags:
---


---
dataType(dt): string
    properties: create, multiuse
    Specifies the dataTypes that are part of BlindData node being created.
Allowable strings are "int", "float", "double", "string", "boolean" and "binary".
Must be used togeter with the -ldn and -sdn flags to specify each attribute.

---
longDataName(ldn): string
    properties: create, multiuse
    Specifies the long names of the datas that are part of BlindData node being
created. Must be used togeter with the -dt and -sdn flags to specify each attribute.

---
longNames(ln): boolean
    properties: create
    Specifies that for a query command the long attributes names be listed.

---
query(q): boolean
    properties: create
    Specifies that this is a special query type command.

---
shortDataName(sdn): string
    properties: create, multiuse
    Specifies the short names of the data that are part of BlindData node being
created. Must be used togeter with the -dt and -ldn flags to specify each attribute.

---
shortNames(sn): boolean
    properties: create
    Specifies that for a query command the short attribute names be listed.

---
typeId(id): int
    properties: create
    Specifies the typeId of the BlindData type being created.

---
typeNames(tn): boolean
    properties: create
    Specifies that for a query command the data types be listed.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/blindDataType.html 
    """


def bluePencilDrawCtx() -> None:
    """Synopsis:
---
---
 bluePencilDrawCtx()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bluePencilDrawCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

// Create blue pencil draw context.
cmds.bluePencilDrawCtx('contextName')

// Flag the draw context as dirty.
cmds.bluePencilDrawCtx(e=True, 'contextName')

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bluePencilDrawCtx.html 
    """


def bluePencilFrame(activeViewport: boolean, clear: boolean, copy: boolean, cutFrame: boolean, delete: boolean, duplicate: boolean, exportFrames: boolean, importFrames: boolean, insert: boolean, move: tuple[int, int, int], moveCopy: tuple[int, int, int], moveToNext: boolean, paste: boolean, relative: boolean, retime: int, scale: tuple[float, boolean, int, int], scaleCopy: tuple[float, boolean, int, int], stepBack: boolean, stepForward: boolean) -> None:
    """Synopsis:
---
---
 bluePencilFrame([activeViewport=boolean], [clear=boolean], [copy=boolean], [cutFrame=boolean], [delete=boolean], [duplicate=boolean], [exportFrames=boolean], [importFrames=boolean], [insert=boolean], [move=[int, int, int]], [moveCopy=[int, int, int]], [moveToNext=boolean], [paste=boolean], [relative=boolean], [retime=int], [scale=[float, boolean, int, int]], [scaleCopy=[float, boolean, int, int]], [stepBack=boolean], [stepForward=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bluePencilFrame is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Frame actions.
cmds.bluePencilFrame(ins=True)
cmds.bluePencilFrame(dup=True)
cmds.bluePencilFrame(del=True)
cmds.bluePencilFrame(cut=True)
cmds.bluePencilFrame(cp=True)
cmds.bluePencilFrame(pst=True)
cmds.bluePencilFrame(clr=True)
cmds.bluePencilFrame(stepForward=True)
cmds.bluePencilFrame(stepBack=True)

Set the distance to the next frame to 5.
cmds.bluePencilFrame(retime=5)

Add 5 to the space to the next frame.
cmds.bluePencilFrame(retime=5, relative=True)

Set the distance to the next frame to 5 and then set the current time to the next frame.
cmds.bluePencilFrame(retime=5, moveToNext=True)

Move frames between 5 and 9 by 15 frames.
cmds.bluePencilFrame(move=(15, 5, 9))

Move frames between 5 and 9 by 15 frames while leaving a copy of the initial keys in their original location.
cmds.bluePencilFrame(moveCopy=(15, 5, 9))

Scale frames between 5 and 9 by 2 from the beginning.
cmds.bluePencilFrame(scale=(2.0, 0, 5, 9))

Scale frames between 5 and 9 by 2 from the beginning while leaving a copy of the initial keys in their original location.
cmds.bluePencilFrame(scaleCopy=(2.0, 0, 5, 9))

Launch import frame dialog.
cmds.bluePencilFrame(importFrames=True)

Launch export frame dialog.
cmds.bluePencilFrame(exportFrames=True)

---


Flags:
---


---
activeViewport(avp): boolean
    properties: create
    Create the frame in the active viewport's camera.

---
clear(clr): boolean
    properties: create
    Erase the data from one or more frames using the highlighted range in Maya's time slider.

---
copy(cp): boolean
    properties: create
    Copy the frame data in the selected range to the clipboard.

---
cutFrame(cut): boolean
    properties: create
    Copy the frame data in the selected range to the clipboard and remove the frames.

---
delete(delete): boolean
    properties: create
    Remove one or more frames using the highlighted range in Maya's time slider.

---
duplicate(dup): boolean
    properties: create
    Insert a frame at the current time that is a duplicate of the previous frame.

---
exportFrames(ex): boolean
    properties: create
    Show blue pencil export frame dialog.

---
importFrames(im): boolean
    properties: create
    Show blue pencil import frame dialog.

---
insert(ins): boolean
    properties: create
    Insert one or more empty frames using the highlighted range in the time slider.

---
move(mv): [int, int, int]
    properties: create
    Move the frames in the specified range by the given offset. Arguments are offset,
range start, range end.

---
moveCopy(mvc) 2024.1: [int, int, int]
    properties: create
    Copy then move the frames in the specified range by the given offset. Arguments are offset,
range start, range end.

---
moveToNext(mvn): boolean
    properties: create
    Move the current time to the next frame after retiming.

---
paste(pst): boolean
    properties: create
    Create new frames using the data in the clipboard at the current time.

---
relative(rel): boolean
    properties: create
    Set the retime action to shift the frames by a relative amount to add or remove space
between frames. When the flag is not set, the spacing between the frames is set to the
retime value.

---
retime(ret): int
    properties: create
    Shift frames or change the frame spacing in a selected range.

---
scale(sc): [float, boolean, int, int]
    properties: create
    Scale the frames in the specified range by the given factor. Arguments are scale factor,
scale from end (true) or beginning (false), range start, range end.

---
scaleCopy(scc) 2024.1: [float, boolean, int, int]
    properties: create
    Copy then scale the frames in the specified range by the given factor. Arguments are scale factor,
scale from end (true) or beginning (false), range start, range end.

---
stepBack(sb): boolean
    properties: create
    Set the current time to the previous blue pencil frame's time.

---
stepForward(sf): boolean
    properties: create
    Set the current time to the next blue pencil frame's time.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bluePencilFrame.html 
    """


def bluePencilLayer(active: int, addLayer: boolean, count: boolean, delete: int, deleteAll: boolean, editLocked: tuple[boolean, int], editName: tuple[string, int], editOpacity: tuple[float, int], editState: tuple[int, int], editVis: tuple[boolean, int], insert: int, layerState: tuple[int, int], move: tuple[int, int], moveAll: boolean, name: tuple[string, int], newCamera: string, queryLocked: int, queryName: int, queryOpacity: int, queryState: int, queryVis: int) -> None:
    """Synopsis:
---
---
 bluePencilLayer([active=int], [addLayer=boolean], [count=boolean], [delete=int], [deleteAll=boolean], [editLocked=[boolean, int]], [editName=[string, int]], [editOpacity=[float, int]], [editState=[int, int]], [editVis=[boolean, int]], [insert=int], [layerState=[int, int]], [move=[int, int]], [moveAll=boolean], [name=[string, int]], [newCamera=string], [queryLocked=int], [queryName=int], [queryOpacity=int], [queryState=int], [queryVis=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bluePencilLayer is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Set the active layer to index 3 on camera perspective1
cmds.bluePencilLayer("perspective1", active=3)

Get the number of layers for perspective1.
cmds.bluePencilLayer("perspective1", count=True)

Create layer.
cmds.bluePencilLayer("perspective1", addLayer=True, name="newLayerName", layerState=1)
cmds.bluePencilLayer("perspective1", insert=3, name="newLayerName", layerState=0)

Remove layer.
cmds.bluePencilLayer("perspective1", delete=3)
cmds.bluePencilLayer("perspective1", deleteAll=True)

Move layer.
cmds.bluePencilLayer("perspective1", move=(3, 6), newCamera="top")
cmds.bluePencilLayer("perspective1", moveAll="top")

Rename layer.
cmds.bluePencilLayer("perspective1", editName=("newLayerName", 3))

Query layer info.
cmds.bluePencilLayer("perspective1", queryName=3)
cmds.bluePencilLayer("perspective1", queryVis=3)
cmds.bluePencilLayer("perspective1", queryOpacity=3)
cmds.bluePencilLayer("perspective1", queryState=3)

Set layer info.
cmds.bluePencilLayer("perspective1", editName=("newName", 3))
cmds.bluePencilLayer("perspective1", editVis=(0, 3))
cmds.bluePencilLayer("perspective1", editOpacity=(0.5, 3))
cmds.bluePencilLayer("perspective1", editState=(1, 3))
cmds.bluePencilLayer("perspective1", editLocked=(1, 3))

---


Flags:
---


---
active(act): int
    properties: create, query, edit
    Sets the active layer index. Query returns the active layer index.

---
addLayer(add): boolean
    properties: 
    Creates a new layer.

---
count(cnt): boolean
    properties: 
    Returns the number of layers.

---
delete(delete): int
    properties: 
    Removes the layer at the specified index.

---
deleteAll(da): boolean
    properties: 
    Removes all layers.

---
editLocked(el): [boolean, int]
    properties: 
    Edit the layer's locked state.

---
editName(en): [string, int]
    properties: 
    Sets name of the layer at the specified index.

---
editOpacity(eo): [float, int]
    properties: 
    Sets the opacity of the layer at the specified index.

---
editState(es): [int, int]
    properties: 
    Edits the layer's state. 0: animated, 1: static.

---
editVis(ev): [boolean, int]
    properties: 
    Sets the visibility of the layer at the specified index.

---
insert(ins): int
    properties: 
    Creates a new layer at the given index.

---
layerState(ls): [int, int]
    properties: 
    Sets the layer state when adding a new layer. 0: animated, 1: static.

---
move(mv): [int, int]
    properties: 
    Moves a layer from one index to another.

---
moveAll(mva): boolean
    properties: 
    Moves all layers from the current camera to the given camera.

---
name(n): [string, int]
    properties: 
    Sets the name of the new layer when using addLayer or insertLayer.

---
newCamera(nc): string
    properties: 
    Sets a new camera to move layers to when using the move test.

---
queryLocked(ql): int
    properties: 
    Query the layer's locked state.

---
queryName(qn): int
    properties: 
    Returns the specified layer's name.

---
queryOpacity(qo): int
    properties: 
    Returns the specified layer's opacity.

---
queryState(qs): int
    properties: 
    Queries the layer's state. 0: animated, 1: static.

---
queryVis(qv): int
    properties: 
    Returns the specified layer's visibility.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bluePencilLayer.html 
    """


def bluePencilNode(camera: string, exists: boolean, frame: boolean, layer: boolean, layerName: string, layerState: uint, refresh: boolean, refreshGhosting: boolean) -> None:
    """Synopsis:
---
---
 bluePencilNode([camera=string], [exists=boolean], [frame=boolean], [layer=boolean], [layerName=string], [layerState=uint], [refresh=boolean], [refreshGhosting=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bluePencilNode is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Refresh node.
cmds.bluePencilNode(r=True)

Check if blue pencil node exists.
cmds.bluePencilNode(exists=True)

Get the active camera name.
cmds.bluePencilNode(q=True, camera=True)

Create a new node.
cmds.bluePencilNode(layer=True, c=CameraName, ln=LayerName, ls=1, f=True)

---


Flags:
---


---
camera(c): string
    properties: create, query
    Specifies the camera on which to create a new layer when creating the node.
Query returns the name of the active camera.

---
exists(ex): boolean
    properties: create
    Returns true if the blue pencil node has been created.

---
frame(f): boolean
    properties: create
    Creates a new frame when creating the new layer when creating the node.

---
layer(l): boolean
    properties: create
    Create a new layer when creating the node.

---
layerName(ln): string
    properties: create
    Specifies the layer name of the new layer when creating the node.

---
layerState(ls): uint
    properties: create
    Specifies the layer state of the new layer. 0: Animated, 1: Static.

---
refresh(r): boolean
    properties: create
    Refresh the viewport of the active camera.

---
refreshGhosting(rg): boolean
    properties: create
    Refresh the ghosting information.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bluePencilNode.html 
    """


def bluePencilStroke(frameAdded: boolean, layerAdded: int) -> None:
    """Synopsis:
---
---
 bluePencilStroke([frameAdded=boolean], [layerAdded=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bluePencilStroke is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Commit active drawing stroke on the perspective camera.
cmds.bluePencilStroke('perspective', layerAdded=2, frameAdded=True)

---


Flags:
---


---
frameAdded(fa): boolean
    properties: create
    The index of the frame added for the new stroke. This is set to remove it when undoing.

---
layerAdded(la): int
    properties: create
    Sets the index of the added layer to remove it when undoing.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bluePencilStroke.html 
    """


def bluePencilUtil(adjustBrushSize: boolean, adjustOpacity: boolean, arrowOptions: tuple[int, int], arrowTool: boolean, brushOptions: tuple[int, int, int, int, int], brushTool: boolean, draw: boolean, drawColor: tuple[int, int, int], ellipseOptions: tuple[int, int], ellipseTool: boolean, eraserOptions: tuple[int, int, int, int, int], eraserTool: boolean, ghostColorNext: tuple[int, int, int], ghostColorOverride: boolean, ghostColorPrevious: tuple[int, int, int], ghostNext: boolean, ghostNextCount: int, ghostPrevious: boolean, ghostPreviousCount: int, layerManager: boolean, layerProperties: boolean, lineOptions: tuple[int, int], lineTool: boolean, pencilOptions: tuple[int, int, int, int], pencilTool: boolean, rectangleOptions: tuple[int, int], rectangleTool: boolean, refreshLayerManager: boolean, refreshTimelineDisplay: boolean, resetTool: boolean, textFontFamily: string, textOptions: tuple[int, int, string], textTool: boolean, timelineFrameDisplay: int, transform: boolean) -> None:
    """Synopsis:
---
---
 bluePencilUtil([adjustBrushSize=boolean], [adjustOpacity=boolean], [arrowOptions=[int, int]], [arrowTool=boolean], [brushOptions=[int, int, int, int, int]], [brushTool=boolean], [draw=boolean], [drawColor=[int, int, int]], [ellipseOptions=[int, int]], [ellipseTool=boolean], [eraserOptions=[int, int, int, int, int]], [eraserTool=boolean], [ghostColorNext=[int, int, int]], [ghostColorOverride=boolean], [ghostColorPrevious=[int, int, int]], [ghostNext=boolean], [ghostNextCount=int], [ghostPrevious=boolean], [ghostPreviousCount=int], [layerManager=boolean], [layerProperties=boolean], [lineOptions=[int, int]], [lineTool=boolean], [pencilOptions=[int, int, int, int]], [pencilTool=boolean], [rectangleOptions=[int, int]], [rectangleTool=boolean], [refreshLayerManager=boolean], [refreshTimelineDisplay=boolean], [resetTool=boolean], [textFontFamily=string], [textOptions=[int, int, string]], [textTool=boolean], [timelineFrameDisplay=int], [transform=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bluePencilUtil is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Activate the drawing tool context.
cmds.bluePencilUtil(draw=True)

Activate the transform tool context.
cmds.bluePencilUtil(transform)

Set the draw color to red.
cmds.bluePencilUtil(drawColor=[255, 0, 0])

Activate tool.
cmds.bluePencilUtil(pencilTool=True)
cmds.bluePencilUtil(brushTool=True)
cmds.bluePencilUtil(eraserTool=True)
cmds.bluePencilUtil(lineTool=True)
cmds.bluePencilUtil(arrowTool=True)
cmds.bluePencilUtil(ellipseTool=True)
cmds.bluePencilUtil(rectangleTool=True)
cmds.bluePencilUtil(textTool=True)

Start adjusting the brush size.
cmds.bluePencilUtil(adjustBrushSize=True)

Stop adjusting the brush size.
cmds.bluePencilUtil(adjustBrushSize=False)

Adjust opacity.
cmds.bluePencilUtil(adjustOpacity=True)

Set pencil options size: 10, opacity 25, pressure size: 35, pressure opacity: 45.
cmds.bluePencilUtil(pencilOptions=[10, 25, 35, 45])

Set pencil options size: 10, opacity 25, hardness: 30,
pressure size: 35, pressure opacity: 45.
cmds.bluePencilUtil(brushOptions=[10, 25, 30, 35, 45])
cmds.bluePencilUtil(eraserOptions=[10, 25, 30, 35, 45])
cmds.bluePencilUtil(lineOptions=[10, 25])
cmds.bluePencilUtil(arrowOptions=[10, 25])
cmds.bluePencilUtil(ellipseOptions=[10, 25])
cmds.bluePencilUtil(rectangleOptions=[10, 25])

Set the text options, size: 12, opacity: 25, font: Arial
cmds.bluePencilUtil(textOptions=[12, 25, 'Arial'])
cmds.bluePencilUtil(textFontFamily='Arial')

Activate ghosting
cmds.bluePencilUtil(ghostPrevious=True)
cmds.bluePencilUtil(ghostNext=True)

Set the number of ghosts.
cmds.bluePencilUtil(ghostPreviousCount=5)
cmds.bluePencilUtil(ghostNextCount=5)

Set the ghost color.
cmds.bluePencilUtil(ghostColorOverride=True)
cmds.bluePencilUtil(ghostColorPrevious=[0, 0, 255])
cmds.bluePencilUtil(ghostColorNext=[255, 255, 0])

Refresh timeline.
cmds.bluePencilUtil(refreshTimelineDisplay=True)

Show layer manager.
cmds.bluePencilUtil(layerManager=True)

Refresh layer manager.
cmds.bluePencilUtil(refreshLayerManager=True)

Show layer properties.
cmds.bluePencilUtil(layerProperties=True)

Reset blue pencil tool settings.
cmds.bluePencilUtil(resetTool=True)

---


Flags:
---


---
adjustBrushSize(abs): boolean
    properties: create, query, edit
    Activates or deactivates the mode to adujst the brush size by dragging.

---
adjustOpacity(aop): boolean
    properties: create, query, edit
    Activates or deactivates the mode to adujst the brush opacity by dragging.

---
arrowOptions(ao): [int, int]
    properties: create, query, edit
    Set the arrow options. The arguments are size, opacity.

---
arrowTool(at): boolean
    properties: create, query, edit
    Activates the arrow tool.
When queried, returns true if the arrow tool is active.

---
brushOptions(bo): [int, int, int, int, int]
    properties: create, query, edit
    Sets the brush options. The arguments in order are size, opacity, hardness
pressure opacity, pressure size.

---
brushTool(bt): boolean
    properties: create, query, edit
    Activates the brush tool.
When queried, returns true if the brush tool is active.

---
draw(d): boolean
    properties: create, query, edit
    Activates the drawing tool context.
When queried, returns true if the drawing tool context is active.

---
drawColor(dc): [int, int, int]
    properties: create, query, edit
    Sets the current drawing color. Color format is RGB with values from 0-255.
When queried, returns the current drawing color.

---
ellipseOptions(elo): [int, int]
    properties: create, query, edit
    Sets the ellipse options. The arguments are size, opacity.

---
ellipseTool(elt): boolean
    properties: create, query, edit
    Activates the ellipse tool.
When queried, returns true if the ellipse tool is active.

---
eraserOptions(eo): [int, int, int, int, int]
    properties: create, query, edit
    Sets the brush options. The arguments in order are size, opacity, hardness
pressure opacity, pressure size.

---
eraserTool(et): boolean
    properties: create, query, edit
    Activates the eraser tool.
When queried, returns true if the eraser tool is active.

---
ghostColorNext(gcn): [int, int, int]
    properties: create, query, edit
    Sets the color for the ghosts of next frames.

---
ghostColorOverride(gco): boolean
    properties: create, query, edit
    Activates or deactivates the color override for the ghosts.

---
ghostColorPrevious(gcp): [int, int, int]
    properties: create, query, edit
    Sets the color for the ghosts of previous frames.

---
ghostNext(gn): boolean
    properties: create, query, edit
    Activates or deactivates the ghosting of next frames.

---
ghostNextCount(gnc): int
    properties: create, query, edit
    Sets the number of ghosts of next frames.

---
ghostPrevious(gp): boolean
    properties: create, query, edit
    Activates or deactivates the ghosting of previous frames.

---
ghostPreviousCount(gpc): int
    properties: create, query, edit
    Sets the number of ghosts of previous frames.

---
layerManager(lm): boolean
    properties: create, query, edit
    Shows the layer manager by showing the tool settings window.
Query returns if the layer manager is shown.

---
layerProperties(lp): boolean
    properties: create, query, edit
    Show the layer properties dialog.

---
lineOptions(lo): [int, int]
    properties: create, query, edit
    Sets the line options. The arguments are size, opacity.

---
lineTool(lt): boolean
    properties: create, query, edit
    Activates the line tool.
When queried, returns true if the line tool is active.

---
pencilOptions(po): [int, int, int, int]
    properties: create, query, edit
    Sets the pencil options. The arguments in order are size, opacity,
pressure opacity, pressure size.

---
pencilTool(pt): boolean
    properties: create, query, edit
    Activates the pencil tool.
When queried, returns true if the pencil tool is active.

---
rectangleOptions(ro): [int, int]
    properties: create, query, edit
    Sets the rectangle options. The arguments are size, opacity.

---
rectangleTool(rt): boolean
    properties: create, query, edit
    Activates the rectangle tool.
When queried, returns true if the rectangle tool is active.

---
refreshLayerManager(rlm): boolean
    properties: create, query, edit
    Refresh the layer manager.

---
refreshTimelineDisplay(rtd): boolean
    properties: create, query, edit
    Refresh the timeline display frames.

---
resetTool(r): boolean
    properties: create, query, edit
    Restore tool settings to default values.

---
textFontFamily(tff): string
    properties: create, query, edit
    Sets the text font family.

---
textOptions(txo): [int, int, string]
    properties: create, query, edit
    Sets the text options. The arguments in order are size, opacity, font family name.

---
textTool(tt): boolean
    properties: create, query, edit
    Activates the text tool.
When queried, returns true if the text tool is active.

---
timelineFrameDisplay(tfd): int
    properties: create, query, edit
    Sets the display mode for blue pencil frames in the timeline.
Modes:

0 Show always
1 Show when context is active
2 Hide

---
transform(t): boolean
    properties: create, query, edit
    Activates the transform tool context.
When queried, returns true if the transform tool context is active.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bluePencilUtil.html 
    """


def boneLattice(after: boolean, afterReference: boolean, before: boolean, bicep: float, components: boolean, deformerTools: boolean, exclusive: string, frontOfChain: boolean, geometry: string, geometryIndices: boolean, ignoreSelected: boolean, includeHiddenSelections: boolean, joint: string, lengthIn: float, lengthOut: float, name: string, parallel: boolean, prune: boolean, remove: boolean, selectedComponents: boolean, split: boolean, transform: string, tricep: float, useComponentTags: boolean, widthLeft: float, widthRight: float) -> string:
    """Synopsis:
---
---
 boneLattice(
objects
    , [after=boolean], [afterReference=boolean], [before=boolean], [bicep=float], [components=boolean], [deformerTools=boolean], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [joint=string], [lengthIn=float], [lengthOut=float], [name=string], [parallel=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean], [split=boolean], [transform=string], [tricep=float], [useComponentTags=boolean], [widthLeft=float], [widthRight=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

boneLattice is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

select a lattice that has been added to a rigid skin shape
---

cmds.boneLattice( joint='joint2' )
cmds.boneLattice( transform='joint1', joint='joint2' )
cmds.boneLattice( 'boneLattice1', edit=True, bicep=0.5 )

---
Return:
---


    string: Name of bone lattice algorithm node created/edited.

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
bicep(bi): float
    properties: create, query, edit
    Affects the bulging of lattice points on the inside of
the bend. Positive/negative values cause the points to bulge
outwards/inwards. Default value is 0.0. When queried, this flag
returns a float.

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
joint(j): string
    properties: create, query, edit
    Specifies which joint will be used to drive the bulging
behaviors.

---
lengthIn(li): float
    properties: create, query, edit
    Affects the location of lattice points along the upper
half of the bone. Positive/negative values cause the points
to move away/towards the center of the bone.  Changing this
parameter also modifies the regions affected by the creasing,
rounding and width parameters. Default value is 0.0. When
queried, this flag returns a float.

---
lengthOut(lo): float
    properties: create, query, edit
    Affects the location of lattice points along the lower
half of the bone. Positive/negative values cause the points
to move away/towards the center of the bone.  Changing this
parameter also modifies the regions affected by the creasing,
rounding and width parameters. Default value is 0.0. When
queried, this flag returns a float.

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
transform(t): string
    properties: create
    Specifies which dag node is being used to rigidly transform
the lattice which this node is going to deform.  If this flag is
not specified an identity matrix will be assumed.

---
tricep(tr): float
    properties: create, query, edit
    Affects the bulging of lattice points on the outside
of the bend. Positive/negative values cause the points to bulge
outwards/inwards. Default value is 0.0. When queried, this flag
returns a float.

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

---
widthLeft(wl): float
    properties: create, query, edit
    Affects the bulging of lattice points on the left side
of the bend. Positive/negative values cause the points to bulge
outwards/inwards. Default value is 0.0. When queried, this flag
returns a float.

---
widthRight(wr): float
    properties: create, query, edit
    Affects the bulging of lattice points on the right
side of the bend. Positive/negative values cause the points to
bulge outwards/inwards. Default value is 0.0. When queried, this
flag returns a float.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/boneLattice.html 
    """


def boundary(caching: boolean, constructionHistory: boolean, endPoint: boolean, endPointTolerance: linear, name: string, nodeState: int, object: boolean, order: boolean, polygon: int, range: boolean) -> list[string]:
    """Synopsis:
---
---
 boundary(
string string string [string]
    , [caching=boolean], [constructionHistory=boolean], [endPoint=boolean], [endPointTolerance=linear], [name=string], [nodeState=int], [object=boolean], [order=boolean], [polygon=int], [range=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

boundary is undoable, queryable, and editable.  Note that there is no tangent continuity option with this command.
Unless all the curve end points are touching, the resulting
surface will not pass through all curves.  Instead, use the birail
command.




Example:
---
import maya.cmds as cmds

Creating boundary surfaces with three curves:

crv1 = cmds.curve(d= 3, p= ((8, 0, 3), (5, 0, 3), (2, 0, 2), (0, 0, 0)) )
crv2 = cmds.curve(d= 3, p= ((8, 0, -4), (5, 0, -3), (2, 0, -2), (0, 0, 0)) )
crv3 = cmds.curve(d= 3, p= ((10, 0, 3), (9, 3, 2), (11, 3, 1), (9, 0, -3)) )

These curves form a rough triangle shape pointing at the origin.
If order is OFF, then the apex of the surface will always between
the 1st and 2nd curves.

cmds.boundary( crv3, crv1, crv2, order=False, ep=0 )
cmds.boundary( crv3, crv2, crv1, order=False, ep=0 )

If order is ON, then think of the order of selection as "rail, rail, profile"
where the boundary is formed by sweeping the profile along two rails.
Direction of the curves becomes important as well; use the reverseCurve
command if you want to change a curve's direction.
cmds.boundary( crv1, crv2, crv3, order=True )


Creating boundary surfaces with four curves:

crv1 = cmds.curve(d= 3, p=((-2, 0, 5), (-1, 0, 3), (1, 0, 3), (3, 0, 4), (6, 0, 5)) )
crv2 = cmds.curve(d= 3, p=(( 7, 0, 4), (8, 0, 2), (8, 0, -3), (7, 0, -4)) )
crv3 = cmds.curve(d= 3, p=(( 6, 0, -5), (2, 0, -3), (1, 0, -5), (-3, 0, -5)) )
crv4 = cmds.curve(d= 3, p=((-2, 0, 4), (-4, 0, 1), (-4, 0, -3), (-2, 0, -4)) )

These curves form a rough square shape around the origin.
To make a boundary surface from four curves, two of the curves are
"rails" while the other two are "profiles".

cmds.boundary( crv1, crv2, crv3, crv4, order=False, ep=0 )
cmds.boundary( crv2, crv3, crv4, crv1, order=False, ep=0 )

profile, rail, profile, rail
Notice that in both cases, the resulting boundary surface passes through
the rail curves.

When order is ON, direction of the curves becomes important;
use the reverseCurve command if you want to change a curve's direction.
Notice the difference between:

cmds.boundary( crv1, crv2, crv3, crv4, order=False, ep=0 )
cmds.boundary( crv1, crv2, crv3, crv4, order=True, ep=0 )

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
endPoint(ep): boolean
    properties: create, query, edit
    True means the curve ends must touch before a surface will be created.
Default: false

---
endPointTolerance(ept): linear
    properties: create, query, edit
    Tolerance for end points, only used if endPoint attribute is true.
Default: 0.1

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
order(order): boolean
    properties: create, query, edit
    True if the curve order is important.
Default: true

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/boundary.html 
    """


def boxDollyCtx(alternateContext: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, toolName: string) -> string:
    """Synopsis:
---
---
 boxDollyCtx([alternateContext=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [toolName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

boxDollyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.boxDollyCtx( 'boxDollyContext', ac=False )

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/boxDollyCtx.html 
    """


def boxZoomCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, zoomScale: float) -> string:
    """Synopsis:
---
---
 boxZoomCtx(
object
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [zoomScale=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

boxZoomCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.boxZoomCtx( 'boxZoomContext', zs=1.0 )

---
Return:
---


    string: The name of the context

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
zoomScale(zs): float
    properties: create, query, edit
    Scale the zoom.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/boxZoomCtx.html 
    """


def bufferCurve(animation: string, attribute: string, controlPoints: boolean, exists: boolean, float: floatrange, hierarchy: string, includeUpperBound: boolean, index: uint, overwrite: boolean, shape: boolean, swap: boolean, time: timerange, useReferencedCurve: boolean) -> int:
    """Synopsis:
---
---
 bufferCurve(
animatedObject
    , [animation=string], [attribute=string], [controlPoints=boolean], [exists=boolean], [float=floatrange], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [overwrite=boolean], [shape=boolean], [swap=boolean], [time=timerange], [useReferencedCurve=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

bufferCurve is undoable, queryable, and NOT editable.
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

This command helps manage buffer curve for animated objects




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

Create a buffer curve for the selected keys
cmds.bufferCurve( animation='keys', overwrite=True )

Set the referenced anim curve to the buffer curve
cmds.bufferCurve( useReferencedCurve=True)

Swap the buffer curve for the selected keys
cmds.bufferCurve( animation='keys', swap=True )

---
Return:
---


    int: Number of buffer curves

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
exists(ex): boolean
    properties: query
    Returns true if a buffer curve currently exists on the
specified attribute; false otherwise.

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
overwrite(ov): boolean
    properties: create
    Create a buffer curve.  "true" means create a buffer curve
whether or not one already existed.  "false" means if a
buffer curve exists already then leave it alone.  If no
flag is specified, then the command defaults to -overwrite false

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
swap(sw): boolean
    properties: create
    For animated attributes which have buffer curves, swap
the buffer curve with the current animation curve

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

---
useReferencedCurve(urc): boolean
    properties: create, query
    In create mode, sets the buffer curve to the referenced curve.
Curves which are not from file references will ignore this flag.
In query mode, returns true if the selected keys are displaying their
referenced curve as the buffer curve, and false if they are not.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/bufferCurve.html 
    """


def buildBookmarkMenu(editor: string, type: string) -> None:
    """Synopsis:
---
---
 buildBookmarkMenu(
string
    , [editor=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

buildBookmarkMenu is undoable, NOT queryable, and NOT editable.
menuName is the string returned by the "menu" command.




Example:
---
import maya.cmds as cmds

Update the bookmarkMenu to show animation (bookmarkAnimCurves)
bookmarks
---

cmds.menu( 'bookmarkMenu' )
cmds.buildBookmarkMenu( 'bookmarkMenu', type='bookmarkAnimCurves' )

---


Flags:
---


---
editor(ed): string
    properties: create
    Name of the editor which this menu belongs to

---
type(typ): string
    properties: create
    Type of bookmark (sets -text) to display

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/buildBookmarkMenu.html 
    """


def buildKeyframeMenu() -> None:
    """Synopsis:
---
---
 buildKeyframeMenu(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

buildKeyframeMenu is undoable, NOT queryable, and NOT editable.
menuName is the string returned by the "menu" command.
The target menu will entries appended to it (and deleted from it) to always
show what's currently keyframable.




Example:
---
import maya.cmds as cmds

Set up "myAttributeMenu" as a menu to always
reflect what's currently keyframable.
---

cmds.buildKeyframeMenu( 'myAttributeMenu' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/buildKeyframeMenu.html 
    """


def button(actOnPress: boolean, actionIsSubstitute: boolean, align: string, annotation: string, backgroundColor: tuple[float, float, float], command: script, defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, recomputeSize: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 button(
[string]
    , [actOnPress=boolean], [actionIsSubstitute=boolean], [align=string], [annotation=string], [backgroundColor=[float, float, float]], [command=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [recomputeSize=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

button is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

def defaultButtonPush(*args):
  print 'Button 1 was pushed.'

cmds.window( width=150 )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Button 1', command=defaultButtonPush )
cmds.button( label='Button 2' )
cmds.button( label='Button 3' )
cmds.button( label='Button 4' )
cmds.showWindow()

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
actOnPress(aop): boolean
    properties: create, query, edit
    If true then the command specified by the command flag
will be executed when a mouse button is pressed.  If false then
that command will be executed after the mouse button is released.
The default value is false.

---
actionIsSubstitute(ais): boolean
    properties: create, query, edit
    This flag is obsolete and should no longer be used.

---
align(al): string
    properties: create, query, edit
    This flag is obsolete and should no longer be used.
The button label will always be center-aligned.

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/button.html 
    """


def buttonManip(icon: string) -> None:
    """Synopsis:
---
---
 buttonManip(
script [selectionItem]
    , [icon=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

buttonManip is undoable, NOT queryable, and NOT editable.
If a dag object is included on the command line, the manip will be
parented to the object. This means moving the object will move the
manip. You can move the manip independently of the object using its
triad.

Note that a buttonManip may not be parented to more than one object.




Example:
---
import maya.cmds as cmds

   Example 1.
---

   Create a button manipulator that will be parented to a sphere and will
   print "Button Manipulator" whenever it is pressed.
---

   Note that moving the sphere will also move the manipulator.
---

sphere = cmds.sphere()
cmds.buttonManip( 'print "Button Manipulator"', sphere[0])

   Example 2.
---

   Create a button manipulator that will execute the 'setKeyframe' command
   when it is pressed.
---

cmds.buttonManip( 'setKeyframe' )

---


Flags:
---


---
icon(i): string
    properties: create
    Specify an icon to represent the manipulator.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/buttonManip.html 
    """
