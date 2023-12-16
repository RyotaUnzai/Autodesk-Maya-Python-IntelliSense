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


def keyTangent(absolute: boolean, animation: string, attribute: string, controlPoints: boolean, float: floatrange, g: boolean, hierarchy: string, inAngle: angle, inTangentType: string, inWeight: float, includeUpperBound: boolean, index: uint, ix: float, iy: float, lock: boolean, outAngle: angle, outTangentType: string, outWeight: float, ox: float, oy: float, pluginTangentTypes: string, relative: boolean, shape: boolean, stepAttributes: boolean, time: timerange, unify: boolean, weightLock: boolean, weightedTangents: boolean) -> int:
    """Synopsis:
---
---
 keyTangent(
[objects]
    , [absolute=boolean], [animation=string], [attribute=string], [controlPoints=boolean], [float=floatrange], [g=boolean], [hierarchy=string], [inAngle=angle], [inTangentType=string], [inWeight=float], [includeUpperBound=boolean], [index=uint], [ix=float], [iy=float], [lock=boolean], [outAngle=angle], [outTangentType=string], [outWeight=float], [ox=float], [oy=float], [pluginTangentTypes=string], [relative=boolean], [shape=boolean], [stepAttributes=boolean], [time=timerange], [unify=boolean], [weightLock=boolean], [weightedTangents=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyTangent is undoable, queryable, and editable.
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

This command edits or queries tangent properties of keyframes
in a keyset.  It is also used to edit or query the default
tangent type of newly created keyframes (see the setKeyframe
command for more information on how to override this default).

Tangents help manage the shape of the animation curve and affect
the interpolation between keys.  The tangent angle specifies the
direction the curve will take as it leaves (or enters) a key.
The tangent weight specifies how much influence the tangent angle
has on the curve before the curve starts towards the next key.

Maya internally represents tangents as x and y values.  Refer to the API
documentation for MFnAnimCurve for a description of the relationship
between tangent angle and weight and the internal x and y values.




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

Set the in-tangent to spline for all keyframes
on an object between 1 and 2 seconds.
---

cmds.keyTangent( 'nurbsSphere1', inTangentType='spline', time=('0sec','2sec') )

Set the angle and value for the out tangent of the
keyframe at time 5 of nurbsSphere1's translateX.
---

cmds.keyTangent( 'nurbsSphere1', edit=True, time=(5,5), attribute='translateX', absolute=True, outAngle=10, outWeight=5 )

---
Return:
---


    int: Number of curves on which tangents were modified.

Flags:
---


---
absolute(a): boolean
    properties: create, edit
    Changes to tangent positions are NOT relative to the
current position.

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
float(f): floatrange
    properties: create, multiuse
    value uniquely representing a non-time-based
key (or key range) on a time-based animCurve.  Valid
floatRange include single values (-f 10) or a
string with a lower and upper bound, separated by a
colon (-f "10:20")
      In query mode, this flag needs a value.

---
g(g): boolean
    properties: create
    Required for all operations on the global tangent type.
The global tangent type is used by the setKeyframe command
when tangent types have not been specifically applied, except
in combination with flags such as 'i/insert' which preserve the shape
of the curve.  It is also used when keys are set from the menu.
The only flags that can appear on a keyTangent command
with the 'g/global' flag are 'itt/inTangentType',
'ott/outTangentType' and 'wt/weightedTangents'.

---
hierarchy(hi): string
    properties: create
    Hierarchy expansion options.  Valid values are "above,"
"below," "both," and "none." (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
inAngle(ia): angle
    properties: create, query, edit
    New value for the angle of the in-tangent.
Returns a float[] when queried.

---
inTangentType(itt): string
    properties: create, query, edit
    Specify the in-tangent type.  Valid values are
"spline," "linear," "fast," "slow," "flat," "step," "stepnext,"
"fixed," "clamped," "plateau", "auto", "autoease", "automix", and "autocustom".
Returns a string[] when queried.

---
inWeight(iw): float
    properties: create, query, edit
    New value for the weight of the in-tangent.
Returns a float[] when queried.

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
ix(ix): float
    properties: create, query, edit
    New value for the x-component of the in-tangent.
This is a unit independent representation of the tangent
component.
Returns a float[] when queried.

---
iy(iy): float
    properties: create, query, edit
    New value for the y-component of the in-tangent.
This is a unit independent representation of the tangent
component.
Returns a float[] when queried.

---
lock(l): boolean
    properties: create, query, edit
    Lock a tangent so in and out tangents move together.
Returns an int[] when queried.

---
outAngle(oa): angle
    properties: create, query, edit
    New value for the angle of the out-tangent.
Returns a float[] when queried.

---
outTangentType(ott): string
    properties: create, query, edit
    Specify the out-tangent type.  Valid values are
"spline," "linear," "fast," "slow," "flat," "step," "stepnext,"
"fixed," "clamped," "plateau" and "auto", "autoease", "automix", and
"autocustom".
Returns a string[] when queried.

---
outWeight(ow): float
    properties: create, query, edit
    New value for the weight of the out-tangent.
Returns a float[] when queried.

---
ox(ox): float
    properties: create, query, edit
    New value for the x-component of the out-tangent.
This is a unit independent representation of the tangent
component.
Returns a float[] when queried.

---
oy(oy): float
    properties: create, query, edit
    New value for the y-component of the out-tangent.
This is a unit independent representation of the tangent
component.
Returns a float[] when queried.

---
pluginTangentTypes(ptt): string
    properties: query
    Returns a list of the plug-in tangent types that have been loaded.
Return type is a string array.

---
relative(r): boolean
    properties: create, edit
    Changes to tangent positions are relative to the
current position.

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
stepAttributes(sa): boolean
    properties: create, edit
    The setKeyframe command will automatically set
tangents for boolean and enumerated attributes to step.  This
flag mirrors this behavior for the keyTangent command.  When
set to false, tangents for these attributes will not be
edited.  When set to true (the default) tangents for these
attributes will be edited.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

---
unify(uni): boolean
    properties: create, edit
    Unify a tangent so in and out tangents are equal and move together.

---
weightLock(wl): boolean
    properties: create, query, edit
    Lock the weight of a tangent so it is fixed.
Returns an int[] when queried.
Note: weightLock is only obeyed within the graph editor.  It
is not obeyed when -inWeight/-outWeight are issued from a command.

---
weightedTangents(wt): boolean
    properties: create, query, edit
    Specify whether or not the tangents on
the animCurve are weighted
Note: switching a curve from weightedTangents
true to false and back to true again will not
preserve fixed tangents properly. Use undo instead.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyTangent.html 
    """


