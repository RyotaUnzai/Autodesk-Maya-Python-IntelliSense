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


def editDisplayLayerGlobals(flagbaseId: int, flagcurrentDisplayLayer: name, flagmergeType: int, flaguseCurrent: boolean) -> boolean | int | string:
    """Synopsis:
---
---
 editDisplayLayerGlobals([baseId=int], [currentDisplayLayer=name], [mergeType=int], [useCurrent=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editDisplayLayerGlobals is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.editDisplayLayerGlobals( cdl='displayLayer1' )

cmds.editDisplayLayerGlobals( query=True, cdl=True )
Result: displayLayer1

cmds.editDisplayLayerGlobals( 'bi', query=True )
Result: 10

cmds.editDisplayLayerGlobals( useCurrent='on' )

---
Return:
---


    boolean: Command success
    string: Current display layer name, when querying
    int: Merge type, when querying
    int: Base ID, when querying

Flags:
---


---
baseId(bi): int
    properties: create, query
    Set base layer ID.  This is the number at which new layers start searching
for a unique ID.

---
currentDisplayLayer(cdl): name
    properties: create, query
    Set current display layer; ie. the one that all new objects are added to.

---
mergeType(mt): int
    properties: create, query
    Set file import merge type.  Valid values are 0, none, 1, by number, and
2, by name.

---
useCurrent(uc): boolean
    properties: create, query
    Set whether or not to enable usage of the current display layer as the
destination for all new nodes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editDisplayLayerGlobals.html 
    """


def editDisplayLayerMembers(flagclear: boolean, flagfullNames: boolean, flagnoRecurse: boolean, flagufeObjects: boolean) -> int | list[string]:
    """Synopsis:
---
---
 editDisplayLayerMembers([clear=boolean], [fullNames=boolean], [noRecurse=boolean], [ufeObjects=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editDisplayLayerMembers is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

cmds.editDisplayLayerMembers( 'displayLayer1', 'sphere1', 'cone1' )
Result : 2

cmds.editDisplayLayerMembers( 'displayLayer1', query=True )
Result : sphere1 cone1

cmds.editDisplayLayerMembers( 'displayLayer1', 'expression1', 'sphere2' )
Warning : Only DAG objects can be in a display layer.  'expression1' ignored.
Result : 1

ufeSel = cmds.ls(selection=True, ufe=True)
cmds.editDisplayLayerMembers('layer1', ufeSel, noRecurse=True)
// Result: 1

cmds.editDisplayLayerMembers('layer1', clear=True)
Result: 1

---
Return:
---


    int: Number of objects added to the layer
    list[string]: Query: List of objects in layer

Flags:
---


---
clear(clr) 2024: boolean
    properties: create
    Remove all the objects contained in the layer by moving them to the default layer.

---
fullNames(fn): boolean
    properties: query
    (Query only.) If set then return the full DAG paths of the objects in the
layer.  Otherwise return just the name of the object.

---
noRecurse(nr): boolean
    properties: create, query
    If set then only add selected objects to the display layer.  Otherwise all
descendants of the selected objects will also be added.

---
ufeObjects(ufe) 2024: boolean
    properties: query
    (Query only.) If set will return objects that are
defined through the UFE interface as well as native Maya objects.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editDisplayLayerMembers.html 
    """


def editMetadata(flagchannelName: string, flagchannelType: string, flagendIndex: string, flagindex: string, flagindexType: string, flagmemberName: string, flagremove: boolean, flagscene: boolean, flagstartIndex: string, flagstreamName: string, flagstringValue: string, flagvalue: float) -> string:
    """Synopsis:
---
---
 editMetadata([channelName=string], [channelType=string], [endIndex=string], [index=string], [indexType=string], [memberName=string], [remove=boolean], [scene=boolean], [startIndex=string], [streamName=string], [stringValue=string], [value=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editMetadata is undoable, NOT queryable, and NOT editable.
This command is used to set metadata elements onto or remove metadata
elements from an object. Before using this command you must first attach
a metadata stream type to the object using the addMetadata command
or an API equivalent. The command has four basic variations:

Set per-component metadata on meshes
Remove per-component metadata on meshes
Set generic metadata on any object
Remove generic metadata on any object


The difference between the set and remove variations
(1,3 vs. 2,4) is that set requires both a member name to be set
and a new value to be set. (The reason removal doesn't use a member
name is that you can only remove an entire metadata structural element,
you cannot remove only a single member from it.)


When metadata values are set or removed the action is performed on
every selected component or index. This provides an easy method to
set or remove a bunch of metadata en masse.


The general usage (variations 3, 4) lets you select specific pieces
of metadata through the channelName and index
flags. Note that since index is a multi-use flag you
can select many different elements from the same Channel and set or
remove the metadata on all of them in one command.


Metadata on meshes is special in that the Channel types "vertex",
"edge", "face", and "vertexFace" are directly connected to the
components of the same name. To make setting these metadata
Channels easier you can simply select or specify on the command
line the corresponding components rather than using the channelName
and index flags. For example the selection "myMesh.vtx[8:10]"
corresponds to channelName = vertex and index = 8, 9, 10
(as a multi-use flag).


Note that the metadata is assigned to an object and except in the special
case of mesh geometry does not flow through the dependency graph. In
meshes the metadata will move from node to node wherever the geometry
is connected, although it will not adjust itself automatically for changes
in topology. Internal data is arranged to minimize the amount of copying
no matter how many other nodes are connected to it.


Only a single node or scene, component type, channel type, and value type
are allowed in a single command. This keeps the data simple at the possible
cost of requiring multiple calls to the command to set more than one
structure member's value.


Certain nodes have metadata supplied by input attributes. If you edit one
of those with an incoming connection on such an attribute then the metadata
edit will not be applied directly it will be put into an 'editMetadata' node
for application during DG evaluation. Since the details of the metadata are
not known until the evaluation happens less rigorous compatibility checking
is performed. The editMetadata node has its own facilities for verifying and
reporting illegal metadata edits. Successive edits to the same metadata in
this way appends each edit to the same editMetadata node.




Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.polyPlane( name='smcPlane', constructionHistory=False )
Result: smcPlane ---

cmds.pickWalk( d='down' )
Result: [u'smcPlaneShape'] ---


Create structure
cmds.dataStructure( format='raw', asString='name=idStructure:int32=ID' )
Result: idStructure ---


Apply structure to plane
cmds.addMetadata( structure='idStructure', streamName='idStream', channelName='vertex' )

Attach a metadata value to three of the components by selection
cmds.select( 'smcPlaneShape.vtx[8:10]', replace=True )
cmds.editMetadata( streamName='idStream', memberName='ID', value=7 )
Result: True ---


Attach a metadata value to another component by manual indexing
cmds.select( 'smcPlaneShape', replace=True )
cmds.editMetadata( streamName='idStream', memberName='ID', channelName='vertex', value=8, index=14 )
Result: True ---


Remove metadata from the middle of the three vertexes set earlier
cmds.select( 'smcPlaneShape.vtx[9]', replace=True )
cmds.editMetadata( streamName='idStream', remove=True )
Result: True ---


---
Return:
---


    string: Name of the node where the new edits reside, empty string if edits failed. It will be an editMetadata node if construction history was present.

Flags:
---


---
memberName(mn): string
    properties: create
    Name of the Structure member being edited. The names of the members are
set up in the Structure definition, either through the description passed
in through the "dataStructure" command or via the API used to create that
Structure.

---
remove(rem): boolean
    properties: create
    If the remove flag is set then the metadata will be removed rather
than have values set. In this mode the "memberName", "value", and
"stringValue" flags are ignored. "memberName" is ignored because when
deleting metadata all members of a structure must be removed as a group.
The others are ignored since when deleting you don't need a value to be set.

---
stringValue(sv): string
    properties: create, multiuse
    String value to be set into the specified metadata locations. This flag
can only be used when the data member is a numeric type. If the member has
N dimensions (e.g. string[2]) then this flag must appear N times (e.g. 2 times)
The same values are applied to the specified metadata member on all affected
components or metadata indices.
Only one of the value, and stringValue flags can be specified at once and the
type must match the type of the structure member named by the "member" flag.

---
value(v): float
    properties: create, multiuse
    Numeric value to be set into the specified metadata locations. This flag
can only be used when the data member is a numeric type. If the member has
N dimensions (e.g. float[3]) then this flag must appear N times (e.g. 3 times)
The same values are applied to the specified metadata member on all affected
components or metadata indices. All numeric member types should use this type
of value specification, i.e. everything except string and matrix types.
Only one of the value, and stringValue flags can be specified at once and the
type must match the type of the structure member named by the "member" flag.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editMetadata.html 
    """


def editRenderLayerAdjustment(flagattributeLog: boolean, flaglayer: name, flagnodeLog: boolean, flagremove: boolean) -> int | list[string]:
    """Synopsis:
---
---
 editRenderLayerAdjustment([attributeLog=boolean], [layer=name], [nodeLog=boolean], [remove=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editRenderLayerAdjustment is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Create two adjustments for layer1
cmds.editRenderLayerAdjustment( 'lambert1.color', 'lambert1.diffuse', layer='layer1' )
Result : 2

List all the adjustments to renderlayer1
cmds.editRenderLayerAdjustment( 'layer1', query=True, layer=True )
Result : lambert1.color lambert1.diffuse

Create adjustments for the current render layer
cmds.editRenderLayerAdjustment( 'lambert1.color' )
Result : 1

Remove one adjustment from the current render layer
cmds.editRenderLayerAdjustment( 'lambert1.color', remove=True )
Result : 1

Query the current layer for the list of adjustments
cmds.editRenderLayerAdjustment( query=True, alg=True )
castsShadows         nurbsSphereShape1.castsShadows
                     pPlaneShape1.castsShadows
                     pSphereShape1.castsShadows
instObjGroups        pCylinderShape1.instObjGroups[0]
motionBlurByFrame    defaultRenderGlobals.motionBlurByFrame
receiveShadows       nurbsSphereShape1.receiveShadows
                     pPlaneShape1.receiveShadows
                     pSphereShape1.receiveShadows
shadingSamples       defaultRenderQuality.shadingSamples

---
Return:
---


    int: Number of adjustments applied
    list[string]: Query: List of plugs adjustments to layer

Flags:
---


---
attributeLog(alg): boolean
    properties: query
    Output all adjustments for the specified layer sorted by attribute name.

---
layer(lyr): name
    properties: create, query
    Specified layer in which the adjustments will be modified. If not specified
the active render layer will be used.

---
nodeLog(nlg): boolean
    properties: query
    Output all adjustments for the specified layer sorted by node name.

---
remove(r): boolean
    properties: create
    Remove the specified adjustments from the render layer. If an adjustment
is removed from the current layer, the specified plug will revert back to
it's master value determined by the default render layer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerAdjustment.html 
    """


