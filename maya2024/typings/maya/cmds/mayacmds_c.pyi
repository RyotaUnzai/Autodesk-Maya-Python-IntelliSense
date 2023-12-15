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


def cacheEvaluator(flagcacheFillMode: string, flagcacheFillOrder: string, flagcacheInvalidate: timerange, flagcacheName: string, flagcachedFrames: boolean, flagcachingPoints: boolean, flagcreationParameters: boolean, flagdelegateEvaluation: boolean, flagdynamicsAsyncRefresh: boolean, flagdynamicsSupportActive: boolean, flagdynamicsSupportEnabled: boolean, flagflushCache: string, flagflushCacheRange: tuple[timerange, boolean], flagflushCacheSync: boolean, flagflushCacheWait: boolean, flaghybridCacheMode: string, flaglayeredEvaluationActive: boolean, flaglayeredEvaluationCachingPoints: boolean, flaglayeredEvaluationEnabled: boolean, flaglistCacheNames: boolean, flaglistCachedNodes: boolean, flaglistValueNames: boolean, flagnewAction: string, flagnewActionParam: string, flagnewFilter: string, flagnewFilterParam: string, flagnewRule: string, flagnewRuleParam: string, flagpauseInvalidation: boolean, flagpreventFrameSkip: boolean, flagresetRules: boolean, flagresourceUsage: boolean, flagresumeInvalidation: boolean, flagsafeMode: boolean, flagsafeModeMessages: boolean, flagsafeModeTriggered: boolean, flagvalueName: string, flagwaitForCache: float) -> boolean | list[int] | list[string] | string:
    """Synopsis:
---
---
 cacheEvaluator([cacheFillMode=string], [cacheFillOrder=string], [cacheInvalidate=timerange], [cacheName=string], [cachedFrames=boolean], [cachingPoints=boolean], [creationParameters=boolean], [delegateEvaluation=boolean], [dynamicsAsyncRefresh=boolean], [dynamicsSupportActive=boolean], [dynamicsSupportEnabled=boolean], [flushCache=string], [flushCacheRange=[timerange, boolean]], [flushCacheSync=boolean], [flushCacheWait=boolean], [hybridCacheMode=string], [layeredEvaluationActive=boolean], [layeredEvaluationCachingPoints=boolean], [layeredEvaluationEnabled=boolean], [listCacheNames=boolean], [listCachedNodes=boolean], [listValueNames=boolean], [newAction=string], [newActionParam=string], [newFilter=string], [newFilterParam=string], [newRule=string], [newRuleParam=string], [pauseInvalidation=boolean], [preventFrameSkip=boolean], [resetRules=boolean], [resourceUsage=boolean], [resumeInvalidation=boolean], [safeMode=boolean], [safeModeMessages=boolean], [safeModeTriggered=boolean], [valueName=string], [waitForCache=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cacheEvaluator is NOT undoable, queryable, and editable.
This command controls caching configuration.  It allows interaction with the
caching system.


Caching configuration is done through a set of rules.  Most rules are composed
of a "filter", which is the test to be perform in order to determine if the rule
should be applied, and an "action", which is the effect that the rule application
should have on nodes that satisfy the criteria.


A caching mode is therefore a set of rules that determines which nodes are
being cached.  This mode can be serialized to a JSON string using the
"creationParameters" flag in query mode.




Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Enable evaluation cache.
cmds.cacheEvaluator(resetRules=True)
cmds.cacheEvaluator(newFilter="evaluationCacheNodes", newAction="enableEvaluationCache")
cmds.cacheEvaluator(newRule="customEvaluators")

Enable VP2 software cache.
cmds.cacheEvaluator(resetRules=True)
VP2 cache only works on a subset of types (mesh, nurbsCurve, nurbsSurface, bezierCurve),
so we still enable evaluation cache for other types.
cmds.cacheEvaluator(newFilter="evaluationCacheNodes", newAction="enableEvaluationCache")
Enabling VP2 cache will disable evaluation cache on the supported types.
cmds.cacheEvaluator(newFilter="vp2CacheNodes", newAction="enableVP2Cache", newActionParam="useHardware=0")
Custom evaluators of a higher priority than the caching evaluator
may need additional caching points around its boundary to evaluate properly.
cmds.cacheEvaluator(newRule="customEvaluators")

Enable VP2 hardware cache.
cmds.cacheEvaluator(resetRules=True)
VP2 cache only works on a subset of types (mesh, nurbsCurve, nurbsSurface, bezierCurve),
so we still enable evaluation cache for other types.
cmds.cacheEvaluator(newFilter="evaluationCacheNodes", newAction="enableEvaluationCache")
Enabling VP2 cache will disable evaluation cache on the supported types.
Note that using the vp2CacheNodes filter is equivalent to using the
"nodeTypes" filter with the right types specified as the "newFilterParam"
string, i.e. "types=+mesh,+nurbsCurve,+bezierCurve,+nurbsSurface".
cmds.cacheEvaluator(newFilter="vp2CacheNodes", newAction="enableVP2Cache", newActionParam="useHardware=1")
Custom evaluators of a higher priority than the caching evaluator
may need additional caching points around its boundary to evaluate properly.
cmds.cacheEvaluator(newRule="customEvaluators")

Enable evaluation cache using explicit node types.
cmds.cacheEvaluator(resetRules=True)
cmds.cacheEvaluator(newFilter='nodeTypes', newFilterParam='types=-constraint,+transform,+mesh,+nurbsCurve,+bezierCurve,+nurbsSurface,+subdiv,+lattice,+baseLattice,+cMuscleDebug,+cMuscleDirection,+cMuscleDisplace,+cMuscleDisplay,+cMuscleFalloff,+cMuscleKeepOut,+cMuscleObject,+cMuscleSmartCollide,+cMuscleSpline,+cMuscleSurfAttach,-THlocatorShape,+locator,+light,+camera,+imagePlane,+clusterHandle,+deformFunc,+hwShader,+pfxGeometry,+follicle', newAction='enableEvaluationCache')

cmds.cacheEvaluator(resetRules=True)
cmds.cacheEvaluator(newFilter="evaluationCacheNodes", newAction="enableEvaluationCache")
cmds.cacheEvaluator(query=True, creationParameters=True)
Result: [
    {
        "newAction": "enableEvaluationCache",
        "newFilter": "evaluationCacheNodes"
    }
] ---


Query current cache fill mode.
cmds.cacheEvaluator(query=True, cacheFillMode=True)
Result: syncAsync ---


Set new cache fill mode. Options are: 'asyncOnly', 'syncOnly', 'syncAsync'.
cmds.cacheEvaluator(cacheFillMode = 'syncAsync')

Query current cache fill order.
cmds.cacheEvaluator(query=True, cacheFillOrder=True)
Result: bidirectional ---


Set new cache fill order. Options are: 'forward', 'backward', 'bidirectional', 'forwardFromBegin'.
cmds.cacheEvaluator(cacheFillOrder='forward')

Enable the Dynamics (Simulation) Support
Outcome:  Scenes with Dynamics nodes will be cached in 'Dynamics Support Mode'
          Caching HUD will indicates the state as 'On (Dynamics Mode)'
cmds.cacheEvaluator(dynamicsSupportEnabled=True)

Query if Dynamics Support Mode is active (Dynamics nodes present in the scene)
cmds.cacheEvaluator(query=True, dynamicsSupportEnabled=True)

Disable the Dynamics Support
Outcome:  Safe mode being triggered and cached playback is disabled when Dynamics nodes present.
cmds.cacheEvaluator(dynamicsSupportEnabled=False)

Query or set the Dynamics-Async-Refresh option
cmds.cacheEvaluator(q=True,dynamicsAsyncRefresh=False)
cmds.cacheEvaluator(dynamicsAsyncRefresh=True)

Query current hybrid cache mode.
cmds.cacheEvaluator(query=True, hybridCacheMode=True)
Result: disabled ---


Set new hybrid cache mode. Options are: 'disabled', 'smp', 'all'.
cmds.cacheEvaluator(hybridCacheMode = 'smp')


Invalidate cache for all the frames in range from 10 to 20, inclusive, in current time unit.
cmds.cacheEvaluator(cacheInvalidate=('10','20'))
cmds.cacheEvaluator(cacheInvalidate=('10:20',))

Invalidate cache for all the frames in range from 10 onwards to the maximum time in the animation range, in current time unit.
cmds.cacheEvaluator(cacheInvalidate=('10:',))

Invalidate cache for all the frames in range from minimum time on the animation range up to (and including) to 10, in current time unit.
cmds.cacheEvaluator(cacheInvalidate=(':10',))

Invalidate cache from minimum to maximum time on the current animation range.
cmds.cacheEvaluator(cacheInvalidate=(':',))

Check whether or not evaluation cache is active on a given node.
cmds.cacheEvaluator("myNode", query=True, cacheName="evaluation")
Result: [u'1'] ---


cmds.cacheEvaluator("myNode", query=True, cacheName="evaluation", valueName="active")
Result: [u'1'] ---


Check whether or not VP2 cache is active, and using hardware cache.
cmds.cacheEvaluator("myNode", query=True, cacheName="VP2")
Result: [u'1'] ---


cmds.cacheEvaluator("myNode", query=True, cacheName="VP2", valueName="active")
Result: [u'1'] ---


cmds.cacheEvaluator("myNode", query=True, cacheName="VP2", valueName="useHardware")
Result: [u'1'] ---


Check whether or not delegate evaluation is active on a given node.
cmds.cacheEvaluator("myNode", query=True, delegateEvaluation=True)
Result: [u'0'] ---


cmds.cacheEvaluator(query=True, cachingPoints=True)
Result: [u'nurbsCone1', u'nurbsConeShape1'] ---


Flush current cache. "keep" and "destroy" flags can be used to store or destroy the existing cache.
cmds.cacheEvaluator(flushCache='destroy')
Result: destroy ---


Query the cache evaluator's flush synchronization mode.
cmds.cacheEvaluator(query=True, flushCacheSync=True)
Result: 0 ---


Set the cache evaluator's flush synchronization mode. Valid values are: True for synchronous, False for asynchronous.
cmds.cacheEvaluator(flushCacheSync=True)

Wait for cache destruction.
cmds.cacheEvaluator(flushCacheWait=True)

Check the available types of cache.
cmds.cacheEvaluator(query=True, listCacheNames=True)
Result: [u'evaluation', u'VP2'] ---


Query the list of cached nodes.
cmds.cacheEvaluator(query=True, listCachedNodes=True)
Result: nurbsSphere1,nurbsSphereShape1 ---


Check the available values that can be queried for available caches.
cmds.cacheEvaluator(query=True, cacheName="evaluation", listValueNames=True)
Result: [u'active'] ---


cmds.cacheEvaluator(query=True, cacheName="VP2", listValueNames=True)
Result: [u'active', u'useHardware'] ---


Query if prevent-frame-skipping is on.
cmds.cacheEvaluator(query=True, preventFrameSkip=True)
Result: 1 ---


Set prevent-frame-skipping to on.
cmds.cacheEvaluator(preventFrameSkip=True)

Query if the cache invalidation is paused. Returns how many times invalidation is paused.
cmds.cacheEvaluator(query=True, pauseInvalidation=True)
Result: 0 ---


Pause cache invalidation.
cmds.cacheEvaluator(pauseInvalidation=True)

Resume cache invalidation.
cmds.cacheEvaluator(resumeInvalidation=True)

Query whether or not the resource limit has been reached.
cmds.cacheEvaluator(query=True, resourceUsage=True)
Result: okay ---


Turn safe mode state for evaluator on.
cmds.cacheEvaluator(safeMode=True)

Query the safe mode state for evaluator.
cmds.cacheEvaluator(query=True, safeMode=True)
Result: 1 ---


If safe mode was triggered return the safe mode messages
cmds.cacheEvaluator(query=True, safeModeMessages=True)
Result:  ---


Check if safe mode was triggered
cmds.cacheEvaluator(query=True, safeModeTriggered=True)
Result: 0 ---


Wait for 10 seconds for cache to fill in background
cmds.cacheEvaluator(waitForCache=10)
Result: True ---


Save the current caching mode.
cacheModeString = cmds.cacheEvaluator(query=True, creationParameters=True)
useEval = True
if useEval:
    The return string can be evaluated as regular Python code to get an array
    of dictionaries describing the rule.
    cacheMode = eval(cacheModeString)
else:
    json.loads can also be used to parse that string.  However, it creates
    unicode strings as keys which cannot be used as argument names when
    unpacking the dictionary.
    import json
    jsonCacheMode = json.loads(cacheModeString)
    cacheMode = []
    for rule in jsonCacheMode:
        newRule = { key.encode('ascii'): value for key, value in rule.items() }
        cacheMode.append(newRule)

Restore previous cache mode.
cmds.cacheEvaluator(resetRules=True)
for rule in cacheMode:
    cmds.cacheEvaluator(**rule)


Use the CacheEvaluatorManager to get/set modes.
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
manager = CacheEvaluatorManager()
currentMode = manager.cache_mode

from maya.plugin.evaluator.CacheEvaluatorManager import CACHE_STANDARD_MODE_VP2_HW, CACHE_STANDARD_MODE_VP2_SW, CACHE_STANDARD_MODE_EVAL
Enable evaluation cache.
manager.cache_mode = CACHE_STANDARD_MODE_EVAL
Enable VP2 software cache.
manager.cache_mode = CACHE_STANDARD_MODE_VP2_SW
Enable VP2 hardware cache.
manager.cache_mode = CACHE_STANDARD_MODE_VP2_HW

Restore the previous mode.
manager.cache_mode = currentMode

---
Return:
---


    string: The state of whether the memory limit has been reached or not ('out', 'okay', 'low', or 'unlimited' with the 'resourceUsage' flag)
    boolean: The state of whether the safe mode is enabled (with the 'safeMode' flag)
    boolean: The state of whether the safe mode was triggered (with the 'safeModeTriggered' flag)
    boolean: The state of whether prevent frame skipping is enabled (with the 'preventFrameSkip' flag)
    boolean: The state of whether cache in background was calculated (with the 'waitForCache' flag)
    list[string]: The available cache names (with the 'listCacheNames' flag)
    string: The list of nodes currently cached by the cache evaluator (with the 'listCachedNodes' flag).
    list[string]: The available value names (with the 'listValueNames' flag)
    list[string]: The parameter value for the requested node(s) (with the 'cacheName' flag)
    list[string]: The state of whether delegate evaluation is enabled for the requested node(s) (with the 'delegateEvaluation' flag)
    string: The creation parameters for the current mode as a JSON array (with the 'creationParameters' flag)
    list[string]: The list of nodes marked as caching point (with the 'cachingPoints' flag)
    list[string]: The list of nodes forced as caching points because of layered evaluation (with the 'layeredEvaluationCachingPoints' flag)
    list[int]: The list of frames being cached (with the 'cachedFrames' flag)
    string: The current cache fill mode (with the 'cacheFillMode' flag)
    string: The current cache fill order (with the 'cacheFillOrder' flag)
    string: The list of all the safe mode messages (with the 'safeModeMessages' flag)
    string: The current hybrid cache mode (with the 'hybridCacheMode' flag)

Flags:
---


---
cacheFillMode(cfm): string
    properties: create, query
    Specifies the cache fill mode. Valid values are: "syncOnly" to fill cache
during playback, "syncAsync" to cache during playback and in background,
 and "asyncOnly" to fill cache only in background. Query returns current mode.

---
cacheFillOrder(cfo): string
    properties: create, query
    Specifies in which order the cache fills the timeline. Valid values are:
"forward" to fill cache in forward direction, "backward" to fill cache backwards,
"bidirectional" to fill cache in forward and backward directions simultaneously,
 and "forwardFromBegin" to fill cache in forward direction from animation start.
 Query returns current cache fill mode.

---
cacheInvalidate(ci): timerange
    properties: create
    Specifies the frame range in which cache should be invalidated. The range
should be specified as a pair of positive integers.

    Usage examples:

 -ci "10:20"{Python equivalent: ('10','20')} means all frames
        in the range from 10 to 20, inclusive, in the current time unit. 


    Omitting one end of a range means using either end of the animation range
     (or both), as in the following examples:

 -ci "10:" means all frames from time 10 (in the current time unit)
        onwards to the maximum time in the animation range (on the timeline). 
 -ci ":10" means all frames from the minimum time on the animation range
        (on the timeline) up to (and including) time 10 (in the current time unit). 
 -ci ":" is a short form to specify all frames, from minimum to
        maximum time on the current animation range.

---
cacheName(cn): string
    properties: query
    Specifies the name of the cache from which to query a value.
                        In query mode, this flag needs a value.

---
cachedFrames(cfs): boolean
    properties: query
    Get the list of frames with valid cache data.
The result is an integer array containing multiple triplets of (cache-status, begin-frame, end-frame)
For example,
The result is an array of 9 integers [(0b01, 1, 3), (0b10, 7, 10), (0b11, 13, 15)].
In MEL, the result is typed as "int[9]".
In Python, the result is typed as "Tuple[int,int,int][3]".
The result suggests frames 1:3 (1,2,3), 7:10 (7,8,9,19), and 13:15 (13,14,15) are cached.
No other frames contain valid cache data.
The cache-status numbers are always 1 if "layeredEvaluationActive" is false.
The cache-status can be one of {1,2,3}, when "layeredEvaluationActive" is true.
It represents whether the frame is valid on animation cache or dynamics cache, the encoding is:

1 (0b01) : only animation cache is valid
2 (0b10) : only dynamics cache is valid
3 (0b11) : both animation and dynamics cache are valid

In the above example, it suggests:
frames 1:3 are only valid in animation cache.
frames 7:10 are only valid in dynamics cache.
frames 13:15 are valid in both and considered as 'fully-cached'.

---
cachingPoints(cps): boolean
    properties: query
    Get list of nodes marked as caching points, i.e. nodes with at least one
type of cache active.

---
creationParameters(cp): boolean
    properties: query
    Get the current mode creation parameters.  The result is a JSON string which
represents an array with an element for each rule.  Each element is an
association between the parameter name and its value when creating the rule.

---
delegateEvaluation(de): boolean
    properties: query
    Returns whether the specified node(s) are delegating to evaluation.

---
dynamicsAsyncRefresh(dar): boolean
    properties: create, query
    Enable / Disable Asynchronous Refresh in Dynamics Support mode.
Traditionally, edits related to the simulation system require the user to re-playback the scene to see the result.
When Asynchronous Refresh is active, Maya will process the simulation in the background and refresh the viewport once the result is ready.
Note, the automatic refresh will not happen if the frame contains temproary edits. For example, an object is moved without setting the keyframe.

---
dynamicsSupportActive(dsa): boolean
    properties: query
    Query if the Dynamics Support mode is active.
Dynamics Support mode is used to support Physics Simulation, such as Hair, or Fluid.
It will be activated if such nodes are detected in the scene, and "enableDynamicsSupport" is set to true.
When Dynamics Support mode is active, you will notice the following behavior:

Dynamics nodes will be frozen for uncached frame
A separate dynamics cache line will appear on the Time Slider
Dynamics cache starts after the animation cache was filled
Dynamics cache only fills in the background
Dynamics cache always fills forward from the beginning
Dynamics cache evaluation may refresh foreground dynamics nodes (see the flag "dynamicsAsyncRefresh")

---
dynamicsSupportEnabled(dse): boolean
    properties: create, query
    Specifies if Dynamics nodes are allowed to participate in Cached Playback
When disabled, Dynamics nodes will trigger "Safe mode" and prevent caching.
When enabled, Dynamics nodes will participate in caching and trigger "Dynamics support mode".
For more information check flag "dynamicsSupportActive".

---
flushCache(fc): string
    properties: create
    Specifies to flush the current cache. Valid values are: "keep" to store the existing
cache as backup, and "destroy" to delete the current cache.

---
flushCacheRange(fcr): [timerange, boolean]
    properties: create
    Specifies the frame range in which cache should be flushed. By default it will
destroy the cache - if the 'flushCache' is also set then it will define what
to do with the cache range being flushed.
The range should be specified as a pair of positive integers and a boolean.

    Usage examples:

 -flushCacheRange "10:20" on {Python equivalent: ('10','20',True)}
                means all frames in the range from 10 to 20, inclusive, in the current time unit. 
 -flushCacheRange "12:18" off {Python equivalent: ('12','18',False)}
                means all frames before 12 and after 18, not inclusive, in the current time unit. 


    Omitting one end of a range means using either end of the animation range
     (or both), as in the following examples:

 -flushCacheRange "10:" on means all frames from time 10 (in the current time unit)
        onwards to the maximum time in the animation range (on the timeline). 
 -flushCacheRange ":10" on means all frames from the minimum time on the animation range
        (on the timeline) up to (and including) time 10 (in the current time unit). 
 -flushCacheRange ":" on is a short form to specify all frames, from minimum to
        maximum time on the current animation range.

---
flushCacheSync(fcs): boolean
    properties: create, query
    Specifies how to flush the cache: synchronously or asynchronously. True for synchronous, False for asynchronous.

---
flushCacheWait(fcw): boolean
    properties: create
    Wait for the cache destruction to be completed.

---
hybridCacheMode(hcm): string
    properties: create, query
    Specifies the hybrid cache mode. Valid values are: "disabled", not to use
hybrid cache; "smp", to evaluate on the GPU meshes with GPU-supported deformation
stacks if they use Smooth Mesh Preview (instead of caching them);
"all", to evaluate on the GPU all meshes with PU-supported deformation stacks
(instead of caching them). Query returns current mode.

---
layeredEvaluationActive(lea): boolean
    properties: query
    Query if the Layered Evaluation mode is active.
When Layered Evaluation is active, the background cache fill process will be split into multiple passes for different contents (evaluation nodes).
These contents are referred as different 'evaluation layers', representing different level of details (LoD) in animation evaluation.
For example:

The first layer contains regular animations like a character motion. 
The second layer contains dynamics simulations like a character's hair and cloth. 

Maya will create separated cache and cache fill pass for each of the layers.
Additional cache bars will be added to the Time Slider UI to represent these layers.
The background cache fill pass for each of the layer will start in order.
In the above example, two passes of background cache fill will be observed.
In the first pass of background-cache-fill or playback-fill, only Character motions will be evaluated and filled, Hair and Clothes are frozen in-place.
After the cache for first layer have been filled for all the frames,
the second pass of cache fill will start to simulate Hairs and Clothes physics and fill the cache for the 2nd layer.
Once the cache for the 2nd layer is filled for a frame, users can scrub the timeline to view the fully updated effects.
Note, when layered evaluation is active, any foreground playback or manipulation will only evaluate the first evaluation layer,
and all the FX contents will be frozen in the viewport until the background simulation is complete.
For example, when rotating a character’s head, its hair will not follow in real time.
If the flag "dynamicsAsyncRefresh" is enabled, the FX contents will be updated automatically after simulation cached up. Please refer to the flag for more detail.

---
layeredEvaluationCachingPoints(lec): boolean
    properties: query
    Get the list of nodes marked as caching points because of layered evaluation.

---
layeredEvaluationEnabled(lee): boolean
    properties: create, query
    Enable / Disable Layered Evaluation in Dynamics Support mode.
Refering to flags "dynamicsSupportActive" and "layeredEvaluationActive" for details about layered evaluation enabled behavior.
This flag is provided to support plugin developers for testing purpose.
Disabling this option in production is not recommended.
When disabled, dynamics nodes will share the same cache with regular animation.
Allows dynamics nodes to be evaluated and stored to cache in the foreground.
Background "cacheFillOrder" option will be locked to "forwardFromBegin".
When used with cacheFillMode="syncOnly", it can also be used to support legacy dynamics nodes that cannot evaluate in the background.

---
listCacheNames(lcn): boolean
    properties: query
    Return the list of existing cache names.

---
listCachedNodes(lcd): boolean
    properties: query
    Returns the list of cached nodes.

---
listValueNames(lvn): boolean
    properties: query
    Return the list of value names that can be queried for the given cache.

---
newAction(na): string
    properties: create
    Specifies the name of the new action to create in the new filter/action rule.

---
newActionParam(nap): string
    properties: create
    Specifies the parameter string to pass to the new action to create in the new filter/action rule.

---
newFilter(nf): string
    properties: create
    Specifies the name of the new filter to create in the new filter/action rule.

---
newFilterParam(nfp): string
    properties: create
    Specifies the parameter string to pass to the new filter to create in the new filter/action rule.

---
newRule(nr): string
    properties: create
    Specifies the name of the new rule to create.

---
newRuleParam(nrp): string
    properties: create
    Specifies the parameter string to pass to the new rule to create.

---
pauseInvalidation(pi): boolean
    properties: create, query
    Pause all incoming invalidation of the cache. Work in symmetry with resumeInvalidation flag.
PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation.
If queried it will return how much time caching is paused, 0 means it is resumed.

---
preventFrameSkip(pfs): boolean
    properties: create, query
    Specifies if frame skipping is enabled. Following behavior is seen when frame
skipping is enabled, and playback is set to play in real-time.

If cache can't be filled at real-time frame rate, frames will NOT be skipped.
Once all frames have been looped over(and therefore all frames are cached), and if
    playing back from cache still can't be done at real-time frame rate; frames WILL be skipped.
If memory limit is reached before all frames are cached, frames WILL be skipped.
If cache is invalidated will playing(like flushing it), frames will NOT
    be skipped(until the cache is full again).

---
resetRules(rr): boolean
    properties: create
    Reset the cache configuration rules to an empty set of rules.

---
resourceUsage(ru): boolean
    properties: query
    Returns the current state of the resource usage as a string. 'unlimited' = the resource limits
are being ignored, 'out' = the memory limit has been reached, 'low' = the memory usage is at
90% of the specified limit, 'okay' = memory usage is under 90% of the specified limit.

---
resumeInvalidation(ri): boolean
    properties: create, query
    Resume all incoming invalidation of the cache. Work in symmetry with pauseInvalidation flag.
PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation.
If queried it will return true if cache is resumed, false otherwise.

---
safeMode(sf): boolean
    properties: create, query
    Turns safe mode on or off. In query mode, it returns the status of the safe mode for cache evaluator.

---
safeModeMessages(sfm): boolean
    properties: query
    Prints the safe mode messages to the console.

---
safeModeTriggered(sft): boolean
    properties: query
    Returns if the safe mode was triggered for cache evaluator.

---
valueName(vn): string
    properties: query
    Specifies the name of the parameter for which to query the value.
                        In query mode, this flag needs a value.

---
waitForCache(wfc): float
    properties: create
    Specifies to wait for cache to fill in background, with [Time to wait in seconds] timeout.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cacheEvaluator.html 
    """


def cacheFile(flagappendFrame: boolean, flagattachFile: boolean, flagcacheFileNode: string, flagcacheFormat: string, flagcacheInfo: string, flagcacheableAttrs: string, flagcacheableNode: string, flagchannelIndex: boolean, flagchannelName: string, flagconvertPc2: boolean, flagcreateCacheNode: boolean, flagcreationChannelName: string, flagdataSize: boolean, flagdeleteCachedFrame: boolean, flagdescriptionFileName: boolean, flagdirectory: string, flagdoubleToFloat: boolean, flagendTime: time, flagfileName: string, flagformat: string, flaggeometry: boolean, flaginAttr: string, flaginTangent: string, flaginterpEndTime: time, flaginterpStartTime: time, flagnoBackup: boolean, flagoutAttr: string, flagoutTangent: string, flagpc2File: string, flagpointCount: boolean, flagpoints: string, flagpointsAndNormals: string, flagprefix: boolean, flagrefresh: boolean, flagreplaceCachedFrame: boolean, flagreplaceWithoutSimulating: boolean, flagrunupFrames: int, flagsampleMultiplier: int, flagsimulationRate: time, flagsingleCache: boolean, flagstartTime: time, flagstaticCache: boolean, flagworldSpace: boolean) -> string:
    """Synopsis:
---
---
 cacheFile([appendFrame=boolean], [attachFile=boolean], [cacheFileNode=string], [cacheFormat=string], [cacheInfo=string], [cacheableAttrs=string], [cacheableNode=string], [channelIndex=boolean], [channelName=string], [convertPc2=boolean], [createCacheNode=boolean], [creationChannelName=string], [dataSize=boolean], [deleteCachedFrame=boolean], [descriptionFileName=boolean], [directory=string], [doubleToFloat=boolean], [endTime=time], [fileName=string], [format=string], [geometry=boolean], [inAttr=string], [inTangent=string], [interpEndTime=time], [interpStartTime=time], [noBackup=boolean], [outAttr=string], [outTangent=string], [pc2File=string], [pointCount=boolean], [points=string], [pointsAndNormals=string], [prefix=boolean], [refresh=boolean], [replaceCachedFrame=boolean], [replaceWithoutSimulating=boolean], [runupFrames=int], [sampleMultiplier=int], [simulationRate=time], [singleCache=boolean], [startTime=time], [staticCache=boolean], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cacheFile is undoable, queryable, and editable.
When the ia/inAttr flag is used, connects a cacheFile node that
associates the data file on disk with the attribute.

Frames can be replaced/appended to an existing cache with the
rcf/replaceCachedFrame and apf/appendFrame flag.  Replaced frames are never deleted.
They are stored in the same directory as the original cache files with the
name provided by the f/fileName flag. If no file name is provided,
the cacheFile name is prefixed with "backup" followed by a unique number.

Single file caches are backed up in their entirety. To revert to an older
version, simply attach to this cache. One file per frame caches only backup
the description file and the frames that were replaced. To recover these
types of caches, the user must rename these files to the original name.




Example:
---
import maya.cmds as cmds

Create a disk cache containing the points of a plane from
frames 1 - 100. Typically the shape would be deforming.
---

cmds.polyPlane()
cacheFiles = cmds.cacheFile(f='shapeCache', st=1, et=100, points='pPlaneShape1')

Add a historySwitch node to the history of the shape, and attach the
newly created cache into the historySwitch node.
---

switch = maya.mel.eval('createHistorySwitch("pPlaneShape1",false)')
cacheNode = cmds.cacheFile(f=cacheFiles[0], cnm='pPlaneShape1', ia='%s.inp[0]' % switch ,attachFile=True)
cmds.setAttr( '%s.playFromCache' % switch, 1 )

query the files associated with a cacheFile node
---

cmds.cacheFile( cacheNode, query=True, f=True )

Now use the staticCache flag to indicate that the cache should not be
created if the object appears to have no animation.
Since the plane is not animated or deformed, no cache will be created.
---

cmds.polyPlane()
cacheFiles = cmds.cacheFile(f='shapeCache', staticCache=0, st=1, et=100, points='pPlaneShape2')

Convert a maya cache into pc2 format. The maya cache is named
pSphereShape1.xml and located in the directory "c:/test/".
---

cmds.cacheFile(pc2=0,pcf='c:/test/mypc2.pc2',f='pSphereShape1',dir='c:/test/')

Convert a pc2 cache into a maya cache, with the cache data in a single
file.
---

cmds.cacheFile(pc2=1,pcf='c:/test/mypc2.pc2',f='mayaCache2',dir='c:/test/',format='OneFile')

---
Return:
---


    string: name of created cache description file(s)

Flags:
---


---
appendFrame(apf): boolean
    properties: create
    Appends data to the cache for the times specified by the startTime and endTime flags. If no
time is provided, appends the current time. Must be used in conjunction
with the pts/points or cnd/cacheableNode flag. Any overwritten frames will not be
deleted, but renamed as specified by the f/fileName flag.

---
attachFile(af): boolean
    properties: create
    Used to indicate that rather than creating a cache file, that an
existing cache file on disk should be attached to an attribute in the scene.
The inAttr flag is used to specify the attribute.

---
cacheFileNode(cfn): string
    properties: create, multiuse
    Specifies the name of the cache file node(s) we are appending/replacing to
if more than one cache is attached to the specified geometries.
                        In query mode, this flag needs a value.

---
cacheFormat(cf): string
    properties: create, query
    Cache file format, default is Maya's .mcx format, but others available via plugin

---
cacheInfo(ci): string
    properties: create, query, multiuse
    In create mode, used to specify a mel script returning a string array. When
creating the cache, this mel script will be executed and the returned strings
will be written to the .xml description file of the cache.
In query mode, returns descriptive info stored in the cacheFile such as
the user name, Maya scene name and maya version number.

---
cacheableAttrs(cat): string
    properties: query
    Returns the list of cacheable attributes defined on the accompanying cache node.
This argument requires the use of the cacheableNode flag.

---
cacheableNode(cnd): string
    properties: create, multiuse
    Specifies the name of a cacheable node whose contents will be cached.
A cacheable node is a node that is specially designed to work with
the caching mechanism.  An example of a cacheable node is a nCloth node.
                        In query mode, this flag needs a value.

---
channelIndex(chi): boolean
    properties: create, query
    A query-only flag which returns the channel index for the selected geometry
for the cacheFile node specified using the cacheFileNode flag.

---
channelName(cnm): string
    properties: create, query, multiuse
    When attachFile is used, used to indicate the channel in the file that
should be attached to inAttr.  If not specified, the first channel in
the file is used. In query mode, allows user to query the channels associated
with a description file.

---
convertPc2(pc2): boolean
    properties: create
    Convert a PC2 file to the Maya cache format (true), or convert Maya cache to pc2 format (false)

---
createCacheNode(ccn): boolean
    properties: create
    Used to indicate that rather than creating a cache file, that a cacheFile
node should be created related to an existing cache file on disk.

---
creationChannelName(cch): string
    properties: create, multiuse
    When creating a new cache, this multi-use flag specifies the channels to be cached.
The names come from the cacheable channel names defined by the object being cached.
If this flag is not used when creating a cache, then all cacheable channels are cached.

---
dataSize(dsz): boolean
    properties: query
    This is a query-only flag that returns the size of the data being cached per frame.
This flag is to be used in conjunction with the cacheableNode, points,
pointsAndNormals and outAttr flags.

---
deleteCachedFrame(dcf): boolean
    properties: create
    Deletes cached data for the times specified by the startTime/endTime flags.
If no time is provided, deletes the current frame. Must be used in conjunction
with the pts/points or cnd/cacheableNode flag. Deleted frames will not be
removed from disk, but renamed as specified by the f/fileName flag.

---
descriptionFileName(dfn): boolean
    properties: query
    This is a query-only flag that returns the name of the description file
for an existing cacheFile node. Or if no cacheFile node is specified, it
returns the description file name that would be created based on the other
flags specified.

---
directory(dir): string
    properties: create, query
    Specifies the directory where the cache files will be located. If the
directory flag is not specified, the cache files will be placed in the
project data directory.

---
doubleToFloat(dtf): boolean
    properties: create
    During cache creation, double data is stored in the file as floats.  This helps cut down
file size.

---
endTime(et): time
    properties: create
    Specifies the end frame of the cache range.

---
fileName(f): string
    properties: create, query
    Specifies the base file name for the cache files. If more than one object is
being cached and the format is OneFilePerFrame, each cache file will be
prefixed with this base file name. In query mode, returns the files
associated with the specified cacheFile node.
When used with rpf/replaceCachedFrame or apf/appendFrame specifies the name of the backup files.
If not specified, replaced frames will be stored with a default name.
                        In query mode, this flag can accept a value.

---
format(fm): string
    properties: create
    Specifies the distribution format of the cache.  Valid values are "OneFile" and "OneFilePerFrame"

---
geometry(gm): boolean
    properties: query
    A query flag which returns the geometry controlled by the specified cache node

---
inAttr(ia): string
    properties: create, multiuse
    Specifies the name of the attribute that the cache file will drive.
This file is optional when creating cache files.
If this flag is not used during create mode, the cache files will
be created on disk, but will not be driving anything in the scene.
This flag is required when the attachFile flag is used.

---
inTangent(it): string
    properties: create
    Specifies the in-tangent type when interpolating frames before the replaced
frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags.
Valid values are "linear", "smooth" and "step".

---
interpEndTime(iet): time
    properties: create
    Specifies the frame until which there will be linear interpolation, beginning
at endTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flag.
Interpolation is achieved by removing frames between endTime and
interpEndTime from the cache. Removed frames will be renamed as specified
by the f/fileName flag.

---
interpStartTime(ist): time
    properties: create
    Specifies the frame from which to begin linear interpolation, ending at
startTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flags.
Interpolation is achieved by removing  frames between interpStartTime and
startTime from the cache. These removed frames will will be renamed as
specified by the f/fileName flag.

---
noBackup(nb): boolean
    properties: create
    Specifies that backup files should not be created for any files that may be over-written during
append, replace or delete cache frames. Can only be used with the apf/appendFrame,
rpf/replaceCachedFrame or dcf/deleteCachedFrame flags.

---
outAttr(oa): string
    properties: create, multiuse
    Specifies the name of the attribute that will be cached to disk.
                        In query mode, this flag needs a value.

---
outTangent(ot): string
    properties: create
    Specifies the out-tangent type when interpolating frames after the replaced
frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags.
Valid values are "linear", "smooth" and "step".

---
pc2File(pcf): string
    properties: create
    Specifies the full path to the pc2 file.  Must be used in conjunction with the pc2 flag.

---
pointCount(pc): boolean
    properties: query
    A query flag which returns the number of points stored in the cache file.
The channelName flag should be used to specify the channel to be queried.

---
points(pts): string
    properties: create, multiuse
    Specifies the name of a geometry whose points will be cached.
                        In query mode, this flag needs a value.

---
pointsAndNormals(pan): string
    properties: create, multiuse
    Specifies the name of a geometry whose points and normals will be cached.
The normals is per-vertex per-polygon. The normals cache cannot be imported
back to geometry.
This flag can only be used to export cache file. It cannot be used with
the apf/appendFrame, dcf/deleteCachedFrame and rpf/replaceCachedFrame flags.
                        In query mode, this flag needs a value.

---
prefix(p): boolean
    properties: create
    Indicates that the specified fileName should be used as a prefix for the
cacheName.

---
refresh(r): boolean
    properties: create
    When used during cache creation, forces a screen refresh during caching.
This causes the cache creation to be slower but allows you to see how the
simulation is progressing during the cache.

---
replaceCachedFrame(rcf): boolean
    properties: create
    Replaces cached data for the times specified by the startTime/endTime
flags. If no time is provided, replaces cache file for the current time.
Must be used in conjunction with the pts/points or cnd/cacheableNode flag.
Replaced frames will not be deleted, but renamed as specified by the
f/fileName flag.

---
replaceWithoutSimulating(rws): boolean
    properties: edit
    When replacing cached frames, this flag specifies whether the replacement should
come from the cached node without simulating or from advancing time and letting
the simulation run.  This flag is valid only when neither the startTime nor endTime flags
are used or when both the startTime and endTime flags specify the same time value.

---
runupFrames(rf): int
    properties: create, query, edit
    Specifies the number of frames of runup to simulate ahead of the starting frame.
The value must be greater than or equal to 0.  The default is 2.

---
sampleMultiplier(spm): int
    properties: create, query, edit
    Specifies the sample rate when caches are being created as a multiple of
simulation Rate. If the value is 1, then a sample will be cached everytime
the time is advanced.  If the value
is 2, then every other sample will be cached, and so on.  The default is 1.

---
simulationRate(smr): time
    properties: create, query, edit
    Specifies the simulation rate when caches are being created.  During cache
creation, the time will be advanced by the simulation rate, until the end
time of the cache is reached or surpassed.  The value is given in frames.
The default value is 1 frame.

---
singleCache(sch): boolean
    properties: create
    When used in conjunction with the points, pointsAndNormal or cacheableNode
flag, specifies whether multiple geometries should be put into a single
cache or to create one cache per geometry (default).

---
startTime(st): time
    properties: create
    Specifies the start frame of the cache range.

---
staticCache(sc): boolean
    properties: create, query
    If false, during cache creation, do not save a cache for the object if it
appears to have no animation or deformation. If true, save a cache even if
the object appears to have no animation or deformation. Default is true. In
query mode, when supplied a shape, the flag returns true if the shape appears
to have no animation or deformation.

---
worldSpace(ws): boolean
    properties: create
    If the points flag is used, turning on this flag will result in the world
space positions of the points being written. The expected use of this
flag is for cache export.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cacheFile.html 
    """


def cacheFileCombine(flagcacheIndex: boolean, flagchannelName: string, flagconnectCache: string, flagkeepWeights: boolean, flaglayerNode: boolean, flagnextAvailable: boolean, flagobject: string, flagobjectIndex: int) -> string:
    """Synopsis:
---
---
 cacheFileCombine([cacheIndex=boolean], [channelName=string], [connectCache=string], [keepWeights=boolean], [layerNode=boolean], [nextAvailable=boolean], [object=string], [objectIndex=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cacheFileCombine is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a cacheBlend node so that additional caches can be added to
the shape. This will attach the existing cacheFile on the shape
to the new cacheBlend node.
---

cmds.select( 'cachedShape', r=True )
newBlend = cmds.cacheFileCombine()

attach an additional cacheFile to the cacheBlend node
---

cmds.cacheFileCombine( newBlend[0], e=True, cc='cacheFile2' )

query the index of the newly connected cache
---

cmds.cacheFileCombine( newBlend[0], cc='cacheFile2', query=True, cacheIndex=True )

When more than one object is driven by the caches connected
to the cacheBlend node, the -channelName and -objectIndex flags can be
used to control which is connected.
---

Query the objectIndex for the armShape geometry driven by cacheBlend3:
---

index = cmds.cacheFileCombine('cacheBlend3' ,object='armShape', query=True, objectIndex=True)

Connect another cache up to drive the armShape
---

cmds.cacheFileCombine( 'cacheBlend3', channelName='myChannel', objectIndex=index, e=True, cc='cacheFile2' )

---
Return:
---


    string: Name of created cache layer node(s)

Flags:
---


---
cacheIndex(ci): boolean
    properties: query
    A query only flag that returns the index related to the
cache specified with the connectCache flag.

---
channelName(cnm): string
    properties: edit, multiuse
    Used in conjunction with the connectCache flag to indicate the channel(s) that
should be connected.  If not specified, the first channel in the file is used.

---
connectCache(cc): string
    properties: query, edit
    An edit flag that specifies a cacheFile node that should be connected to the next available index on the specified cacheBlend node. As a query flag, it returns a string array containing the cacheFiles that feed into the specified cacheBlend node.
                        In query mode, this flag can accept a value.

---
keepWeights(kw): boolean
    properties: edit
    This is a flag for use in combination with the connectCache flag only. By default, the connectCache flag will set all weights other than the newly added cacheWeight to 0 so that the new cache gets complete control. This flag disables that behavior so that all existing blend weights are retained.

---
layerNode(ln): boolean
    properties: query
    A query flag that returns a string array of the existing cacheBlends on the selected object(s). Returns an empty string array if no cacheBlends are found.

---
nextAvailable(na): boolean
    properties: query
    A query flag that returns the next available index on the selected cacheBlend node.

---
object(obj): string
    properties: query
    This flag is used in combination with the objectIndex flag. It is
used to specify the object whose index you wish to query.
                        In query mode, this flag needs a value.

---
objectIndex(oi): int
    properties: query, edit
    In edit mode, used in conjunction with the connectCache flag to indicate
the objectIndex to be connected.
In query mode, returns the index related to the object specified with
the object flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cacheFileCombine.html 
    """


def cacheFileMerge(flagendTime: time, flaggeometry: boolean, flagstartTime: time) -> float[] | list[string]:
    """Synopsis:
---
---
 cacheFileMerge([endTime=time], [geometry=boolean], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cacheFileMerge is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Find associated geometry nodes
---

geom = cmds.cacheFileMerge('cache1', 'cache2' ,query=True, geometry=True)

Validate merging of caches and find out start/end times.
This will give a warning if there is a gap letting you know that
simulation data will fill the gap.
---

startEndTimes = cmds.cacheFileMerge('cache1', 'cache2')
Result: { 0, 20, 5, 10 }

start = startEndTimes[0]
end = startEndTimes[1]
gapStart = startEndTimes[2]
gapEnd = startEndTimes[3]

Create a new merged cache, using simulation data to fill in
any gaps between cache1 and cache2.
---

cacheFiles = cmds.cacheFile(fileName='mergedCache', startTime=start, endTime=end, points=geom[0])
switch = maya.mel.eval('createHistorySwitch("pPlaneShape1", false)');
cmds.cacheFile( attachFile=True, f=cacheFiles[0], ia='%s.inp[0]' % switch)
cmds.setAttr( '%s.playFromCache' % switch, 1 )

Alternatively, can use append to make sure that we interpolate
for the frames in the gap between cache1 and cache2.
---

cacheFiles = cmds.cacheFile(fileName='mergedCache', startTime=start, endTime=gapStart, points=geom[0])
switch = maya.mel.eval('createHistorySwitch("pPlane1", false)');
cmds.cacheFile( attachFile=True, f=cacheFiles[0], ia='%s.inp[0]' % switch)
cmds.setAttr( '%s.playFromCache' % switch, 1 )
cmds.cacheFile( replaceCachedFrame=True, startTime=gapEnd, endTime=end, points=geom[0] )

---
Return:
---


    float[]: The start and end times of merged cache followed by start/end of any gaps
    list[string]: Names of geometry associated with specified cache in query mode.

Flags:
---


---
endTime(et): time
    properties: create
    Specifies the end frame of the merge range. If not specified, will figure
out range from times of caches being merged.

---
geometry(g): boolean
    properties: query
    Query-only flag used to find the geometry nodes associated with the specified cache files.

---
startTime(st): time
    properties: create
    Specifies the start frame of the merge range. If not specified, will figure
out range from the times of the caches being merged.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cacheFileMerge.html 
    """


def cacheFileTrack(flaginsertTrack: uint, flaglock: boolean, flagmute: boolean, flagremoveEmptyTracks: boolean, flagremoveTrack: uint, flagsolo: boolean, flagtrack: uint) -> None:
    """Synopsis:
---
---
 cacheFileTrack([insertTrack=uint], [lock=boolean], [mute=boolean], [removeEmptyTracks=boolean], [removeTrack=uint], [solo=boolean], [track=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cacheFileTrack is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Move the cache clip named "cubeCache2" to track 3
---

cmds.cacheFileTrack( 'cubeCache2', track=3 )

Lock the track containing the cache clip named "sphCache1"
---

cmds.cacheFileTrack( 'sphCache1', lock=True )

Remove any empty cache tracks for the object "sphereShape1"
---

cmds.cacheFileTrack('sphereShape1',removeEmptyTracks=True)

query the track index of the cache clip named "sphCache1"
---

cmds.cacheFileTrack( 'sphCache1', q=True, track=True )

---


Flags:
---


---
insertTrack(it): uint
    properties: create
    This flag is used to insert a new empty track at the track index
specified.

---
lock(l): boolean
    properties: create, query, edit
    This flag specifies whether clips on a track are to be locked or not.

---
mute(m): boolean
    properties: create, query, edit
    This flag specifies whether clips on a track are to be muted or not.

---
removeEmptyTracks(ret): boolean
    properties: create
    This flag is used to remove all tracks that have no clips.

---
removeTrack(rt): uint
    properties: create
    This flag is used to remove the track with the specified index.  The
track must have no clips on it before it can be removed.

---
solo(so): boolean
    properties: create, query, edit
    This flag specifies whether clips on a track are to be soloed or not.

---
track(t): uint
    properties: create, query, edit
    Used to specify a new track index for a cache to be displayed. Track-indices are 1-based.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cacheFileTrack.html 
    """


def callbacks(flagaddCallback: script, flagclearAllCallbacks: boolean, flagclearCallbacks: boolean, flagdescribeHooks: boolean, flagdumpCallbacks: boolean, flagexecuteCallbacks: boolean, flaghook: string, flaglistCallbacks: boolean, flagowner: string, flagremoveCallback: script) -> list[string]:
    """Synopsis:
---
---
 callbacks([addCallback=script], [clearAllCallbacks=boolean], [clearCallbacks=boolean], [describeHooks=boolean], [dumpCallbacks=boolean], [executeCallbacks=boolean], [hook=string], [listCallbacks=boolean], [owner=string], [removeCallback=script])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

callbacks is NOT undoable, NOT queryable, and NOT editable.describeHooks


Example:
---
import maya.cmds as cmds

def myCallbackFunction(arg1, arg2):
                return arg1 + arg2

add a new callback for myPlugin to be called when creating the attribute editor UI
cmds.callbacks(addCallback=myCallbackFunction, hook='desiredHook', owner='myPlugin')
remove an individual callback
cmds.callbacks(removeCallback=myCallbackFunction, hook='desiredHook', owner='myPlugin')
remove all callbacks for myPlugin for a specified hook
cmds.callbacks(clearCallbacks=True, hook='desiredHook', owner='myPlugin')
remove all callbacks for myPlugin for all hooks
cmds.callbacks(clearCallbacks=True, owner='myPlugin')
list callbacks for a specified hook
callbacks = cmds.callbacks(listCallbacks=True, hook='desiredHook')
list callbacks for a specified hook and for a specified owner
callbacks = cmds.callbacks(listCallbacks=True, hook='desiredHook', owner='myPlugin')
get a list of the standard Maya hooks
cmds.callbacks(describeHooks=True)
execute the callbacks for the hook 'desiredHook'
results = cmds.callbacks('arg1', 'arg2', executeCallbacks=True, hook='desiredHook')

---
Return:
---


    list[string]: Command result

Flags:
---


---
addCallback(ac): script
    properties: create
    Add a callback for the specified hook. The owner must also be specified
when adding callbacks.

---
clearAllCallbacks(cac): boolean
    properties: create
    Clear all the callbacks for all hooks and owners. This is generally
only used during plugin development and testing as it affects all callbacks
registered by Maya and other third parties.

---
clearCallbacks(cc): boolean
    properties: create
    Clear all the callbacks for the specified owner. If a hook is specified,
only the callbacks for that hook and owner will be cleared.

---
describeHooks(dh): boolean
    properties: create
    List the standard Maya hooks. Below is a list of the hooks and their associated arguments
and return values. Custom hooks added by third parties are not listed.


hyperShadePanelBuildCreateMenu

This hook is called to add content to the Hypershade panel create menu. It will
be called after the standard Maya node entries have been created.

This callback does not have any arguments or return values. In order to preserve
the desired look in the Maya UI, these callbacks should add a menu item divider just
before returning using: menuItem -divider true.

hyperShadePanelBuildCreateSubMenu

This hook is called to get a classification string for the custom renderer
shading nodes, to prevent them from being listed with the standard Maya nodes.

This callback does not have any arguments.

returns: a classification string, such as rendernode/myrenderer


hyperShadePanelPluginChange

This hook is called when a plugin change event (loading / unloading) has occurred to inform Maya whether the
Hypershade panel needs to be rebuilt.

classification (string): classification string belonging to a plugin node,
    possibly from another plugin
changeType (string): either loadPlugin or unloadPlugin
returns: (int) non-zero if your plugin is responsible for nodes of this classification,
    and a Hypershade rebuild is required


createRenderNodeSelectNodeCategories

This hook is called when the Create Render Node dialog is being constructed, and allows
a third party to have their nodes selected by default. A flag of the form -allWithMyRendererUp
is the standard form, and the selection can be set up in the tree lister in the callback.

There is no return value for this callback.

flag (string): flag passed to the Create Render Node dialog command with the leading minus (-) removed
treeLister (string): the tree lister widget which should be affected


For example, your callback might look like:


global proc myRendererCreateRenderNodeSelectNodeCategoriesCallback(string $flag, string $treeLister){
    if($flag == "allWithMyRendererUp") {
        treeLister -e -selectPath "myrenderer" $treeLister;
    }
}


createRenderNodePluginChange

This hook is called when a plugin change event has occurred to decide if the
Create Render Node dialog needs to be closed.

classification (string): classification string belonging to a plugin node,
    possibly from another plugin
returns: (int) non-zero if your plugin is responsible for nodes of this classification,
    and the Create Render Node dialog needs to be closed


renderNodeClassification

This hook is called to get a classification string for the custom renderer
shading nodes.  This is used to determine if a given node type belongs to
a plugin renderer.

This callback does not have any arguments.

returns: a classification string, such as rendernode/myrenderer


createRenderNodeCommand

This hook is called to give plugin renderers the chance to register their own command for
creating their nodes from the render node treeLister and Node Editor. The callback should
determine from the classification of the node type in question if it is theirs, and if so,
return the appropriate command for creating new nodes of that type.


postCommand (string): command to be run after the create command
type (string): nodeType
returns: (string) MEL create command


buildRenderNodeTreeListerContent

This hook is called to give plugin renderers the chance to add their content to the render node
tree lister.


renderNodeTreeLister (string): the render node tree lister
postCommand (string): command to be run post-creation
filterString (string): a space delimited list of filters


AETemplateCustomContent

This hook is called to give plugins a chance to add content to the Attribute Editor for nodes which source AEdependNodeTemplate.


nodeName (string): the name of the node for which the Attribute Editor is being constructed


firstConnectedShader

This hook is called to determine the primary custom shader connected to the given Shading Engine.


nodeName (string): the name of the Shading Engine
returns (string): the name of the custom shader if applicable


allConnectedShaders

This hook is called to determine all the shaders connected to the given Shading Engine.


nodeName (string): the name of the Shading Engine
returns (string): a colon separated list of the connected custom shaders (shader1:shader2:shader3)


renderLayerPresetMenu

This hook is called to give plugins a chance to add presets to a renderLayer node.


nodeName (string): the name of the renderLayer node


addBakingMenuItems

This hook is called to give plugins a chance to add baking menu items to the global Render - Lighting/Shading menu.


menuItemAnchor (string): the name of the menuItem which the new baking menu items should be inserted after. 


addVertexBakingMenuItems

This hook is called to give plugins a chance to add baking menu items to the global Polygon - Color menu.


addPrelightMenuItems

This hook is called to give plugins a chance to add pre-lighting menu items to the global Polygon - Color Set Editor menu.


addRMBBakingMenuItems

This hook is called to give plugins a chance to add baking menu items to the RMB menu.


objectName (string): the name of the object the right mouse button event occured on.


addMayaRenderingPreferences

This hook is called to give plugins a chance to add custom preferences to the Maya's Rendering Preferences section.


updateMayaRenderingPreferences

This hook is called to give plugins a chance to update custom preferences of the Maya's Rendering Preferences section.


addMayaMuscleMenuItems

This hook is called to give plugins a chance to add menu items to the Maya muscle Displace menu.


menuItemAnchor (string): the name of the menuItem which the new Maya muscle menu items should be inserted after. 


addMayaMuscleShelfButtons

This hook is called to give plugins a chance to add items to the Maya muscle shelves.


addBackburnerRendererMenuItems

This hook is called to give plugins a chance to add items to Maya's Backburner list of available renderers. Note: The menuItem added must be named with the short name equivalent of the renderer. eg: The Maya software renderer adds a menuItem named 'sw'.


provideAETemplateForNodeType

This hook is called to give plugins a chance to provide a UI template for nodes which do not have a corresponding AE'nodeType'Template procedure.


nodeType (string): the type of the node for which the AE is being constructed. 
returns (string): the name of a MEL command or procedure to use as the AETemplate for the requested node type. 


AEnewMultiHandler

This hook is called to give plugins a chance to provide a UI creation handler for multi attributes.


nodeName (string): the name of the node for which the AE is being constructed. 
atributeName (string): the name of the multi attribute.
uiName (string): the UI name of the attribute.
changedCommand (string): the MEL command or procedure to be executed when the value of the multi attribute is changed.
elementIndexString (string): a colon separated list of indices at which the elements of the multi attribute live.
returns (string): if the callback handled the attribute then it should return the full name of the topmost UI element that it created, otherwise it should return an empty string.


AEreplaceMultiHandler

This hook is called to give plugins a chance to provide an update handler for multi attributes.


layoutName (string): the well defined name of the Maya UI component which represents the multi attribute (.
nodeName (string): the name of the node for which the AE is being constructed. 
atributeName (string): the name of the multi attribute.
changedCommand (string): the MEL command or procedure to be executed when the value of the multi attribute is changed.
elementIndexString (string): a colon separated list of indices at which the elements of the multi attribute live.
returns (int): Return 1 if the callback handled the multi attribute, Return 0 if Maya should provide its default handling.


AEnewAttributeHandler

This hook is called to give plugins a chance to provide a UI creation handler for attributes.


nodeName (string): the name of the node for which the AE is being constructed. 
atributeName (string): the name of the attribute.
uiName (string): the UI name of the attribute.
changedCommand (string): the MEL command or procedure to be executed when the value of the attribute is changed.
returns (string): if the callback handled the attribute then it should return the full name of the topmost UI element that it created, otherwise it should return an empty string.


AEreplaceAttributeHandler

This hook is called to give plugins a chance to provide an update handler for attributes.


nodeName (string): the name of the node for which the AE is being constructed. 
atributeName (string): the name of the attribute.
changedCommand (string): the MEL command or procedure to be executed when the value of the attribute is changed.
returns (int): Return 1 if the callback handled the attribute, Return 0 if Maya should provide its default handling.


provideClassificationStrings

This hook must be supplied by all third parties that add nodes to the 'shader/surface' classification namespace.


returns (string): a colon separated list representing the different plugin node classifications.


provideClassificationExclusionStrings

This hook is called to give plugins a chance to provide a list of classifications which should be filtered out from a nodeTreeLister category. For example a plugin might want to filter out nodes classified as both 'material' and 'legacy' out of the 'material' category.


classification (string): the classification the nodeTreeBuilder is inquiring about.
returns (string): a colon separated list representing the different classifications that should be excluded from the classification the nodeTreeBuilder is inquiring about.


provideClassificationStringsForFilteredTreeLister

This hook is called by 'createAssignNewMaterialTreeLister' and gives plugins a chance to append to the classification filter passed to the Tree Lister builder. It must return a string where each new classification is separated by a white space.


currentFilterString (string): a white-space-separated string representing the current classifications.


nodeCanBeUsedAsMaterial

The hook is used by the RMB 'Assign Favorite Material' menu to determine which shading nodes can be used as materials. It must return 1 if the node can be used as a material node and 0 otherwise.


nodeId (string): the node Id of the shading node being queried.
nodeOwner (string): the name of the plugin the node belongs to.


addHeaderContentToMayaLambertianShadersAE

This hook is called to give plugins a chance to add content to the header of the Attribute Editor of Maya's Lambertian-​derived shaders.


nodeName (string): the name of the node for which the Attribute Editor is being constructed.


provideNodeToAttrConnection

This hook is called to give plugins a chance to provide which output attribute should be used when a node is connected to an input attribute.
If an input attribute type is given an output attribute of matching type should be returned. If no attribute type is specified (empty string)
a preferred output attribute of any type can be returned. If no output attribute of matching type is available an empty string should be returned.


nodeType (string): the node type of the node queried.
attributeType (string): the data type of the input attribute.
returns (string): the name of the output attribute to use.


provideNodeToNodeConnection

This hook is called to give plugins a chance to provide which attributes should be connected when a node to node connection is made.
Both the source and destination attributes should be returned in a colon separated list, e.g. "src1:dst1:src2:dst2:src3:dst3"


srcType (string): the node type of the source node.
dstType (string): the node type of the destination node.
returns (string): A colon separated list of source and destination attribute names.


provideOutputAttributeNameForTextureNode

This hook is called to give plugins a chance to provide a different output attribute name for Texture nodes. If this hook isn't provided 'outColor' is used.


nodeName (string): the name of the texture node queried.
returns (string): the output attribute name of the Texture node.


addItemsToHypergraphNodePopupMenu

This hook is called to give plugins a chance to add items to the Hypergraph node popup menu.
Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the popup menu.


nodeName (string): the name of the node for which the Hypergraph node menu is being constructed.


addItemsToOutlinerNodePopupMenu

This hook is called to give plugins a chance to add items to the Outliner node popup menu.
Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the popup menu.


nodeName (string): the name of the node or Ufe path string for which the Outliner node menu is being constructed.


addItemsToRenderLayerEditorPopupMenu

This hook is called to give plugins a chance to add items to the Render Layer Editor popup menu.
Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the popup menu.


layerName (string): the name of the render layer for which the popup menu is being constructed.


preventMaterialDeletionFromCleanUpSceneCommand

This hook is called by the cleanUpScene command and gives the plugin a chance to communicate that a material node is still in use and shouldn't be deleted. The hook is called once per plug/connection pair of each shader instance.


shader (string): the name of the shader node being deleted.
plug (string): the name of the plug queried.
connection (string): the name of the connection queried.


connectNodeToNodeOverrideCallback

This hook is called to give plugins a chance to redefine the behavior of drag and drop.


srcNode (string): the name of the source node (the dragged node).
dstNode (string): the name of the destination node (the dropped-on node).
returns (int): Return 1 if Maya should perform the operation that would normally result from this connection. Return 0 to override and provide custom behavior.


prepareRenderChanged

This hook is called after an edit on a traversal set with the prepareRender command.


enableRenderPassMenuOfRenderView

This hook is called to give plugins a chance to tell Maya it should enable the render pass menu of the render view (under File->Load Render Pass). 'addRenderPassMenuItemsToRenderView' can be used to add items to this menu.


returns (int): Return 1 if the plugin wants the render pass menu of the render view to be enabled. Return 0 otherwise.


addItemsToRenderPassMenuOfRenderView

This hook is called to give plugins a chance to add menu items to the 'render pass' menu of the render view (under File->Load Render Pass). 'enableRenderPassMenuOfRenderView' can be used to enable the render pass menu of the render view.


addItemsToRMBMenuOfTreeLister

This hook is called to give plugins a chance to populate the RMB menu of nodes listed in a tree lister. Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the RMB menu.


nodeType (string): The node type of the tree lister node for which the RMB menu is being built.
scriptCommand (string): The script command associated with the tree lister node for which the RMB menu is being built.
returns (int): Return 0 if Maya should append its own items to the menu of the current node type. This should be the return value for all node types a plugin isn't explicitly interested in. Return 1 if Maya shouldn't add any of its items to the menu of the current node type. Note: All menu items related to managing the 'Favorites' section of the tree lister will always be added to the RMB menu regardless of the return value (those are treated as special cases).


saveCustomNodePresetAttributes

This hook is called to give plugins a chance to store extra commands in the node preset file being saved.


presetNodeToSave (string): The name of the preset node being saved.
returns (string): The custom procedure to use to generate the mel script to be appended to the nodePreset -custom flag of the current presetNode save event (see the documentation of the nodePreset command for more information on the format of the -custom flag).


addItemToFileMenu

This hook is called to give plugins a chance to add menu items to the main File menu.


addItemToCreateLightMenu

This hook is called to give plugins a chance to add menu items to the create light menu.

textureReload

This hook is called to give plugins a chance to update all nodes that reference the texture file.


file (string): the file path of the texture to reload.


renderSettingsBuilt

This hook is called after the render settings window has been built.

rendererAddOneTabToGlobalsWindowCreateProc

This hook is called to allow renderers the opportunity to add renderer specific tabs to the unified render globals window (render settings window).


createProc (string): the name of the procedure used to create the content of the tab. 


shouldEarlyReturnFromUpdateMultiCameraBufferNamingMenu

This hook is called to allow users to early return from the updateMultiCameraBufferNamingMenu() function by returning "true" in the callback handler.


returns (string): Returns "true" if the caller wishes to early return from the updateMultiCameraBufferNamingMenu() function.


shouldEarlyReturnFromUpdateMayaSoftwareImageFormatControl

This hook is called to allow users to early return from the updateMayaSoftwareImageFormatControl() function by returning "true" in the callback handler.


returns (string): Returns "true" if the caller wishes to early return from the updateMayaSoftwareImageFormatControl() function.


shouldEarlyReturnFromUpdateDefaultTraversalSetMenu

This hook is called to allow users to early return from the updateDefaultTraversalSetMenu() function by returning "true" in the callback handler.


returns (string): Returns "true" if the caller wishes to early return from the updateDefaultTraversalSetMenu() function.


shouldEarlyReturnFromShouldAppearInNodeCreateUI

This hook is called to allow users to early return from the shouldAppearInNodeCreateUI() function by returning "true" in the callback handler.


returns (string): Returns "true" if the caller wishes to early return from the shouldAppearInNodeCreateUI() function.


updateAE

This hook is called at the end of the updateAE() function.

---
dumpCallbacks(dc): boolean
    properties: create
    Gives a list of all the registered callbacks for all hooks and owners. Can be
useful for debugging.

---
executeCallbacks(ec): boolean
    properties: create
    Execute the callbacks for the specified hook, passing the extra arguments to
each callback when it is executed.  Returns an array (MEL) or list (Python)
containing the return values from each callback that was executed.
If a callback returns no value, the array will contain an empty string (MEL)
or None (Python).

---
hook(h): string
    properties: create
    The name of the hook for which the callback should be registered.

---
listCallbacks(lc): boolean
    properties: create
    Get the list of callbacks for the specified hook name. If the owner is
specified, only callbacks for the specified hook and owner will be listed.

---
owner(o): string
    properties: create
    The name of the owner registering the callback. This is typically a plugin name.

---
removeCallback(rc): script
    properties: create
    Remove an existing callback for the specified hook name. The owner must
also be specified when removing a callback.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/callbacks.html 
    """


def camera(flagaspectRatio: float, flagcameraScale: float, flagcenterOfInterest: linear, flagclippingPlanes: boolean, flagdepthOfField: boolean, flagdisplayFieldChart: boolean, flagdisplayFilmGate: boolean, flagdisplayFilmOrigin: boolean, flagdisplayFilmPivot: boolean, flagdisplayGateMask: boolean, flagdisplayResolution: boolean, flagdisplaySafeAction: boolean, flagdisplaySafeTitle: boolean, flagfStop: float, flagfarClipPlane: linear, flagfarFocusDistance: linear, flagfilmFit: string, flagfilmFitOffset: float, flagfilmRollOrder: string, flagfilmRollValue: angle, flagfilmTranslateH: float, flagfilmTranslateV: float, flagfocalLength: float, flagfocusDistance: linear, flaghomeCommand: string, flaghorizontalFieldOfView: angle, flaghorizontalFilmAperture: float, flaghorizontalFilmOffset: float, flaghorizontalPan: float, flaghorizontalRollPivot: float, flaghorizontalShake: float, flagjournalCommand: boolean, flaglensSqueezeRatio: float, flaglockTransform: boolean, flagmotionBlur: boolean, flagname: string, flagnearClipPlane: linear, flagnearFocusDistance: linear, flagorthographic: boolean, flagorthographicWidth: linear, flagoverscan: float, flagpanZoomEnabled: boolean, flagposition: tuple[linear, linear, linear], flagpostScale: float, flagpreScale: float, flagrenderPanZoom: boolean, flagrotation: tuple[angle, angle, angle], flagshakeEnabled: boolean, flagshakeOverscan: float, flagshakeOverscanEnabled: boolean, flagshutterAngle: angle, flagstartupCamera: boolean, flagstereoHorizontalImageTranslate: float, flagstereoHorizontalImageTranslateEnabled: boolean, flagverticalFieldOfView: angle, flagverticalFilmAperture: float, flagverticalFilmOffset: float, flagverticalLock: boolean, flagverticalPan: float, flagverticalRollPivot: float, flagverticalShake: float, flagworldCenterOfInterest: tuple[linear, linear, linear], flagworldUp: tuple[linear, linear, linear], flagzoom: float) -> list[string]:
    """Synopsis:
---
---
 camera(
[camera]
    , [aspectRatio=float], [cameraScale=float], [centerOfInterest=linear], [clippingPlanes=boolean], [depthOfField=boolean], [displayFieldChart=boolean], [displayFilmGate=boolean], [displayFilmOrigin=boolean], [displayFilmPivot=boolean], [displayGateMask=boolean], [displayResolution=boolean], [displaySafeAction=boolean], [displaySafeTitle=boolean], [fStop=float], [farClipPlane=linear], [farFocusDistance=linear], [filmFit=string], [filmFitOffset=float], [filmRollOrder=string], [filmRollValue=angle], [filmTranslateH=float], [filmTranslateV=float], [focalLength=float], [focusDistance=linear], [homeCommand=string], [horizontalFieldOfView=angle], [horizontalFilmAperture=float], [horizontalFilmOffset=float], [horizontalPan=float], [horizontalRollPivot=float], [horizontalShake=float], [journalCommand=boolean], [lensSqueezeRatio=float], [lockTransform=boolean], [motionBlur=boolean], [name=string], [nearClipPlane=linear], [nearFocusDistance=linear], [orthographic=boolean], [orthographicWidth=linear], [overscan=float], [panZoomEnabled=boolean], [position=[linear, linear, linear]], [postScale=float], [preScale=float], [renderPanZoom=boolean], [rotation=[angle, angle, angle]], [shakeEnabled=boolean], [shakeOverscan=float], [shakeOverscanEnabled=boolean], [shutterAngle=angle], [startupCamera=boolean], [stereoHorizontalImageTranslate=float], [stereoHorizontalImageTranslateEnabled=boolean], [verticalFieldOfView=angle], [verticalFilmAperture=float], [verticalFilmOffset=float], [verticalLock=boolean], [verticalPan=float], [verticalRollPivot=float], [verticalShake=float], [worldCenterOfInterest=[linear, linear, linear]], [worldUp=[linear, linear, linear]], [zoom=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

camera is undoable, queryable, and editable.

The resulting camera can be repositioned using the viewPlace
command. Many of the camera settings only affect the resulting
rendered image. E.g. the F/Stop, shutter speed, the film related
options, etc. Scaling the camera icon does not change any camera
properties.




Example:
---
import maya.cmds as cmds

Create a camera and get the shape name.
cameraName = cmds.camera()
cameraShape = cameraName[1]

Get the focal length of the camera.
focalLength = cmds.camera(cameraShape, q=True, fl=True)

Change the film fit type.
cmds.camera( cameraShape, e=True, ff='overscan' )

---
Return:
---


    list[string]: (transform name and shape name)

Flags:
---


---
aspectRatio(ar): float
    properties: create, query, edit
    The ratio of the film back width to the film back height.

---
cameraScale(cs): float
    properties: create, query, edit
    Scale the camera.

---
centerOfInterest(coi): linear
    properties: create, query, edit
    Set the linear distance from the camera's eye point to the
center of interest.

---
clippingPlanes(cp): boolean
    properties: create, query, edit
    Activate manual clipping planes.

---
depthOfField(dof): boolean
    properties: create, query, edit
    Determines whether a depth of field calculation is performed
to give varying focus depending on the distance of the
objects.

---
displayFieldChart(dfc): boolean
    properties: create, query, edit
    Activate display of the video field chart when looking through
the camera.

---
displayFilmGate(dfg): boolean
    properties: create, query, edit
    Activate display of the film gate icons when looking through
the camera.

---
displayFilmOrigin(dfo): boolean
    properties: create, query, edit
    Activate the display of the film origin guide when
looking through the camera.

---
displayFilmPivot(dfp): boolean
    properties: create, query, edit
    Activate display of the film pivot guide when looking
through the camera.

---
displayGateMask(dgm): boolean
    properties: create, query, edit
    Display the gate mask, file or resolution, as a shaded area
to the edge of the viewport.

---
displayResolution(dr): boolean
    properties: create, query, edit
    Activate display of the current rendering resolution (as
defined in the render globals) when looking through the
camera.

---
displaySafeAction(dsa): boolean
    properties: create, query, edit
    Activate display of the video Safe Action guide
when looking through the camera.

---
displaySafeTitle(dst): boolean
    properties: create, query, edit
    Activate display of the video Safe Title guide
when looking through the camera.

---
fStop(fs): float
    properties: create, query, edit
    A real lens normally contains a diaphragm or other stop which
blocks some of the light that would otherwise pass through
it. This stop is usually approximately round, and its diameter
as seen from the front of the lens is called the lens
diameter. The lens diameter is often described by its relation
to the focal length of the lens. A lens whose diameter is
one-eighth its local length is said to have an F-stop of
8. This is an optical property of the lens.

---
farClipPlane(fcp): linear
    properties: create, query, edit
    Specify the distance to the far clipping plane.

---
farFocusDistance(ffd): linear
    properties: create, query, edit
    Linear distance to the far focus plane.

---
filmFit(ff): string
    properties: create, query, edit
    This describes how the digital image (in pixels) relates to
the film back. Since the film back is defined in terms of real
numbers with some arbitrary film aspect, and the digital image
is defined in integer pixels with an equally arbitrary (and
different) resolution, relating the two can get
complicated. There are 4 choices: 

horizontal 
In this case the digital image is made to fit the film
back exactly in the horizontal direction. This then gives each
pixel a horizontal size = (film back width) / (horizontal
resolution). The pixel height is then = (pixel width) / (pixel
aspect ratio). Now that the pixel has a size, resolution gives
us a complete image. That image will match the film back
exactly in width. It will almost never match in height, either
being too tall or too short. By playing with the numbers you
can get it pretty close though.
vertical
This is the same idea as horizontal fit, only applied
vertically. Thus the digital image will match the film back
exactly in height, but miss in width.
fill
This is a convenience item. The system calculates both
horizontal and vertical fits and then applies the one that
makes the digital image larger than the film back.
overscan
Overscanning the film gate in the camera view allows us
to choreograph action outside of the frustum from within the
camera view without having to resort to a dolly or zoom. This
feature is also essential for animating image planes.

---
filmFitOffset(ffo): float
    properties: create, query, edit
    Since we know from the above that the digital image may not
match the film back exactly, we now have the question of how
to position one relative to the other. Thus fit
offset. Normally the centers are aligned. Fit offset lets you
move the smaller image within the larger one. Specify the
distance for film offset (inches).

---
filmRollOrder(fro): string
    properties: create, query, edit
    Specifies how the roll is applied with respect to the
pivot value.

Rotate-Translate
The film back is first rotated then translated by the
pivot point value.
Translate-Rotate
The film back is first translated then rotated by the
film roll value.

---
filmRollValue(frv): angle
    properties: create, query, edit
    This specifies that amount of rotation around the film back.
The roll value is specified in degrees. The rotation occurs around
the specified pivot point. This value is used to compute a film
roll matrix, which is a component of the post-projection matrix.

---
filmTranslateH(fth): float
    properties: create, query, edit
    The horizontal film translation. Values are normalized to
the viewing area.

---
filmTranslateV(ftv): float
    properties: create, query, edit
    The vertical film translation. Values are normalized to the
viewing area.

---
focalLength(fl): float
    properties: create, query, edit
    This is the distance along the lens axis between the lens and
the film plane when "focal distance" is infinitely large. This
is an optical property of the lens. This double precision
parameter is always specified in millimeters.

---
focusDistance(fd): linear
    properties: create, query, edit
    Set the focus at a certain distance in front of the camera.

---
homeCommand(hc): string
    properties: create, query, edit
    Specify the command to execute when "viewSet -home" is applied
to this camera. All occurances of "%camera" will be replaced
with the cameras name before viewSet runs the command.

---
horizontalFieldOfView(hfv): angle
    properties: create, query, edit
    This is the film back width as seen by the lens when focused
at infinity (ie., focal length away) measured as an
angle. Note that it has nothing to do with pixels or the
digital image or any aspects. Angle of view is a derived
field, that is, it is not used internally by Alias and can be
completely determined from other information. It is included
as a convenience for the user. Its derivation is aov = 2 *
atan( fbw / (2 * f) ) where "aov" is the angle of view, "fbw"
is the film back width and "f" is the focal length.

---
horizontalFilmAperture(hfa): float
    properties: create, query, edit
    The horizontal width of the camera's film plane. The camera's
film is located on the film plane. The extent of the film
which will be exposed to an image of the scene in front of the
lens is limited to a rectangular area described by the film
back. This double precision parameter is always specified in
inches.

---
horizontalFilmOffset(hfo): float
    properties: create, query, edit
    Horizontal offset from the center of the film back. Normally
the film back will be centered on the lens axis. However, this
need not be so. Film offset is the displacement of the center
of the film back from the lens axis, also measured in
inches. Note that offsetting the film back will distort the
image, but will not alter the focus. This double precision
parameter is always specified in inches.

---
horizontalPan(hpn): float
    properties: create, query, edit
    Horizontal 2D camera pan (inches)

---
horizontalRollPivot(hrp): float
    properties: create, query, edit
    The horizontal pivot point from the center of the film back.
The pivot point is used during rotation of the film back.  The pivot
is the point where the rotation occurs around. This double precision
parameter corresponds to the normalized viewport. This value is a
part of the post projection matrix.

---
horizontalShake(hs): float
    properties: create, query, edit
    Another horizontal offset from the center of the film back,
which can be used and stored on the camera in addition to the
horizonal film offset attribute.  This allows for film-based
camera shake internal to the camera.  This works in exactly the same
units and coordinates that the film offset attribute does.
The effect of this attribute is toggled by the shake enabled attribute.

---
journalCommand(jc): boolean
    properties: create, query, edit
    Journal interactive camera commands. Commands can be undone
when a camera is journaled.

---
lensSqueezeRatio(lsr): float
    properties: create, query, edit
    This is presently just an information field in the camera
editor is meant to convey the horizontal distortion of the
anamorphic lens normally used with some film formats. If it
were used, it would do something like pixel aspect. Remember
however that lens distortion (intentional or not) is slightly
different than the output hardware's quantization. The fact
that a "net" distortion parameter could be used for both may
or may not confuse the issue.

---
lockTransform(lt): boolean
    properties: create, query, edit
    Lock the camera. When a camera is locked, its transformation information,
that is, its Translate and Rotate properties cannot be adjusted, and the
center of interest point cannot be moved.
For orthographic cameras, Orthographic Width is also locked.
For camera groups, Aim and Up locator's translate is also locked.
For stereo cameras, the root camera is locked.

---
motionBlur(mb): boolean
    properties: create, query, edit
    Determines whether the camera's image is motion blured (as
opposed to an object's image). For example, if you want to
blur the camera movement when you are performing a flyby.

---
name(n): string
    properties: create, query, edit
    Name of the camera.

---
nearClipPlane(ncp): linear
    properties: create, query, edit
    Specify the distance to the NEAR clipping plane.

---
nearFocusDistance(nfd): linear
    properties: create, query, edit
    Linear distance to the near focus plane.

---
orthographic(o): boolean
    properties: create, query, edit
    Activate the orthographic camera.

---
orthographicWidth(ow): linear
    properties: create, query, edit
    Set the orthographic projection width.

---
overscan(ovr): float
    properties: create, query, edit
    Set the percent of overscan.

---
panZoomEnabled(pze): boolean
    properties: create, query, edit
    Toggle camera 2D pan and zoom

---
position(p): [linear, linear, linear]
    properties: create, query, edit
    Three linear values can be specified to translate the camera.

---
postScale(pts): float
    properties: create, query, edit
    The post-scale value.  This value multiplied against
the computed projection matrix. It is applied after the
the film roll.

---
preScale(prs): float
    properties: create, query, edit
    The pre-scale value. The value is multiplied against
the computed projection matrix. It is applied before the film
roll.

---
renderPanZoom(rpz): boolean
    properties: create, query, edit
    Toggle camera 2D pan and zoom in render

---
rotation(rot): [angle, angle, angle]
    properties: create, query, edit
    Three angular values can be specified to rotate the camera.

---
shakeEnabled(se): boolean
    properties: create, query, edit
    Toggles the effect of the horizontal and vertical shake
attributes.

---
shakeOverscan(so): float
    properties: create, query, edit
    Controls the amount of overscan in the output rendered image.
For use when adding film-based camera shake.  Acts as a multiplier
to the film aperture on the camera.

---
shakeOverscanEnabled(soe): boolean
    properties: create, query, edit
    Toggles the effect of the shake overscan attribute.

---
shutterAngle(sa): angle
    properties: create, query, edit
    Specify the shutter angle (degrees).

---
startupCamera(sc): boolean
    properties: create, query, edit
    A startup camera is marked undeletable and implicit. This flag
can be used to set or query the startup state of a
camera. There must always be at least one startup camera.

---
stereoHorizontalImageTranslate(hit): float
    properties: create, query, edit
    A film-back offset for use in stereo camera rigs.

---
stereoHorizontalImageTranslateEnabled(she): boolean
    properties: create, query, edit
    Toggles the effect of the stereo HIT attribute.

---
verticalFieldOfView(vfv): angle
    properties: create, query, edit
    Set the vertical field of view.

---
verticalFilmAperture(vfa): float
    properties: create, query, edit
    The vertical height of the camera's film plane. This double
precision parameter is always specified in inches.

---
verticalFilmOffset(vfo): float
    properties: create, query, edit
    Vertical offset from the center of the film back. This double
precision parameter is always specified in inches.

---
verticalLock(vl): boolean
    properties: create, query, edit
    Lock the size of the vertical film aperture.

---
verticalPan(vpn): float
    properties: create, query, edit
    Vertical 2D camera pan (inches)

---
verticalRollPivot(vrp): float
    properties: create, query, edit
    Vertical pivot point used for rotating the film back. This
double precision parameter corresponds to the normalized viewport.
This value is used to compute the film roll matrix, which is a
component of the post projection matrix.

---
verticalShake(vs): float
    properties: create, query, edit
    Vertical offset from the center of the film back.  See horizontal
shake attribute description.  This is toggled by the shake enabled
attribute.

---
worldCenterOfInterest(wci): [linear, linear, linear]
    properties: create, query, edit
    Camera world center of interest point.

---
worldUp(wup): [linear, linear, linear]
    properties: create, query, edit
    Camera world up vector.

---
zoom(zom): float
    properties: create, query, edit
    The percent over the film viewable frustum to display

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/camera.html 
    """


def cameraSet(flagactive: boolean, flagappendTo: boolean, flagcamera: string, flagclearDepth: boolean, flagdeleteAll: boolean, flagdeleteLayer: boolean, flaginsertAt: boolean, flaglayer: int, flagname: string, flagnumLayers: boolean, flagobjectSet: string, flagorder: int) -> string:
    """Synopsis:
---
---
 cameraSet([active=boolean], [appendTo=boolean], [camera=string], [clearDepth=boolean], [deleteAll=boolean], [deleteLayer=boolean], [insertAt=boolean], [layer=int], [name=string], [numLayers=boolean], [objectSet=string], [order=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cameraSet is undoable, queryable, and editable.
For example, a set of stereo parameters may make the background
objects divergent beyond the tolerable range of the human perceptual
system. However, you like the settings because the main focus is in
the foreground and the depth is important to the visual look of the
scene.  You can use camera sets to break apart the shot into a
foreground stereo camera and background stereo camera. The foreground
stereo camera will retain the original parameters; however, it will
only focus on the foreground elements.  The background stereo camera
will have a different set of stereo parameters and will only draw the
background element.

Camera sets can be viewed using the stereo viewer and are currently only
designed to work with stereo camera rigs.




Example:
---
import maya.cmds as cmds

create some objects
cmds.sphere(n='sphere1')
cmds.cone(n='cone1')

create a set with whatever is currently active
cmds.select( 'sphere1', 'cone1')
newSet2 = cmds.sets()

cmds.loadPlugin( "stereoCamera", qt=True )
from maya.app.stereo import stereoCameraRig
rig = stereoCameraRig.createStereoCameraRig('StereoCamera')

Create a new cameraSet node.
cmds.cameraSet()

Add the cam & object set to the set
cmds.cameraSet( 'cameraSet1', edit=True, appendTo=True, cam=rig[0], objectSet=newSet2 )

---
Return:
---


    string: The new cameraSet node (when in create mode)

Flags:
---


---
active(a): boolean
    properties: create, query, edit
    Gets / sets the active camera layer.

---
appendTo(atl): boolean
    properties: create, edit
    Append a new camera and/or object set to then end of the cameraSet layer
list. This flag cannot be used in conjunction with insert flag. Additionally,
it requires the camera and/or objectSet flag to be used.

---
camera(cam): string
    properties: create, query, edit
    Set/get the camera for a particular layer. When in query mode, You
must specify the layer with the layer flag.

---
clearDepth(cd): boolean
    properties: create, query, edit
    Specifies if the drawing buffer should be cleared before beginning the draw
for that layer.

---
deleteAll(da): boolean
    properties: create, edit
    Delete all camera layers

---
deleteLayer(d): boolean
    properties: create, edit
    Delete a layer from the camera set. You must specify the layer using the
layer flag.

---
insertAt(ins): boolean
    properties: create, edit
    Inserts the specified camera and/or object set at the specified layer.
This flag cannot be used in conjunction with the append flag. Additionally,
this flag requires layer and camera (or objectSet) flag to be used.

---
layer(l): int
    properties: create, query, edit
    Specifies the layer index to be used when accessing layer information

---
name(n): string
    properties: create, query
    Gets or sets the name for the created camera set.

---
numLayers(nl): boolean
    properties: create, query
    Returns the number of layers defined in the specified cameraSet

---
objectSet(os): string
    properties: create, query, edit
    Set/get the objectSet for a particular layer. When in query mode, you must
specify the layer with the layer flag.

---
order(o): int
    properties: create, query, edit
    Set the order in which a particular layer is processed. This flag must be
used in conjunction with the layer flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cameraSet.html 
    """


def cameraView(flagaddBookmark: boolean, flaganimate: boolean, flagbookmarkType: int, flagcamera: name, flagname: string, flagremoveBookmark: boolean, flagsetCamera: boolean, flagsetView: boolean) -> string:
    """Synopsis:
---
---
 cameraView(
[object]
    , [addBookmark=boolean], [animate=boolean], [bookmarkType=int], [camera=name], [name=string], [removeBookmark=boolean], [setCamera=boolean], [setView=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cameraView is undoable, NOT queryable, and editable.

This command can be used for creation or edit of camera view
objects.  This command can only be executed with one of the add
bookmark, or remove bookmark and one of set camera, or the set
view flags set.




Example:
---
import maya.cmds as cmds

Save the current position of the persp camera.
homeName = cmds.cameraView(camera='persp')

Add this view to the persp bookmark menu.
cmds.cameraView( homeName, e=True, camera='persp', ab=True )

Change the persp camera position.
cmds.dolly( 'persp', distance=-30 )

Create another bookmark for the zoomed position.
cmds.cameraView( camera='persp', name='zoom', ab=True )

Restore original camera position.
cmds.cameraView( homeName, e=True, camera='persp', sc=True )

Save the current 2D pan/zoom attributes of the persp camera
panZoomBookmark = cmds.cameraView( camera='persp', ab=True, typ=1 )

Enable 2D pan/zoom
cmds.setAttr( 'perspShape.panZoomEnabled', True )

Pan right
cmds.panZoom( 'persp', r=0.6 )

Restore original film position
cmds.cameraView( panZoomBookmark, e=True, camera='persp', sc=True )

---
Return:
---


    string: (name of the camera view)

Flags:
---


---
addBookmark(ab): boolean
    properties: create, edit
    Associate this view with the camera specified or the camera in
the active model panel. This flag can be used for creation or
edit.

---
animate(an): boolean
    properties: create, edit
    Set the animation capability for view switches.

---
bookmarkType(typ): int
    properties: create
    Specify the bookmark type, which can be: 0. 3D bookmark; 1. 2D
Pan/Zoom bookmark.

---
camera(c): name
    properties: edit
    Specify the camera to use. This flag should be used in
conjunction with the add bookmark, remove bookmark, set
camera, or set view flags. If this flag is not specified the
camera in the active model panel will be used.

---
name(n): string
    properties: create
    Set the name of the view. This flag can only be used for
creation.

---
removeBookmark(rb): boolean
    properties: edit
    Remove the association of this view with the camera specified
or the camera in the active model panel. This can only be used
with edit.

---
setCamera(sc): boolean
    properties: edit
    Set this view into a camera specified by the camera flag or the
camera in the active model panel. This flag can only be used
with edit.

---
setView(sv): boolean
    properties: edit
    Set the camera view to match a camera specified or the active
model panel. This flag can only be used with edit.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cameraView.html 
    """


def canCreateCaddyManip() -> boolean:
    """Synopsis:
---
---
 canCreateCaddyManip(
object
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

canCreateCaddyManip is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

canWeCreateIt = cmds.canCreateCaddyManip('node')

---
Return:
---


    boolean: The queried value

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/canCreateCaddyManip.html 
    """


def canCreateManip() -> boolean:
    """Synopsis:
---
---
 canCreateManip(
object
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

canCreateManip is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

canWeCreateIt = cmds.canCreateManip('node')

---
Return:
---


    boolean: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/canCreateManip.html 
    """


def canvas(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghsvValue: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpressCommand: script, flagpreventOverride: boolean, flagrgbValue: tuple[float, float, float], flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 canvas(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [hsvValue=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [pressCommand=script], [preventOverride=boolean], [rgbValue=[float, float, float]], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

canvas is undoable, queryable, and editable.
Note: The -dgc/dragCallback and -dpc/dropCallback are not available
for this control.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( rowSpacing=5 )
cmds.canvas( rgbValue=(0, 0, 1), width=100, height=20 )
cmds.canvas( hsvValue=(60, 1, 1), width=100, height=20 )
cmds.canvas( rgbValue=(1, 0, 1), width=100, height=20 )
cmds.showWindow()

---
Return:
---


    string: The full name of the canvas.

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
hsvValue(hsv): [float, float, float]
    properties: create, query, edit
    Three float values corresponding to the hue, saturation, and
value color components, where the hue value ranges from 0.0 to 360.0
and the saturation and value components range from 0.0 to 1.0.

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
pressCommand(pc): script
    properties: create, edit
    Command to be executed when there is a mouse press.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
rgbValue(rgb): [float, float, float]
    properties: create, query, edit
    Three float values corresponding to the red, green, and blue
color components, all of which range from 0.0 to 1.0.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/canvas.html 
    """


def changeSubdivComponentDisplayLevel(flaglevel: int, flagrelative: boolean) -> int:
    """Synopsis:
---
---
 changeSubdivComponentDisplayLevel([level=int], [relative=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

changeSubdivComponentDisplayLevel is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

change the selected subdivision surface to display level 4 components
cmds.changeSubdivComponentDisplayLevel( l=4 )

increase the display level of the selected subivision surface by 1
cmds.changeSubdivComponentDisplayLevel( l=1, r=True )

---
Return:
---


    int: Command result

Flags:
---


---
level(l): int
    properties: create, query
    Specifies the display level of components.

---
relative(r): boolean
    properties: create, query
    If set, level refers to the relative display level

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/changeSubdivComponentDisplayLevel.html 
    """


def changeSubdivRegion(flagaction: int, flaglevel: int) -> boolean:
    """Synopsis:
---
---
 changeSubdivRegion([action=int], [level=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

changeSubdivRegion is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

delete the selection region on the base mesh
cmds.changeSubdivRegion( a=1, l=0 )

expand the selection region at the current level
cmds.changeSubdivRegion( a=2 )

---
Return:
---


    boolean: Command result

Flags:
---


---
action(a): int
    properties: create
    Specifies the action to the selection region
     1 = delete selection region
     2 = enlarge selection region

---
level(l): int
    properties: create
    Specify the level of the subdivision surface to perform the operation

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/changeSubdivRegion.html 
    """


def channelBox(flagannotation: string, flagattrBgColor: tuple[float, float, float], flagattrColor: tuple[float, float, float], flagattrFilter: string, flagattrRegex: string, flagattributeEditorMode: boolean, flagbackgroundColor: tuple[float, float, float], flagcontainerAtTop: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagenableLabelSelection: boolean, flagexecute: tuple[string, boolean], flagexists: boolean, flagfieldWidth: int, flagfixedAttrList: list[string], flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghistoryObjectList: boolean, flaghyperbolic: boolean, flaginputs: boolean, flagisObscured: boolean, flaglabelWidth: int, flaglongNames: boolean, flagmainListConnection: string, flagmainObjectList: boolean, flagmanage: boolean, flagmaxHeight: int, flagmaxWidth: int, flagniceNames: boolean, flagnoBackground: boolean, flagnodeRegex: string, flagnumberOfPopupMenus: boolean, flagoutputObjectList: boolean, flagoutputs: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagrebuildCommand: script, flagselect: string, flagselectedHistoryAttributes: boolean, flagselectedMainAttributes: boolean, flagselectedOutputAttributes: boolean, flagselectedShapeAttributes: boolean, flagshapeObjectList: boolean, flagshapes: boolean, flagshowNamespace: boolean, flagshowTransforms: boolean, flagspeed: float, flagstatusBarMessage: string, flagtakeFocus: boolean, flagufeFixedAttrList: tuple[string, list[string]], flagupdate: boolean, flaguseManips: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 channelBox(
[string]
    , [annotation=string], [attrBgColor=[float, float, float]], [attrColor=[float, float, float]], [attrFilter=string], [attrRegex=string], [attributeEditorMode=boolean], [backgroundColor=[float, float, float]], [containerAtTop=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enableLabelSelection=boolean], [execute=[string, boolean]], [exists=boolean], [fieldWidth=int], [fixedAttrList=string[]], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [historyObjectList=boolean], [hyperbolic=boolean], [inputs=boolean], [isObscured=boolean], [labelWidth=int], [longNames=boolean], [mainListConnection=string], [mainObjectList=boolean], [manage=boolean], [maxHeight=int], [maxWidth=int], [niceNames=boolean], [noBackground=boolean], [nodeRegex=string], [numberOfPopupMenus=boolean], [outputObjectList=boolean], [outputs=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rebuildCommand=script], [select=string], [selectedHistoryAttributes=boolean], [selectedMainAttributes=boolean], [selectedOutputAttributes=boolean], [selectedShapeAttributes=boolean], [shapeObjectList=boolean], [shapes=boolean], [showNamespace=boolean], [showTransforms=boolean], [speed=float], [statusBarMessage=string], [takeFocus=boolean], [ufeFixedAttrList=[string, string[]]], [update=boolean], [useManips=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

channelBox is undoable, queryable, and editable.
Note: when setting the color of attribute names, that color is only valid
for its current Maya session; each subsequent session will display the default
color for the attribute name(s) listed in the Channel Box. Any subsequent
attributes that are added to the Channel Box will be affected by prior
regular expressions in their current Maya session.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.formLayout( 'form' )
cmds.channelBox( 'dave' )
cmds.formLayout( 'form', e=True, af=(('dave', 'top', 0), ('dave', 'left', 0), ('dave', 'right', 0), ('dave', 'bottom', 0)) )
cmds.showWindow()

// Color all attributes names, which have an attribute name
// beginning with "T", white for all current and future objects
// in the current Maya session

cmds.channelBox( 'cb1', attrRegex='T*', attrColor=(1.0, 1.0, 1.0), attrBgColor=(0.0, 0.0, 0.0) )
cmds.channelBox( 'cb1', e=True, nodeRegex='D*', attrRegex='A*', attrColor=(0, 0, 0) )

---
Return:
---


    string: (the name of the new channel box)

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
attrBgColor(bc): [float, float, float]
    properties: create, query, edit
    Controls the background text color of specific attribute names. As with the foreground
option, this text coloring also depends on the node name choice for the nodeRegex flag.
Arguments correspond to the red, green, and blue color components.
Each component ranges in value from 0.0 to 1.0. If attrRegex is
unspecified then it will assume a value of "*" for a regular expression.
The same idea simultaneously applies to the flag nodeRegex.
Note: nodes that are renamed will have their node name coloring be affected
in the channel box.

---
attrColor(ac): [float, float, float]
    properties: create, query, edit
    Controls the foreground text color of specific attribute names. This
text coloring also depends on the node name choice for the nodeRegex flag.
Arguments correspond to the red, green, and blue color components.
Each component ranges in value from 0.0 to 1.0. If attrRegex is
unspecified then it will assume a value of "*" for a regular expression.
The same idea simultaneously applies to the flag nodeRegex.
Note: nodes that are renamed will have their node name coloring be affected
in the channel box.

---
attrFilter(af): string
    properties: query, edit
    Specifies the name of an itemFilter object to be placed on the channel box.
This filters the attributes displayed. A filter of "0" can be used to reset the
filter.

---
attrRegex(ar): string
    properties: create, query, edit
    Specifies a valid regular expression to specify which attribute names
should be selected for foreground text coloring. If attrRegex is
unspecified then it will assume a value of "*" for a regular expression.
The same idea simultaneously applies to the flag nodeRegex.
The attrColor flag is required to be specified.
Note: this regular expression will be treated as though it were case-insensitve

---
attributeEditorMode(aem): boolean
    properties: query, edit
    Modifies what appears in the channel box for use in the
attribute editor. Default is false. Queried, returns a boolean.

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
containerAtTop(cat): boolean
    properties: query, edit
    This flag can be used to specify whether or not the container is drawn at the
top of the channel box when a node in the container is selected.

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
enableLabelSelection(els): boolean
    properties: query, edit
    Enables the selection of attributes in the channelBox
when used in conjunction with -attributeEditorMode.
Default is false.  Queried, returns a boolean.

---
execute(exe): [string, boolean]
    properties: edit
    Immediately executes the command string once for every cell (or every
selected cell, if the boolean argument is TRUE) in the
channel box, for every matching selected object (ie, for every object would
be affected if you changed a cell value.)  Before the command is executed,
"#A" is substituted with the name of the attribute, and "#N" with the name
of the node, and "#P" with the full path name of the node.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fieldWidth(fw): int
    properties: query, edit
    An optional flag which is used to modify the width assigned
to fields appearing in the channelBox.

---
fixedAttrList(fal): string[]
    properties: create, query, edit
    Forces the channel box to only display attributes with the
specified names, in the order they are specified.  If an empty
list is specified, then the channel box will revert to its default
behaviour of listing all keyable attributes.

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
historyObjectList(hol): boolean
    properties: query
    Returns a list of strings, the names of every INPUT node associated with
an object on the main object list that is of the same type as the node
displayed in the INPUT section of the channel box.

---
hyperbolic(hyp): boolean
    properties: create, query, edit
    Determines whether or not the distance that the mouse has been dragged
should be interpreted as a linear or hyperbolic function.  The default
is set to hyperbolic being false.

---
inputs(inputs): boolean
    properties: query
    Returns the items shown under the 'INPUTS' heading in the channel box.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
labelWidth(lw): int
    properties: query, edit
    An optional flag which is used to modify the width assigned
to labels appearing in the channelBox.

---
longNames(ln): boolean
    properties: query, edit
    Controls whether long or short attribute names will be used
in the interface.  Note that this flag is ignored if the -niceNames
flag is set.  Default is short names. Queried, returns a boolean.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object which the
editor will use as its source of content.  The channel box will
only display the (last) item contained in the selectionConnection object.
If a NULL string ("") is specified, then the channel box will revert
to its default behaviour of working on the active list.

---
mainObjectList(mol): boolean
    properties: query
    Returns a list of strings, the names of every object on the active
list that is the same type as the object displayed in the top (main)
section of the channel box.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxHeight(mh): int
    properties: query, edit
    An optional flag which is used to limit the height of the
channelBox.

---
maxWidth(mw): int
    properties: query, edit
    An optional flag which is used to limit the width of the
channelBox.

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
nodeRegex(nr): string
    properties: create, query, edit
    Specifies a valid regular expression to specify which node names should
(potentially) have their attributes selected for foreground text coloring.
If nodeRegex is unspecified then it will assume a value of "*' for a
regular expression. The same idea simultaneously applies to the flag
attrRegex. The attrColor flag is required to be specified.
Note: this regular expression will be treated as though it were case-insensitve
Note: nodes in namespaces have regular expressions applied as though those
nodes weren't in namespaces

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
outputObjectList(ool): boolean
    properties: query
    Returns a list of strings, the names of every OUTPUT node associated
an object on the main object list that is of the same type as the node
displayed in the OUTPUT section of the channel box.

---
outputs(out): boolean
    properties: query
    Returns the items shown under the 'OUTPUTS' heading in the channel box.

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
rebuildCommand(rbc): script
    properties: create, query, edit
    Command that gets executed when the channel box is rebuilt, e.g. when a new
object is selected.

---
select(s): string
    properties: edit, multiuse
    Allows programmatic selection of items (nodes or plugs) in the channel box.
Selection is equivalent to clicking the item with the mouse; therefore
only items currently shown in the channel box can be selected this way.

---
selectedHistoryAttributes(sha): boolean
    properties: query
    Returns a list of strings, the names of all the selected attributes
in the INPUT section of the channel box.

---
selectedMainAttributes(sma): boolean
    properties: query
    Returns a list of strings, the names of all the selected attributes in the
top section of the channel box.

---
selectedOutputAttributes(soa): boolean
    properties: query
    Returns a list of strings, the names of all the selected attributes
in the OUTPUT section of the channel box.

---
selectedShapeAttributes(ssa): boolean
    properties: query
    Returns a list of strings, the names of all the selected attributes
in the middle (shape) section of the channel box.

---
shapeObjectList(sol): boolean
    properties: query
    Returns a list of strings, the names of every shape associated with
an object on the main object list that is of the same type as the object
displayed in the middle (shape) section of the channel box.

---
shapes(shp): boolean
    properties: query
    Returns the items shown under the 'SHAPES' heading in the channel box.

---
showNamespace(sn): boolean
    properties: create, query, edit
    Controls whether or not the namespace of an object is displayed
if the object is not in the root namespace.

---
showTransforms(st): boolean
    properties: query, edit
    Controls whether this control will display transform attributes
only, or all other attributes. False by default. Queried, returns a
boolean.

---
speed(spd): float
    properties: create, query, edit
    Controls the speed at which the attributes are changed based on the
distance the mouse has been dragged.  Common settings for
slow/medium/fast are 0.1/1.0/10.0 respectively.  The default is 1.0.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
takeFocus(tf): boolean
    properties: edit
    causes the channel box to take over the keyboard focus, if it can.

---
ufeFixedAttrList(ual): [string, string[]]
    properties: create, query, edit
    Forces the channel box to only display attributes for the given
UFE runtime with the specified names, in the order they are specified.
The attribute list accepts wildcard ('?' for one char, '*' for many) and
will use pattern matching for finding attributes to display.
If an empty list is specified, then the channel box will display no
attributes for the given UFE runtime (since there is no keyable
attribute concept in UFE).
      In query mode, this flag can accept a value.

---
update(u): boolean
    properties: edit
    This flag can be used to force an update of the channel box display, for
example after changing a display preference.

---
useManips(mnp): string
    properties: create, query, edit
    When you click on a field or label in the channel box, the
tool switches to a manipulator that can change that value if you
drag in the 3d view.  This flag controls the kind of manips.  Allowed
values are "none" (self-explanatory), "invisible" (you won't see anything,
but dragging in the window will adjust any of the selected attributes),
and "standard" (the same as invisible, except for scale, rotate, and
translate, which will be represented by their usual manips.)

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/channelBox.html 
    """


def character(flagaddElement: name, flagaddOffsetObject: string, flaganyMember: name, flagcharacterPlug: boolean, flagclear: name, flagempty: boolean, flagexcludeDynamic: boolean, flagexcludeRotate: boolean, flagexcludeScale: boolean, flagexcludeTranslate: boolean, flagexcludeVisibility: boolean, flagflatten: name, flagforceElement: name, flaginclude: name, flagintersection: name, flagisIntersecting: name, flagisMember: name, flaglibrary: boolean, flagmemberIndex: uint, flagname: string, flagnoWarnings: boolean, flagnodesOnly: boolean, flagoffsetNode: boolean, flagremove: name, flagremoveOffsetObject: string, flagroot: string, flagscheduler: boolean, flagsplit: name, flagsubtract: name, flagtext: string, flagunion: name, flaguserAlias: name) -> boolean | list[string] | string:
    """Synopsis:
---
---
 character(
objects
    , [addElement=name], [addOffsetObject=string], [anyMember=name], [characterPlug=boolean], [clear=name], [empty=boolean], [excludeDynamic=boolean], [excludeRotate=boolean], [excludeScale=boolean], [excludeTranslate=boolean], [excludeVisibility=boolean], [flatten=name], [forceElement=name], [include=name], [intersection=name], [isIntersecting=name], [isMember=name], [library=boolean], [memberIndex=uint], [name=string], [noWarnings=boolean], [nodesOnly=boolean], [offsetNode=boolean], [remove=name], [removeOffsetObject=string], [root=string], [scheduler=boolean], [split=name], [subtract=name], [text=string], [union=name], [userAlias=name])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

character is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

create two characters with whatever is currently active
cmds.character()
cmds.character()

create a set which contains two sub characters
cmds.character( 'character1', 'character2', n='parentCharacter' )

Add the keyable attributes of ikHandle1 to a character
cmds.character( 'ikHandle1', add='character1' )

Remove the scale attributes for a transform from a character
cmds.character( 'sphere1.sx', 'sphere1.sy', 'sphere1.sz', remove='character1' )

Query the members of the character
members = cmds.character('character1', query=True)

Query the character plug for a specified member
cmds.character( members[0], q=True, cp=True )

Query the library and scheduler of the character
cmds.character( 'character1', q=True, library=True )
cmds.character( 'character2', q=True, sc=True )

Add the sphere as an offset object on the character
cmds.character( 'pSphere1', e=True, addOffsetObject = 'character1' )

---
Return:
---


    string: For creation operations (name of the character that was created or edited)
    list[string]: For query operation (names of items in the character)
    boolean: For isMember operation

Flags:
---


---
addElement(add): name
    properties: edit
    Adds the list of items to the given character.  If some of the
items cannot be added to the character because they are in another
character, the command will fail.  When another character is passed to
to -addElement, is is added as a sub character.  When a node is
passed in, it is expanded into its keyable attributes, which are
then added to the character.

---
addOffsetObject(aoo): string
    properties: query, edit
    Indicates that the selected character member objects should be used when
calculating and applying offsets. The flag argument is used to specify the
character.

---
anyMember(am): name
    properties: create
    An operation which tests whether any of the given items
are members of the given set.

---
characterPlug(cp): boolean
    properties: query
    Returns the plug on the character that corresponds to the
specified character member.

---
clear(cl): name
    properties: edit
    An operation which removes all items from the given character.

---
empty(em): boolean
    properties: create
    Indicates that the character to be created should be empty. (i.e.
it ignores any arguments identifying objects to be added to
the character.

---
excludeDynamic(ed): boolean
    properties: create
    When creating the character, exclude dynamic attributes.

---
excludeRotate(er): boolean
    properties: create
    When creating the character, exclude rotate attributes from
transform-type nodes.

---
excludeScale(es): boolean
    properties: create
    When creating the character, exclude scale attributes from
transform-type nodes.

---
excludeTranslate(et): boolean
    properties: create
    When creating the character, exclude translate attributes from
transform-type nodes. For example, if your character contains
joints only, perhaps you only want to include rotations in the
character.

---
excludeVisibility(ev): boolean
    properties: create
    When creating the character, exclude visibility attribute from
transform-type nodes.

---
flatten(fl): name
    properties: edit
    An operation that flattens the structure of the given character. That is,
any characters contained by the given character will be replaced by its
members so that the character no longer contains other characters but contains
the other characters' members.

---
forceElement(fe): name
    properties: edit
    For use in edit mode only. Forces addition of the items
to the character. If the items are in another character which
is in the character partition, the items will be removed
from the other character in order to keep the characters in the
character partition mutually exclusive with respect to membership.

---
include(include): name
    properties: edit
    Adds the list of items to the given character.  If some of the
items cannot be added to the character, a warning will be issued.
This is a less strict version of the -add/addElement operation.

---
intersection(int): name
    properties: query
    An operation that returns a list of items which are members of
all the character in the list.  In general, characters should be
mutually exclusive.

---
isIntersecting(ii): name
    properties: query
    An operation which tests whether or not the characters in the list have
common members.  In general, characters should be mutually exclusive, so
this should always return false.

---
isMember(im): name
    properties: query
    An operation which tests whether or not all the given items
are members of the given character.

---
library(lib): boolean
    properties: query
    Returns the clip library associated with this character, if there is one. A clip library will only exist if you have created clips on your character.

---
memberIndex(mi): uint
    properties: query
    Returns the memberIndex of the specified character member if used after the query flag. Or if used before the query flag, returns the member that corresponds to the specified index.

---
name(n): string
    properties: create
    Assigns string as the name for a new character. Valid for operations that
create a new character.

---
noWarnings(nw): boolean
    properties: create
    Indicates that warning messages should not be reported such
as when trying to add an invalid item to a character. (used by UI)

---
nodesOnly(no): boolean
    properties: query
    This flag modifies the results of character membership queries.
When listing the attributes (e.g. sphere1.tx) contained in the
character, list only the nodes.  Each node will only be listed
once, even if more than one attribute or component of the node
exists in the character.

---
offsetNode(ofs): boolean
    properties: query
    Returns the name of the characterOffset node used to add offsets to the root of the character.

---
remove(rm): name
    properties: edit
    Removes the list of items from the given character.

---
removeOffsetObject(roo): string
    properties: edit
    Indicates that the selected character offset objects should be removed
as offsets. The flag argument is used to specify the character.

---
root(rt): string
    properties: create
    Specifies the transform node which will act as the root of the character being created.
This creates a characterOffset node in addition to the character node, which can be used to add offsets
to the character to change the direction of the character's animtion without inserting additional nodes
in its hierarchy.

---
scheduler(sc): boolean
    properties: query
    Returns the scheduler associated with this character, if there is one. A scheduler will only exist if you have created clips on your character.

---
split(sp): name
    properties: create
    Produces a new set with the list of items and removes
each item in the list of items from the given set.

---
subtract(sub): name
    properties: query
    An operation between two characters which returns the members of the
first character that are not in the second character. In general,
characters should be mutually exclusive.

---
text(t): string
    properties: create, query, edit
    Defines an annotation string to be stored with the character.

---
union(un): name
    properties: query
    An operation that returns a list of all the members of all characters
listed.

---
userAlias(ua): name
    properties: query
    Returns the user defined alias for the given attribute on
the character or and empty string if there is not one.  Characters
automatically alias the attributes where character animation data
is stored.  A user alias will exist when the automatic aliases are
overridden using the aliasAttr command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/character.html 
    """


def characterMap(flagmapAttr: tuple[string, string], flagmapMethod: string, flagmapNode: tuple[string, string], flagmapping: string, flagproposedMapping: boolean, flagunmapAttr: tuple[string, string], flagunmapNode: tuple[string, string]) -> string:
    """Synopsis:
---
---
 characterMap([mapAttr=[string, string]], [mapMethod=string], [mapNode=[string, string]], [mapping=string], [proposedMapping=boolean], [unmapAttr=[string, string]], [unmapNode=[string, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

characterMap is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a mapping between character1 and character2, or if a map already
exists, update the mapping between any unmapped members.
---

cmds.characterMap( 'character1', 'character2' )

Query as to whether a mapping exists between two characters
---

cmds.characterMap( 'character1', 'character2', query=True )

Query which attributes are mapped between two characters
---

cmds.characterMap( 'character1', 'character2', query=True, mapAttr=True )

Delete the mapping between two pairs of attributes. If no mapping
exists between the attributes, nothing will happen.
---

cmds.characterMap( 'character1', 'character2', unmapAttr=('sphere1.tx','sphere2.tx') )

Add a mapping between two attributes.  Only attributes that
are members of characters can be mapped.
---

cmds.characterMap( 'character1', 'character2', mapAttr=('sphere1.tx','sphere2.tx') )

Query what attribute(s) are mapped to sphere1.tx between character1 and
character2
---

cmds.characterMap( 'character1', 'character2', mapping='sphere1.tx' )

---
Return:
---


    string: characterMap name

Flags:
---


---
mapAttr(ma): [string, string]
    properties: create, query, edit
    In query mode, this flag can be used to query the mapping stored by the specified map node. It returns an array of strings.
In non-query mode, this flag can be used to create a mapping between the specified character members. Any previous mapping on the attributes is removed in favor of the newly specified mapping.

---
mapMethod(mm): string
    properties: create
    This is is valid in create mode only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", and "byAttrOrder". "byAttrOrder" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence.

---
mapNode(mn): [string, string]
    properties: create, query
    This flag can be used to map all the attributes on the source node to their matching attributes on the destination node.

---
mapping(m): string
    properties: query
    This flag is valid in query mode only. It must be used before the query flag with a string argument. It is used for querying the mapping for a particular attribute.  A string array is returned.

---
proposedMapping(pm): boolean
    properties: query
    This flag is valid in query mode only. It is used to get an array of the mapping that the character map would prvide if called with the specified characters and the (optional) specified mappingMethod. If a character map exists on the characters, the map is not affected by the query operation.  A string array is returned.

---
unmapAttr(ua): [string, string]
    properties: create, edit
    This flag can be used to unmap the mapping stored by the specified map node.

---
unmapNode(umn): [string, string]
    properties: create
    This flag can be used to unmap all the attributes on the source node to their matching attributes on the destination node. Note that mapped attributes which do not have matching names, will not be unmapped.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/characterMap.html 
    """


def characterize(flagactivatePivot: boolean, flagaddAuxEffector: boolean, flagaddFloorContactPlane: boolean, flagaddMissingEffectors: boolean, flagattributeFromHIKProperty: string, flagattributeFromHIKPropertyMode: string, flagautoActivateBodyPart: boolean, flagchangePivotPlacement: boolean, flageffectors: string, flagfkSkeleton: string, flagname: string, flagpinHandFeet: boolean, flagplaceNewPivot: boolean, flagposture: string, flagsourceSkeleton: string, flagstancePose: string, flagtype: string) -> string:
    """Synopsis:
---
---
 characterize([activatePivot=boolean], [addAuxEffector=boolean], [addFloorContactPlane=boolean], [addMissingEffectors=boolean], [attributeFromHIKProperty=string], [attributeFromHIKPropertyMode=string], [autoActivateBodyPart=boolean], [changePivotPlacement=boolean], [effectors=string], [fkSkeleton=string], [name=string], [pinHandFeet=boolean], [placeNewPivot=boolean], [posture=string], [sourceSkeleton=string], [stancePose=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

characterize is undoable, queryable, and editable.
Note that a minimum set of required joint names or joint labels  must be
found in order for the characterize command to succeed. Please refer to the
Maya documentation for details on properly naming or labeling your skeleton.
The skeleton should also be z-facing, with its y-axis up, its
left hand parallel to positive x-axis and right hand parallel to
negative x-axis.
END_COMMENT




Example:
---
import maya.cmds as cmds

Characterize a skeleton.  Select the root of the skeleton and enter
the following. The skeleton joints must be named according to the
FBIK naming conventions described in the main Maya documentation.
---

cmds.characterize( pinHandFeet=True )

Characterize a skeleton that has not been named according to the
FBIK naming conventions by using the -sk flag to define the
purpose of the joints. Select the skeleton and enter the following.
---

cmds.characterize( sk = 'pelvis Hips,hipL LeftUpLeg,kneeL LeftLeg,footL LeftFoot,toeL LeftToeBase,hipR RightUpLeg,kneeR RightLeg,footR RightFoot,toeR RightToeBase,spine Spine,spine1 Spine1,collarL LeftShoulder,shoulderL LeftArm,elbowL LeftForeArm,handL LeftHand,collarR RightShoulder,shoulderR RightArm,elbowR RightForeArm,handR RightHand,neck Neck,head Head,spine2 Spine2' )

Add a floor contact plane to the selected effector
---

cmds.select('LeftFootEff', r=True)
cmds.characterize( e=True, addFloorContactPlane=True )

Add a full body pivot to the selected effector.
---

cmds.select('LeftHandEff', r=True)
cmds.characterize( e=True, placeNewPivot=True )
cmds.move( 1, 1, 0, r=True)

Activate a new pivot now that it has been placed in the desired location.
---

cmds.characterize( e=True, activatePivot=True )

De-activate a pivot so that it can be moved to another location.
---

cmds.characterize( e=True, changePivotPlacement=True )

---
Return:
---


    string: Names of full body IK effectors that were created.

Flags:
---


---
activatePivot(apv): boolean
    properties: edit
    Activates a pivot that has been properly placed.  After activating this new
pivot, you will now be able to rotate and translate about this pivot.
A pivot behaves in all ways the same as an effector (it IS an
effector, except that it is offset from the normal position of the effector
to allow one to rotate about a different point.

---
addAuxEffector(aae): boolean
    properties: edit
    Adds an auxilliary (secondary) effector to an existing effector.

---
addFloorContactPlane(afp): boolean
    properties: edit
    Adds a floor contact plane to one of the hands or feet.  With this plane,
you will be able to adjust the floor contact height.  Select a hand or foot
effector and then issue the characterize command with this flag.

---
addMissingEffectors(ame): boolean
    properties: edit
    This flag tells the
characterize command to look for any effectors that can be added to the
skeleton. For example, if the user has deleted some effectors or added fingers
to an existing skeleton, "characterize -e -addMissingEffectors" can be used to
restore them.

---
attributeFromHIKProperty(ahk): string
    properties: query
    Query for the attribute name associated with a MotionBuilder property.

---
attributeFromHIKPropertyMode(mhk): string
    properties: query
    Query for the attribute name associated with a MotionBuilder property mode.

---
autoActivateBodyPart(aab): boolean
    properties: query, edit
    Query or change whether auto activation of character nodes representing body parts
should be enabled.

---
changePivotPlacement(cpp): boolean
    properties: edit
    Reverts a pivot back into pivot placement mode.  A pivot that is in placement
mode will not participate in full body manipulation until it has been activated
with the -activatePivot flag.

---
effectors(ef): string
    properties: create
    Specify the effectors to be used by human IK by providing
2 pieces of information for each effector:  1) the partial path of the
effector and 2) the name of the full body effector this represents.  1) and
2) are to be separated by white space, and multiple entries separated by ",".
Normally, the effectors are automatically created.  This flag is
for advanced users only.

---
fkSkeleton(fk): string
    properties: create, edit
    Specify the fk skeleton to be used by human IK by providing 2 pieces of
information for each joint of the FK skeleton:  1) the partial path of the
joint and 2) the name of the full body joint this represents.  1) and 2) are
to be separated by white space, and multiple entries separated by ",".
Normally, the fk control skeleton is automatically created.  This
flag is for advanced users only.

---
name(nm): string
    properties: create
    At characterization (FBIK creation) time, use this flag to name your FBIK character.
This will affect the name of the hikHandle node and the control rig will be put
into a namespace that matches the name of your character.  If you do not specify
the character name, a default one will be used.
At the moment edit and query of the character name is not supported.

---
pinHandFeet(phf): boolean
    properties: create
    When the character is first being characterized, pin the hands and feet by default.

---
placeNewPivot(pnp): boolean
    properties: edit
    Creates a new pivot and puts it into placement mode.  Note that you will
not be able to do full body manipulation about this pivot until you have
activated it with the -activatePivot flag. A pivot behaves in all ways the
same as an effector (it IS an effector, except that it is offset from the
normal position of the effector to allow one to rotate about a different
point). A new pivot created with this flag allow you to adjust the offset
interactively before activating it.

---
posture(pos): string
    properties: create
    Specifies the posture of the character. Valid options are "biped" and
"quadruped". The default is "biped".

---
sourceSkeleton(sk): string
    properties: create, edit
    This flag can be used to characterize a skeleton that has not been named or
labelled according to the FBIK guidelines. It specifies the association
between the actual joint names and the expected FBIK joint names. The format
of the string is as follows: For each
joint that the user wants to involve in the solve:  1) the partial path of
the joint and 2) the name of the full body joint this represents.  1) and 2)
are to be separated by white space, and multiple entries separated by ",".

---
stancePose(sp): string
    properties: create, query
    Specify the default stance pose to be used by human IK.  The stance pose is
specified by providing 2 pieces of information for each joint involved in
the solve:
1) the partial path to the joint and 2) 9 numbers representing translation
rotation and scale.
1) and 2) are to be separated by white space, and multiple entries separated
by ",".
Normally, the stance pose is taken from the selected skeleton.  This flag is
for advanced users only.

---
type(typ): string
    properties: create
    Specifies the technique used by the characterization to identify the joint
type. Valid options are "label" and "name". When "label" is used, the joints
must be labelled using the guidelines described in the Maya documentation.
When name is used, the joint names must follow the naming conventions
described in the Maya documentation. The default is "name". This flag
cannot be used in conjunction with the sourceSkeleton flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/characterize.html 
    """


def checkBox(flagalign: string, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagoffCommand: script, flagonCommand: script, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrecomputeSize: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvalue: boolean, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 checkBox(
[string]
    , [align=string], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [recomputeSize=boolean], [statusBarMessage=string], [useTemplate=string], [value=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

checkBox is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

window = cmds.window('window', width=150)
cmds.columnLayout( adjustableColumn=True )
cmds.checkBox( label='One' )
cmds.checkBox( label='Two' )
cmds.checkBox( label='Three' )
cmds.checkBox( label='Four' )
cmds.showWindow( window )

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
The check box label will always be left-aligned.

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
    Command executed when the check box's state is changed.
Note that this flag should not be used in conjunction with
onCommand and offCommand. That is, one should either use
changeCommand and test the state of the check box from inside
the callback, or use onCommand and offCommand as separate
callbacks.

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
    The edit state of the check box.  By default, this flag is
set to true and the check box value may be changed by clicking on
it.  If false then the check box is 'read only' and can not be
clicked on. The value of the check box can always be changed with
the -v/value flag regardless of the state of
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
    The label text. The default label is the name of
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
    properties: create, query, edit
    Command executed when the check box is turned off.

---
onCommand(onc): script
    properties: create, query, edit
    Command executed when the check box is turned on.

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
value(v): boolean
    properties: create, query, edit
    State of the check box.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/checkBox.html 
    """


def checkBoxGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagchangeCommand1: script, flagchangeCommand2: script, flagchangeCommand3: script, flagchangeCommand4: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flageditable: boolean, flagenable: boolean, flagenable1: boolean, flagenable2: boolean, flagenable3: boolean, flagenable4: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flaglabel1: string, flaglabel2: string, flaglabel3: string, flaglabel4: string, flaglabelArray2: tuple[string, string], flaglabelArray3: tuple[string, string, string], flaglabelArray4: tuple[string, string, string, string], flagmanage: boolean, flagnoBackground: boolean, flagnumberOfCheckBoxes: int, flagnumberOfPopupMenus: boolean, flagoffCommand: script, flagoffCommand1: script, flagoffCommand2: script, flagoffCommand3: script, flagoffCommand4: script, flagonCommand: script, flagonCommand1: script, flagonCommand2: script, flagonCommand3: script, flagonCommand4: script, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flaguseTemplate: string, flagvalue1: boolean, flagvalue2: boolean, flagvalue3: boolean, flagvalue4: boolean, flagvalueArray2: tuple[boolean, boolean], flagvalueArray3: tuple[boolean, boolean, boolean], flagvalueArray4: tuple[boolean, boolean, boolean, boolean], flagvertical: boolean, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 checkBoxGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [changeCommand1=script], [changeCommand2=script], [changeCommand3=script], [changeCommand4=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean], [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [label1=string], [label2=string], [label3=string], [label4=string], [labelArray2=[string, string]], [labelArray3=[string, string, string]], [labelArray4=[string, string, string, string]], [manage=boolean], [noBackground=boolean], [numberOfCheckBoxes=int], [numberOfPopupMenus=boolean], [offCommand=script], [offCommand1=script], [offCommand2=script], [offCommand3=script], [offCommand4=script], [onCommand=script], [onCommand1=script], [onCommand2=script], [onCommand3=script], [onCommand4=script], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [useTemplate=string], [value1=boolean], [value2=boolean], [value3=boolean], [value4=boolean], [valueArray2=[boolean, boolean]], [valueArray3=[boolean, boolean, boolean]], [valueArray4=[boolean, boolean, boolean, boolean]], [vertical=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

checkBoxGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates from one to four check boxes in a single row.
They can have an optional text label.

TelfBaseGrpCmd.cpp




Example:
---
import maya.cmds as cmds

exampleWindow = cmds.window()
cmds.columnLayout()
cmds.checkBoxGrp( numberOfCheckBoxes=3, label='Three Buttons', labelArray3=['One', 'Two', 'Three'] )
cmds.checkBoxGrp( numberOfCheckBoxes=4, label='Four Buttons', labelArray4=['I', 'II', 'III', 'IV'] )
cmds.showWindow( exampleWindow )

Place a single checkbox with a label width of 100 pixels, and a checkbox
width of 165 pixels.  In this example, the two columns of the checkBoxGrp
controlled by the columnWidth2 flag are the label column and the checkbox
column.  Horizontal positioning of the checkbox can be controlled by
adjusting the width of the first column.
exampleWindow = cmds.window()
cmds.rowLayout()
cmds.checkBoxGrp(columnWidth2=[100, 165], numberOfCheckBoxes=1, label='A Label', label1='A Checkbox', v1=True)
cmds.showWindow(exampleWindow)

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
changeCommand and test the state of a check box from inside
the callback, or use onCommand and offCommand as separate
callbacks.

---
changeCommand4(cc4): script
    properties: create, edit
    Specify a changed state command for each respective check
box.

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
editable(ed): boolean
    properties: create, query, edit
    The edit state of the group.  By default, this flag
is set to true and the check box values may be changed by
clicking on them.  If false then the check boxes are 'read only'
and can not be clicked on. The value of the check boxes can
always be changed with the -v/value flags regardless of
the state of the -ed/editable flag.

---
enable(en): boolean
    properties: create, query, edit
    The enable state of the control.  By default, this flag is
set to true and the control is enabled.  Specify false and the control
will appear dimmed or greyed-out indicating it is disabled.

---
enable4(en4): boolean
    properties: create, query, edit
    Enable state of the individual check boxes.

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
built with the group.  The string specifes the label text.

---
label4(l4): string
    properties: create, query, edit
    Specify label strings for the respective check boxes in
the group.

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
numberOfCheckBoxes(ncb): int
    properties: create
    Number of check boxes in the group (1 - 4).

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
offCommand(ofc): script
    properties: create, edit
    Command executed when any check box turns off.

---
offCommand4(of4): script
    properties: create, edit
    Off command for each respective check box.

---
onCommand(onc): script
    properties: create, edit
    Command executed when any check box turns on.

---
onCommand4(on4): script
    properties: create, edit
    On command for each respective check box.

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
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value4(v4): boolean
    properties: create, query, edit
    Values for the respective check boxes in the group.

---
valueArray4(va4): [boolean, boolean, boolean, boolean]
    properties: create, query, edit
    Specifies multiple values in a single flag.  These flags
are ignored if the number of check boxes doesn't match.

---
vertical(vr): boolean
    properties: create, query
    Whether the orientation of the checkbox controls in this group
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/checkBoxGrp.html 
    """


def checkDefaultRenderGlobals() -> None:
    """Synopsis:
---
---
 checkDefaultRenderGlobals([string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

checkDefaultRenderGlobals is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.checkDefaultRenderGlobals(q=1) can be replaced with a call to the ls command
To check if the defaultRenderGlobals node is marked dirty or not, do this:
if( 'defaultRenderGlobals' in cmds.ls(modified=1) ):
        do something...
        pass

To mark the entire scene dirty.
cmds.file( modified=1 )

To mark the entire scene clean
cmds.file( modified=0 )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/checkDefaultRenderGlobals.html 
    """


def choice(flagattribute: string, flagcontrolPoints: boolean, flagindex: uint, flagname: string, flagselector: name, flagshape: boolean, flagsourceAttribute: name, flagtime: time) -> list[string]:
    """Synopsis:
---
---
 choice(
[objects]
    , [attribute=string], [controlPoints=boolean], [index=uint], [name=string], [selector=name], [shape=boolean], [sourceAttribute=name], [time=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

choice is undoable, queryable, and editable.

The choice command creates a choice node (if one does not already
exist) on all specified attributes of the selected objects.
If the attribute was already connected to something, that something
is now reconnected to the i'th index of the choice node's input (or
the next available input if the -in/index flag is not specified).
If a source attribute is specified, then that attribute is connected
to the choice node's i'th input instead.

The choice node operates by using the value of its selector attribute
to determine which of its input attributes to pass through to its output.
The input attributes can be of any type. For example, if the selector
attribute was connected by an animation curve with keyframes at
(1,1), (30,2) and (50,1), then that would mean that the choice node
would pass on the data from input[1] from time 1 to 30, and after time 50,
and the data from input[2] between times 30 and 50.

This command returns the names of the created or modified choice nodes,
and if a keyframe was added to the animation curve, it specifies the
index (or value on the animation curve).




Example:
---
import maya.cmds as cmds

This example animates an object airplane along a motion path
from frames 1 to 30, then continues with keyframe animation until
frame 50, then returns to the motion path at frame 50.
path = cmds.curve(d=3,p=[(-10, 0, 0),(-6, 0, 10),(-3, 0, -10),(10, 0, 0)],k=[0, 0, 0, 1, 1, 1])
cmds.polyPlane()
cmds.pathAnimation('pPlane1',c=path,stu=1,etu=100)

Set a choice node on the path animation, ensuring that the choice
selects path animation from 1 to 30, and then returns at 50.
cmds.choice( 'pPlane1', at='ty', t=[1,30,50] )

Start a new kind of choice at time 31
cmds.choice( 'pPlane1', at='ty', t=31 )

Create some keyframe animation between times 31 and 49
cmds.currentTime( 31 )
cmds.setKeyframe( 'pPlane1', at="ty" )
cmds.move( 1, 2, 3, r=True )
cmds.setKeyframe( 'pPlane1', at="ty", t=40 )
cmds.move( 4, 5, 6, r=True )
cmds.setKeyframe( 'pPlane1', at="ty", t=49 )

Note that the -at/attribute and -t/time flags are not
queryable in themselves, but they can be used to
modify the choice nodes to query.

What is the attribute that is connected to the pPlane1.ty choice node's
selector attribute?
cmds.choice( 'pPlane1', at='ty', query=True, sl=True)

Which indices will be evaluated for the choice node to pPlane1.ty
at the given times?
cmds.choice( 'pPlane1', at='ty', t=[1,30,50], query=True, index=True)

---
Return:
---


    list[string]: The newly created and/or modified choice nodes, with the attribute
for which a selector keyframe was created.For example: choice1.input[3] choice2.input[3]

Flags:
---


---
attribute(at): string
    properties: create, multiuse
    specifies the attributes onto which choice node(s) should
be created. The default is all keyable attributes of the given
objects. Note that although this flag is not queryable, it can
be used to qualify which attributes of the given objects to query.
      In query mode, this flag needs a value.

---
controlPoints(cp): boolean
    properties: create
    Explicitly specify whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.

---
index(index): uint
    properties: create, query
    specifies the multi-input index of the choice node to connect
the source attribute to. When queried, returns a list of integers
one per specified -t/time that indicates the multi-index of the
choice node to use at that time.

---
name(n): string
    properties: create, query
    the name to give to any newly created choice node(s).
When queried, returns a list of strings.

---
selector(sl): name
    properties: create, query
    specifies the attribute to be used as the choice node's
selector. The value of the selector at a given time
determines which of the choice node's multi-indices should
be used as the output of the choice node at that time.
This flag is only editable (it cannot be specified
at creation time).
When queried, returns a list of strings.

---
shape(s): boolean
    properties: create
    Consider all attributes of shapes below transforms as well,
except "controlPoints". Default: true

---
sourceAttribute(sa): name
    properties: create
    specifies the attribute to connect to the choice node
that will be selected at the given time(s) specified by -t/time.

---
time(t): time
    properties: create, multiuse
    specifies the time at which the choice should use the given
source attribute, or the currently connected attribute if
source attribute is not specified. The default is the curren time.
Note that although this flag is not queryable, it can be used
to qualify the times at which to query the other attributes.
      In query mode, this flag needs a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/choice.html 
    """


def circle(flagcaching: boolean, flagcenter: tuple[linear, linear, linear], flagcenterX: linear, flagcenterY: linear, flagcenterZ: linear, flagconstructionHistory: boolean, flagdegree: int, flagfirst: tuple[linear, linear, linear], flagfirstPointX: linear, flagfirstPointY: linear, flagfirstPointZ: linear, flagfixCenter: boolean, flagname: string, flagnodeState: int, flagnormal: tuple[linear, linear, linear], flagnormalX: linear, flagnormalY: linear, flagnormalZ: linear, flagobject: boolean, flagradius: linear, flagsections: int, flagsweep: angle, flagtolerance: linear, flaguseTolerance: boolean) -> list[string]:
    """Synopsis:
---
---
 circle([caching=boolean], [center=[linear, linear, linear]], [centerX=linear], [centerY=linear], [centerZ=linear], [constructionHistory=boolean], [degree=int], [first=[linear, linear, linear]], [firstPointX=linear], [firstPointY=linear], [firstPointZ=linear], [fixCenter=boolean], [name=string], [nodeState=int], [normal=[linear, linear, linear]], [normalX=linear], [normalY=linear], [normalZ=linear], [object=boolean], [radius=linear], [sections=int], [sweep=angle], [tolerance=linear], [useTolerance=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

circle is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

create full circle at origin on the x-y plane
cmds.circle( nr=(0, 0, 1), c=(0, 0, 0) )

create half circle at origin on the x-y plane with radius 2
cmds.circle( nr=(0, 0, 1), c=(0, 0, 0), sw=180, r=2 )

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
    The center point of the circle.

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
3 - cubic
Default: 3

---
first(fp): [linear, linear, linear]
    properties: create, query, edit
    The start point of the circle if fixCenter is false.
Determines the orientation of the circle if fixCenter is true.

---
firstPointX(fpx): linear
    properties: create, query, edit
    X of the first point.
Default: 1

---
firstPointY(fpy): linear
    properties: create, query, edit
    Y of the first point.
Default: 0

---
firstPointZ(fpz): linear
    properties: create, query, edit
    Z of the first point.
Default: 0

---
fixCenter(fc): boolean
    properties: create, query, edit
    Fix the center of the circle to the specified center point.
Otherwise the circle will start at the specified first point.
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
normal(nr): [linear, linear, linear]
    properties: create, query, edit
    The normal of the plane in which the circle will lie.

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
radius(r): linear
    properties: create, query, edit
    The radius of the circle.
Default: 1.0

---
sections(s): int
    properties: create, query, edit
    The number of sections determines the resolution of the circle.
Used only if useTolerance is false.
Default: 8

---
sweep(sw): angle
    properties: create, query, edit
    The sweep angle determines the completeness of the circle.
A full circle is 2Pi radians, or 360 degrees.
Default: 6.2831853

---
tolerance(tol): linear
    properties: create, query, edit
    The tolerance with which to build a circle.
Used only if useTolerance is true
Default: 0.01

---
useTolerance(ut): boolean
    properties: create, query, edit
    Use the specified tolerance to determine resolution.
Otherwise number of sections will be used.
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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/circle.html 
    """


def circularFillet(flagcaching: boolean, flagconstructionHistory: boolean, flagcurveOnSurface: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagpositionTolerance: float, flagprimaryRadius: linear, flagsecondaryRadius: linear, flagtangentTolerance: float) -> list[string]:
    """Synopsis:
---
---
 circularFillet(
[surface] [surface]
    , [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [name=string], [nodeState=int], [object=boolean], [positionTolerance=float], [primaryRadius=linear], [secondaryRadius=linear], [tangentTolerance=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

circularFillet is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.circularFillet( 'surface1', 'surface2', ch=True, pr=-1.0, sr=1.0, cos=False )
cmds.circularFillet( 'surface3', 'surface4', ch=False, pr=-1.0, sr=2.0, cos=True, pt=0.001 )

---
Return:
---


    list[string]: Object name, node name.

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
positionTolerance(pt): float
    properties: create, query, edit
    C(0) Tolerance For Fillet Surface
Default: 0.01

---
primaryRadius(pr): linear
    properties: create, query, edit
    primary Radius
Default: 1.0

---
secondaryRadius(sr): linear
    properties: create, query, edit
    secondary Radius
Default: 1.0

---
tangentTolerance(tt): float
    properties: create, query, edit
    G(1) Tolerance For Fillet Surface
Default: 0.01

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/circularFillet.html 
    """


def clearCache(flagallNodes: boolean, flagcomputed: boolean, flagdirty: boolean) -> int:
    """Synopsis:
---
---
 clearCache([allNodes=boolean], [computed=boolean], [dirty=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

clearCache is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


Clear one node's datablock cache
cmds.clearCache( 'node' )

Clear caches in all dependency graph nodes
cmds.clearCache( all=True )

---
Return:
---


    int: Number of items removed from caches

Flags:
---


---
allNodes(all): boolean
    properties: create
    If toggled then all nodes in the graph are cleared.  Otherwise only those
nodes that are selected are cleared.

---
computed(c): boolean
    properties: create
    If toggled then remove all data that is computable.  (Warning: If the data
is requested for redraw then the recompute will immediately fill the data
back in.)

---
dirty(d): boolean
    properties: create
    If toggled then remove all heavy data that is dirty.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/clearCache.html 
    """


def clip(flagabsolute: boolean, flagabsoluteRotations: boolean, flagactive: string, flagaddTrack: boolean, flagallAbsolute: boolean, flagallClips: boolean, flagallRelative: boolean, flagallSourceClips: boolean, flaganimCurveRange: boolean, flagcharacter: boolean, flagconstraint: boolean, flagcopy: boolean, flagdefaultAbsolute: boolean, flagduplicate: boolean, flagendTime: time, flagexpression: boolean, flagignoreSubcharacters: boolean, flagisolate: boolean, flagleaveOriginal: boolean, flagmapMethod: string, flagname: string, flagnewName: string, flagpaste: boolean, flagpasteInstance: boolean, flagremove: boolean, flagremoveTrack: boolean, flagrotationOffset: tuple[float, float, float], flagrotationsAbsolute: boolean, flagscheduleClip: boolean, flagsourceClipName: boolean, flagsplit: time, flagstartTime: time, flagtranslationOffset: tuple[float, float, float], flaguseChannel: string) -> list[string]:
    """Synopsis:
---
---
 clip([absolute=boolean], [absoluteRotations=boolean], [active=string], [addTrack=boolean], [allAbsolute=boolean], [allClips=boolean], [allRelative=boolean], [allSourceClips=boolean], [animCurveRange=boolean], [character=boolean], [constraint=boolean], [copy=boolean], [defaultAbsolute=boolean], [duplicate=boolean], [endTime=time], [expression=boolean], [ignoreSubcharacters=boolean], [isolate=boolean], [leaveOriginal=boolean], [mapMethod=string], [name=string], [newName=string], [paste=boolean], [pasteInstance=boolean], [remove=boolean], [removeTrack=boolean], [rotationOffset=[float, float, float]], [rotationsAbsolute=boolean], [scheduleClip=boolean], [sourceClipName=boolean], [split=time], [startTime=time], [translationOffset=[float, float, float]], [useChannel=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

clip is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

First, create a character to hold the clips. The character will be
a 3-bone skeleton named "arm".
---

cmds.select( d=True )
cmds.joint( p=(0, 0, 0) )
cmds.joint( p=(0, 4, 0)  )
cmds.joint( 'joint1', e=True, zso=True, oj='xyz' )
cmds.joint( p=(0, 8, -1) )
cmds.joint( 'joint2', e=True, zso=True, oj='xyz' )
cmds.joint( p=(0, 9, -2) )
cmds.joint( 'joint3', e=True, zso=True, oj='xyz' )
cmds.select( 'joint1', 'joint2', 'joint3', r=True )
cmds.character( name='arm' )

Create some animation for the character. For this example the animation will
be quite trivial.
---

cmds.select( 'joint3', r=True )
cmds.currentTime( 0 )
cmds.setKeyframe( 'joint3.rx' )
cmds.currentTime( 10 )
cmds.setKeyframe( 'joint3.rx', v=90 )
cmds.currentTime( 20 )
cmds.setKeyframe( 'joint3.rx', v=0 )

Create a clip for the current animation named "handWave"
---

cmds.clip( 'arm', startTime=0, endTime=20, name='handWave' )

Create a 2nd animation for the character.
---

cmds.select( 'joint2', r=True )
cmds.currentTime( 0 )
cmds.setKeyframe( 'joint2.rx' )
cmds.setKeyframe( 'joint2.ry', v=20 )
cmds.currentTime( 10 )
cmds.setKeyframe( 'joint2.rx', v=45 )
cmds.setKeyframe( 'joint2.ry', v=-20 )
cmds.currentTime( 20 )
cmds.setKeyframe( 'joint2.rx', v=0 )
cmds.setKeyframe( 'joint2.ry', v=20 )

Create a clip for the current animation named "elbowWave"
---

cmds.clip( 'arm', startTime=0, endTime=20, name='elbowWave' )

Query the existing source clips
---

cmds.clip( 'arm', query=True, n=True )
Result:[u'handWaveSource', u'elbowWaveSource'] ---


Query the active clip. Note that the default clip is always active unless
another clip has been specified as active. This means that new keyframes
always go into the default clip unless you make another clip active.
---

cmds.clip( 'arm', query=True, active=True )
Result: default ---


Duplicate the clip named "elbowWaveSource" on the character named "arm" and
place the duplicate in the schedule at a start time of 50
---

cmds.clip( 'arm', duplicate=True, name='elbowWaveSource', s=50 )

Duplicate the clip named "wiggle" on the character named "arm" and
do not place the duplicate in the schedule
---

cmds.clip( 'arm', duplicate=True, sc=False, name='wiggle' )

Remove the clip from the character altogether. All instances of the clip will be
removed from the schedule and deleted from the library.
---

cmds.clip( 'arm', rm=True, name='elbowWaveSource')

Make the handWave clip active. This means that any new keyframes get
placed in the handWave clip, and modifications to existing handWave
keyframes can be made.
---

cmds.clip( 'arm', edit=True, active='handWave' )

Split the clip named "handWave" into two clips at time 10
---

cmds.clip( 'arm', split=10, name='handWave' )

Query the startTime of a clip. This is the start frame of the animation
curve range of the clip, and may differ from the scheduled time of the clip,
which is accessed using the clipSchedule command.
---

cmds.clip( 'arm', name='handWave', query=True, s=True )

---
Return:
---


    list[string]: clip names

Flags:
---


---
absolute(abs): boolean
    properties: create
    This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead.  This flag controls whether the clip follows its keyframe values or whether they are offset by a value to maintain a smooth path. Default is true.

---
absoluteRotations(abr): boolean
    properties: create
    This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead. If true, this overrides the -absolute flag so that rotation channels are always calculated with absolute offsets. This allows you to have absolute offsets on rotations and relative offsets on all other channels.

---
active(a): string
    properties: query, edit
    Query or edit the active clip. This flag is not valid in create mode. Making a
clip active causes its animCurves to be hooked directly to the character attributes in addition to being attached to the clip library node. This makes it easier to access the animCurves if you want to edit, delete or add additional animCruves to the clip.

---
addTrack(at): boolean
    properties: 
    This flag is now obsolete. Use the insertTrack flag on the clipSchedule command instead.

---
allAbsolute(aa): boolean
    properties: create
    Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.

---
allClips(ac): boolean
    properties: query
    This flag is used to query all the clips in the scene. Nodes of type "animClip" that are storing poses, are not returned by this command.

---
allRelative(ar): boolean
    properties: create
    Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.

---
allSourceClips(asc): boolean
    properties: query
    This flag is used to query all the source clips in the scene. Nodes of type "animClip" that are storing poses or clip instances, are not returned by this command.

---
animCurveRange(acr): boolean
    properties: create
    This flag can be used at the time you create the clip instead of the startTime and endTime flags. It specifies that you want the range of the clip to span the range of keys in the clips associated animCurves.

---
character(ch): boolean
    properties: query
    This is a query only flag which operates on the specified clip. It returns the names of any characters that a clip is associated with.

---
constraint(cn): boolean
    properties: create
    This creates a clip out of any constraints on the character. The constraint will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.

---
copy(c): boolean
    properties: create, query
    This flag is used to copy a clip or clips to the clipboard. It should be used in conjunction with the name flag to copy the named clips on the specified character and its subcharacters. In query mode, this flag allows you to query what, if anything, has been copied into the clip clipboard.

---
defaultAbsolute(da): boolean
    properties: create
    Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.

---
duplicate(d): boolean
    properties: query
    Duplicate the clip specified by the name flag. The start time of the new clip should be specified with the startTime flag.

---
endTime(end): time
    properties: create, query, edit
    Specify the clip end

---
expression(ex): boolean
    properties: create
    This creates a clip out of any expressions on the character. The expression will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.

---
ignoreSubcharacters(ignoreSubcharacters): boolean
    properties: create
    During clip creation, duplication and isolation, subcharacters are included by default. If you want to create a clip on the top level character only, or you want to duplicate the clip on the top level character without including subCharacters, use the ignoreSubcharacters flag.

---
isolate(i): boolean
    properties: create
    This flag should be used in conjunction with the name flag to specify that a clip or clips should be copied to a new clip library. The most common use of this flag is for export, when you want to only export certain clips from the character, without exporting all of the clips.

---
leaveOriginal(lo): boolean
    properties: create
    This flag is used when creating a clip to specify that the animation curves should be copied to the clip library, and left on the character.

---
mapMethod(mm): string
    properties: create
    This is is valid with the paste and pasteInstance flags only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", "byCharacterMap", "byAttrOrder", "byMapOrAttrName" and "byMapOrNodeName". "byAttrName" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence, "byCharacterMap" uses the existing characterMap node to do the mapping. "byMapOrAttrName" uses a character map if one exists, otherwise uses the attribute name. "byMapOrNodeName" uses a character map if one exists, otherwise uses the attribute name.

---
name(n): string
    properties: create, query, multiuse
    In create mode, specify the clip name. In query mode, return a list of all the clips. In duplicate mode, specify the clip to be duplicated. In copy mode, specify the clip to be copied. This flag is multi-use, but multiple use is only supported with the copy flag. For use during create and with all other flags, only the first instance of the name flag will be utilized.
                        In query mode, this flag can accept a value.

---
newName(nn): string
    properties: create
    Rename a clip. Must be used in conjunction with the clip name flag, which is used to specify the clip to be renamed.

---
paste(p): boolean
    properties: create
    This flag is used to paste a clip or clips from the clipboard to a character. Clips are added to the clipboard using the c/copy flag.

---
pasteInstance(pi): boolean
    properties: create
    This flag is used to paste an instance of a clip or clips from the clipboard to a character. Unlike the p/paste flag, which duplicates the animCurves from the original source clip, the pi/pasteInstance flag shares the animCurves from the source clip.

---
remove(rm): boolean
    properties: query
    Remove the clip specified by the name flag. The clip will be
permanently removed from the library and deleted from any times
where it has been scheduled.

---
removeTrack(rt): boolean
    properties: create
    This flag is now obsolete. Use removeTrack flag on the clipSchedule command instead.

---
rotationOffset(rof): [float, float, float]
    properties: create, query
    Return the channel offsets used to modify the clip's rotation.

---
rotationsAbsolute(ra): boolean
    properties: create
    Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.

---
scheduleClip(sc): boolean
    properties: create
    This flag is used when creating a clip to specify whether or not the clip should immediately be scheduled at the current time. If the clip is not scheduled, the clip will be placed in the library for future use, but will not be placed on the timeline. This flag is for use only when creating a new clip or duplicating an existing. The default is true.

---
sourceClipName(scn): boolean
    properties: query
    This flag is for query only. It returns the name of the source clip that controls an instanced clip.

---
split(sp): time
    properties: create, edit
    Split an existing clip into two clips. The split occurs around the specified time.

---
startTime(s): time
    properties: create, query, edit
    Specify the clip start

---
translationOffset(tof): [float, float, float]
    properties: create, query
    Return the channel offsets used to modify the clip's translation.

---
useChannel(uc): string
    properties: create, multiuse
    Specify which channels should be acted on. This flag is valid only in
conjunction with clip creation, and the isolate flag. The specified channels
must be members of the character.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/clip.html 
    """


def clipEditor(flagallTrackHeights: int, flagautoFit: string, flagautoFitTime: string, flagclipDropCmd: string, flagclipStyle: int, flagcontrol: boolean, flagdefineTemplate: string, flagdeleteCmd: string, flagdeselectAll: boolean, flagdisplayActiveKeyTangents: string, flagdisplayActiveKeys: string, flagdisplayInfinities: string, flagdisplayKeys: string, flagdisplayTangents: string, flagdisplayValues: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flagframeAll: boolean, flagframeRange: tuple[float, float], flaghighlightConnection: string, flaghighlightedBlend: tuple[string, string], flaghighlightedClip: tuple[string, string], flaginitialized: boolean, flaglistAllCharacters: boolean, flaglistCurrentCharacters: boolean, flaglockMainConnection: boolean, flaglookAt: string, flagmainListConnection: string, flagmanageSequencer: boolean, flagmenuContext: string, flagpanel: string, flagparent: string, flagselectBlend: tuple[string, string, string], flagselectClip: tuple[string, string], flagselectionConnection: string, flagsnapTime: string, flagsnapValue: string, flagstateString: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 clipEditor(
editorName
    , [allTrackHeights=int], [autoFit=string], [autoFitTime=string], [clipDropCmd=string], [clipStyle=int], [control=boolean], [defineTemplate=string], [deleteCmd=string], [deselectAll=boolean], [displayActiveKeyTangents=string], [displayActiveKeys=string], [displayInfinities=string], [displayKeys=string], [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [frameAll=boolean], [frameRange=[float, float]], [highlightConnection=string], [highlightedBlend=[string, string]], [highlightedClip=[string, string]], [initialized=boolean], [listAllCharacters=boolean], [listCurrentCharacters=boolean], [lockMainConnection=boolean], [lookAt=string], [mainListConnection=string], [manageSequencer=boolean], [menuContext=string], [panel=string], [parent=string], [selectBlend=[string, string, string]], [selectClip=[string, string]], [selectionConnection=string], [snapTime=string], [snapValue=string], [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

clipEditor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.clipEditor( "clipEditorName" )

---
Return:
---


    string: Editor name

Flags:
---


---
allTrackHeights(th): int
    properties: 
    OBSOLETE flag. Use clipStyle instead.

---
autoFit(af): string
    properties: query, edit
    on | off | tgl
Auto fit-to-view.

---
autoFitTime(aft): string
    properties: query, edit
    on | off | tgl
Auto fit-to-view along the time axis, as well.

---
clipDropCmd(cd): string
    properties: edit
    Command executed when clip node is dropped on the TraX editor

---
clipStyle(cs): int
    properties: query, edit
    Set/return the clip track style in the specified editor. Default is 2. Valid values are 1-3.

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
deleteCmd(dc): string
    properties: edit
    Command executed when backspace key is pressed

---
deselectAll(da): boolean
    properties: edit
    Deselect all clips and blends in the editor.

---
displayActiveKeyTangents(dat): string
    properties: edit
    on | off | tgl
Display active key tangents in the editor.

---
displayActiveKeys(dak): string
    properties: edit
    on | off | tgl
Display active keys in the editor.

---
displayInfinities(di): string
    properties: edit
    on | off | tgl
Display infinities in the editor.

---
displayKeys(dk): string
    properties: edit
    on | off | tgl
Display keyframes in the editor.

---
displayTangents(dtn): string
    properties: edit
    on | off | tgl
Display tangents in the editor.

---
displayValues(dv): string
    properties: edit
    on | off | tgl
Display active keys and tangents values in the editor.

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
frameAll(fa): boolean
    properties: edit
    Frame view around all clips in the editor.

---
frameRange(fr): [float, float]
    properties: query, edit
    The editor's current frame range.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
highlightedBlend(hb): [string, string]
    properties: query
    Returns the highlighted blend, listed as scheduler and index

---
highlightedClip(hc): [string, string]
    properties: query
    Returns the highlighted clip, listed as scheduler and index

---
initialized(it): boolean
    properties: query
    Returns whether the clip editor is fully initialized, and has a port to draw through.
If not, the -frameRange and -frameAll flags will fail.

---
listAllCharacters(lac): boolean
    properties: edit
    List all characters in the editor and outliner.

---
listCurrentCharacters(lc): boolean
    properties: edit
    List only the characters in the editor and outliner.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
lookAt(la): string
    properties: edit
    all | selected | currentTime
FitView helpers.

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
manageSequencer(ms): boolean
    properties: create, query, edit
    Sets/returns whether the clip editor should manage sequencer nodes.  If so,
animation clips and characters are not represented.

---
menuContext(mc): string
    properties: query
    Returns a string array denoting the type of data object the cursor
is over.  Returned values are:
{"timeSlider"}
{"nothing"}
{"track", "track index", "character node name", "group name"}
{"clip", "clip node name"}

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
selectBlend(sb): [string, string, string]
    properties: query, edit
    Select the blends specified by the scheduler name and the indicies
of the two clips used in the blend.
When queried, a string containing the scheduler name and the
two clip indicies for all of the selected blends is returned.

---
selectClip(sc): [string, string]
    properties: query, edit
    Selects the clip specified by the scheduler name and the clip index.
When queried, a string containing the scheduler and clip index
of all of the selected clips is returned.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
snapTime(st): string
    properties: query, edit
    none | integer | keyframe
Keyframe move snap in time.

---
snapValue(sv): string
    properties: query, edit
    none | integer | keyframe
Keyframe move snap in values.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/clipEditor.html 
    """


def clipEditorCurrentTimeCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 clipEditorCurrentTimeCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

clipEditorCurrentTimeCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.clipEditorCurrentTimeCtx()

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/clipEditorCurrentTimeCtx.html 
    """


def clipMatching(flagclipDst: tuple[string, float], flagclipSrc: tuple[string, float], flagmatchRotation: uint, flagmatchTranslation: uint) -> None:
    """Synopsis:
---
---
 clipMatching([clipDst=[string, float]], [clipSrc=[string, float]], [matchRotation=uint], [matchTranslation=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

clipMatching is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


Compute and set the offset on the "walk" clip in order to have it's start
pose align to the end of the "tornadoKick" clip at the LeftAnkle match
element.  Note that here we are matching the translation by specifying
with mt = 1.
---

cmds.select( 'character', 'LeftAnkle' )
cmds.clipMatching( mt=1, cs=("walk",0.0), cd=("tornadoKick",1.0) )

---


Flags:
---


---
clipDst(cd): [string, float]
    properties: create
    The clip to match so that the source clip can be offsetted correctly.  This flag
takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order
to have the source clip match at a certain time in the destination clip.

---
clipSrc(cs): [string, float]
    properties: create
    The clip to offset so that it aligns with the destination clip.  This flag takes
in a clip name and the percentage value ranging from 0.0 to 1.0 in order to
have it match at a certain time in the clip.

---
matchRotation(mr): uint
    properties: create
    This flag sets the rotation match type. By default, it is set to not match the
rotation.
0 - None
1 - Match full rotation
2 - Match projected rotation on ground plane

---
matchTranslation(mt): uint
    properties: create
    This flag sets the translation match type. By default, it is set to not match
the translation.
0 - None
1 - Match full translation
2 - Match projected translation on ground plane

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/clipMatching.html 
    """


def clipSchedule(flagallAbsolute: boolean, flagallRelative: boolean, flagblend: tuple[uint, uint], flagblendNode: tuple[uint, uint], flagblendUsingNode: string, flagcharacter: boolean, flagclipIndex: uint, flagcycle: float, flagdefaultAbsolute: boolean, flagenable: boolean, flaggroup: boolean, flaggroupIndex: uint, flaggroupName: string, flaghold: time, flaginsertTrack: uint, flaginstance: string, flaglistCurves: boolean, flaglistPairs: boolean, flaglock: boolean, flagmute: boolean, flagname: string, flagpostCycle: float, flagpreCycle: float, flagremove: boolean, flagremoveBlend: tuple[uint, uint], flagremoveEmptyTracks: boolean, flagremoveTrack: uint, flagrotationsAbsolute: boolean, flagscale: float, flagshift: int, flagshiftIndex: uint, flagsolo: boolean, flagsourceClipName: boolean, flagsourceEnd: time, flagsourceStart: time, flagstart: time, flagtrack: uint, flagweight: float, flagweightStyle: uint) -> string:
    """Synopsis:
---
---
 clipSchedule([allAbsolute=boolean], [allRelative=boolean], [blend=[uint, uint]], [blendNode=[uint, uint]], [blendUsingNode=string], [character=boolean], [clipIndex=uint], [cycle=float], [defaultAbsolute=boolean], [enable=boolean], [group=boolean], [groupIndex=uint], [groupName=string], [hold=time], [insertTrack=uint], [instance=string], [listCurves=boolean], [listPairs=boolean], [lock=boolean], [mute=boolean], [name=string], [postCycle=float], [preCycle=float], [remove=boolean], [removeBlend=[uint, uint]], [removeEmptyTracks=boolean], [removeTrack=uint], [rotationsAbsolute=boolean], [scale=float], [shift=int], [shiftIndex=uint], [solo=boolean], [sourceClipName=boolean], [sourceEnd=time], [sourceStart=time], [start=time], [track=uint], [weight=float], [weightStyle=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

clipSchedule is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

First, create a character to hold the clips. The character will be
a 3-bone skeleton named "arm".
---

cmds.select( d=True )
cmds.joint( p=(0, 0, 0) )
cmds.joint( p=(0, 4, 0)  )
cmds.joint( 'joint1', e=True, zso=True, oj='xyz' )
cmds.joint( p=(0, 8, -1) )
cmds.joint( 'joint2', e=True, zso=True, oj='xyz' )
cmds.joint( p=(0, 9, -2) )
cmds.joint( 'joint3', e=True, zso=True, oj='xyz' )
cmds.select( 'joint1', 'joint2', 'joint3', r=True )
cmds.character( name='arm' )

Create some animation for the character. For this example the animation will
be quite trivial.
---

cmds.select( 'joint3', r=True )
cmds.currentTime( 0 )
cmds.setKeyframe( 'joint3.rx' )
cmds.currentTime( 10 )
cmds.setKeyframe( 'joint3.rx', v=90 )
cmds.currentTime( 20 )
cmds.setKeyframe( 'joint3.rx', v=0 )

Create a clip for the current animation named "handWave"
---

cmds.clip( 'arm', startTime=0, endTime=20, name='handWave' )

Query the name of the clipScheduler for this character
---

cmds.character( 'arm', query=True, sc=True )
Result: armScheduler1

Create a 2nd animation for the character.
---

cmds.select( 'joint2', r=True )
cmds.currentTime( 0 )
cmds.setKeyframe( 'arm' )
cmds.currentTime( 10 )
cmds.setKeyframe( 'joint2.rx', v=45 )
cmds.setKeyframe( 'joint2.ry', v=-20 )
cmds.currentTime( 20 )
cmds.setKeyframe( 'joint2.rx', v=0 )
cmds.setKeyframe( 'joint2.ry', v=20 )

Create a clip for the current animation named "elbowWave"
---

cmds.clip( 'arm', startTime=0, endTime=20, name='elbowWave' )

Instance handeWave at time 10
---

cmds.clipSchedule( 'armScheduler1', instance='handWave', s=10 )

Query the clip index of the latest instance of handWave. Each instance
of a clip received a unique clipIndex. The clip index is used to
edit and query data for existing clips.
---

cmds.clipSchedule( 'armScheduler1', name='handWave1', query=True, ci=True )

Query whether the clip associated with index 2 is enabled or not
---

cmds.clipSchedule( 'armScheduler1', ci=2, query=True, enable=True )

Query the name of the clip associated with index 2
---

cmds.clipSchedule( 'armScheduler1', ci=2, query=True, n=True )

Query the weight of the clip associated with index 2
---

cmds.clipSchedule( 'armScheduler1', ci=2, query=True, weight=True )

Modify the elbowWave clip to start at frame 10 instead of frame 0
---

cmds.clipSchedule( 'armScheduler1', start=10, ci=1 )

Trim the start of the elbowWave clip to
use the animation starting at frame 5 instead 0
---

cmds.clipSchedule( 'armScheduler1', sourceStart=5, ci=1 )

Trim the end of the elbowWave clip to
use the animation up to frame 15 instead 20
---

cmds.clipSchedule( 'armScheduler1', sourceEnd=15, ci=1 )

Modify the handWave clip to have two cycles instead of 1
---

cmds.clipSchedule( 'armScheduler1', postCycle=1, ci=0 )

list the animation curves associated with a particular clip
---

cmds.clipSchedule( 'armScheduler1', ci=2, listCurves=True )

Move a particular clip to a particular track
---

cmds.clipSchedule( 'armScheduler1', track=2, ci=0 )

Add a blend between clips 1 and 2
---

cmds.clipSchedule( 'armScheduler1', b=(1, 2) )

Query the name of the blendNode between clips 1 and 2
---

cmds.clipSchedule( 'armScheduler1', q=True, bn=(1, 2) )

Lock the first track and then query its state
---

cmds.clipSchedule( 'armScheduler1', track=1, e=True, lock=1 )
cmds.clipSchedule( 'armScheduler1', track=1, query=True, lock=True )

Query the existing clips in the scheduler.
In query mode, returns an array of strings in this form:
(clipName,index,start,sourceStart,sourceEnd,scale,preCycle,postCycle,hold)
---

In this case there are three scheduled clips:
 2 instances of "handWave" and 1 of "elbowWave". The clip indices for "handWave" are 0
 and 3. The clip index for "elbowWave" is 2. Note that the clip indices can be sparse
 since a clip maintains its index as long as it is in the schedule (the TraX editor).
---

cmds.clipSchedule( 'armScheduler1', query=True )
Result: handWave,0,0.000000,0.000000,20.000000,1.000000,0.00000,2.00000 elbowWave,1,0.000000,5.000000,15.000000,1.000000,0.00000,1.00000 handWave,2,10.000000,0.000000,20.000000,1.000000,0.00000,1.00000
---


Shift clips 1 and 2 up 3 tracks
---

cmds.clipSchedule( 'armScheduler1', sh=-3, shi=1, shi=2 )

Print out which anim curves animate which channels for the
clip with an index of 2.
---

out = cmds.clipSchedule('armScheduler1' ,ci=2, query=True, lp=True)
for pair in out:
   print pair

---
Return:
---


    string: Clip name

Flags:
---


---
allAbsolute(aa): boolean
    properties: query, edit
    Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.

---
allRelative(ar): boolean
    properties: query, edit
    Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.

---
blend(b): [uint, uint]
    properties: create, query
    This flag is used to blend two clips, whose indices are provided as flag arguments.

---
blendNode(bn): [uint, uint]
    properties: query
    This query only flag list all of the blend nodes associated with the blend defined by the two clip indices. This flag returns a string array.
                        In query mode, this flag can accept a value.

---
blendUsingNode(bun): string
    properties: create
    This flag is used to blend using an existing blend node. It is used in conjunction with the blend flag. The blend flag specifies the clip indices for the blend. The name of an existing animBlend node should be supplied supplied as an argument for the blendUsingNode flag.

---
character(ch): boolean
    properties: query
    This flag is used to query which characters this scheduler controls. It returns an array of strings.

---
clipIndex(ci): uint
    properties: create, query
    Specify the index of the clip to schedule. In query mode, returns
an array of strings in this form:
(clipName,index,start,sourceStart,sourceEnd,scale,preCycle,postCycle)
                        In query mode, this flag can accept a value.

---
cycle(c): float
    properties: create, query
    This flag is now obsolete. Use the postCycle flag instead.

---
defaultAbsolute(da): boolean
    properties: query, edit
    Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.

---
enable(en): boolean
    properties: create, query
    This flag is used to enable or disable a clip. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be enabled or disabled.

---
group(grp): boolean
    properties: create
    This flag is used to add (true) or remove (false) a list of clips (specified with groupIndex) into a group.

---
groupIndex(gri): uint
    properties: create, multiuse
    This flag specifies a multiple number of clips to be added or removed from a group.

---
groupName(gn): string
    properties: create, query
    This flag is used to specify the group that should be added to.  If no group
by that name exists and new group is created with that name.  By default if
this is not specified a new group will be created.

---
hold(ph): time
    properties: create, query
    Specify how long to hold the last value of the clip after its normal or cycled end.

---
insertTrack(it): uint
    properties: create
    This flag is used to insert a new empty track at the track index
specified.

---
instance(instance): string
    properties: create
    Create an instanced copy of the named clip. An instanced clip is one that is linked to an original clip. Thus, changes to the animation curve of the original curve will also modify all instanced clips. The name of the instanced clip is returned
as a string.

---
listCurves(lc): boolean
    properties: create, query
    This flag is used to list the animation curves associated with a clip. It should be used in conjunction with the clipIndex flag, which specifies the clip of interest.

---
listPairs(lp): boolean
    properties: query
    This query only flag returns a string array containing the channels
in a character that are used by a clip and the names of the animation
curves that drive the channels. Each string in the string array consists
of the name of a channel, a space, and the name of the animation curve
animating that channel. This flag must be used with the ci/clipIndex flag.

---
lock(l): boolean
    properties: query, edit
    This flag specifies whether clips on a track are to be locked or not.
Must be used in conjuction with the track flag.

---
mute(m): boolean
    properties: query, edit
    This flag specifies whether clips on a track are to be muted or not.
Must be used in conjuction with the track flag.

---
name(n): string
    properties: create, query
    This flag is used to query the name of the clip node associated with the specified clip index, or to specify the name of the instanced clip during instancing.
                        In query mode, this flag can accept a value.

---
postCycle(poc): float
    properties: create, query
    Specify the number of times to repeat the clip after its normal end.

---
preCycle(prc): float
    properties: create, query
    Specify the number of times to repeat the clip before its normal start.

---
remove(rm): boolean
    properties: create
    This flag is used to remove a clip from the timeline. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be removed from the timeline, but will still exist in the library and any instanced clips will remain in the timeline. To permanently remove a clip from the scene, the clip command should be used instead.

---
removeBlend(rb): [uint, uint]
    properties: create
    This flag is used to remove an existing blend between two clips, whose indices are provided as flag arguments.

---
removeEmptyTracks(ret): boolean
    properties: create
    This flag is used to remove all tracks that have no clips.

---
removeTrack(rt): uint
    properties: create
    This flag is used to remove the track with the specified index.  The
track must have no clips on it before it can be removed.

---
rotationsAbsolute(ra): boolean
    properties: query, edit
    Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.

---
scale(sc): float
    properties: create, query
    Specify the amount to scale the clip. Values must be greater than 0.

---
shift(sh): int
    properties: create
    This flag allows multiple clips to be shifted by a certain number of tracks
and works in conjunction with the shiftIndex flag.  The flag specifies the
number of tracks to shift the associated clips.  Positive values shift the
clips down an negative values shift the clips up.

---
shiftIndex(shi): uint
    properties: create, multiuse
    This flag allows multiple clips to be shifted by a certain number of tracks
and works in conjunction with the shiftAmount flag.  The flag specifies the
index of the clip to shift.  This flag can be used multiple times on the command
line to specify a number of clips to shift.

---
solo(so): boolean
    properties: query, edit
    This flag specifies whether clips on a track are to be soloed or not.
Must be used in conjuction with the track flag.

---
sourceClipName(scn): boolean
    properties: create, query
    This flag is used to query the name of the source clip node associated with the specified clip index.

---
sourceEnd(se): time
    properties: create, query
    Specify where to end in the source clip's animation curves

---
sourceStart(ss): time
    properties: create, query
    Specify where to start in the source clip's animation curves

---
start(s): time
    properties: create, query
    Specify the placement of the start of the clip

---
track(t): uint
    properties: create, query
    Specify the track to operate on. For example, which track to place
a clip on, which track to mute/lock/solo.  In query mode, it may be used
in conjuction with the clipIndex flag to return the track number of a clip,
where track 1 is the first track of the character.
                        In query mode, this flag can accept a value.

---
weight(w): float
    properties: create, query
    This flag is used in to set or query the weight of the clip associated with the specified clip index.

---
weightStyle(ws): uint
    properties: create, query
    This flag is used to set or query the weightStyle attribute of the clip associated with the specified clip index.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/clipSchedule.html 
    """


def clipSchedulerOutliner(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagclipScheduler: string, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 clipSchedulerOutliner(
string
    , [annotation=string], [backgroundColor=[float, float, float]], [clipScheduler=string], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

clipSchedulerOutliner is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.window( 'myWindow', rtf=0, width=200 )
cmds.formLayout( 'myForm' )
cmds.clipSchedulerOutliner( 'myOutliner', clipScheduler='charScheduler1' )
cmds.formLayout( 'myForm', e=True, af=[('myOutliner', 'top', 0), ('myOutliner', 'left', 0), ('myOutliner', 'bottom', 0), ('myOutliner', 'right', 0)] )
cmds.showWindow()

---
Return:
---


    string: The name of the outliner control.

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
clipScheduler(cs): string
    properties: edit
    Name of the clip scheduler for which to display information.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/clipSchedulerOutliner.html 
    """


def closeCurve(flagblendBias: float, flagblendKnotInsertion: boolean, flagcaching: boolean, flagconstructionHistory: boolean, flagcurveOnSurface: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagparameter: float, flagpreserveShape: int, flagreplaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 closeCurve(
curve
    , [blendBias=float], [blendKnotInsertion=boolean], [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [name=string], [nodeState=int], [object=boolean], [parameter=float], [preserveShape=int], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

closeCurve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.closeCurve( 'curve1', ch=True, ps=True )
Closes curve1 with history and by preserving shape.  The result will
be the name of the closed curve, and the name of the newly created
dependency node.

cmds.closeCurve( 'curve1', ch=True, ps=False )
Closes curve1 with history and will not preserve the shape of the
curve.

cmds.closeCurve( 'curve1', ch=True, rpo=True )
Closes curve1 with history and replaces the original curve with
the closed one.

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
blendBias(bb): float
    properties: create, query, edit
    Skew the result toward the first or the second curve depending
on the blend value being smaller or larger than 0.5.
Default: 0.5

---
blendKnotInsertion(bki): boolean
    properties: create, query, edit
    If set to true, insert a knot in one of the original curves
(relative position given by the parameter attribute below)
in order to produce a slightly different effect.
Default: false

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
parameter(p): float
    properties: create, query, edit
    The parameter value for the positioning of the newly inserted knot.
Default: 0.1

---
preserveShape(ps): int
    properties: create, query, edit
    0 - without preserving the shape
1 - preserve shape
2 - blend
Default: 1

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
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/closeCurve.html 
    """


def closeSurface(flagblendBias: float, flagblendKnotInsertion: boolean, flagcaching: boolean, flagconstructionHistory: boolean, flagdirection: int, flagname: string, flagnodeState: int, flagobject: boolean, flagparameter: float, flagpreserveShape: int, flagreplaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 closeSurface(
[surface|surfaceIsoparm]
    , [blendBias=float], [blendKnotInsertion=boolean], [caching=boolean], [constructionHistory=boolean], [direction=int], [name=string], [nodeState=int], [object=boolean], [parameter=float], [preserveShape=int], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

closeSurface is undoable, queryable, and editable.
The pathname to the newly closed surface and the name of the resulting
dependency node are returned.

This command also handles selected surface isoparms. For example, if
an isoparm is specified, surface1.u[0.33], then the surface will be
closed in V, regardless of the direction flag.




Example:
---
import maya.cmds as cmds

cmds.closeSurface( 'surface1', ch=True, d=0, ps=True )
Closes surface1 in the U direction with history and by preserving shape.
The name of the closed surface, and the name of the newly created
dependency node are returned.

cmds.closeSurface( 'surface1', ch=True, d=2, ps=False )
Closes surface1 in both U and V directions, with history.  Closing
the surface will not preserve the shape of the surface.

cmds.closeSurface( 'surface1.u[0.66]', ch= True )
Closes surface1 in the V direction, with history.  The direction is
implied from the specified isoparm.

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
blendBias(bb): float
    properties: create, query, edit
    Skew the result toward the first or the second surface depending on the blend value being smaller or larger than 0.5.
Default: 0.5

---
blendKnotInsertion(bki): boolean
    properties: create, query, edit
    If set to true, insert a knot in one of the original surfaces (relative position given by the parameter attribute below) in order to produce a slightly different effect.
Default: false

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
direction(d): int
    properties: create, query, edit
    The direction in which to close:
0 - U,
1 - V,
2 - Both U and V
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
parameter(p): float
    properties: create, query, edit
    The parameter value for the positioning of the newly inserted knot.
Default: 0.1

---
preserveShape(ps): int
    properties: create, query, edit
    0 - without preserving the shape
1 - preserve shape
2 - blend
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
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/closeSurface.html 
    """


def cluster(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagbindState: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagenvelope: float, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flagname: string, flagparallel: boolean, flagprune: boolean, flagrelative: boolean, flagremove: boolean, flagresetGeometry: boolean, flagselectedComponents: boolean, flagsplit: boolean, flaguseComponentTags: boolean, flagweightedNode: tuple[string, string]) -> list[string]:
    """Synopsis:
---
---
 cluster(
[objects]
    , [after=boolean], [afterReference=boolean], [before=boolean], [bindState=boolean], [components=boolean], [deformerTools=boolean], [envelope=float], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string], [parallel=boolean], [prune=boolean], [relative=boolean], [remove=boolean], [resetGeometry=boolean], [selectedComponents=boolean], [split=boolean], [useComponentTags=boolean], [weightedNode=[string, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cluster is undoable, queryable, and editable.
After creating a cluster, the cluster's weights can be modified
using the percent command or the set editor window.




Example:
---
import maya.cmds as cmds

Create a cluster which uses the transformation of elbow1
---

cmds.joint(p=(2,0,0),name="elbow1")
cmds.joint(p=(4,0,0),name="wrist1")

cmds.sphere()
cmds.cluster( wn=('elbow1', 'elbow1') )

Edit cluster1 to use the transformation of wrist1.
---

cmds.cluster( 'cluster1', e=True, bs=1, wn=('wrist1', 'wrist1') )

Create a relative cluster with its own cluster handle. The
cluster handle is drawn as the letter "C".
---

cmds.cluster( rel=True )

Modify the membership of an existing cluster. First, find
the name of the cluster's associated set, then use the sets
command to edit the set membership (add a cube and remove a plane).
---

cmds.listConnections( 'cluster1', type="objectSet" )
Result: cluster1Set
cmds.sets( 'pCube1', add='cluster1Set' )
cmds.sets( 'pPlane1', rm='cluster1Set' )

---
Return:
---


    list[string]: (the cluster node name and the cluster handle name)

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
bindState(bs): boolean
    properties: create
    When turned on, this flag adds in a compensation to ensure
the clustered objects preserve their spatial position
when clustered. This is required to prevent the geometry
from jumping at the time the cluster is created
in situations when the
cluster transforms at cluster time are not identity.

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
envelope(en): float
    properties: create, query, edit
    Set the envelope value for the deformer. Default is 1.0

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
relative(rel): boolean
    properties: create
    Enable relative mode for the cluster. In relative mode,
Only the transformations directly above the cluster are used
by the cluster. Default is off.

---
remove(rm): boolean
    properties: edit, multiuse
    Specifies that objects listed after the -g flag should
be removed from this deformer.

---
resetGeometry(rg): boolean
    properties: edit
    Reset the geometry matrices for the objects being deformed
by the cluster. This flag is used to get rid of undesirable
effects that happen if you scale an object that
is deformed by a cluster.

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

---
weightedNode(wn): [string, string]
    properties: create, query, edit
    Transform node in the DAG above the cluster to which all percents are
applied. The second DAGobject specifies the descendent of the first
DAGobject from where the transformation matrix is evaluated. Default is
the cluster handle.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cluster.html 
    """


def cmdFileOutput(flagclose: uint, flagcloseAll: boolean, flagopen: string, flagstatus: uint) -> int:
    """Synopsis:
---
---
 cmdFileOutput([close=uint], [closeAll=boolean], [open=string], [status=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cmdFileOutput is undoable, queryable, and NOT editable.
To enable logging to commence as soon as Maya starts up, the
environment variable MAYA_CMD_FILE_OUTPUT may be specified prior
to launching Maya. Setting MAYA_CMD_FILE_OUTPUT to a filename
will create and output to that given file. To access the descriptor
after Maya has started, use the -query and -open flags together.




Example:
---
import maya.cmds as cmds

cmds.cmdFileOutput( o='dbOutput.txt' )
Result: 1 ---

print( 'This message is in the file\n' )
This message is in the file
cmds.cmdFileOutput( s=1 )
Result: 0 ---

cmds.cmdFileOutput( s=2 )
Result: -3 ---

cmds.cmdFileOutput( c=1 )
Result: 0 ---

Notice that the 'This message is in the file' string is in the file,
as are all of the entered commands and the
'Result: ...' lines, etc.

Turn on logging to a file on Maya startup so as to log all error
messages which happen on startup.
---

Set the environment variable MAYA_CMD_FILE_OUTPUT to "trace.txt"
Start up Maya
Messages should now be logged to the file "trace.txt" as well as the
script editor window.

Turn off logging to the filename specified by $MAYA_CMD_FILE_OUTPUT
after Maya has completed startup.
---

import os
traceFile = os.environ[ "MAYA_CMD_FILE_OUTPUT" ]
descriptor = cmds.cmdFileOutput( q=True, o=traceFile )
if -1 != descriptor:
        cmds.cmdFileOutput( close=descriptor )

---
Return:
---


    int: : On open, returns a value (descriptor) that can be used to query
the status or close the file. Otherwise, a status code
indicating status of file

Flags:
---


---
close(c): uint
    properties: create
    Closes the file corresponding to the given descriptor.
If -3 is returned, the file did not exist. -1 is returned
on error, 0 is returned on successful close.

---
closeAll(ca): boolean
    properties: create
    Closes all open files.

---
open(o): string
    properties: create, query
    Opens the given file for writing (will overwrite if it exists
and is writable). If successful, a value is returned to enable
status queries and file close. -1 is returned if the file cannot
be opened for writing. The -open flag can also be specified in
-query mode. In query mode, if the named file is currently opened,
the descriptor for the specified file is returned, otherwise -1 is
returned. This is an easy way to check if a given file is
currently open.
      In query mode, this flag needs a value.

---
status(s): uint
    properties: create, query
    Queries the status of the given descriptor. -3 is returned
if no such file exists, -2 indicates the file is not open,
-1 indicates an error condition, 0 indicates file is ready
for writing.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cmdFileOutput.html 
    """


def cmdScrollFieldExecuter(flagannotation: string, flagappendText: string, flagautoCloseBraces: boolean, flagbackgroundColor: tuple[float, float, float], flagclear: boolean, flagcommandCompletion: boolean, flagcopySelection: boolean, flagcurrentLine: uint, flagcutSelection: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexecute: boolean, flagexecuteAll: boolean, flagexists: boolean, flagfileChangedCommand: script, flagfilename: boolean, flagfilterKeyPress: script, flagfullPathName: boolean, flaghasFocus: boolean, flaghasSelection: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaginsertText: string, flagisObscured: boolean, flagload: boolean, flagloadContents: string, flagloadFile: string, flagmanage: boolean, flagmodificationChangedCommand: script, flagmodified: boolean, flagnoBackground: boolean, flagnumberOfLines: uint, flagnumberOfPopupMenus: boolean, flagobjectPathCompletion: boolean, flagparent: string, flagpasteSelection: boolean, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagredo: boolean, flagremoveStoredContents: string, flagreplaceAll: tuple[string, string], flagsaveFile: string, flagsaveSelection: string, flagsaveSelectionToShelf: boolean, flagsearchAndSelect: boolean, flagsearchDown: boolean, flagsearchMatchCase: boolean, flagsearchString: string, flagsearchWraps: boolean, flagselect: tuple[uint, uint], flagselectAll: boolean, flagselectedText: boolean, flagshowLineNumbers: boolean, flagshowTabsAndSpaces: boolean, flagshowTooltipHelp: boolean, flagsource: boolean, flagsourceType: string, flagspacesPerTab: uint, flagstatusBarMessage: string, flagstoreContents: string, flagtabsForIndent: boolean, flagtext: string, flagtextLength: boolean, flagundo: boolean, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 cmdScrollFieldExecuter([annotation=string], [appendText=string], [autoCloseBraces=boolean], [backgroundColor=[float, float, float]], [clear=boolean], [commandCompletion=boolean], [copySelection=boolean], [currentLine=uint], [cutSelection=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [execute=boolean], [executeAll=boolean], [exists=boolean], [fileChangedCommand=script], [filename=boolean], [filterKeyPress=script], [fullPathName=boolean], [hasFocus=boolean], [hasSelection=boolean], [height=int], [highlightColor=[float, float, float]], [insertText=string], [isObscured=boolean], [load=boolean], [loadContents=string], [loadFile=string], [manage=boolean], [modificationChangedCommand=script], [modified=boolean], [noBackground=boolean], [numberOfLines=uint], [numberOfPopupMenus=boolean], [objectPathCompletion=boolean], [parent=string], [pasteSelection=boolean], [popupMenuArray=boolean], [preventOverride=boolean], [redo=boolean], [removeStoredContents=string], [replaceAll=[string, string]], [saveFile=string], [saveSelection=string], [saveSelectionToShelf=boolean], [searchAndSelect=boolean], [searchDown=boolean], [searchMatchCase=boolean], [searchString=string], [searchWraps=boolean], [select=[uint, uint]], [selectAll=boolean], [selectedText=boolean], [showLineNumbers=boolean], [showTabsAndSpaces=boolean], [showTooltipHelp=boolean], [source=boolean], [sourceType=string], [spacesPerTab=uint], [statusBarMessage=string], [storeContents=string], [tabsForIndent=boolean], [text=string], [textLength=boolean], [undo=boolean], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cmdScrollFieldExecuter is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

this will create a tiny window with a Mel command executer.
cmds.window()
cmds.columnLayout()
cmds.cmdScrollFieldExecuter(width=200, height=100)
cmds.showWindow()

this will create a tiny window with a Python command executer.
cmds.window()
cmds.columnLayout()
cmds.cmdScrollFieldExecuter(width=200, height=100, sourceType="python")
cmds.showWindow()

---
Return:
---


    string: The name of the executer control

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
appendText(at): string
    properties: create, edit
    Appends text to the end of this field.

---
autoCloseBraces(acb): boolean
    properties: create, query, edit
    Specifies whether a closing brace should automatically be added when
hitting enter after an opening brace. (default on)

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
clear(clr): boolean
    properties: create, edit
    Clears the field.

---
commandCompletion(cco): boolean
    properties: create, query, edit
    Enable/disable command completion

---
copySelection(cp): boolean
    properties: create, edit
    Copies the current selection from this field.

---
currentLine(cl): uint
    properties: create, query, edit
    Sets/returns the current line which the cursor is on.

---
cutSelection(ct): boolean
    properties: create, edit
    Cuts the current selection from this field.

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
execute(exc): boolean
    properties: create, edit
    Executes the current selection.  If there is no selection, all text is executed.

---
executeAll(exa): boolean
    properties: create, edit
    Executes all text.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fileChangedCommand(fcc): script
    properties: create, edit
    Only valid when this field contains a file.
Sets a script which will be called whenever the file is externally modified,
renamed or removed from disk.
In MEL, the function should have the following signature:

proc fileChanged(string $file)

---
filename(fn): boolean
    properties: query
    Returns the full path + filename of the script which was either loaded or saved.
If there isn't one returns an empty string.

---
filterKeyPress(fkp): script
    properties: create, query, edit
    Sets a script which will be called to handle key-press events.
The function should have the following signature:

proc int filterKeyPress(int $modifiers, string $key)

modifiers: a bit mask where Shift is bit 1, Ctrl is bit 3,
Alt is bit 4, and bit 5 is the 'Windows' key on Windows keyboards
and the Command key on Mac keyboards.

key: Specifies what key was pressed. The key is either a single
ascii character or one of the keyword strings for the special
keyboard characters. For example:
Up, Down, Right, Left,
Home, End, Page_Up, Page_Down, Insert
Return, Space
F1 to F12

The function should return 1 to indicate that they key event has been
handled, and 0 to indicate that it has not been handled.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
hasFocus(hf): boolean
    properties: query
    Whether this control is currently in focus.

---
hasSelection(hsl): boolean
    properties: query
    Whether this control currently has a selection or not.

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
insertText(it): string
    properties: create, edit
    Inserts the specified text into the position under the cursor,
replacing any currently selected text. The selection and cursor
position can be set using the select flag. Appends text to the
end of this field.

---
isObscured(io): boolean
    properties: query
    Return whether the control can actually be seen by the user.
The control will be obscured if its state is invisible, if it is
blocked (entirely or partially) by some other control, if it or a
parent layout is unmanaged, or if the control's window is
invisible or iconified.

---
load(ld): boolean
    properties: create, edit
    Prompts the user for a script to load into this field.  The loaded filename becomes
associated with this executer field and saving will save directly to the file.

---
loadContents(ldc): string
    properties: create, edit
    Loads the contents of the specified filename into this field.  The path and extension for this filename
is provided internally.  This command is only intended for loading the contents of this executer field from a previous
instance of this executer field.

---
loadFile(ldf): string
    properties: create, edit
    If the provided string is a fully specified file path, then attempts to load the
file contents into this field.  If the string is empty or not valid then prompts
the user for a script to load into this field.  In both cases the filename becomes
associated with this executer field and saving will save directly to the file.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
modificationChangedCommand(mcc): script
    properties: create, edit
    Sets a script which will be called whenever the content of this field changes in
a way that affects the modification state.
In MEL, the function should have the following signature:

proc modificationChanged(int $m)

If $m is true, the field has been modified; otherwise it is false.

---
modified(mod): boolean
    properties: query, edit
    Sets or returns whether the field has been modified.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfLines(nl): uint
    properties: query
    Returns the total number of lines in the document.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
objectPathCompletion(opc): boolean
    properties: create, query, edit
    Enable/disable path completion

---
parent(p): string
    properties: create, query
    The parent layout for this control.

---
pasteSelection(pst): boolean
    properties: create, edit
    Pastes text into this field at the current caret position.

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
redo(rd): boolean
    properties: create, edit
    Redo the last operation.

---
removeStoredContents(rsc): string
    properties: create, edit
    Removes the stored contents of this field with the specified filename.  The path and extension for the file is
provided internally.  This command is only intended for removing previously stored contents of this executer field.

---
replaceAll(rpa): [string, string]
    properties: create, edit
    Replaces all instances of the first string in the field text with the
second string.  The case sensitivity of this operation is set with the
-searchMatchCase flag.

---
saveFile(svf): string
    properties: create, edit
    Saves the entire script contents of this field directly to the specified file path.

---
saveSelection(sv): string
    properties: create, edit
    Prompts to save the current selection to a file.  The default filename prompt will be prepended with the given string.

---
saveSelectionToShelf(svs): boolean
    properties: create, edit
    Prompts to save the current selection to an item in the shelf.

---
searchAndSelect(sas): boolean
    properties: query
    Searches for (and selects) the specified search string using the
specified search options.

---
searchDown(sd): boolean
    properties: create, query, edit
    Specifies whether to search from the cursor down, or up.

---
searchMatchCase(smc): boolean
    properties: create, query, edit
    Specifies whether the search is to be case sensitive or not.

---
searchString(ss): string
    properties: create, query, edit
    Specifies the string to search for.

---
searchWraps(sw): boolean
    properties: create, query, edit
    Specifies whether the search should wrap around.

---
select(sl): [uint, uint]
    properties: create, edit
    Selects text within a specified range.

---
selectAll(sla): boolean
    properties: create, edit
    Selects all text.

---
selectedText(slt): boolean
    properties: query
    The text in the current selection range.

---
showLineNumbers(sln): boolean
    properties: create, query, edit
    Shows/hides the line numbes column.

---
showTabsAndSpaces(sts): boolean
    properties: create, query, edit
    Visually show tab and space indicators. (default off)

---
showTooltipHelp(sth): boolean
    properties: create, query, edit
    Enable/disable tooltips in the command execution window

---
source(src): boolean
    properties: create, edit
    Prompts the user for a script to source (execute without loading).

---
sourceType(st): string
    properties: create, query
    Sets the source type for this command executer field.
Valid values are "mel" (enabled by default)
and "python".

---
spacesPerTab(spt): uint
    properties: create, query, edit
    Specifies the number of spaces equivalent to one tab stop. (default 4)

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
storeContents(stc): string
    properties: create, edit
    If the provided string is a fully specified file path, then attempts to store the contents of this field
to that path. Otherwise, uses the provided string as a filename only and uses an internally generated
path and extension for the file, as used by the -loadContents and -removeStoredContents flags.
In both cases, a new unique filename will be generated if the specified name exists.
Returns the filename of the file saved upon completion, and an empty string otherwise.

---
tabsForIndent(tfi): boolean
    properties: create, query, edit
    Specifies whether tab characters should be inserted when indenting. (default on)

---
text(t): string
    properties: create, query, edit
    Replaces the field text with the given string.

---
textLength(tl): boolean
    properties: query
    The number of characters in this text field.

---
undo(ud): boolean
    properties: create, edit
    Undo the last operation.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cmdScrollFieldExecuter.html 
    """


def cmdScrollFieldReporter(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagclear: boolean, flagcopySelection: boolean, flagcutSelection: boolean, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagechoAllCommands: boolean, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfilterSourceType: string, flagfullPathName: boolean, flaghasFocus: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglineNumbers: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpasteSelection: boolean, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagreceiveFocusCommand: script, flagsaveSelection: string, flagsaveSelectionToShelf: boolean, flagselect: tuple[uint, uint], flagselectAll: boolean, flagstackTrace: boolean, flagstatusBarMessage: string, flagsuppressErrors: boolean, flagsuppressInfo: boolean, flagsuppressResults: boolean, flagsuppressStackTrace: boolean, flagsuppressWarnings: boolean, flagtext: string, flagtextLength: boolean, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 cmdScrollFieldReporter([annotation=string], [backgroundColor=[float, float, float]], [clear=boolean], [copySelection=boolean], [cutSelection=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [echoAllCommands=boolean], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [filterSourceType=string], [fullPathName=boolean], [hasFocus=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [lineNumbers=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [pasteSelection=boolean], [popupMenuArray=boolean], [preventOverride=boolean], [receiveFocusCommand=script], [saveSelection=string], [saveSelectionToShelf=boolean], [select=[uint, uint]], [selectAll=boolean], [stackTrace=boolean], [statusBarMessage=string], [suppressErrors=boolean], [suppressInfo=boolean], [suppressResults=boolean], [suppressStackTrace=boolean], [suppressWarnings=boolean], [text=string], [textLength=boolean], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cmdScrollFieldReporter is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

this will create a tiny window with a command history reporter
cmds.window()
cmds.columnLayout()
cmds.cmdScrollFieldReporter(width=200, height=100)
cmds.showWindow()

---
Return:
---


    string: The name of the reporter control

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
clear(clr): boolean
    properties: create, edit
    Clears the field.

---
copySelection(cp): boolean
    properties: create, edit
    Copies the current selection from this field.

---
cutSelection(ct): boolean
    properties: create, edit
    Cuts the current selection from this field.

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
echoAllCommands(eac): boolean
    properties: create, query, edit
    Echo all commands.    (Global parameter, affects all command reporters)

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
filterSourceType(fst): string
    properties: create, query, edit
    Filters the specified source type from showing in this command reporter.
Currently supports either "mel", "python", or "" (default).
Setting the filter to the empty string ("") will remove all filtering and show both "mel" and "python" results.

---
fullPathName(fpn): boolean
    properties: query
    Return the full path name of the widget, which includes all the parents.

---
hasFocus(hf): boolean
    properties: query
    Whether this control is currently in focus.

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
lineNumbers(ln): boolean
    properties: create, query, edit
    Show line numbers (in Error/Warning messages).    (Global parameter, affects all command reporters)

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
pasteSelection(pst): boolean
    properties: create, edit
    Pastes text into this field at the current caret position.

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
    properties: create, edit
    Command executed when the field receives focus.

---
saveSelection(sv): string
    properties: create, edit
    Prompts to save the current selection to a file. The default filename prompt will be prepended with the given string.

---
saveSelectionToShelf(svs): boolean
    properties: create, edit
    Prompts to save the current selection to an item in the shelf.

---
select(sl): [uint, uint]
    properties: create, edit
    Selects text within a specified range.

---
selectAll(sla): boolean
    properties: create, edit
    Selects all text.

---
stackTrace(st): boolean
    properties: create, query, edit
    Show stack trace.    (Global parameter, affects all command reporters)

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
suppressErrors(se): boolean
    properties: create, query, edit
    Suppress errors.

---
suppressInfo(si): boolean
    properties: create, query, edit
    Suppress info.

---
suppressResults(sr): boolean
    properties: create, query, edit
    Suppress results.

---
suppressStackTrace(sst): boolean
    properties: create, query, edit
    Suppress stack trace.

---
suppressWarnings(sw): boolean
    properties: create, query, edit
    Suppress warnings.

---
text(t): string
    properties: create, query, edit
    Replaces the field text with the given string.

---
textLength(tl): boolean
    properties: query
    The number of characters in this text field.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cmdScrollFieldReporter.html 
    """


def cmdShell(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagclear: boolean, flagcommand: string, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfHistoryLines: int, flagnumberOfPopupMenus: boolean, flagnumberOfSavedLines: int, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagprompt: string, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 cmdShell(
[string]
    , [annotation=string], [backgroundColor=[float, float, float]], [clear=boolean], [command=string], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfHistoryLines=int], [numberOfPopupMenus=boolean], [numberOfSavedLines=int], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [prompt=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cmdShell is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

   Delete the window if it already exists.
---

if cmds.window( 'ExampleWindow', exists=True):
        cmds.deleteUI( 'ExampleWindow', window=True)

   Create a window containing a cmdShell and a couple buttons.
---

   Use a form layout to position the controls.
---

cmds.window( 'ExampleWindow', widthHeight=(300, 300) )
form = cmds.formLayout()
cmdShell = cmds.cmdShell()
clearButton = cmds.button(label='Clear', command=('cmds.cmdShell(\"' + cmdShell + '\", edit=True, clear=True)' ))
closeButton = cmds.button(label='Close', command=('cmds.deleteUI( "ExampleWindow", window=True )' ) )

   Set up the attachments.
---

cmds.formLayout( form, edit=True,
        attachForm=((cmdShell, 'top', 0), (cmdShell, 'left', 0), (cmdShell, 'right', 0), (clearButton, 'left', 0),
                                                                (clearButton, 'bottom', 0), (closeButton, 'bottom', 0), (closeButton, 'right', 0)),
        attachControl=(cmdShell, 'bottom', 0, clearButton),
        attachNone=((clearButton, 'top'), (closeButton, 'top')),
        attachPosition=((clearButton, 'right', 0, 50), (closeButton, 'left', 0, 50)))

cmds.showWindow( 'ExampleWindow' )

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
clear(cl): boolean
    properties: create
    Erases all visible text, and also deletes any text that had
scrolled of the top of the field.  After clearing the field
it will be blank, and you will not be able to scroll up to
see previous lines.  This flag does not affect the command
history buffer, however.

---
command(c): string
    properties: create, query, edit
    Command executed when the contents change.

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
numberOfHistoryLines(nhl): int
    properties: create, query, edit
    The number of input lines to be saved in the
command history buffer.  You can cycle through this buffer by
pressing the up and down arrow keys.  Valid values are 0 through
32767.  Any value less than 0 will be handled as if 0 was
specified.  Similarly, any value greater than 32767 will be
handled as if 32767 was specified.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
numberOfSavedLines(nsl): int
    properties: create, query, edit
    The total number of lines (the scrolled lines and
currently visible lines) that will be remembered by the field.
Any lines beyond this number will be lost, and the user will not
be able to review them by scrolling.  Valid values are 1 through
32767.  Any value less than 1 will be handled as if 1 was
specified.  Similarly, any value greater than 32767 will be
handled as if 32767 was specified.

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
prompt(pr): string
    properties: create, query, edit
    The text that is used as a prompt.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cmdShell.html 
    """


def coarsenSubdivSelectionList() -> boolean:
    """Synopsis:
---
---
 coarsenSubdivSelectionList()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

coarsenSubdivSelectionList is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

after selecting components of a subdivision surface
cmds.coarsenSubdivSelectionList()

---
Return:
---


    boolean: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/coarsenSubdivSelectionList.html 
    """


def collision(flagfriction: float, flagname: string, flagoffset: float, flagresilience: float) -> list[string]:
    """Synopsis:
---
---
 collision(
[objects]
    , [friction=float], [name=string], [offset=float], [resilience=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

collision is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
The collision command causes particles to collide with geometry.
It also allows you to specify values for the surface properties
(friction and resilience) of the collision.  These values are stored
in the geoConnector node for the geometry object.  Unlike earlier versions
of Maya, there is no separate "collision node."

If a soft object is in the selection list, the collision command assumes
that you want to make it a collider.  In order to make the soft object
collide with something use, use connectDynamic -c.  The collision menu
option sorts this out using the lead object rule and issues the necessary
commands.
On creation, this command returns a string array of the geometry names that were setup for particle collision.
When the command is used to query information, there are several possible return types.
These include:


If the -resilience or -friction flag is passed on the command line
and a single collision geometry is either selected or on the command
line, then resilience or friction value for that collision geometry is
returned as a single float value.

 If the -resilience or -friction flag is passed on the command
line and a single collision geometry and a single particle object are
either selected or on the command line, then two results might occur.
If the particle object is not set up to collide with the geometry,
then an error is displayed stating that.  If the objects are set up to
collide with each other, then the resilience or friction value that
the particle object is using for collisions with the geometry is
returned as a single float value.  This can be different than
the geometry's resilience and friction, because the user may break the
connection from the geometry's geoConnector node's resilience or
friction to the particle, and set a different value in the particle's
collisionResilience, collisionFriction or collisionOffset attribute
that is used for that geometry.  This allows the user to make each
particle respond to the same surface differently. 

 If neither flag is pass on the command line and a single geometry
and single particle object are either selected or on the command line,
then a single integer value of 1 is returned if the objects are
set up to collide with each other, and 0 is returned if they are
not. 

Lastly, if no flags are passed on the command line and a single
particle object is either selected or on the command line, then a
string array with the names of all geometries that the particle
object will collide against and the multiIndex that the geometries are
connected to is returned.  The array is formatted as follows:


pPlaneShape1:0 pPlaneShape2:2 nurbsSphereShape1:3


...where the number following the ":" is the multiIndex.






Example:
---
import maya.cmds as cmds

cmds.collision( 'nurbsSphere1', 'particle1', r=.75, f=.1 )
Causes particles of particle1 to collide with nurbsSphere1,
and sets a resilience value of 0.75 and a friction value of 0.1
for the surface.

cmds.collision( 'nurbsSphere1', q=True, f=1 )
Returns the friction value stored in the geoConnector for nurbsSphere1.

cmds.collision( 'particleShape1', 'nurbsSphere1', q=True, f=1 )
Returns the friction value that particleShape1 is using for collisions
against nurbsSphere1.  This may be the same as the friction stored in
nurbsSphere1's geoConnector.  Or, if the user broke that connection,
then it is whatever value is in the particleShape1's collisionFriction
attribute that is used for collision with nurbsSphere1.

cmds.collision( 'nurbsSphere1', 'particleShape1', q=True )
Returns whether or not particleShape1 is checking for collisions
against nurbsSphere1.

cmds.collision( 'particleShape1', q=True )
Returns all of the geometries that particleShape1 is colliding with.

---
Return:
---


    list[string]: Geometry names that were setup for particle collision.

Flags:
---


---
friction(f): float
    properties: query, edit
    Friction of the surface.  This is the amount of the colliding particle's
velocity parallel to the surface which is removed when the particle collides.
A value of 0 will mean that no tangential velocity is lost, while a value
of 1 will cause the particle to reflect straight along the normal of
the surface.

---
name(n): string
    properties: query, edit
    name of field

---
offset(o): float
    properties: query, edit
    Offset value for the connector.

---
resilience(r): float
    properties: query, edit
    Resilience of the surface.  This is the amount of the colliding particle's
velocity reflected along the normal of the surface.  A value of 1 will
give perfect reflection, while a value of 0 will have no reflection along
the normal of the surface.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/collision.html 
    """


def color(flagrgbColor: tuple[float, float, float], flaguserDefined: int) -> None:
    """Synopsis:
---
---
 color(
[objects]
    , [rgbColor=[float, float, float]], [userDefined=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

color is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

create a sphere and deselect it
cmds.sphere( n='sphere1' )
cmds.select( d=True )

Set the inactive wireframe color of the sphere to the
first user defined color
cmds.color( 'sphere1', ud=1 )

rgb defined color (red)
cmds.color( 'sphere1', rgb=(1, 0, 0) )

set the wireframe color of the sphere back to its default color
cmds.color( 'sphere1' )

---


Flags:
---


---
rgbColor(rgb): [float, float, float]
    properties: create
    Specifies and rgb color to set the selected object to.

---
userDefined(ud): int
    properties: create
    Specifies the user defined color index to set selected
object to. The valid range of numbers is [1-8].

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/color.html 
    """


def colorAtPoint(flagcoordU: float, flagcoordV: float, flagmaxU: float, flagmaxV: float, flagminU: float, flagminV: float, flagoutput: string, flagsamplesU: uint, flagsamplesV: uint) -> None:
    """Synopsis:
---
---
 colorAtPoint([coordU=float], [coordV=float], [maxU=float], [maxV=float], [minU=float], [minV=float], [output=string], [samplesU=uint], [samplesV=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorAtPoint is NOT undoable, NOT queryable, and NOT editable.colorAtPoint
return values (-o A or RGB or RGBA )
individual UV coordinates to sample (-u float  -v float )
  (numbers of calls to -u and -v must match)
uniform grid of points to sample (-su int -sv int)
  (may not use this in combination with -u or -v)
bounds for sample grid  (-mu float  -mv float -xu float -xv float)



Example:
---
import maya.cmds as cmds

The return value is the array of values determined by the number of
coord flag uses or samplesU * samplesV. The default return value is alpha.
If instead the return value is RGB there will be 3 times as many values returned,
and if it is RGBA there will be 4 times as many values.

cmds.createNode( 'checker' )

cmds.colorAtPoint( 'checker1' )
returns the alpha value at uv (0.0,0.0) for texture checker1
The return array will have one entry corresponding to this alpha.

cmds.colorAtPoint( 'checker1', u=.5, v=.5 )
returns the alpha value at uv (0.5,0.5) for texture checker1
The return array will have one entry corresponding to this alpha.

cmds.colorAtPoint( 'checker1', o='RGB', u=(.5, 0.0), v=(.5, 0.1) )
returns the colors at uv (0.5,0.5) and (0.0, 0.01) for texture checker1
The return array will have 6 values in the following order: RGBRGB

cmds.colorAtPoint( 'checker1', o='A', su=11, sv=6 )
returns the alpha for 50 points in a uniform 11 by 6 grid mapped across
uv (0.0, 0.0) to uv (1.0, 1.0) The 12th point would be the first point
in the second row of samples where uv = (0.0, 0.2)

cmds.colorAtPoint( 'checker1', o='A', su=3, sv=3, mu=0.3, mv=0.3, xu=0.4, xv=0.4 )
returns the alpha for 9 points in a uniform 3 by 3 grid mapped across
uv (0.3, 0.3) to uv (0.4, 0.4) The 4th point would be the first point
in the second row of samples where uv = (0.35, 0.3).

---


Flags:
---


---
coordU(u): float
    properties: create, multiuse
    Input u coordinate to sample texture at.

---
coordV(v): float
    properties: create, multiuse
    Input v coordinate to sample texture at.

---
maxU(xu): float
    properties: create
    DEFAULT 1.0
Maximum u bounds to sample.

---
maxV(xv): float
    properties: create
    DEFAULT 1.0
Maximum v bounds to sample.

---
minU(mu): float
    properties: create
    DEFAULT 0.0
Minimum u bounds to sample.

---
minV(mv): float
    properties: create
    DEFAULT 0.0
Minimum v bounds to sample.

---
output(o): string
    properties: create
    Type of data to output:
        A        = alpha only
        RGB  = color only
        RGBA = color and alpha

---
samplesU(su): uint
    properties: create
    DEFAULT 1
The number of points to sample in the U dimension.

---
samplesV(sv): uint
    properties: create
    DEFAULT 1
The number of points to sample in the V dimension.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorAtPoint.html 
    """


def colorEditor(flagalpha: float, flaghsvValue: tuple[float, float, float], flagmini: boolean, flagparent: string, flagposition: tuple[int, int], flagresult: boolean, flagrgbValue: tuple[float, float, float]) -> string:
    """Synopsis:
---
---
 colorEditor([alpha=float], [hsvValue=[float, float, float]], [mini=boolean], [parent=string], [position=[int, int]], [result=boolean], [rgbValue=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorEditor is undoable, queryable, and NOT editable.colorEditor
The command will return the user's color component values along with a
boolean to indicate whether the dialog was dismissed by pressing
the "OK" button.  As an alternative to responding to
the colorEditor command's return string you can now query
the -rgb/rgbValue, -hsv/hsvValue, and -r/result
flags to get the same information.




Example:
---
import maya.cmds as cmds

   Example 1.
---

cmds.colorEditor()
if cmds.colorEditor(query=True, result=True):
        values = cmds.colorEditor(query=True, rgb=True)
        print 'RGB = ' + str(values)
        values = cmds.colorEditor(query=True, hsv=True)
        print 'HSV = ' + str(values)
        alpha = cmds.colorEditor(query=True, alpha=True)
        print 'Alpha = ' + str(alpha)
else:
        print 'Editor was dismissed'

   Example 2.
---

result = cmds.colorEditor()
buffer = result.split()
if '1' == buffer[3]:
        values = cmds.colorEditor(query=True, rgb=True)
        print 'RGB = ' + str(values)
        alpha = cmds.colorEditor(query=True, alpha=True)
        print 'Alpha = ' + str(alpha)
else:
        print 'Editor was dismissed'

---
Return:
---


    string: The string format is "float float float boolean". The first three
float values correspond to the color components.The final argument is 1 if the dialog's "OK" button was pressed,
and 0 if the "Cancel" button was pressed.

Flags:
---


---
alpha(a): float
    properties: create, query
    Float values corresponding to the alpha transparency component,
, which ranges from 0.0 to 1.0.  Use this flag to specify the
initial alpha value of the Color Editor, or query
this flag to determine the alpha value set in the editor.

---
hsvValue(hsv): [float, float, float]
    properties: create, query
    Three float values corresponding to the hue, saturation, and
value color components, where the hue value ranges from 0.0 to 360.0
and the saturation and value components range from 0.0 to 1.0.  Use
this flag to specify the initial color of the Color Editor, or query
this flag to determine the color set in the editor.

---
mini(m): boolean
    properties: create
    Enable the mini color editor mode.

---
parent(p): string
    properties: create
    Specify the parent window for the dialog.  The dialog will
be centered on this window and raise and lower with it's parent.
By default, the dialog is not parented to a particular window and
is simply centered on the screen.

---
position(pos): [int, int]
    properties: create
    Specify the window position for the dialog.

---
result(r): boolean
    properties: query
    This query only flag returns true if the dialog's "OK" button
was pressed, false otherwise.  If you query this flag immediately
after showing the Color Editor then it will return the same value
as the boolean value returned in the colorEditor command's
return string.

---
rgbValue(rgb): [float, float, float]
    properties: create, query
    Three float values corresponding to the red, green, and blue
color components, all of which range from 0.0 to 1.0.  Use this
flag to specify the initial color of the Color Editor, or query
this flag to determine the color set in the editor.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorEditor.html 
    """


def colorIndex(flagactive: boolean, flagdormant: boolean, flaghueSaturationValue: boolean, flagresetToFactory: boolean, flagresetToSaved: boolean, flaguserColor: boolean) -> int:
    """Synopsis:
---
---
 colorIndex(
int [float float float]
    , [active=boolean], [dormant=boolean], [hueSaturationValue=boolean], [resetToFactory=boolean], [resetToSaved=boolean], [userColor=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorIndex is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Set the first entry in the color palette to have RGB values 1 0 0 - red.
cmds.colorIndex( 1, 1, 0, 0 )

Set the first entry in the color palette to have HSV values 360 1 1 - red.
cmds.colorIndex( 1, 360, 0, 0, hsv=True )

Return the RGB color values of the first entry of the color palette.
cmds.colorIndex( 1, q=True )

Return the HSV color values of the first entry of the color palette.
cmds.colorIndex( 1, q=True, hsv=True )

---
Return:
---


    int: Returns 1 on success.

Flags:
---


---
active(atv) 2024: boolean
    properties: create
    Combined with query mode, with given index, query the active color palette.

---
dormant(dor) 2024: boolean
    properties: create
    Combined with query mode, with given index, query the dormant color palette.

---
hueSaturationValue(hsv): boolean
    properties: create, query
    Indicates that rgb values are really hsv values.
Upon query, returns the HSV valuses as an array of 3 floats.

---
resetToFactory(rf): boolean
    properties: create
    Resets all color index palette entries to their
factory defaults.

---
resetToSaved(rs): boolean
    properties: create
    Resets all color palette entries to their saved values.

---
userColor(uc) 2024: boolean
    properties: create
    Combined with query mode, with given index, query the user color palette.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorIndex.html 
    """


def colorIndexSliderGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagextraLabel: string, flagforceDragRefresh: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaginvisible: int, flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagmaxValue: int, flagminValue: int, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flaguseTemplate: string, flagvalue: int, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 colorIndexSliderGrp(
groupName
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string], [forceDragRefresh=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [invisible=int], [isObscured=boolean], [label=string], [manage=boolean], [maxValue=int], [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [useTemplate=string], [value=int], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorIndexSliderGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a color slider group consisting of a label, a
color canvas and a slider. The value of the slider defines a color
index into the a color table. The corresponding color is displayed
in the canvas.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.colorIndexSliderGrp( label='Select Color', min=0, max=20, value=10 )
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
    Command executed when the value changes.  This command is
not invoked when the value changes via the -v/value flag.

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
dragCommand(dc): script
    properties: create, edit
    Command executed when the value changes by dragging the
slider's value marker.

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
    Sets the string to be the text for the extra label.

---
forceDragRefresh(fdr): boolean
    properties: create, query, edit
    If used then force refresh on drag

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
invisible(inv): int
    properties: create, query, edit
    Set the invisible color index.

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
    Label text for the group.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxValue(max): int
    properties: create, query, edit
    Maximum color index.

---
minValue(min): int
    properties: create, query, edit
    Minimum color index.

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
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
value(v): int
    properties: create, query, edit
    Color index.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorIndexSliderGrp.html 
    """


def colorInputWidgetGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagalphaValue: float, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagforceDragRefresh: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghsvValue: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrgbValue: tuple[float, float, float], flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 colorInputWidgetGrp(
groupName
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [alphaValue=float], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [forceDragRefresh=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [hsvValue=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rgbValue=[float, float, float]], [rowAttach=[int, string, int]], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorInputWidgetGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

Create a color slider group consisting of a label, a color canvas,
RGB and HSV sliders.  Clicking on the canvas will bring up the
color editor.




Example:
---
import maya.cmds as cmds

cmds.window( title='Colors' )
cmds.columnLayout()
cmds.colorInputWidgetGrp( label='Color', rgb=(1, 0, 0) )
cmds.showWindow()

---
Return:
---


    string: (the name of the created group)

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
alphaValue(alp): float
    properties: create, query, edit
    Alpha (transparency) of the color. Will show the alpha UI.
Alpha will be set only if RGB or HSV is also set at the same time.

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
    Command string executed when slider value changes.

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
forceDragRefresh(fdr): boolean
    properties: create
    If used then force refresh on drag

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
hsvValue(hsv): [float, float, float]
    properties: create, query, edit
    Color in hue, saturation, and value format.

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
    Label text for the group.

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
rgbValue(rgb): [float, float, float]
    properties: create, query, edit
    Color in red, green, and blue format.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorInputWidgetGrp.html 
    """


def colorManagementCatalog(flagaddTransform: string, flageditUserTransformPath: string, flaglistSupportedExtensions: boolean, flaglistTransformConnections: boolean, flagpath: string, flagqueryUserTransformPath: boolean, flagremoveTransform: string, flagtransformConnection: string, flagtype: string) -> None:
    """Synopsis:
---
---
 colorManagementCatalog([addTransform=string], [editUserTransformPath=string], [listSupportedExtensions=boolean], [listTransformConnections=boolean], [path=string], [queryUserTransformPath=boolean], [removeTransform=string], [transformConnection=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorManagementCatalog is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.colorManagementCatalog(addTransform='My Custom Viewing LUT', type='view', path='/path/to/myCustomViewingLUT.lut', transformConnection='ACES')

cmds.colorManagementCatalog(removeTransform='My Custom Viewing LUT', type='view')

cmds.colorManagementCatalog(listTransformConnections=True, type='view')

cmds.colorManagementCatalog(editUserTransformPath='/path/transforms')

---


Flags:
---


---
addTransform(adt): string
    properties: create
    Add transform to collection.

---
editUserTransformPath(eut): string
    properties: create
    Edit the user transform directory. By changing the directory, all custom
transforms currently added could be changed, and new ones could appear.

---
listSupportedExtensions(lse): boolean
    properties: create
    List the file extensions that are supported by add transform.  This list is
valid for all transform types, and therefore this flag does not require
use of the type flag.

---
listTransformConnections(ltc): boolean
    properties: create
    List the transforms that can be used as source (for "view" and "output" types)
or destination (for "input" and "rendering space" types) to connect a custom
transform to the rest of the transform collection.

---
path(pth): string
    properties: create
    In addTransform mode, the path to the transform data file.

---
queryUserTransformPath(qut): boolean
    properties: create
    Query the user transform directory.

---
removeTransform(rmt): string
    properties: create
    Remove transform from collection.

---
transformConnection(tcn): string
    properties: create
    In addTransform mode, an existing transform to which the added transform
will be connected. For an input transform or rendering space transform, this
will be a destination. For a view or output transform, this will be a source.

---
type(typ): string
    properties: create
    The type of transform added, removed, or whose transform connections are to
be listed. Must be one of "view", "rendering space", "input", or "output".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorManagementCatalog.html 
    """


def colorManagementConvert(flagtoDisplaySpace: tuple[float, float, float]) -> None:
    """Synopsis:
---
---
 colorManagementConvert([toDisplaySpace=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorManagementConvert is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds
color = cmds.colorManagementConvert(toDisplaySpace=[0.5, 0.5, 0.5])

---


Flags:
---


---
toDisplaySpace(tds): [float, float, float]
    properties: create
    Converts the given RGB value to display space.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorManagementConvert.html 
    """


def colorManagementFileRules(flagaddRule: string, flagcolorSpace: string, flagcolorSpaceDescription: string, flagcolorSpaceFamilies: string, flagcolorSpaceNames: boolean, flagdown: string, flagenabled: boolean, flagevaluate: string, flagextension: string, flaglistRules: boolean, flagload: boolean, flagmoveUp: string, flagpattern: string, flagremove: string, flagrestoreDefaults: boolean, flagsave: boolean) -> None:
    """Synopsis:
---
---
 colorManagementFileRules([addRule=string], [colorSpace=string], [colorSpaceDescription=string], [colorSpaceFamilies=string], [colorSpaceNames=boolean], [down=string], [enabled=boolean], [evaluate=string], [extension=string], [listRules=boolean], [load=boolean], [moveUp=string], [pattern=string], [remove=string], [restoreDefaults=boolean], [save=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorManagementFileRules is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
cmds.colorManagementFileRules(remove='ruleName')
cmds.colorManagementFileRules(up='ruleName')
cmds.colorManagementFileRules(down='ruleName')

cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
cmds.colorManagementFileRules('ruleName', query=True, extension=True)
cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)

cmds.colorManagementFileRules(save=True)
cmds.colorManagementFileRules(load=True)

Return array of rule name strings.
cmds.colorManagementFileRules(listRules=True)

Return input space corresponding to file path.
cmds.colorManagementFileRules(evaluate=filePath)

---


Flags:
---


---
addRule(add): string
    properties: create
    Add a rule with the argument name to the list of rules, as the
highest-priority rule.  If this flag is used, the pattern, extension, and
colorSpace flags must be used as well, to specify the file rule pattern,
extension, and color space, respectively.

---
colorSpace(cs): string
    properties: create, query, edit
    The input color space for the rule.  If the rule matches a file path, this
is the color space that is returned.  This color space must match an existing
color space in the input color space list.

---
colorSpaceDescription(csd): string
    properties: query
    Returns the description for a specific color space.
                        In query mode, this flag needs a value.

---
colorSpaceFamilies(csf): string
    properties: query
    Returns the list of families for a specific color space. Used to add submenus
when populating the color spaces UI popup of a rule.
                        In query mode, this flag needs a value.

---
colorSpaceNames(csn): boolean
    properties: query
    Returns the list of available color spaces. Used to populate the color
spaces UI popup of a rule.

---
down(dwn): string
    properties: create
    Move the rule with the argument name down one position towards lower priority.

---
enabled(ena): boolean
    properties: query
    Are the file rules enabled?

---
evaluate(ev): string
    properties: create
    Evaluates the list of rules and returns the input color space name that
corresponds to the argument file path.

---
extension(ext): string
    properties: create, query, edit
    The file extension for the rule is case insensitive

---
listRules(lsr): boolean
    properties: create
    Returns an array of rule name strings, in order, from lowest-priority (rule 0)
to highest-priority (last rule in array).

---
load(ld): boolean
    properties: create
    Read the rules from Maya preferences.  Any existing rules are cleared.

---
moveUp(up): string
    properties: create
    Move the rule with the argument name up one position towards higher priority.

---
pattern(pat): string
    properties: create, query, edit
    The file path pattern for the rule.  This is the substring to match in the
file path, expressed as a glob pattern: for example, '*' matches all files.
For more information about glob pattern syntax, see
http://en.wikipedia.org/wiki/Glob_%28programming%29.

---
remove(rm): string
    properties: create
    Remove the rule with the argument name from the list of rules.

---
restoreDefaults(rde): boolean
    properties: create
    Restore the list of rules to the default ones only.

---
save(sav): boolean
    properties: create
    Save the rules to Maya preferences.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorManagementFileRules.html 
    """


def colorManagementPrefs(flagcmConfigFileEnabled: boolean, flagcmEnabled: boolean, flagcolorManageAllNodes: boolean, flagcolorManagePots: boolean, flagcolorManagedNodes: boolean, flagcolorManagementSDKVersion: string, flagconfigFilePath: string, flagconfigFileVersion: string, flagdefaultInputSpaceName: string, flagdisplayName: string, flagdisplayNames: boolean, flagequalsToPolicyFile: string, flagexportPolicy: string, flaginhibitEvents: boolean, flaginputSpaceDescription: string, flaginputSpaceFamilies: string, flaginputSpaceNames: boolean, flagloadPolicy: string, flagloadedDefaultInputSpaceName: string, flagloadedDisplayName: string, flagloadedOutputTransformName: string, flagloadedRenderingSpaceName: string, flagloadedViewName: string, flagloadedViewTransformName: string, flagmissingColorSpaceNodes: boolean, flagocioRulesEnabled: boolean, flagociov2Enabled: boolean, flagoutputTarget: string, flagoutputTransformEnabled: boolean, flagoutputTransformName: string, flagoutputTransformNames: boolean, flagoutputTransformUseColorConversion: boolean, flagoutputUseViewTransform: boolean, flagpolicyFileName: string, flagpopupOnError: boolean, flagrefresh: boolean, flagrenderingSpaceName: string, flagrenderingSpaceNames: boolean, flagrestoreDefaults: boolean, flagviewDisplayNames: string, flagviewName: string, flagviewNames: boolean, flagviewTransformName: string, flagviewTransformNames: boolean) -> None:
    """Synopsis:
---
---
 colorManagementPrefs([cmConfigFileEnabled=boolean], [cmEnabled=boolean], [colorManageAllNodes=boolean], [colorManagePots=boolean], [colorManagedNodes=boolean], [colorManagementSDKVersion=string], [configFilePath=string], [configFileVersion=string], [defaultInputSpaceName=string], [displayName=string], [displayNames=boolean], [equalsToPolicyFile=string], [exportPolicy=string], [inhibitEvents=boolean], [inputSpaceDescription=string], [inputSpaceFamilies=string], [inputSpaceNames=boolean], [loadPolicy=string], [loadedDefaultInputSpaceName=string], [loadedDisplayName=string], [loadedOutputTransformName=string], [loadedRenderingSpaceName=string], [loadedViewName=string], [loadedViewTransformName=string], [missingColorSpaceNodes=boolean], [ocioRulesEnabled=boolean], [ociov2Enabled=boolean], [outputTarget=string], [outputTransformEnabled=boolean], [outputTransformName=string], [outputTransformNames=boolean], [outputTransformUseColorConversion=boolean], [outputUseViewTransform=boolean], [policyFileName=string], [popupOnError=boolean], [refresh=boolean], [renderingSpaceName=string], [renderingSpaceNames=boolean], [restoreDefaults=boolean], [viewDisplayNames=string], [viewName=string], [viewNames=boolean], [viewTransformName=string], [viewTransformNames=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorManagementPrefs is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


ws = cmds.colorManagementPrefs(q=True, renderingSpaceName=True)
cmds.colorManagementPrefs(e=True, viewTransformName="Log")

renderingSpaces = cmd.colorManagementPrefs(q=True, renderingSpaceNames=True)
viewingTransforms = cmd.colorManagementPrefs(q=True, viewTransformNames=True)

cmds.colorManagementPrefs(e=True, configFilePath="/project/local_config.ocio")

---


Flags:
---


---
cmConfigFileEnabled(cfe): boolean
    properties: query, edit
    Turn on or off applying an OCIO configuration file.  If set, the color
management configuration set in the preferences is used.

---
cmEnabled(cme): boolean
    properties: query, edit
    Turn on or off color management in general.  If set, the color
management configuration set in the preferences is used.

---
colorManageAllNodes(cma): boolean
    properties: create
    Adds color management to all input nodes such as file texture nodes

---
colorManagePots(cmp): boolean
    properties: query, edit
    Turn on or off color management of color pots in the UI.  If set, colors
in color pots are taken to be in rendering space, and are displayed after being
transformed by the view transform set in the preferences.

---
colorManagedNodes(cmn): boolean
    properties: query
    Gets the names of all nodes that apply color management to bring pixels from an input color space
to the rendering space. Examples include file texture node.

---
colorManagementSDKVersion(cmv): string
    properties: query
    Obtain the version of the color management SDK used by Maya.

---
configFilePath(cfp): string
    properties: query, edit
    The configuration file to be used, if color management is enabled.

---
configFileVersion(cfv): string
    properties: query
    Obtain the version of the config version.

---
defaultInputSpaceName(din): string
    properties: query, edit
    This flag is obsolete.  See the colorManagementFileRules command for more
information.

---
displayName(dn): string
    properties: query, edit
    The display from the (display, view) pair, to be applied by color managed viewers and color
managed UI controls.

---
displayNames(dns): boolean
    properties: query
    Returns the list of available displays.  Used to populate the color
management preference UI popup.

---
equalsToPolicyFile(etp): string
    properties: query
    Query if the current loaded policy settings is the same with the settings described
in the policy file which is the argument of the command.
                        In query mode, this flag needs a value.

---
exportPolicy(epy): string
    properties: create
    Export the color management parameters to policy file

---
inhibitEvents(ie): boolean
    properties: create
    Inhibit client-server notifications and event triggers which occur when changing
the color management settings.

---
inputSpaceDescription(isd): string
    properties: query
    Returns the description for a specific input color space.
                        In query mode, this flag needs a value.

---
inputSpaceFamilies(isf): string
    properties: query
    Returns the list of families for a specific input color space. Used to add submenus
when populating the input color spaces UI popup.
                        In query mode, this flag needs a value.

---
inputSpaceNames(iss): boolean
    properties: query
    Returns the list of available input color spaces. Used to populate the input color
spaces UI popup.

---
loadPolicy(lpy): string
    properties: create
    Load the color management policy file. This file overides the color management settings.

---
loadedDefaultInputSpaceName(ldn): string
    properties: query
    This flag is obsolete.

---
loadedDisplayName(ld): string
    properties: query
    Gets the loaded display from the (display, view) pair.  Used by file open, import, and reference
to check for missing color spaces or transforms.

---
loadedOutputTransformName(lon): string
    properties: query
    Gets the loaded output transform.  Used by file open, import, and reference
to check for missing color spaces or transforms.

---
loadedRenderingSpaceName(lrn): string
    properties: query
    Gets the loaded rendering space.  Used by file open, import, and reference
to check for missing color spaces or transforms.

---
loadedViewName(lv): string
    properties: query
    Gets the loaded view from the (display, view) pair.  Used by file open, import, and reference
to check for missing color spaces or transforms.

---
loadedViewTransformName(lvn): string
    properties: query
    Gets the loaded view transform.  Used by file open, import, and reference
to check for missing color spaces or transforms.

---
missingColorSpaceNodes(mcn): boolean
    properties: query
    Gets the names of the nodes that have color spaces not defined in the selected transform collection
or in the selected config file. Note that an inactive color space is not a missing color space.

---
ocioRulesEnabled(ore): boolean
    properties: query, edit
    Turn on or off the use of colorspace assignment rules from the OCIO library.

---
ociov2Enabled(oci): boolean
    properties: query
    Is OCIOv2 the colour management system by default.

---
outputTarget(ott): string
    properties: query, edit
    Indicates to which output the outputTransformEnabled or the outputTransformName
flags are to be applied. Valid values are "renderer" or "playblast".
                        In query mode, this flag needs a value.

---
outputTransformEnabled(ote): boolean
    properties: query, edit
    Turn on or off applying the output transform for out of viewport renders.
If set, the output transform set in the preferences is used.

---
outputTransformName(otn): string
    properties: query, edit
    The output transform to be applied for out of viewport renders.  Disables
output use view transform mode.

---
outputTransformNames(ots): boolean
    properties: query
    Returns the list of available output transforms.

---
outputTransformUseColorConversion(otc): boolean
    properties: query, edit
    Turn on or off selecting the color space conversion for the output color space
of viewport renders.  If set, a conversion color space is used; otherwise,
a view transform is used.

---
outputUseViewTransform(ovt): boolean
    properties: query, edit
    Turns use view transform mode on.  In this mode, the output transform is set
to match the view transform.  To turn the mode off, set an output transform
using the outputTransformName flag.

---
policyFileName(pfn): string
    properties: query, edit
    Set the policy file name

---
popupOnError(poe): boolean
    properties: edit
    Turn on or off displaying a modal popup on error (as well as the normal
script editor reporting of the error), for this invocation of the
command.  Default is off.

---
refresh(rfr): boolean
    properties: create
    Refresh the color management.

---
renderingSpaceName(rsn): string
    properties: query, edit
    The color space to be used during rendering.  This is the
source color space to the viewing transform, for color managed viewers and
color managed UI controls, and the destination color space for color managed
input pixels.

---
renderingSpaceNames(rss): boolean
    properties: query
    Returns the list of available rendering spaces.  Used to populate the color
management preference UI popup.

---
restoreDefaults(rde): boolean
    properties: create
    Restore the color management settings to their default value.

---
viewDisplayNames(vds): string
    properties: query
    Returns the list of available views for a specific display. Used to populate the view name
list UI for file and image plane nodes.
                        In query mode, this flag needs a value.

---
viewName(vn): string
    properties: query, edit
    The view from the (display, view) pair, to be applied by color managed viewers and color
managed UI controls.

---
viewNames(vns): boolean
    properties: query
    Returns the list of available views from the selected display.  Used to populate the color
management preference UI popup.

---
viewTransformName(vtn): string
    properties: query, edit
    The view transform to be applied by color managed viewers and color
managed UI controls.

---
viewTransformNames(vts): boolean
    properties: query
    Returns the list of available view transforms.  Used to populate the color
management preference UI popup.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorManagementPrefs.html 
    """


def colorSliderButtonGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagalphaValue: float, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagbuttonCommand: script, flagbuttonLabel: string, flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagforceDragRefresh: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghsvValue: tuple[float, float, float], flagimage: string, flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrgbValue: tuple[float, float, float], flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flagsymbolButtonCommand: script, flagsymbolButtonDisplay: boolean, flaguseDisplaySpace: boolean, flaguseTemplate: string, flaguseVpColorPicker: boolean, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 colorSliderButtonGrp(
[string]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [alphaValue=float], [annotation=string], [backgroundColor=[float, float, float]], [buttonCommand=script], [buttonLabel=string], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [forceDragRefresh=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [hsvValue=[float, float, float]], [image=string], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rgbValue=[float, float, float]], [rowAttach=[int, string, int]], [statusBarMessage=string], [symbolButtonCommand=script], [symbolButtonDisplay=boolean], [useDisplaySpace=boolean], [useTemplate=string], [useVpColorPicker=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorSliderButtonGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command object creates a new color slider group with a button and a
symbol button. This control is primarily used in the rendering UI. In this
context, the button brings up a dialog that allows the user to assign a
texture map to this parameter. Once a texture map is available, a symbol
button shows up. When this symbol button is pressed, the user is taken to
another dialog to edit the texture map.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.colorSliderButtonGrp( label='Label', buttonLabel='Button', rgb=(1, 0, 0), symbolButtonDisplay=True, columnWidth=(5, 30), image='navButtonUnconnected.png' )
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
alphaValue(alp): float
    properties: create, query, edit
    Alpha (transparency) of the color. Will show the alpha UI.
Alpha will be set only if RGB or HSV is also set at the same time.

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
buttonCommand(bc): script
    properties: create, edit
    Command string executed when the button is pressed.

---
buttonLabel(bl): string
    properties: create, query, edit
    The button text.

---
changeCommand(cc): script
    properties: create, edit
    Command string executed when slider value changes.

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
dragCommand(dc): script
    properties: create, edit
    Command string executed when slider value marker is dragged.

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
forceDragRefresh(fdr): boolean
    properties: create, query, edit
    If used then force refresh on drag

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
hsvValue(hsv): [float, float, float]
    properties: create, query, edit
    Color in hue, saturation, and value format.

---
image(i): string
    properties: create, query, edit
    Image displayed on the symbol button.

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
    Label text for the group.

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
rgbValue(rgb): [float, float, float]
    properties: create, query, edit
    Color in red, green, and blue format.

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
symbolButtonCommand(sbc): script
    properties: create, edit
    Command string executed when the symbol button is pressed.

---
symbolButtonDisplay(sbd): boolean
    properties: create, query, edit
    Visibility of the symbol button.

---
useDisplaySpace(uds): boolean
    properties: create, query, edit
    Set the command call to be done in display space. This sets the color picker to
display space. Using the flag when setting or getting the color also converts it
accordingly.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
useVpColorPicker(vcp): boolean
    properties: create, edit
    Enabled to sample the 32bit float version from the viewport instead of the 8 bit integer that QT sees.
Note that the viewport color picker does not allow to pick color on hud elements.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorSliderButtonGrp.html 
    """


def colorSliderGrp(flagadjustableColumn: int, flagadjustableColumn2: int, flagadjustableColumn3: int, flagadjustableColumn4: int, flagadjustableColumn5: int, flagadjustableColumn6: int, flagalphaValue: float, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchangeCommand: script, flagcolumnAlign: tuple[int, string], flagcolumnAlign2: tuple[string, string], flagcolumnAlign3: tuple[string, string, string], flagcolumnAlign4: tuple[string, string, string, string], flagcolumnAlign5: tuple[string, string, string, string, string], flagcolumnAlign6: tuple[string, string, string, string, string, string], flagcolumnAttach: tuple[int, string, int], flagcolumnAttach2: tuple[string, string], flagcolumnAttach3: tuple[string, string, string], flagcolumnAttach4: tuple[string, string, string, string], flagcolumnAttach5: tuple[string, string, string, string, string], flagcolumnAttach6: tuple[string, string, string, string, string, string], flagcolumnOffset2: tuple[int, int], flagcolumnOffset3: tuple[int, int, int], flagcolumnOffset4: tuple[int, int, int, int], flagcolumnOffset5: tuple[int, int, int, int, int], flagcolumnOffset6: tuple[int, int, int, int, int, int], flagcolumnWidth: tuple[int, int], flagcolumnWidth1: int, flagcolumnWidth2: tuple[int, int], flagcolumnWidth3: tuple[int, int, int], flagcolumnWidth4: tuple[int, int, int, int], flagcolumnWidth5: tuple[int, int, int, int, int], flagcolumnWidth6: tuple[int, int, int, int, int, int], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdragCommand: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagforceDragRefresh: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghsvValue: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrgbValue: tuple[float, float, float], flagrowAttach: tuple[int, string, int], flagstatusBarMessage: string, flaguseDisplaySpace: boolean, flaguseTemplate: string, flaguseVpColorPicker: boolean, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 colorSliderGrp(
name
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [alphaValue=float], [annotation=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [forceDragRefresh=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [hsvValue=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rgbValue=[float, float, float]], [rowAttach=[int, string, int]], [statusBarMessage=string], [useDisplaySpace=boolean], [useTemplate=string], [useVpColorPicker=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

colorSliderGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a color Slider group consisting of a label, a
color canvas and a slider.  Clicking on the canvas will bring up
the color editor dialog.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.colorSliderGrp( label='Blue', rgb=(0, 0, 1) )
cmds.colorSliderGrp( label='Green', hsv=(120, 1, 1) )
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
alphaValue(alp): float
    properties: create, query, edit
    Alpha (transparency) of the color. Will show the alpha UI.
Alpha will be set only if RGB or HSV is also set at the same time.

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
    Command string executed when slider value changes.

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
dragCommand(dc): script
    properties: create, edit
    Command string executed when slider value marker is dragged.

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
forceDragRefresh(fdr): boolean
    properties: create, query, edit
    If used then force refresh on drag

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
hsvValue(hsv): [float, float, float]
    properties: create, query, edit
    Color in hue, saturation, and value format.

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
    Label text for the group.

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
rgbValue(rgb): [float, float, float]
    properties: create, query, edit
    Color in red, green, and blue format.

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
useDisplaySpace(uds): boolean
    properties: create, query, edit
    Set the command call to be done in display space. This sets the color picker to
display space. Using the flag when setting or getting the color also converts it
accordingly.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
useVpColorPicker(vcp): boolean
    properties: create, edit
    Enabled to sample the 32bit float version from the viewport instead of the 8 bit integer that QT sees.
Note that the viewport color picker does not allow to pick color on hud elements.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/colorSliderGrp.html 
    """


def columnLayout(flagadjustableColumn: boolean, flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagchildArray: boolean, flagcolumnAlign: string, flagcolumnAttach: tuple[string, int], flagcolumnOffset: tuple[string, int], flagcolumnWidth: int, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flaggeneralSpacing: int, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagmargins: int, flagnoBackground: boolean, flagnumberOfChildren: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagrowSpacing: int, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 columnLayout(
[string]
    , [adjustableColumn=boolean], [annotation=string], [backgroundColor=[float, float, float]], [childArray=boolean], [columnAlign=string], [columnAttach=[string, int]], [columnOffset=[string, int]], [columnWidth=int], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [generalSpacing=int], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [margins=int], [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowSpacing=int], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

columnLayout is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 )
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
adjustableColumn(adj): boolean
    properties: create, edit
    Sets the children of the layout to be attached on both sides.
They will stretch or shrink with the layout.

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
columnAlign(cal): string
    properties: create, edit
    Sets the alignment of children containing text or pixmaps.
Align values: "left" | "right" | "center".

---
columnAttach(cat): [string, int]
    properties: create, edit
    Sets the attachment and offsets for the children of the
layout.  Side values: "left" | "right" | "both".  Left or both is
recommended.

---
columnOffset(co): [string, int]
    properties: create, edit
    Sets the offsets for children of the layout.
Side values: "left" | "right" | "both".

---
columnWidth(cw): int
    properties: create, query, edit
    Sets the width of the column.  Unless the children are
attached to both sides of the column, the width cannot be enforced.
Larger children will expand layout.

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
rowSpacing(rs): int
    properties: create, query, edit
    Sets the space between children.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/columnLayout.html 
    """


def combinationShape(flagaddDriver: boolean, flagallDrivers: boolean, flagblendShape: string, flagcombinationTargetIndex: int, flagcombinationTargetName: string, flagcombineMethod: int, flagdriverTargetIndex: int, flagdriverTargetName: string, flagexist: boolean, flagremoveDriver: boolean) -> Int:
    """Synopsis:
---
---
 combinationShape([addDriver=boolean], [allDrivers=boolean], [blendShape=string], [combinationTargetIndex=int], [combinationTargetName=string], [combineMethod=int], [driverTargetIndex=int], [driverTargetName=string], [exist=boolean], [removeDriver=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

combinationShape is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Set a blend shape target as combination target, and another two blend shape targets as drivers, using target indexes.
---

cmds.combinationShape(blendShape='blendShape1', combinationTargetIndex=1, driverTargetIndex=[2,3])

Add two blend shape targets as drivers to a blend shape combination target, using target names.
---

cmds.combinationShape(edit='1', blendShape='blendShape1', combinationTargetName='TargetA', addDriver=1, driverTargetName=['TargetB', 'TargetC'])

Remove two blend shape targets from drivers of a blend shape combination target.
---

cmds.combinationShape(edit='1', blendShape='blendShape1', combinationTargetIndex=1, removeDriver=1, driverTargetName='TargetB', driverTargetIndex=2;

Change combine method of a blend shape combination target
---

cmds.combinationShape(edit='1', blendShape='blendShape1', combinationTargetIndex=1, combineMethod=2;

Remove all drivers of a blend shape combination target.
---

cmds.combinationShape(edit='1', blendShape='blendShape1', combinationTargetIndex=1, removeDriver=1, allDrivers=1)

Query all drivers of a blend shape combination target.
---

cmds.combinationShape(query='1', blendShape='blendShape1', combinationTargetIndex=1, allDrivers=1)

---
Return:
---


    Int: In edit mode, return the newly created combination shape node name.

Flags:
---


---
addDriver(add): boolean
    properties: 
    Add drivers to the combination shape

---
allDrivers(ald): boolean
    properties: query
    All drivers of the combination shape

---
blendShape(bs): string
    properties: create
    Associated blend shape node of the combination shape
                        In query mode, this flag can accept a value.

---
combinationTargetIndex(cti): int
    properties: create
    Driven blend shape target index of the combination shape
                        In query mode, this flag can accept a value.

---
combinationTargetName(ctn): string
    properties: create
    Driven blend shape target name of the combination shape
                        In query mode, this flag can accept a value.

---
combineMethod(cm): int
    properties: create, query, edit
    Combine method of the combination shape:

0 : Multiplication
1 : Lowest Weighting
2 : Lowest Weighting (Smooth)

---
driverTargetIndex(dti): int
    properties: create, multiuse
    Driver blend shape target index of the combination shape

---
driverTargetName(dtn): string
    properties: create, multiuse
    Driver blend shape target name of the combination shape

---
exist(ex): boolean
    properties: query
    If the combination shape exist

---
removeDriver(rmd): boolean
    properties: 
    Remove drivers from the combination shape

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/combinationShape.html 
    """


def commandEcho(flagaddFilter: list[string], flagfilter: list[string], flaglineNumbers: boolean, flagstate: boolean) -> None:
    """Synopsis:
---
---
 commandEcho([addFilter=string[]], [filter=string[]], [lineNumbers=boolean], [state=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

commandEcho is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Echo everything
cmds.commandEcho( state=True )
Go back to normal
cmds.commandEcho( state=False )
Display line number information in messages.  This is the default.
cmds.commandEcho( lineNumbers=True )
Do not display line number information in messages.
cmds.commandEcho( lineNumbers=False )
Do not display changeToolIcon, escapeCurrentTool or autoUpdateAttrEd commands when echoing everything
cmds.commandEcho( filter=('changeToolIcon', 'escapeCurrentTool', 'autoUpdateAttrEd') );
Do not display setLastFocusedCommandReporter or setLastFocusedCommandExecuter when echoing everything
cmds.commandEcho( filter=('setLastFocusedCommand') );
 Add to the current filter
cmds.commandEcho( addFilter=('addToolIcon') );

---


Flags:
---


---
addFilter(af): string[]
    properties: create
    This flag allows you to append filters to the current list of filtered commands when echo all commands is enabled.
Just like the filter flag, you can provide a partial command name, so all commands that start with a substring specified in the addFilter entry will be filtered out.

---
filter(f): string[]
    properties: create, query
    This flag allows you to filter out unwanted commands when echo all commands is enabled.
You can provide a partial command name, so all commands that start with a substring specified in filter entry will be filtered out.
If filter is empty, all commands are echoed to the command window.

---
lineNumbers(ln): boolean
    properties: create, query
    If true then file name and line number information is provided in
error and warning messages.
If false then no file name and line number information is provided
in error and warning messages.

---
state(st): boolean
    properties: create, query
    If true then all commands are echoed to the command window.
If false then only relevant commands are echoed.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/commandEcho.html 
    """


def commandLine(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagcommand: script, flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagenterCommand: script, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagholdFocus: boolean, flaginputAnnotation: string, flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfHistoryLines: int, flagnumberOfPopupMenus: boolean, flagoutputAnnotation: string, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagsourceType: string, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 commandLine(
[name]
    , [annotation=string], [backgroundColor=[float, float, float]], [command=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [holdFocus=boolean], [inputAnnotation=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfHistoryLines=int], [numberOfPopupMenus=boolean], [outputAnnotation=string], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [sourceType=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

commandLine is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a window that contains a command line.
---

window = cmds.window('window')
form = cmds.formLayout()
field = cmds.scrollField()

cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)
cmds.commandLine( cmdLine, edit=True, sourceType="python")
cmds.formLayout( form, edit=True, attachForm=[(cmdLine, 'top', 0), (cmdLine, 'left', 0), (cmdLine, 'right', 0), (field, 'left', 0), (field, 'bottom', 0), (field, 'right', 0)], attachNone=(cmdLine, 'bottom'), attachControl=(field, 'top', 5, cmdLine) )

   Give the command line initial keyboard focus.
---

cmds.setFocus( cmdLine )
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
command(c): script
    properties: create, edit
    Command executed when the command line text changes.

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
enterCommand(ec): script
    properties: create, edit
    Command executed when the keypad 'Enter' key is pressed.

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
holdFocus(hf): boolean
    properties: create, query, edit
    Sets whether the command line should hold focus after exectuing a command.

---
inputAnnotation(ian): string
    properties: create, query, edit
    Annotate the input field with an extra string value.

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
numberOfHistoryLines(nhl): int
    properties: create, query, edit
    Sets the maximum number of commands saved to the
command line history. Up to -nhl/numberOfHistoryLines previous commands
will be available by pressing the up-arrow from within the input field.
The default value is 50.

---
numberOfPopupMenus(npm): boolean
    properties: query
    Return the number of popup menus attached to this control.

---
outputAnnotation(oan): string
    properties: create, query, edit
    Annotate the output field with an extra string value.

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
sourceType(st): string
    properties: create, query, edit
    Sets the source type of this command line.
Currently supports "mel" (enabled by default)
and "python".

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/commandLine.html 
    """


def commandLogging(flaghistorySize: uint, flaglogCommands: boolean, flaglogFile: string, flagrecordCommands: boolean, flagresetLogFile: boolean) -> None:
    """Synopsis:
---
---
 commandLogging([historySize=uint], [logCommands=boolean], [logFile=string], [recordCommands=boolean], [resetLogFile=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

commandLogging is undoable, queryable, and NOT editable.
Note that if commands are logged in memory, they will
be available to the crash reporter and appear in crash logs.




Example:
---
import maya.cmds as cmds

Set the number of commands logged in memory to 20
---

cmds.commandLogging( historySize=20 )

Query the number of commands being logged in memory
---

cmds.commandLogging( q=True, historySize=True )
Result: 20

Query the log file location
---

cmds.commandLogging( q=True, logFile=True )
Result: C:/Users/foobar/Documents/maya/mayaCommandLog.txt

Change the log file location
---

cmds.commandLogging( logFile='C:/temp/log.txt' )

Reset the log file to default
---

cmds.commandLogging( resetLogFile=True )

---


Flags:
---


---
historySize(hs): uint
    properties: create, query
    Sets the number of entries
in the in-memory command history.

---
logCommands(lc): boolean
    properties: create, query
    Enables or disables the on-disk logging
of commands.

---
logFile(lf): string
    properties: create, query
    Sets the filename to use for the on-disk log.
If logging is active, the current file will be closed
before the new one is opened.

---
recordCommands(rc): boolean
    properties: create, query
    Enables or disables the in-memory logging
of commands.

---
resetLogFile(rl): boolean
    properties: create, query
    Reset the log filename to the default
('mayaCommandLog.txt' in the application folder,
alongside 'Maya.env' and the default projects folder).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/commandLogging.html 
    """


def commandPort(flagbufferSize: int, flagclose: boolean, flagechoOutput: boolean, flaglistPorts: boolean, flagname: string, flagnoreturn: boolean, flagpickleOutput: boolean, flagprefix: string, flagreturnNumCommands: boolean, flagsecurityWarning: boolean, flagsourceType: string) -> boolean:
    """Synopsis:
---
---
 commandPort([bufferSize=int], [close=boolean], [echoOutput=boolean], [listPorts=boolean], [name=string], [noreturn=boolean], [pickleOutput=boolean], [prefix=string], [returnNumCommands=boolean], [securityWarning=boolean], [sourceType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

commandPort is undoable, queryable, and NOT editable.
It supports multi-byte commands and uses utf-8 as its transform
format. It will receive utf8 command string and decode it to Maya native
coding. The result will also be encoded to utf-8 before sending back.

Care should be taken regarding INET domain sockets as no user
identification, or authorization is required to connect to a given
socket, and all commands (including "system(...)") are allowed and
executed with the user id and permissions of the Maya user. The prefix
flag can be used to reduce this security risk, as only the prefix
command is executed.

The query flag can be used to determine if a given command port exists.
See examples below.




Example:
---
import maya.cmds as cmds

Open a command port with the default name "mayaCommand".
cmds.commandPort()

Close the command port with the default name. Open client connections
are not broken.
cmds.commandPort( cl=True )

Query to see if the command command port "mayaCommand" exists.
cmds.commandPort( 'mayaCommand', q=True )

---
Return:
---


    boolean: - in query mode

Flags:
---


---
bufferSize(bs): int
    properties: create
    Commands and results are each subject to size limits. This option allows
the user to specify the size of the buffer used to communicate with Maya. If
unspecified the default buffer size is 4096 characters.
Commands longer than bufferSize characters will cause the client connection to close.
Results longer that bufferSize characters are replaced with an error message.

---
close(cl): boolean
    properties: create
    Closes the commandPort, deletes the pipes

---
echoOutput(eo): boolean
    properties: create
    Sends a copy of all command output to the command port. Typically
only the result is transmitted. This option provides a copy of
all output.

---
listPorts(lp): boolean
    properties: create
    Returns the available ports

---
name(n): string
    properties: create
    Specifies the name of the command port which this command
creates. CommandPort names of the form name create a
UNIX domain socket on the localhost corresponding to
name. If name does not begin with "/",
then /tmp/name is used. If name begins
with "/", name denotes the full path to the socket. 
Names of the form :port number create an INET domain
on the local host at the given port.

---
noreturn(nr): boolean
    properties: create
    Do not write the results from executed commands back to the
command port socket. Instead, the results from executed
commands are written to the script editor window. As no information
passes back to the command port client regarding the execution
of the submitted commands, care must be taken not to overflow
the command buffer, which would cause the connection to close.

---
pickleOutput(po): boolean
    properties: create
    Python output will be pickled.

---
prefix(pre): string
    properties: create
    The string argument is the name of a Maya command taking one string
argument. This command is called each time data is sent to the command
port. The data written to the command port is passed as the argument to
the prefix command. The data from the command port is encoded as with
enocodeString and enclosed in quotes. 
If newline characters are embedded in the command port data,
the input is split into individual lines.
These lines are treated as if they were separate
writes to the command port. Only the result to the last
prefix command is returned.

---
returnNumCommands(rnc): boolean
    properties: create
    Ignore the result of the command, but return the number of
commands that have been read and executed in this call. This
is a simple way to track buffer overflow. This flag is ignored
when the noreturn flag is specified.

---
securityWarning(sw): boolean
    properties: create
    Enables security warning on command port input.

---
sourceType(stp): string
    properties: create
    The string argument is used to indicate which source type
would be passed to the commandPort, like "mel", "python".
The default source type is "mel".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/commandPort.html 
    """


def componentBox(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexecute: tuple[string, boolean], flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabelWidth: int, flagmanage: boolean, flagmaxHeight: int, flagmaxWidth: int, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagprecision: int, flagpreventOverride: boolean, flagrowHeight: int, flagselectedAttr: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 componentBox(
[name]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [execute=[string, boolean]], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [labelWidth=int], [manage=boolean], [maxHeight=int], [maxWidth=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowHeight=int], [selectedAttr=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

componentBox is undoable, queryable, and editable.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.formLayout( 'form' )
cmds.componentBox( 'cbox' )
cmds.formLayout( 'form', e=True, af=(('cbox', 'top', 0), ('cbox', 'left', 0), ('cbox', 'right', 0), ('cbox', 'bottom', 0)) )
cmds.showWindow()

---
Return:
---


    string: (the name of the new component box)

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
execute(exe): [string, boolean]
    properties: edit
    Immediately executes the command string once for every cell (or every
selected cell, if the boolean argument is TRUE) in the
component box, for every matching selected object (ie, for every object would
be affected if you changed a cell value.)  Before the command is executed,
"#A" is substituted with the name of the attribute, and "#N" with the name
of the node, and "#P" with the full path name of the node.

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
labelWidth(lw): int
    properties: query, edit
    An optional flag which is used to modify the width assigned
to labels appearing in the componentBox.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxHeight(mh): int
    properties: query, edit
    An optional flag which is used to limit the height of the
componentBox.

---
maxWidth(mw): int
    properties: query, edit
    An optional flag which is used to limit the width of the
componentBox.

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
point that will be displayed for float-valued components.
Default is 3.  Queried, returns an int.

---
preventOverride(po): boolean
    properties: create, query, edit
    If true, this flag prevents overriding the control's
attribute via the control's right mouse button menu.

---
rowHeight(rh): int
    properties: edit
    An optional flag which is used to set the height of all rows in the
componentBox.

---
selectedAttr(sla): boolean
    properties: query
    Returns a list of names of all the attributes that are selected.
This flag is ignored when not being queried.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/componentBox.html 
    """


def componentEditor(flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagfloatField: string, flagfloatSlider: string, flagforceMainConnection: string, flaghidePathName: boolean, flaghideZeroColumns: boolean, flaghighlightConnection: string, flagjustifyHeaders: int, flaglockInput: boolean, flaglockMainConnection: boolean, flagmainListConnection: string, flagnewTab: tuple[string, string, string], flagnormalizeWeights: int, flagoperationCount: boolean, flagoperationLabels: boolean, flagoperationType: int, flagpanel: string, flagparent: string, flagprecision: int, flagremoveTab: string, flagselected: boolean, flagselectionConnection: string, flagsetOperationLabel: tuple[int, string], flagshowNamespaces: boolean, flagshowObjects: boolean, flagshowSelected: boolean, flagsortAlpha: boolean, flagstateString: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 componentEditor(
name
    , [control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [floatField=string], [floatSlider=string], [forceMainConnection=string], [hidePathName=boolean], [hideZeroColumns=boolean], [highlightConnection=string], [justifyHeaders=int], [lockInput=boolean], [lockMainConnection=boolean], [mainListConnection=string], [newTab=[string, string, string]], [normalizeWeights=int], [operationCount=boolean], [operationLabels=boolean], [operationType=int], [panel=string], [parent=string], [precision=int], [removeTab=string], [selected=boolean], [selectionConnection=string], [setOperationLabel=[int, string]], [showNamespaces=boolean], [showObjects=boolean], [showSelected=boolean], [sortAlpha=boolean], [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

componentEditor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

componentEditorWindow is a MEL procedure so need to call through MEL.
import maya.mel
maya.mel.eval('componentEditorWindow()')
cmds.componentEditor( 'componentEditorWinComponEditor', q=True, ctl=True )

---
Return:
---


    string: The panel name

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
floatField(ff): string
    properties: create, query, edit
    assigns a float field that the component editor will
use for editing groups of values.

---
floatSlider(fs): string
    properties: create, query, edit
    assigns a float slider that the component editor will
use for editing groups of values.

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
hidePathName(hpn): boolean
    properties: create, query, edit
    Hides path name of displayed element.  By default
this flag is set to false.

---
hideZeroColumns(hzc): boolean
    properties: create, query, edit
    Hides columns whose elements are all zero.  By default
this flag is set to false.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
justifyHeaders(jh): int
    properties: create, query, edit
    Set justification mode for headers of columns.  Possible values
are 0 (right justify), or 1 (left justify). By default
this flag is set to 0.

---
lockInput(li): boolean
    properties: create, query, edit
    Prevents the editor from responding to changes in
the active list. Independent of selection connection.

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
newTab(nt): [string, string, string]
    properties: create, edit
    Creates a new tab, named by the first argument, based on an existing tab, given as the second argument
using elements from a set, given in the third argument

---
normalizeWeights(nw): int
    properties: edit
    Specifies automatic normalization mode of skin clusters. Can be 0, meaning "None", or 1,
meaning "Interactive", or 2, meaning "Post". It corresponds to the "normalizeWeights" attribute
of skinCluster node.

---
operationCount(oc): boolean
    properties: query
    returns the total number of operation types
known to the component editor.

---
operationLabels(ol): boolean
    properties: query
    returns a string array containing the names for all
operation types known to the editor.

---
operationType(ot): int
    properties: create, query, edit
    Tells the editor which of its known operation types
it should be performing. This is a 0-based index.

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
precision(pre): int
    properties: create, query, edit
    Specifies the maximum number of digits displayed to the right
of the decimal place.  Can be 0 to 20.

---
removeTab(rt): string
    properties: edit
    Removes the tab based on the set provided

---
selected(sl): boolean
    properties: query
    Returns a list of strings, containing the labels of the currently selected columns

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
setOperationLabel(sol): [int, string]
    properties: edit
    uses the string as the new name for the existing operation type
specified by the integer index. Note that there is no messaging
system which allows UI to be informed of changes made by this flag.

---
showNamespaces(sn): boolean
    properties: create, query, edit
    Show the namespaces for objects, if any.  By default
this flag is set to true.

---
showObjects(so): boolean
    properties: create
    Restricts the display to columns that are in the current active list.

---
showSelected(ss): boolean
    properties: create, edit
    Restricts the display to those columns which are currently selected. By default
this flag is set to false, so all columns are selected. The results from this flag
obey the current -hideZeroColumns setting.

---
sortAlpha(sa): boolean
    properties: create, query, edit
    Controls alphabetical (true), or hierarchical sorting of columns

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/componentEditor.html 
    """


def componentTag(flagcreate: boolean, flagdelete: boolean, flaginjectionLocation: string, flagmodify: string, flagnewTagName: string, flagqueryEdit: boolean, flagrename: boolean, flagtagName: string, flaguniqueTagName: boolean) -> Any:
    """Synopsis:
---
---
 componentTag(
[objects]
    , [create=boolean], [delete=boolean], [injectionLocation=string], [modify=string], [newTagName=string], [queryEdit=boolean], [rename=boolean], [tagName=string], [uniqueTagName=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

componentTag is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

    Make a geometry
    import maya.cmds as cmds
    cmds.polyCylinder(ch=True, o=True, r=3.0, h=8.0, sc=1, sx=6, sy=9, cuv=3, name='cyl')

    Create some tags
    cmds.componentTag(['cyl.f[0:17]'], cr=True, ntn='bottomSection')
    cmds.componentTag(['cyl.f[36:53]'], cr=True, ntn='topSection')

    Edit a tag
    cmds.componentTag(['cyl.f[18:35]'], tn='bottomSection', m='add')

    Rename the tag
    cmds.componentTag('cyl', rn=True, tn='bottomSection', ntn='lowerSection')

    Delete tags (using a wild card)
    cmds.componentTag('cyl', d=True, tn='*Section')

---
Return:
---


    Any: The name of the created componentTag, or whether the command succeeded or the information
about what can be edited

Flags:
---


---
create(cr): boolean
    properties: create
    This creates a componentTag on the geometry. The name can be specified with the
-newTagName option. If no new name is specified one will be generated.
The name of the created tag is returned

---
delete(d): boolean
    properties: create
    This deletes the componentTags specified with the -tagName option.

---
injectionLocation(il): string
    properties: create
    The name of the injection node at which the componentTag will be edited.
This is only necessary in the rare case where a particular componentTag
can be altered at multiple injection locations.

---
modify(m): string
    properties: create
    This modifies the componentTag specified with the -tagName option.
The mode determines whether components are, replaced, cleared, added or removed.

---
newTagName(ntn): string
    properties: create
    The name of the new componentTag to be created or the new name
of the componentTag that is being renamed.

---
queryEdit(qe): boolean
    properties: create
    This returns what edits are allowed with the given parameters. When the command
is issued in Python a dictionary object containing what is allowed is returned.

---
rename(rn): boolean
    properties: create
    This renames the componentTag specified with the -tagName option to the
name specified with the -newTagName option

---
tagName(tn): string
    properties: create, multiuse
    The name(s) of the componentTags to be edited. This can be a single name or
a list of names. The names can contain wildcard like '*' to match multiple
existing componentTags.

---
uniqueTagName(utn) 2024.2: boolean
    properties: create
    This flag is used along the create and newTagName flags. It makes
the command generate a unique tag name if the name provided by newTagName
is already used by a tag on the injectionNode or its parents.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/componentTag.html 
    """


def condition(flagdelete: boolean, flagdependency: string, flaginitialize: boolean, flagscript: string, flagstate: boolean) -> None:
    """Synopsis:
---
---
 condition(
string
    , [delete=boolean], [dependency=string], [initialize=boolean], [script=string], [state=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

condition is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a new condition, called "UndoNorRedo", which is true if
   and only if undo is not available and redo is not available:

def isUndoNorRedo() :
        return not cmds.isTrue('UndoAvailable') and not cmds.isTrue('RedoAvailable')

cmds.condition('UndoNorRedo', initialize=True, d=['UndoAvailable', 'RedoAvailable'], s='python("isUndoNorRedo()")')

Try out the new condition
---

if cmds.isTrue('UndoNorRedo') :
        print 'Neither undo nor redo is available'
else :
        print 'Undo or redo is available'

cmds.condition('UndoNorRedo', delete=True)

---


Flags:
---


---
delete(delete): boolean
    properties: create
    Deletes the condition.

---
dependency(d): string
    properties: create, multiuse
    Each -dependency flag specifies another condition that the
new condition will be dependent on.  When any of these conditions
change, the new-state-script will run, and the state of this
condition will be set accordingly.  It is possible to define infinite loops,
but they will be caught and handled correctly at run-time.

---
initialize(i): boolean
    properties: create
    Initializes the condition, by forcing it to run its script
as soon as it is created.  If this flag is not specified, the
script will not run until one of the dependencies is triggered.

---
script(s): string
    properties: create
    The script that determines the new state of
the condition.

---
state(st): boolean
    properties: create, query, edit
    Sets the state of the condition. This can be used to create
a manually triggered condition: you could create a condition
without any dependencies and without a new-state-script. This
condition would only change state in response to the -st/state flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/condition.html 
    """


def cone(flagaxis: tuple[linear, linear, linear], flagcaching: boolean, flagconstructionHistory: boolean, flagdegree: int, flagendSweep: angle, flagheightRatio: float, flagname: string, flagnodeState: int, flagobject: boolean, flagpivot: tuple[linear, linear, linear], flagpolygon: int, flagradius: linear, flagsections: int, flagspans: int, flagstartSweep: angle, flagtolerance: linear, flaguseOldInitBehaviour: boolean, flaguseTolerance: boolean) -> list[string]:
    """Synopsis:
---
---
 cone([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean], [degree=int], [endSweep=angle], [heightRatio=float], [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [radius=linear], [sections=int], [spans=int], [startSweep=angle], [tolerance=linear], [useOldInitBehaviour=boolean], [useTolerance=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cone is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.cone()
cmds.cone( ch= True, radius=10, hr=3 )
cmds.cone( r=5, axis=(1, 1, 1), pivot=(0, 0, 1), ssw='0deg', esw='90deg' )
cmds.cone( ut=True, tol=0.01 )

---
Query the radius of the selected cone
r = cmds.cone( q=True, r=True )

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
    The degree of the resulting surface:
1 - linear,
3 - cubic
Default: 3

---
endSweep(esw): angle
    properties: create, query, edit
    The angle at which to end the surface of revolution.
Default is 2Pi radians, or 360 degrees.
Default: 6.2831853

---
heightRatio(hr): float
    properties: create, query, edit
    Ratio of "height" to "width"
Default: 2.0

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
    The primitive's pivot point

---
radius(r): linear
    properties: create, query, edit
    The radius of the object
Default: 1.0

---
sections(s): int
    properties: create, query, edit
    The number of sections determines the resolution of the surface in the sweep direction.
Used only if useTolerance is false.
Default: 8

---
spans(nsp): int
    properties: create, query, edit
    The number of spans determines the resolution of the surface in the opposite direction.
Default: 1

---
startSweep(ssw): angle
    properties: create, query, edit
    The angle at which to start the surface of revolution
Default: 0

---
tolerance(tol): linear
    properties: create, query, edit
    The tolerance with which to build the surface.
Used only if useTolerance is true
Default: 0.01

---
useOldInitBehaviour(oib): boolean
    properties: create, query, edit
    Create the cone with base on the origin as in Maya V8.0 and below
Otherwise create cone centred at origin
Default: false

---
useTolerance(ut): boolean
    properties: create, query, edit
    Use the specified tolerance to determine resolution.
Otherwise number of sections will be used.
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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cone.html 
    """


def confirmDialog(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagbutton: string, flagcancelButton: string, flagdefaultButton: string, flagdismissString: string, flagicon: string, flagmessage: string, flagmessageAlign: string, flagparent: string, flagtitle: string) -> string:
    """Synopsis:
---
---
 confirmDialog([annotation=string], [backgroundColor=[float, float, float]], [button=string], [cancelButton=string], [defaultButton=string], [dismissString=string], [icon=string], [message=string], [messageAlign=string], [parent=string], [title=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

confirmDialog is undoable, NOT queryable, and NOT editable.dismissString
The default behaviour when no arguments are specified is to create an
empty single button dialog.




Example:
---
import maya.cmds as cmdsCreate an empty single button dialog.
---


cmds.confirmDialog()Create a basic Yes/No dialog.
---


cmds.confirmDialog( title='Confirm', message='Are you sure?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )

---
Return:
---


    string: Indicates how the dialog was dismissed. If a button is
pressed then the label of the button is returned. If the dialog is
closed then the value for the flagdismissStringis
returned.

Flags:
---


---
annotation(ann): string
    properties: create, multiuse
    set the annotation for the buttons

---
backgroundColor(bgc): [float, float, float]
    properties: create
    The background color of the dialog. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0. (Windows only flag)

---
button(b): string
    properties: create, multiuse
    Create a button with the given string as it's text.

---
cancelButton(cb): string
    properties: create
    The cancel button is activated by pressing the escape key.
Note that this flag does not create a button, it simply indicates
which button created via the button flag shall respond
to the escape key.

---
defaultButton(db): string
    properties: create
    The default button is activated by pressing the enter key.
Note that this flag does not create a button, it simply indicates
which button created via the button flag shall respond
to the enter key.

---
dismissString(ds): string
    properties: create
    The string returned when the user selects the 'Close' item
from the Window Manager menu.  If this flag is not set then the
string "dismiss" is returned.

---
icon(icn): string
    properties: create
    The user can specify one of the four standard icons -- "question", "information", "warning" and "critical".  The question icon indicates that the messsage is asking a question.  The information icon indicates that the message is nothing out of the ordinary.  The warning icon indicates that the message is a warning, but can be dealt with.  The critical icon indicates that the message represents a critical problem.
When no icon flag is present, we assume the user does not want to
include any icon in the confirm dialog.

---
message(m): string
    properties: create
    The message text appearing in the dialog.

---
messageAlign(ma): string
    properties: create
    Align the message left, center, or right.

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/confirmDialog.html 
    """


def connectAttr(flagforce: boolean, flaglock: boolean, flagnextAvailable: boolean, flagreferenceDest: string) -> string:
    """Synopsis:
---
---
 connectAttr(
attribute attribute
    , [force=boolean], [lock=boolean], [nextAvailable=boolean], [referenceDest=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

connectAttr is undoable, NOT queryable, and NOT editable.
Refer to dependency node documentation.




Example:
---
import maya.cmds as cmds

cmds.createNode( 'transform', n='firstGuy' )
cmds.createNode( 'transform', n='secondGuy' )

Connect the translation of two nodes together
cmds.connectAttr( 'firstGuy.t', 'secondGuy.translate' )

Connect the rotation of one node to the override colour
of a second node.
cmds.connectAttr( 'firstGuy.rotate', 'secondGuy.overrideColor' )

---
Return:
---


    string: A phrase containing the names of the connected attributes.

Flags:
---


---
force(f): boolean
    properties: create
    Forces the connection.  If the destination is already
connected, the old connection is broken and the new one
made.

---
lock(l): boolean
    properties: create
    If the argument is true, the destination attribute
is locked after making the connection. If the argument is false,
the connection is unlocked before making the connection.

---
nextAvailable(na): boolean
    properties: create
    If the destination multi-attribute has set the indexMatters
to be false with this flag specified, a connection is made to
the next available index. No index need be specified.

---
referenceDest(rd): string
    properties: create
    This flag is used for file io only. The flag indicates that
the connection replaces a connection made in a
referenced file, and the flag argument indicates the original
destination from the referenced file. This
flag is used so that if the reference file is modified, maya
can still attempt to make the appropriate connections in the
main scene to the referenced object.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/connectAttr.html 
    """


def connectControl(flagfileName: boolean, flagindex: uint, flagpreventContextualMenu: boolean, flagpreventOverride: boolean) -> None:
    """Synopsis:
---
---
 connectControl(
string attribute...
    , [fileName=boolean], [index=uint], [preventContextualMenu=boolean], [preventOverride=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

connectControl is undoable, NOT queryable, and NOT editable.index
This command sets up a two-way connection between the control
and the (first-specified) attribute. If this first attribute is
changed in any way, the control will be appropriately updated to match
its value.

Summary: if you change the control, ALL the connected attributes
change. If you change the FIRST attribute attached to the control,
then the control will change.

NOTE: the two-way connection will not be established if the attributes
do not exist when the connectControl command is run. If the
user later uses the control, the connection will be established at
that time.

To effectively use connectControl with radioCollections and
optionMenus, you must attach a piece of data to each radioButton and
menuItem. This piece of data (an integer) can be attached using the
data flag in the radioButton and menuItem
commands. When the button/item is selected, the attribute will be set
to the value of its data. When the attribute is changed, the
collection (or optionMenu) will switch to the item that matches the
new attribute value. If no item matches, it will be left unchanged.

There are some specialized controls that have connection capability
(and more) built right into them. See attrFieldSliderGrp,
attrFieldGrp, and attrColorSliderGrp. Using these classes can be
easier than using connectControl.




Example:
---
import maya.cmds as cmds

sphereNames = cmds.sphere()
sphereName = sphereNames[0]
window = cmds.window()
cmds.columnLayout()
cmds.text( l='X Value:' )
cmds.floatField( 'xx' )
cmds.connectControl( 'xx', '%s.tx' % sphereName )
cmds.text( l='Visibility' )
cmds.checkBox( 'vis' )
cmds.connectControl( 'vis', '%s.visibility' % sphereName )
cmds.floatFieldGrp( 'rot', l='Rotation:', numberOfFields=3 )
index 1 would be the text label
cmds.connectControl( 'rot', '%s.rx' % sphereName, index=2 )
cmds.connectControl( 'rot', '%s.ry' % sphereName, index=3 )
cmds.connectControl( 'rot', '%s.rz' % sphereName, index=4 )
cmds.showWindow( window )

Connecting two attributes to a single control
---

cmds.window()
cmds.columnLayout()
cmds.floatSlider( 'slider' )
cmds.showWindow()

cmds.polySphere()
cmds.polyCube()
cmds.move( 0, 2, 0 )
cmds.connectControl( 'slider', 'pCube1.tx', 'pSphere1.tx' )

---


Flags:
---


---
fileName(fi): boolean
    properties: create
    This flag causes the connection to be treated as a
filename, and the conversion from internal to external
filename representation is made as the data is
copied. This only applies to connections to Tfield
controls.

---
index(index): uint
    properties: create
    This flag enables you to pick out a sub-control from a
group that contains a number of different controls.
For example, you can connect one field of a
floatFieldGrp.  You must count each member of the
group, including any text labels that may exist.  For
example, if you have a check box group with a label,
the label will count as index 1, and the first check
box as index 2.  (Indices are 1-based)

---
preventContextualMenu(pcm): boolean
    properties: create
    If true, this flag will block the right mouse button menu
of the associated control attribute.

---
preventOverride(po): boolean
    properties: create
    If true, this flag disallows overriding the control's
attribute via the control's right mouse button menu.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/connectControl.html 
    """


def connectDynamic(flagaddScriptHandler: script, flagcollisions: string, flagdelete: boolean, flagemitters: string, flagfields: string, flagremoveScriptHandler: int) -> string:
    """Synopsis:
---
---
 connectDynamic(
[objects]
    , [addScriptHandler=script], [collisions=string], [delete=boolean], [emitters=string], [fields=string], [removeScriptHandler=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

connectDynamic is undoable, NOT queryable, and NOT editable.
Connections are made to individual fields, emitters, collisions.  So, if
an object owns several fields, if the user wants some of the fields to
affect an object, s/he can specify each field with a "-f" flag; but if
the user wants to connect all the fields owned by an object, s/he can
specify the object name with the "-f" flag. The same is true for
emitters and collisions.
Different connection types (i.e., for fields vs. emitters)
between the same pair of objects are logically
independent. In other words, an
object can be influenced by another object's fields without being
influenced by its emitters or collisions.

Each connected object must be a dynamic object. The object connected to
can be any object that
owns fields, emitters, etc.; it need not be dynamic. Objects that can
own influences are particles, geometry objects (nurbs and polys) and
lattices.  You can specify either the shape name or the transform name of
the object to be influenced.




Example:
---
import maya.cmds as cmds

cmds.connectDynamic( 'Book', c='Floor' )
Connects the dynamic object "Book" to the collision model of the
"Floor". This means that the book will collide with and bounce off of
the floor.

cmds.connectDynamic( 'Moon', 'Spaceship', f='Moon' )
Connects dynamic object "Spaceship" to the all fields and emitters
owned by "Moon".

cmds.connectDynamic( 'Spaceship', f='newtonField1' )
Connects dynamic object "Spaceship" to "newtonField1" owned by "Moon".

cmds.connectDynamic( 'Moon', f='newtonField1' )
If the selection list consists of "Spaceship", connects dynamic object
"Spaceship" to "newtonField1" and all emitters owned by "Moon".

cmds.connectDynamic( 'Spaceship', d=True, f='Moon' )
Deletes the field connection between all the fields owned by "Moon" and
"Spaceship". Note that the command establishing the connection need not
be in the undo queue.

cmds.connectDynamic( 'Spaceship', d=True, f='newtonField1' )
Deletes the field connection between "newtonField1" owned by "Moon" and
"Spaceship".

def callback(fields, emitters, collisionObjects, objects):
        '''
        Test callback for intercepting calls to the connectDynamic command
        '''
    print 'Fields: %s' % str(fields)
    print 'Emitters: %s' % str(emitters)
    print 'Collision Objects: %s' % str(collisionObjects)
    print 'Objects: %s' % str(objects)

    Let connectDynamic handle the connection
    return False

handler_id = cmds.connectDynamic(addScriptHandler=callback)
Installs the above handler to intercept calls to the connectDynamic command

cmds.connectDynamic(removeScriptHandler=handler_id)
Remove the above script handler

---
Return:
---


    string: Command result

Flags:
---


---
addScriptHandler(ash): script
    properties: create
    Registers a script that will be given a chance to handle calls to the
dynamicConnect command. This flag allows other dynamics systems to
override the behaviour of the connectDynamic command. You must pass a Python
function as the argument for this flag, and that function must take the
following keyword arguments: fields, emitters, collisionObjects and objects.
The python function must return True if it has handled the call to
connectDynamic. In the case that the script returns true, the connectDynamic
command will not do anything as it assumes that the work was handled by the
script. If all of the callbacks return false, the connectDynamic command will
proceed as normal.

The addScriptHandler flag may not be used with any other flags. When the
flag is used, the command will return a numerical id that can be used to
deregister the callback later (see the removeScriptHandler flag)

---
collisions(c): string
    properties: create, multiuse
    Connects each object to the collision models of the given object.

---
delete(d): boolean
    properties: create
    Deletes existing connections.

---
emitters(em): string
    properties: create, multiuse
    Connects each object to the emitters of the given object.

---
fields(f): string
    properties: create, multiuse
    Connects each object to the fields of the given object.

---
removeScriptHandler(rsh): int
    properties: create
    This flag is used to remove a callback that was previously registered
with the addScriptHandler flag. The argument to this flag is the numerical
id returned by dynamicConnect when the addScriptHandler flag was used.
If this flag is called with an invalid id, then the command will do
nothing.

This flag may not be used with any other flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/connectDynamic.html 
    """


def connectJoint(flagconnectMode: boolean, flagparentMode: boolean) -> None:
    """Synopsis:
---
---
 connectJoint(
[objects]
    , [connectMode=boolean], [parentMode=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

connectJoint is undoable, NOT queryable, and NOT editable.
Note1: The first selected joint must be the root of a skeleton.
The second selected joint must have a parent.

Note2: If a joint name is specified in the command line, it is used as the
child and the first selected joint will be the parent. If no joint
name is given at the command line, two joints must be selected.




Example:
---
import maya.cmds as cmds

make joint1 a child of joint4.
---

cmds.connectJoint( 'joint1', 'joint4', pm=True )

make joint1 a child of joint4's parent
---

cmds.connectJoint( 'joint1', 'joint4', cm=True )

---


Flags:
---


---
connectMode(cm): boolean
    properties: create
    The first selected joint will be parented under the parent of the
second selected joint.

---
parentMode(pm): boolean
    properties: create
    The first selected joint will be parented under the second selected
joint. Both joints will be in the active list(selection list).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/connectJoint.html 
    """


def connectionInfo(flagdestinationFromSource: boolean, flaggetExactDestination: boolean, flaggetExactSource: boolean, flaggetLockedAncestor: boolean, flagisDestination: boolean, flagisExactDestination: boolean, flagisExactSource: boolean, flagisLocked: boolean, flagisSource: boolean, flagsourceFromDestination: boolean) -> boolean | list[string] | string:
    """Synopsis:
---
---
 connectionInfo(
string
    , [destinationFromSource=boolean], [getExactDestination=boolean], [getExactSource=boolean], [getLockedAncestor=boolean], [isDestination=boolean], [isExactDestination=boolean], [isExactSource=boolean], [isLocked=boolean], [isSource=boolean], [sourceFromDestination=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

connectionInfo is undoable, NOT queryable, and NOT editable.connectionInfo



Example:
---
import maya.cmds as cmds

   Create a sphere and a cone and make the Z translation of the cone
   be dependent on the X translation of the sphere.
---

cone = cmds.cone()
sphere = cmds.sphere()
sphereTx = '%s.tx' % sphere[0]
coneTz = '%s.tz' % cone[0]
cmds.connectAttr(sphereTx, coneTz)

   Verify the connection and print out the source plug.
---

if cmds.connectionInfo( coneTz, isDestination=True):
  print( 'Source: %s' % cmds.connectionInfo(coneTz,sourceFromDestination=True) )

   Verify the connection and print out the destination plug.
---

if cmds.connectionInfo( sphereTx, isSource=True):
  destinations = cmds.connectionInfo(sphereTx, destinationFromSource=True)
  for destination in destinations:
    print destination

---
Return:
---


    boolean: When asking for a property, depending on the flags used.
    string: When asking for a plug name.
    list[string]: When asking for a list of plugs.

Flags:
---


---
destinationFromSource(dfs): boolean
    properties: create
    If the specified plug (or its ancestor) is a source, this flag returns
the list of destinations connected from the source. (array of strings,
empty array if none)

---
getExactDestination(ged): boolean
    properties: create
    If the plug or its ancestor is connection destination, this returns the
name of the plug that is the exact destination. (empty string if there
is no such connection).

---
getExactSource(ges): boolean
    properties: create
    If the plug or its ancestor is a connection source, this returns the
name of the plug that is the exact source. (empty string if there is
no such connection).

---
getLockedAncestor(gla): boolean
    properties: create
    If the specified plug is locked, its name is returned.  If an
ancestor of the plug is locked, its name is returned.  If more
than one ancestor is locked, only the name of the closest one
is returned.  If neither this plug nor any ancestors are locked,
an empty string is returned.

---
isDestination(id): boolean
    properties: create
    Returns true if the plug (or its ancestor) is the destination
of a connection, false otherwise.

---
isExactDestination(ied): boolean
    properties: create
    Returns true if the plug is the exact destination of a connection,
false otherwise.

---
isExactSource(ies): boolean
    properties: create
    Returns true if the plug is the exact source of a connection,
false otherwise.

---
isLocked(il): boolean
    properties: create
    Returns true if this plug (or its ancestor) is locked

---
isSource(isSource): boolean
    properties: create
    Returns true if the plug (or its ancestor) is the source of a
connection, false otherwise.

---
sourceFromDestination(sfd): boolean
    properties: create
    If the specified plug (or its ancestor) is a destination, this flag returns
the source of the connection. (string, empty if none)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/connectionInfo.html 
    """


def constrain(flagbarrier: boolean, flagdamping: float, flagdirectionalHinge: boolean, flaghinge: boolean, flaginterpenetrate: boolean, flagnail: boolean, flagname: string, flagorientation: tuple[float, float, float], flagpinConstraint: boolean, flagposition: tuple[float, float, float], flagrestLength: float, flagspring: boolean, flagstiffness: float) -> None:
    """Synopsis:
---
---
 constrain([barrier=boolean], [damping=float], [directionalHinge=boolean], [hinge=boolean], [interpenetrate=boolean], [nail=boolean], [name=string], [orientation=[float, float, float]], [pinConstraint=boolean], [position=[float, float, float]], [restLength=float], [spring=boolean], [stiffness=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

constrain is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

"Nail" a rigid body at position <<0.0, 2.5, 0.0>>
---

cmds.constrain( 'rigidBody1', nail=True, p=(0, 2.5, 0) )

"Pin" two rigid bodies together at the position <<0.0, 2.5, 0.0>>.
---

cmds.constrain( 'rigidBody1', 'rigidBody2', pin=True, n='pin', p=(0, 2.5, 0) )

"Hinge" a rigid body at the position <<0.0, 2.5, 0.0>>.
---

cmds.constrain( 'rigidBody1', hinge=True, p=(0, 2.5, 0) )

Create a barrier for a rigid body which will not allow the rigid body
to fall below (in y by default) the plane defined by the
barrier point <<0.0, 2.5, 0.0>>.
---

cmds.constrain( 'rigidBody1', barrier=True, p=(0, 2.5, 0) )

Add a "Spring" to a rigid body at the position <<0.0, 2.5, 0.0>>
connected on the rigid body at point <<0, 0, 0>>
---

cmds.constrain( 'rigidBody1', spring=True, name='spring', p=(0, 2.5, 0), rl=1.0 )

---


Flags:
---


---
barrier(br): boolean
    properties: create, query
    Creates a barrier constraint.  This command requires one rigid bodies.

---
damping(d): float
    properties: create, query, edit
    Sets the damping constant.
Default value: 0.1
Range: -1000.0 to 1000.0

---
directionalHinge(dhi): boolean
    properties: create, query
    Creates a directional hinge constraint.  This command requires two rigid bodies.
The directional hinge always maintains the initial direction of its axis.

---
hinge(hi): boolean
    properties: create, query
    Creates a hinge constraint.  This command requires one or two rigid bodies.

---
interpenetrate(i): boolean
    properties: create, query, edit
    Allows (or disallows) the rigid bodies defined in the constrain to ipenetrate.

---
nail(na): boolean
    properties: create, query
    Creates a nail constraint.  This command requires one rigid body.

---
name(n): string
    properties: create, query, edit
    Names the rigid constraint.

---
orientation(o): [float, float, float]
    properties: create, query, edit
    Set initial orientation of the constraint in world space.  This
command is only valid with hinge and barrier constraints
Default value: 0.0 0.0 0.0

---
pinConstraint(pin): boolean
    properties: create, query
    Creates a pin constraint.  This command requires two rigid bodies.

---
position(p): [float, float, float]
    properties: create, query, edit
    Set initial position of the constraint in world space.
Default value: 0.0 0.0 0.0 for uni-constraints, midpoint of bodies for deul constraint.

---
restLength(rl): float
    properties: create, query, edit
    Sets the rest length.
Default value: 1.0

---
spring(s): boolean
    properties: create, query
    Creates a spring constraint.  This command requires one or two rigidies.

---
stiffness(st): float
    properties: create, query, edit
    Sets the springs stiffness constant.
Default value: 5.0

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/constrain.html 
    """


def constructionHistory(flagtoggle: boolean) -> None:
    """Synopsis:
---
---
 constructionHistory([toggle=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

constructionHistory is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.constructionHistory( tgl=True )
cmds.constructionHistory( tgl=False )

Returns true if construction history is on.
Returns false if construction history is off.
cmds.constructionHistory( q=True, tgl=True )

---


Flags:
---


---
toggle(tgl): boolean
    properties: create, query
    Turns construction history on or off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/constructionHistory.html 
    """


def container(flagaddNode: list[string], flagasset: list[string], flagassetMember: string, flagbindAttr: tuple[string, string], flagconnectionList: boolean, flagcurrent: boolean, flagfileName: list[string], flagfindContainer: list[string], flagforce: boolean, flagincludeHierarchyAbove: boolean, flagincludeHierarchyBelow: boolean, flagincludeNetwork: boolean, flagincludeNetworkDetails: string, flagincludeShaders: boolean, flagincludeShapes: boolean, flagincludeTransform: boolean, flagisContainer: boolean, flagname: string, flagnodeList: boolean, flagnodeNamePrefix: boolean, flagparentContainer: boolean, flagpreview: boolean, flagpublishAndBind: tuple[string, string], flagpublishAsChild: tuple[string, string], flagpublishAsParent: tuple[string, string], flagpublishAsRoot: tuple[string, boolean], flagpublishAttr: string, flagpublishConnections: boolean, flagpublishName: string, flagremoveContainer: boolean, flagremoveNode: list[string], flagtype: string, flagunbindAndUnpublish: string, flagunbindAttr: tuple[string, string], flagunbindChild: string, flagunbindParent: string, flagunpublishChild: string, flagunpublishName: string, flagunpublishParent: string, flagunsortedOrder: boolean) -> string:
    """Synopsis:
---
---
 container(
[string...]
    , [addNode=string[]], [asset=string[]], [assetMember=string], [bindAttr=[string, string]], [connectionList=boolean], [current=boolean], [fileName=string[]], [findContainer=string[]], [force=boolean], [includeHierarchyAbove=boolean], [includeHierarchyBelow=boolean], [includeNetwork=boolean], [includeNetworkDetails=string], [includeShaders=boolean], [includeShapes=boolean], [includeTransform=boolean], [isContainer=boolean], [name=string], [nodeList=boolean], [nodeNamePrefix=boolean], [parentContainer=boolean], [preview=boolean], [publishAndBind=[string, string]], [publishAsChild=[string, string]], [publishAsParent=[string, string]], [publishAsRoot=[string, boolean]], [publishAttr=string], [publishConnections=boolean], [publishName=string], [removeContainer=boolean], [removeNode=string[]], [type=string], [unbindAndUnpublish=string], [unbindAttr=[string, string]], [unbindChild=string], [unbindParent=string], [unpublishChild=string], [unpublishName=string], [unpublishParent=string], [unsortedOrder=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

container is undoable, queryable, and editable.
 add and remove nodes from the container
 publish attributes from nodes inside the container
 replace the connections and values from one container onto another one
 remove a container without removing its member nodes




Example:
---
import maya.cmds as cmds

Create a container holding a locator transform only (not its shape)
---

loc = cmds.spaceLocator()
con1 = cmds.container(addNode=[loc[0]])

Select the nodes that would be in the container, but don't create it
---

cmds.container(preview=True,addNode=[cone[0]],includeNetwork=True,includeHierarchyBelow=True)


Create a container holding a polygon shape, its transform and its
history node. Publish its tx attr.
---

cone = cmds.polyCone()
con2 = cmds.container(addNode=[cone[0]],includeNetwork=True,includeHierarchyBelow=True)

Publish the cone's tx and the locator's tx with the same name
---

cmds.container(con1,edit=True,publishName='main_tx')
cmds.container(con1,edit=True,bindAttr=['%s.tx' % loc[0],'main_tx'])
cmds.container(con2,edit=True,publishName='main_tx')
cmds.container(con2,edit=True,bindAttr=['%s.tx' % cone[0],'main_tx'])

Publish the name "sam", but don't bind it to anything
---

cmds.container(con1,edit=True,publishName='sam')

Query the bound publications
---

cmds.container(con1,query=True,bindAttr=1)
Result: [u'locator1.translateX', u'main_tx'] ---


Query all the published names:
---

cmds.container(con1,query=True,publishName=1)
Result: [u'main_tx' u'sam'] ---


Query just the bound published names:
---

cmds.container(con1,query=True,publishName=1,bindAttr=1)
Result: [u'main_tx'] ---


Query just the unbound published names:
---

cmds.container(con1,query=True,publishName=1,unbindAttr=1)
Result: [u'sam'] ---


Query just the published name for the published attribute locator1.translateX
---

cmds.container(con1,query=True,publishName=1,publishAttr='locator1.translateX')
Result: [u'main_tx'] ---


keyframe the cone's tx
---

cmds.currentTime(0)
coneTx = '%s.tx' % cone[0]
cmds.setKeyframe(coneTx)
cmds.currentTime(4)
cmds.setAttr(coneTx,10.0)
cmds.setKeyframe(coneTx)

Query the nodes in the container
---

nodes = cmds.container(con2,query=True,nodeList=True)

Remove a node from the container
---

cmds.container(con2,edit=True,removeNode=nodes[2])

Remove the container without deleting the nodes within it
---

cmds.container(con2,edit=True,removeContainer=True)

query a referenced scenes for its assets
---

cmds.container(q=True,fileName='C:/My Documents/maya/projects/default/scenes/refFile.mb')

---
Return:
---


    string: Name of the node created.

Flags:
---


---
addNode(an): string[]
    properties: create, edit
    Specifies the list of nodes to add to container.

---
asset(a): string[]
    properties: query
    When queried, if all the nodes in nodeList belong to the same container, returns container's name.
Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.

---
assetMember(am): string
    properties: query
    Can be used during query in conjunction with the bindAttr flag to query
for the only published attributes related to the specified node within the
container.
      In query mode, this flag needs a value.

---
bindAttr(ba): [string, string]
    properties: query, edit
    Bind a contained attribute to an unbound published name on the interface of the
container; returns a list of bound published names.
The first string specifies the node and attribute name to be
bound in "node.attr" format. The second string specifies the name of the
unbound published name. In query mode, returns a string array of the published
names and their corresponding attributes. The flag can also be used in query
mode in conjunction with the -publishName, -publishAsParent, and
-publishAsChild flags.

---
connectionList(cl): boolean
    properties: query
    Returns a list of the exterior connections to the container node.

---
current(c): boolean
    properties: create, query, edit
    In create mode, specify that the newly created asset should be current.
In edit mode, set the selected asset as current. In query, return the
current asset.

---
fileName(fn): string[]
    properties: query
    Used to query for the assets associated with a given file name.
      In query mode, this flag needs a value.

---
findContainer(fc): string[]
    properties: query
    When queried, if all the nodes in nodeList belong to the same container, returns container's name.
Otherwise returns empty string.
      In query mode, this flag needs a value.

---
force(f): boolean
    properties: create, edit
    This flag can be used in conjunction with -addNode and -removeNode flags only.
If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one.
If specified with -removeNode, nodes will be removed from all containers, instead of remaining in the parent container if being removed from a nested container.

---
includeHierarchyAbove(iha): boolean
    properties: create, edit
    Used to specify that the parent hierarchy of the supplied node list should
also be included in the container (or deleted from the container). Hierarchy
inclusion will stop at
nodes which are members of other containers.

---
includeHierarchyBelow(ihb): boolean
    properties: create, edit
    Used to specify that the hierarchy below the supplied node list should
also be included in the container (or delete from the container). Hierarchy
inclusion will stop at
nodes which are members of other containers.

---
includeNetwork(inc): boolean
    properties: create, edit
    Used to specify that the node network connected to supplied node list
should also be included in the container.
Network traversal will stop at default nodes and nodes which are members of
other containers.

---
includeNetworkDetails(ind): string
    properties: create, edit, multiuse
    Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even when constraints are not specified as an input.

---
includeShaders(isd): boolean
    properties: create, edit
    Used to specify that for any shapes included, their shaders will
also be included in the container.

---
includeShapes(ish): boolean
    properties: create, edit
    Used to specify that for any transforms selected, their direct child shapes
will be included in the container (or deleted from the container). This flag
is not necessary when
includeHierarchyBelow is used since the child shapes and all other
descendents will automatically be included.

---
includeTransform(it): boolean
    properties: create, edit
    Used to specify that for any shapes selected, their parent transform
will be included in the container (or deleted from the container).
This flag is not necessary when
includeHierarchyAbove is used since the parent transform and
all of its parents will automatically be included.

---
isContainer(isc): boolean
    properties: query
    Return true if the selected or specified node is a container node.
If multiple containers are queried, only the state of the first will be
returned.

---
name(n): string
    properties: create
    Sets the name of the newly-created container.

---
nodeList(nl): boolean
    properties: query
    When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container.
This will also display any reordering done with the reorderContainer command.

---
nodeNamePrefix(nnp): boolean
    properties: create, edit
    Specifies that the name of published attributes should be of the form "node_attr".
Must be used with the -publishConnections/-pc flag.

---
parentContainer(par): boolean
    properties: query
    Flag to query the parent container of a specified container.

---
preview(p): boolean
    properties: create
    This flag is valid in create mode only. It indicates that you do not
want the container to be created, instead you want to preview its contents.
When this flag is used, Maya will select the
nodes that would be put in the container if you did create the
container. For example you can see what would go into the container
with -includeNetwork, then modify your selection as desired, and do a
create container with the selected objects only.

---
publishAndBind(pb): [string, string]
    properties: edit
    Publish the given name and bind the attribute to the given name.
First string specifies the node and attribute name in "node.attr" format.
Second string specifies the name it should be published with.

---
publishAsChild(pac): [string, string]
    properties: query, edit
    Publish contained node to the interface of the container to indicate it can
be a child of external nodes. The second string is the name of the published
node. In query mode, returns a string of the published names and the
corresponding nodes. If -publishName flag is used in query mode, only
returns the published names; if -bindAttr flag is used in query mode, only
returns the name of the published nodes.

---
publishAsParent(pap): [string, string]
    properties: query, edit
    Publish contained node to the interface of the container to indicate it can
be a parent to external nodes. The second string is the name of the published
node. In query mode, returns a string of array of the published names and
the corresponding nodes. If -publishName flag is used in query mode, only
returns the published names; if -bindAttr flag is used in query mode, only
returns the name of the published nodes.

---
publishAsRoot(pro): [string, boolean]
    properties: query, edit
    Publish or unpublish a node as a root. The significance of root transform
node is twofold. When container-centric selection is enabled, the root
transform will be selected if a container node in the hierarchy below it is
selected in the main scene view. Also, when exporting a container proxy,
any published root transformation attributes such as translate, rotate or
scale will be hooked up to attributes on a stand-in node.
In query mode, returns the node that has been published as root.

---
publishAttr(pa): string
    properties: query
    In query mode, can only be used with the -publishName(-pn) flag, and takes
an attribute as an argument; returns the published name of the attribute, if
any.
      In query mode, this flag needs a value.

---
publishConnections(pc): boolean
    properties: create, edit
    Publish all connections from nodes inside the container to nodes outside
the container.

---
publishName(pn): string
    properties: query, edit
    Publish a name to the interface of the container, and returns the actual name
published to the interface.  In query mode, returns the
published names for the container. If the -bindAttr flag is specified, returns
only the names that are bound; if the -unbindAttr flag is specified, returns
only the names that are not bound; if the -publishAsParent/-publishAsChild
flags are specified, returns only names of published parents/children.
if the -publishAttr is specified with an attribute argument in the "node.attr"
format, returns the published name for that attribute, if any.

---
removeContainer(rc): boolean
    properties: edit
    Disconnects all the nodes from container and deletes container node.

---
removeNode(rn): string[]
    properties: edit
    Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.

---
type(typ): string
    properties: create, query
    By default, a container node will be created. Alternatively, the
type flag can be used to indicate that a different type of container
should be created. At the present time, the only other valid type of
container node is "dagContainer".

---
unbindAndUnpublish(ubp): string
    properties: edit
    Unbind the given attribute (in "node.attr" format) and unpublish its associated name.
Unbinding a compound may trigger unbinds of its compound parents/children. So the
advantage of using this one flag is that it will automatically unpublish the names
associated with these automatic unbinds.

---
unbindAttr(ua): [string, string]
    properties: query, edit
    Unbind a published attribute from its published name on the interface of the
container, leaving an unbound published name on the interface of the
container; returns a list of unbound published names.
The first string specifies the node and attribute name to be
unbound in "node.attr" format, and the second string specifies the name of
the bound published name. In query mode, can only be used with the -publishName,
-publishAsParent and -publishAsChild flags.

---
unbindChild(unc): string
    properties: edit
    Unbind the node published as child, but do not remove its published name
from the interface of the container.

---
unbindParent(unp): string
    properties: edit
    Unbind the node published as parent, but do not remove its published name
from the interface of the container.

---
unpublishChild(upc): string
    properties: edit
    Unpublish node published as child from the interface of the container

---
unpublishName(un): string
    properties: edit
    Unpublish an unbound name from the interface of the container.

---
unpublishParent(upp): string
    properties: edit
    Unpublish node published as parent from the interface of the container

---
unsortedOrder(uso): boolean
    properties: query
    This flag has no effect on the operation of the container command (OBSOLETE).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/container.html 
    """


def containerBind(flagallNames: boolean, flagbindingSet: string, flagbindingSetConditions: boolean, flagbindingSetList: boolean, flagforce: boolean, flagpreview: boolean) -> None:
    """Synopsis:
---
---
 containerBind([allNames=boolean], [bindingSet=string], [bindingSetConditions=boolean], [bindingSetList=boolean], [force=boolean], [preview=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

containerBind is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


query the template binding sets available for this container
---

cmds.containerBind(container1, query=1, bindingSetList=1)

attempt to bind published names on the container
using matching information in the bindingSet specified.
By default only unbound names are considered.
---

cmds.containerBind(container1, bindingSet="MayaBindings")

Attempt to bind all published names on the container
using matching information in the bindingSet specified.
Previously bound names will only be re-bound if the bindingSet
produces an appropriate match.
---

cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1)

Forcibly re-bind all published names on the container
using matching information in the bindingSet specified.
All previously bound names will be unbound and will only
be re-bound if the binding set produces an appropriate match.
---

cmds.containerBind(container1, bindingSet="MayaBindings", allNames=1, force=1)

preview what the results of a binding operation would be, but do
not actually perform it.
cmds.containerBind(container1, bindingSet="MayaBindings", preview=1, allNames=1, force=1)

---


Flags:
---


---
allNames(all): boolean
    properties: create
    Specifies that all published names on the container should be considered
during the binding operation.  By default only unbound published names
will be operated on.  Additionally specifying the 'force' option with 'all'
will cause all previously bound published names to be reset (or unbound)
before the binding operation is performed; in the event that there is no
appropriate binding found for the published name, it will be left in the
unbound state.

---
bindingSet(bs): string
    properties: query
    Specifies the name of the template binding set to use for the bind or
query operation.
This flag is not available in query mode.
                        In query mode, this flag needs a value.

---
bindingSetConditions(bsc): boolean
    properties: query
    Used in query mode, returns a list of binding set condition entries from the
specified template binding set.  The list returned is composed of
of all published name / condition string pairs for each entry in the
binding set.
This flag returns all entries in the associated binding set and does not take
into account the validity of each entry with respect to the container's
list of published names, bound or unbound state, etc.

---
bindingSetList(bsl): boolean
    properties: query, edit
    Used in query mode, returns a list of available binding sets that
are defined on the associated container template.

---
force(f): boolean
    properties: create
    This flag is used to force certain operations to proceed that would normally
not be performed.

---
preview(p): boolean
    properties: create
    This flag will provide a preview of the results of a binding operation but
will not actually perform it.  A list of publishedName/boundName
pairs are returned for each published name that would be affected by the
binding action.
If the binding of a published name will not change as a result of the action it
will not be listed.
Published names that were bound but will become unbound are also listed,
in this case the associated boundName will be indicated by an empty string.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/containerBind.html 
    """


def containerProxy(flagfromTemplate: string, flagtype: string) -> None:
    """Synopsis:
---
---
 containerProxy([fromTemplate=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

containerProxy is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


create a proxy for container1
---

cmds.containerProxy('container1')

---


Flags:
---


---
fromTemplate(ft): string
    properties: create
    Specifies the name of a template file which will be used to create the new
container proxy. Stand-in attributes will be created and published for all
the numeric attributes on the proxy.

---
type(typ): string
    properties: create
    Specifies the type of container node to use for the proxy. This flag is only
valid in conjunction with the fromTemplate flag. When creating a proxy for an
existing container, the type created will always be identical to that of the source
container. The default value for this flag is 'container'.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/containerProxy.html 
    """


def containerPublish(flagbindNode: tuple[string, string], flagbindTemplateStandins: boolean, flaginConnections: boolean, flagmergeShared: boolean, flagoutConnections: boolean, flagpublishNode: tuple[string, string], flagunbindNode: string, flagunpublishNode: string) -> None:
    """Synopsis:
---
---
 containerPublish([bindNode=[string, string]], [bindTemplateStandins=boolean], [inConnections=boolean], [mergeShared=boolean], [outConnections=boolean], [publishNode=[string, string]], [unbindNode=string], [unpublishNode=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

containerPublish is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


create a proxy for container1
---

cmds.containerPublish(container1,inConnections=True,mergeShared=True)

add a published name 'mainShader' of type 'objectSet'
---

cmds.containerPublish(container1,publishNode=['mainShadingSet','objectSet']

bind a shading group to the published name
---

containerPublish -bindNode "mainShadingSet" blinn1SG container1;

query what is bound
---

container -q -bindNode container1;

unbind the shading group
---

containerPublish -unbindNode "mainShadingSet" container1;

---


Flags:
---


---
bindNode(bn): [string, string]
    properties: create, query, edit
    Bind the specified node to the published node name.

---
bindTemplateStandins(bts): boolean
    properties: create, query, edit
    This flag will create a temporary stand-in attribute for any
attributes that exist in the template but are not already bound.
This enables you to set values for unbound attributes.

---
inConnections(ic): boolean
    properties: create
    Specifies that the unpublished connections to nodes in the container
from external nodes should be published.

---
mergeShared(ms): boolean
    properties: create
    For use with the inConnections flag. Indicates that when an external
attribute connects to multiple internal attributes within the container, a
single published attribute should be used to correspond to all of the
internal attributes.

---
outConnections(oc): boolean
    properties: create
    Specifies that the unpublished connections from nodes in the container
to external nodes should be published.

---
publishNode(pn): [string, string]
    properties: create, query, edit
    Publish a name and type. When first published, nothing will be bound.
To bind a node to the published name, use the bindNode flag.

---
unbindNode(ubn): string
    properties: create, query, edit
    Unbind the node that is published with the name specified by the flag.

---
unpublishNode(upn): string
    properties: create, query, edit
    Unpublish the specified published node name.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/containerPublish.html 
    """


def containerTemplate(flagaddBindingSet: string, flagaddNames: boolean, flagaddView: string, flagallKeyable: boolean, flagattribute: string, flagattributeList: string, flagbaseName: string, flagbindingSetList: string, flagchildAnchor: boolean, flagdelete: boolean, flagexists: boolean, flagexpandCompounds: boolean, flagfileName: string, flagforce: boolean, flagfromContainer: string, flagfromSelection: boolean, flaglayoutMode: int, flagload: boolean, flagmatchFile: string, flagmatchName: string, flagparentAnchor: boolean, flagpublishedNodeList: string, flagremoveBindingSet: string, flagremoveView: string, flagrootTransform: boolean, flagsave: boolean, flagsearchPath: string, flagsilent: boolean, flagtemplateList: string, flagunload: boolean, flagupdateBindingSet: string, flaguseHierarchy: boolean, flagviewList: string) -> None:
    """Synopsis:
---
---
 containerTemplate([addBindingSet=string], [addNames=boolean], [addView=string], [allKeyable=boolean], [attribute=string], [attributeList=string], [baseName=string], [bindingSetList=string], [childAnchor=boolean], [delete=boolean], [exists=boolean], [expandCompounds=boolean], [fileName=string], [force=boolean], [fromContainer=string], [fromSelection=boolean], [layoutMode=int], [load=boolean], [matchFile=string], [matchName=string], [parentAnchor=boolean], [publishedNodeList=string], [removeBindingSet=string], [removeView=string], [rootTransform=boolean], [save=boolean], [searchPath=string], [silent=boolean], [templateList=string], [unload=boolean], [updateBindingSet=string], [useHierarchy=boolean], [viewList=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

containerTemplate is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


   Create a container template.
---

cmds.containerTemplate( 'characterRig' )

Create a container template using the published attribute information from
container1.
cmds.containerTemplate ('characterRig', fromContainer='container1')
---

Save the template to a template file in the default template location.
cmds.containerTemplate ('characterRig', save=True)
Load a template (the template is located along the template search path)
cmds.containerTemplate ('characterRig', load=True)
Re-load a template that has already been loaded
This is useful if you have made edits to the template outside of maya
cmds.containerTemplate ('characterRig', force=True, load=True)
Determine the file that a template was loaded from
cmds.containerTemplate ('characterRig', query=True, fileName=True)
Result: C:/myTemplates/characterRig.template ---

---

Add a view to a container template. This view will be generated from the
given container, and will use a group-by-node hierarchical layout.
The view can be subesequently customized if desired.
---

cmds.containerTemplate ('characterRig', edit=True, addView='newView', fromContainer='container1', layoutMode=1)
cmds.containerTemplate ('characterRig', save=True)
---

Add another view to a container template.
This view will be generated with a default layout and can be
subsequently customized.
---

cmds.containerTemplate ('characterRig', edit=True, addView="newView2")
cmds.containerTemplate ('characterRig', save=True)
---

Get the list of attributes in the template.  This will return
a flat list of attribute names in the order in which they appear
in the template definition.
---

cmds.containerTemplate ('characterRig', query=True, attributeList=True)
Result: [u'attribute1', u'attribute2', u'attribute3'] ---

---

List all loaded templates
list = cmds.containerTemplate(query=True, templateList=True)
Result: [u'Object', u'characterRig'] ---

---

List all templates matching a a given template name
Note that all templates with matching base name (in any package) will
be returned.
cmds.containerTemplate (query=True, templateList=True, matchName='characterRig')
Result: [u'characterRig'] ---

---


---


Flags:
---


---
addBindingSet(abs): string
    properties: create, edit
    This argument is used to add a new binding set with the given name to a template.
A default binding set will be created. If the binding set already exists, the
force flag must be used to replace the existing binding set.
When used with the fromContainer option, default bindings will be entered based
on the current bindings of the designated container.
When used without a reference container, the binding set will be made with
placeholder entries.
The template must be saved before the new binding set is permanently stored with
the template file.

---
addNames(an): boolean
    properties: edit
    In edit mode, when used with the fromContainer flag, any published name on the
container not present as an attribute on the template will be added to the
template.

---
addView(av): string
    properties: create, edit
    This argument is used to add a new view with the given name to a template.
By default a view containing a flat list of all template attributes
will be created.  The layoutMode flag provides more layout options.
The template must be saved before the new view is permanently stored with
the template file.

---
allKeyable(ak): boolean
    properties: create, edit
    Used when the fromSelection flag is true and fromContainer is false. If true we will use
all keyable attributes to define the template or the view, if false we use the attributes
passed in with the attribute flag.

---
attribute(at): string
    properties: create, edit, multiuse
    If fromSelection is true and allKeyable is false, this
attribute name will be used to create an attribute item in the template file.

---
attributeList(al): string
    properties: create, query, edit
    Used in query mode, returns a list of attributes contained in the
template definition.

---
baseName(bn): string
    properties: create, query
    Used in query mode, returns the base name of the template.
The basename is the template name with any package qualifiers stripped off.

---
bindingSetList(bsl): string
    properties: create, query
    Used in query mode, returns a list of all binding sets defined on the template.

---
childAnchor(can): boolean
    properties: create, query
    This flag can be optionally specified when querying the publishedNodeList.
The resulting list will contain only childAnchor published nodes.

---
delete(d): boolean
    properties: create
    Delete the specified template and its file.
All objects that are associated with this template or contained in the
same template file will be deleted.
To simply unload a template without permanently deleting its file,
use unload instead.

---
expandCompounds(ec): boolean
    properties: create, edit
    This argument is used to determine how compound parent attributes
and their children will be added to generated views when both are published
to the container.
When true, the compound parent and all compound child attributes published to the
container will be included in the view.
When false, only the parent attribute is included in the view.
Note: if only the child attributes are published and not the parent, the children
will be included in the view, this flag is only used in the situation where both
parent and child attributes are published to the container.
The default value is false.

---
fromContainer(fc): string
    properties: create
    This argument is used in create or edit mode to specify a container node
to be used for generating the template contents.
In template creation mode, the template definition will be created
based on the list of published attributes in the specified container.
In edit mode, when used with the addNames flag or with no other flag, any
published name on the container not present as an attribute
on the template will be added to the template.
This flag is also used in conjunction with flags such as addView.

---
fromSelection(fs): boolean
    properties: create, edit
    If true, we will use the active selection list to create the template or the view.
If allKeyable is also true then we will create the template from all keyable
attributes in the selection, otherwise we will create the template using the
attributes specified with the attribute flag.

---
layoutMode(lm): int
    properties: create
    This argument is used to specify the layout mode when creating a view.
Values correspond as follows:
0: layout in flat list (default when not creating view from container)
1: layout grouped by node (default if creating view from container)
The fromContainer or fromSelection argument is required to provide the
reference container or selection for layout modes that require node
information.  Note that views can only refer to defined template attributes.
This means that when using the fromContainer or from Selection flag to
add a view to an existing template, only attributes that are defined on
both the template and the container or the current selection will be
included in the view (i.e. published attributes on the container that
are not defined in the template will be ignored).

---
matchName(mn): string
    properties: query
    Used in query mode in conjunction with other flags this flag specifies
an optional template name that is to be matched as part of the query operation.
The base template name is used for matching, any template with the same
basename will be matched even across different packages.
                        In query mode, this flag needs a value.

---
parentAnchor(pan): boolean
    properties: create, query
    This flag can be optionally specified when querying the publishedNodeList.
The resulting list will contain only parentAnchor published nodes.

---
publishedNodeList(pnl): string
    properties: create, query, edit
    Used in query mode, returns a list of published nodes contained in the
template definition.
By default all published nodes on the template will be returned.
The list of published nodes can be limited to only include certain types of
published nodes using one of the childAnchor, parentAnchor or rootTransform flags.
If an optional flag is are specified, only nodes of the specified type
will be returned.

---
removeBindingSet(rbs): string
    properties: create, edit
    This argument is used to remove the named binding set from the template.
The template must be saved before the binding set is permanently removed from
the template file.

---
removeView(rv): string
    properties: create, edit
    This argument is used to remove the named view from the template.
The template must be saved before the view is permanently removed from
the template file.

---
rootTransform(rtn): boolean
    properties: create, query
    This flag can be optionally specified when querying the publishedNodeList.
The resulting list will contain only rootTransform published nodes.

---
save(s): boolean
    properties: create
    Save the specified template to a file.
If a filename is specified for the template, the entire file
(and all templates associated with it) will be saved.
If no file name is specified, a default filename will be assumed,
based on the template name.

---
searchPath(sp): string
    properties: query, edit
    The template searchPath is an ordered list of all locations that are being
searched to locate template files (first location searched to last location
searched).
The template search path setting is stored in the current workspace
and can also be set and queried as the file rule entry for 'templates'
(see the workspace command for more information).
In edit mode, this flag allows the search path setting to be customized.
When setting the search path value, the list should conform to a path list format
expected on the current platform.  This means that paths should be
separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX.
Environment variables can also be used.
Additional built-in paths may be added automatically by maya to the customized
settings.
In query mode, this flag returns the current contents of the search path;
all paths, both customized and built-in, will be included in the query return
value.

---
templateList(tl): string
    properties: query
    Used in query mode, returns a list of all loaded templates.
This query can be used with optional matchFile and matchName flags.
When used with the matchFile flag, the list of templates will be restricted
to those associated with the specified file.  When used with the matchName
flag, the list of templates will be restricted to those matching the specified
template name.

---
updateBindingSet(ubs): string
    properties: create, edit
    This argument is used to update an existing binding set with new bindings.
When used with the fromContainer argument binding set entries with be replaced
or merged in the binding set based on the bindings of the designated container.
If the force flag is used, existing entries in the binding set are replaced
with new values.
When force is not used, only new entries are merged into the binding set,
any existing entries will be left as-is.
When used without a reference container, the binding set will be updated
with placeholder entries.
The template must be saved before the new binding set is permanently stored with
the template file.

---
useHierarchy(uh): boolean
    properties: create, edit
    If true, and the fromSelection flag is set, the selection list will expand
to include it's hierarchy also.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/containerTemplate.html 
    """


def containerView(flagitemInfo: string, flagitemList: boolean, flagviewDescription: boolean, flagviewLabel: boolean, flagviewList: boolean, flagviewName: string) -> None:
    """Synopsis:
---
---
 containerView([itemInfo=string], [itemList=boolean], [viewDescription=boolean], [viewLabel=boolean], [viewList=boolean], [viewName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

containerView is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


Obtain a list of all available views for container1
---

cmds.containerView ( 'container1', query=True, viewList=True);
Result: [u'Animation', u'Rendering'] ---

---

Get a list of view items in the current view for container1
In this example the list returned will include only the name for
each item in the view.
cmds.containerView ( 'container1', itemList=True, itemInfo="itemName", query=True)
Result: [u'RenderSetup', u'color', u'intensity', u'Transform', u'rotateY'] ---

---

Get a list of view items.
In this query the list returned will include the group boolean and label
for each item in the view.
cmds.containerView ( 'container1', itemList=True, itemInfo="itemIsGroup:itemLabel", query=True)
Result: [u'1', u'RenderSetup', u'0', u'Color', u'0', u'Intensity', u'1', u'Transform', u'0', u'Rotate Y'] ---


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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/containerView.html 
    """


def contentBrowser(flagaddContentPath: string, flagcontext: string | tuple[string, ...], flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaghighlightConnection: string, flaglocation: string, flaglockMainConnection: boolean, flagmainListConnection: string, flagpanel: string, flagparent: string, flagpreview: boolean, flagrefreshTreeView: boolean, flagremoveContentPath: string, flagsaveCurrentContext: boolean, flagselectionConnection: string, flagstateString: boolean, flagthumbnailView: boolean, flagtreeView: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 contentBrowser(
[string]
    , [addContentPath=string], [context=[string, [, string, ], [, string, ]]], [control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightConnection=string], [location=string], [lockMainConnection=boolean], [mainListConnection=string], [panel=string], [parent=string], [preview=boolean], [refreshTreeView=boolean], [removeContentPath=string], [saveCurrentContext=boolean], [selectionConnection=string], [stateString=boolean], [thumbnailView=boolean], [treeView=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

contentBrowser is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Create the Content Browser and select library in the Examples tab.
cmds.scriptedPanel('contentBrowserPanel1', edit=True, tearOff=True, label='Content Browser')
panelNames = cmds.getPanel(scriptType='contentBrowserPanel')
panelName = panelNames[0]
panelCompleteName = panelName + 'ContentBrowser'
cmds.contentBrowser(panelCompleteName, edit=True, location='Examples/FX/Fluids/Ocean Examples')

Hide the preview pane.
cmds.contentBrowser(panelCompleteName, edit=True, preview=False)
cmds.scriptedPanel('contentBrowserPanel1', edit=True, tearOff=True, label='Content Browser')

---
Return:
---


    string: The name of the panel

Flags:
---


---
addContentPath(acp): string
    properties: edit
    Adds the given path(s) to the libraries displayed on the Examples tab.
Also updates the corresponding MAYA_CONTENT_PATH environment variable.

---
context(ctx): [string, [, string, ], [, string, ]]
    properties: query, edit
    Sets the default location for the given context. The two optional arguments
(Python only) are the category (tab) and location. To clear the content use
empty strings for category and location.

In query mode, it returns the context of the content browser in an array of 3 strings :
the name of the context, the default category name, the default location.

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
location(loc): string
    properties: edit
    Switches to the Examples tab and selects the given library location.

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
preview(pv): boolean
    properties: edit
    Shows / hides the preview panel.
Note: this flag will not affect the currently opened Content Browser, but only
any subsequently opened ones.

---
refreshTreeView(rtv): boolean
    properties: edit
    Forces a refresh of the Examples tab tree view pane.

---
removeContentPath(rcp): string
    properties: edit
    Removes the given path(s) from the libraries displayed on the Examples tab.
Also updates the corresponding MAYA_CONTENT_PATH environment variable.

---
saveCurrentContext(scc): boolean
    properties: edit
    Saves the context for the current Content Browser tab.

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
thumbnailView(th): boolean
    properties: edit
    Shows / hides the thumbnail panel.
Note: this flag will not affect the currently opened Content Browser, but only
any subsequently opened ones.

---
treeView(tr): boolean
    properties: edit
    Shows / hides the tree view panel.
Note: this flag will not affect the currently opened Content Browser, but only
any subsequently opened ones.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/contentBrowser.html 
    """


def contextInfo(flagc: boolean, flagescapeContext: boolean, flagexists: boolean, flagimage1: boolean, flagimage2: boolean, flagimage3: boolean, flagtitle: boolean) -> string:
    """Synopsis:
---
---
 contextInfo(
[context name]
    , [c=boolean], [escapeContext=boolean], [exists=boolean], [image1=boolean], [image2=boolean], [image3=boolean], [title=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

contextInfo is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a particle tool context, then switch to it
cmds.dynParticleCtx('dynParticleCtx1')
cmds.setToolTo('dynParticleCtx1')

Get the class type of the current context
ctx = cmds.currentCtx()
cmds.contextInfo(ctx, c=True)
Result: dynParticle ---


Get the title of the current context
cmds.contextInfo(ctx, t=True)
Result: Particle Tool ---


---
Return:
---


    string: Info requested

Flags:
---


---
c(c): boolean
    properties: create
    Return the class type of the named context.

---
escapeContext(esc): boolean
    properties: create
    Return the command string that will allow you to exit the current tool.

---
exists(ex): boolean
    properties: create
    Return true if the context exists, false if it does not
exists (or is internal and therefore untouchable)

---
image1(i1): boolean
    properties: create
    Returns the name of an xpm associated with the named context.

---
image2(i2): boolean
    properties: create
    Returns the name of an xpm associated with the named context.

---
image3(i3): boolean
    properties: create
    Returns the name of an xpm associated with the named context.

---
title(t): boolean
    properties: create
    Return the title string of the named context.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/contextInfo.html 
    """


def control(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> None:
    """Synopsis:
---
---
 control(
string
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

control is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

   Create a simple window containing a single column layout
   and a button.
---

window = cmds.window(title='Control Example')
column = cmds.columnLayout()
button = cmds.button()
cmds.showWindow( window )

   If you don't know that the control is actually a 'button' then
   you may use the 'control' command to determine certain properties.
---

cmds.control( button, query=True, width=True )
cmds.control( button, query=True, height=True )
cmds.control( button, edit=True, visible=False )
cmds.control( button, query=True, visible=True )

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/control.html 
    """


def controller(flagallControllers: boolean, flagchildren: boolean, flaggroup: boolean, flagindex: int, flagisController: string, flagparent: boolean, flagpickWalkDown: boolean, flagpickWalkLeft: boolean, flagpickWalkRight: boolean, flagpickWalkUp: boolean, flagunparent: boolean) -> string:
    """Synopsis:
---
---
 controller([allControllers=boolean], [children=boolean], [group=boolean], [index=int], [isController=string], [parent=boolean], [pickWalkDown=boolean], [pickWalkLeft=boolean], [pickWalkRight=boolean], [pickWalkUp=boolean], [unparent=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

controller is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.controller("object")

---
Return:
---


    string: Command result

Flags:
---


---
allControllers(ac): boolean
    properties: create, query
    When this flag is queried, returns all dependNode attached to a controller in the scene.

---
children(cld): boolean
    properties: query
    Return true if the specified dependNode is a controller.

---
group(g): boolean
    properties: create, query
    Create a controller that is not associated with any object. This new controller will be the parent of all the selected objects.

---
index(idx): int
    properties: query, edit
    In query mode, returns the index of the controller in the parent controller's list of children.
In edit mode, reorder the parent controller's children connections so that the current controller is assigned the given index.

---
isController(ic): string
    properties: create, query
    Returns true if the specified dependNode is a controller.

---
parent(p): boolean
    properties: create, query, edit
    Set or query the parent controller of the selected controller node.

---
pickWalkDown(pwd): boolean
    properties: query
    Return the first child.

---
pickWalkLeft(pwl): boolean
    properties: query
    Return the previous sibling.

---
pickWalkRight(pwr): boolean
    properties: query
    Return the next sibling.

---
pickWalkUp(pwu): boolean
    properties: query
    Return the parent.

---
unparent(unp): boolean
    properties: edit
    Unparent all selected controller objects from their respective parent.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/controller.html 
    """


def convertIffToPsd(flagiffFileName: string, flagpsdFileName: string, flagxResolution: int, flagyResolution: int) -> None:
    """Synopsis:
---
---
 convertIffToPsd([iffFileName=string], [psdFileName=string], [xResolution=int], [yResolution=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

convertIffToPsd is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.convertIffToPsd( 'd:/test.iff', 'd:/test.psd', xr=640, yr=320 )

---


Flags:
---


---
iffFileName(ifn): string
    properties: create, query
    Input iff file name

---
psdFileName(pfn): string
    properties: create, query
    Output file name

---
xResolution(xr): int
    properties: create, query
    X resolution of the image

---
yResolution(yr): int
    properties: create, query
    Y resolution of the image

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/convertIffToPsd.html 
    """


def convertSolidTx(flagalpha: boolean, flagantiAlias: boolean, flagbackgroundColor: tuple[int, int, int], flagbackgroundMode: string, flagcamera: name, flagcomponentRange: boolean, flagdoubleSided: boolean, flagfileFormat: string, flagfileImageName: string, flagfillTextureSeams: boolean, flagforce: boolean, flagfullUvRange: boolean, flagname: string, flagpixelFormat: string, flagresolutionX: int, flagresolutionY: int, flagreuseDepthMap: boolean, flagsamplePlane: boolean, flagsamplePlaneRange: tuple[float, float, float, float], flagshadows: boolean, flaguvBBoxIntersect: boolean, flaguvRange: tuple[float, float, float, float], flaguvSetName: string) -> list[string]:
    """Synopsis:
---
---
 convertSolidTx(
[node|attribute] [object...]
    , [alpha=boolean], [antiAlias=boolean], [backgroundColor=[int, int, int]], [backgroundMode=string], [camera=name], [componentRange=boolean], [doubleSided=boolean], [fileFormat=string], [fileImageName=string], [fillTextureSeams=boolean], [force=boolean], [fullUvRange=boolean], [name=string], [pixelFormat=string], [resolutionX=int], [resolutionY=int], [reuseDepthMap=boolean], [samplePlane=boolean], [samplePlaneRange=[float, float, float, float]], [shadows=boolean], [uvBBoxIntersect=boolean], [uvRange=[float, float, float, float]], [uvSetName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

convertSolidTx is undoable, queryable, and editable.
The current selection will be used if a texture and surface are not
specified.

An image file will be generated for each object and stored in your
image segment of your project. The filename will be formatted using
the texture and surface names as follows:

 {texture}-{surface}.{fileExtension} 

However, if force is off and there is a name collision a version
number will be determined and the filename will be formatted as
follows:

 {texture}-{surface}.{version}.{fileExtension} 

If uv/uvsetName option is specified the filename will include
{surface}-{uvname} instead of {surface}.




Example:
---
import maya.cmds as cmds

cmds.file( f=True, new=True )

Create a blinn shader with a marble texture.
cmds.shadingNode( 'blinn', asShader=True )
cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG' )
cmds.connectAttr( 'blinn1.outColor', 'blinn1SG.surfaceShader', f=True )
cmds.shadingNode( 'marble', asTexture=True )
cmds.connectAttr( 'marble1.outColor', 'blinn1.color', f=True )

Create two objects, and assign the blinn shader to them.
cmds.polySphere()
cmds.sets( e=True, forceElement='blinn1SG' )
cmds.polyPlane()
cmds.move( 2, 0, 0 )
cmds.sets( e=True, forceElement='blinn1SG' )

Create a low resolution texture for the sphere
cmds.convertSolidTx( 'marble1', 'pSphere1', rx=64, ry=64 )

Create a transparency texture forthe plane.
cmds.convertSolidTx( 'marble1.outAlpha', 'pPlane1' )

Create a texture named myTexture.iff for the sphere.
cmds.convertSolidTx( 'marble1', 'pSphere1', bm='extend', fileImageName='myTexture.iff' )

---
Return:
---


    list[string]: File texture nodes

Flags:
---


---
alpha(al): boolean
    properties: create
    Specify whether to compute the transparency when baking
lighting. The conversion will sample both the color and
transparency of the shading network; the alpha channel of the
file texture will be set to correspond to the result from sampling
the transparency. By default transparency is not computed.

---
antiAlias(aa): boolean
    properties: create
    Perform anti-aliasing on the resulting image. Convert solid
texture will generally take four times longer than without
anti-aliasing. By default this flag is off.

---
backgroundColor(bc): [int, int, int]
    properties: create
    Set the background color to a specific value. Default is to
use the shader default color to fill the background. Valid
values range from 0 to 255 if the pixel format is 8 bits per channel,
or 0 to 65535 if the pixel format is 16 bits per channel.
This flag automatically sets -backgroundMode to "color".
Default is black: 0 0 0.

---
backgroundMode(bm): string
    properties: create
    Defines how the background of the texture should be
filled. Three modes are available:
"shader" or 1: uses the default shader color.
"color" or 2: uses the color given by
-backgroundColor flag.
"extend" or 3: extends outwards the color along the
seam edges.
Default is "shader".

---
camera(cam): name
    properties: create
    Specify a camera to use in baking lighting. If a camera is not
specified the camera in the active view will be used.

---
componentRange(cr): boolean
    properties: create
    If one or more components have been selected to use, then
if this flag is set, then the uv range of the components
is used to fit into the texture map resolution. By default this
flag is set to false.

---
doubleSided(ds): boolean
    properties: create
    Specify whether the sampler should flip the surface normal if the
sample point faces away from the camera. Note: flipping the normal
will make the result dependent on the camera (ie. one camera may
flip normals where different camera wouldn't). It's not recommended
that doubleSided be used in combination with shadows. By default
this flag is false.

---
fileFormat(fil): string
    properties: create
    File format to be used for output. IFF is the default if
unspecified. Other valid formats are:
als: Alias PIX
cin: Cineon
eps: EPS
gif: GIF
iff: Maya IFF
jpg: JPEG
yuv: Quantel
rla: Wavefront RLA
sgi: SGI
si: SoftImage (.pic)
tga: Targa
tif: TIFF
bmp: Windows Bitmap

---
fileImageName(fin): string
    properties: create
    Specify the output path and name of file texture image. If the
file name doesn't contain a directory separator, the image
will be written to source images of the current project. The
file will not be versioned if it already exists.

---
fillTextureSeams(fts): boolean
    properties: create
    Specify whether or not to overscan the polygon beyond its outer
edges, when creating the file texture, in order to fill the texture
seams.
Default is true.

---
force(f): boolean
    properties: create
    If the output image already exists overwrite it. By default
this flag is off.

---
fullUvRange(fur): boolean
    properties: create
    Sample using the full uv range of the surface. This flag
cannot be used with the -uvr flag. A 2D texture placement node
will be created and connected to the file texture. The placement's
translate and coverage will be set according to the full UV range of
the surface.

---
name(n): string
    properties: create
    Set the name of the file texture node. Name conflict
resolution will be used to determine valid names when multiple
objects are specified.

---
pixelFormat(pf): string
    properties: create
    Specifies the pixel format of the image.
Note that not all file formats support all pixel formats.
Available options:
"8": 8 bits per channel, unsigned (0-255)
"16": 16 bits per channel, unsigned (0-65535)
Default is "8".

---
resolutionX(rx): int
    properties: create
    Set the horizontal image resolution. If this flag
is not specified, the resolution will be set to 256.

---
resolutionY(ry): int
    properties: create
    Set the vertical image resolution. If this flag
is not specified, the resolution will be set to 256.

---
reuseDepthMap(rdm): boolean
    properties: create
    Specify whether or not to reuse all the generated dmaps.
Default is false.

---
samplePlane(sp): boolean
    properties: create
    Specify whether to sample using a virtual plane. This virtual plane
has texture coordinates in the rectangle defined by the
-samplePlaneRange flag. If the -samplePlaneRange flag is not set then
the virtual plane defaults to having texture coordinates in the
(0,0) to (1,1) square. If this option is set than all surface based
arguments will be ignored.

---
samplePlaneRange(spr): [float, float, float, float]
    properties: create
    Specify the uv range of the texture coordinates used to sample if
the -samplePlane option is set. There are four arguments corresponding
to uMin, uMax, vMin and vMax. By default the virtual plane is from
uMin 0 to uMax 1, and vMin 0 to vMax 1.

---
shadows(sh): boolean
    properties: create
    Specify whether to compute shadows when baking lighting. Disk based
shadow maps will be used. Only lights with depth map shadows enabled
will contribute to the shading. By default shadows are not computed.

---
uvBBoxIntersect(ubi): boolean
    properties: create
    This flag is obsolete.

---
uvRange(uvr): [float, float, float, float]
    properties: create
    Specify the uv range in which samples will be computed. There are
four arguments corresponding to uMin, uMax, vMin and vMax. Each
value should be specified based on the surface's uv space. A 2D
texture placement node will be created and connected to the file
texture. The placement's frame translate and coverage will be set
according to the uv range specified. By default the entire uv range
of the surface will be used.

---
uvSetName(uv): string
    properties: create
    Specify which uv set has to be used as the driving parametrization
for convert solid.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/convertSolidTx.html 
    """


def convertTessellation(flagallCameras: boolean, flagcamera: name) -> boolean:
    """Synopsis:
---
---
 convertTessellation([allCameras=boolean], [camera=name])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

convertTessellation is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Convert the basic tessellation settings to advanced.
cmds.convertTessellation( 'nurbsSphere1' )

Set the tessellation for nurbsSphere1 based on camera projection
from persp.
cmds.convertTessellation( 'nurbsSphere1', camera='persp' )

Set tessellation based on all renderable cameras.
cmds.convertTessellation( 'nurbsSphere2', allCameras='nurbsSphere1' )

Set the tessellation for all selected objects.
cmds.convertTessellation()

---
Return:
---


    boolean: Success or Failure.

Flags:
---


---
allCameras(acm): boolean
    properties: create
    Specifies that all renderable cameras should be used in calculating
    the screen based tessellation.

---
camera(cam): name
    properties: create
    Specifies the camera which should be used in calculating the screen
    based tessellation.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/convertTessellation.html 
    """


def convertUnit(flagfromUnit: string, flagtoUnit: string) -> float:
    """Synopsis:
---
---
 convertUnit(
string
    , [fromUnit=string], [toUnit=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

convertUnit is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Returns string "4.80315in", which is 12.2cm in inches.
cmds.convertUnit( '12.2', fromUnit='cm', toUnit='in' )

Returns string "3.499563yd", which is 3.2m in yards.
cmds.convertUnit( '3.2m', toUnit='yard' )

Returns float value 13.716, which is 5.4 inches in cm (default system units).
cmds.convertUnit( '5.4', fromUnit='inch' )

---
Return:
---


    float: or string

Flags:
---


---
fromUnit(f): string
    properties: create
    The unit to convert from.  If not supplied, it is assumed to be the
system default.  The from unit may also be supplied as part of the
value e.g. 11.2m (11.2 meters).

---
toUnit(t): string
    properties: create
    The unit to convert to.  If not supplied, it is assumed to be the
system default

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/convertUnit.html 
    """


def copyAttr(flagattribute: string, flagcontainerParentChild: boolean, flaginConnections: boolean, flagkeepSourceConnections: boolean, flagoutConnections: boolean, flagrenameTargetContainer: boolean, flagvalues: boolean) -> None:
    """Synopsis:
---
---
 copyAttr([attribute=string], [containerParentChild=boolean], [inConnections=boolean], [keepSourceConnections=boolean], [outConnections=boolean], [renameTargetContainer=boolean], [values=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

copyAttr is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


transfer input connections and values from locator1 to locator2
---

cmds.copyAttr('locator1','locator2',inConnections=True,values=True)

transfer only the translateX and translateY values
---

cmds.copyAttr('locator1','locator2',values=True,attribute=['tx','translateY'])

---


Flags:
---


---
attribute(at): string
    properties: create, multiuse
    The name of the attribute(s) for which connections and/or values will be
transferred. If no attributes are specified, then all attributes will be
transferred.

---
containerParentChild(cpc): boolean
    properties: create
    For use when copying from one container to another only. This option indicates
that the published parent and/or child relationships on the original container
should be transferred to the target container if the published names match.

---
inConnections(ic): boolean
    properties: create
    Indicates that incoming connections should be transferred.

---
keepSourceConnections(ksc): boolean
    properties: create
    For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out connections on the source node will be broken and made to the target node.

---
outConnections(oc): boolean
    properties: create
    Indicates that outgoing connections should be transferred.

---
renameTargetContainer(rtc): boolean
    properties: create
    For use when copying from one container to another only. This option will
rename the target container to the name of the original container, and
rename the original container to its old name + "Orig". You would want to
use this option if your original container was referenced and edited,
and you want those edits from the main scene to now apply to the
new container.

---
values(v): boolean
    properties: create
    Indicates that values should be transferred.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/copyAttr.html 
    """


def copyDeformerWeights(flagdestinationDeformer: string, flagdestinationShape: string, flagmirrorInverse: boolean, flagmirrorMode: string, flagnoMirror: boolean, flagsmooth: boolean, flagsourceDeformer: string, flagsourceShape: string, flagsurfaceAssociation: string, flaguvSpace: tuple[string, string]) -> None:
    """Synopsis:
---
---
 copyDeformerWeights([destinationDeformer=string], [destinationShape=string], [mirrorInverse=boolean], [mirrorMode=string], [noMirror=boolean], [smooth=boolean], [sourceDeformer=string], [sourceShape=string], [surfaceAssociation=string], [uvSpace=[string, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

copyDeformerWeights is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create plane and a cluster.
---

cmds.file( f=True,new=True )
cmds.polyPlane( ch=1, w=10, h=10, sx=5, sy=5, ax=(0,1,0) )
cmds.cluster( n='testCluster', 'pPlane1' )

Modify some weights on the -x side of the character
---

cmds.select( ['pPlane1.vtx[0]', 'pPlane1.vtx[6]', 'pPlane1.vtx[12]', 'pPlane1.vtx[18]'])
cmds.percent( 'testCluster', v='0.5' )

Mirror the skin weights to the other side of the character
Mirror inverse is chosen since we want to go from -x to +x, not +x to -x.
---

cmds.copyDeformerWeights( ss='pPlane1', ds='pPlane1', sd='testCluster', mirrorMode='YZ', mirrorInverse = True)
cmds.select( ['pPlane1.vtx[5]', 'pPlane1.vtx[11]', 'pPlane1.vtx[17]', 'pPlane1.vtx[23]'])
cmds.percent( 'testCluster', q=True, v=True )

---


Flags:
---


---
destinationDeformer(dd): string
    properties: create, query, edit
    Specify the deformer used by the destination shape

---
destinationShape(ds): string
    properties: create, query, edit
    Specify the destination deformed shape

---
mirrorInverse(mi): boolean
    properties: create, query, edit
    Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.

---
mirrorMode(mm): string
    properties: create, query, edit
    The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.

---
noMirror(nm): boolean
    properties: create, query, edit
    When the no mirror flag is used, the weights are copied instead of mirrored.

---
smooth(sm): boolean
    properties: create, query, edit
    When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.

---
sourceDeformer(sd): string
    properties: create, query, edit
    Specify the deformer whose weights should be mirrored.  When queried, returns the deformers used by the source shapes.

---
sourceShape(ss): string
    properties: create, query, edit
    Specify the source deformed shape

---
surfaceAssociation(sa): string
    properties: create, query, edit
    The surfaceAssociation flag controls how the weights are transferred between the
surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.

---
uvSpace(uv): [string, string]
    properties: create, query, edit
    The uvSpace flag indicates that the weight transfer should occur in UV space, based on the
source and destination UV sets specified.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/copyDeformerWeights.html 
    """


def copyFlexor() -> string:
    """Synopsis:
---
---
 copyFlexor(
[objects]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

copyFlexor is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Copy flexor ffd1Lattice to joint8
---

cmds.copyFlexor( 'ffd1Lattice', 'joint8' )

---
Return:
---


    string: The name of the new flexor node

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/copyFlexor.html 
    """


def copyKey(flaganimLayer: string, flaganimation: string, flagattribute: string, flagclipboard: string, flagcontrolPoints: boolean, flagfloat: floatrange, flagforceIndependentEulerAngles: boolean, flaghierarchy: string, flagincludeUpperBound: boolean, flagindex: uint, flagoption: string, flagshape: boolean, flagtime: timerange) -> int:
    """Synopsis:
---
---
 copyKey(
[objects]
    , [animLayer=string], [animation=string], [attribute=string], [clipboard=string], [controlPoints=boolean], [float=floatrange], [forceIndependentEulerAngles=boolean], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [option=string], [shape=boolean], [time=timerange])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

copyKey is undoable, NOT queryable, and NOT editable.
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

This command copies curve segments's hierarchies from
specified targets and puts them in the clipboard.  Source
curves are unchanged.  The pasteKey command applies these
curves to other objects.

The shape of the copied curve placed in the clipboard
depends on the copyKey "-option" specified.  Each of these options
below will be explained using an example.  For all the explanations,
let us assume that the source animation curve (from which keys will
be copied) has 5 keyframes at times 10, 15, 20, 25, and 30.

 copyKey -t "12:22" -option keys

A 5-frame animation curve with one key at 15 and another key at 20
is placed into the keyset clipboard.

 copyKey -t "12:22" -option curve

A 10-frame animation is placed into the clipboard. The curve
contains the original source-curve keys at times 15 and 20, as well
as new keys inserted at times 12 and 22 to preserve the shape of the
curve at the given time segment.




TbaseKeySetCmd.h




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

Copy keyframes from frame 10 to 20 of cube1's "Translate X" attribute
---

cmds.copyKey( 'cube1', time=(10,20), attribute='translateX', option="curve" )

Copy from all active objects all keys in the range 0 to 60
---

cmds.copyKey( time=(0,60) )

---
Return:
---


    int: Number of animation curves copied.

Flags:
---


---
animLayer(al): string
    properties: create
    Specifies that the keys getting copied should come from this
specified animation layer. If no keys on the object exist
on this layer, then no keys are copied.

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
clipboard(cb): string
    properties: create
    Specifies the clipboard to which animation is copied.
Valid clipboards are "api" and "anim".  The default clipboard
is: anim

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
forceIndependentEulerAngles(fea): boolean
    properties: create
    Specifies that the rotation curves should always be placed on the
clipboard as independent Euler Angles. The default value is false.

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
option(o): string
    properties: create
    The option to use when performing the copyKey operation.
Valid options are "keys," and "curve."  The default copy option
is: keys

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/copyKey.html 
    """


def copySkinWeights(flagdestinationSkin: string, flaginfluenceAssociation: string, flagmirrorInverse: boolean, flagmirrorMode: string, flagnoBlendWeight: boolean, flagnoMirror: boolean, flagnormalize: boolean, flagsampleSpace: uint, flagselectedComponents: boolean, flagsmooth: boolean, flagsourceSkin: string, flagsurfaceAssociation: string, flaguvSpace: tuple[string, string]) -> None:
    """Synopsis:
---
---
 copySkinWeights([destinationSkin=string], [influenceAssociation=string], [mirrorInverse=boolean], [mirrorMode=string], [noBlendWeight=boolean], [noMirror=boolean], [normalize=boolean], [sampleSpace=uint], [selectedComponents=boolean], [smooth=boolean], [sourceSkin=string], [surfaceAssociation=string], [uvSpace=[string, string]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

copySkinWeights is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create plane and a skeleton. Bind the skin.
---

cmds.file( f=True,new=True )
cmds.polyPlane( ch=1, w=10, h=10, sx=5, sy=5, ax=(0,1,0) )
cmds.select( d=True )
cmds.joint( p=(0, 0, -6) )
cmds.joint( p=(0, 0, -4) )
cmds.joint( 'joint1', e=True, zso=True, oj='xyz')
cmds.joint( p=(2, 0, -4) )
cmds.joint( 'joint2', e=True, zso=True, oj='xyz')
cmds.joint( p=(5, 0, -3) )
cmds.joint( 'joint3', e=True, zso=True, oj='xyz')
cmds.select( 'joint2', r=True )
cmds.joint( p=(-2, 0, -4) )
cmds.joint( 'joint4', e=True, zso=True, oj='xyz')
cmds.joint( p=(-5, 0, -3) )
cmds.joint( 'joint5', e=True, zso=True, oj='xyz')
cmds.select( 'joint2', r=True )
cmds.joint( p=(0, 0, 3) )
cmds.joint( 'joint6', e=True, zso=True, oj='xyz')
cmds.joint( p=(5, 0, 5) )
cmds.joint( 'joint7', e=True, zso=True, oj='xyz')
cmds.select( 'joint7', r=True )
cmds.joint( p=(-5, 0, 5) )
cmds.joint( 'joint8', e=True, zso=True, oj='xyz')
cmds.select( 'pPlane1', 'joint1', r=True )
maya.mel.eval('createSkinCluster "-mi 5 -dr 4"' )

Modify some weights on the -x side of the character
---

cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[30]', tv=('joint2',0.200000) )
cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[31]', tv=('joint2',0.200000) )
cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[24]', tv=('joint5',0.550000) )
cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[25]', tv=('joint5',0.550000) )

Mirror the skin weights to the other side of the character
Mirror inverse is chosen since we want to go from -x to +x, not +x to -x.
---

cmds.copySkinWeights( ss='skinCluster1', ds='skinCluster1', mirrorMode='YZ', mirrorInverse=True )

Now create a second plane and bind it as skin
---

cmds.polyPlane( ch=1, w=10, h=10, sx=5, sy=5, ax=(0,1,0) )
cmds.select( 'pPlane2', r='joint1' )
maya.mel.eval('createSkinCluster "-mi 5 -dr 4"' )

Copy the skin weights from the first plane onto the new plane.
The -noMirror flag is used since we want to copy directly, not mirror.
---

cmds.copySkinWeights( ss='skinCluster1', ds='skinCluster2', noMirror=True )

---


Flags:
---


---
destinationSkin(ds): string
    properties: create, query, edit
    Specify the destination skin shape

---
influenceAssociation(ia): string
    properties: create, query, edit, multiuse
    The influenceAssociation flag controls how the influences on the source and target skins
are matched up. The flag can be included multiple times to specify multiple association
schemes that will be invoked one after the other until all influences have been matched
up. Supported values are "closestJoint", "closestBone", "label", "name", "oneToOne". The
default is closestJoint.

---
mirrorInverse(mi): boolean
    properties: create, query, edit
    Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.

---
mirrorMode(mm): string
    properties: create, query, edit
    The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.

---
noBlendWeight(nbw): boolean
    properties: create, query, edit
    When the no blend flag is used, the blend weights on the skin cluster will not be copied across to
the destination.

---
noMirror(nm): boolean
    properties: create, query, edit
    When the no mirror flag is used, the weights are copied instead of mirrored.

---
normalize(nr): boolean
    properties: create, query, edit
    Normalize the skin weights.

---
sampleSpace(spa): uint
    properties: create, query, edit
    Selects which space the attribute transfer is performed in.
0 is world space, 1 is model space. The default is world space.

---
selectedComponents(sc) 2024.1: boolean
    properties: create, query, edit
    The selectedComponents flag can be used in combination with the sourceSkin and destinationSkin
flags to specify that only the skin weights on the selected components should be copied.

---
smooth(sm): boolean
    properties: create, query, edit
    When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.

---
sourceSkin(ss): string
    properties: create, query, edit
    Specify the source skin shape

---
surfaceAssociation(sa): string
    properties: create, query, edit
    The surfaceAssociation flag controls how the weights are transferred between the
surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.

---
uvSpace(uv): [string, string]
    properties: create, query, edit
    The uvSpace flag indicates that the weight transfer should occur in UV space, based on the
source and destination UV sets specified.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/copySkinWeights.html 
    """


def crashInfo(flagcrashFile: boolean, flagcrashLog: boolean, flagsavedBeforeCrash: boolean) -> None:
    """Synopsis:
---
---
 crashInfo([crashFile=boolean], [crashLog=boolean], [savedBeforeCrash=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

crashInfo is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

query the crash file full path name
---

cmds.crashInfo( q = True, cf = True)
Result: C:/Users/maya/AppData/Local/Temp/maya.20160413.2009.ma ---


query the crash log full path name
---

cmds.crashInfo( q = True, cl = True)
Result: C:/Users/maya/AppData/Local/Temp/maya.20160413.2009.log ---


query the saved file full path name before crash
---

cmds.crashInfo( q = True, sbc = True)
Result: C:/Users/maya/Documents/maya/projects/default/scenes/test.mb ---


---


Flags:
---


---
crashFile(cf): boolean
    properties: query
    Return the crash file full path name.

---
crashLog(cl): boolean
    properties: query
    Return the crash log full path name.

---
savedBeforeCrash(sbc): boolean
    properties: query
    Return the saved file full path name before crash.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/crashInfo.html 
    """


def createAttrPatterns(flagpatternDefinition: string, flagpatternFile: string, flagpatternType: string) -> string:
    """Synopsis:
---
---
 createAttrPatterns([patternDefinition=string], [patternFile=string], [patternType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

createAttrPatterns is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.createAttrPatterns( patternType="xmlPattern", patternFile="patterns/patternFile.xml" )
// Result: [myXMLPattern] //

---
Return:
---


    string: Name of created pattern

Flags:
---


---
patternDefinition(pd): string
    properties: create
    Hardcoded string containing the pattern definition, for simpler formats that
don't really need a separate file for definition.

---
patternFile(pf): string
    properties: create
    File where the pattern information can be found

---
patternType(pt): string
    properties: create
    Name of the pattern definition type to use in creating this instance
of the pattern.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/createAttrPatterns.html 
    """


def createDisplayLayer(flagempty: boolean, flagmakeCurrent: boolean, flagname: string, flagnoRecurse: boolean, flagnumber: int) -> string:
    """Synopsis:
---
---
 createDisplayLayer([empty=boolean], [makeCurrent=boolean], [name=string], [noRecurse=boolean], [number=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

createDisplayLayer is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

   Create a sphere.
---

objectArray = cmds.sphere()

   Select the sphere.
---

cmds.select( objectArray[0] )

   Create a layer. The selected object will be placed
   in this layer. Note in this case both the nurbsSphere
   and nurbsSphere shape are placed in the layer.
---

cmds.createDisplayLayer()

   Create a cone.
---

objectArray = cmds.cone()

   Select the cone.
---

cmds.select( objectArray[0] )

   Create a layer but only put the nurbsCone in the layer.
   The nurbsConeShape will remain in the default layer
   as a result of specifying the -nr/noRecurse flag.
---

   Note also that you can specify the name of the layer
   with the -n/name flag.
---


cmds.createDisplayLayer( noRecurse=True, name='ExampleLayer' )

---
Return:
---


    string: Name of display layer node that was created

Flags:
---


---
empty(e): boolean
    properties: create
    If set then create an empty display layer.  ie. Do not add the selected
items to the new display layer.

---
makeCurrent(mc): boolean
    properties: create
    If set then make the new display layer the current one.

---
name(n): string
    properties: create
    Name of the new display layer being created.

---
noRecurse(nr): boolean
    properties: create
    If set then only add selected objects to the display layer.  Otherwise all
descendants of the selected objects will also be added.

---
number(num): int
    properties: create
    Number for the new display layer being created.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/createDisplayLayer.html 
    """


def createEditor(flagnoCloseOnDelete: boolean, flagqueueForDelete: boolean) -> None:
    """Synopsis:
---
---
 createEditor(
string node
    , [noCloseOnDelete=boolean], [queueForDelete=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

createEditor is undoable, NOT queryable, and NOT editable.
The property sheets created by this command can by user-customized
using the editorTemplate command.




Example:
---
import maya.cmds as cmds

The following command will create an attribute
editor in someWindow|topLayout for curve2.
---

cmds.createEditor( 'someWindow|toplayout', 'curve2' )

---


Flags:
---


---
noCloseOnDelete(nc): boolean
    properties: create
    If this flag is set then don't close the editor when the data is deleted

---
queueForDelete(qfd): boolean
    properties: create
    The specified layout is put on a queue.  When the queue
is full, layouts past the end of the queue are automatically
deleted.  If the layout is already on the queue, it is
moved to the front.  This allows us to dispose of editors
when they are no longer being used.  This flag should only be
used by the showEditor.mel script.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/createEditor.html 
    """


def createLayeredPsdFile(flagimageFileName: tuple[string, string, string], flagpsdFileName: string, flagxResolution: uint, flagyResolution: uint) -> None:
    """Synopsis:
---
---
 createLayeredPsdFile([imageFileName=[string, string, string]], [psdFileName=string], [xResolution=uint], [yResolution=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

createLayeredPsdFile is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Creates a layered PSD file with "Layer 1" as one of the layers. The image which
gets transfered to "Layer 1" is picked from D:/test.iff. The blend mode assigned to
is the "Normal" mode.
cmds.createLayeredPsdFile( 'D:/test.psd', xr=640, yr=480, ifn=('D:/test.iff', 'Normal', 'Layer 1') )

---


Flags:
---


---
imageFileName(ifn): [string, string, string]
    properties: create, multiuse
    Layer name, blend mode, Image file name  The image in the file will be
transferred to layer specified. The image file specified can be in any
of the formats supported by maya (ex. iff, jpg, gif, tif etc.). The blend
mode options are : "Normal", "Dissolve", "Dark", "Multiply", "Color Burn",
"Linear Burn", "Lighten", "Screen", "Color Dodge", "Linear Dogde", "Overlay",
"Soft Light", "Hard Light", "Dissolve", "Vivid Light", "Linear Light", "Pin Light",
"Hard Mix", "Difference", "Exclusion", "Hue", "Saturation", "Color",  "Luminosity"

---
psdFileName(psf): string
    properties: create
    PSD file name.

---
xResolution(xr): uint
    properties: create
    X - resolution of the image.

---
yResolution(yr): uint
    properties: create
    Y - resolution of the image.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/createLayeredPsdFile.html 
    """


def createNode(flagname: string, flagparent: string, flagshared: boolean, flagskipSelect: boolean) -> string:
    """Synopsis:
---
---
 createNode(
string
    , [name=string], [parent=string], [shared=boolean], [skipSelect=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

createNode is undoable, NOT queryable, and NOT editable.



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

---
Return:
---


    string: The name of the new node.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/createNode.html 
    """


def createRenderLayer(flagempty: boolean, flagg: boolean, flagmakeCurrent: boolean, flagname: string, flagnoRecurse: boolean, flagnumber: int) -> string:
    """Synopsis:
---
---
 createRenderLayer([empty=boolean], [g=boolean], [makeCurrent=boolean], [name=string], [noRecurse=boolean], [number=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

createRenderLayer is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Add nut and nutShape to a new render layer
---

cmds.select( 'nut' )
cmds.createRenderLayer()
Result: renderLayer1 ---


Add only bolt to a new render layer
---

cmds.createRenderLayer( 'bolt', noRecurse=True )
Result: renderLayer2 ---


Add washer to the new render layer 'assembly'.
---

cmds.createRenderLayer( 'washer', noRecurse=True, name='assembly' )
Result: assembly ---


Create a layer that will always contains everything
---

cmds.createRenderLayer( g=True )
Result: renderLayer3 ---


---
Return:
---


    string: Name of render layer node that was created

Flags:
---


---
empty(e): boolean
    properties: create
    If set then create an empty render layer. The global flag or specified
member list will take precidence over  use of this flag.

---
g(g): boolean
    properties: create
    If set then create a layer that contains all DAG objects in the scene. Any
future objects created will also automatically become members of this layer.
The global flag will take precidence over use of the empty flag or specified
member list.

---
makeCurrent(mc): boolean
    properties: create
    If set then make the new render layer the current one.

---
name(n): string
    properties: create
    Name of the new render layer being created.

---
noRecurse(nr): boolean
    properties: create
    If set then only add specified objects to the render layer.  Otherwise all
descendants will also be added.

---
number(num): int
    properties: create
    Number for the new render layer being created.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/createRenderLayer.html 
    """


def createSubdivRegion() -> boolean:
    """Synopsis:
---
---
 createSubdivRegion()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

createSubdivRegion is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

after selecting components of a subdivision surface
cmds.createSubdivRegion()

---
Return:
---


    boolean: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/createSubdivRegion.html 
    """


def ctxAbort() -> None:
    """Synopsis:
---
---
 ctxAbort()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ctxAbort is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a new particle tool context, then switch to it
cmds.dynParticleCtx('dynParticleCtx1')
cmds.setToolTo('dynParticleCtx1')
Click the positions where you want to place the particles

This command will reset the particle tool, clear the particles you have just created
cmds.ctxAbort();

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ctxAbort.html 
    """


def ctxCompletion() -> None:
    """Synopsis:
---
---
 ctxCompletion()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ctxCompletion is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a curve
cmds.curve(p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9), (12, 10, 2)], k=[0,0,0,1,2,2,2])
Result: curve1 ---


Create a new curve editor context to modify the curve, then switch to it
You can modify the curve using the manipulator handle
cmds.curveEditorCtx('curveEditorCtx1')
cmds.setToolTo('curveEditorCtx1')

This command ends curve editing, the manipulator handle will disappear, leaving the modified curve
cmds.ctxCompletion()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ctxCompletion.html 
    """


def ctxEditMode(flagbuttonDown: boolean, flagbuttonUp: boolean) -> None:
    """Synopsis:
---
---
 ctxEditMode([buttonDown=boolean], [buttonUp=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ctxEditMode is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a poly cube
cmds.polyCube(w=2, h=2, d=2, n='pCube1')

Create a new rotate manip context, then switch to it.
cmds.manipRotateContext('manipRotateContext1')
cmds.setToolTo('manipRotateContext1')

Switch to edit mode to change pivots
cmds.ctxEditMode()

---


Flags:
---


---
buttonDown(btd): boolean
    properties: create
    Edit mode is being invoked from a hotkey press event.

---
buttonUp(btu): boolean
    properties: create
    Edit mode is being invoked from a hotkey release event.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ctxEditMode.html 
    """


def ctxTraverse(flagdown: boolean, flagleft: boolean, flagright: boolean, flagup: boolean) -> None:
    """Synopsis:
---
---
 ctxTraverse([down=boolean], [left=boolean], [right=boolean], [up=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ctxTraverse is undoable, NOT queryable, and NOT editable.
Some contexts will ignore this command. Individual contexts
determine what up/down left/right mean.




Example:
---
import maya.cmds as cmds

Create a particle context, then switch to it
cmds.dynParticleCtx('dynParticleCtx1')
cmds.setToolTo('dynParticleCtx1')

Now you can create particles by mouse clicking
After creating several particles, we switch to edit mode
cmds.ctxEditMode()

Traverse in the created particles
cmds.ctxTraverse(left=True)
cmds.ctxTraverse(left=True)
cmds.ctxTraverse(right=True)

---


Flags:
---


---
down(d): boolean
    properties: create
    Move "down" as defined by the current context.

---
left(l): boolean
    properties: create
    Move "left" as defined by the current context.

---
right(r): boolean
    properties: create
    Move "right" as defined by the current context.

---
up(up): boolean
    properties: create
    Move "up" as defined by the current context.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ctxTraverse.html 
    """


def currentCtx() -> string:
    """Synopsis:
---
---
 currentCtx()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

currentCtx is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.currentCtx()

---
Return:
---


    string: : The name of the currently selected tool context.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/currentCtx.html 
    """


def currentTime(flagupdate: boolean) -> time:
    """Synopsis:
---
---
 currentTime(
[time]
    , [update=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

currentTime is NOT undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Query the current time
---

cmds.currentTime( query=True )

Change the current time to "30" in current time units
---

cmds.currentTime( 30, edit=True )
cmds.currentTime( 30 )

Change the current time to 2 seconds
---

cmds.currentTime( '2sec', edit=True )

Change the current time, but do not cause the model
to update.
---

cmds.currentTime( -10, update=False, edit=True )

---
Return:
---


    time: Command result

Flags:
---


---
update(u): boolean
    properties: create
    change the current time, but do not update the world.
Default value is true.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/currentTime.html 
    """


def currentTimeCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 currentTimeCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

currentTimeCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.currentTimeCtx()

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/currentTimeCtx.html 
    """


def currentUnit(flagangle: string, flagfullName: boolean, flaglinear: string, flagtime: string, flagupdateAnimation: boolean) -> string:
    """Synopsis:
---
---
 currentUnit([angle=string], [fullName=boolean], [linear=string], [time=string], [updateAnimation=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

currentUnit is undoable, queryable, and NOT editable.
The current unit affects how all commands in Maya interpret their
numeric values. For example, if the current linear unit is cm,
then the command:

move 5 -2 3;
sphere -radius 4;

will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as
creating a sphere with radius 4cm. Similarly, if the current time unit
is Film (24 frames per second), then the command:

currentTime 6;

will be interpreted as setting the current time to frame 6 in the Film
unit, which is 6/24 or 0.25 seconds.

You can always override the unit of a particular numeric value to a
command be specifying it one the command. For example, using the above
examples:

move 5m -2mm 3cm;
sphere -radius 4inch;
currentTime 6ntsc;

would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters
in Z, create a sphere of radius 4 inches, and change the current time
to 6 frames in the NTSC unit, which would be 0.2 seconds, or 4.8 frames
in the current (Film) unit.




Example:
---
import maya.cmds as cmds

What is the current linear unit?
cmds.currentUnit( query=True, linear=True )

What is the current angular unit in its long name form?
cmds.currentUnit( fullName=True, query=True, angle=True )

Change the current time unit to ntsc
cmds.currentUnit( time='ntsc' )

Change the current linear unit to inches
cmds.currentUnit( linear='in' )

---
Return:
---


    string: The new current unit that has been set

Flags:
---


---
angle(a): string
    properties: create, query
    Set the current angular unit. Valid strings are:

[deg | degree | rad | radian]

When queried, returns a string which is the current angular unit

---
fullName(f): boolean
    properties: query
    A query only flag. When specified in conjunction with any of
the -linear/-angle/-time flags, will return the long form of the unit.
For example, mm and millimeter are the same unit, but
the former is the short form of the unit name, and the latter is the
long form of the unit name.

---
linear(l): string
    properties: create, query
    Set the current linear unit. Valid strings are:

[mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]

When queried, returns a string which is the current linear unit

---
time(t): string
    properties: create, query
    Set the current time unit. Valid strings are:

[hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]

When queried, returns a string which is the current time unit

Note that there is no long form for any of the time units.
The non-seconds based time units are interpreted as the following
frames per second:

game: 15 fps
film: 24 fps
pal: 25 fps
ntsc: 30 fps
show: 48 fps
palf: 50 fps
ntscf: 60 fps

---
updateAnimation(ua): boolean
    properties: create
    An edit only flag.  When specified in conjunction with the -time
flag indicates that times for keys are not updated.  By default when the
current time unit is changed, the times for keys are modified so that
playback timing is preserved.  For example a key set a frame 12film is
changed to frame 15ntsc when the current time unit is changed to ntsc,
since they both represent a key at a time of 0.5 seconds.  Specifying
-updateAnimation false would leave the key at frame 12ntsc.
Default is -updateAnimation true.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/currentUnit.html 
    """


def curve(flagappend: boolean, flagbezier: boolean, flagdegree: float, flageditPoint: tuple[linear, linear, linear], flagknot: float, flagname: string, flagobjectSpace: boolean, flagperiodic: boolean, flagpoint: tuple[linear, linear, linear], flagpointWeight: tuple[linear, linear, linear, float], flagreplace: boolean, flagworldSpace: boolean) -> string:
    """Synopsis:
---
---
 curve(
string
    , [append=boolean], [bezier=boolean], [degree=float], [editPoint=[linear, linear, linear]], [knot=float], [name=string], [objectSpace=boolean], [periodic=boolean], [point=[linear, linear, linear]], [pointWeight=[linear, linear, linear, float]], [replace=boolean], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curve is undoable, NOT queryable, and NOT editable. To create a curve-on-surface, use the curveOnSurface command.
 To change the degree of a curve, use the rebuildCurve command.
 To change the of parameter range curve, use the rebuildCurve command.




Example:
---
import maya.cmds as cmds

These commands create curves with four control vertices.
The first one is created without weights.  The third command
shows how you can use units to specify position.
cmds.curve( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)] )
cmds.curve( pw=[(0, 0, 0, 1), (3, 5, 6, 1), (5, 6, 7, 1), (9, 9, 9, 1)] )
cmds.curve( p=[('0cm', '0cm', '0cm'), ('3in', '5in', '6in'), ('5ft', '6ft', '7ft'), (9, 9, 9)] )

This command replaces an existing curve, curve1, with the given points.
Do not use this flag on a curve that is a result of a construction
history operation.
cmds.curve( 'curve1', r=True, p=[(0, 0, 0), (3, 5, 6), (10, 12, 14), (9, 9, 9)] )

This command adds two CVs to an existing curve, curve1.
The "-ws" flag can be used if the specified CVs are in world space.
Do not use this flag on a curve that is a result of a construction
history operation.
cmds.curve( 'curve1', a=True, p=[(13, 13, 13), (13, 15, 16)] )

This command creates a curve with five control vertices,
with a knot vector. Notice that there must be
(number of CVs + degree - 1) knots and that the knot
vector must be non-decreasing.
cmds.curve( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9), (12, 10, 2)], k=[0,0,0,1,2,2,2] )

This command creates a closed (or "periodic") curve with
four distinct CVs. You must specify a knot vector when the
"-per" flag is used. Notice that the first "degree" points
are the same as the last "degree" points (ie. the first three
points are the same as the last three points). Notice also
that the knot spacing between the first "degree" knots must
be the same as the spacing between the last "degree" knots
(ie. the space between the 1st and 2nd knots is the same as
the space between the 7th and 8th knots, and the space between
the 2nd and 3rd knots is the same as the space between the
8th and 9th knots). There must be space between the first
"degree" knots, unlike the previous example, where the first
"degree" knots are the same.
cmds.curve( per=True, p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9), (0, 0, 0), (3, 5, 6), (5, 6, 7)], k=[-2,-1,0,1,2,3,4,5,6] )

How to query curve properties:

This returns the degree of the curve.  Note that the
number of CVs = degree + spans.
cmds.getAttr( 'curve1.degree' )

This returns the number of spans in the curve.  Note that the
number of CVs = degree + spans.
cmds.getAttr( 'curve1.spans' )

This returns the curve form.
cmds.getAttr( 'curve1.form' )

This returns the minimum parameter value on the curve.
cmds.getAttr( 'curve1.minValue' )

This returns the maximum parameter value on the curve.
cmds.getAttr( 'curve1.maxValue' )

This returns the local x,y,z of the 1st CV.  Use a curve info node if
the curve is a result of a construction history operation.
cmds.getAttr( 'curve1.cv[0]' )

This returns the local x,y,z of the 1st three CVs.  Use a curve info
node if the curve is a result of a construction history operation.
cmds.getAttr( 'curve1.cv[*]' )

This returns the local x,y,z of all CVs.  Use a curve info node if
the curve is a result of a construction history operation.
cmds.getAttr( 'curve1.cv[0:2]' )

This returns the arc length of the curve.  Use "-ch" flag with
the arclen command to get a curve info node that constantly updates
to the current arc length.
cmds.arclen( 'curve1' )

This sequence creates a curve info node, connects the info node to the
curve and queries the knot vector of the curve using the curve info node.
You can use the curve info node to query other attributes such as
world space CV values and arc length.
cmds.createNode( 'curveInfo' )
cmds.connectAttr( 'curveShape1.worldSpace', 'curveInfo1.inputCurve' )
cmds.getAttr( 'curveInfo1.knots[*]' )

---
Return:
---


    string: The path to the new curve or the replaced curve

Flags:
---


---
append(a): boolean
    properties: create
    Appends point(s) to the end of an existing curve.
If you use this flag, you must specify the name of the
curve to append to, at the end of the command.  (See examples below.)

---
bezier(bez): boolean
    properties: create
    The created curve will be a bezier curve.

---
degree(d): float
    properties: create
    The degree of the new curve.  Default is 3.  Note that you need
(degree+1) curve points to create a visible curve span.  eg. you
must place 4 points for a degree 3 curve.

---
editPoint(ep): [linear, linear, linear]
    properties: create, multiuse
    The x, y, z position of an edit point.  "linear" means that this flag
can take values with units.  This flag can not be used with
the -point or the -pointWeight flags.

---
knot(k): float
    properties: create, multiuse
    A knot value in a knot vector.  One flag per knot value.
There must be (numberOfPoints + degree - 1) knots and the knot
vector must be non-decreasing.

---
name(n): string
    properties: create
    Name of the curve

---
objectSpace(os): boolean
    properties: create
    Points are in object, or "local" space.  This is the default.
You cannot specify both "-os" and "-ws" in the same command.

---
periodic(per): boolean
    properties: create
    If on, creates a curve that is periodic.  Default is off.

---
point(p): [linear, linear, linear]
    properties: create, multiuse
    The x, y, z position of a point.  "linear" means that this flag
can take values with units.

---
pointWeight(pw): [linear, linear, linear, float]
    properties: create, multiuse
    The x,y,z and w values of a point, where the w is a weight value.
A rational curve will be created if this flag is used.
"linear" means that this flag can take values with units.

---
replace(r): boolean
    properties: create
    Replaces an entire existing curve.
If you use this flag, you must specify the name of the curve to
replace, at the end of the command.  (See examples below.)

---
worldSpace(ws): boolean
    properties: create
    Points are in world space.  The default is "-os".
You cannot specify both "-os" and "-ws" in the same command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curve.html 
    """


def curveAddPtCtx(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string) -> string:
    """Synopsis:
---
---
 curveAddPtCtx([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveAddPtCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new context:
cmds.curveAddPtCtx("CurveAddPtCtx")
cmds.setToolTo("CurveAddPtCtx")

---
Return:
---


    string: (name of the new context)

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveAddPtCtx.html 
    """


def curveCVCtx(flagbezier: boolean, flagdegree: uint, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagmultEndKnots: boolean, flagname: string, flagpreserveShape: boolean, flagrational: boolean, flagrefit: boolean, flagsymmetry: boolean, flaguniform: boolean) -> string:
    """Synopsis:
---
---
 curveCVCtx([bezier=boolean], [degree=uint], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [multEndKnots=boolean], [name=string], [preserveShape=boolean], [rational=boolean], [refit=boolean], [symmetry=boolean], [uniform=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveCVCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new context that will create curves of degree 5:
cmds.curveCVCtx( "curveCVContext", degree=5 )
cmds.setToolTo("curveCVContext")

To query the degree of an existing context:
cmds.curveCVCtx( "curveCVContext", q=True, degree=True )

To edit the degree of an existing context:
cmds.curveCVCtx( "curveCVContext", , e=True, degree=7 )

---
Return:
---


    string: (name of the new context)

Flags:
---


---
degree(d): uint
    properties: create, query, edit
    Curve degree

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
multEndKnots(me): boolean
    properties: create, query, edit
    Specify if multiple end knots are to be created.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
preserveShape(ps): boolean
    properties: create, query, edit
    Set this flag to make the operation preserve the shape

---
rational(rl): boolean
    properties: create, query, edit
    Should the curve be rational?

---
refit(rf): boolean
    properties: create, query, edit
    Set this flag to refit the curve

---
symmetry(sm): boolean
    properties: create, query, edit
    Specify if symmetry is to be used

---
uniform(un): boolean
    properties: create, query, edit
    Should the curve use uniform parameterization?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveCVCtx.html 
    """


def curveEPCtx(flagbezier: boolean, flagdegree: uint, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagpreserveShape: boolean, flagpreserveShapeFraction: float, flagrefit: boolean, flaguniform: boolean) -> string:
    """Synopsis:
---
---
 curveEPCtx([bezier=boolean], [degree=uint], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [preserveShape=boolean], [preserveShapeFraction=float], [refit=boolean], [uniform=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveEPCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new context that will create curves of degree 5:
cmds.curveEPCtx( degree=5 )

To query the degree of an existing context:
cmds.curveEPCtx( 'curveEPCtx1', q=True, degree=True )

To edit the degree of an existing context:
cmds.curveEPCtx( 'curveEPCtx1', e=True, degree=7 )

---
Return:
---


    string: (name of the new context)

Flags:
---


---
bezier(bez): boolean
    properties: create, query, edit
    Use bezier curves

---
degree(d): uint
    properties: create, query, edit
    Curve degree

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
preserveShape(ps): boolean
    properties: create, query, edit
    Set this flag to make the operation preserve the shape

---
preserveShapeFraction(pf): float
    properties: create, query, edit
    Fraction value used when preserving the shape

---
refit(rf): boolean
    properties: create, query, edit
    Set this flag to refit the curve

---
uniform(un): boolean
    properties: create, query, edit
    Should the curve use uniform parameterization?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveEPCtx.html 
    """


def curveEditorCtx(flagdirection: int, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagrelativeTangentSize: float, flagtitle: string) -> string:
    """Synopsis:
---
---
 curveEditorCtx([direction=int], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [relativeTangentSize=float], [title=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveEditorCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a curve
cmds.curve(p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9), (12, 10, 2)], k=[0,0,0,1,2,2,2])
Result: curve1 ---


Create a new curve editor context to modify the curve, then switch to it
You can modify the curve using the manipulator handle
cmds.curveEditorCtx('curveEditorCtx1')
cmds.setToolTo('curveEditorCtx1')

---
Return:
---


    string: (name of the new context)

Flags:
---


---
direction(dir): int
    properties: query
    Query the current direction of the tangent control.  Always
zero for the curve case.  In the surface case, its 0 for the normal
direction, 1 for U direction and 2 for V direction.

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
relativeTangentSize(rts): float
    properties: create, query, edit
    Relative size of the tangent manipulator handle.  Helps
to adjust as the surface parameterization controls the size of the
tangent, even if the shape of the surface remains the same.
The default is 4.

---
title(t): string
    properties: query, edit
    The title for the tool.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveEditorCtx.html 
    """


def curveIntersect(flagcaching: boolean, flagconstructionHistory: boolean, flagdirection: tuple[linear, linear, linear], flagdirectionX: linear, flagdirectionY: linear, flagdirectionZ: linear, flagnodeState: int, flagtolerance: linear, flaguseDirection: boolean) -> string:
    """Synopsis:
---
---
 curveIntersect(
string string
    , [caching=boolean], [constructionHistory=boolean], [direction=[linear, linear, linear]], [directionX=linear], [directionY=linear], [directionZ=linear], [nodeState=int], [tolerance=linear], [useDirection=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveIntersect is undoable, queryable, and editable.
This command either returns the parameter values at which the given
pair of curves intersect, or returns a dependency node that provides
the intersection information. If you want to find the intersection of
the curves in a specific direction you must use BOTH the
"-useDirection" flag and the "direction" flag.




Example:
---
import maya.cmds as cmds

cmds.curveIntersect( 'curve1', 'curve2' )
Returns the parameter values that the curves intersect at.
eg. if 6 parameter values are returned, the first 3 are
on curve1 and the last 3 are on curve2.


cmds.curveIntersect( 'curve1', 'curve2', useDirection=True, direction=(0, 1, 0) )
Returns the parameter values that the curves intersect at
when projected along vector (0, 1, 0).  This is useful
for example when you are viewing the two curves in an orthographic
view and the curves appear to intersect, even though
they do not intersect in 3D.

node = cmds.curveIntersect('curve1', 'curve2', ch= True)
p1 = cmds.getAttr(node + ".parameter1" )   or use ".p1"
p2 = cmds.getAttr(node + ".parameter2" )   or use ".p2"
Returns a string which is the name of a new curveIntersect
dependency node.
The "getAttr" commands return the parameter values at
which the curves intersect each other.

---
Return:
---


    string: the parameter values at which two curves intersect.

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
direction(d): [linear, linear, linear]
    properties: query, edit
    The direction that the input curves are projected in
before intersecting.  This vector is only used if
"useDirection" flag is true.

---
directionX(dx): linear
    properties: query, edit
    The X component of the direction that the input curves are projected in
before intersecting.  This vector is only used if "useDirection" flag is true.

---
directionY(dy): linear
    properties: query, edit
    The Y component of the direction that the input curves are projected in
before intersecting.  This vector is only used if "useDirection" flag is true.

---
directionZ(dz): linear
    properties: query, edit
    The Z component of the direction that the input curves are projected in
before intersecting.  This vector is only used if "useDirection" flag is true.

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
    properties: query, edit
    The tolerance that the intersection is calculated with.
For example, given two curves end-to-end, the ends must be
within tolerance for an intersection to be returned.
Default: 0.001

---
useDirection(ud): boolean
    properties: query, edit
    If true, use direction flag.  The input curves are first
projected in a specified direction and then intersected.
If false, this command will only find true 3D intersections.
Default: false

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveIntersect.html 
    """


def curveMoveEPCtx(flagexists: boolean, flagimage1: string, flagimage2: string, flagimage3: string) -> string:
    """Synopsis:
---
---
 curveMoveEPCtx([exists=boolean], [image1=string], [image2=string], [image3=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveMoveEPCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a curve
cmds.curve(p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9), (12, 10, 2)], k=[0,0,0,1,2,2,2])
Result: curve1 ---


Change the selection mode to components, and set edit-point selection mask on only
cmds.selectMode(co=True)
cmds.selectType(allComponents=False, editPoint=True)

Create a new curve edit point editor context, then switch to it
You can move the edit points using manipulator
cmds.curveMoveEPCtx('curveMoveEPCtx1')
cmds.setToolTo('curveMoveEPCtx1')

---
Return:
---


    string: (name of the new context)

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveMoveEPCtx.html 
    """


def curveOnSurface(flagappend: boolean, flagdegree: float, flagknot: float, flagname: string, flagperiodic: boolean, flagpositionUV: tuple[float, float], flagreplace: boolean) -> string:
    """Synopsis:
---
---
 curveOnSurface(
string
string
    , [append=boolean], [degree=float], [knot=float], [name=string], [periodic=boolean], [positionUV=[float, float]], [replace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveOnSurface is undoable, NOT queryable, and NOT editable. To create a curve-on-surface, use the curveOnSurface command.
 To change the degree of a curve, use the rebuildCurve command.
 To change the of parameter range curve, use the rebuildCurve command.

The curve-on-surface command creates a new curve-on-surface from a
list of control vertices (CVs).  A string is returned containing
the pathname to the newly created curve-on-surface.
You can replace an existing curve by using the "-r/replace"
flag. You can append points to an existing curve-on-surface by
using the "-a/append" flag.
See also the curve command, which describes how to query curve
attributes.




Example:
---
import maya.cmds as cmds

These commands create curves with four control vertices.
The first one is created without weights.  The third command
shows how you can use units to specify position.
cmds.curve( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)] )
cmds.curve( pw=[(0, 0, 0, 1), (3, 5, 6, 1), (5, 6, 7, 1), (9, 9, 9, 1)] )
cmds.curve( p=[('0cm', '0cm', '0cm'), ('3in', '5in', '6in'), ('5ft', '6ft', '7ft'), (9, 9, 9)] )

This command replaces an existing curve, curve1, with the given points.
Do not use this flag on a curve that is a result of a construction
history operation.
cmds.curve( 'curve1', r=True, p=[(0, 0, 0), (3, 5, 6), (10, 12, 14), (9, 9, 9)] )

This command adds two CVs to an existing curve, curve1.
The "-ws" flag can be used if the specified CVs are in world space.
Do not use this flag on a curve that is a result of a construction
history operation.
cmds.curve( 'curve1', a=True, p=[(13, 13, 13), (13, 15, 16)] )

This command creates a curve with five control vertices,
with a knot vector. Notice that there must be
(number of CVs + degree - 1) knots and that the knot
vector must be non-decreasing.
cmds.curve( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9), (12, 10, 2)], k=[0,0,0,1,2,2,2] )

This command creates a closed (or "periodic") curve with
four distinct CVs. You must specify a knot vector when the
"-per" flag is used. Notice that the first "degree" points
are the same as the last "degree" points (ie. the first three
points are the same as the last three points). Notice also
that the knot spacing between the first "degree" knots must
be the same as the spacing between the last "degree" knots
(ie. the space between the 1st and 2nd knots is the same as
the space between the 7th and 8th knots, and the space between
the 2nd and 3rd knots is the same as the space between the
8th and 9th knots). There must be space between the first
"degree" knots, unlike the previous example, where the first
"degree" knots are the same.
cmds.curve( per=True, p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9), (0, 0, 0), (3, 5, 6), (5, 6, 7)], k=[-2,-1,0,1,2,3,4,5,6] )

How to query curve properties:

This returns the degree of the curve.  Note that the
number of CVs = degree + spans.
cmds.getAttr( 'curve1.degree' )

This returns the number of spans in the curve.  Note that the
number of CVs = degree + spans.
cmds.getAttr( 'curve1.spans' )

This returns the curve form.
cmds.getAttr( 'curve1.form' )

This returns the minimum parameter value on the curve.
cmds.getAttr( 'curve1.minValue' )

This returns the maximum parameter value on the curve.
cmds.getAttr( 'curve1.maxValue' )

This returns the local x,y,z of the 1st CV.  Use a curve info node if
the curve is a result of a construction history operation.
cmds.getAttr( 'curve1.cv[0]' )

This returns the local x,y,z of the 1st three CVs.  Use a curve info
node if the curve is a result of a construction history operation.
cmds.getAttr( 'curve1.cv[*]' )

This returns the local x,y,z of all CVs.  Use a curve info node if
the curve is a result of a construction history operation.
cmds.getAttr( 'curve1.cv[0:2]' )

This returns the arc length of the curve.  Use "-ch" flag with
the arclen command to get a curve info node that constantly updates
to the current arc length.
cmds.arclen( 'curve1' )

This sequence creates a curve info node, connects the info node to the
curve and queries the knot vector of the curve using the curve info node.
You can use the curve info node to query other attributes such as
world space CV values and arc length.
cmds.createNode( 'curveInfo' )
cmds.connectAttr( 'curveShape1.worldSpace', 'curveInfo1.inputCurve' )
cmds.getAttr( 'curveInfo1.knots[*]' )

cmds.curveOnSurface( 'surface1', d=3, uv=((0, 0),(0.3, 0.5), (0.5, 0.6), (0.9, 1.0)) )
This command creates a curve-on-surface of degree three with
four control vertices on surface1.

cmds.curveOnSurface( 'surface1', uv=((0, 0), (0.3, 0.5), (0.5, 0.6), (0.7, 0.8), (1.0, 1.0)), k=(0, 0, 0, 1, 2, 2, 2) )
This command creates a curve-on-surface with five CVs
and a knot vector, on surface1. Notice that there must be
(number of CVs + degree - 1) knots and that the knot
vector must be non-decreasing.

cmds.curveOnSurface( 'surface1', degree=3, per=True, uv=((0, 0), (0.2, 0.6), (0.4, 0.7), (0.9, 0.9), (0.0, 0.0), (0.2, 0.6), (0.4, 0.7)), k=(-2, -1, 0, 1, 2, 3, 4, 5, 6) )
This command creates a closed (or "periodic") curve-on-surface with
four distinct CVs. You must specify a knot vector when the
"-per" flag is on. Notice that the first "degree" points
are the same as the last "degree" points (ie. the first three
points are the same as the last three points). Notice also
that the knot spacing between the first "degree" knots must
be the same as the spacing between the last "degree" knots
(ie. the space between the 1st and 2nd knots is the same as
the space between the 7th and 8th knots, and the space between
the 2nd and 3rd knots is the same as the space between the
8th and 9th knots). There must be space between the first
"degree" knots, unlike the previous example, where the first
"degree" knots are the same.

cmds.curveOnSurface( 'surface1->curve1', append=True, uv=(1.0, 1.0) )
This command appends a point to an existing curve-on-surface.
Notice that the curve-on-surface is specified, not just the surface.

cmds.curveOnSurface( 'surface1->curve1', replace=True, d=1, uv=((1.0, 1.0), (2.0, 2.0)) )
This command replaces an existing curve, surface1->curve1, with a
new curve of degree 1 having the given points. Do not use this
flag on a curve that is a result of a construction history operation.

---
Return:
---


    string: - name of new curve-on-surface
    string: The path to the new curve or the replaced curve

Flags:
---


---
append(a): boolean
    properties: create
    Appends point(s) to the end of an existing curve.
If you use this flag, you must specify the name of the
curve to append to, at the end of the command.  (See examples below.)

---
degree(d): float
    properties: create
    The degree of the new curve.  Default is 3.  Note that you need
(degree+1) curve points to create a visible curve span.  eg. you
must place 4 points for a degree 3 curve.

---
knot(k): float
    properties: create, multiuse
    A knot value in a knot vector.  One flag per knot value.
There must be (numberOfPoints + degree - 1) knots and the knot
vector must be non-decreasing.

---
name(n): string
    properties: create
    Name of the curve

---
periodic(per): boolean
    properties: create
    If on, creates a curve that is periodic.  Default is off.

---
positionUV(uv): [float, float]
    properties: create, multiuse
    The uv position of a point.

---
replace(r): boolean
    properties: create
    Replaces an entire existing curve.
If you use this flag, you must specify the name of the curve to
replace, at the end of the command.  (See examples below.)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveOnSurface.html 
    """


def curveRGBColor(flaghueSaturationValue: boolean, flaglist: boolean, flaglistNames: boolean, flagremove: boolean, flagresetToFactory: boolean, flagresetToSaved: boolean) -> float[]:
    """Synopsis:
---
---
 curveRGBColor([hueSaturationValue=boolean], [list=boolean], [listNames=boolean], [remove=boolean], [resetToFactory=boolean], [resetToSaved=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveRGBColor is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Set all "translateX" curves to draw magenta
cmds.curveRGBColor( 'translateX', 1, 0, 1 )

Set all curves whose names end in "Y" to draw yellow
cmds.curveRGBColor( '*Y', 1, 1, 0 )

Remove the custom color for "translateX" curves
(which will revert to the standard UI color)
cmds.curveRGBColor( r=True, 'translateX' )

List the currently defined custom curve colors
cmds.curveRGBColor( list=True )

---
Return:
---


    float[]: HSV values from querying the hsv flag

Flags:
---


---
hueSaturationValue(hsv): boolean
    properties: create, query
    Indicates that rgb values are really hsv values.

---
list(l): boolean
    properties: create
    Writes out a list of all curve color names and their values.

---
listNames(ln): boolean
    properties: create
    Returns an array of all curve color names.

---
remove(r): boolean
    properties: create
    Removes the named curve color.

---
resetToFactory(rf): boolean
    properties: create
    Resets all the curve colors to their factory defaults.

---
resetToSaved(rs): boolean
    properties: create
    Resets all the curve colors to their saved values.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveRGBColor.html 
    """


def curveSketchCtx(flagdegree: uint, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 curveSketchCtx(
[object]
    , [degree=uint], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

curveSketchCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new sketch context, which creates degree 3 curves:
cmds.curveSketchCtx( "pencilContext", degree=3 )
cmds.setToolTo("pencilContext")

To query the degree of an existing context:
cmds.curveSketchCtx( "pencilContext",q=True, degree=True )

To edit the degree of an existing context:
cmds.curveSketchCtx( "pencilContext", e=True, degree=1 )

---
Return:
---


    string: (name of the new curve sketch context)

Flags:
---


---
degree(d): uint
    properties: create, query, edit
    Valid values are 1 or 3

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/curveSketchCtx.html 
    """


def cutKey(flaganimation: string, flagattribute: string, flagclear: boolean, flagcontrolPoints: boolean, flagfloat: floatrange, flaghierarchy: string, flagincludeUpperBound: boolean, flagindex: uint, flagoption: string, flagselectKey: boolean, flagshape: boolean, flagtime: timerange) -> int:
    """Synopsis:
---
---
 cutKey(
[targetList]
    , [animation=string], [attribute=string], [clear=boolean], [controlPoints=boolean], [float=floatrange], [hierarchy=string], [includeUpperBound=boolean], [index=uint], [option=string], [selectKey=boolean], [shape=boolean], [time=timerange])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cutKey is undoable, NOT queryable, and NOT editable.
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

The cutKey command cuts curve segment hierarchies from specified
targets and puts them in the clipboard.  The pasteKey command
applies these curves to other objects.

The shape of the cut curve placed in the clipboard, and
the effect of the cutKey command on the source animation curve
depends on the cutKey "-option" specified.  Each of these options
below will be explained using an example.  For all the explanations,
let us assume that the source animation curve (from which keys will
be cut) has 5 keyframes at times 10, 15, 20, 25, and 30.

TbaseKeySetCmd.h


 cutKey -t "12:22" -option keys

Keyframes at times 15 and 20 are removed. All other keys are unchanged.
A 5-frame animation curve is placed into the keyset clipboard.

 cutKey -t "12:22" -option keysCollapse

Keyframes at times 15 and 20 are removed.  Shift all keys after time 20
to the left by 5 frames, preserving all their values.
A 5-frame animation curve is placed into the keyset clipboard.

 cutKey -t "12:22" -option keysConnect

Keyframes at times 15 and 20 are removed.  Shift all keys after time 20
to the left by 5 frames, and place the key that used to be at time 25 at the
value of the key that used to be at time 15.
A 5-frame animation curve is placed into the keyset clipboard.

 cutKey -t "12:22" -option curve

Keyframes at times 15 and 20 are removed.  Keys are inserted at
times 12 and 22.
A 10-frame animation curve is placed into the keyset clipboard.

 cutKey -t "12:22" -option curveCollapse

Keyframes at times 15 and 20 are removed.  Keys are inserted at
times 12 and 22.  Shift all keys from time 22 to the left by 10 frames,
preserving their values.
A 10-frame animation curve is placed into the keyset clipboard.

 cutKey -t "12:22" -option curveConnect

Keyframes at times 15 and 20 are removed.  Keys are inserted at
times 12 and 22.  Shift all keys from time 22 to the left by 10 frames,
and replace the key inserted at time 12 with the newly inserted key
at time 22.
A 10-frame animation curve is placed into the keyset clipboard.

 cutKey -t "12:22" -option areaCollapse

Keyframes at times 15 and 20 are removed. Shift all keys from time 22
to the left by 10 frames, preserving their values.
A 10-frame animation curve is placed into the keyset clipboard.






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

Cut keyframes from frame 10 to 20 of cube1's "Translate X" attribute
---

cmds.cutKey( 'cube1', time=(10,20), attribute='translateX', option="keys" )

Cut from all active objects all keys in the range 0 to 60
---

cmds.cutKey( time=(0,60) )

---
Return:
---


    int: Number of animation curves cut.

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
clear(cl): boolean
    properties: create
    Just remove the keyframes (i.e. do not overwrite the clipboard)

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
option(o): string
    properties: create
    Option for how to perform the cutKey operation.  Valid
values for this flag are "keys", "curve",
"curveCollapse", "curveConnect", "areaCollapse".  The default cut
option is: keys

---
selectKey(sl): boolean
    properties: create
    Select the keyframes of curves which have had keys removed

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cutKey.html 
    """


def cycleCheck(flagall: boolean, flagchildren: boolean, flagdag: boolean, flagevaluation: boolean, flagfirstCycleOnly: boolean, flagfirstPlugPerNode: boolean, flaglastPlugPerNode: boolean, flaglist: boolean, flaglistSeparator: string, flagparents: boolean, flagsecondary: boolean, flagtimeLimit: time) -> boolean | list[string]:
    """Synopsis:
---
---
 cycleCheck(
string[]
    , [all=boolean], [children=boolean], [dag=boolean], [evaluation=boolean], [firstCycleOnly=boolean], [firstPlugPerNode=boolean], [lastPlugPerNode=boolean], [list=boolean], [listSeparator=string], [parents=boolean], [secondary=boolean], [timeLimit=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cycleCheck is undoable, queryable, and NOT editable.
Normally the return value is a boolean indicating whether or not the
given items were involved in a cycle.  If the -list flag is used then
the return value is the list of all plugs in cycles (involving the
selected plug or node if any).

Note that it is possible for evaluation cycles to occur even where
no DG connections exist. Here are some examples:

1) Nodes with evaluation-time dependent connections: An example is
expression nodes, because we cannot tell what an expression
node is actually referring to until it is evaluated, and such
evaluation-time dependent nodes may behave differently based on
the context (e.g. time) they are evaluated at. If you suspect a
cycle due to such a connection, the best way to detect the
cycle is through manual inspection.

2) Cycles due to DAG hierarchy: noting that DAG nodes are implicitely
connected through parenting, if a child DAG node connects an output into
the input of a parent node, a cycle will exist if the plugs involved
also affect each other. In order to enable detection of cycles
involving the DAG, add the -dag flag to the command line.

Note also that this command may incorrectly report a cycle on
an instanced skeleton where some of the instances use IK.
You will have to examine the reported cycle yourself to determine
if it is truly a cycle or not.
The evaluation time cycle checking will not report false cycles.




Example:
---
import maya.cmds as cmds

Print a message if xNode.tx is in a cycle.
cmds.createNode( 'transform', n='xNode' )
if cmds.cycleCheck('xNode.tx') > 0:
  print('xNode.tx is in a cycle')

Get the list of plugs in a cycle with xNode.ty
cmds.connectAttr( 'xNode.tx', 'xNode.ty' )
cmds.connectAttr( 'xNode.ty', 'xNode.tx' )
cycles = cmds.cycleCheck()

Print a message if there are any cycles in the graph.
if cmds.cycleCheck(all=True, tl='10sec') > 0:
  print("Your graph has a cycle.")
else:
  print("Your graph probably does not have a cycle")

List all cycles involving the DG and DAG hierarchy.
cmds.cycleCheck(all=True,dag=True,l=True )

---
Return:
---


    boolean: in the general case.
    list[string]: When the list flag is used.

Flags:
---


---
all(all): boolean
    properties: create
    search the entire graph for cycles instead of the selection list.
(Note: if nothing is selected, -all is assumed).

---
children(c): boolean
    properties: create
    Do not consider cycles on the children, only the specified plugs

---
dag(dag): boolean
    properties: create
    Also look for cycles due to relationships in the DAG. For each DAG node,
the parenting connection on its children is also considered when searching
for cycles.

---
evaluation(e): boolean
    properties: create, query
    Turn on and off cycle detection during graph evaluation

---
firstCycleOnly(fco): boolean
    properties: create
    When -list is used to return a plug list, the list may contain
multiple cycles or partial cycles. When -firstCycleOnly is specified
only the first such cycle (which will be a full cycle) is returned.

---
firstPlugPerNode(fpn): boolean
    properties: create
    When -list is used to return a plug list, the list will typically contain
multiple plugs per node (e.g. ... A.output B.input B.output C.input ...),
reflecting internal "affects" relationships rather than external DG connections.
When -firstPlugPerNode is specified, only the first plug in the list for each
node is returned (B.input in the example).

---
lastPlugPerNode(lpn): boolean
    properties: create
    When -list is used to return a plug list, the list will typically contain
multiple plugs per node (e.g. ... A.output B.input B.output C.input ...),
reflecting internal "affects" relationships rather than external DG connections.
When -lastPlugPerNode is specified, only the last plug in the list for each
node is returned (B.output in the example).

---
list(l): boolean
    properties: create
    Return all plugs involved in one or more cycles.  If not
specified, returns a boolean indicating whether a cycle exists.

---
listSeparator(ls): string
    properties: create
    When -list is used to return a plug list, the list may contain
multiple cycles or partial cycles. Use -listSeparator to specify
a string that will be inserted into the returned string array
to separate the cycles.

---
parents(p): boolean
    properties: create
    Do not consider cycles on the parents, only the specified plugs

---
secondary(s): boolean
    properties: create
    Look for cycles on related plugs as well as the specified plugs
Default is "on" for the "-all" case and "off" for others

---
timeLimit(tl): time
    properties: create
    Limit the search to the given amount of time

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cycleCheck.html 
    """


def cylinder(flagaxis: tuple[linear, linear, linear], flagcaching: boolean, flagconstructionHistory: boolean, flagdegree: int, flagendSweep: angle, flagheightRatio: float, flagname: string, flagnodeState: int, flagobject: boolean, flagpivot: tuple[linear, linear, linear], flagpolygon: int, flagradius: linear, flagsections: int, flagspans: int, flagstartSweep: angle, flagtolerance: linear, flaguseTolerance: boolean) -> list[string]:
    """Synopsis:
---
---
 cylinder([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean], [degree=int], [endSweep=angle], [heightRatio=float], [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [radius=linear], [sections=int], [spans=int], [startSweep=angle], [tolerance=linear], [useTolerance=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

cylinder is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.cylinder()
cmds.cylinder( ch=True, radius=10, hr=3 )
cmds.cylinder( r=5, axis=(1, 1, 1), pivot=(0, 0, 1), ssw='0deg', esw='90deg' )
cmds.cylinder( ut=True, tol=0.01 )

---
Query the radius of the selected cylinder
r = cmds.cylinder( q=True, r=True )

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
    The degree of the resulting surface:
1 - linear,
3 - cubic
Default: 3

---
endSweep(esw): angle
    properties: create, query, edit
    The angle at which to end the surface of revolution.
Default is 2Pi radians, or 360 degrees.
Default: 6.2831853

---
heightRatio(hr): float
    properties: create, query, edit
    Ratio of "height" to "width"
Default: 2.0

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
    The primitive's pivot point

---
radius(r): linear
    properties: create, query, edit
    The radius of the object
Default: 1.0

---
sections(s): int
    properties: create, query, edit
    The number of sections determines the resolution of the surface in the sweep direction.
Used only if useTolerance is false.
Default: 8

---
spans(nsp): int
    properties: create, query, edit
    The number of spans determines the resolution of the surface in the opposite direction.
Default: 1

---
startSweep(ssw): angle
    properties: create, query, edit
    The angle at which to start the surface of revolution
Default: 0

---
tolerance(tol): linear
    properties: create, query, edit
    The tolerance with which to build the surface.
Used only if useTolerance is true
Default: 0.01

---
useTolerance(ut): boolean
    properties: create, query, edit
    Use the specified tolerance to determine resolution.
Otherwise number of sections will be used.
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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/cylinder.html 
    """