def keyframe(absolute: boolean, adjustBreakdown: boolean, animation: string, attribute: string, breakdown: boolean, clipTime: tuple[time, time, float], controlPoints: boolean, eval: boolean, float: floatrange, floatChange: float, hierarchy: string, includeUpperBound: boolean, index: uint, indexValue: boolean, keyframeCount: boolean, lastSelected: boolean, name: boolean, option: string, relative: boolean, selected: boolean, shape: boolean, tickDrawSpecial: boolean, time: timerange, timeChange: time, valueChange: float) -> int:
    """Synopsis:
---
---
 keyframe(
[objects]
    , [absolute=boolean], [adjustBreakdown=boolean], [animation=string], [attribute=string], [breakdown=boolean], [clipTime=[time, time, float]], [controlPoints=boolean], [eval=boolean], [float=floatrange], [floatChange=float], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [indexValue=boolean], [keyframeCount=boolean], [lastSelected=boolean], [name=boolean], [option=string], [relative=boolean], [selected=boolean], [shape=boolean], [tickDrawSpecial=boolean], [time=timerange], [timeChange=time], [valueChange=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframe is undoable, queryable, and editable.
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

This command edits the time and/or value of keys of
specified objects and/or parameter curves

Unless otherwise specified by the -query flag, the command
defaults to editing keyframes.




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

import maya.cmds as cmds

Keys on animation curves are identified by either time values or indices.
Times and indices can be given as a ranges or list of ranges.

When specifying times/indices by range,
---

 time=()         means all keys.
 time=(10,)      means all keys at time 10 (in the current time unit).
 time=(10,20)    means all keys in the range from 10 to 20, inclusive, in the current time unit.
 time=('10:',)   means all keys at and after time 10
 time=(':20',)   means all keys before or at time 20
 time=('10pal',) means the key at frame 10 (PAL format).
---

 index=(0,0)     means the first key of each animation curve (i.e., indices are 0-based.)
 index=(1,5)     means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
 index=('2:',)   means all keys at and after the 3rd key
 index=(':5',)   means all keys before or at the 6th key
 index=('1:5',)  means the 2nd - 6th keys (inclusive).
---

When specifying times/indices by list
---

 time=[(1.0,1.0),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
 index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
---


Two ways to find out how many keys there are on the
paramCurve connected to surface1.translateX;
---

cmds.keyframe( 'surface1', attribute='translateX', query=True, keyframeCount=True )
cmds.keyframe( 'surface1.translateX', query=True, keyframeCount=True )

Two ways to query all keyframes of object "surface1" within the time range 0 to 20.
---

cmds.keyframe( 'surface1', time=(0,20), query=True, valueChange=True, timeChange=True);
cmds.keyframe( 'surface1', time=('0:20',), query=True, valueChange=True, timeChange=True);

Three ways to query the time of the second key in the translate X
parameter curve. Note that since indices are 0-based, the second key is at index 1.
---

cmds.keyframe('surface1.translateX',index=('1:1',),query=True);
cmds.keyframe('surface1.translateX',index=(1,1),query=True);
cmds.keyframe('surface1.translateX',index=(1,),query=True);

Shift all the active object's keys in the range 10-20
by one (current) time unit (frame, second, etc.)
---

cmds.keyframe(edit=True,relative=True,timeChange=1,time=(10,20))

Two ways to move all keys at time 10 of the active object
to time 12.  Note that "-absolute" is the default.
---

cmds.keyframe(time=(10,),timeChange=12)
cmds.keyframe(time=(10,10),absolute=True,timeChange=12)

Set the 2nd keyframe of cube1's Translate X parameter
curve to be 10.25 at time 1.5 seconds.
---

cmds.keyframe('surface1.translateX',edit=True,index=(1,1),timeChange='1.5sec',valueChange=10.25)

Evaluate the animCurve feeding into nurbsCone1's translateX attribute at time 3
---

cmds.keyframe('nurbsCone1',at='tx',t=(3,3),q=True,eval=True)

Query the times of the active keys on attribute translateX of nurbsCone1
---

cmds.keyframe( 'nurbsCone1', at='tx', sl=True, q=True, tc=True )

How many keys are selected on nurbsCone1?
---

cmds.keyframe( 'nurbsCone1', sl=True, q=True, kc=True )

Here's a script to print out all a cone's animCurves that have
keys selected.  Each animCurve is followed by a list of times
for the selected keys. The result of this script is:
  nurbsCone1_translateX: [5.0]
  nurbsCone1_translateY: [12.0]
  nurbsCone1_translateZ: [4.0, 14.0]
---

myCone = cmds.cone()
cmds.setKeyframe( myCone[0], t=[0,5,10], at='tx', v=5 )
cmds.setKeyframe( myCone[0], t=[2,7,12], at='ty', v=10 )
cmds.setKeyframe( myCone[0], t=[4,9,14], at='tz', v=15 )
cmds.selectKey( t=[(5,5),(12,12),(4,4)] )
cmds.selectKey( animation='objects', add=True, t=(14,14) )

nodes = cmds.keyframe(myCone,query=True,name=True)
for node in nodes:
   keyTimes = cmds.keyframe(node,sl=True,query=True,tc=True)
   print "  {}: {}".format(node, keyTimes)

For the above sample script, the last selected key is
nurbsCone1_translateZ: 14.  The following may be used to query
the values for that key
---

cmds.keyframe( query=True, lastSelected=True, name=True )
cmds.keyframe( query=True, lastSelected=True, timeChange=True )
cmds.keyframe( query=True, lastSelected=True, valueChange=True )

---
Return:
---


    int: (except where noted below)
Number of curves on which keys were modified.
In -query mode, the command can return a variety of things,
as described with each queryable flag below.

Flags:
---


---
absolute(a): boolean
    properties: create
    Move amounts are absolute.

---
adjustBreakdown(abd): boolean
    properties: create
    When false, moving keys will not preserve breakdown
timing, when true (the default) breakdowns will be adjusted
to preserve their timing relationship.

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
breakdown(bd): boolean
    properties: create, query, edit
    Sets the breakdown state for the key.  Returns
an integer.  Default is false.  The breakdown state of a key
cannot be set in the same command as it is moved (i.e., via
the -tc or -fc flags).

---
clipTime(ct): [time, time, float]
    properties: create
    Modifies the final time where a key is inserted using an
offset, pivot, and scale.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
eval(ev): boolean
    properties: create, query
    Returns the value(s) of the animCurves when evaluated
(without regard to input connections)
at the times given by the -t/time or -f/float flags.  Cannot
be used in combination with other query flags, and
cannot be used with time ranges (-t "5:10").
When no -t or -f flags appear on the command line, the
evals are queried at the current time.  Query returns a float[].

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
floatChange(fc): float
    properties: create, query, edit
    How much (with -relative) or where (with -absolute)
to move keys (on non-time-input animation curves)
along the x (float) axis. Returns float[] when queried.

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
indexValue(iv): boolean
    properties: create, query
    Query-only flag that returns an int for the key's index.

---
keyframeCount(kc): boolean
    properties: create, query
    Returns an int for the number of keys found for the
targets.

---
lastSelected(lsl): boolean
    properties: create, query
    When used in queries, this flag returns requested values
for the last selected key.

---
name(n): boolean
    properties: create, query
    Returns the names of animCurves of specified nodes,
attributes or keys.

---
option(o): string
    properties: create, edit
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

---
relative(r): boolean
    properties: create
    Move amounts are relative to a key's current position.

---
selected(sl): boolean
    properties: create, query
    When used in queries, this flag returns requested values
for any active keys.

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
tickDrawSpecial(tds): boolean
    properties: create, edit
    Sets the special drawing state for this key when it
is drawn as a tick in the timeline.

---
time(t): timerange
    properties: create, multiuse
    time uniquely representing a key (or key
range) on a time-based animCurve. See the code
examples below on how to format for a single
frame or frame ranges.
      In query mode, this flag needs a value.

---
timeChange(tc): time
    properties: create, query, edit
    How much (with -relative) or where (with -absolute)
to move keys (on time-input animation curves)
along the x (time) axis.  Returns float[] when queried.

---
valueChange(vc): float
    properties: create, query, edit
    How much (with -relative) or where (with -absolute)
to move keys along the y (value) axis. Returns float[]
when queried.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframe.html 
    """