def editRenderLayerGlobals(flagbaseId: int, flagcurrentRenderLayer: name, flagenableAutoAdjustments: boolean, flagmergeType: int, flaguseCurrent: boolean) -> boolean | int | string:
    """Synopsis:
---
---
 editRenderLayerGlobals([baseId=int], [currentRenderLayer=name], [enableAutoAdjustments=boolean], [mergeType=int], [useCurrent=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editRenderLayerGlobals is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.editRenderLayerGlobals( currentRenderLayer='layer1' )

cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True )
Result: layer1

cmds.editRenderLayerGlobals( query=True, baseId=True )
Result: 1

cmds.editRenderLayerGlobals( useCurrent=True )

Enable automatic creation of adjustments
cmds.editRenderLayerGlobals( enableAutoAdjustments=True )

---
Return:
---


    boolean: Command success
    string: Current render layer name, when querying
    int: Merge type, when querying
    int: Base ID, when querying

Flags:
---


---
baseId(bi): int
    properties: create, query
    Set base layer ID.  This is the number at which new layers start searching
for a unique ID.

---
currentRenderLayer(crl): name
    properties: create, query
    Set current render layer. This will will update the renderLayerManger and
all DAG objects to identify them as members of the render layer. This
flag may also be used in conjunction with "useCurrent" to automatically
add new DAG objects to the active layer. The "isCurrentRenderLayerChanging"
condition can be used to determine when the current layer is being changed
and adjustments are being applied to the scene.

---
enableAutoAdjustments(eaa): boolean
    properties: create, query
    Set whether or not to enable automatic creation of adjustments when
certain attributes (ie. surface render stats, shading group assignment,
or render settings) are changed.

---
mergeType(mt): int
    properties: create, query
    Set file import merge type.  Valid values are 0, none, 1, by number, and
2, by name.

---
useCurrent(uc): boolean
    properties: create, query
    Set whether or not to enable usage of the current render layer as the
destination for all new nodes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerGlobals.html 
    """


def editRenderLayerMembers(flagfullNames: boolean, flagnoRecurse: boolean, flagremove: boolean) -> int | list[string]:
    """Synopsis:
---
---
 editRenderLayerMembers([fullNames=boolean], [noRecurse=boolean], [remove=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editRenderLayerMembers is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.editRenderLayerMembers( 'layer1', 'sphere1', 'cone1' )
Result : 4

cmds.editRenderLayerMembers( 'layer1', query=True )
Result : sphere1 sphere1Shape cone1 cone1Shape

cmds.editRenderLayerMembers( 'layer1', 'expression1', 'sphere2' )
Result : 2

cmds.editRenderLayerMembers( 'layer1', 'sphere1', remove=True)
Result : 2

---
Return:
---


    int: Number of objects added to the layer
    list[string]: Query: List of objects in layer

Flags:
---


---
fullNames(fn): boolean
    properties: query
    (Query only.) If set then return the full DAG paths of the objects in the
layer.  Otherwise return just the name of the object.

---
noRecurse(nr): boolean
    properties: create
    If set then only add selected objects to the render layer.  Otherwise all
descendants of the selected objects will also be added. This flag may be
applied to adding or removing objects from the layer.

---
remove(r): boolean
    properties: create
    Remove the specified objects from the render layer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerMembers.html 
    """


