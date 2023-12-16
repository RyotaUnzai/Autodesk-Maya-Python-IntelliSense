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


def joint(absolute: boolean, angleX: angle, angleY: angle, angleZ: angle, assumePreferredAngles: boolean, automaticLimits: boolean, children: boolean, component: boolean, degreeOfFreedom: string, exists: string, limitSwitchX: boolean, limitSwitchY: boolean, limitSwitchZ: boolean, limitX: tuple[angle, angle], limitY: tuple[angle, angle], limitZ: tuple[angle, angle], name: string, orientJoint: string, orientation: tuple[angle, angle, angle], position: tuple[linear, linear, linear], radius: float, relative: boolean, rotationOrder: string, scale: tuple[float, float, float], scaleCompensate: boolean, scaleOrientation: tuple[angle, angle, angle], secondaryAxisOrient: string, setPreferredAngles: boolean, stiffnessX: float, stiffnessY: float, stiffnessZ: float, symmetry: boolean, symmetryAxis: string, zeroScaleOrient: boolean) -> string:
    """Synopsis:
---
---
 joint(
[objects]
    , [absolute=boolean], [angleX=angle], [angleY=angle], [angleZ=angle], [assumePreferredAngles=boolean], [automaticLimits=boolean], [children=boolean], [component=boolean], [degreeOfFreedom=string], [exists=string], [limitSwitchX=boolean], [limitSwitchY=boolean], [limitSwitchZ=boolean], [limitX=[angle, angle]], [limitY=[angle, angle]], [limitZ=[angle, angle]], [name=string], [orientJoint=string], [orientation=[angle, angle, angle]], [position=[linear, linear, linear]], [radius=float], [relative=boolean], [rotationOrder=string], [scale=[float, float, float]], [scaleCompensate=boolean], [scaleOrientation=[angle, angle, angle]], [secondaryAxisOrient=string], [setPreferredAngles=boolean], [stiffnessX=float], [stiffnessY=float], [stiffnessZ=float], [symmetry=boolean], [symmetryAxis=string], [zeroScaleOrient=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

joint is undoable, queryable, and editable.
Multiple objects are allowed only for the edit mode. The same
edit flags will be applied on all the joints selected, except
for -p without -r (set joint position in the world space). An
ik handle in the object list is equivalent to the list of
joints the ik handle commands. When -ch/children is present,
all the child joints of the specified joints, including the
joints implied by possible ik handles, will also be included.

In the creation mode, a new joint will be created as a child
of a selected transform or starts a hierarchy by itself if no
transform is selected. An ik handle will be treated as a
transform in the creation mode.

The default values of the arguments are:

-degreeOfFreedom xyz

-name "Joint#"

-position 0 0 0

-absolute

-dof "xyz"

-scale 1.0 1.0 1.0

-scaleCompensate true

-orientation 0.0 0.0 0.0

-scaleOrientation 0.0 0.0 0.0

-limitX -360 360

-limitY -360 360

-limitZ -360 360

-angleX 0.0

-angleY 0.0

-angleZ 0.0

-stiffnessX 0.0

-stiffnessY 0.0

-stiffnessZ 0.0

-limitSwitchX no

-limitSwitchY no

-limitSwitchZ no

-rotationOrder xyz

Those arguments can be specified in the creation mode,
editied in the edit mode (-e), or queried in the query mode
(-q).




Example:
---
import maya.cmds as cmds

Create a 3-joint chain
---

cmds.select( d=True )
cmds.joint( p=(0, 0, 0) )
cmds.joint( p=(0, 4, 0)  )
cmds.joint( 'joint1', e=True, zso=True, oj='xyz' )
cmds.joint( p=(0, 8, -1) )
cmds.joint( 'joint2', e=True, zso=True, oj='xyz' )

Create a fourth joint with z joint limits of -90 deg for
the lower limit and 90 deg for the upper limit.  The
joint will be positioned at (0, 0, 4) in world
coordinates.
---

cmds.joint( lz=('-90deg', '90deg'), p=(0, 8, 4) )

Set the joint limits but leave them disabled.
cmds.joint( edit=True, lz=('-90deg', '90deg'), lsz=False )

---
Return:
---


    string: Command result

Flags:
---


---
absolute(a): boolean
    properties: create, query, edit
    The joint center position is in absolute world coordinates.
(This is the default.)

---
angleX(ax): angle
    properties: create, query, edit
    Set the x-axis angle. When queried, this flag
returns a float.

---
angleY(ay): angle
    properties: create, query, edit
    Set the y-axis angle. When queried, this flag
returns a float.

---
angleZ(az): angle
    properties: create, query, edit
    Set the z-axis angle. When queried, this flag
returns a float.

---
assumePreferredAngles(apa): boolean
    properties: edit
    Meaningful only in the edit mode. It sets the
joint angles to the corresponding preferred
angles.

---
automaticLimits(al): boolean
    properties: create
    Meaningful only in edit mode. It sets the joint to
appropriate hinge joint with joint limits. It modifies
the joint only if (a) it connects exactly to two
joints (one parent, one child), (b) it does not lie on
the line drawn between the two connected joints, and
the plane it forms with the two connected joints
is perpendicular to one of its rotation axes.

---
children(ch): boolean
    properties: edit
    It tells the command to apply all the edit options
not only to the selected joints, but also to their
descendent joints in the DAG.

---
component(co): boolean
    properties: create, edit
    Use with the -position switch to position the joint
relative to its parent (like -relative) but to compute
new positions for all children joints so their world
coordinate positions do not change.

---
degreeOfFreedom(dof): string
    properties: create, query, edit
    Specifies the degrees of freedom for the IK.
Valid strings consist of non-duplicate letters from x,
y, and z. The letters in the string indicate what
rotations are to be used by IK. The order a letter
appear in the string does not matter. Examples are x,
yz, xyz. When queried, this flag returns a string.
Modifying dof will change the locking state of the
corresponding rotation attributes. The rule is: if an
rotation is turned into a dof, it will be unlocked if
it is currently locked. When it is turned into a
non-dof, it will be locked if it is not currently
locked.

---
exists(ex): string
    properties: query
    Does the named joint exist? When queried, this flag
returns a boolean.

---
limitSwitchX(lsx): boolean
    properties: create, query, edit
    Use the limit the x-axis rotation? When
queried, this flag returns a boolean.

---
limitSwitchY(lsy): boolean
    properties: create, query, edit
    Use the limit the y-axis rotation? When
queried, this flag returns a boolean.

---
limitSwitchZ(lsz): boolean
    properties: create, query, edit
    Use the Limit the z-axis rotation? When
queried, this flag returns a boolean.

---
limitX(lx): [angle, angle]
    properties: create, query, edit
    Set lower and upper limits on the x-axis of
rotation.  Also turns on
the joint limit. When queried, this flag returns 2 floats.

---
limitY(ly): [angle, angle]
    properties: create, query, edit
    Set lower and upper limits on the y-axis of
rotation.  Also turns on
the joint limit. When queried, this flag returns 2 floats.

---
limitZ(lz): [angle, angle]
    properties: create, query, edit
    Set lower and upper limits on the z-axis of
rotation.  Also turns on
the joint limit. When queried, this flag returns 2 floats.

---
name(n): string
    properties: create, query, edit
    Specifies the name of the joint. When queried,
this flag returns a string.

---
orientJoint(oj): string
    properties: edit
    The argument can be one of the following strings: xyz,
yzx, zxy, zyx, yxz, xzy, none.

It modifies the joint orientation and scale orientation
so that the axis indicated by the first letter in the argument
will be aligned with the vector from this joint to its first
child joint. For example, if the argument is "xyz", the x-axis will
point towards the child joint.

The alignment of the remaining two joint orient axes are
dependent on whether or not the -sao/-secondaryAxisOrient flag
is used. If the -sao flag is used, see the documentation for
that flag for how the remaining axes are aligned.

In the absence of a user specification for the secondary axis
orientation, the rotation axis indicated by the last letter in
the argument will be aligned with the vector perpendicular to
first axis and the vector from this joint to its parent joint.

The remaining axis is aligned according the right hand rule.

If the argument is "none", the joint orientation
will be set to zero and its effect to the hierarchy
below will be offset by modifying the scale
orientation.

The flag will be ignored if:

A. the joint has non-zero rotations when the argument
is not "none".

B. the joint does not have child joint, or the
distance to the child joint is zero when the argument
is not "none".

C. either flag -o or -so is set.

---
orientation(o): [angle, angle, angle]
    properties: create, query, edit
    The joint orientation. When queried, this flag
returns 3 floats.

---
position(p): [linear, linear, linear]
    properties: create, query, edit
    Specifies the position of the center of the joint.
This position may be relative to the joint's parent
or in absolute world coordinates (see -r and -a
below). When queried, this flag returns 3 floats.

---
radius(rad): float
    properties: create, query, edit
    Specifies the joint radius.

---
relative(r): boolean
    properties: create, query, edit
    The joint center position is relative to the joint's parent.

---
rotationOrder(roo): string
    properties: create, query, edit
    The rotation order of the joint. The
argument can be one of the following strings: xyz,
yzx, zxy, zyx, yxz, xzy.

---
scale(s): [float, float, float]
    properties: create, query, edit
    Scale of the joint. When queried, this flag
returns 3 floats.

---
scaleCompensate(sc): boolean
    properties: create, query, edit
    It sets the scaleCompenstate attribute of
the joint to the given argument. When this is true,
the scale of the parent joint will be compensated
before any rotation of this joint is applied, so that
the bone to the joint is scaled but not the bones to
its child joints. When queried, this flag returns an
boolean.

---
scaleOrientation(so): [angle, angle, angle]
    properties: create, query, edit
    Set the orientation of the coordinate axes for
scaling. When queried, this flag returns 3 floats.

---
secondaryAxisOrient(sao): string
    properties: edit
    The argument can be one of the following strings: xup, xdown,
yup, ydown, zup, zdown, none.

This flag is used in conjunction with the -oj/orientJoint
flag. It specifies the scene axis that the second axis should
align with. For example, a flag combination of "-oj yzx -sao yup"
would result in the y-axis pointing down the bone, the
z-axis oriented with the scene's positive y-axis, and
the x-axis oriented according to the right hand rule.

---
setPreferredAngles(spa): boolean
    properties: edit
    Meaningful only in the edit mode. It sets the
preferred angles to the current joint angles.

---
stiffnessX(stx): float
    properties: create, query, edit
    Set the stiffness (from 0 to 100.0) for x-axis.
When queried, this flag returns a float.

---
stiffnessY(sty): float
    properties: create, query, edit
    Set the stiffness (from 0 to 100.0) for y-axis.
When queried, this flag returns a float.

---
stiffnessZ(stz): float
    properties: create, query, edit
    Set the stiffness (from 0 to 100.0) for z-axis.
When queried, this flag returns a float.

---
symmetry(sym): boolean
    properties: create, edit
    Create a symmetric joint from the current joint.

---
symmetryAxis(sa): string
    properties: create, edit
    This flag specifies the axis used to mirror symmetric joints. Any combination of x, y, z can be used. This option is only used when the symmetry flag is set to True.

---
zeroScaleOrient(zso): boolean
    properties: edit
    It sets the scale orientation to zero and
compensate the change by modifing the translation and
joint orientation for joint or rotation for general
transform of all its child transformations.

The flag will be ignored if the flag -so is set.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/joint.html 
    """