def keyframeOutliner(animCurve: string, annotation: string, backgroundColor: tuple[float, float, float], defineTemplate: string, display: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 keyframeOutliner(
string
    , [animCurve=string], [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [display=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeOutliner is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.window( 'myWindow', width=850, height=75 )
cmds.formLayout( 'myForm' )
cmds.keyframeOutliner( 'myOutliner', animCurve='animCurve1' )
cmds.formLayout( 'myForm', e=True, af=[('myOutliner', 'top', 0), ('myOutliner', 'left', 0), ('myOutliner', 'bottom', 0), ('myOutliner', 'right', 0)] )
cmds.showWindow()

---
Return:
---


    string: The name of the outliner control.

Flags:
---


---
animCurve(ac): string
    properties: edit
    Name of the animation curve for which to display keyframes.

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
display(dsp): string
    properties: query, edit
    narrow | wide
What columns to display.  When "narrow", time and value will
be displayed, when "wide" tangent information will be displayed
as well

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeOutliner.html 
    """


def keyframeRegionCurrentTimeCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string) -> string:
    """Synopsis:
---
---
 keyframeRegionCurrentTimeCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionCurrentTimeCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.keyframeRegionCurrentTimeCtx()

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionCurrentTimeCtx.html 
    """


def keyframeRegionDirectKeyCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, option: string) -> string:
    """Synopsis:
---
---
 keyframeRegionDirectKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [option=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionDirectKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a direct key context for the dope sheet editor
---

cmds.keyframeRegionDirectKeyCtx( 'keyframeRegionDirectKeyContext' )

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
option(o): string
    properties: create
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionDirectKeyCtx.html 
    """


def keyframeRegionDollyCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string) -> string:
    """Synopsis:
---
---
 keyframeRegionDollyCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionDollyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a dolly view context for the dope sheet editor
---

cmds.keyframeRegionDollyCtx( 'keyframeRegionDollyContext' )

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionDollyCtx.html 
    """


def keyframeRegionInsertKeyCtx(breakdown: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string) -> string:
    """Synopsis:
---
---
 keyframeRegionInsertKeyCtx(
contextName
    , [breakdown=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionInsertKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create an insert key context for the dope sheet editor
---

cmds.keyframeRegionInsertKeyCtx( 'keyframeRegionInsertKeyContext' )

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionInsertKeyCtx.html 
    """


def keyframeRegionMoveKeyCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, option: string) -> string:
    """Synopsis:
---
---
 keyframeRegionMoveKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [option=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionMoveKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a move key context which works in insert mode
for the dope sheet editor
---

cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )

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
option(o): string
    properties: create, query, edit
    Valid values are "move," "insert," "over," and
"segmentOver". Specifies the keyframe -option to use.  When you
"move" a key, the key will not cross over
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionMoveKeyCtx.html 
    """


def keyframeRegionScaleKeyCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, scaleSpecifiedKeys: boolean, type: string) -> string:
    """Synopsis:
---
---
 keyframeRegionScaleKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [scaleSpecifiedKeys=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionScaleKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a manipulator style scale key context
for the dope sheet editor
---

cmds.keyframeRegionScaleKeyCtx( 'keyframeRegionScaleKeyContext', type='rect' )

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
scaleSpecifiedKeys(ssk): boolean
    properties: query, edit
    Determines if only the specified keys should be scaled. If false,
the non-selected keys will be adjusted during the scale. The default
is true.

---
type(typ): string
    properties: edit
    rect | manip
Specifies the type of scale manipulator to use

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionScaleKeyCtx.html 
    """


def keyframeRegionSelectKeyCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string) -> string:
    """Synopsis:
---
---
 keyframeRegionSelectKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionSelectKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a select key context for the dope sheet editor
---

cmds.keyframeRegionSelectKeyCtx( 'keyframeRegionSelectKeyContext' )

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionSelectKeyCtx.html 
    """


def keyframeRegionSetKeyCtx(breakdown: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string) -> string:
    """Synopsis:
---
---
 keyframeRegionSetKeyCtx(
contextName
    , [breakdown=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionSetKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a set key context for the dope sheet editor
---

cmds.keyframeRegionSetKeyCtx( 'keyframeRegionSetKeyContext' )

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionSetKeyCtx.html 
    """


def keyframeRegionTrackCtx(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string) -> string:
    """Synopsis:
---
---
 keyframeRegionTrackCtx([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeRegionTrackCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a track view context for the dope sheet editor
---

cmds.keyframeRegionTrackCtx( 'keyframeRegionTrackContext' )

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionTrackCtx.html 
    """


def keyframeStats(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, animEditor: string, annotation: string, autoUnitWidth: int, backgroundColor: tuple[float, float, float], classicMode: boolean, columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, precision: int, preventOverride: boolean, rowAttach: tuple[int, string, int], statusBarMessage: string, timeAnnotation: string, useTemplate: string, valueAnnotation: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 keyframeStats(
string
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [animEditor=string], [annotation=string], [autoUnitWidth=int], [backgroundColor=[float, float, float]], [classicMode=boolean], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [timeAnnotation=string], [useTemplate=string], [valueAnnotation=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeStats is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates, edits, queries a keyframe stats control.




Example:
---
import maya.cmds as cmds

cmds.window( 'myWindow', rtf=0, width=200 )
cmds.formLayout( 'myForm' )
cmds.keyframeStats( 'myOutliner' )
cmds.formLayout( 'myForm', e=True, af=[('myOutliner', 'top', 0), ('myOutliner', 'left', 0), ('myOutliner', 'bottom', 0), ('myOutliner', 'right', 0)] )
cmds.showWindow()

---
Return:
---


    string: The name of the stats control.

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
animEditor(ae): string
    properties: query, edit
    The name of the animation editor which is associated with the control

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
autoUnitWidth(auw): int
    properties: create, query, edit
    When this is non-zero the time fied widget will automatically scale
based on the unit time settings (frame or timecode). The value
of autoUnitWidth specifies the number of digits that should be
able to be displayed as the frame number. So a value of 4 will
make sure frame number 8723 can be displayed.
When the value is zero the normal widget width will be used.

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
classicMode(cm): boolean
    properties: query, edit
    Edit display mode. True means stats only, otherwise show time value.

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
precision(pre): int
    properties: query, edit
    Controls the number of digits to the right of the decimal
point that will be displayed for float-valued channels.
Default is 3.  Queried, returns an int.

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
timeAnnotation(tan): string
    properties: create, query, edit
    Annotate the time field with an extra string value.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
valueAnnotation(van): string
    properties: create, query, edit
    Annotate the value field with an extra string value.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeStats.html 
    """


def keyframeTangentControl(annotation: string, backgroundColor: tuple[float, float, float], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, precision: int, preventOverride: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 keyframeTangentControl(
string
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyframeTangentControl is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.formLayout()
cmds.keyframeTangentControl(precision=2)
cmds.showWindow()

---
Return:
---


    string: The name of the tangent control.

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
precision(pre): int
    properties: query, edit
    Controls the number of digits to the right of the decimal
point that will be displayed.
Default is 3. Queried, returns an int.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyframeTangentControl.html 
    """


def keyingGroup(activator: name, addElement: name, afterFilters: boolean, anyMember: name, category: string, clear: name, color: int, copy: name, edges: boolean, editPoints: boolean, empty: boolean, excludeDynamic: boolean, excludeRotate: boolean, excludeScale: boolean, excludeTranslate: boolean, excludeVisibility: boolean, facets: boolean, flatten: name, forceElement: name, include: name, intersection: name, isIntersecting: name, isMember: name, layer: boolean, minimizeRotation: boolean, name: string, noIntermediate: boolean, noSurfaceShader: boolean, noWarnings: boolean, nodesOnly: boolean, remove: name, removeActivator: name, renderable: boolean, setActiveFilter: string, size: boolean, split: name, subtract: name, text: string, union: name, vertices: boolean) -> boolean | list[string] | string:
    """Synopsis:
---
---
 keyingGroup(
objects
    , [activator=name], [addElement=name], [afterFilters=boolean], [anyMember=name], [category=string], [clear=name], [color=int], [copy=name], [edges=boolean], [editPoints=boolean], [empty=boolean], [excludeDynamic=boolean], [excludeRotate=boolean], [excludeScale=boolean], [excludeTranslate=boolean], [excludeVisibility=boolean], [facets=boolean], [flatten=name], [forceElement=name], [include=name], [intersection=name], [isIntersecting=name], [isMember=name], [layer=boolean], [minimizeRotation=boolean], [name=string], [noIntermediate=boolean], [noSurfaceShader=boolean], [noWarnings=boolean], [nodesOnly=boolean], [remove=name], [removeActivator=name], [renderable=boolean], [setActiveFilter=string], [size=boolean], [split=name], [subtract=name], [text=string], [union=name], [vertices=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

keyingGroup is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

cmds.file(f=1, new=1)

Create a keying group with keyable attrs of the currently selected
object
---

cmds.polySphere(n='sphere1')
sphereKG = cmds.keyingGroup(n='sphereKG')

Query the members: should return sphere1's visiblity and TRS
members = cmds.keyingGroup(sphereKG, q=True)

Create a keying group which contains another keying group
parentKG = cmds.keyingGroup(sphereKG, n='parentKG')

keying the parent KG should automatically key the sub KGs as well
cmds.select(parentKG)
cmds.setKeyframe(time=1)

Add 2 other spheres to the sphereKG
cmds.polySphere(n='sphere2');
cmds.polySphere(n='sphere3');
cmds.keyingGroup('sphere2', 'sphere3', e=True, add=sphereKG)

Make another object the activator for the sphereKG. So if
this object is keyed, the sphereKG will be keyed
Note: the activator itself does not have to be part of the
keying group. If it is not part of the keyingGroup, it
will not be keyed. So only the spheres will be keyed below.
If the cube is to be keyed as well, execute:
cmds.keyingGroup('cube1',e=True, add=sphereKG)
cmds.polyCube(n='cube1')
cmds.keyingGroup('cube1',e=True,activator=sphereKG)

Set the global active keying group filter to work on
all keying group categories.
cmds.keyingGroup(fil='AllKeyingGroups')

cmds.select('cube1')
cmds.setKeyframe(t=10)

---
Return:
---


    string: For creation operations (name of the keying group that was created or edited)
    list[string]: For query operation (names of items in the keying group)
    boolean: For isMember operation

Flags:
---


---
activator(act): name
    properties: query, edit
    Sets the selected node(s) as activators for the given keying group.
In query mode, returns list of objects that activate the given keying group

---
addElement(add): name
    properties: edit
    Adds the list of items to the given set.  If some of the
items cannot be added to the set because they are in another
set which is in the same partition as the set to edit, the
command will fail.

---
afterFilters(af): boolean
    properties: edit
    Default state is false. This flag is valid in edit mode only.
This flag is for use on sets that are acted on by deformers
such as sculpt, lattice, blendShape. The default edit mode
is to edit the membership of the group acted on by the deformer.
If you want to edit the group but not change the membership of
the deformer, set the flag to true.

---
anyMember(am): name
    properties: create
    An operation which tests whether any of the given items
are members of the given set.

---
category(cat): string
    properties: create, query, edit
    Sets the keying group's category. This is what the global, active keying
group filter will use to match.

---
clear(cl): name
    properties: edit
    An operation which removes all items from the given set making
the set empty.

---
color(co): int
    properties: create, query, edit
    Defines the hilite color of the set. Must be a value in
range [-1, 7] (one of the user defined colors).  -1 marks the
color has being undefined and therefore not having any affect.
Only the vertices of a vertex set will be displayed in this
color.

---
copy(cp): name
    properties: create
    Copies the members of the given set to a new set.
This flag is for use in creation mode only.

---
edges(eg): boolean
    properties: create, query
    Indicates the new set can contain edges only.
This flag is for use in creation or query mode only.
The default value is false.

---
editPoints(ep): boolean
    properties: create, query
    Indicates the new set can contain editPoints only.
This flag is for use in creation or query mode only.
The default value is false.

---
empty(em): boolean
    properties: create
    Indicates that the set to be created should be empty. That is,
it ignores any arguments identifying objects to be added to
the set. This flag is only valid for operations that create a new set.

---
excludeDynamic(ed): boolean
    properties: create
    When creating the keying group, exclude dynamic attributes.

---
excludeRotate(er): boolean
    properties: create
    When creating the keying group, exclude rotate attributes from
transform-type nodes.

---
excludeScale(es): boolean
    properties: create
    When creating the keying group, exclude scale attributes from
transform-type nodes.

---
excludeTranslate(et): boolean
    properties: create
    When creating the keying group, exclude translate attributes from
transform-type nodes. For example, if your keying group contains
joints only, perhaps you only want to include rotations in the
keying group.

---
excludeVisibility(ev): boolean
    properties: create
    When creating the keying group, exclude visibility attribute from
transform-type nodes.

---
facets(fc): boolean
    properties: create, query
    Indicates the new set can contain facets only.
This flag is for use in creation or query mode only.
The default value is false.

---
flatten(fl): name
    properties: edit
    An operation that flattens the structure of the given set.
That is, any sets contained by the given set will be replaced by
its members so that the set no longer contains other sets but
contains the other sets' members.

---
forceElement(fe): name
    properties: edit
    For use in edit mode only. Forces addition of the items
to the set. If the items are in another set which is in the
same partition as the given set, the items will be removed
from the other set in order to keep the sets in the partition
mutually exclusive with respect to membership.

---
include(include): name
    properties: edit
    Adds the list of items to the given set.  If some of the
items cannot be added to the set, a warning will be issued.
This is a less strict version of the -add/addElement operation.

---
intersection(int): name
    properties: create
    An operation that returns a list of items which are members of
all the sets in the list.

---
isIntersecting(ii): name
    properties: create
    An operation which tests whether the sets in the list have
common members.

---
isMember(im): name
    properties: create
    An operation which tests whether all the given items
are members of the given set.

---
layer(l): boolean
    properties: create
    OBSOLETE. DO NOT USE.

---
minimizeRotation(mr): boolean
    properties: create, query, edit
    This flag only affects the attribute contained in the immediate keyingGroup.
It does not affect attributes in sub-keyingGroups.
Those will need to set minimizeRotation on their respective keyingGroups

---
name(n): string
    properties: create
    Assigns string as the name for a new set. This flag is
only valid for operations that create a new set.

---
noIntermediate(ni): boolean
    properties: create, query
    Excludes intermediate objects when querying set members or
using the subtract, union, itersection, or isIntersecting
flags.

---
noSurfaceShader(nss): boolean
    properties: create
    If set is renderable, do not connect it to the default surface
shader.  Flag has no meaning or effect for non renderable sets.
This flag is for use in creation mode only.
The default value is false.

---
noWarnings(nw): boolean
    properties: create
    Indicates that warning messages should not be reported such
as when trying to add an invalid item to a set. (used by UI)

---
nodesOnly(no): boolean
    properties: query
    This flag is usable with the -q/query flag but is ignored if
used with another queryable flags. This flag modifies the results
of the set membership query such that
when there are attributes (e.g. sphere1.tx) or components of
nodes included in the set, only the nodes will be listed.
Each node will only be listed once, even if more than one attribute
or component of the node exists in the set.

---
remove(rm): name
    properties: edit
    Removes the list of items from the given set.

---
removeActivator(rac): name
    properties: edit
    Removes the selected node(s) as activators for the given keying group.

---
renderable(r): boolean
    properties: create, query
    This flag indicates that a special type of set should
be created. This type of set (shadingEngine as opposed to
objectSet) has certain restrictions on its membership in that
it can only contain renderable elements such as lights and
geometry. These sets are referred to as shading groups and
are automatically connected to the "renderPartition" node when
created (to ensure mutual exclusivity of the set's members with
the other sets in the partition).
This flag is for use in creation or query mode only.
The default value is false which means a normal set is
created.

---
setActiveFilter(fil): string
    properties: create, query, edit
    Sets the global, active keying group filter, which will affect activation of
keying groups. Only keying groups with categories that match the filter will be
activated. If the setActiveFilter is set to "NoKeyingGroups", keying groups will
not be activated at all. If the setActiveFilter is set to "AllKeyingGroups", we
will activate any keying group rather than just those with matching categories.

---
size(s): boolean
    properties: query
    Use the size flag to query the length of the set.

---
split(sp): name
    properties: create
    Produces a new set with the list of items and removes
each item in the list of items from the given set.

---
subtract(sub): name
    properties: create
    An operation between two sets which returns the members of the
first set that are not in the second set.

---
text(t): string
    properties: create, query, edit
    Defines an annotation string to be stored with the set.

---
union(un): name
    properties: create
    An operation that returns a list of all the members of all sets
listed.

---
vertices(v): boolean
    properties: create, query
    Indicates the new set can contain vertices only.
This flag is for use in creation or query mode only.
The default value is false.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/keyingGroup.html 
    """