def editor(flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaghighlightConnection: string, flaglockMainConnection: boolean, flagmainListConnection: string, flagpanel: string, flagparent: string, flagselectionConnection: string, flagstateString: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 editor(
editorName
    , [control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightConnection=string], [lockMainConnection=boolean], [mainListConnection=string], [panel=string], [parent=string], [selectionConnection=string], [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To change the selection connection for any editor
---

cmds.editor( 'anyEditor', edit=True, mainListConnection='newConnection' )

---
Return:
---


    string: Name of the editor

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editor.html 
    """


def editorTemplate(flagaddAdskAssetControls: boolean, flagaddComponents: boolean, flagaddControl: tuple[string, script], flagaddDynamicControl: tuple[string, script], flagaddExtraControls: boolean, flagaddSeparator: boolean, flagannotateFieldOnly: boolean, flagannotation: string, flagbeginLayout: string, flagbeginNoOptimize: boolean, flagbeginScrollLayout: boolean, flagcallCustom: tuple[script, script], flagcollapse: boolean, flagdebugMode: boolean, flagdimControl: tuple[string, string, boolean], flagendLayout: boolean, flagendNoOptimize: boolean, flagendScrollLayout: boolean, flagextraControlsLabel: string, flagforceRebuild: boolean, flaginterruptOptimize: boolean, flaglabel: string, flaglistExtraAttributes: string, flagpreventOverride: boolean, flagqueryControl: tuple[string, string], flagqueryLabel: tuple[string, string], flagqueryName: tuple[string, string], flagsuppress: string) -> string:
    """Synopsis:
---
---
 editorTemplate([addAdskAssetControls=boolean], [addComponents=boolean], [addControl=[string, script]], [addDynamicControl=[string, script]], [addExtraControls=boolean], [addSeparator=boolean], [annotateFieldOnly=boolean], [annotation=string], [beginLayout=string], [beginNoOptimize=boolean], [beginScrollLayout=boolean], [callCustom=[script, script]], [collapse=boolean], [debugMode=boolean], [dimControl=[string, string, boolean]], [endLayout=boolean], [endNoOptimize=boolean], [endScrollLayout=boolean], [extraControlsLabel=string], [forceRebuild=boolean], [interruptOptimize=boolean], [label=string], [listExtraAttributes=string], [preventOverride=boolean], [queryControl=[string, string]], [queryLabel=[string, string]], [queryName=[string, string]], [suppress=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

editorTemplate is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

You will most likely want to use this command when defining the controls
that appear in the Attribute Editor for a custom node created in a plugin.

To see how this is done compile and load the transCircleNode plugin. Then
create a node of type "transCircle" and show the Attribute Editor.

Now look at the AEtransCircleTemplate.mel script to see how the
editorTemplate command is used to define the controls that appear in
the Attribute Editor.

As you may have noticed the name of the template script must match the
node type you create, ie. AEnodeTypeTemplate.mel.

---
Return:
---


    string: For queryControl, the appropriate attribute type will be
returned.
string array
For listExtraAttributes, extra attributes will be returned.

Flags:
---


---
addAdskAssetControls(aac): boolean
    properties: create
    Adds controls for dynamic attributes of adskMaterial nodes
and organizes them in a layout according to the XML ui
description specified in the asset library.

---
addComponents(acp): boolean
    properties: create
    This flag will add a frameLayout with a channel box
which will display any selected components for the
object.

---
addControl(ac): [string, script]
    properties: create
    The first argument is the name of the attribute for which
you wish to add a control. You can assume that when the editor
is created from the template, an appropriate type of control
will be used.
The second string argument is optional, and can be used
to specify a command (or script) to be executed when the
attribute is changed.

---
addDynamicControl(adc): [string, script]
    properties: create
    As -addControl with the exception that the attribute
for which the control is to be created/attached is dynamic.
[Note: -addControl will also work for dynamic attributes,
but will not preserve their order in the attribute editor].

---
addExtraControls(aec): boolean
    properties: create
    By default, if there are attributes of a node which you do
not -addControl or -suppress, then controls will be created
automatically and appended to the end of editor created from the
template. This flag allows you to specify a particular place
in the template for such controls to be automatically inserted.
If dynamic attributes have not already been addressed
with -addControl, they will also be placed here.  A frameLayout
will automatically be generated for you when you use this flag.

---
addSeparator(addSeparator): boolean
    properties: create
    Adds a separator to the template.

---
annotateFieldOnly(afo): boolean
    properties: create
    This flag can only be used with the -annotation flag.  By
default, for any Attribute Editor controlGroups created by
the -addControl flag, the -annotation flag displays its
annotation string when the mouse hovers over any control
that is part (the label, the value field, etc.) of the
group.  Use this flag to limit display of the annotation to
only the value field of the controlGroup.  This flag is
ignored if the controlGroup has no value field (e.g., checkBoxGrp)

---
annotation(ann): string
    properties: create
    This flag can only be used with the -addControl or
the -addDynamicControl flags. The string will be used as
an annotation on the controls created in the attribute editor.

---
beginLayout(bl): string
    properties: create
    Begins a layout in the template with the title specified
by the string argument.
Items between this flag and    its corresponding -endLayout flag
will be contained within the layout. You can assume that when
the editor is created from the template, an appropriate type of
layout will be used. (frameLayout).

---
beginNoOptimize(bn): boolean
    properties: create
    Specifies that the layout of items between this flag and its
corresponding -endNoOptimize flag is not to be optimized to
minimize space.

---
beginScrollLayout(bsl): boolean
    properties: create
    Begins a scrollLayout.  Items between this flag and its
corresponding -endScrollLayout flag will be contained within
the layout.

---
callCustom(ccu): [script, script]
    properties: create
    Specifies that at this point in the template when building the
dialog, the procedure specified by the first argument is to be
called to create some UI objects when a new node type is edited.
The procedure specified by the second argument is to be called if
an attribute editor already exists and another node of the same
type is now to be edited. The replacing procedure should connect
any controls created by the creating procedure to the equivalent
attributes in the new node. A list of zero or more attributes
specifies the attributes which the two procedures will involve.
The procedures should have the signature:

proc AEcustomNew(string attributeName1, string attributeName2)

The number of attributes specified in the call should correspond
to the number of attributes in the procedure signature.

---
collapse(cl): boolean
    properties: create
    This flag is only valid when used in conjunction with
a -bl/beginLayout flag.  It is used to specify the initial
expand/collapse state of the layout.  A true value will cause the
layout to be collapsed upon creation, while a false value will
expand the layout.  The default is true (ie. collapsed).

---
debugMode(dbm): boolean
    properties: create
    Set debugging mode for the template

---
dimControl(dc): [string, string, boolean]
    properties: create
    This flag is only useful AFTER a control has already been
created (using the -addControl flag).  The first argument
is the node name and the second is the attribute
whose control you wish to affect.  The third argument is a
boolean which specifies whether to dim (true) or undim (false)
the associated control.

---
endLayout(el): boolean
    properties: create
    Ends a layout in the template started by -beginLayout.

---
endNoOptimize(en): boolean
    properties: create
    Ends a set of non-optimized items.

---
endScrollLayout(esl): boolean
    properties: create
    Ends a scrollLayout.

---
extraControlsLabel(ecl): string
    properties: create
    By default the label is "Extra Attributes". Specify an
alternate label or an empty string to hide the label. This flag
must be used in conjuction with the -aec/addExtraControls flag.

---
forceRebuild(fr): boolean
    properties: create
    Force a template to always destroy/create itself rather
than use the replace feature.  Both the default replace
behavior and force rebuild preserve the collapse/expand
status of all the layout sections.

---
interruptOptimize(io): boolean
    properties: create
    Enforces a division between two sets of items whose layouts
may be optimized.

---
label(l): string
    properties: create
    This flag can only be used with the -addControl or
the -addDynamicControl flags.  And it must be specified FIRST.
The string will override the name of the attribute that
will be displayed in the attribute editor.

---
listExtraAttributes(lea): string
    properties: create
    List extra attributes.This flag is only useful AFTER a control
has already been created (using the -addControl flag). The
first argument is the node name.

---
preventOverride(po): boolean
    properties: create
    If true, this flag disallows overriding the control's
attribute via the control's right mouse button menu.

---
queryControl(qc): [string, string]
    properties: create
    This flag is only useful AFTER a control has already been
created (using the -addControl flag).  The first argument is
the node name and the second is the attribute whose control
you wish to query.  Note that in most cases, using this
flag is identical to issuing a getAttr command, however, in
the case of textFields (e.g. for message attributes), the text
value currently being displayed will be returned, NOT the actual
attribute value.

---
queryLabel(ql): [string, string]
    properties: create
    This flag is only useful AFTER a control has already been
created (using the -addControl flag).  The first argument is
the node name and the second is the attribute whose control
label you wish to query.  In most cases this flag
returns the same value as the attribute's nice name,
but when a -label flag was present on the -addControl command that
created the control, -queryLabel will return that value instead

---
queryName(qn): [string, string]
    properties: create
    This flag is only useful AFTER a control has already been
created (using the -addControl flag).  The first argument is
the node name and the second is the attribute whose control name
you wish to query.

---
suppress(s): string
    properties: create
    Prevent a control for the attribute specified by the
string argument from appearing in the editor created from the
template.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/editorTemplate.html 
    """


def effector(flaghide: boolean, flagname: string) -> string:
    """Synopsis:
---
---
 effector(
[object]
    , [hide=boolean], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

effector is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Will cause effector1 not to be displayed if attached to a handle.
This is the default.
---

cmds.effector( 'effector1', e=True, hi=False )

Will cause effector1 to be displayed if attached to a handle.
---

cmds.effector( 'effector1', e=True, hi=True )

---
Return:
---


    string: Command result

Flags:
---


---
hide(hi): boolean
    properties: create, query, edit
    Specifies whether to hide drawing of effector
if attached to a handle.

---
name(n): string
    properties: create, query, edit
    Specifies the name of the effector.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/effector.html 
    """


def emit(flagattribute: string, flagfloatValue: float, flagobject: string, flagposition: tuple[float, float, float], flagvectorValue: tuple[float, float, float]) -> list[int]:
    """Synopsis:
---
---
 emit([attribute=string], [floatValue=float], [object=string], [position=[float, float, float]], [vectorValue=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

emit is undoable, NOT queryable, and NOT editable.emit
The particles created do not become a part of the initial state
for the particle object, and will disappear when the scene is rewound unless
they are saved into the initial state by the user explicitly.  In addition,
a particle object will accept particles from an emit action ONLY at frames
greater than or equal to its start frame.  For example, if you want to use the
emit action to create particles at frame -5, you must set startFrame for that
particle shape to -5 or less.
Unlike many commands or actions, the emit action uses the order of its flags
as important information as to how it works.  The -object and -position
flags can appear anywhere in the argument list.  The -attribute and the
value flags are interpreted based on their order.  Any value flags after an
-attribute flag and before the next -attribute flag will set the values for
the attribute specified by the closest -attribute flag before them in the
argument list.  See the Examples section below for more detail on
how these flags work.
Currently, no creation expression is executed for the new particles
unless they are created from within a particle expression defined with
the dynExpression command or the Expression Editor.  If you
want any particular values put into the particles at the time they are
created, then those values should be set using the -attribute,
-vectorValue, and -floatValue flags.




Example:
---
import maya.cmds as cmds

cmds.particle()
cmds.emit( object='particle1', position=(1, 1, 1) )

This will create one particle at position <<1,1,1>> in the
already-existing particle object <i>particle1</i>.
---


cmds.particle()
cmds.emit( object='particle1', position=((1, 1, 1), (2, 2, 2)), attribute=('velocity', 'rgbPP'), vectorValue=((1, 2, 3), (2, 3, 4), (.5, 1, 0)), floatValue=.1 )

This will create two particles at positions <<1,1,1>> and <<2,2,2>> in
the already-existing particle object <i>particle1</i>.  Then the velocity
attribute of those particles is set to <<1,2,3>> and <<2,3,4>>,
respectively.  Also, the rgbPP values are set to <<.5,1,0>> and
<<.1,.1,.1>>, respectively.  Notice that the rgbPP value for the
second particle was set with the -floatValue flag, even though rgbPP
is a vector attribute.  The single value was converted into a vector.

cmds.particle()
cmds.emit( object='particle1', position=((1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)), attribute=('velocity', 'mass', 'velocity'), vectorValue=((1, 2, 3), (2, 3, 4), (.1, .2, .3), (3, 4, 5)), floatValue=.5)

This will create five particles in <i>particle1</i>.  The values
for their attributes are:
---

Attribute  Particle1   Particle2   Particle3   Particle4   Particle5
----------+-----------+-----------+-----------+-----------+---------
position   <<<<1,1,1>>>>   <<<<2,2,2>>>>   <<<<3,3,3>>>>   <<<<4,4,4>>>>   <<<<5,5,5>>>>
velocity   <<<<1,2,3>>>>   <<<<2,3,4>>>>   <<<<3,4,5>>>>   <b><<<<3,4,5>>>>   <<<<3,4,5>>>></b>
mass     .5          .3742       <b>.3742       .3742       .3742</b>
---

Notice that the second value for mass was seet with the -vectorValue
flag, even though mass is a float attribute.  The vector was
converted into a float by taking its length.  Also, notice the <b>bold</b>
values in the table.  The values for those attribute values were not
explicitly set in the command.  If there are fewer values given for
an attribute than there are position flags, the remaining unset
values are set to the last value set for that attribute.  This
allows the user to set many of the values to be the same without
having to use multiple value flags.  One last note.  Notice that the
attribute flag was passed twice for the attribute velocity.  The value
flags for repeated attributes pick up where the previous ones left
off.

x = rand(1)
y = rand(1)
z = rand(1)
p = sphrand(5)
cmds.emit( object='particle1', pos=((x, y, z), ('($p.x)', '($p.y)', '($p.z)')) )

This is a piece of Python code that could be put in a script or
even in an expression.  It adds a random number of particles
to the already-existing particle object <i>particle1</i>.  Since
the number of particles as well as the positions and velocities
of the particles are random, it would be impossible to just have
the emit action itself in the expression or script.  It must be
built as a string and then sent to the command processor with the
<b>eval</b> or <b>evalEcho</b> commands.  Notice that when appending
the vector variables to the string, it is not necessary to append
each component of the vectors separately.  When they are converted
from a vector to a string, the three components get separated with
a space automatically, thus formatting them in the desired way.
An example of a possible result from this "script" could be:

cmds.emit( object='particle1', pos=((1.899864198, -6.721569708, 0.585203937), (8.103957656, -4.042442985, 2.047724209), (-1.392914569, -0.109724376, 8.62265813), (1.960103537, -3.203145195, -7.6892516), (2.564072614, -6.049536895, 1.334818295), (-5.603376821, 4.33595058, 6.952385447), (-2.478591746, 6.286855715, 6.851659059), (2.424670276, -4.083412217, 6.320538621), (6.440800453, 3.405519296, 5.462135819), (2.445192551, 1.397203422, 3.443755853)), at='velocity', vv=((-2.348796409, 4.022130218, 0.5316172944), (4.149667117, -1.023146404, 1.97965556), (-0.08429132578, -0.5518495233, 1.591812495), (2.597930963, 1.033536331, -1.398351383), (-3.102859272, 3.423569856, 0.7895603241), (-2.519331228, -2.5684916, -1.530779154), (-2.645169119, -0.3186551381, 0.9164776099), (-0.6183816487, -1.060784068, -0.8748223942), (-0.2460372256, 3.567980747, -2.007567372), (1.735044809, -3.660099445, -1.765401859)) )

The spacing in the string is just for formatting reasons and does
not affect how the action executes or compiles.

---
Return:
---


    list[int]: Integer array containing the list of the particleId attribute values
for the created particles in the same order that thepositionflags
were passed.

Flags:
---


---
attribute(at): string
    properties: create, multiuse
    Specifies the attribute on the particle object that any
value flags following it and before the next -attribute flag
will be associated with.  The same attribute can be specified
later in the command to pick up where the first one left off.
The attributes used must be per-particle attributes.  This
will accept both long and short names for the attributes.
Note the per-particle attribute must already exist on the
particle object prior to being specified via this command flag.

---
floatValue(fv): float
    properties: create, multiuse
    Sets the float value to be used for the "current" attribute of
the "current" particle.  By current attribute, it is meant the
attribute specified by the most recent -attribute flag.  By
current particle, it is meant the particle in the list of -position
flags that corresponds to the number of values that  have
been set for the "current" attribute.  If the current attribute
is a vector-per-particle attribute, then the float value
specified will be used for all three components of the vector.

---
object(o): string
    properties: create
    This flag takes the name of a particleShape or the transform
directly above it in the DAG as its parent.  It specifies
which object to add the particles to.  This flag must
be passed, as the selection list is ignored for this action.

---
position(pos): [float, float, float]
    properties: create, multiuse
    Specifies the positions in the particle object's space
(usually world space) where the particles are to be created.
One particle is created for each occurence of this flag.

---
vectorValue(vv): [float, float, float]
    properties: create, multiuse
    Sets the vector value to be used for the "current" attribute of
the "current" particle.  By current attribute, it is meant the
attribute specified by the most recent -attribute flag.  By
current particle, it is meant the particle in the list of -position
flags that corresponds to the number of values that have
been set for the "current" attribute.  If the current attribute
is a float-per-particle attribute, then the length of the
vector described by this flag will be used.  The length is
described as SQR( xVal2 + yVal2 + zVal2 ).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/emit.html 
    """


def emitter(flagalongAxis: float, flagaroundAxis: float, flagawayFromAxis: float, flagawayFromCenter: float, flagcycleEmission: string, flagcycleInterval: int, flagdirectionX: linear, flagdirectionY: linear, flagdirectionZ: linear, flagdirectionalSpeed: float, flagmaxDistance: linear, flagminDistance: linear, flagname: string, flagneedParentUV: boolean, flagnormalSpeed: float, flagposition: tuple[linear, linear, linear], flagrandomDirection: float, flagrate: float, flagscaleRateByObjectSize: boolean, flagscaleSpeedBySize: boolean, flagspeed: float, flagspeedRandom: float, flagspread: float, flagtangentSpeed: float, flagtorusSectionRadius: linear, flagtype: string, flagvolumeOffset: tuple[linear, linear, linear], flagvolumeShape: string, flagvolumeSweep: angle) -> string:
    """Synopsis:
---
---
 emitter(
[objects]
    , [alongAxis=float], [aroundAxis=float], [awayFromAxis=float], [awayFromCenter=float], [cycleEmission=string], [cycleInterval=int], [directionX=linear], [directionY=linear], [directionZ=linear], [directionalSpeed=float], [maxDistance=linear], [minDistance=linear], [name=string], [needParentUV=boolean], [normalSpeed=float], [position=[linear, linear, linear]], [randomDirection=float], [rate=float], [scaleRateByObjectSize=boolean], [scaleSpeedBySize=boolean], [speed=float], [speedRandom=float], [spread=float], [tangentSpeed=float], [torusSectionRadius=linear], [type=string], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

emitter is undoable, queryable, and editable.
If an emitter was created, the command returns the name of the object
owning the emitter, and the name of emitter shape. If an emitter was
queried, the command returns the results of the query.

Keyframeable attributes of the emitter node: rate, directionX,
directionY, directionZ, minDistance, maxDistance, spread.




Example:
---
import maya.cmds as cmds

cmds.particle( p=((-1, 5, 2), (2, 2, 2), (3, 3, 3)), n='particles' )
cmds.emitter( 'particles', r=300, mnd=1.5, mxd=2.5, n='emitter' )
cmds.particle( n='emitted' )
cmds.connectDynamic( 'emitted', em='emitter' )

Creates a particle emitter.

cmds.emitter( dx=1, dy=0, dz=0, sp=0.33, pos=(1, 1, 1), n='myEmitter' )
cmds.particle( n='emittedParticles' )
cmds.connectDynamic( 'emittedParticles', em='myEmitter' )

Creates a point emitter.

---
Return:
---


    string: Command result

Flags:
---


---
alongAxis(alx): float
    properties: query, edit
    Initial velocity multiplier in the direction along
the central axis of the volume.  See the diagrams in
the documentation.  Applies only to volume emitters.

---
aroundAxis(arx): float
    properties: query, edit
    Initial velocity multiplier in the direction around
the central axis of the volume.  See the diagrams
in the documentation.  Applies only to volume emitters.

---
awayFromAxis(afx): float
    properties: query, edit
    Initial velocity multiplier in the direction away
from the central axis of the volume.  See the diagrams
in the documentation.  Used only with the cylinder, cone,
and torus volume emitters.

---
awayFromCenter(afc): float
    properties: query, edit
    Initial velocity multiplier in the direction away from
the center point of a cube or sphere volume emitter. Used only with
the cube and sphere volume emitters.

---
cycleEmission(cye): string
    properties: query, edit
    Possible values are "none" and "frame."
Cycling emission restarts the random number stream after
a specified interval.  This can either be a number of frames
or a number of emitted particles.  In each case the number
is specified by the cycleInterval attribute. Setting cycleEmission to
"frame" and cycleInterval to 1 will then re-start the random stream every
frame. Setting cycleInterval to values greater than 1 can be used
to generate cycles for games work.

---
cycleInterval(cyi): int
    properties: query, edit
    Specifies the number of frames or particles between restarts of
the random number stream.  See cycleEmission.  Has no effect if
cycleEmission is set to None.

---
directionX(dx): linear
    properties: query, edit
    x-component of emission direction.
Used for directional emitters, and for volume emitters with
directionalSpeed.

---
directionY(dy): linear
    properties: query, edit
    y-component of emission direction.
Used for directional emitters, and for volume emitters with
directionalSpeed.

---
directionZ(dz): linear
    properties: query, edit
    z-component of emission direction.
Used for directional emitters, and for volume emitters with
directionalSpeed.

---
directionalSpeed(drs): float
    properties: query, edit
    For volume emitters only, adds a component of speed in the
direction specified by the directionX, Y, and Z attributes.
Applies only to volume emitters. Does not apply to other types
of emitters.

---
maxDistance(mxd): linear
    properties: query, edit
    Maximum distance at which emission ends.

---
minDistance(mnd): linear
    properties: query, edit
    Minimum distance at which emission starts.

---
name(n): string
    properties: create, query, edit
    Object name

---
needParentUV(nuv): boolean
    properties: query, edit
    If aNeedParentUV is true, compute parentUV value from
each triangle or each line segment, then send out to the
target particle object. You also need to add parentU and
parentV attributes to the particle object to store these values.

---
normalSpeed(nsp): float
    properties: query, edit
    Normal speed multiple for point emission. For each emitted
particle, multiplies the component of the velocity normal
to the surface or curve by this amount. Surface and curve
emitters only.

---
position(pos): [linear, linear, linear]
    properties: create, query, edit, multiuse
    world-space position

---
randomDirection(rnd): float
    properties: query, edit
    Magnitude of a random component of the speed
from volume emission.

---
rate(r): float
    properties: query, edit
    Rate at which particles emitted (can be non-integer).
For point emission this is rate per point per unit time.
For surface emission it is rate per square unit of area per unit time.

---
scaleRateByObjectSize(sro): boolean
    properties: query, edit
    Applies to curve and surface emitters, only.
If true, number of particles is determined by object size
(area or length) times rate value.  If false, object size
is ignored and the rate value is used without modification.
The former is the way Maya behaved prior to version 3.0.

---
scaleSpeedBySize(ssz): boolean
    properties: query, edit
    Indicates whether the scale of a volume emitter
affects its velocity.

---
speed(spd): float
    properties: query, edit
    Speed multiple.  Multiplies the velocity of the
emitted particles by this amount. Does not apply to volume
emitters.  For that emitter type, use directionalSpeed.

---
speedRandom(srn): float
    properties: query, edit
    Identifies a range of random variation for the speed of
each generated particle.  If set to a non-zero value, speed
becomes the mean value of the generated particles, whose speeds
vary by a random amount up to plus or minus speedRandom/2.
For example, speed 5 and speedRandom 2 will make the speeds
vary between 4 and 6.

---
spread(sp): float
    properties: query, edit
    Random spread (0-1), as a fraction of 90 degrees,
along specified direction.   Directional emitters only.

---
tangentSpeed(tsp): float
    properties: query, edit
    Tangent speed multiple for point emission.
For each emitted particle, multiplies the component of the velocity
tangent to the surface  or curve by this amount.
Surface and curve emitters only.

---
torusSectionRadius(tsr): linear
    properties: query, edit
    Section radius for a torus volume.  Applies only to torus.
Similar to the section radius in the torus modelling primitive.

---
type(typ): string
    properties: query, edit
    Type of emitter. The choices are omni | dir | direction | surf |
surface | curve | curv. The default is omni.
The full definition of these types are: omnidirectional point emitter,
directional point emitter, surface emitter, or curve emitter.

---
volumeOffset(vof): [linear, linear, linear]
    properties: query, edit
    Volume offset of the emitter.  Volume offset translates
the emission volume by the specified amount from the actual
emitter location.  This is in the emitter's local space.

---
volumeShape(vsh): string
    properties: query, edit
    Volume shape of the emitter.  Sets/edits/queries the
field's volume shape attribute.  If set to any value other
than "none", determines a 3-D volume within which
particles are generated.
Values are: "cube," "sphere," "cylinder," "cone," "torus."

---
volumeSweep(vsw): angle
    properties: query, edit
    Volume sweep of the emitter.  Applies only to sphere, cone,
cylinder, and torus.  Similar effect to the sweep attribute
in modelling.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/emitter.html 
    """


def enableDevice(flagapply: boolean, flagdevice: string, flagenable: boolean, flagmonitor: boolean, flagrecord: boolean) -> None:
    """Synopsis:
---
---
 enableDevice([apply=boolean], [device=string], [enable=boolean], [monitor=boolean], [record=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

enableDevice is undoable, queryable, and NOT editable.

-monitor
affects all assignInputDevice and attachDeviceAttr actions for
the named device
-record
controls if the device is recorded (by default) by a recordDevice
action
-apply channelName [channelName ... ]
controls if data from the  device channel is applied (by default)
by applyTake to the param curves attached to the named channel.

Disabling a channel for applyTake cause applyTake to ignore
the enable state of all "child" channels -- treating them as disabled.




Example:
---
import maya.cmds as cmds

Enables all assignInputDevice and attachDeviceAttr actions for the
device named "clock"
cmds.enableDevice( enable=True, d='clock' )

Stops applyTake (with no arguments) from updating param curves
attached to the minutes  and hours channels of device named "clock"
cmds.enableDevice( 'minutes', 'hours', enable=False, d='clock', apply=True )

---


Flags:
---


---
apply(a): boolean
    properties: create, query
    enable/disable "applyTake" for the specified channel(s)

---
device(d): string
    properties: create, query
    specifies the device to change

---
enable(en): boolean
    properties: create, query
    enable (or disable) monitor/record/apply

---
monitor(m): boolean
    properties: create, query
    enables/disables visible update for the device (default)

---
record(rec): boolean
    properties: create, query
    enable/disable "recordDevice" device recording

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/enableDevice.html 
    """


def encodeString() -> string:
    """Synopsis:
---
---
 encodeString(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

encodeString is undoable, NOT queryable, and NOT editable. double quotes newlines tabs 



Example:
---
import maya.cmds as cmds

Set the string s to: print('Hello\n');
quote = '\"'
backslash = '\\'
s = 'print(' + quote + 'Hello' + backslash + 'n' + quote + ')'
print 's=' + s
s=print("Hello\n")

es = cmds.encodeString(s)
print 'es=' + es
es=print(\"Hello\\n\")

---
Return:
---


    string: Command result

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/encodeString.html 
    """


def error(flagnoContext: boolean, flagshowLineNumber: boolean) -> None:
    """Synopsis:
---
---
 error([noContext=boolean], [showLineNumber=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

error is NOT undoable, NOT queryable, and NOT editable.
The error command is provided so that the user can issue
error messages from his/her scripts and
control execution in the event of runtime errors.


The string argument is displayed in the command window
(or stdout if running in batch mode) after
being prefixed with an error message heading and
surrounded by //.


The error command also causes execution to terminate with an error.
Using error is like raising an exception because the error will
propagate up through the call chain. You can use catch to
handle the error from the caller side. If you don't want
execution to end, then you probably want to use the warning
command instead.




Example:
---
import maya.cmds as cmds


import maya.cmds as cmds
def lightError():
    l = cmds.ls( lights=True )
    if len(l) == 0:
        cmds.error( "No Lights" )
lightError()

The above will produce the following output and raise a RuntimeError
exception from the script containing it:
---

  Error: No Lights ---

---

If the option to display line numbers or the stack trace is turned on
the following output will be produced and the same exception raised:
---

  Error: line 13 of 'lightError' in '<maya console'>: No Lights ---

---


---


Flags:
---


---
noContext(n): boolean
    properties: create
    Do not include the context information with the error message.

---
showLineNumber(sl): boolean
    properties: create
    Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the
script editor that enables line number display instead.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/error.html 
    """


def eval() -> Any:
    """Synopsis:
---
---
 eval(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

eval is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.mel as mel

mel.eval('match "a+b+" "abbcc"')
Result: abb ---


Eval can be used to access global MEL variables. For example, the following
assigns the current value in $gMainWindow to a Python variable.
myPythonVar=mel.eval('$tempMelVar=$gMainWindow')

Print the value retrieved.
print myPythonVar
Result: MayaWindow

---
Return:
---


    Any: depending on input.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/eval.html 
    """


def evalDeferred(flagevaluateNext: boolean, flaglist: boolean, flaglowPriority: boolean, flaglowestPriority: boolean) -> list[string]:
    """Synopsis:
---
---
 evalDeferred(
[script]
    , [evaluateNext=boolean], [list=boolean], [lowPriority=boolean], [lowestPriority=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

evalDeferred is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
button = cmds.button(label='Delete Me')
cmds.button(button, edit=True, command=('cmds.evalDeferred("cmds.deleteUI(button)")'))
cmds.showWindow()

---
Return:
---


    list[string]: Command result

Flags:
---


---
evaluateNext(en): boolean
    properties: create
    Specified that the command to be executed should be ran with the
highest priority, ideally queued up next.

---
list(ls): boolean
    properties: create
    Return a list of the command strings that are currently pending on
the idle queue. By default, it will return the list of commands for all
priorities. The -lowestPriority and -lowPriority can be used to
restrict the list of commands to a given priority level.

---
lowPriority(low): boolean
    properties: create
    Specified that the command to be executed should be deferred with the
low priority. That is, it will be executed whenever Maya is idle.

---
lowestPriority(lp): boolean
    properties: create
    Specified that the command to be executed should be deferred with the
lowest priority. That is, it will be executed when no other idle
events are scheduled.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/evalDeferred.html 
    """


def evaluationManager(flagcycleCluster: string, flagdisableInfo: string, flagdownstreamFrom: string, flagempty: boolean, flagenabled: boolean, flagfallbackTriggered: boolean, flagidleAction: int, flagidleBuild: boolean, flaginvalidate: boolean, flagmanipulation: boolean, flagmanipulationPrevalidation: boolean, flagmanipulationReady: boolean, flagmode: string, flagnodeTypeGloballySerialize: boolean, flagnodeTypeParallel: boolean, flagnodeTypeSerialize: boolean, flagnodeTypeUntrusted: boolean, flagreduceGraphRebuild: boolean, flagsafeMode: boolean, flagupstreamFrom: string) -> Int | boolean | boolean[] | list[string] | string:
    """Synopsis:
---
---
 evaluationManager([cycleCluster=string], [disableInfo=string], [downstreamFrom=string], [empty=boolean], [enabled=boolean], [fallbackTriggered=boolean], [idleAction=int], [idleBuild=boolean], [invalidate=boolean], [manipulation=boolean], [manipulationPrevalidation=boolean], [manipulationReady=boolean], [mode=string], [nodeTypeGloballySerialize=boolean], [nodeTypeParallel=boolean], [nodeTypeSerialize=boolean], [nodeTypeUntrusted=boolean], [reduceGraphRebuild=boolean], [safeMode=boolean], [upstreamFrom=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

evaluationManager is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Enable evaluation manager in serial mode
cmds.evaluationManager( mode="serial" )
Result: True ---


Confirm that the evaluation manager is currently enabled
cmds.evaluationManager( query=True, enabled=True )
Result: True ---


Check if the evaluation manager has at least one animated node in it
cmds.evaluationManager( query=True, empty=True )
Result: True ---


Does nothing since it was already in serial mode
cmds.evaluationManager( mode="serial" )
Result: True ---


Return the current evaluation manager mode and graph state
cmds.evaluationManager( query=True, mode=True )
Result: [u'serial'] ---


Return all legal evaluation modes
cmds.evaluationManager( query=True )
Result: [u'off', u'serial'] ---


Disable evaluation manager
cmds.evaluationManager( mode="off" )
Result: True ---


Activate parallel scheduling override on transform nodes
cmds.evaluationManager( "transform", nodeTypeParallel=True, on=True )
Result: True ---


Query for node types with the parallel scheduling override
cmds.evaluationManager( query=True, nodeTypeParallel=True )
Result: ["transform"] ---


Query the parallel scheduling override of a particular node type
cmds.evaluationManager( "transform", query=True, nodeTypeParallel=True )
Result: True ---


Activate locally serial scheduling override on transform nodes
cmds.evaluationManager( "transform", nodeTypeSerialize=True, on=True )
Result: True ---


Query for node types with the locally serial scheduling override
cmds.evaluationManager( query=True, nodeTypeSerialize=True )
Result: ["transform"] ---


Query the locally serial scheduling override of a particular node type
cmds.evaluationManager( "transform", query=True, nodeTypeSerialize=True )
Result: True ---


Activate globally serial scheduling override on transform nodes
cmds.evaluationManager( "transform", nodeTypeGloballySerialize=True, on=True )
Result: True ---


Query for node types with the globally serial scheduling override
cmds.evaluationManager( query=True, nodeTypeGloballySerialize=True )
Result: ["transform"] ---


Query the globally serial scheduling override of a particular node type
cmds.evaluationManager( "transform", query=True, nodeTypeGloballySerialize=True )
Result: True ---


Activate untrusted scheduling override on transform nodes
cmds.evaluationManager( "transform", nodeTypeUntrusted=True, on=True )
Result: True ---


Query for node types with the untrusted scheduling override
cmds.evaluationManager( query=True, nodeTypeUntrusted=True )
Result: ["transform"] ---


Query the untrusted scheduling override of a particular node type
cmds.evaluationManager( "transform", query=True, nodeTypeUntrusted=True )
Result: True ---


Force rebuild of evaluation graph for normal context
cmds.evaluationManager( invalidate=True )
Result: True ---


Test if evaluation graph is valid for normal context
cmds.evaluationManager( query=True, invalidate=True )
Result: False ---


Activate safe mode for parallel executor
cmds.evaluationManager( safeMode=True )
Result: True ---


Query safe mode for parallel executor
cmds.evaluationManager( query=True, safeMode=True )
Result: True ---


Enable manipulation with evaluation manager
cmds.evaluationManager( manipulation=True )
Result: True ---


Query manipulation with evaluation manager
cmds.evaluationManager( query=True, manipulation=True )
Result: True ---


Enable manipulation prevalidation with evaluation manager
cmds.evaluationManager( manipulationPrevalidation=True )
Result: True ---


Query manipulation prevalidation with evaluation manager
cmds.evaluationManager( query=True, manipulationPrevalidation=True )
Result: True ---


Query if evaluation manager manipulation is ready/allowed
cmds.evaluationManager( query=True, manipulationReady=True )
Result: True ---


Show downstream nodes
cmds.evaluationManager( downstreamFrom='myNode' )
Result: ['myDownstreamNode'] ---


Show all downstream nodes
cmds.evaluationManager( query=True, downstreamFrom='myRoot' )
Result: ['0', 'myRoot', '1', 'myNode', '2', 'myDownstreamNode' ] ---


Show upstream nodes
cmds.evaluationManager( upstreamFrom='myDownstreamNode' )
Result: ['myNode'] ---


Show cycle cluster
cmds.evaluationManager( cycleCluster='myNodeInCycle' )
Result: ['myNode', 'myNodeInCycle', 'myNode'] ---


Activate idle rebuild
cmds.evaluationManager( idleAction=1 )
Result: True ---


Query idleAction
cmds.evaluationManager( query=True, idleAction=True )
Result: 1 ---


Show the reasons the evaluation manager was disabled
cmds.evaluationManager( query=True, disableInfo=True )
Result: ---


Query for fallback evaluation state
cmds.evaluationManager( query=True, fallbackTriggered=True )
Result: False ---


---
Return:
---


    list[string]: The names of all evaluation manager modes (querying without flags)
    list[string]: The names of all nodes involved in a cycle cluster with the selected one.
    boolean: The success of activating of deactivating manipulation (with the 'manipulation' flag)
    boolean: The manipulation active or inactive state (querying the 'manipulation' flag)
    boolean: The manipulation prevalidation active or inactive state (querying the 'manipulationPrevalidation' flag)
    boolean: The manipulation allowed or disallowed state (querying the 'manipulationReady' flag)
    boolean: The success of setting the evaluation manager mode (with the 'mode' flag)
    boolean: The success of setting the evaluation manager idle action (with the 'idleAction' flag)
    boolean: False if there are any nodes in the evaluation graph (with the 'empty' flag)
    Int: The Evaluation Manager idle action (querying with the 'idleAction' flag)
    boolean: Is the evaluation graph currently valid? (querying with the 'invalidate' flag)
    boolean: The success of setting the node type parallel scheduling mode (with the 'nodeTypeParallel' flag)
    boolean[]: The parallel scheduling states of specified node types (querying the 'nodeTypeParallel' flag with object(s))
    list[string]: The names of all node types in parallel scheduling mode (querying the 'nodeTypeParallel' flag alone)
    boolean: The success of setting the node type serialized mode (with the 'nodeTypeSerialize' flag)
    boolean[]: The serialized states of specified node types (querying the 'nodeTypeSerialize' flag with object(s))
    list[string]: The names of all node types in serial scheduling mode (querying the 'nodeTypeSerialize' flag alone)
    boolean: The success of setting the node type globally serialized mode (with the 'nodeTypeGloballySerialize' flag)
    boolean[]: The globally serialized states of specified node types (querying the 'nodeTypeGloballySerialize' flag with object(s))
    list[string]: The names of all node types in globally serialized scheduling mode (querying the 'nodeTypeGloballySerialize' flag alone)
    boolean: The success of setting the node type untrusted mode (with the 'nodeTypeUntrusted' flag)
    boolean[]: The untrusted of specified node types (querying the 'nodeTypeUntrusted' flag with object(s))
    list[string]: The names of all node types in untrusted scheduling mode (querying the 'nodeTypeUntrusted' flag alone)
    string: The evaluation manager mode (querying with the 'mode' flag)
    list[string]: The names of all nodes immediately downstream/upstream of the named one(s) (with the 'upstreamFrom' or 'downstreamFrom' flags)
    list[string]: The list of reasons the evaluation manager has been disabled (querying the 'disableInfo' flag)
    boolean: The state of fallback serial evaluation (querying the 'fallbackTriggered' flag)
    boolean: The state of reduceGraphRebuild Support (querying the 'reduceGraphRebuild ' flag)

Flags:
---


---
cycleCluster(ccl): string
    properties: create, query
    Returns a list of nodes that are stored together with the given one in
a cycle cluster. The list will be empty when the evaluation mode is not
active or the node is not in a cycle.

---
disableInfo(di): string
    properties: query
    Returns a list of strings that contain the reasons that the evaluation manager has
been disabled (as distinct from it being deliberately turned off, e.g. because an
unsupported node type or attribute value was encountered).
If the list is empty then the evaluation manager is operating normally.

---
empty(mt): boolean
    properties: query
    Valid in query mode only. Checks to see if the evaluation graph has any nodes in it.
This is independent of the current mode.

---
enabled(e): boolean
    properties: query
    Valid in query mode only. Checks to see if the evaluation manager is currently enabled.
This is independent of the current mode.

---
fallbackTriggered(ft): boolean
    properties: query
    Valid in query mode only. Checks to see if fallback serial evaluation has been triggered.
Will be true if errors during parallel execution have forced a fallback to serial mode.
Will reset to false if the mode is changed again after the fallback was triggered.

---
idleAction(ia): int
    properties: create, query
    This flag sets the actions EM will perform on idle. It accepts the following values:

0 - No action
1 - Graph Rebuild
2 - EM Manipulation Preparation
3 - Graph Rebuild and EM Manipulation Preparation


Where:

Graph Rebuild will rebuild the evaluation graph on an idle event as soon
as it is able to do so.
EM ManipulationPreparation will get the evaluation manager to perform all
the steps necessary for EM manipulation to be available after the next idle event.


Note: These idle actions only apply to the graph attached to the normal context.
All other graphs will be built according to their own rules.

The disadvantage of enabling idle actions is that for some workflows that are
changing the graph frequently, or very large graphs, the graph build and
manipulation preparation time may impact the workflow. If workflows are impacted
it is suggested to turn idle actions off by passing this flag a value of 0.

---
idleBuild(ib): boolean
    properties: create, query
    This flag is obsolete. Please use the -idleAction flag with a value of 1
in order to activate evaluation graph rebuild on idle.

---
invalidate(inv): boolean
    properties: create, query
    This flag invalidates the graph. Value is used to control auto rebuilding on idle (false) or forced (true).
This command should be used as a last resort.
In query mode it checks to see if the graph is valid.

---
manipulation(man): boolean
    properties: create, query
    This flag is used to activate evaluation manager manipulation support.

---
manipulationPrevalidation(mp): boolean
    properties: create, query
    This flag is used to activate evaluation manager manipulation prevalidation.
Prevalidation checks for known patterns in manipulation.  In case of a
successful prevalidation, there is no need to use dirty propagation in the
first frame of manipulation to validate that EM manipulation can safely be used,
and fast manipulation can start right away.

---
manipulationReady(mr): boolean
    properties: query
    Valid in query mode only. Checks to see if the evaluation manager manipulation is currently ready/allowed.
This is independent of the current mode.

---
mode(m): string
    properties: create, query
    Changes the current evaluation mode in the evaluation manager. Supported values are
"off", "serial" and "parallel".

---
downstreamFrom(dst): string
    properties: create, query
    Find the DG nodes that are immediately downstream of the named one in
the evaluation graph. Note that the connectivity is via evaluation mode
connections, not DG connections.
In query mode the graph is walked and any nodes downstream of the named
one are returned. The return type is alternating pairs of values that
represent the graph level and the node name, e.g. if you walk downstream
from A in the graph A -> B -> C then the return will be the array of
strings ("0","A","1","B","2","C"). Scripts can deconstruct this
information into something more visually recognizable. Note that cycles
are likely to be present so any such scripts would have to handle them.
                        In query mode, this flag needs a value.

---
nodeTypeGloballySerialize(ntg): boolean
    properties: create, query
    This flag is used only when the evaluation manager is in "parallel" mode
but can be set at anytime. It activates or deactivates the override to force
global serial scheduling for the class name argument(s) in the evaluation manager.
Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".
When queried without specified nodes, it returns the list of nodes with the
global serial scheduling override active.
Scheduling overrides take precedence over all of the node and node type
scheduling rules. Use with caution; certain nodes may not react well to
alternative scheduling types.

---
nodeTypeParallel(ntp): boolean
    properties: create, query
    This flag is used only when the evaluation manager is in "parallel" mode
but can be set at anytime. It activates or deactivates the override to force
parallel scheduling for the class name argument(s) in the evaluation manager.
Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".
When queried without specified nodes, it returns the list of nodes with the
parallel scheduling override active.
Scheduling overrides take precedence over all of the node and node type
scheduling rules. Use with caution; certain nodes may not react well to
alternative scheduling types.

---
nodeTypeSerialize(nts): boolean
    properties: create, query
    This flag is used only when the evaluation manager is in "parallel" mode
but can be set at anytime. It activates or deactivates the override to force
local serial scheduling for the class name argument(s) in the evaluation manager.
Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".
When queried without specified nodes, it returns the list of nodes with the
local serial scheduling override active.
Scheduling overrides take precedence over all of the node and node type
scheduling rules. Use with caution; certain nodes may not react well to
alternative scheduling types.

---
nodeTypeUntrusted(ntu): boolean
    properties: create, query
    This flag is used only when the evaluation manager is in "parallel" mode
but can be set at anytime. It activates or deactivates the override to force
untrusted scheduling for the class name argument(s) in the evaluation manager.
Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".
When queried without specified nodes, it returns the list of nodes with the
untrusted scheduling override active.
Scheduling overrides take precedence over all of the node and node type
scheduling rules. Use with caution; certain nodes may not react well to
alternative scheduling types.
Untrusted scheduling will allow nodes to be evaluated in a critical section,
separately from any other node evaluation. It should be used only as a last resort
since the lost parallelism caused by untrusted nodes can greatly reduce performance.

---
upstreamFrom(ust): string
    properties: create, query
    Find the DG nodes that are immediately upstream of the named one in
the evaluation graph. Note that the connectivity is via evaluation mode
connections, not DG connections.
In query mode the graph is walked and any nodes upstream of the named
one are returned. The return type is alternating pairs of values that
represent the graph level and the node name, e.g. if you walk upstream
from C in the graph A -> B -> C then the return will be the array of
strings ("0","C","1","B","2","A"). Scripts can deconstruct this
information into something more visually recognizable. Note that cycles
are likely to be present so any such scripts would have to handle them.
                        In query mode, this flag needs a value.

---
reduceGraphRebuild(rgr): boolean
    properties: create, query
    This flag is used to activate evaluation manager mode to minimize rebuild when animated node are connected to EM prepopulated plug.

---
safeMode(sfm): boolean
    properties: create, query
    This flag activates/deactivates parallel evaluation safe mode. When
enabled, parallel execution will fall back to serial when evaluation
graph is missing dependencies. Detection is happening on scheduling
of parallel evaluation, which means potential fallback will happen at
the next evaluation.
WARNING: This mode should be disabled with extreme caution. It will
prevent parallel mode from falling back to serial mode when an invalid
evaluation is detected. Sometimes the evaluation will still work
correctly in those situations and use of this flag will keep the peak
parallel performance running. However since the safe mode is used to
catch invalid evaluation disabling it may also cause problems with
evaluation, anything from invalid values, missing evaluation, or even
crashes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/evaluationManager.html 
    """


def evaluator(flagclusters: boolean, flagconfiguration: string, flagenable: boolean, flaginfo: boolean, flagname: string, flagnodeType: string, flagnodeTypeChildren: boolean, flagpriority: int, flagvalueName: string) -> boolean | int | list[string] | string:
    """Synopsis:
---
---
 evaluator([clusters=boolean], [configuration=string], [enable=boolean], [info=boolean], [name=string], [nodeType=string], [nodeTypeChildren=boolean], [priority=int], [valueName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

evaluator is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

Load a custom evaluator plug-in (not a real plug-in, just an example)
cmds.loadPlugin( 'MY_CUSTOM_EVALUATOR' );
Result: MY_CUSTOM_EVALUATOR ---


List the available evaluators
cmds.evaluator( query=True );
Result: [u'MY_CUSTOM_EVALUATOR'] ---


Is 'MY_CUSTOM_EVALUATOR' disabled?
cmds.evaluator( query=True, name='MY_CUSTOM_EVALUATOR' )
Result: False ---


Check which evaluators are disabled
cmds.evaluator( enable=False, query=True )
Result: [u'MY_CUSTOM_EVALUATOR'] ---


Turn on 'MY_CUSTOM_EVALUATOR'
cmds.evaluator( enable=True, name='MY_CUSTOM_EVALUATOR' )
Result: False ---


Check to see which evaluators are enabled
cmds.evaluator( enable=True, query=True )
Result: [u'MY_CUSTOM_EVALUATOR'] ---


Make 'MY_CUSTOM_EVALUATOR' handle nodes of type 'transform'
cmds.evaluator( enable=True, name='MY_CUSTOM_EVALUATOR', nodeType='transform' )
Result: [u'transform'] ---


Make 'MY_CUSTOM_EVALUATOR' handle nodes of type 'transform' and all derived types
cmds.evaluator( enable=True, name='MY_CUSTOM_EVALUATOR', nodeType='transform', nodeTypeChildren=True )
Result: [u'transform', u'joint', <large list omitted>] ---


Get the list of clustered nodes handled by 'MY_CUSTOM_EVALUATOR' in the current scene.
cmds.evaluator( name='MY_CUSTOM_EVALUATOR', query=True, clusters=True )
Result: ['2', 'transform1', 'transform2', '3', 'joint3', 'joint4', 'joint5' ] ---


Send a configuration message to 'MY_CUSTOM_EVALUATOR'
cmds.evaluator( name='MY_CUSTOM_EVALUATOR', configuration='cluster=subgraph' )
Result: ---


Query information about 'MY_CUSTOM_EVALUATOR'
cmds.evaluator( query=True, name='MY_CUSTOM_EVALUATOR', info=True )
Result: ---


Query 'pruneRoots' priority
cmds.evaluator( query=True, name='pruneRoots', priority=True )
Result: 1000

Set "pruneRoots" priority to 2500
cmds.evaluator( name='pruneRoots', priority=2500 )
Result: True

---
Return:
---


    list[string]: the list of available evaluators (querying with no evaluator flag or invalid evaluator name)
    boolean: the previous active state of the named evaluator (with 'name' and 'enable' flags)
    boolean: the active state of the named evaluator (query with 'name' and 'enable' flags)
    list[string]: the list of evaluators in the requested active state (query 'enable' flag alone)
    list[string]: the list of nodes for which the evaluator was activated or deactivated (with 'nodeType' or 'nodeTypeChildren' flags)
    string: the queried value for the evaluator (with 'name' and 'valueName' flags)
    boolean: true if the configuration request was accepted by the evaluator (with 'name' flag and 'configuration' flag)
    list[string]: the list of configuration parameters accepted by the evaluator (query mode with 'name' flag and 'configuration' flag)
    list[string]: the list of clusters currently assigned to the evaluator with intervening sublist sizes (query mode with 'name' flag and 'clusters' flag)
    string: the help information supplied by the evaluator (query mode with 'name' flag and 'info' flag)
    int: the priority value of the evaluator (query mode with 'name' flag and 'priority' flag)

Flags:
---


---
clusters(cl): boolean
    properties: query
    This flag queries the list of clusters currently assigned to the named custom evaluator.
The return value will be an array of strings where the array consists of a
set of (number, string[]) groups. e.g. If an evaluator has 2 clusters with
2 and 3 nodes in them respectively the output would be something like:
(2, 'transform2', 'transform3', 3, 'joint1', 'joint2', 'joint3')

---
configuration(c): string
    properties: create, query, multiuse
    Sends configuration information to a custom evaluator. It's up to the evaluator
to understand what they mean.
Multiple configuration messages can be sent in a single command.
Query this flag for a given evaluator to find out what configuration
messages it accepts.

---
enable(en): boolean
    properties: create, query
    Enables or disables a specific graph evaluation runtime, depending on the
state of the flag.  In order to use this flag you must also specify the
name in the 'name' argument.
When the 'enable' flag is used in conjunction with the 'nodeType' flag then
it is used to selectively turn on or off the ability of the given evaluator
to handle nodes of the given type (i.e. it no longer toggles the evaluator
enabled state).
When the 'enable' flag is used in conjunction with the 'configuration' flag then
it is passed along with the configuration message interpreted by the custom
evaluator.

---
info(i): boolean
    properties: query
    Queries the evaluator information. Only valid in query mode since the
information is generated by the evaluator's internal state and cannot be
changed.
In order to use this flag, the 'name' argument must also be specified.

---
name(n): string
    properties: create, query
    Names a particular DG evaluation override evaluator. Evaluators are registered
automatically by name. Query this flag to get a list of available runtimes.
When a runtime is registered it is enabled by default. Use the 'enable'
flag to change its enabled state.
                        In query mode, this flag can accept a value.

---
nodeType(nt): string
    properties: create, query, multiuse
    Names a particular node type to be passed to the evaluator request.
Evaluators can either use or ignore the node type information as passed.
                        In query mode, this flag can accept a value.

---
nodeTypeChildren(ntc): boolean
    properties: create, query
    If enabled when using the 'nodeType' flag then handle all of the node types
derived from the given one as well. Default is to only handle the named
node type.

---
priority(p): int
    properties: create, query
    Query or set the evaluator priority. Custom evaluator with highest priority
order will get the chance to claim the nodes first.  Evaluators must have
unique priority values.
In order to use this flag you must also specify the name in the 'name' argument.

---
valueName(vn): string
    properties: query
    Queries a value from a given evaluator.  Evaluators can define a set of
values for which they answer.
                        In query mode, this flag can accept a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/evaluator.html 
    """


def event(flagcount: uint, flagdelete: boolean, flagdieAtCollision: boolean, flagemit: uint, flaglist: boolean, flagname: string, flagproc: script, flagrandom: boolean, flagrename: string, flagselect: boolean, flagsplit: uint, flagspread: float, flagtarget: string) -> string:
    """Synopsis:
---
---
 event(
[object]
    , [count=uint], [delete=boolean], [dieAtCollision=boolean], [emit=uint], [list=boolean], [name=string], [proc=script], [random=boolean], [rename=string], [select=boolean], [split=uint], [spread=float], [target=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

event is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.event( em=2, t='newCloud' )
At every collision, emit two new particles into the object
newCloud. The original colliding particles will survive and
remain in their original object. This event will be
assigned to the currently selected object.

cmds.event( em=2 )
At every collision, emit two new particles into the same object.

cmds.event( count=1, em=2 )
At the first collision for each particle, emit two new particles
into the same object.
Subsequent collisions for that same particle will not cause any
additional particles to be emitted. However, the new particles will
each emit two new ones at their first collision, since they also
belong to the object for which this event has been assigned.

cmds.event( die=1, count=2 )
All particles in the selected object will die at their second
collision.

cmds.event( 'myCloud', name='foo', count=1, q=1 )
Return the current value of the count parameter for the event "foo"
assigned to particle shape myCloud.  The order of the flags is
important.  Thef lag you are querying (in this case, -count) must
come before the -q.  The -name flag and the particle object name must
come after.

cmds.event( 'myCloud', d=True, name='foo' )
Delete the event "foo" assigned to particle shape myCloud.

cmds.event( 'myCloud', e=True, name='foo', emit=2 )
Edit the "emit" value of the event "foo" assigned to
particle shape myCloud.

cmds.event( 'myCloud', proc='myProc' )
Call the MEL proc "myProc(name, id, name) each time a particle
of myCloud collides with anything.

cmds.event( name='oldName', e=1, rename='newName' )
For the selected particle shape, rename the event "oldName" to "newName."

---
Return:
---


    string: for creation; string array for list.

Flags:
---


---
count(ct): uint
    properties: query, edit
    Collision number (for each particle) to which this event
applies. Zero (the default) indicates that it applies to all
collisions.

---
delete(d): boolean
    properties: create
    Delete the specified event.

---
dieAtCollision(die): boolean
    properties: query, edit
    Particle dies at the collision specified by "count."
If no count value is given, die at first collision.

---
emit(em): uint
    properties: query, edit
    Emit n additional particles into the assigned target object.
The original (colliding) particle survives as well, and remains
in its original object.  The new particles have age zero and mass
equal to the emitting particle. They use the velocity inheritance
parameter of the target object.

---
list(ls): boolean
    properties: create
    List all events for the chosen shape, like this:
event1Name event2Name ...
If no shape identified, list all events for all shapes, like this:
shape1Name event1Name shape2Name event2Name...
Returns a string array.

---
name(n): string
    properties: create, query, edit
    Assign a name to an event you are creating, or identify an
event you wish to edit, query, or delete. See examples.

---
proc(pr): script
    properties: create, query, edit
    Specify a MEL proc to be called each time the event occurs.
This must be a global proc with arguments as follows:
global proc procName( string obj, int id, string objHit );
Arguments passed in are the name of the particle object, the
id of the particle which collided, and the name of the object
collided with.  You can use particle -id -q to get values of
the particle's attributes.

---
random(r): boolean
    properties: query, edit
    Used with -split and -emit flags.  If -random is set true
and -split or -emit is set to n, then a random number of particles
uniformly distributed between 1 and n will be created at the event.

---
rename(re): string
    properties: query
    Assign a new name to an event you are editing. See examples.

---
select(s): boolean
    properties: 
    This flag is obsolete.  See the -name flag.

---
split(spl): uint
    properties: query, edit
    Colliding particle splits into specified number of
new particles. These new particles become part of the assigned
target object. If no target has been assigned, they become part of
the same object.  The new particles inherit the current age of
the particle that split.  They use the velocity inheritance
parameter of the target object.  If you set both emit and split,
the event will do both: first emit new particles, then split
the original one. This is a change from earlier versions where emit
and split were mutually exclusive.

---
spread(sp): float
    properties: query, edit
    Particles created at collision will spread out a random amount
from the rebound direction of the colliding particle.  The spread is
specified as a fraction (0-1) of 90 degrees.  If spread is set at 0
(the default) all the new particles created may coincide.

---
target(t): string
    properties: query, edit
    Target object for emitting or split particles. New particles
created through the -emit or -split flags join this object.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/event.html 
    """


def exactWorldBoundingBox(flagcalculateExactly: boolean, flagignoreInvisible: boolean) -> float[]:
    """Synopsis:
---
---
 exactWorldBoundingBox(
[dagObject...]
    , [calculateExactly=boolean], [ignoreInvisible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

exactWorldBoundingBox is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

bbox = cmds.exactWorldBoundingBox( 'sphere1', 'cube1', 'cone2')
print 'Bounding box ranges from: %f' % bbox[0], ', %f' % bbox[1], ', %f' % bbox[2],
print ' to %f' % bbox[3], ', %f' % bbox[4], ', %f' % bbox[5]

---
Return:
---


    float[]: xmin, ymin, zmin, xmax, ymax, zmax.

Flags:
---


---
calculateExactly(ce): boolean
    properties: create
    Should the bounding box calculation be exact?

---
ignoreInvisible(ii): boolean
    properties: create
    Should the bounding box calculation include or exclude
invisible objects?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/exactWorldBoundingBox.html 
    """


def excludeObjectDisplayPreset() -> string:
    """Synopsis:
---
---
 excludeObjectDisplayPreset()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

excludeObjectDisplayPreset is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.excludeObjectDisplayPreset( listPresets=True )
Result: ['All', 'None']

---
Return:
---


    string: array

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/excludeObjectDisplayPreset.html 
    """


def exclusiveLightCheckBox(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flaglight: name, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 exclusiveLightCheckBox([annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [light=name], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

exclusiveLightCheckBox is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a spot light
myLight = cmds.spotLight(coneAngle=45)

myWindow = cmds.window()
cmds.columnLayout('cl')
cmds.exclusiveLightCheckBox(width=200, label='Exclusive', light=myLight)
cmds.showWindow(myWindow)

---
Return:
---


    string: Full name to the control

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
label(l): string
    properties: create, edit
    Value of the checkbox label

---
light(lt): name
    properties: create
    The light that is to be made exclusive/non-exclusive.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/exclusiveLightCheckBox.html 
    """


def expandedSelection(flagdepth: uint, flagexpansionType: string) -> list[string] | string:
    """Synopsis:
---
---
 expandedSelection([depth=uint], [expansionType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

expandedSelection is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.createNode( 'transform' name='t1' )
cmds.createNode( 'transform' name='t2' )
cmds.connectAttr( 't1.tx', 't2.tx' )
cmds.select( 't1' );

Get the list of all DG nodes at most one connection away from the selected one, including it
cmds.expandedSelection( depth=1, expansionType='DG' )
Result: ['t1', 't2'] ---


---
Return:
---


    string: List of objects in the requested selection list expansion
    list[string]: List of nodes visited in the DG expansion
    list[string]: (Python only) List of single nodes and tuples visited in the EG or SG expansion, where tuples represent the DG nodes in a cluster

Flags:
---


---
depth(d): uint
    properties: create
    Number of steps away from current selection to expand to.
A value of 0 will not expand the selection at all.

---
expansionType(et): string
    properties: create
    The type of graph along which to expand the selection. Legal values are:
DG : Use the normal DG connections
EG : Use the evaluation graph connections
SG : Use the scheduling graph connections within the evaluation graph

If the actual selected node is not included in the graph being expanded on, e.g.
there is no evaluation node when using the EG type, then the selected node will not
appear in the output.
If this flag is not specified then the type defaults to DG.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/expandedSelection.html 
    """


def exportEdits(flageditCommand: string, flagexcludeHierarchy: boolean, flagexcludeNode: string, flagexportSelected: boolean, flagforce: boolean, flagincludeAnimation: boolean, flagincludeConstraints: boolean, flagincludeDeformers: boolean, flagincludeNetwork: boolean, flagincludeNode: string, flagincludeSetAttrs: boolean, flagincludeSetDrivenKeys: boolean, flagincludeShaders: boolean, flagonReferenceNode: string, flagselected: boolean, flagtype: string) -> list[string]:
    """Synopsis:
---
---
 exportEdits([editCommand=string], [excludeHierarchy=boolean], [excludeNode=string], [exportSelected=boolean], [force=boolean], [includeAnimation=boolean], [includeConstraints=boolean], [includeDeformers=boolean], [includeNetwork=boolean], [includeNode=string], [includeSetAttrs=boolean], [includeSetDrivenKeys=boolean], [includeShaders=boolean], [onReferenceNode=string], [selected=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

exportEdits is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


query nodes to be exported, target is selected nodes, include related shaders
nodeList = cmds.exportEdits(query=1,selected=1,includeShaders=1)

exported selected nodes and related animation nodes to file
cmds.exportEdits("myExportFile.ma",type='editMA',selected=1,includeShaders=1)
Result: C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/myExportFile.editMA

---
Return:
---


    list[string]: For query execution.

Flags:
---


---
excludeHierarchy(ehr): boolean
    properties: create, query
    By default, all DAG parents and DAG history are written to the export file.
To prevent any DAG relations not otherwise connected to the target nodes to be
included, specify the -excludeHierarchy flag.

---
excludeNode(en): string
    properties: create, query, multiuse
    Prevent the node from being included in the list of nodes being
exported. This flag is useful to exclude specific scene nodes that might
otherwise be exported. In the case where more than one Maya node has the
same name, the DAG path can be specified to uniquely identify the node.

---
exportSelected(exs): boolean
    properties: create, query
    The selected nodes and their connections to each other will be exported. Additionally,
any dangling connections to non-exported nodes will be exported.
Default nodes are ignored and never exported.
Note that when using the exportSelected flag, only selected nodes are exported, and
-include/-exclude flags such as -includeHierarchy are ignored.

---
force(f): boolean
    properties: create, query
    Force the export action to take place. This flag is required to overwrite an existing file.

---
includeAnimation(ian): boolean
    properties: create, query
    Additionally include animation nodes and animation helper nodes associated with
the target nodes being exported.

---
includeConstraints(ic): boolean
    properties: create, query
    Additionally include constraint-related nodes associated with the target nodes being exported.

---
includeDeformers(idf): boolean
    properties: create, query
    Additionally include deformer networks associated with the target nodes being exported.

---
includeNetwork(inw): boolean
    properties: create, query
    Additionally include the network of nodes connected to the target nodes being exported.

---
includeNode(includeNode): string
    properties: create, query, multiuse
    Additionally include the named node in the list of nodes being
exported. In the case where more than one Maya node has the
same name, the DAG path can be specified to uniquely identify the node.

---
includeSetAttrs(isa): boolean
    properties: create, query
    When using the -selected/-sel flag, if any of the selected nodes are referenced,
also include/exclude any setAttr edits on those nodes. If used with the -onReferenceNode/-orn
flag, include/exclude any setAttr edits on the reference.

---
includeSetDrivenKeys(sdk): boolean
    properties: create, query
    Additionally include setDrivenKey-related nodes associated with the target nodes being exported.

---
includeShaders(ish): boolean
    properties: create, query
    Additionally include shaders associated with the target nodes being exported.

---
selected(sel): boolean
    properties: create, query
    Export will operate on the list of nodes currently selected. This flag differs from the
exportSelected flag in that the selected nodes are not exported, only the edits on
them, and any nodes found via the include flags that are used (such as includeAnimation,
includeNetwork and so on).

---
type(typ): string
    properties: create, query
    Set the type of the exported file.
Valid values are "editMA" or "editMB".
Note that this command respects the global "defaultExtensions" setting
for file naming that is controlled with the file command defaultExtensions
option.  See the file command for more information.

---
editCommand(ec): string
    properties: create, query, multiuse
    This is a secondary flag used to indicate which type of reference edits should
be considered by the command.
If this flag is not specified all edit types will be included.
This flag requires a string parameter. Valid values are: "addAttr",
"connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr",
"lock" and "unlock". In some contexts, this flag may be specified
more than once to specify multiple edit types to consider.

---
onReferenceNode(orn): string
    properties: create, query, multiuse
    This is a secondary flag used to indicate that only those edits which are stored
on the indicated reference node should be considered. This flag only supports
multiple uses when specified with the "exportEdits" command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/exportEdits.html 
    """


def expression(flagalwaysEvaluate: uint, flaganimated: uint, flagattribute: string, flagname: string, flagobject: string, flagsafe: boolean, flagshortNames: boolean, flagstring: string, flagtimeDependent: boolean, flagunitConversion: string) -> string:
    """Synopsis:
---
---
 expression([alwaysEvaluate=uint], [animated=uint], [attribute=string], [name=string], [object=string], [safe=boolean], [shortNames=boolean], [string=string], [timeDependent=boolean], [unitConversion=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

expression is undoable, queryable, and editable.
If this command is being sent by the command line or in a script, then
the user should be sure to embed escaped newlines (\n), tabs (\t) for
clarity when reading them in the expression editor.  Also, quotes in an
expression must be escaped (\") so that they are not confused by the system
as the end of your string.  When using the expression editor, these
characters are escaped for you unless they are already within quotes.
Note, expressions that alter or use per-particle attributes of a particle
shape should use the 'dynExpression' command.




Example:
---
import maya.cmds as cmds

cmds.expression( s='a.translateX = b.translateX * sin(c.translateX)' )

cmds.expression( o='ball', s='tx = sin(time);' )

---
Return:
---


    string: The name of the expression

Flags:
---


---
alwaysEvaluate(ae): uint
    properties: create, query, edit
    If this is TRUE (the default), then the expression will be evaluated
whenever time changes regardless of whether the other inputs have
changed, and an output is requested.  If it is FALSE, then the expression
will only be evaluated if one or more of the inputs changes and an output is requested.  Note, if
'time' or 'frame' are inputs, then the expression will act as if this
was set to TRUE.

---
animated(an): uint
    properties: create, query, edit
    Sets the animation mode on the expression node:
0 = Not Animated,
1 = Animated,
2 = Animated with No Callback.

---
attribute(a): string
    properties: create, query, edit
    Sets the name of the attribute to use for the expression

---
name(n): string
    properties: create, query, edit
    Sets the name of the dependency graph node to use for the expression

---
object(o): string
    properties: create, query, edit
    Sets the "default" object for the expression.  This allows the
expression writer to not type the object name for frequently-used
objects.  See the examples below.

---
safe(sf): boolean
    properties: query
    Returns true if no potential side effect can occurs running that expression.
Safe expression will be optimized to evaluate only when needed even if flagged alwaysEvaluate.

---
shortNames(sn): boolean
    properties: create, query, edit
    When used with the -q/query flag, tells the command to return the expression with attribute names as short as possible.
The default is to return the FULL attribute name, regardless of how the user entered
it into the expression, including the object names.  With this flag set, attribute names
are returned as their short versions, and any attribute that belongs to the default object,
if there is one specified, will not display the object's name.

---
string(s): string
    properties: create, query, edit
    Set the expression string

---
timeDependent(td): boolean
    properties: query
    Returns true if expression is evaluated when time change.
An expression can be time-dependent for the following reasons:
- The expression refers to 'time' or 'frame' keywords.
- The expression have side effects (unsafe).
- The expression node's "time" attribute is connected manually.
If the expression is safe and not time dependend, then they will always evaluate on depend, even if alwaysEvaluate is on.

---
unitConversion(uc): string
    properties: query, edit
    Insert specified unit conversion nodes at creation: "all", "none,"
or "angularOnly." Default is "all."  For angularOnly, will insert unit
conversion nodes only for angular attributes (allowing degrees-to-radians
conversion).  This is for performance tuning.
If queried, returns the option used when the expression was created
or last edited.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/expression.html 
    """


def expressionEditorListen(flaglistenFile: string, flaglistenForAttr: string, flaglistenForExpression: string, flaglistenForName: string, flagstopListenForAttr: string, flagstopListenForExpression: string, flagstopListenForName: string) -> None:
    """Synopsis:
---
---
 expressionEditorListen([listenFile=string], [listenForAttr=string], [listenForExpression=string], [listenForName=string], [stopListenForAttr=string], [stopListenForExpression=string], [stopListenForName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

expressionEditorListen is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.expressionEditorListen()

---


Flags:
---


---
listenFile(lf): string
    properties: create
    Listen for changes to the file argument.

---
listenForAttr(la): string
    properties: create
    Listen for changes to the attributes of the node argument.

---
listenForExpression(le): string
    properties: create
    Listen for changes to the named expression

---
listenForName(ln): string
    properties: create
    Listen for name changes for the node argument.

---
stopListenForAttr(sla): string
    properties: create
    Stop listening for changes to the attributes of the
node argument.

---
stopListenForExpression(sle): string
    properties: create
    Stop listening for changes to the named expression

---
stopListenForName(sln): string
    properties: create
    Stop listening for name changes for the node argument.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/expressionEditorListen.html 
    """


def extendCurve(flagcaching: boolean, flagconstructionHistory: boolean, flagcurveOnSurface: boolean, flagdistance: linear, flagextendMethod: int, flagextensionType: int, flaginputPoint: tuple[linear, linear, linear], flagjoin: boolean, flagname: string, flagnoChanges: boolean, flagnodeState: int, flagobject: boolean, flagpointX: linear, flagpointY: linear, flagpointZ: linear, flagrange: boolean, flagremoveMultipleKnots: boolean, flagreplaceOriginal: boolean, flagstart: int) -> list[string]:
    """Synopsis:
---
---
 extendCurve(
object
    , [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [distance=linear], [extendMethod=int], [extensionType=int], [inputPoint=[linear, linear, linear]], [join=boolean], [name=string], [noChanges=boolean], [nodeState=int], [object=boolean], [pointX=linear], [pointY=linear], [pointZ=linear], [range=boolean], [removeMultipleKnots=boolean], [replaceOriginal=boolean], [start=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

extendCurve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

to extend the start of a curve with a line of distance 3
cmds.extendCurve( em=0, et=0, s=True, d=3.0 )

to extend the end of a curve to a point
cmds.extendCurve( em=2, s=False, ip=(1, 2, 3) )

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
    The distance to extend
Used only for extendMethod is byDistance.
Default: 1

---
extendMethod(em): int
    properties: create, query, edit
    The method with which to extend:
0 - based on distance,
2 - to a 3D point
Default: 0

---
extensionType(et): int
    properties: create, query, edit
    The type of extension:
0 - linear,
1 - circular,
2 - extrapolate
Default: 0

---
inputPoint(ip): [linear, linear, linear]
    properties: create, query, edit
    The point to extend to (optional)

---
join(jn): boolean
    properties: create, query, edit
    If true, join the extension to original curve
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
pointX(px): linear
    properties: create, query, edit
    X of the point to extend to
Default: 0

---
pointY(py): linear
    properties: create, query, edit
    Y of the point to extend to
Default: 0

---
pointZ(pz): linear
    properties: create, query, edit
    Z of the point to extend to
Default: 0

---
removeMultipleKnots(rmk): boolean
    properties: create, query, edit
    If true remove multiple knots at join
Used only if join is true.
Default: false

---
start(s): int
    properties: create, query, edit
    Which end of the curve to extend.
0 - end,
1 - start,
2 - both
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
noChanges(nc): boolean
    properties: create, query, edit
    If set then the operation node will be automatically put into pass-through mode.

---
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
range(rn): boolean
    properties: create
    Force a curve range on complete input curve.

---
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/extendCurve.html 
    """


def extendSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagdistance: linear, flagextendDirection: int, flagextendMethod: int, flagextendSide: int, flagextensionType: int, flagjoin: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagreplaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 extendSurface(
surface [surface]
    , [caching=boolean], [constructionHistory=boolean], [distance=linear], [extendDirection=int], [extendMethod=int], [extendSide=int], [extensionType=int], [join=boolean], [name=string], [nodeState=int], [object=boolean], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

extendSurface is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

---
Create a nurbs plane, then extend both sides of the plane by 10
cmds.nurbsPlane(n='plane1')
cmds.extendSurface('plane1', d=10, es=2)

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
    The distance to extend (for by distance only)
Default: 1

---
extendDirection(ed): int
    properties: create, query, edit
    Which parametric direction of the surface to extend ( 0 - U, 1 - V, 2 - both )
Default: 0

---
extendMethod(em): int
    properties: create, query, edit
    The extend method (0 - distance)
Default: 0

---
extendSide(es): int
    properties: create, query, edit
    Which end of the surface to extend ( 0 - end, 1 - start, 2 - both )
Default: 1

---
extensionType(et): int
    properties: create, query, edit
    The type of extension (0 - tangent, 2 - extrapolate)
Default: 0

---
join(jn): boolean
    properties: create, query, edit
    Join extension to original
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/extendSurface.html 
    """


def extrude(flagcaching: boolean, flagconstructionHistory: boolean, flagdegreeAlongLength: int, flagdirection: tuple[linear, linear, linear], flagdirectionX: linear, flagdirectionY: linear, flagdirectionZ: linear, flagextrudeType: int, flagfixedPath: boolean, flaglength: linear, flagmergeItems: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagpivot: tuple[linear, linear, linear], flagpolygon: int, flagrange: boolean, flagrebuild: boolean, flagreverseSurfaceIfPathReversed: boolean, flagrotation: angle, flagscale: float, flagsubCurveSubSurface: boolean, flaguseComponentPivot: int, flaguseProfileNormal: boolean) -> list[string]:
    """Synopsis:
---
---
 extrude(
curve [curve]
    , [caching=boolean], [constructionHistory=boolean], [degreeAlongLength=int], [direction=[linear, linear, linear]], [directionX=linear], [directionY=linear], [directionZ=linear], [extrudeType=int], [fixedPath=boolean], [length=linear], [mergeItems=boolean], [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [range=boolean], [rebuild=boolean], [reverseSurfaceIfPathReversed=boolean], [rotation=angle], [scale=float], [subCurveSubSurface=boolean], [useComponentPivot=int], [useProfileNormal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

extrude is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

extrude profile curve "distance" 5 units along x axis
cmds.extrude ('profile', et = 0, d= (1, 0, 0), l= 5)

extrude profile curve along path curve using "flat" method
cmds.extrude( 'profile', 'path', et=1 )

extrude profile curve along path curve using "tube" method
cmds.extrude( 'profile', 'path', et=2 )

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
degreeAlongLength(dl): int
    properties: create, query, edit
    Surface degree along the distance when a distance extrude is performed
Default: 1

---
direction(d): [linear, linear, linear]
    properties: create, query, edit
    The direction in which to extrude.
Use only for distance extrudeType and useProfileNormal off

---
directionX(dx): linear
    properties: create, query, edit
    X of the direction
Default: 0

---
directionY(dy): linear
    properties: create, query, edit
    Y of the direction
Default: 1

---
directionZ(dz): linear
    properties: create, query, edit
    Z of the direction
Default: 0

---
extrudeType(et): int
    properties: create, query, edit
    The extrude type (distance-0, flat-1, or tube-2)
Default: 2

---
fixedPath(fpt): boolean
    properties: create, query, edit
    If true, the resulting surface will be placed at the path curve.
Otherwise, the resulting surface will be placed at the profile curve.
Default: false

---
length(l): linear
    properties: create, query, edit
    The distance to extrude.
Use only for distance extrudeType
Default: 1

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
    The pivot point used for tube extrudeType

---
reverseSurfaceIfPathReversed(rsp): boolean
    properties: create, query, edit
    If true, extrude type is tube (2) and path has been internally reversed then computed surface is reversed in the direction corresponding to the path.
Default: false

---
rotation(ro): angle
    properties: create, query, edit
    Amount to rotate the profile curve as it sweeps along the path curve.
Default: 0.0

---
scale(sc): float
    properties: create, query, edit
    Amount to scale the profile curve as it sweeps along the path curve.
Default: 1.0

---
subCurveSubSurface(scs): boolean
    properties: create, query, edit
    If true, curve range on the path will get applied to the resulting surface instead of cut before the extrude.
Default: false

---
useComponentPivot(ucp): int
    properties: create, query, edit
    Use closest endpoint of the path - 0, component pivot - 1 or the center of the bounding box of the profile - 2
Default: 0

---
useProfileNormal(upn): boolean
    properties: create, query, edit
    If true, use the profile curve normal for the direction in which to extrude.
Use only for distance or tube extrudeType.
Default: false

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
mergeItems(mi): boolean
    properties: create
    Merge component results where possible. For example, instead of returning a[1] and a[2], return a[1:2].

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/extrude.html 
    """