def jointCluster(aboveBound: float, aboveCluster: boolean, aboveDropoffType: string, aboveValue: float, belowBound: float, belowCluster: boolean, belowDropoffType: string, belowValue: float, deformerTools: boolean, joint: string, name: string) -> string:
    """Synopsis:
---
---
 jointCluster(
string
    , [aboveBound=float], [aboveCluster=boolean], [aboveDropoffType=string], [aboveValue=float], [belowBound=float], [belowCluster=boolean], [belowDropoffType=string], [belowValue=float], [deformerTools=boolean], [joint=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

jointCluster is undoable, queryable, and editable.

.                a <---- aboveBound
.    ____________a_________
.                a         \
.     Joint1     a       Joint2
.   _____________a_______    \
.                a       \    \     b  <--- belowBound
.                a        \    \  b
.                          \    b
.                           \ b  \
.                           b\    \
.                         b   \ Joint3





Example:
---
import maya.cmds as cmds

To add a joint cluster to a rigidly bound skin.
Note the skin should be at bind pose when the cluster is added.
---

cmds.jointCluster( j='joint2', ab=20, bb=20 )

---
Return:
---


    string: Name of the new jointCluster node

Flags:
---


---
aboveBound(ab): float
    properties: create, query, edit
    Specifies the where the drop-off begins in the
direction of the bone above the joint. A value of 100 indicates
the entire length of the bone. The default value is 10.

---
aboveCluster(ac): boolean
    properties: query
    Returns the name of the cluster associated with the bone
above this joint.

---
aboveDropoffType(adt): string
    properties: create, query, edit
    Specifies the type of percentage drop-off in the direction
of the bone above this joint. Valid values are "linear",
"exponential", "sine" and "none". Default is linear.

---
aboveValue(av): float
    properties: create, query, edit
    Specifies the drop-off percentage of the joint cluster in the
direction of the bone above the cluster. A value of 100 indicates
the entire length of the bone. The default value is 50.

---
belowBound(bb): float
    properties: create, query, edit
    Specifies where the drop-off ends in the
direction of the bone below the joint. A value of 100 indicates
the entire length of the bone. The default value is 10.

---
belowCluster(bc): boolean
    properties: query
    Returns the name of the cluster associated with this joint.

---
belowDropoffType(bdt): string
    properties: create, query, edit
    Specifies the type of type of percentage drop-off in the direction
of the bone below this joint. Valid values are "linear",
"exponential", "sine" and "none".
Default is linear.

---
belowValue(bv): float
    properties: create, query, edit
    Specifies the drop-off percentage of the joint cluster in the
direction of the joint below the cluster. A value of 100 indicates
the entire length of the bone. The default value is 50.

---
deformerTools(dt): boolean
    properties: query
    Used to query for the helper nodes associated with the jointCluster.

---
joint(j): string
    properties: create
    Specifies the joint that the cluster should act about.

---
name(n): string
    properties: create
    This flag is obsolete.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/jointCluster.html 
    """


def jointCtx(autoJointOrient: string, autoPriorityH: boolean, createIKHandle: boolean, degreeOfFreedomJ: string, exists: boolean, forceSolverH: boolean, image1: string, image2: string, image3: string, jointAutoLimits: boolean, jointOrientationJ: tuple[angle, angle, angle], largeBoneLength: float, largeBoneRadius: float, poWeightH: float, priorityH: int, scaleCompensateJ: boolean, scaleJ: tuple[float, float, float], scaleOrientationJ: tuple[angle, angle, angle], secondaryAxisOrient: string, smallBoneLength: float, smallBoneRadius: float, snapHandleH: boolean, solverTypeH: string, stickyH: string, symmetry: boolean, symmetryAxis: string, variableBoneSize: boolean, weightH: float) -> string:
    """Synopsis:
---
---
 jointCtx(
[object]
    , [autoJointOrient=string], [autoPriorityH=boolean], [createIKHandle=boolean], [degreeOfFreedomJ=string], [exists=boolean], [forceSolverH=boolean], [image1=string], [image2=string], [image3=string], [jointAutoLimits=boolean], [jointOrientationJ=[angle, angle, angle]], [largeBoneLength=float], [largeBoneRadius=float], [poWeightH=float], [priorityH=int], [scaleCompensateJ=boolean], [scaleJ=[float, float, float]], [scaleOrientationJ=[angle, angle, angle]], [secondaryAxisOrient=string], [smallBoneLength=float], [smallBoneRadius=float], [snapHandleH=boolean], [solverTypeH=string], [stickyH=string], [symmetry=boolean], [symmetryAxis=string], [variableBoneSize=boolean], [weightH=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

jointCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a joint context that makes a ikHandle with an ikRPSolver.
   The use the tool.
---

cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
cmds.setToolTo( 'myJointContext' )

---
Return:
---


    string: The name of the context.

Flags:
---


---
autoJointOrient(ajo): string
    properties: create, query, edit
    Specifies the joint orientation. Valid string choices are
permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz",
"zyx". The first letter determines which axis is aligned with the
bone.
C: The default is "xyz".
Q: When queried, this flag returns a string.

---
autoPriorityH(apH): boolean
    properties: create, query, edit
    Specifies if the ikHandle's priority is assigned
automatically.
C: The default is off.
Q: When queried, this flag returns an int.

---
createIKHandle(ikh): boolean
    properties: create, query, edit
    Enables the joint tool to create an ikHandle when the tool
is completed.
C: The default is off.
Q: When queried, this flag returns an int.

---
degreeOfFreedomJ(dJ): string
    properties: create, query, edit
    Specifies the degrees of freedom for all of the joints
created by the tool. Valid string choices are the free axes;
"x", "y", "z", "xy", "xz", "yz", "xyz", and "none".
C: The default is "xyz".
Q: When queried, this flag returns a string.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
forceSolverH(fsH): boolean
    properties: create, query, edit
    Specifies if the ikSolver for the ikHandle is enabled.
C: The default is on.
Q: When queried, this flag returns an int.

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
jointAutoLimits(jal): boolean
    properties: create, query, edit
    Automatically computes the joint limits based on the
kind of joint created. 
C: The default is off.
Q: When queried, this flag returns an int.

---
jointOrientationJ(joJ): [angle, angle, angle]
    properties: create, query, edit
    Sets the orientation of the joints created by the tool.
If autoJointOrient in on, these values will be ignored.
C: The default is 0 0 0.
Q: When queried, this flag returns an array of three floats.

---
largeBoneLength(lbl): float
    properties: create, query, edit
    Specifies the length above which bones should be assigned the largeBoneRadius.

---
largeBoneRadius(lbr): float
    properties: create, query, edit
    Specifies the radius for bones whose length is above the largeBoneLength

---
poWeightH(pwH): float
    properties: create, query, edit
    Specifies the position/orientation weight of the ikHandle.
C: The default is 1.
Q: When queried, this flag returns a float.

---
priorityH(pH): int
    properties: create, query, edit
    Specifies the priority of the ikHandle.
C: The default is on.
Q: When queried, this flag returns an int.

---
scaleCompensateJ(scJ): boolean
    properties: create, query, edit
    Specifies if scale compensate is enabled.
C: The default is on.
Q: When queried, this flag returns an int.

---
scaleJ(sJ): [float, float, float]
    properties: create, query, edit
    Sets the scale for the joints created by the tool.
C: The default is 1 1 1.
Q: When queried, this flag returns an array of three floats.

---
scaleOrientationJ(soJ): [angle, angle, angle]
    properties: create, query, edit
    Sets the current value for the scale orientation.
If autoJointOrient in on, these values will be ignored.
C: The default is 0 0 0.
Q: When queried, this flag returns an array of three floats.

---
secondaryAxisOrient(sao): string
    properties: create, query, edit
    Specifies the orientation of the secondary rotate axis.
Valid string choices are: "xup", "xdown",
"yup", "ydown", "zup", "zdown", "none".

---
smallBoneLength(sbl): float
    properties: create, query, edit
    Specifies the length below which bones should be assigned the smallBoneRadius.

---
smallBoneRadius(sbr): float
    properties: create, query, edit
    Specifies the radius for bones whose length is below the smallBoneLength.

---
snapHandleH(snH): boolean
    properties: create, query, edit
    Sepcifies if snapping is enabled for the ikHandle. 
C: The default is on.
Q: When queried, this flag returns an int.

---
solverTypeH(stH): string
    properties: create, query, edit
    Sets the name of the solver to use with the ikHandle. 
C: The default is the solver set to the default in the user
preferences.
Q: When queried, this flag returns a string.

---
stickyH(sH): string
    properties: create, query, edit
    Specifies if the ikHandle is sticky or not. If "sticky" is
passed then the ikHandle will be sticky. If "off" is used then
ikHandle stickiness will be turned off.
C: The default is "off".
Q: When queried, this flag returns a string.

---
symmetry(sym): boolean
    properties: create, query, edit
    Automaticaly create a symmetry joint based if symmetry is on. 
C: The default is off.
Q: When queried, this flag returns an int.

---
symmetryAxis(sa): string
    properties: create, query, edit
    Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry. 
C: The default is x.
Q: When queried, this flag returns a string.

---
variableBoneSize(vbs): boolean
    properties: create, query, edit
    Specifies whether or not variable bone length and radius settings should be used.

---
weightH(wH): float
    properties: create, query, edit
    Specifies the weight of the ikHandle. The weight is
relative to the other ikHandles in the scene.
C: The default is 1.
Q: When queried, this flag returns a float.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/jointCtx.html 
    """


def jointDisplayScale(absolute: boolean, ikfk: float) -> float:
    """Synopsis:
---
---
 jointDisplayScale(
float
    , [absolute=boolean], [ikfk=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

jointDisplayScale is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Half the display size with respect to the default size.
---

cmds.jointDisplayScale( 0.5 )

Set the display diameter of the joint to 2 linear units.
---

cmds.jointDisplayScale( 2.0, a=True )

Set the display diameter of ik/fk joints to 2 linear units.
---

cmds.jointDisplayScale(2.0, a=True, ik=True);

---
Return:
---


    float: Returns current display size of skeleton joints.

Flags:
---


---
absolute(a): boolean
    properties: create, query, edit
    Interpret the float argument as the display size as
opposed to the scale factor.

---
ikfk(ik): float
    properties: create, query, edit
    Set the display size of ik/fk skeleton joints.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/jointDisplayScale.html 
    """


def jointLattice(after: boolean, afterReference: boolean, before: boolean, components: boolean, creasing: float, deformerTools: boolean, exclusive: string, frontOfChain: boolean, geometry: string, geometryIndices: boolean, ignoreSelected: boolean, includeHiddenSelections: boolean, joint: string, lengthIn: float, lengthOut: float, lowerBindSkin: string, lowerTransform: string, name: string, parallel: boolean, prune: boolean, remove: boolean, rounding: float, selectedComponents: boolean, split: boolean, upperBindSkin: string, upperTransform: string, useComponentTags: boolean, widthLeft: float, widthRight: float) -> string:
    """Synopsis:
---
---
 jointLattice(
selectionList
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [creasing=float], [deformerTools=boolean], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [joint=string], [lengthIn=float], [lengthOut=float], [lowerBindSkin=string], [lowerTransform=string], [name=string], [parallel=boolean], [prune=boolean], [remove=boolean], [rounding=float], [selectedComponents=boolean], [split=boolean], [upperBindSkin=string], [upperTransform=string], [useComponentTags=boolean], [widthLeft=float], [widthRight=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

jointLattice is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Select a "dualBase" lattice that is connected to a rigidly bound skin.
To create a dualBase lattice, use the dualBase flag on the lattice command.
---

cmds.jointLattice( joint='joint2', upperBindSkin='joint1Cluster1',lowerBindSkin='joint2Cluster2' )
cmds.jointLattice( upperTransform='joint1', lowerTransform='joint2', joint='joint2', upperBindSkin='joint1Cluster1',lowerBindSkin='joint2Cluster1' )
cmds.jointLattice( 'jointLattice1', edit=True, creasing=0.5 )

---
Return:
---


    string: Name of joint lattice algorithm node created/edited.

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
components(cmp): boolean
    properties: query
    Returns the components used by the deformer

---
creasing(cr): float
    properties: create, query, edit
    Affects the bulging of lattice points on the inside of
the bend.  Positive/negative values cause the points to bulge
outwards/inwards. Default value is 0.0. When queried, this flag
returns a float.

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
    properties: create
    Specifies the joint which will be used to drive the
bulging behaviours.

---
lengthIn(li): float
    properties: create, query, edit
    Affects the location of lattice points on the parent
bone.  Positive/negative values cause the points to move
away/towards the joint. Changing this parameter also modifies
the regions affected by the creasing, rounding and width
parameters. Default value is 0.0. When queried, this flag
returns a float.

---
lengthOut(lo): float
    properties: create, query, edit
    Affects the location of lattice points on the child bone.
Positive/negative values cause the points to move away/towards
the joint. Changing this parameter also modifies the regions
affected by the creasing, rounding and width parameters. Default
value is 0.0. When queried, this flag returns a float.

---
lowerBindSkin(lb): string
    properties: create
    Specifies the node which is performing the bind skin
operation on the geometry associated with the lower bone.

---
lowerTransform(lt): string
    properties: create
    Specifies which dag node is being used to rigidly transform
the lower part of the lattice which this node is going to deform.
If this flag is not specified an identity matrix will be assumed.

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
rounding(ro): float
    properties: create, query, edit
    Affects the bulging of lattice points on the outside
of the bend. Positive/negative values cause the points to bulge
outwards/inwards. Default value is 0.0. When queried, this flag
returns a float.

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
upperBindSkin(ub): string
    properties: create
    Specifies the node which is performing the bind skin
operation on the geometry associated with the upper bone.

---
upperTransform(ut): string
    properties: create
    Specifies which dag node is being used to rigidly transform
the upper part of the lattice which this node is going to deform.
If this flag is not specified an identity matrix will be assumed.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/jointLattice.html 
    """
