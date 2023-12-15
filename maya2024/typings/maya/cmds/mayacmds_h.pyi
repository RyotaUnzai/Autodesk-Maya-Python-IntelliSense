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


def hardenPointCurve(flagcaching: boolean, flagconstructionHistory: boolean, flagmultiplicity: int, flagname: string, flagnodeState: int, flagobject: boolean, flagreplaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 hardenPointCurve(
curve
    , [caching=boolean], [constructionHistory=boolean], [multiplicity=int], [name=string], [nodeState=int], [object=boolean], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hardenPointCurve is undoable, queryable, and editable.

limitations
The CV whose multiplicity is being raised needs to have its
neighbouring CVs of multiplicity 1.  How many neighbours depends on
the degree of the curve and the difference in CV multiplicities before
and after this operation.  For example, if you're changing a CV of
multiplicity 1 into a CV of multiplicity 3, you will need the 4
neighbouring CVs (2 on each side) to be of multiplicity 1.  The CVs
that do not satisfy that requirement will be ignored.




Example:
---
import maya.cmds as cmds

Make the example curve.
cmds.curve( d=3, p=((-7.253894, 0, 10.835724), (-7.423939, 0, 6.977646), (-7.400778, 0, 2.798971), (-7.458196, 0, -1.524959), (-2.411453, 0, -1.07677), (1.44791, 0, -0.8977448), (5.526346, 0, -0.8610371), (5.740407, 0, 3.780402), (6.293634, 0, 7.571941), (5.957847, 0, 10.72273), (2.753946, 0, 10.894312), (-0.6375988, 0, 11.062571), (-5.889847, 0, 10.940658)), k=(0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10) )

Raise the ones that you want to have "sharp" corners
cmds.hardenPointCurve( 'curve1.cv[3]', 'curve1.cv[6]', 'curve1.cv[9]', ch=True, rpo=True, m=-1 )

Same result, as the in-between CVs are ignored:
cmds.undo()
cmds.hardenPointCurve( 'curve1.cv[0:12]', ch=1, rpo=1, m=-1 )

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
multiplicity(m): int
    properties: create, query, edit
    the required multiplicity of the curve knot
Default: -1

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hardenPointCurve.html 
    """


def hardware(flagbrdType: boolean, flagcpuType: boolean, flaggraphicsType: boolean, flagmegaHertz: boolean, flagnumProcessors: boolean) -> string:
    """Synopsis:
---
---
 hardware([brdType=boolean], [cpuType=boolean], [graphicsType=boolean], [megaHertz=boolean], [numProcessors=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hardware is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.hardware( cpu=True )
cmds.hardware( brd=True )

---
Return:
---


    string: Command result

Flags:
---


---
brdType(brd): boolean
    properties: create
    Returns IP number identifying the CPU motherboard

---
cpuType(cpu): boolean
    properties: create
    Returns type of CPU

---
graphicsType(gfx): boolean
    properties: create
    Returns string identifying graphics hardware type

---
megaHertz(mhz): boolean
    properties: create
    Returns string identifying the speed of the CPU chip

---
numProcessors(npr): boolean
    properties: create
    Returns string identifying the number of processors

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hardware.html 
    """


def hardwareRenderPanel(flagcamera: string, flagcontrol: boolean, flagcopy: string, flagcreateString: boolean, flagdefineTemplate: string, flagdocTag: string, flageditString: boolean, flagexists: boolean, flagglRenderEditor: boolean, flaginit: boolean, flagisUnique: boolean, flaglabel: string, flagmenuBarRepeatLast: boolean, flagmenuBarVisible: boolean, flagneedsInit: boolean, flagparent: string, flagpopupMenuProcedure: script, flagreplacePanel: string, flagtearOff: boolean, flagtearOffCopy: string, flagtearOffRestore: boolean, flagunParent: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 hardwareRenderPanel(
panelName
    , [camera=string], [control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean], [glRenderEditor=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hardwareRenderPanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window( width=500 )
theLayout = cmds.formLayout()
theHWbuffer = cmds.hardwareRenderPanel()
cmds.formLayout( theLayout, e=True, af=((theHWbuffer, 'top', 0), (theHWbuffer, 'left', 0), (theHWbuffer, 'bottom', 0), (theHWbuffer, 'right', 0)) )
cmds.showWindow()

---
Return:
---


    string: Panel name

Flags:
---


---
camera(cam): string
    properties: query, edit
    Query or edit the camera in a gl render panel.

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
glRenderEditor(gre): boolean
    properties: query
    Query only. This flag returns the name of the
gl render editor contained in the panel.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hardwareRenderPanel.html 
    """


def hasMetadata(flagasList: boolean, flagchannelName: string, flagchannelType: string, flagendIndex: string, flagignoreDefault: boolean, flagindex: string, flagindexType: string, flagmemberName: string, flagscene: boolean, flagstartIndex: string, flagstreamName: string) -> boolean[] | list[string]:
    """Synopsis:
---
---
 hasMetadata([asList=boolean], [channelName=string], [channelType=string], [endIndex=string], [ignoreDefault=boolean], [index=string], [indexType=string], [memberName=string], [scene=boolean], [startIndex=string], [streamName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hasMetadata is NOT undoable, NOT queryable, and NOT editable.
This command is used to query for the presence of metadata elements on a node,
components, or scene. The command works at all levels of metadata presence, from
the existence of any metadata at all on a node or scene right down to the presence
of metadata values set on a particular metadata Stream index.

Filter Flags
channelName - Only look for metadata on one particular Channel type
streamName - Only look for metadata on one particular named Stream. When
used in conjunction with channelName then ignore Streams with a matching
name but a different Channel type
index - Only look for metadata on one or more specific Index values of
a Stream. Requires use of the streamName flag. Does not require the
indexType flag as that will be inferred by the streamName.
startIndex/endIndex - Same as index but using an entire range of
Index values rather than a single one
indexType - Only look for metadata using a particular Index type. Can
have its scope narrowed by other filter flags as well.
ignoreDefault - Treat any metadata that still has the default value
(e.g. 0 for numerics, "" for strings) the same as metadata that isn't present.
This means that any metadata with default values will not be reported. It is
useful for quickly finding values that you have changed. When this flag is
set you can also use the memberName filter to narrow down the check to
a particular member of the metadata Structure. Without that filter it will only
skip over metadata where every member of the Structure has a non-default value.
memberName - Only look at one particular Member in the metadata in a
Structure. Only used when checking for non-default values as existence is based
on the entire Structure, not any particular Member.

Operation Flags
normal mode - Return True for every specified location containing
metadata. This combines with the filter flags as follows:
no flag - True if there is any metadata at all on the node or scene
channelName - True if there is any metadata at all on the Channel
        with the given name
streamName - True if there is any metadata at all on the Stream
        with the given name
index/startIndex/endIndex - An array of booleans ordered the same
        as the natural ordering of the Index values (i.e. specifying index 3, 2, and 4
        in that order will still return booleans in the order for indices 2,3,4)
        where True means that there is metadata assigned at that Index. This form is
        better suited with the asList modification since with that variation it
        is easier to tell exactly which indices have the metadata.


asList - Adding this flag switches the return values from a single boolean
or array of booleans to an array of strings indicating exactly which metadata elements
have values. The return values of the command are changed to be the following:
no flag - List of Channel names with metadata
channelName - List of Stream names in the Channel with metadata
streamName - List of Index values on the Stream with metadata
index/startIndex/endIndex - List of Index values with metadata,
        restricted to the set of specified Index values.






Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.polyPlane( name='smcPlane', constructionHistory=False )
Result: smcPlane ---


Create structures
cmds.dataStructure( format='raw', asString='name=idStructure:int32=ID' )
Result: idStructure ---

cmds.dataStructure( format='raw', asString='name=keyValueStructure:string=value' )
Result: keyValueStructure ---


Apply structures to plane
cmds.select( 'smcPlaneShape', replace=True )
cmds.addMetadata( structure='idStructure', streamName='idStream', channelName='vertex' )
cmds.addMetadata( structure='keyValueStructure', streamName='keyValueStream', channelName='key', indexType='string' )

Apply the metadata values to three of the components by selection
cmds.select( 'smcPlaneShape.vtx[8:10]', replace=True )
cmds.editMetadata( streamName='idStream', memberName='ID', value=7 )
Result: 3 ---


Verify existence of the three newly set metadata values at the node level
cmds.select( 'smcPlaneShape', replace=True )
cmds.hasMetadata()
Result: [True] ---


Verify existence of the three newly set metadata values at the Channel level
cmds.hasMetadata( channelName='vertex' )
Result: [True] ---

cmds.hasMetadata( channelName='edge' )
Result: [False] ---


Verify existence of the three newly set metadata values at the Stream level
cmds.hasMetadata( channelName='vertex', streamName='idStream' )
Result: [True] ---

cmds.hasMetadata( channelName='edge', streamName='someOtherStream' )
Result: [False] ---


Verify existence of the three newly set metadata values at the Index level
cmds.hasMetadata( channelName='vertex', streamName='idStream', index=['8','9'] )
Result: [True, True] ---

cmds.hasMetadata( channelName='vertex', streamName='idStream', index=['8','9999'] )
Result: [True, False] ---


Verify existence of default metadata values at the Index level. Since the
index range was established to be 0-17 by assignment and the Stream
defaults to returning default values for unassigned indices the lower index
values "0" and "1" do have metadata (as default values) but the higher one
"9999" in the above example does not.
cmds.hasMetadata( channelName='vertex', streamName='idStream', index=['0','1'] )
Result: [True, True] ---


Verify non-existence of non-default metadata values at the Index level
cmds.hasMetadata( ignoreDefault=True, channelName='edge', streamName='idStream', memberName='ID', index=['0','1'] )
Result: [False, False] ---


Get the list of Index values with assigned metadata on the object
cmds.select( 'smcPlaneShape.vtx[8:20]', replace=True )
cmds.hasMetadata( channelName='vertex', streamName='idStream', asList=True )
Result: [u'8', u'9', u'10'] ---


Set metadata values using the complex index type='string'
cmds.editMetadata( streamName='keyValueStream', memberName='value', stringValue='Starry Night', indexType='string', index='Title' )
cmds.editMetadata( streamName='keyValueStream', memberName='value', stringValue='Vincent Van Gogh', indexType='string', index='Artist' )

Verify existence of the complex index data
cmds.hasMetadata( streamName='keyValueStream', memberName='value', channelName='key', index=['Title','Artist'], indexType='string', asList=True )
Result: [u'Artist', u'Title'] ---


---
Return:
---


    list[string]: List of indexes in the filtered list which contain metadata
    boolean[]: List of answers to whether the specified item(s) have metadata

Flags:
---


---
asList(al): boolean
    properties: create
    Use this flag when you want to return string values indicating where the
metadata lives rather than boolean values. See the command description
for more details on what this flag will return.

---
ignoreDefault(id): boolean
    properties: create
    Use this flag when you want to skip over any metadata that has only
default values. i.e. the metadata may exist but it hasn't had a new
value set yet (non-zero for numerics, non-empty strings, etc.)
See the command description for more details on how this flag filters
the search.

---
memberName(mn): string
    properties: create
    Name of the Structure member being checked. The names of the members are
set up in the Structure definition, either through the description passed
in through the "dataStructure" command or via the API used to create that
Structure. As the assignment of metadata is on a per-structure basis this
flag only needs to be specified when querying for non-default values. If
you query for non-default values and omit this flag then it checks that
any of the members have a non-default value.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hasMetadata.html 
    """


def headsUpDisplay(flagallDescendants: boolean, flagallowOverlap: boolean, flagattachToRefresh: boolean, flagattributeChange: string, flagblock: int, flagblockAlignment: string, flagblockSize: string, flagcommand: script, flagconditionChange: string, flagconditionFalse: string, flagconditionTrue: string, flagconnectionChange: string, flagdataAlignment: string, flagdataFontSize: string, flagdataWidth: int, flagdecimalPrecision: int, flagdisregardIndex: boolean, flagevent: string, flagexists: boolean, flaggetOption: string, flaggridColor: int, flaglabel: string, flaglabelFontSize: string, flaglabelWidth: int, flaglastOccupiedBlock: int, flaglayoutVisibility: boolean, flaglistConditions: boolean, flaglistEvents: boolean, flaglistHeadsUpDisplays: boolean, flaglistNodeChanges: boolean, flaglistPresets: boolean, flagname: string, flagnextFreeBlock: int, flagnodeChanges: string, flagpadding: int, flagpreset: string, flagrefresh: boolean, flagremove: boolean, flagremoveID: int, flagremovePosition: tuple[int, int], flagresetNodeChanges: string, flagscriptResult: boolean, flagsection: int, flagsetOption: tuple[string, string], flagshowGrid: boolean, flagvisible: boolean) -> int | string | int | int[2]:
    """Synopsis:
---
---
 headsUpDisplay([string], [allDescendants=boolean], [allowOverlap=boolean], [attachToRefresh=boolean], [attributeChange=string], [block=int], [blockAlignment=string], [blockSize=string], [command=script], [conditionChange=string], [conditionFalse=string], [conditionTrue=string], [connectionChange=string], [dataAlignment=string], [dataFontSize=string], [dataWidth=int], [decimalPrecision=int], [disregardIndex=boolean], [event=string], [exists=boolean], [getOption=string], [gridColor=int], [label=string], [labelFontSize=string], [labelWidth=int], [lastOccupiedBlock=int], [layoutVisibility=boolean], [listConditions=boolean], [listEvents=boolean], [listHeadsUpDisplays=boolean], [listNodeChanges=boolean], [listPresets=boolean], [name=string], [nextFreeBlock=int], [nodeChanges=string], [padding=int], [preset=string], [refresh=boolean], [remove=boolean], [removeID=int], [removePosition=[int, int]], [resetNodeChanges=string], [scriptResult=boolean], [section=int], [setOption=[string, string]], [showGrid=boolean], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

headsUpDisplay is NOT undoable, queryable, and editable.
The only mandatory flags, on creation are the section and block flags. Note if the preset
OR command/trigger flags are not present, only a label will be drawn on the viewport.

Upon creation of a HUD object, an ID number will be assigned to it. This can be used to
remove the HUD object (-rid/removeID [int IDNumber]), if desired. Alternatively, HUD
objects may be removed via their position (section and block), or their unique name.




Example:
---
import maya.cmds as cmds

---

---
Define a procedure that returns a value to be used by the Heads Up Display
---

def objectPosition(*args):
        try:
                selectedNodes = cmds.selectedNodes()
                mainObj = selectedNodes[-1]
                positionList = cmds.getAttr('%s.translate' % mainObj)
                return positionList[0]
        except:
                return (0.0,0.0,0.0)

---

---
Now, create a HUD object to display the return value of the above procedure
---

---
Attributes:
---

       - Section 1, block 0, represents the top second slot of the view.
       - Set the blockSize to "medium", instead of the default "small"
       - Assigned the HUD the label: "Position"
       - Defined the label font size to be large
       - Assigned the HUD a command to run on a SelectionChanged trigger
       - Attached the attributeChange node change to the SelectionChanged trigger
         to allow the update of the data on attribute changes.
---

cmds.headsUpDisplay( 'HUDObjectPosition', section=1, block=0, blockSize='medium', label='Position', labelFontSize='large', command=objectPosition, event='SelectionChanged', nodeChanges='attributeChange' )

---

---
Create a preset HUD object to display the camera names.
---

---
Attributes:
---

   - Section 2, block 0, represents the top middle slot of the view.
   - Using blockalign, the HUD object is centered in the middle of the block
   - Setting a dw of 50, allocates a space of 50 pixels for the data to reside in.
   - Finally setting the preset to "cameraNames", selects a preset which will
     automatically insert the associated data into the data field.
---

cmds.headsUpDisplay( 'HUDCameraName', s=2, b=0, ba='center', dw=50, pre='cameraNames')

---

---
Now, remove these two HUDs. Both can be removed in three ways: name, ID or position.
---
The following examples will demonstrate removal by name and position
---

cmds.headsUpDisplay( 'HUDObjectPosition', rem=True )

cmds.headsUpDisplay( rp=(7, 0) )

---
Return:
---


    int: ID number of the Heads-Up Display (HUD), for regular command execution.
    string|int|int[2]: HUD name, HUD ID or Section and block value, for respective remove commands.

Flags:
---


---
allDescendants(ad): boolean
    properties: create, edit
    This flag can only be used in conjunction with the -ac/attributeChange
flag. If it is specified, and the HUD is attached to a compound or multi
attribute, then the HUD command will run due to changes to the specified
attribute as well as changes to its descendants.

---
allowOverlap(ao): boolean
    properties: create, query, edit
    Sets the Heads-Up Display to be visible regardless of overlapping section
widths/limitations (see -s/section flag description for more details).

---
attachToRefresh(atr): boolean
    properties: create, query, edit
    Attaches the command to the refresh process. The script is then run each time
an idle refresh is run and updates directly following it.

---
attributeChange(ac): string
    properties: create, edit
    Runs the command when the named attribute changes value. The string must
identify both the dependency node and the particular attribute. If the
dependency node is deleted, this HUD is removed (even if the deletion is
undoable).

---
block(b): int
    properties: create, query, edit
    Denotes the individual block that the HUD will reside in, within a
section. Each section is composed of a single column of blocks.
The total number of blocks contained within each section is variable.

The number of blocks that will be visible within each section is
dependent on the size of blocks contained in each section and the
current size of the window. Blocks begin enumerating from 0 and
flexibly increase based on need.

The resultant output string of each HUD is formatted within each block,
using parameters defined by the formatting flags listed below (eg. justify,
padding, labelWidth and dataWidth). The layout is shown in the following
diagram:

 __________________________________________
|     |     |        |         |     |     |
|  P  |  J  |   LW   |   DWX   |  J  |  P  |
|_____|_____|________|_________|_____|_____|
P = Sub-block of width, padding
J = Justification of the entire block
LW = Sub-block of width, labelWidth
DWX = X number of sub-blocks of width, dataWidth, for X data elements.


Block Layout

The above diagram shows the layout of each block. The widths: padding,
labelWidth and dataWidth are defined by their respective flags. To
elaborate on the layout of the blocks, First the padding of the block is
calculated. Then the two main sub-blocks (LW and DWX) in the above diagram,
are justified and positioned together between the left and right margins
of the block. The widths of the main sub-blocks are not variable based on
it's contents. The only sub-block in the above diagram which is unique is the
DWX sub-block which actually represents X number of sub-blocks, where X
is the number of data elements returned by the command.

Block Positioning

Blocks on the top section begin from the top edge of the main
viewport, while the bottom section begins from the bottom edge.
Blocks are dynamically removed from visibility from the midpoint
of the viewport. So, a relatively large block number will not
draw to the viewport.

Lastly, there can be at most one HUD occupying a block at any time.
Trying to position a HUD in an occupied block will result in an error.
Keep this in mind when positioning the HUD.

---
blockAlignment(ba): string
    properties: create, query, edit
    Specifies the alignment of the block within its respective column. Available
alignments are: "center", "left" and "right". The default alignment is "left".

---
blockSize(bs): string
    properties: create, query, edit
    Sets the height of each block. Available heights are: small, medium and large.
In pixel measurements, each corresponds to a 20, 35 or 50 pixel height, respectively.

---
command(c): script
    properties: create, query, edit
    Specifies the procedure or script to run, in order to obtain the
desired information. This must return a value or an array of values.
A warning will be displayed if the command does not return a value.
This flag MUST always be accompanied by a trigger flag (eg. a condition flag,
an event flag, an attachToRefresh flag, etc.).

---
conditionChange(cc): string
    properties: create, edit
    A trigger which runs the command (to sample the data), when the
named condition changes. The named condition must be pre-defined or a
user defined boolean. To get a list of what conditions exist, use
the -lc/listConditions flag.

---
conditionFalse(cf): string
    properties: create, edit
    A trigger which runs the command (to sample the data), when the
named condition becomes false. The named condition must be pre-defined or
a user defined boolean. To get a list of what conditions exist, use
the -lc/listConditions flag.

---
conditionTrue(ct): string
    properties: create, edit
    A trigger which runs the command (to sample the data), when the
named condition becomes true. The named condition must be pre-defined or a
user defined boolean. To get a list of what conditions exist, use
the -lc/listConditions flag.

---
connectionChange(con): string
    properties: create, edit
    Runs the command when the named attribute changes its connectivity. The
string must identify both the dependency node and the particular attribute.
If the dependency node is deleted, this HUD is removed (even if the deletion
is undoable).

---
dataAlignment(da): string
    properties: create, query, edit
    Specifies the alignment of the data blocks and the data text, within a HUD block.
Available alignments are: "left" and "right". The default alignment is "left".

---
dataFontSize(dfs): string
    properties: create, query, edit
    Sets the font size of the returned data. Available sizes are: small and large.

---
dataWidth(dw): int
    properties: create, query, edit
    Specifies the pixel width of the virtual "textbox" which will hold a data value.
For commands which return more than one value (ie. arrays), one of these "textboxes"
will be created for each data element, each with this specified width. If the width
of the data value exceeds the width of the "textbox", the data value will be
truncated to fit within the dimensions of the "textbox." (To see a layout of a
block, see the description of the -block flag.)

---
decimalPrecision(dp): int
    properties: create, query, edit
    Sets the decimal precision of any floating point value returned by the command. The valid
range of precision values are 1 to 8.

---
disregardIndex(di): boolean
    properties: create, edit
    This flag can only be used in conjunction with the -ac/attributeChange
flag. If it is specified, and the HUD is attached to a multi (indexed)
attribute, then the HUD command will run no matter which attribute in
the multi changes.

---
event(ev): string
    properties: create, edit
    Runs the command when the named event occurs. The named event, must be a
pre-defined Maya event. To get a list of what events exist, use the
-le/listEvents flag.

---
exists(ex): boolean
    properties: create, query
    This flag returns whether the given object exists in the Heads-Up Display layout.
An object name must be supplied with this command. This flag cannot be combined
with any other flag.

---
getOption(op): string
    properties: query
    This flag will return the value of the option specified by the string.
See setOption for a list of options
                        In query mode, this flag needs a value.

---
gridColor(gco): int
    properties: create, query, edit
    This flag specifies a color for the grid lines using the inactive color palette. Specifying
an index number between 1 to 23 will select the corresponding color in the palette.

---
label(l): string
    properties: create, query, edit
    Text string that appears to the left of the desired information.

---
labelFontSize(lfs): string
    properties: create, query, edit
    Sets the font size of the label. Available sizes are: small and large.

---
labelWidth(lw): int
    properties: create, query, edit
    Specifies the pixel width of the virtual "textbox" which will hold the label. The
contents of this "textbox" will be left justified. If the width of the actual label
exceeds the width of the "textbox," the label will be truncated to fit within the
dimensions of the "textbox." (To see a layout of a block, see the description
of the -block flag.)

---
lastOccupiedBlock(lob): int
    properties: create
    Returns the block number of the last occupied block in a given section.

---
layoutVisibility(lv): boolean
    properties: create, query, edit
    Sets the visibility of Heads-Up Display layout on and off. This does not
modify individual visibilities of heads-up displays, but turns off the layout
so that no heads-up displays will draw to screen. Personalized settings for
the visibilities of HUDs are kept safe. This flag can only be used by itself,
excepting edit and query.

---
listConditions(lc): boolean
    properties: create, query
    This flag will return a string array containing all names of the available
conditions.

---
listEvents(le): boolean
    properties: create, query
    This flag will return a string array containing all names of the available
events.

---
listHeadsUpDisplays(lh): boolean
    properties: create, query
    This flag will return a string array containing all names of existing HUDs.

---
listNodeChanges(lnc): boolean
    properties: create, query
    This flag will return a string array containing all names of the available
node changes.

---
listPresets(lp): boolean
    properties: create, query
    This flag will return a string array containing all names of the available
preset HUDs.

---
name(n): string
    properties: edit
    This flag only permits the EDITING of the name of the Heads-Up Display.

---
nextFreeBlock(nfb): int
    properties: create
    Returns the block number of the next free block in a given section.

---
nodeChanges(nc): string
    properties: create, query, edit, multiuse
    Works only with selection based triggers (ie. "SelectionChanged" or "SomethingSelected"),
otherwise this flag is ignored. This flag attaches the HUD script to execute on specific
node changes of any selected node. This flag is used to set a nodeChange. In order to
reset a nodeChange, use the -rnc/resetNodeChanges flag. To view a list of all available
node changes, use the -lnc/listNodeChanges flag. The following is a list of available node
changes and their function:

attributeChange:  The script will be sensitive to any attribute changes in the currently
                  selected nodes.

connectionChange: The script will be sensitive to any connection changes in the currently
                  selected nodes.

instanceChange:   The script will be sensitive to any changes to an instance in the
                  currently selected nodes.


On query mode, this flag will return the values of all nodeChanges in pairs of values
(the name of the nodeChange followed by its value).

WARNING: (Performance Warning)
         Attaching a nodeChange trigger to a selection based trigger can cause a large
         performance drop, if the node change that is being watched is caused by the
         HUD script itself.

         With this said, an attempt should be made to keep the HUD command/script
                 simple and limited to retrieving data. Changing an attribute, creating or
                 modifying a connection or instance will all result in a performance drop.

---
padding(p): int
    properties: create, query, edit
    Specifies the width of both the left and right margins of a block. Default
value is 15 pixels.

---
preset(pre): string
    properties: create, query, edit
    This setting is used to select certain pre-defined HUDs, some of which retrieve
specific data, that is unobtainable through normal MEL commands or scripts. This flag
is mutually exclusive from the command and trigger flag combination. However, presets
can work with all other headsUpDisplay attribute flags (ie. block alignment, label,
dataFontSize, etc.), unless otherwise specified below. To obtain a list
of available presets, use the -lp/listPresets flag on this command.

The following is a list of available presets and a description of each:

cameraNames
This will return the camera name that the view is looking through, in
the data block, for each view that the HUD is drawing to.
polyVerts
This will return three values in the data block, regarding the number of
vertices that are visible by the camera.

1st Value: Represents the number of camera visible vertices, both
active and inactive.
2nd Value: Represents the number of camera visible vertices, on
active objects only.
3rd Value: Represents the number of camera visible vertices, that
are active.

polyEdges
This will return three values in the data block, regarding the number of
edges that are visible by the camera. The order of these three values are
similar to the polyVerts preset.
polyFaces
This will return three values in the data block, regarding the number of
faces that are visible by the camera. The order of these three values are
similar to the polyVerts preset.
polyUVs
This will return three values in the data block, regarding the number of
UVs that are visible by the camera. The order of these three values are
similar to the polyVerts preset.
polyTriangles
This will return three values in the data block, regarding the number of
triangles that are visible by the camera. The order of these three values are
similar to the polyVerts preset.
materialLoadingCount
This will return the material loading count.
It updates on each refresh.
textureLoadingCount
This will return the texture loading count.
It updates on each refresh.
frameRate
This will return a single string carrying both the frame rate and the "fps"
string in the data block. It updates on each refresh.
viewAxis
This will draw the orientation of the grid axes within the HUD. It updates
on each refresh. While this preset can take in all attribute flags, the
only one which will have an effect are block attribute related flags
(ie. block alignment and block size). The block dimensions of this preset
are: blockSize - "large" and blockWidth - "50", which results in a 50x50
pixel region.
distanceFromCamera
This will return in the data block the distance from the view's camera
to the centre of the bounding box containing the selected objects in the view.

---
refresh(r): boolean
    properties: create
    This flag forces the given Heads-Up Display element to refresh, updating
the value displayed.  This flag cannot be combined with any other flag.

---
remove(rem): boolean
    properties: create, edit
    This command will remove a given HUD object, given a specified HUD name. This flag will
override all other flags and is mutually exclusive from the other remove flags.

---
removeID(rid): int
    properties: create, edit
    This command will remove a given HUD object, given a specified HUD ID number assigned
to it at creation time. This flag will override all other flags and is mutually exclusive
from the other remove flags.

---
removePosition(rp): [int, int]
    properties: create, edit
    This command will remove the contents of a specific block location in the HUD layout.
This flag will override all other flags and is mutually exclusive from the other remove
flags. Syntax for this flag is: -removePosition/rp [section] [block].

---
resetNodeChanges(rnc): string
    properties: edit, multiuse
    This flag will reset a specificied nodeChange back to false. This flag only operates under
the edit flag. See the description for the -nc/nodeChanges flag for further details.

---
scriptResult(sr): boolean
    properties: query
    This flag is only used in conjunction with the query flag. Calling a query on this flag
returns the most recent result of the HUD.

---
section(s): int
    properties: create, query, edit
    Defines the section the HUD will appear in. There are 10 sections
divided across the screen. Five columns and two rows make up the
ten element matrix which divide the main viewport. Here is a visual
layout of the sections.

 ________________________
|    |    |    |    |    |
|    |    |    |    |    |
| 0  | 1  | 2  | 3  | 4  |
|    |    |    |    |    |
|____|____|____|____|____|
|    |    |    |    |    |
|    |    |    |    |    |
| 5  | 6  | 7  | 8  | 9  |
|    |    |    |    |    |
|____|____|____|____|____|
Each section is denoted by a number from 0 to 9 as illustrated above.
For example, if the second column of the top row was desired, the
section would be defined as: -sec 1

To prevent HUD objects from displaying over each other and causing a
clutter of letters, each row has a defined visibility precedence,
where each section would have a visibility priority level. Depending
on each priority level, when the screen space begins to shrink to
a point where the section widths of a given row begin to collide, the
HUD automatically compensates for this by removing the sections of
least priority. These sections are made invisible and a warning is
issued to inform the user of the removal. This continues until only
the section of highest priority remains.

For each row, the priorities are defined as follows. Using the top
row as an example: Section 0, has the highest priority, followed
by Section 4, making the outermost sections of highest priority.
Next in the list is Section 2, and lastly Sections 1 and 3 are of
the equal and least priority. This priority structure can be applied
to the bottom row as well. The two outermost sections have the highest
priority, followed by the middle section, and finally the remaining
two sections are of lowest priority.

This means that as the viewport gradually decreases in width
to the point where sections in the top row begin to overlap, sections
1 and 3 will be removed from view first, followed by section 2, and
finally section 4. A similar note is provided below for the block layout.

---
setOption(so): [string, string]
    properties: edit
    This flag will edit the option specified by the first string. Current options are:
smpPolyCount - "cage" or "smp" - in smooth mesh preview, determines the poly count display

---
showGrid(sg): boolean
    properties: create, query, edit
    This flag will toggle the display of the grid lines of the HUD layout.

---
visible(vis): boolean
    properties: create, query, edit
    Sets the visibility of the Heads-Up Display on and off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/headsUpDisplay.html 
    """


def headsUpMessage(flaghorizontalOffset: int, flagobject: string, flagselection: boolean, flagtime: float, flaguvTextureEditor: boolean, flagverticalOffset: int, flagviewport: boolean) -> None:
    """Synopsis:
---
---
 headsUpMessage(
[message string]
    , [horizontalOffset=int], [object=string], [selection=boolean], [time=float], [uvTextureEditor=boolean], [verticalOffset=int], [viewport=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

headsUpMessage is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.headsUpMessage( 'Ouch!' )
cmds.headsUpMessage( 'This is Circle 1', object='circle1' )
cmds.headsUpMessage( 'These objects are selected', selection=True )
cmds.headsUpMessage( 'Text appears for minimum of 5 seconds.', time=5.0 )
cmds.headsUpMessage( 'Text appears 0 pixels above point.', verticalOffset=20 )
cmds.headsUpMessage( 'Text appears 20 pixels to the left of the point.', horizontalOffset=-20 )

---


Flags:
---


---
horizontalOffset(ho): int
    properties: create
    If this flag is specified, the message will appear
the specified distance (in pixels) to the right of
the point.  Otherwise, a default horizontal offset of 0
pixels is used.

---
object(o): string
    properties: create
    If an object is specified, then the message is drawn
just above the object's bounding-box centre point.
If this flag is not specified, or the object is not
found, then the message is centred in the current view.

---
selection(s): boolean
    properties: create
    If this flag is specified, the message will be
centred among the currently selected objects.  This
flag does nothing if the object flag is also specified.

---
time(t): float
    properties: create
    If this flag is specified, the message will be
displayed for a minimum of the given amount of time
(in seconds).  Otherwise a default time of 1.0 seconds
is used.

---
uvTextureEditor(uve): boolean
    properties: create
    Should the HUD be shown in the UV Texture Editor?

---
verticalOffset(vo): int
    properties: create
    If this flag is specified, the message will appear
the specified distance (in pixels) above the point.
Otherwise, a default vertical offset of 0 pixels is used.

---
viewport(vp): boolean
    properties: create
    Should the HUD be shown in the viewport?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/headsUpMessage.html 
    """


def help(flagdocumentation: boolean, flaglanguage: string, flaglist: boolean, flagpopupDisplayTime: uint, flagpopupMode: boolean, flagpopupPauseTime: uint, flagpopupSimpleMode: boolean, flagrolloverMode: boolean, flagsyntaxOnly: boolean) -> None:
    """Synopsis:
---
---
 help(
[string]
    , [documentation=boolean], [language=string], [list=boolean], [popupDisplayTime=uint], [popupMode=boolean], [popupPauseTime=uint], [popupSimpleMode=boolean], [rolloverMode=boolean], [syntaxOnly=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

help is undoable, queryable, and NOT editable.
Pattern follows the following syntax:


*            matches any string
?            matches any character
[agj]        matches a, g or j
[^0-9]       matches anything but a digit
x+           matches any number of subsequent x
a{3}         matches aaa
a{3,}        matches aaa, aaaa, ...
a{3,5}       matches aaa, aaaa, or aaaaa
(ab)(CD)\2\1 matches abCDCDab (\1 to \9 available)





Example:
---
import maya.cmds as cmds

List all commands starting with a, b or c
cmds.help( '[a-c]*', list=True )

List all commands without vowels!
cmds.help( '[^aeiou]+', list=True )

Print a message explaining how to use help
cmds.help()

Bring up the main on-line help index
cmds.help( doc=True)

Bring up the Python version of command documentation for the polySphere
command
cmds.help( language='python', doc='polySphere' )

Bring up the on-line help for the disable command.
cmds.help( 'disable', doc=True )

---


Flags:
---


---
documentation(doc): boolean
    properties: create
    Use a browser to show the documentation associated with the single
command name given. A pattern cannot be used with this flag. If no
command name is specified, then this flag will go to the main
documentation index.

---
language(lng): string
    properties: create
    Show the help for this command in the specified language.
Valid values are "mel" and "python".
The default is Mel.
Used with the doc flag.

---
list(l): boolean
    properties: create
    List all the commands whose names match the regular expression. Pass the
regular expression as the first argument to the command specified.

---
popupDisplayTime(pdt): uint
    properties: create, query
    Set the amount of time, in seconds, that the popup help
will be displayed.  The default is 4 seconds.
This flag is mutually exclusive of the list and doc flags.

---
popupMode(pm): boolean
    properties: create, query
    Turn on or off popup help mode.  This flag is mutually exclusive
of the list and doc flags.

---
popupPauseTime(ppt): uint
    properties: create, query
    Set the amount of time, in milliseconds, before the popup help
will be displayed. The default is 800 milliseconds.
This flag is mutually exclusive of the list and doc flags.

---
popupSimpleMode(psm): boolean
    properties: create, query
    Turn on or off simple popup help mode. If set, ToolClips will display
only name and keyboard shortcut.

---
rolloverMode(rm): boolean
    properties: create, query
    Turn on or off rollover help mode.  This flag is mutually exclusive
with the list and doc flags.

---
syntaxOnly(so): boolean
    properties: create
    When no other flag is specified, return only the syntax part of the
quick help.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/help.html 
    """


def helpLine(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 helpLine(
[name]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

helpLine is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Create a window with a menu bar, some buttons and a help
   line.  Attach some annontations to the UI so that they
   appear in the help line.
---

window = cmds.window( menuBar=True )
cmds.menu( label='File' )
cmds.menuItem( label='New', annotation='Help for New' )
cmds.menuItem( label='Open', annotation='Help for Open' )
cmds.menuItem( label='Close', annotation='Help for Close' )

form = cmds.formLayout()
column = cmds.rowLayout(numberOfColumns=4,
                        columnWidth4=(32, 32, 32, 32),
                        columnAttach4=('both', 'both', 'both', 'both'))
cmds.button( label='A', height=32, annotation='Help for A' )
cmds.button( label='B', height=32, annotation='Help for B' )
cmds.button( label='C', height=32, annotation='Help for C' )
cmds.button( label='D', height=32, annotation='Help for D' )
cmds.setParent( '..' )

frame = cmds.frameLayout( labelVisible=False )
cmds.helpLine()
cmds.formLayout( form, edit=True,
                 attachForm=((column, 'top', 0), (column, 'left', 0),
                             (column, 'right', 0), (frame, 'left', 0),
                             (frame, 'bottom', 0), (frame, 'right', 0)),
                 attachNone=((column, 'bottom'), (frame, 'top')) )
cmds.showWindow( window )

---
Return:
---


    string: Full path name of control.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/helpLine.html 
    """


def hide(flagallObjects: boolean, flagclearLastHidden: boolean, flagclearSelection: boolean, flaginvertComponents: boolean, flagreturnHidden: boolean, flagtestVisibility: boolean) -> None:
    """Synopsis:
---
---
 hide(
[objects]
    , [allObjects=boolean], [clearLastHidden=boolean], [clearSelection=boolean], [invertComponents=boolean], [returnHidden=boolean], [testVisibility=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hide is undoable, NOT queryable, and NOT editable.hide



Example:
---
import maya.cmds as cmds

cmds.hide( all=True )
cmds.hide( cmds.ls( type='nurbsSurface' ) )

---


Flags:
---


---
allObjects(all): boolean
    properties: create
    Make everything invisible (top level objects).

---
clearLastHidden(clh): boolean
    properties: create
    Clear the last hidden list.

---
clearSelection(cs): boolean
    properties: create
    Clear selection after the operation.

---
invertComponents(ic): boolean
    properties: create
    Hide components that are not specified.

---
returnHidden(rh): boolean
    properties: create
    Hide objects, but also return list of hidden objects.

---
testVisibility(tv): boolean
    properties: create
    Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hide.html 
    """


def hikGlobals(flagreleaseAllPinning: boolean) -> boolean:
    """Synopsis:
---
---
 hikGlobals([releaseAllPinning=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hikGlobals is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Enable the global release all pinning HIK flag
cmds.hikGlobals( rap=1 )

---
Return:
---


    boolean: Giving the state of the option

Flags:
---


---
releaseAllPinning(rap): boolean
    properties: query, edit
    Sets the global release all pinning hik flag. When this flag is set,
all pinning states are ignored.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hikGlobals.html 
    """


def hilite(flagreplace: boolean, flagtoggle: boolean, flagunHilite: boolean) -> None:
    """Synopsis:
---
---
 hilite(
[objects]
    , [replace=boolean], [toggle=boolean], [unHilite=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hilite is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

   Create a few objects.
---

sphere = cmds.sphere()
cmds.move( 0, 0, 3, relative=True )
cone = cmds.cone()
cmds.move( 0, 0, -3, relative=True )
cylinder = cmds.cylinder()

   Select the sphere.
---

cmds.select( sphere, replace=True )

   Add the cone and cylinder to the hilite list.
---

cmds.hilite( cone[0], cylinder[0] )

   Toggle the hilite state of the cylinder.
---

cmds.hilite( cylinder[0], toggle=True )

   Replace the hilite list with the current selected objects.
---

cmds.hilite( replace=True )

---


Flags:
---


---
replace(r): boolean
    properties: create
    Hilite the specified objects.  Any objects previously
hilited will no longer be hilited.

---
toggle(tgl): boolean
    properties: create
    Toggle the hilite state of the specified objects.

---
unHilite(u): boolean
    properties: create
    Remove the specified objects from the hilite list.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hilite.html 
    """


def hitTest() -> list[string]:
    """Synopsis:
---
---
 hitTest(stringintint)  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hitTest is NOT undoable, NOT queryable, and NOT editable.hitTest


Example:
---
import maya.cmds as cmds

   Let's say that you have the name of a model editor that was
   created elsewhere.
---

editor = "MyModelEditor"

   Here's your drop callback:
---

def myModelEditorDropCallback( dragControl,
                                                           dropControl,
                                                           msgs,
                                                           x,
                                                           y,
                                                           type ):
        ---
        Inside the callback we can hit-test the (x,y) drop-point
        ---
        against the control. This will return a list of DAG objects
        ---
        underneath the drop-point.
        ---

        objects = cmds.hitTest( dropControl, x, y )
        if len( objects ):
                ---
        The hit-test returned something. You can now do something
                ---
        with these objects.
                pass

---

---
        Attach a drop callback to this model editor.
---

try:
        control = cmds.editor( editor ,query=True, control=True )
        if cmds.control( control, exists=True ):
                cmds.control( control, edit=True, dropCallback=myModelEditorDropCallback )
except RuntimeError:
        pass

---
Return:
---


    list[string]: items underneath the hit-point

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hitTest.html 
    """


def hotBox(flagPaneOnlyMenus: boolean, flagPaneToggleMenus: boolean, flaganimationOnlyMenus: boolean, flaganimationToggleMenus: boolean, flagclothOnlyMenus: boolean, flagclothToggleMenus: boolean, flagcommonOnlyMenus: boolean, flagcommonToggleMenus: boolean, flagcustomMenuSetsToggleMenus: boolean, flagdisplayCenterOnly: boolean, flagdisplayHotbox: boolean, flagdisplayStyle: boolean, flagdisplayZonesOnly: boolean, flagdynamicsOnlyMenus: boolean, flagdynamicsToggleMenus: boolean, flagliveOnlyMenus: boolean, flagliveToggleMenus: boolean, flagmenuSetOnly: string, flagmenuSetToggle: tuple[string, boolean], flagmodelingOnlyMenus: boolean, flagmodelingToggleMenus: boolean, flagnoClickCommand: script, flagnoClickDelay: float, flagnoClickPosition: boolean, flagnoKeyPress: boolean, flagpolygonsOnlyMenus: boolean, flagpolygonsToggleMenus: boolean, flagposition: tuple[uint, uint], flagrelease: boolean, flagrenderingOnlyMenus: boolean, flagrenderingToggleMenus: boolean, flagriggingOnlyMenus: boolean, flagriggingToggleMenus: boolean, flagrmbPopups: boolean, flagshowAllToggleMenus: boolean, flagsurfacesOnlyMenus: boolean, flagsurfacesToggleMenus: boolean, flagtransparenyLevel: int, flagupdateMenus: boolean) -> None:
    """Synopsis:
---
---
 hotBox([PaneOnlyMenus=boolean], [PaneToggleMenus=boolean], [animationOnlyMenus=boolean], [animationToggleMenus=boolean], [clothOnlyMenus=boolean], [clothToggleMenus=boolean], [commonOnlyMenus=boolean], [commonToggleMenus=boolean], [customMenuSetsToggleMenus=boolean], [displayCenterOnly=boolean], [displayHotbox=boolean], [displayStyle=boolean], [displayZonesOnly=boolean], [dynamicsOnlyMenus=boolean], [dynamicsToggleMenus=boolean], [liveOnlyMenus=boolean], [liveToggleMenus=boolean], [menuSetOnly=string], [menuSetToggle=[string, boolean]], [modelingOnlyMenus=boolean], [modelingToggleMenus=boolean], [noClickCommand=script], [noClickDelay=float], [noClickPosition=boolean], [noKeyPress=boolean], [polygonsOnlyMenus=boolean], [polygonsToggleMenus=boolean], [position=[uint, uint]], [release=boolean], [renderingOnlyMenus=boolean], [renderingToggleMenus=boolean], [riggingOnlyMenus=boolean], [riggingToggleMenus=boolean], [rmbPopups=boolean], [showAllToggleMenus=boolean], [surfacesOnlyMenus=boolean], [surfacesToggleMenus=boolean], [transparenyLevel=int], [updateMenus=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hotBox is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Bind the hotBox to the spacebar.
---

cmds.nameCommand( 'NameComPop_hotBox', annotation='Pop Hotbox', command='hotBox' )
cmds.hotkey( k=' ', name='NameComPop_hotBox' )

Give the hotBox a 'noClickCommand' which displays the screen position at
which the hotBox was requested. Note that 'showPos' function is passed
to the 'noClickCommand' flag as a function, not as a string. This is necessary
to allow Maya to pass the coordinates to it properly.
---

def showPos(x, y):
    print("hotBox requested at (%d, %d)" % (x, y))

cmds.hotBox(noClickCommand=showPos, noClickPosition=True)

---


Flags:
---


---
PaneOnlyMenus(po): boolean
    properties: create
    Sets a row of menus to be the only visible row.

---
PaneToggleMenus(pt): boolean
    properties: create, query
    Sets the visibilty of a row of menus to on or off.

---
displayCenterOnly(dco): boolean
    properties: create
    Three different display styles are defined for the hotBox. It can
be fully displayed (dh), display only the marking menu zones
(dzo) or no display (dco) which means that the entire
screen can be used to access the marking menus defined in the center zone.

---
displayStyle(ds): boolean
    properties: query
    Returns a string that identifies the flag used to set the current
display style. The results can be dh, dzo, or
dco, depending on  which style the hotBox is using at the moment.

---
menuSetOnly(mso): string
    properties: create
    Show only the named menu set

---
menuSetToggle(mst): [string, boolean]
    properties: create
    Update the given menu sets with the paired toggle value

---
noClickCommand(ncc): script
    properties: create
    The command to be executed if the hotBox is engaged
and then disengaged within noClickDelay time units.

---
noClickDelay(ncd): float
    properties: create
    If the hotBox is engaged and then disengaged within
this time interval, then the noClickCommand is executed.
The time interval is in seconds.  The default value is 0.1.

---
noClickPosition(ncp): boolean
    properties: create
    If a -noClickCommand has been specified then this flag will cause the X and Y
screen coordinates of the mouse pointer to be appended as arguments to that command.
The coordinates used are those of the pointer at the time when the hotbox command was
initiated.

---
noKeyPress(nkp): boolean
    properties: create, query
    Normally the hotbox is popped by a pressing a keyboard key. Use the
nkp flag to pop the hotbox from a device other than the keyboard
(still use the rl flag to unpop the hotbox).

---
position(pos): [uint, uint]
    properties: create
    Specify the screen position the hotbox should be centered at next time
it is displayed.  The default is the cursor position.

---
release(rl): boolean
    properties: create, query
    Action to be called on the release of the key which invoked the hotbox

---
rmbPopups(rmb): boolean
    properties: create, query
    Enables/Disables a popup menu of the current function set.
This popup menu appear when the right mouse button is pressed
in the center zone of the hotbox.

---
showAllToggleMenus(a): boolean
    properties: create, query
    Sets the visibility of all menus to on or off.
When queried, will only return true if all menu rows are visible.

---
transparenyLevel(tr): int
    properties: create, query
    The percentage of transparency, from 0 to 100.
Currently, only the values 0, 25, 50, 75 and 100 are
supported.  Any other values will be rounded off
to the nearest supported value.

---
updateMenus(um): boolean
    properties: create
    Reloads the hotBox menus from the main menubar.
This flag is used when the menus in the main menubar are modified,
and the hotBox menus need to be refreshed.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hotBox.html 
    """


def hotkey(flagaltModifier: boolean, flagautoSave: boolean, flagcommandModifier: boolean, flagctrlModifier: boolean, flagctxClient: string, flagdragPress: boolean, flagfactorySettings: boolean, flagisModifier: boolean, flagkeyShortcut: string, flagname: string, flagpressCommandRepeat: boolean, flagreleaseCommandRepeat: boolean, flagreleaseName: string, flagshiftModifier: boolean, flagsourceUserHotkeys: boolean) -> None:
    """Synopsis:
---
---
 hotkey([altModifier=boolean], [autoSave=boolean], [commandModifier=boolean], [ctrlModifier=boolean], [ctxClient=string], [dragPress=boolean], [factorySettings=boolean], [isModifier=boolean], [keyShortcut=string], [name=string], [pressCommandRepeat=boolean], [releaseCommandRepeat=boolean], [releaseName=string], [shiftModifier=boolean], [sourceUserHotkeys=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hotkey is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Here's an example of how to create a namedCommand
object and then map it to a key.
---

cmds.nameCommand( 'circleToolNamedCommand', annotation='Select Circle Tool', command='setToolTo circleContext')
cmds.hotkey( k='F5', alt=True, name='circleToolNamedCommand' )


Here are more examples of how to use the hotkey command.
---

cmds.hotkey( k='d', name='Delete_Command' )
cmds.hotkey( k='d', name='' ) unsets the above command

cmds.hotkey( k='d', name='Delete_Command' )
cmds.hotkey( k='d', releaseName='After_Delete_Command' )
cmds.hotkey( k='d', name='' ) ---
only unsets the key press name
cmds.hotkey( k='d', releaseName='' ) ---
only unsets the key release name
cmds.hotkey( k='d', n='', rn='' ) ---
unsets both the key press and release name

   Determine if a command is attached to either the press or release
   of the "z" hotkey.
---

cmds.hotkey( 'z', query=True )

   Likewise, for the modified variations of the "z" key.
---

cmds.hotkey( 'z', query=True, alt=True )
cmds.hotkey( 'z', query=True, ctl=True )
cmds.hotkey( 'z', query=True, alt=True, ctl=True )

   Determine the press command attached to the "z" key.
---

cmds.hotkey( 'z', query=True, name=True )

   To query the "-" hotkey use the string "Dash" instead.
---

cmds.hotkey( 'Dash', query=True )

---


Flags:
---


---
autoSave(autoSave): boolean
    properties: create
    If set to true then the hotkeys will always be saved when
you quit.  If false then the hotkeys are not saved unless
"savePrefs -hotkeys" is used.

---
commandModifier(cmd): boolean
    properties: create
    The Command key must be pressed to get the hotkey.
This is only available on systems which have a separate
command key.
Note that if menu item accelerator keys are being used
(menuItem -ke/keyEquivalent), then the accelerator key
settings override the hotkey settings.

---
ctrlModifier(ctl): boolean
    properties: create, query
    The Ctrl key must be pressed to get the hotkey.
Note that if menu item accelerator keys are being used
(menuItem -ke/keyEquivalent), then the accelerator key
settings override the hotkey settings.

---
ctxClient(cc): string
    properties: create, query
    Specifies the hotkey context. It is used together with the other flags to modify or query
the hotkey for a certain hotkey context. If it is not specified, the global hotkey context will be taken into
account. Check hotkeyCtx command to see how the hotkeys work with the hotkey contexts.

---
dragPress(dp): boolean
    properties: create
    Specify true and the command may be executed during
manipulator dragging, if the tool context also allows
this. This flag is false by default.

---
factorySettings(fs): boolean
    properties: create
    Resets the hotkeys back to the initial defaults.

---
isModifier(mod): boolean
    properties: create
    This flag is obsolete and should no longer be used.

---
keyShortcut(k): string
    properties: create
    Specify what key is being set. The key must be either a single
ascii character (capital and lowercase can be set independently)
or one of the keyword
strings for the special keyboard characters.

The valid keywords are:
Up, Down, Right, Left,
Home, End, Page_Up, Page_Down, Insert
Return, Space
F1 to F12
Tab (Will only work when modifiers are specified)
Delete, Backspace (Will only work when modifiers are specified)

---
name(n): string
    properties: create, query
    The name of the namedCommand object that will be executed when the key is pressed.

---
pressCommandRepeat(pcr): boolean
    properties: create
    Specify true and the command may be repeated by executing
the command repeatLast. This flag is false by default.

---
releaseCommandRepeat(rcr): boolean
    properties: create
    Specify true and the command may be repeated by executing
the command repeatLast. This flag is false by default.

---
releaseName(rn): string
    properties: create, query
    The name of the namedCommand object that will be executed when the key is released.

---
shiftModifier(sht): boolean
    properties: create, query
    The Shift key must be pressed to get the hotkey.

---
sourceUserHotkeys(suh): boolean
    properties: create
    This flag is obsolete. Please use import flag from hotkeySet command
to import the user hotkeys.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hotkey.html 
    """


def hotkeyCheck(flagaltModifier: boolean, flagcommandModifier: boolean, flagctrlModifier: boolean, flagisRepeatable: boolean, flagkeyString: string, flagkeyUp: boolean, flagoptionModifier: boolean) -> string:
    """Synopsis:
---
---
 hotkeyCheck([altModifier=boolean], [commandModifier=boolean], [ctrlModifier=boolean], [isRepeatable=boolean], [keyString=string], [keyUp=boolean], [optionModifier=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hotkeyCheck is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

   Create a window in which you can type a hotkey character
   and determine via the 'hotkeyCheck' command the annotation
   of the command attached.
---

window = cmds.window( title='hotkeyCheck Example' )
cmds.columnLayout( adjustableColumn=True )

   A few instructions in a scrollField for the user.
---

instructions = "Enter a single character in the field below.  \
Then press the 'Query' button to determine the annotation of the command attached to that hotkey."

cmds.scrollField( text=instructions, editable=False, height=120, wordWrap=True )
textFieldGrp = cmds.textFieldGrp( label="Enter a single hotkey character", text='a', columnWidth2=(200, 50) )

   Create a couple controls for specifying modifier keys and the
   key press/release information.
---

checkBoxGrp = cmds.checkBoxGrp( label="Modifiers",
                                                        numberOfCheckBoxes=2,
                                                        labelArray2=('Ctrl', 'Alt'),
                                                        columnWidth3=(100, 75, 75))
radioButtonGrp = cmds.radioButtonGrp( label="Action",
                                                        numberOfRadioButtons=2,
                                                        select=1,
                                                        labelArray2=('Press', 'Release'),
                                                        columnWidth3=(100, 75, 75))

   Create a scroll field for printing the results.
---

scrollField = cmds.scrollField(editable=False, height=120, wordWrap=True)

   Create a button for querying the hotkey.
---

cmds.button( label='Query', command=('ExampleHotkeyCheck("' + textFieldGrp + '","' + checkBoxGrp + '","' + radioButtonGrp + '","' + scrollField + '")'))
cmds.showWindow( window )

   This procedure uses the 'hotkeyCheck' command to determine the
   annotation of the command attached to a hotkey.
---

def ExampleHotkeyCheck( textFieldGrp, checkBoxGrp, radioButtonGrp, scrollField):
           Get the hotkey character, modifier state and key press/release
           information from the window.
        ---

        key = cmds.textFieldGrp(textFieldGrp, query=True, text=True)
        ctrl = cmds.checkBoxGrp(checkBoxGrp, query=True, value1=True)
        alt = cmds.checkBoxGrp(checkBoxGrp, query=True, value2=True)
        press = cmds.radioButtonGrp(radioButtonGrp, query=True, select=True)

           Get the hotkey mapping taking into consideration key up or down
           and the state of the modifier keys.
        ---

        if 1 == press:
                if not ctrl and not alt:
                        mapping = cmds.hotkeyCheck(keyString=key)
                        result = key + '-Press'
                elif ctrl and not alt:
                        mapping = cmds.hotkeyCheck(keyString=key, ctl=True)
                        result = 'Ctrl-' + key + '-Press'
                elif not ctrl and alt:
                        mapping = cmds.hotkeyCheck(keyString=key, alt=True)
                        result = 'Alt-' + key + '-Press'
                elif ctrl and alt:
                        mapping = cmds.hotkeyCheck(keyString=key, ctl=True, alt=True)
                        result = 'Ctrl-Alt-' + key + '-Press'
        else:
                if not ctrl and not alt:
                        mapping = cmds.hotkeyCheck(keyString=key, keyUp=True)
                        result = key + '-Release'
                elif ctrl and not alt:
                        mapping = cmds.hotkeyCheck(keyString=key, ctl=True, keyUp=True)
                        result = 'Ctrl-' + key + '-Release'
                elif not ctrl and alt:
                        mapping = cmds.hotkeyCheck(keyString=key, alt=True, keyUp=True)
                        result = 'Alt-' + key + '-Release'
                elif ctrl and alt:
                        mapping = cmds.hotkeyCheck(keyString=key, ctl=True, alt=True, keyUp=True)
                        result = 'Ctrl-Alt-' + key + '-Release'


           Print the results in the example window.
        ---

        if mapping == "": mapping = 'Nothing'
        cmds.scrollField( scrollField, edit=True, text=(result + ' is mapped to:\n\n' + mapping ) )

---
Return:
---


    string: Contains all clients name, each followed by the annotation of the corresponding nameCommand object, or
an empty string.

Flags:
---


---
altModifier(alt): boolean
    properties: create
    Specifies if the Alt key is pressed.

---
commandModifier(cmd): boolean
    properties: create
    Specifies if the command key is pressed.

---
ctrlModifier(ctl): boolean
    properties: create
    Specifies if the Ctrl key is pressed.

---
isRepeatable(ir): boolean
    properties: create
    Specify this flag if the hotkey is repeatable.

---
keyString(k): string
    properties: create
    The key to check.

---
keyUp(kup): boolean
    properties: create
    Specifies if the hotkey is on keyup or keydown
(i.e. Release or Press).

---
optionModifier(opt): boolean
    properties: create
    Specifies if the option key is pressed.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hotkeyCheck.html 
    """


def hotkeyCtx(flagaddClient: string, flagclientArray: boolean, flagcurrentClient: string, flaginsertTypeAt: tuple[string, string], flagremoveAllClients: boolean, flagremoveClient: string, flagremoveType: string, flagtype: string, flagtypeArray: boolean, flagtypeExists: string) -> None:
    """Synopsis:
---
---
 hotkeyCtx([addClient=string], [clientArray=boolean], [currentClient=string], [insertTypeAt=[string, string]], [removeAllClients=boolean], [removeClient=string], [removeType=string], [type=string], [typeArray=boolean], [typeExists=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hotkeyCtx is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Here are some examples of how to use hotkeyCtx command.
---


Create a new context type
cmds.hotkeyCtx( insertTypeAt=('Global', 'CustomEditor') )
cmds.hotkeyCtx( ita=('CustomEditor', 'CustomTool') )

Query all existing context types
ctxTypes = cmds.hotkeyCtx( typeArray=True, query=True )
print str(ctxTypes)

Remove an existing context type
cmds.hotkeyCtx( removeType='CustomTool' )

Determine if the given context type exists.
cmds.hotkeyCtx( te='CustomTool', query=True )

Associate the clients to the specific context type.
cmds.hotkeyCtx( t='CustomEditor', ac=['hyperGraphPanel', 'outlinerPanel'] )

Set current context
cmds.hotkeyCtx( t='CustomEditor', cc='hyperGraphPanel' )

Unassign the client from the specific context type.
cmds.hotkeyCtx( t='CustomEditor', rc='outlinerPanel' )

Query all associated clients for the given context type.
cl = cmds.hotkeyCtx( t='CustomEditor', ca=True, query=True )
print str(cl)

Remove all associated clients
cmds.hotkeyCtx( t='CustomEditor', rac=True )

---


Flags:
---


---
addClient(ac): string
    properties: create, multiuse
    Associates a client to the given hotkey context type.
This flag needs to be used with the flag "type" which specifies the context type.

---
clientArray(ca): boolean
    properties: query
    Returns an array of the all context clients associated to the hotkey context type.
This flag needs to be used with the flag "type" which specifies the context type.

---
currentClient(cc): string
    properties: create, query
    Current client for the given hotkey context type.
This flag needs to be used with the flag "type" which specifies the context type.

---
insertTypeAt(ita): [string, string]
    properties: create
    Inserts a new hotkey context type in the front of the given type.
The first argument specifies an existing type. If it's empty,
the new context type will be inserted before "Global" context type.
The second argument specifies the name of new context type.

---
removeAllClients(rac): boolean
    properties: create
    Removes all the clients associated to the hotkey context type.
This flag needs to be used with the flag "type" which specifies the context type.

---
removeClient(rc): string
    properties: create, multiuse
    Removes a client associated to the hotkey context type.
This flag needs to be used with the flag "type" which specifies the context type.

---
removeType(rt): string
    properties: create
    Removes the given hotkey context type.

---
type(t): string
    properties: create, query
    Specifies the context type. It's used together with the other flags such as
"currentClient", "addClient", "removeClient" and so on.

---
typeArray(ta): boolean
    properties: query
    Returns a string array containing the names of all hotkey context types,
ordered by priority.

---
typeExists(te): string
    properties: query
    Returns true|false depending upon whether the specified hotkey context type
exists.
      In query mode, this flag needs a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hotkeyCtx.html 
    """


def hotkeyEditorPanel(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 hotkeyEditorPanel(
[name]
    , [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hotkeyEditorPanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

window = cmds.window( widthHeight=(400, 300) )
cmds.hotkeyEditorPanel()
cmds.showWindow( window )

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hotkeyEditorPanel.html 
    """


def hotkeySet(flagcurrent: boolean, flagdelete: boolean, flagexists: boolean, flagexport: string, flaghotkeySetArray: boolean, flagip: string, flagrename: string, flagsource: string) -> string:
    """Synopsis:
---
---
 hotkeySet(
[name]
    , [current=boolean], [delete=boolean], [exists=boolean], [export=string], [hotkeySetArray=boolean], [ip=string], [rename=string], [source=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hotkeySet is undoable, queryable, and editable.
A new hotkey set is always duplicated from an existing hotkey set. In create mode, users can choose to specify
which hotkey set to duplicate by using the -source flag. A duplicated hotkey set is independent from the source
hotkey set.




Example:
---
import maya.cmds as cmds

Create a new key set and set it as the active key set.
The current active hotkey set is used as its source.
MyNewKeySet = 'MyNewKeySet'
cmds.hotkeySet( MyNewKeySet, current=True )

Query the name of the current key set
cmds.hotkeySet( q=True, current=True )

Create a new hotkey set with a user hotkey set as source
MyNewKeySet2 = 'MyNewKeySet2'
cmds.hotkeySet( MyNewKeySet2, source='MyNewKeySet' )

Delete the created hotkey set.
cmds.hotkeySet( MyNewKeySet, edit=True, delete=True )

Returns all available hotkey sets in Maya
cmds.hotkeySet( q=True, hotkeySetArray=True )

Export a hotkey set
fileName = (cmds.internalVar( userTmpDir=True ) + "exportHotkeySet1.mhk");
cmds.hotkeySet( MyNewKeySet2, e=True, export=fileName);

Import a hotkey set
cmds.hotkeySet( e=True, ip=fileName);

---
Return:
---


    string: The name of the hotkey set.

Flags:
---


---
current(cu): boolean
    properties: create, query, edit
    Sets the hotkey set as the current active hotkey set. In query mode, returns the name of
the current hotkey set.

---
delete(delete): boolean
    properties: edit
    Deletes the hotkey set if it exists. Other flags are ignored.
Returns true|false depending on the delete operation.

---
exists(ex): boolean
    properties: create
    Returns true|false depending upon whether the specified object
exists. Other flags are ignored.

---
export(ep): string
    properties: edit
    Exports a hotkey set. The argument is used to specify a full path of the output file.

---
hotkeySetArray(hsa): boolean
    properties: query
    Returns a string array of all existing hotkey set names.

---
ip(ip): string
    properties: edit
    Imports a hotkey set. The argument is used to specify a full path of the hotkey set file to import.

---
rename(re): string
    properties: edit
    Renames an existing hotkey set. All white spaces will be replaced with '_' during operation.

---
source(src): string
    properties: create
    Specifies the source hotkey set. If flag is not provided, the current active hotkey set is used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hotkeySet.html 
    """


def hudButton(flagallowOverlap: boolean, flagblock: int, flagblockAlignment: string, flagblockSize: string, flagbuttonShape: string, flagbuttonWidth: int, flaglabel: string, flaglabelFontSize: string, flagpadding: int, flagpressCommand: script, flagreleaseCommand: script, flagsection: int, flagvisible: boolean) -> int | string | int | int[2]:
    """Synopsis:
---
---
 hudButton([string], [allowOverlap=boolean], [block=int], [blockAlignment=string], [blockSize=string], [buttonShape=string], [buttonWidth=int], [label=string], [labelFontSize=string], [padding=int], [pressCommand=script], [releaseCommand=script], [section=int], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hudButton is NOT undoable, queryable, and editable.
Although this command provides much of the same functionality as the headsUpDisplay
command, it does not provide headsUpDisplay layout controls such as layoutVisibility,
nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality,
please use the headsUpDisplay command. This command is focused solely around the creation
and management of HUD button controls. Similarly, all operations performed by
this command are limited to HUDs that are button controls.

The only mandatory flags, on creation are the section and block flags.

Like the headsUpDisplay command, upon creation of a HUD button, an ID number
will be assigned to it. This can be used to remove the HUD via the headsUpDisplay
command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay
command can remove HUD objects via their position (section and block),
or their unique name.




Example:
---
import maya.cmds as cmds

Define a "Hello!" counter procedure. This procedure will output
"Hello! [number]"
each time it is run. The number is incremented at the end of each call.
---

gHelloCount = 0

def HUDButtonHello(*args):
  global gHelloCount
  print 'Hello!( %i )' % gHelloCount
  gHelloCount += 1

Now create our button. Only execute on mouse release.
---

cmds.hudButton('HUDHelloButton', s=7, b=5, vis=1, l='Button', bw=80, bsh='roundRectangle', rc=HUDButtonHello )

---
Return:
---


    int: ID number of the Heads-Up Display (HUD).
    string|int|int[2]: HUD name, HUD ID or Section and block value, for respective remove commands.

Flags:
---


---
allowOverlap(ao): boolean
    properties: create, query, edit
    Sets the Heads-Up Display to be visible regardless of overlapping section
widths/limitations (see -s/section flag description for more details).

---
block(b): int
    properties: create, query, edit
    Denotes the individual block that the HUD will reside in, within a
section. Each section is composed of a single column of blocks.
The total number of blocks contained within each section is variable.

The number of blocks that will be visible within each section is
dependent on the size of blocks contained in each section and the
current size of the window. Blocks begin enumerating from 0 and
flexibly increase based on need.

For HUD buttons, the format differs from that of the standard HUD.
The layout using parameters defined by the formatting flags listed
below (eg. justify, padding, buttonWidth) is shown below:

 __________________________________
|     |     |          |     |     |
|  P  |  J  |  Button  |  J  |  P  |
|_____|_____|__________|_____|_____|
P = Sub-block of width, padding
J = Justification of the entire block
Button = Sub-block of width, buttonWidth


Block Positioning

Blocks on the top section begin from the top edge of the main
viewport, while the bottom section begins from the bottom edge.
Blocks are dynamically removed from visibility from the midpoint
of the viewport. So, a relatively large block number will not
draw to the viewport.

Lastly, there can be at most one HUD occupying a block at any time.
Trying to position a HUD in an occupied block will result in an error.
Keep this in mind when positioning the HUD.

---
blockAlignment(ba): string
    properties: create, query, edit
    Specifies the alignment of the block within its respective column. Available
alignments are: "center", "left" and "right". The default alignment is "left".

---
blockSize(bs): string
    properties: create, query, edit
    Sets the height of each block. Available heights are: small, medium and large.
In pixel measurements, each corresponds to a 20, 35 or 50 pixel height, respectively.

---
buttonShape(bsh): string
    properties: create, query, edit
    Specifies the shape of the button. Available button shapes are:
"rectangle" and "roundRectangle". The first will draw a rectangular
button, while the latter is a rectangle with rounded edges.

---
buttonWidth(bw): int
    properties: create, query, edit
    Specifies the width of the button.

---
label(l): string
    properties: create, query, edit
    Text label of the HUD button.

---
labelFontSize(lfs): string
    properties: create, query, edit
    Sets the font size of the label. Available sizes are: small and large.

---
padding(p): int
    properties: create, query, edit
    Specifies the width of both the left and right margins of a block. Default
value is 15 pixels.

---
pressCommand(pc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a mouse click event.

---
releaseCommand(rc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a mouse release event.

---
section(s): int
    properties: create, query, edit
    Defines the section the HUD will appear in. There are 10 sections
divided across the screen. Five columns and two rows make up the
ten element matrix which divide the main viewport. Here is a visual
layout of the sections.

 ________________________
|    |    |    |    |    |
|    |    |    |    |    |
| 0  | 1  | 2  | 3  | 4  |
|    |    |    |    |    |
|____|____|____|____|____|
|    |    |    |    |    |
|    |    |    |    |    |
| 5  | 6  | 7  | 8  | 9  |
|    |    |    |    |    |
|____|____|____|____|____|
Each section is denoted by a number from 0 to 9 as illustrated above.
For example, if the second column of the top row was desired, the
section would be defined as: -sec 1

To prevent HUD objects from displaying over each other and causing a
clutter of letters, each row has a defined visibility precedence,
where each section would have a visibility priority level. Depending
on each priority level, when the screen space begins to shrink to
a point where the section widths of a given row begin to collide, the
HUD automatically compensates for this by removing the sections of
least priority. These sections are made invisible and a warning is
issued to inform the user of the removal. This continues until only
the section of highest priority remains.

For each row, the priorities are defined as follows. Using the top
row as an example: Section 0, has the highest priority, followed
by Section 4, making the outermost sections of highest priority.
Next in the list is Section 2, and lastly Sections 1 and 3 are of
the equal and least priority. This priority structure can be applied
to the bottom row as well. The two outermost sections have the highest
priority, followed by the middle section, and finally the remaining
two sections are of lowest priority.

This means that as the viewport gradually decreases in width
to the point where sections in the top row begin to overlap, sections
1 and 3 will be removed from view first, followed by section 2, and
finally section 4. A similar note is provided below for the block layout.

---
visible(vis): boolean
    properties: create, query, edit
    Sets the visibility of the Heads-Up Display on and off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hudButton.html 
    """


def hudSlider(flagallowOverlap: boolean, flagblock: int, flagblockAlignment: string, flagblockSize: string, flagdecimalPrecision: int, flagdragCommand: script, flaginternalPadding: int, flaglabel: string, flaglabelFontSize: string, flaglabelWidth: int, flagmaxValue: float, flagminValue: float, flagpadding: int, flagpressCommand: script, flagreleaseCommand: script, flagsection: int, flagsliderIncrement: float, flagsliderLength: int, flagtype: string, flagvalue: float, flagvalueAlignment: string, flagvalueFontSize: string, flagvalueWidth: int, flagvisible: boolean) -> int | string | int | int[2]:
    """Synopsis:
---
---
 hudSlider([string], [allowOverlap=boolean], [block=int], [blockAlignment=string], [blockSize=string], [decimalPrecision=int], [dragCommand=script], [internalPadding=int], [label=string], [labelFontSize=string], [labelWidth=int], [maxValue=float], [minValue=float], [padding=int], [pressCommand=script], [releaseCommand=script], [section=int], [sliderIncrement=float], [sliderLength=int], [type=string], [value=float], [valueAlignment=string], [valueFontSize=string], [valueWidth=int], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hudSlider is NOT undoable, queryable, and editable.
Although this command provides much of the same functionality as the headsUpDisplay
command, it does not provide headsUpDisplay layout controls such as layoutVisibility,
nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality,
please use the headsUpDisplay command. This command is focused solely around the creation
and management of HUD sliders. Similarly, all operations performed by this command
are limited to HUDs that are sliders.

The only mandatory flags, on creation are the section and block flags.

Like the headsUpDisplay command, upon creation of a HUD slider, an ID number will be
assigned to it. This can be used to remove the HUD slider via the headsUpDisplay
command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay
command can remove HUD objects via their position (section and block),
or their unique name.




Example:
---
import maya.cmds as cmds

Define a procedure to execute on press/drag/release. This procedure
will explicitly set any selected transforms to a given position along
the X axis based on the value of a given HUD slider.
---


def translateXSlider( HUD ):
        Since undo is not turned off automatically, we must
        do it ourselves. The HUD will fire off many calls to this
        procedure during a drag so we don't want to flood the undo
        queue.
        cmds.undoInfo( swf=False )
        try:
                for object in cmds.ls( sl=True ):
                        if cmds.objectType( object, isType='transform' ):
                           translateX = object + '.tx'
                           value = cmds.hudSlider( HUD, q=True, v=True )
                           cmds.setAttr( translateX, value )
        finally:
                Re-enable the undo queue.
                cmds.undoInfo( swf=True)

Now create our slider HUD
---

cmds.hudSlider( 'HUDTranslateXSlider',
                                section=2,
                                block=5,
                                visible=1,
                                label="TranslateX:",
                                value=0,
                                type="int",
                                minValue=-10,
                                maxValue=10,
                                labelWidth=80,
                                valueWidth=50,
                                sliderLength=100,
                                sliderIncrement=1,
                                pressCommand='translateXSlider( "HUDTranslateXSlider" )',
                                dragCommand='translateXSlider( "HUDTranslateXSlider" )',
                                releaseCommand='translateXSlider( "HUDTranslateXSlider" )')

---
Return:
---


    int: ID number of the Heads-Up Display (HUD).
    string|int|int[2]: HUD name, HUD ID or Section and block value, for respective remove commands.

Flags:
---


---
allowOverlap(ao): boolean
    properties: create, query, edit
    Sets the Heads-Up Display to be visible regardless of overlapping section
widths/limitations (see -s/section flag description for more details).

---
block(b): int
    properties: create, query, edit
    Denotes the individual block that the HUD will reside in, within a
section. Each section is composed of a single column of blocks.
The total number of blocks contained within each section is variable.

The number of blocks that will be visible within each section is
dependent on the size of blocks contained in each section and the
current size of the window. Blocks begin enumerating from 0 and
flexibly increase based on need.

For HUD sliders, the format differs from that of the standard HUD.
The layout using parameters defined by the formatting flags listed
below (eg. justify, padding, labelWidth, valueWidth) is shown below:

 __________________________________________________________________
|     |     |        |            |      |             |     |     |
|  P  |  J  |   LW   |   Slider   |  IP  | SliderValue |  J  |  P  |
|_____|_____|________|____________|______|_____________|_____|_____|
P = Sub-block of width, padding
J = Justification of the entire block
LW = Sub-block of width, labelWidth
Slider = Length of the slider
SliderValue = Sub-block of width, valueWidth
IP = Internal padding


Block Positioning

Blocks on the top section begin from the top edge of the main
viewport, while the bottom section begins from the bottom edge.
Blocks are dynamically removed from visibility from the midpoint
of the viewport. So, a relatively large block number will not
draw to the viewport.

Lastly, there can be at most one HUD occupying a block at any time.
Trying to position a HUD in an occupied block will result in an error.
Keep this in mind when positioning the HUD.

---
blockAlignment(ba): string
    properties: create, query, edit
    Specifies the alignment of the block within its respective column. Available
alignments are: "center", "left" and "right". The default alignment is "left".

---
blockSize(bs): string
    properties: create, query, edit
    Sets the height of each block. Available heights are: small, medium and large.
In pixel measurements, each corresponds to a 20, 35 or 50 pixel height, respectively.

---
decimalPrecision(dp): int
    properties: create, query, edit
    Sets the decimal precision of any floating point value returned by the command. The valid
range of precision values are 1 to 8.

---
dragCommand(dc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a mouse drag event.

---
internalPadding(ip): int
    properties: create, query, edit
    Specifies the amount of padding between the internal elements of the HUD. For the
hudSlider, this represents the padding between the slider bar and the slider
value. The default padding is 10.

---
label(l): string
    properties: create, query, edit
    Text label of the HUD.

---
labelFontSize(lfs): string
    properties: create, query, edit
    Sets the font size of the label. Available sizes are: small and large.

---
labelWidth(lw): int
    properties: create, query, edit
    Specifies the pixel width of the virtual "textbox" which will hold the label. The
contents of this "textbox" will be left justified. If the width of the actual label
exceeds the width of the "textbox," the label will be truncated to fit within the
dimensions of the "textbox." (To see a layout of a block, see the description
of the -block flag.)

---
maxValue(max): float
    properties: create, query, edit
    Specify the maximum value of the slider.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
minValue(min): float
    properties: create, query, edit
    Specify the minimum value of the slider.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
padding(p): int
    properties: create, query, edit
    Specifies the width of both the left and right margins of a block. Default
value is 15 pixels.

---
pressCommand(pc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a mouse click event.

---
releaseCommand(rc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a mouse release event.

---
section(s): int
    properties: create, query, edit
    Defines the section the HUD will appear in. There are 10 sections
divided across the screen. Five columns and two rows make up the
ten element matrix which divide the main viewport. Here is a visual
layout of the sections.

 ________________________
|    |    |    |    |    |
|    |    |    |    |    |
| 0  | 1  | 2  | 3  | 4  |
|    |    |    |    |    |
|____|____|____|____|____|
|    |    |    |    |    |
|    |    |    |    |    |
| 5  | 6  | 7  | 8  | 9  |
|    |    |    |    |    |
|____|____|____|____|____|
Each section is denoted by a number from 0 to 9 as illustrated above.
For example, if the second column of the top row was desired, the
section would be defined as: -sec 1

To prevent HUD objects from displaying over each other and causing a
clutter of letters, each row has a defined visibility precedence,
where each section would have a visibility priority level. Depending
on each priority level, when the screen space begins to shrink to
a point where the section widths of a given row begin to collide, the
HUD automatically compensates for this by removing the sections of
least priority. These sections are made invisible and a warning is
issued to inform the user of the removal. This continues until only
the section of highest priority remains.

For each row, the priorities are defined as follows. Using the top
row as an example: Section 0, has the highest priority, followed
by Section 4, making the outermost sections of highest priority.
Next in the list is Section 2, and lastly Sections 1 and 3 are of
the equal and least priority. This priority structure can be applied
to the bottom row as well. The two outermost sections have the highest
priority, followed by the middle section, and finally the remaining
two sections are of lowest priority.

This means that as the viewport gradually decreases in width
to the point where sections in the top row begin to overlap, sections
1 and 3 will be removed from view first, followed by section 2, and
finally section 4. A similar note is provided below for the block layout.

---
sliderIncrement(si): float
    properties: create, query, edit
    Specify the number of increments along the slider. If not specified or set to 0 or less,
the slider will be linearly even and continuous from minValue to maxValue.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
sliderLength(sl): int
    properties: create, query, edit
    Specifies the length of the slider in pixels.

---
type(t): string
    properties: create, query, edit
    Specify the numeric type of the HUD. Available types are:
"float" and "int".

---
value(v): float
    properties: create, query, edit
    Set/Return the slider value if the HUD is a valid HUD slider.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
valueAlignment(va): string
    properties: create, query, edit
    Specifies the alignment of the data blocks and the data text, within a HUD block.
Available alignments are: "left" and "right". The default alignment is "left".

---
valueFontSize(vfs): string
    properties: create, query, edit
    Sets the font size of the slider value. Available sizes are: small and large.

---
valueWidth(vw): int
    properties: create, query, edit
    Specifies the pixel width of the virtual "textbox" which will hold the slider value.
(To see a layout of a block, see the description of the -block flag.)

---
visible(vis): boolean
    properties: create, query, edit
    Sets the visibility of the Heads-Up Display on and off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hudSlider.html 
    """


def hudSliderButton(flagallowOverlap: boolean, flagblock: int, flagblockAlignment: string, flagblockSize: string, flagbuttonLabel: string, flagbuttonLabelFontSize: string, flagbuttonPressCommand: script, flagbuttonReleaseCommand: script, flagbuttonShape: string, flagbuttonWidth: int, flagdecimalPrecision: int, flaginternalPadding: int, flagmaxValue: float, flagminValue: float, flagpadding: int, flagsection: int, flagsliderDragCommand: script, flagsliderIncrement: float, flagsliderLabel: string, flagsliderLabelFontSize: string, flagsliderLabelWidth: int, flagsliderLength: int, flagsliderPressCommand: script, flagsliderReleaseCommand: script, flagtype: string, flagvalue: float, flagvalueAlignment: string, flagvalueFontSize: string, flagvalueWidth: int, flagvisible: boolean) -> int | string | int | int[2]:
    """Synopsis:
---
---
 hudSliderButton([string], [allowOverlap=boolean], [block=int], [blockAlignment=string], [blockSize=string], [buttonLabel=string], [buttonLabelFontSize=string], [buttonPressCommand=script], [buttonReleaseCommand=script], [buttonShape=string], [buttonWidth=int], [decimalPrecision=int], [internalPadding=int], [maxValue=float], [minValue=float], [padding=int], [section=int], [sliderDragCommand=script], [sliderIncrement=float], [sliderLabel=string], [sliderLabelFontSize=string], [sliderLabelWidth=int], [sliderLength=int], [sliderPressCommand=script], [sliderReleaseCommand=script], [type=string], [value=float], [valueAlignment=string], [valueFontSize=string], [valueWidth=int], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hudSliderButton is NOT undoable, queryable, and editable.
Although this command provides much of the same functionality as the headsUpDisplay
command, it does not provide headsUpDisplay layout controls such as layoutVisibility,
nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality,
please use the headsUpDisplay command. This command is focused solely around the creation
and management of HUD slider button controls. Similarly, all operations performed by
this command are limited to HUDs that are slider button controls.

The only mandatory flags, on creation are the section and block flags.

Like the headsUpDisplay command, upon creation of a HUD slider button, an ID number
will be assigned to it. This can be used to remove the HUD slider via the headsUpDisplay
command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay
command can remove HUD objects via their position (section and block),
or their unique name.




Example:
---
import maya.cmds as cmds

Define a procedure to execute on press/drag/release. This procedure
will explicitly set any selected transforms to a given position along
the X axis based on the value of a given HUD slider.
---

def translateXSliderButton( HUD ):
        cmds.undoInfo( swf=True )
        selList = cmds.ls( sl=True )
        for object in selList:
                if cmds.objectType( object, isType='transform' ):
                        cmds.setAttr( object+".tx", cmds.hudSliderButton( HUD, query=True, v=True ) )

Create our slider button.  Use lambda to create an "anonymous" function that invokes the
callback with the desired button name argument.
---

cmds.hudSliderButton( 'HUDTranslateXSliderButton', s=5, b=5, vis=True, sl='Slider:', value=0, type='int', min=-10, max=10, slw=50, vw=50, sln=100, si=1, bl='Button', bw=60, bsh='rectangle', brc=lambda : translateXSliderButton( 'HUDTranslateXSliderButton' ))

---
Return:
---


    int: ID number of the Heads-Up Display (HUD).
    string|int|int[2]: HUD name, HUD ID or Section and block value, for respective remove commands.

Flags:
---


---
allowOverlap(ao): boolean
    properties: create, query, edit
    Sets the Heads-Up Display to be visible regardless of overlapping section
widths/limitations (see -s/section flag description for more details).

---
block(b): int
    properties: create, query, edit
    Denotes the individual block that the HUD will reside in, within a
section. Each section is composed of a single column of blocks.
The total number of blocks contained within each section is variable.

The number of blocks that will be visible within each section is
dependent on the size of blocks contained in each section and the
current size of the window. Blocks begin enumerating from 0 and
flexibly increase based on need.

For HUD sliders, the format differs from that of the standard HUD.
The layout using parameters defined by the formatting flags listed
below (eg. justify, padding, labelWidth, valueWidth) is shown below:

__________________________________________________________________________
|     |     |      |           |      |       |      |        |     |     |
|  P  |  J  |  LW  |  Slider   |  IP  | Value |  IP  | Button |  J  |  P  |
|_____|_____|______|___________|______|_______|______|________|_____|_____|
P = Sub-block of width, padding
J = Justification of the entire block
LW = Sub-block of width, labelWidth
Slider = Length of the slider
SliderValue = Sub-block of width, valueWidth
Button = Sub-block of width, buttonWidth
IP = Internal Padding


Block Positioning

Blocks on the top section begin from the top edge of the main
viewport, while the bottom section begins from the bottom edge.
Blocks are dynamically removed from visibility from the midpoint
of the viewport. So, a relatively large block number will not
draw to the viewport.

Lastly, there can be at most one HUD occupying a block at any time.
Trying to position a HUD in an occupied block will result in an error.
Keep this in mind when positioning the HUD.

---
blockAlignment(ba): string
    properties: create, query, edit
    Specifies the alignment of the block within its respective column. Available
alignments are: "center", "left" and "right". The default alignment is "left".

---
blockSize(bs): string
    properties: create, query, edit
    Sets the height of each block. Available heights are: small, medium and large.
In pixel measurements, each corresponds to a 20, 35 or 50 pixel height, respectively.

---
buttonLabel(bl): string
    properties: create, query, edit
    Text label of the HUD button.

---
buttonLabelFontSize(bfs): string
    properties: create, query, edit
    Sets the font size of the button label. Available sizes are: small and large.

---
buttonPressCommand(bpc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a button mouse click event.

---
buttonReleaseCommand(brc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a button mouse release event.

---
buttonShape(bsh): string
    properties: create, query, edit
    Specifies the shape of the button. Available button shapes are:
"rectangle" and "roundRectangle". The first will draw a rectangular
button, while the latter is a rectangle with rounded edges.

---
buttonWidth(bw): int
    properties: create, query, edit
    Specifies the width of the button.

---
decimalPrecision(dp): int
    properties: create, query, edit
    Sets the decimal precision of any floating point value returned by the command. The valid
range of precision values are 1 to 8.

---
internalPadding(ip): int
    properties: create, query, edit
    Specifies the amount of padding between the internal elements of the HUD. For the
hudSlider, this represents the padding between the slider bar and the slider
value. The default padding is 10.

---
maxValue(max): float
    properties: create, query, edit
    Specify the maximum value of the slider.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
minValue(min): float
    properties: create, query, edit
    Specify the minimum value of the slider.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
padding(p): int
    properties: create, query, edit
    Specifies the width of both the left and right margins of a block. Default
value is 15 pixels.

---
section(s): int
    properties: create, query, edit
    Defines the section the HUD will appear in. There are 10 sections
divided across the screen. Five columns and two rows make up the
ten element matrix which divide the main viewport. Here is a visual
layout of the sections.

 ________________________
|    |    |    |    |    |
|    |    |    |    |    |
| 0  | 1  | 2  | 3  | 4  |
|    |    |    |    |    |
|____|____|____|____|____|
|    |    |    |    |    |
|    |    |    |    |    |
| 5  | 6  | 7  | 8  | 9  |
|    |    |    |    |    |
|____|____|____|____|____|
Each section is denoted by a number from 0 to 9 as illustrated above.
For example, if the second column of the top row was desired, the
section would be defined as: -sec 1

To prevent HUD objects from displaying over each other and causing a
clutter of letters, each row has a defined visibility precedence,
where each section would have a visibility priority level. Depending
on each priority level, when the screen space begins to shrink to
a point where the section widths of a given row begin to collide, the
HUD automatically compensates for this by removing the sections of
least priority. These sections are made invisible and a warning is
issued to inform the user of the removal. This continues until only
the section of highest priority remains.

For each row, the priorities are defined as follows. Using the top
row as an example: Section 0, has the highest priority, followed
by Section 4, making the outermost sections of highest priority.
Next in the list is Section 2, and lastly Sections 1 and 3 are of
the equal and least priority. This priority structure can be applied
to the bottom row as well. The two outermost sections have the highest
priority, followed by the middle section, and finally the remaining
two sections are of lowest priority.

This means that as the viewport gradually decreases in width
to the point where sections in the top row begin to overlap, sections
1 and 3 will be removed from view first, followed by section 2, and
finally section 4. A similar note is provided below for the block layout.

---
sliderDragCommand(sdc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a slider mouse drag event.

---
sliderIncrement(si): float
    properties: create, query, edit
    Specify the number of increments along the slider. If not specified or set to 0 or less,
the slider will be linearly even and continuous from minValue to maxValue.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
sliderLabel(sl): string
    properties: create, query, edit
    Text label of the HUD slider.

---
sliderLabelFontSize(sfs): string
    properties: create, query, edit
    Sets the font size of the slider label. Available sizes are: small and large.

---
sliderLabelWidth(slw): int
    properties: create, query, edit
    Specifies the pixel width of the virtual "textbox" which will hold the label. The
contents of this "textbox" will be left justified. If the width of the actual label
exceeds the width of the "textbox," the label will be truncated to fit within the
dimensions of the "textbox." (To see a layout of a block, see the description
of the -block flag.)

---
sliderLength(sln): int
    properties: create, query, edit
    Specifies the length of the slider in pixels.

---
sliderPressCommand(spc): script
    properties: create, query, edit
    Specifies the procedure or script to run during a slider mouse click event.

---
sliderReleaseCommand(src): script
    properties: create, query, edit
    Specifies the procedure or script to run during a slider mouse release event.

---
type(t): string
    properties: create, query, edit
    Specify the numeric type of the HUD. Available types are:
"float" and "int".

---
value(v): float
    properties: create, query, edit
    Set/Return the slider value if the HUD is a valid HUD slider.
Note: Although this flag takes in a FLOAT as an argument, if the
HUD type is "int", the value will be automatically converted
internally to an integer.

---
valueAlignment(va): string
    properties: create, query, edit
    Specifies the alignment of the data blocks and the data text, within a HUD block.
Available alignments are: "left" and "right". The default alignment is "left".

---
valueFontSize(vfs): string
    properties: create, query, edit
    Sets the font size of the slider value. Available sizes are: small and large.

---
valueWidth(vw): int
    properties: create, query, edit
    Specifies the pixel width of the virtual "textbox" which will hold the slider value.
(To see a layout of a block, see the description of the -block flag.)

---
visible(vis): boolean
    properties: create, query, edit
    Sets the visibility of the Heads-Up Display on and off.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hudSliderButton.html 
    """


def hwReflectionMap(flagbackTextureName: string, flagbottomTextureName: string, flagcubeMap: boolean, flagdecalMode: boolean, flagenable: boolean, flagfrontTextureName: string, flagleftTextureName: string, flagrightTextureName: string, flagsphereMapTextureName: string, flagtopTextureName: string) -> string:
    """Synopsis:
---
---
 hwReflectionMap([backTextureName=string], [bottomTextureName=string], [cubeMap=boolean], [decalMode=boolean], [enable=boolean], [frontTextureName=string], [leftTextureName=string], [rightTextureName=string], [sphereMapTextureName=string], [topTextureName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hwReflectionMap is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.hwReflectionMap( cm=1, en=1, ftn='D:\\Textures\\room.front.jpg', bkn='D:\\Textures\\room.back.jpg', tpn='D:\\Textures\\room.top.jpg', bmn='D:\\Textures\\room.bottom.jpg', ltn='D:\\Textures\\room.left.jpg', rtn='D:\\Textures\\room.right.jpg', smn='D:\\Textures\\room.front.jpg' )

---
Return:
---


    string: (name of the created hwReflectionMap node)

Flags:
---


---
backTextureName(bkn): string
    properties: query
    This flag specifies the file texture name for the back side of the cube.
Default is none
When queried, this flag returns a string.

---
bottomTextureName(bmn): string
    properties: query
    This flag specifies the file texture name for the bottom side of the cube.
Default is none
When queried, this flag returns a string.

---
cubeMap(cm): boolean
    properties: query
    If on, the reflection of the textures is done using the cube mapping.
Default is false. The reflection is done using sphere mapping.
When queried, this flag returns a boolean.

---
decalMode(dm): boolean
    properties: query
    If on, the reflection color replaces the surface shading.
Default is false. The reflection is multiplied to the surface shading.
When queried, this flag returns a boolean.

---
enable(en): boolean
    properties: query
    If on, enable the corresponding hwReflectionMap node.
Default is false.
When queried, this flag returns a boolean.

---
frontTextureName(ftn): string
    properties: query
    This flag specifies the file texture name for the front side of the cube.
Default is none
When queried, this flag returns a string.

---
leftTextureName(ltn): string
    properties: query
    This flag specifies the file texture name for the left side of the cube.
Default is none
When queried, this flag returns a string.

---
rightTextureName(rtn): string
    properties: query
    This flag specifies the file texture name for the right side of the cube.
Default is none
When queried, this flag returns a string.

---
sphereMapTextureName(smn): string
    properties: query
    This flag specifies the file texture name for the sphere mapping option.
Default is none
When queried, this flag returns a string.

---
topTextureName(tpn): string
    properties: query
    This flag specifies the file texture name for the top side of the cube.
Default is none
When queried, this flag returns a string.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hwReflectionMap.html 
    """


def hwRender(flagacceleratedMultiSampleSupport: boolean, flagactiveTextureCount: boolean, flagcamera: string, flagcurrentFrame: boolean, flagcurrentView: boolean, flagedgeAntiAliasing: tuple[uint, uint], flagfixFileNameNumberPattern: boolean, flagframe: float, flagfullRenderSupport: boolean, flagheight: uint, flagimageFileName: boolean, flaglayer: name, flaglimitedRenderSupport: boolean, flaglowQualityLighting: boolean, flagnoRenderView: boolean, flagnotWriteToFile: boolean, flagprintGeometry: boolean, flagrenderHardwareName: boolean, flagrenderRegion: tuple[uint, uint, uint, uint], flagrenderSelected: boolean, flagtextureResolution: uint, flagwidth: uint, flagwriteAlpha: boolean, flagwriteDepth: boolean) -> boolean:
    """Synopsis:
---
---
 hwRender([acceleratedMultiSampleSupport=boolean], [activeTextureCount=boolean], [camera=string], [currentFrame=boolean], [currentView=boolean], [edgeAntiAliasing=[uint, uint]], [fixFileNameNumberPattern=boolean], [frame=float], [fullRenderSupport=boolean], [height=uint], [imageFileName=boolean], [layer=name], [limitedRenderSupport=boolean], [lowQualityLighting=boolean], [noRenderView=boolean], [notWriteToFile=boolean], [printGeometry=boolean], [renderHardwareName=boolean], [renderRegion=[uint, uint, uint, uint]], [renderSelected=boolean], [textureResolution=uint], [width=uint], [writeAlpha=boolean], [writeDepth=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hwRender is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Create a poly sphere.
cmds.polySphere()

Render it
cmds.hwRender()

Render the region where left=20, right=50, bottom=30, top=60.
And do not write the output to a file.
---

cmds.hwRender( renderRegion=(20, 50, 30, 60), notWriteToFile=True )

Render with the specified width and height.
---

cmds.hwRender( width=100, height=200 )

Returns the imageFileName for image frame 11.
---

cmds.hwRender( imageFileName=True, frame=11 )

Returns the imageFileName for current frame.
---

cmds.hwRender( imageFileName=True )

Returns a version of the image file name after its number pattern
being represented in a unique way.
---

cmds.hwRender( query=True, fixFileNameNumberPattern=True )

Render the specified render layer.
cmds.hwRender( layer='layer1' )

---
Return:
---


    boolean: Command result

Flags:
---


---
acceleratedMultiSampleSupport(ams): boolean
    properties: query
    This flag when used with query will return whether the graphics supports
    hardware accelerated multi-sampling.

---
activeTextureCount(atc): boolean
    properties: query
    This flag when used with query will return the number of textures that
    have been bound to the graphics by the hardware renderer.

---
camera(cam): string
    properties: create, query
    Specify the camera to use.  Use the first available camera if the camera
        given is not found.

---
currentFrame(cf): boolean
    properties: create, query
    Render the current frame.

---
currentView(cv): boolean
    properties: create, query
    When turned on, only the current view will be rendered.

---
edgeAntiAliasing(eaa): [uint, uint]
    properties: create, query
    Enables multipass rendering. Controls for the number of exposures rendered
per frame are provided in the form of two associated flag arguments. The first
specifies the sampling algorithm:

0 - Uniform Weighted Grid Sampling
1 - Rotated Grid Super Sampling (RGSS)
2 - Gaussian Weighted Sampling

 Use of a sampling method other than the others listed above, will result in
use of the default sample method of Uniform Weighted Grid Sampling. The second
argument specifies a number of samples to use. For each sampling algorithm
there is a fixed set of sample counts available:

0 - Uniform Weighted Grid Sampling
1 Sample
3 Samples
4 Samples
5 Samples
7 Samples
9 Samples
16 Samples
25 Samples
36 Samples
1 - Rotated Grid Super Sampling (RGSS)
1 Sample
4 Samples
5 Samples
2 - Gaussian Weighted Sampling
1 Sample
3 Samples
4 Samples
5 Samples
7 Samples
9 Samples
16 Samples
25 Samples
36 Samples

 Using a sampling count other than the allowable options for the given
sampling method will result in using the default sample count of 5. The values
passed via the command will override settings stored in the
hardwareRenderGlobals node.

---
fixFileNameNumberPattern(fnp): boolean
    properties: create, query
    This flag allows the user to take the hardwareRenderGlobals
    filename as the initial filename pattern,
    fix the frame number pattern in the filename in a unique way,
    returns the new filename pattern.  This does not change the
    hardwareRenderGlobals's filename.

---
frame(f): float
    properties: create
    Specify the frame to render.

---
fullRenderSupport(frs): boolean
    properties: create, query
    This flag may be used in the create or query context.
    In the create context, it will force the renderer to abort and not
    render any frames if the hardware is not fully supported.
        In the query context, it will return whether full quality rendering
    is supported on the current graphics system. Please see the graphics
    card qualification charts for an explanation of limited support.

---
height(h): uint
    properties: create, query
    Height. If not used, the height is taken from the render globals settings.

---
imageFileName(ifn): boolean
    properties: create, query
    This flag let people query the image name for a specified frame.
    The frame can be specified using the "-frame" flag.
    When no "-frame" is used, the
    current frame number is used.

---
layer(l): name
    properties: create, query
    Render the specified render layer.
        Only this render layer will be rendered,
        regardless of the renderable attribute value of the render layer.
        The layer name will be appended to the output image file name.
        The specified render layer becomes the current render layer before rendering,
        and remains as current render layer after the rendering.

---
limitedRenderSupport(lrs): boolean
    properties: query
    This flag when used with query will return whether limited rendering is supported
        on the current graphics system. Please see the graphics card qualification
        charts for the current definition of limited support.

---
lowQualityLighting(lql): boolean
    properties: create, query
    Disable lighting evaluation per pixel (fragment).
        Note: The values passed via the command will override settings stored in
    the hardware render globals node.

---
noRenderView(nrv): boolean
    properties: create, query
    When turned on, the render view is not updated after image computation

---
notWriteToFile(nwf): boolean
    properties: create, query
    This flag is set to true if the user does not want to write
    the image to a file.  It is set to false, otherwise.
    The default value of the flag is "false".

---
printGeometry(pg): boolean
    properties: create, query
    Print the geomety objects as they get translated.

---
renderHardwareName(rhw): boolean
    properties: query
    This flag will create a graphics context and return the name of the
    graphics hardware being used. The graphics hardware is determined by
    creating an off screen buffer and querying the GL_RENDERER string
    from OpenGL. If the off screen buffer cannot be created an empty
    string is returned.

---
renderRegion(reg): [uint, uint, uint, uint]
    properties: create, query
    Render region. The parameters are 4 integers, indicating
            left right bottom top
    of the region.

---
renderSelected(rs): boolean
    properties: create, query
    Only renders the selected objects.

---
textureResolution(res): uint
    properties: create, query
    Specify the desired resolution of baked textures.

---
width(w): uint
    properties: create, query
    Width. If not used, the width is taken from the render globals settings.

---
writeAlpha(a): boolean
    properties: create, query
    Read the alpha channel of color buffer and return as tif file.

---
writeDepth(d): boolean
    properties: create, query
    Read the depth buffer and return as tif file.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hwRender.html 
    """


def hwRenderLoad() -> None:
    """Synopsis:
---
---
 hwRenderLoad()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hwRenderLoad is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Load the HW render engine
cmds.hwRenderLoad()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hwRenderLoad.html 
    """


def hyperGraph(flagaddBookmark: boolean, flagaddDependGraph: name, flagaddDependNode: name, flaganimateTransition: boolean, flagattributeEditor: string, flagbackward: boolean, flagbookmarkName: boolean, flagbreakConnectionCommand: string, flagclear: boolean, flagcollapseContainer: boolean, flagconnectionDrawStyle: string, flagcontrol: boolean, flagcurrentEdge: string, flagcurrentNode: string, flagdebug: string, flagdefineTemplate: string, flagdeleteBookmark: string, flagdependGraph: boolean, flagdependNode: string, flagdirectoryPressCommand: string, flagdocTag: string, flagdown: boolean, flagdownstream: boolean, flagdragAndDropBehaviorCommand: string, flagdropNode: string, flagdropTargetNode: string, flagedgeDblClickCommand: string, flagedgeDimmedDblClickCommand: string, flagedgeDropCommand: string, flagedgePressCommand: string, flagedgeReleaseCommand: string, flagenableAutomaticLayout: boolean, flagexists: boolean, flagexpandContainer: boolean, flagfeedbackGadget: string, flagfeedbackNode: string, flagfilter: string, flagfilterDetail: tuple[string, boolean], flagfitImageToHeight: boolean, flagfitImageToWidth: boolean, flagfocusCommand: string, flagfold: boolean, flagforceMainConnection: string, flagforceRefresh: boolean, flagforward: boolean, flagframe: boolean, flagframeBranch: boolean, flagframeGraph: boolean, flagframeGraphNoRebuild: boolean, flagframeHierarchy: boolean, flagfreeform: boolean, flagfromAttr: string, flagfromNode: string, flaggetNodeList: boolean, flaggetNodePosition: string, flaggraphDescription: boolean, flaggraphLayoutStyle: string, flaggraphType: string, flagheatMapDisplay: boolean, flaghighlightConnection: string, flagiconSize: string, flagimage: string, flagimageEnabled: boolean, flagimageForContainer: boolean, flagimagePosition: tuple[float, float], flagimageScale: float, flaginitializeScript: string, flagisHotkeyTarget: boolean, flaglayout: boolean, flaglayoutSelected: string, flaglimitGraphTraversal: int, flaglockMainConnection: boolean, flaglook: tuple[float, float], flagmainListConnection: string, flagmergeConnections: boolean, flagnavigateHome: boolean, flagnavup: boolean, flagnewInputConnection: string, flagnewOutputConnection: string, flagnextView: boolean, flagnodeConnectCommand: string, flagnodeDblClickCommand: string, flagnodeDropCommand: string, flagnodeMenuCommand: string, flagnodePressCommand: string, flagnodeReleaseCommand: string, flagopaqueContainers: boolean, flagorientation: string, flagpanView: tuple[float, float], flagpanel: string, flagparent: string, flagpopupMenuScript: string, flagpreviousView: boolean, flagrange: tuple[float, float], flagrebuild: boolean, flagremoveNode: string, flagrename: boolean, flagresetFreeform: boolean, flagrestoreBookmark: string, flagscrollUpDownNoZoom: boolean, flagselectionConnection: string, flagsetNodePosition: tuple[string, float, float], flagshowCachedConnections: boolean, flagshowConnectionFromSelected: boolean, flagshowConnectionToSelected: boolean, flagshowConstraintLabels: boolean, flagshowConstraints: boolean, flagshowDeformers: boolean, flagshowExpressions: boolean, flagshowInvisible: boolean, flagshowRelationships: boolean, flagshowShapes: boolean, flagshowUnderworld: boolean, flagstateString: boolean, flagtoAttr: string, flagtoNode: string, flagtransitionFrames: int, flagunParent: boolean, flagunfold: boolean, flagunfoldAll: boolean, flagunfoldAllShapes: boolean, flagunfoldHidden: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flagupdateNodeAdded: boolean, flagupdateSelection: boolean, flagupstream: boolean, flaguseDrawOverrideColor: boolean, flaguseFeedbackList: boolean, flaguseTemplate: string, flagviewOption: string, flagvisibility: boolean, flagzoom: float) -> string:
    """Synopsis:
---
---
 hyperGraph(
[string]
    , [addBookmark=boolean], [addDependGraph=name], [addDependNode=name], [animateTransition=boolean], [attributeEditor=string], [backward=boolean], [bookmarkName=boolean], [breakConnectionCommand=string], [clear=boolean], [collapseContainer=boolean], [connectionDrawStyle=string], [control=boolean], [currentEdge=string], [currentNode=string], [debug=string], [defineTemplate=string], [deleteBookmark=string], [dependGraph=boolean], [dependNode=string], [directoryPressCommand=string], [docTag=string], [down=boolean], [downstream=boolean], [dragAndDropBehaviorCommand=string], [dropNode=string], [dropTargetNode=string], [edgeDblClickCommand=string], [edgeDimmedDblClickCommand=string], [edgeDropCommand=string], [edgePressCommand=string], [edgeReleaseCommand=string], [enableAutomaticLayout=boolean], [exists=boolean], [expandContainer=boolean], [feedbackGadget=string], [feedbackNode=string], [filter=string], [filterDetail=[string, boolean]], [fitImageToHeight=boolean], [fitImageToWidth=boolean], [focusCommand=string], [fold=boolean], [forceMainConnection=string], [forceRefresh=boolean], [forward=boolean], [frame=boolean], [frameBranch=boolean], [frameGraph=boolean], [frameGraphNoRebuild=boolean], [frameHierarchy=boolean], [freeform=boolean], [fromAttr=string], [fromNode=string], [getNodeList=boolean], [getNodePosition=string], [graphDescription=boolean], [graphLayoutStyle=string], [graphType=string], [heatMapDisplay=boolean], [highlightConnection=string], [iconSize=string], [image=string], [imageEnabled=boolean], [imageForContainer=boolean], [imagePosition=[float, float]], [imageScale=float], [initializeScript=string], [isHotkeyTarget=boolean], [layout=boolean], [layoutSelected=string], [limitGraphTraversal=int], [lockMainConnection=boolean], [look=[float, float]], [mainListConnection=string], [mergeConnections=boolean], [navigateHome=boolean], [navup=boolean], [newInputConnection=string], [newOutputConnection=string], [nextView=boolean], [nodeConnectCommand=string], [nodeDblClickCommand=string], [nodeDropCommand=string], [nodeMenuCommand=string], [nodePressCommand=string], [nodeReleaseCommand=string], [opaqueContainers=boolean], [orientation=string], [panView=[float, float]], [panel=string], [parent=string], [popupMenuScript=string], [previousView=boolean], [range=[float, float]], [rebuild=boolean], [removeNode=string], [rename=boolean], [resetFreeform=boolean], [restoreBookmark=string], [scrollUpDownNoZoom=boolean], [selectionConnection=string], [setNodePosition=[string, float, float]], [showCachedConnections=boolean], [showConnectionFromSelected=boolean], [showConnectionToSelected=boolean], [showConstraintLabels=boolean], [showConstraints=boolean], [showDeformers=boolean], [showExpressions=boolean], [showInvisible=boolean], [showRelationships=boolean], [showShapes=boolean], [showUnderworld=boolean], [stateString=boolean], [toAttr=string], [toNode=string], [transitionFrames=int], [unParent=boolean], [unfold=boolean], [unfoldAll=boolean], [unfoldAllShapes=boolean], [unfoldHidden=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [updateNodeAdded=boolean], [updateSelection=boolean], [upstream=boolean], [useDrawOverrideColor=boolean], [useFeedbackList=boolean], [useTemplate=string], [viewOption=string], [visibility=boolean], [zoom=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hyperGraph is undoable, queryable, and editable.
The hypergraph provides the user with the ability to view and edit
the maya scene graph.  The hypergraph supports two types of graphs:
the DAG or scene hierarchy and the dependency graph.

The default view of the hypergraph editor is the DAG view.
The user can show the dependency graph for a collection of nodes by
first selecting the nodes and navigating to the dependency graph using one
of the graph options.  The user can save any view by setting a
bookmark to that view.  The user can also show previous views using
the view options provided.

The hypergraph supports a simple editing mechanism for editing hierarchy
in the DAG view and connections in dependency graph view.
In the DAG  view, the user can reparent or reorder nodes in the graph
using drag-and-drop. In the dependency graph view, the user can select
connections and delete them or make new connections by dragging and
dropping nodes or existing connections.

The hypergraph supports two layout modes in the DAG view: automatic and
freeform.  In automatic mode, the graph nodes are automatically
positioned according to the layout preferences.  In freeform mode, the
user can position nodes manually.  The node position is saved in the scene.
A background image can be placed behind DG or DAG in freeform mode.
This can be used as a template for positioning nodes in a user-defined
layout.

Nodes in the DAG view can be expanded or collapsed.  The state is saved
in the scene.  The performance of the graph drawing will increase
as hierarchies are collapsed.

In addition to hierachy relationships, the hypergraph can show
expression, constraint and deformation relationships in the DAG.
These can be enabled/disabled through the options provided.  There
are also additional filters for showing shape nodes and invisible
nodes.  The amount of detail show may affect the speed of the display
of the graph.

Most of the UI features of the hypergraph are addressable through the
hypergraph command-line interface.  The available command-line
options are described in the next section.




Example:
---
import maya.cmds as cmds

The hyperGraph command is not one which would commonly be used
by the user.
cmds.polySphere( r=1, sx=20, sy=20, ax=(0, 1, 0), tx=2, ch=1 )

Gets the position of the node in the graph.
maya.mel.eval( "HypergraphHierarchyWindow" )
position = cmds.hyperGraph( 'hyperGraphPanel1HyperGraphEd', query=True, getNodePosition='pSphere1' )
print position

---
Return:
---


    string: the name of the panel

Flags:
---


---
addBookmark(abk): boolean
    properties: create, edit
    Create a bookmark for the current hypergraph view.

---
addDependGraph(adg): name
    properties: create, edit
    Add a dependency graph starting at the named node to the view

---
addDependNode(adn): name
    properties: create, edit
    Add a dependency node to the dependency graph view

---
animateTransition(atr): boolean
    properties: create, query, edit
    Turns animate transitions off and on.

---
attributeEditor(ae): string
    properties: create, edit
    Launches attribute editor on selected node.

---
backward(bak): boolean
    properties: create, edit
    Navigate backward one step.

---
bookmarkName(bn): boolean
    properties: query
    Returns the bookmark name for the most recently created bookmark.

---
breakConnectionCommand(bco): string
    properties: create, query, edit
    Specify the command to call when a connection is broken.

---
clear(clr): boolean
    properties: create, edit
    Clears the current hypergraph view and deletes the graph UI.
(see also -rebuild flag)

---
collapseContainer(cc): boolean
    properties: create, edit
    Collapses containers selected in DG graph.

---
connectionDrawStyle(cds): string
    properties: create, edit
    Specify how connections between nodes should be drawn. Valid
values are "center" (draws connection lines from the center of one node
to the center of the other) and "side" (draws connection lines from the
right side of the source node to the left side of the destination
node). The default is "center". This flag does not apply to Hypershade
graphs, which are always drawn with the "side" connection draw style.

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
currentEdge(ced): string
    properties: query, edit
    Return the current edge name.

---
currentNode(cno): string
    properties: query, edit
    Return the current node name.

---
debug(deb): string
    properties: create, edit
    Run a debug method on the graph

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
deleteBookmark(dbk): string
    properties: create, edit
    Delete the bookmark with the corresponding node name.

---
dependGraph(dg): boolean
    properties: create, edit
    Displays dependency graph iterated from specified node.

---
dependNode(dn): string
    properties: create, edit
    Displays dependency node in view.

---
directoryPressCommand(dp): string
    properties: create, edit
    Specify a command to run when a directory is pressed.

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
down(do): boolean
    properties: create, edit
    Navigate down to the dependency graph containing the current selection.
Shows upstream and downstream connections.

---
downstream(ds): boolean
    properties: create, edit
    Show downstream dependency graph of selected node(s).

---
dragAndDropBehaviorCommand(ddc): string
    properties: create, edit
    Mel proc called when a drag and drop onto a hyperGraph
node has occurred. Proc signature is
procName (string $editor, string $sourceNode, string $destinationNode).

---
dropNode(dr): string
    properties: query
    Returns the name of the source node in a drag and drop connection,
when called during processing of a drop.

---
dropTargetNode(drt): string
    properties: query
    Returns the name of the destination node in a drag and drop
connection, when called during processing of a drop.

---
edgeDblClickCommand(edc): string
    properties: create, edit
    Mel proc called when an edge is double clicked.  Proc signature is
procName (string $editor, string $edge).

---
edgeDimmedDblClickCommand(edd): string
    properties: create, edit
    Mel proc called when a dimmed edge is double clicked.  Proc signature is
procName (string $editor, string $edge).

---
edgeDropCommand(edr): string
    properties: create, edit
    Command to execute when an edge drop occurs.

---
edgePressCommand(ep): string
    properties: create, edit
    Command to execute when an edge press occurs.

---
edgeReleaseCommand(er): string
    properties: create, edit
    Command to execute when an edge release occurs.

---
enableAutomaticLayout(eal): boolean
    properties: create, edit
    Rebuild the graph if a node is added or removed from the graph
via drag and drop or dg messages. Default is true.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
expandContainer(ec): boolean
    properties: create, edit
    Expands containers selected in DG graph.

---
feedbackGadget(fbg): string
    properties: query
    Returns the name of the current gadget.

---
feedbackNode(fbn): string
    properties: query
    Returns the name of the current feedback or highlight node.

---
filter(f): string
    properties: create, query, edit
    Specifies the name of an itemFilter object to be used with this editor.
This filters the information coming onto the main list
of the editor.

---
filterDetail(fd): [string, boolean]
    properties: create, edit
    This flag is obsolete. Use the showConstraints, showExpressions,
showDeformer, showInvisible, showShapes and showUnderworld flags
instead.

---
fitImageToHeight(fih): boolean
    properties: create
    Changes position and scale of background image, so its height fits current editor view.

---
fitImageToWidth(fiw): boolean
    properties: create
    Changes position and scale of background image, so its width fits current editor view.

---
focusCommand(fc): string
    properties: create, edit
    Mel proc to be run when the mouse is clicked in the hyper
graph. Primarily of use in setting the window focus.

---
fold(fo): boolean
    properties: create, edit
    Folds (Collapses) selected object.

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
forceRefresh(frf): boolean
    properties: create, edit
    Forces the hypergraph to refresh (redraw) its contents.

---
forward(fow): boolean
    properties: create, edit
    Navigate forward one step.

---
frame(fr): boolean
    properties: create, edit
    Frames the selected objects

---
frameBranch(frb): boolean
    properties: create, edit
    Frames the the branch from the selected node on downward.

---
frameGraph(fg): boolean
    properties: create, edit
    Frames the entire graph.

---
frameGraphNoRebuild(fgn): boolean
    properties: create, edit
    Specify that on zoom out the graph should not rebuild; for efficiency.

---
frameHierarchy(frh): boolean
    properties: create, edit
    Frames the hierarchy that contains the selected node.

---
freeform(fre): boolean
    properties: create, query, edit
    Enable freeform layout mode.

---
fromAttr(fat): string
    properties: query
    Returns the name of the source attribute in a drag and drop
connection, when called during processing of a drop.

---
fromNode(frn): string
    properties: query
    Returns the name of the source node in a drag and drop
connection, when called during processing of a drop.

---
getNodeList(gnl): boolean
    properties: query
    Returns a string array that represents a list
of all the nodes in the graph.

---
getNodePosition(gnp): string
    properties: query
    Returns the position of a specified node in x,y graph coords.
This flag and its argument must be passed to the command before the
-q flag (see examples).
      In query mode, this flag can accept a value.

---
graphDescription(gd): boolean
    properties: create, edit
    When used, return a description of the current graph.

---
graphLayoutStyle(gls): string
    properties: create, query, edit
    This flag is obsolete.  The only supported graph layout style is "hierarchicalLayout".
Use of any other style will trigger a warning.

---
graphType(gt): string
    properties: query
    Returns the type name of the current graph in the view
(either DAG or DG).

---
heatMapDisplay(hmd): boolean
    properties: query, edit
    Specify whether the heat map should be shown or not.

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
iconSize(ics): string
    properties: create, query, edit
    Set or query the icon size for this hyper graph editor.
The currently allowed icon sizes are "smallIcons", "mediumIcons",
"largeIcons" and "superIcons".

---
image(img): string
    properties: create, query, edit
    Specify background image to be loaded from the project image directory.

---
imageEnabled(ime): boolean
    properties: create, query, edit
    Enable display of a loaded background image (Freeform DAG view or DG view)

---
imageForContainer(ifc): boolean
    properties: create, query, edit
    Specify that the following flags work on selected containers instead of the whole image:
-imageScale,-imagePosition, fitImageToWidth, -fitImageToHeight, -image

---
imagePosition(imp): [float, float]
    properties: create, query, edit
    Position of the background image.

---
imageScale(ims): float
    properties: create, query, edit
    Uniform scale of the background image.

---
initializeScript(ini): string
    properties: create, edit
    Script to call when the graph is initialized.

---
isHotkeyTarget(iht): boolean
    properties: query
    For internal use.

---
layout(lay): boolean
    properties: create, edit
    Perform an automatic layout on the graph.

---
layoutSelected(lsl): string
    properties: create, edit
    This flag is obsolete.  The only supported graph layout style is "hierarchicalLayout".
Use of any other style will trigger a warning.

---
limitGraphTraversal(lgt): int
    properties: create, edit
    Limit the graph traversal to a certain number of levels.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
look(loo): [float, float]
    properties: create, edit
    Look at a coordinate in the graph view

---
mainListConnection(mlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will use as its source of content. The editor will
only display items contained in the selectionConnection object.

---
mergeConnections(mc): boolean
    properties: create, query, edit
    Merge groups of connections into 'fat' connections.

---
navigateHome(hom): boolean
    properties: create, edit
    Navigate to the home (DAG) view.

---
navup(nu): boolean
    properties: create, edit
    Navigate up to the dependency graph containing the current selection.
Shows upstream and downstream connections.

---
newInputConnection(nin): string
    properties: create, edit
    Specify a new connection, input side

---
newOutputConnection(nou): string
    properties: create, edit
    Specify a new connection, output side

---
nextView(nvw): boolean
    properties: create, edit
    Changes the view to the next DAG view.

---
nodeConnectCommand(nco): string
    properties: create, edit
    Command to call when a node is connected.

---
nodeDblClickCommand(ndc): string
    properties: create, edit
    Command to call when a node is double-clicked.

---
nodeDropCommand(ndr): string
    properties: create, edit
    Set the command to be called when a node is dropped in the
hypergraph window.

---
nodeMenuCommand(nm): string
    properties: create, edit
    Command to call when a node menu is activated.

---
nodePressCommand(np): string
    properties: create, edit
    Set the command to be called when the user presses a mouse button
while the cursor is over a node in the hypergraph window.

---
nodeReleaseCommand(nr): string
    properties: create, edit
    Set the command to be called when the user releases a mouse button
while the cursor is over a node in the hypergraph window.

---
opaqueContainers(opc): boolean
    properties: query, edit
    Sets expanded container background opacity.

---
orientation(orientation): string
    properties: create, query, edit
    Selects orientation style of graph: "horiz"|"vert"

---
panView(pan): [float, float]
    properties: create, edit
    Pan the view to a new center.

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
popupMenuScript(pms): string
    properties: create, edit
    Set the script to be called to register the popup menu with the
control for this hypergraph. The script will be called with a string
argument which gives the name of the hypergraph whose control the popup
menu should be parented to.

---
previousView(pvw): boolean
    properties: create, edit
    Changes the view back to the previous DAG view.

---
range(rg): [float, float]
    properties: create, query, edit
    Limits the display of nodes to only those within the range.
There are two float values expected, the first the lower threshold
of the range and the second the upper threshold of the range.
The values are absolute timing values, not percentages.

---
rebuild(rb): boolean
    properties: create, edit
    Rebuilds graph

---
removeNode(rmn): string
    properties: create, edit
    Removes the node identified by string from the graph.

---
rename(rn): boolean
    properties: create, edit
    Pops up text field over selected object for renaming

---
resetFreeform(rf): boolean
    properties: create, edit
    Resets freeform position on all nodes.

---
restoreBookmark(rbk): string
    properties: create, edit
    Restore the view corresponding to the bookmark.

---
scrollUpDownNoZoom(snz): boolean
    properties: create, edit
    Specify if we want to be in the
scroll along y only with no free zooming mode.
By default, hyper graph editor allows user to
pan left and right.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
setNodePosition(snp): [string, float, float]
    properties: create, edit
    Sets the node identified by string to the (x,y) position
in the window specified by the two floats. If
the node is not in the graph than it will be added to the
graph and then moved to the new position.

---
showCachedConnections(scc): boolean
    properties: create, edit
    Specify whether cached connections should be shown.

---
showConnectionFromSelected(scf): boolean
    properties: create, query, edit
    Show the connects (constraints, expresions, and deformers - see showConstraints for example)
leaving from selected nodes. This can be combined with showConnectionToSelected to show both
arrive and leaving connects. If both flags are false then all the connections will be shown.

---
showConnectionToSelected(sct): boolean
    properties: create, query, edit
    Show the connects (constraints, expresions, and deformers - see showConstraints for example)
arriving at selected nodes. This can be combined with
showConnectionFromSelected to show both arrive and leaving connects. If both flags
are false then all the connections will be shown.

---
showConstraintLabels(scl): boolean
    properties: create, edit
    Specify whether constraint labels should be shown.

---
showConstraints(shc): boolean
    properties: create, query, edit
    Show constraint relationships in the DAG.

---
showDeformers(shd): boolean
    properties: create, query, edit
    Show deformer or geometry filter relationships in the DAG.

---
showExpressions(shx): boolean
    properties: create, query, edit
    Show expression relationships in the DAG.

---
showInvisible(shi): boolean
    properties: create, query, edit
    Show invisible nodes in the DAG.

---
showRelationships(shr): boolean
    properties: create, query, edit
    Show relationship (message) connections.

---
showShapes(shs): boolean
    properties: create, query, edit
    Show shape nodes in the DAG.

---
showUnderworld(shu): boolean
    properties: create, query, edit
    Show underworld graphs in the DAG.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
toAttr(tat): string
    properties: query
    Returns the name of the destination attribute in a drag and drop
connection, when called during processing of a drop.

---
toNode(ton): string
    properties: query
    Returns the name of the destination node in a drag and drop
connection, when called during processing of a drop.

---
transitionFrames(tfr): int
    properties: create, query, edit
    Specify te number of transition frames for animate transitions.

---
unParent(up): boolean
    properties: create, edit
    Specifies that the editor should be removed from its layout.
This cannot be used in query mode.

---
unfold(uf): boolean
    properties: create, edit
    Unfolds (expands) selected object.

---
unfoldAll(ua): boolean
    properties: create, edit
    Unfolds everything under selected object.

---
unfoldAllShapes(uas): boolean
    properties: create, edit
    Unfolds all shapes.

---
unfoldHidden(ufh): boolean
    properties: create, edit
    Unfolds all hidden objects.

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
updateNodeAdded(una): boolean
    properties: create, query, edit
    Update graph when a new node is added to the database

---
updateSelection(us): boolean
    properties: create, query, edit
    Update selection state in the graph when the selection state of
database changes.

---
upstream(ups): boolean
    properties: create, edit
    Show upstream dependency graph of selected node(s).

---
useDrawOverrideColor(drc): boolean
    properties: create, edit
    Specify whether or not to use draw override coloring.

---
useFeedbackList(ufl): boolean
    properties: create, query, edit
    Use feedback or highlight list as the target selection when
processing other hypergraph command-line options.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
viewOption(vo): string
    properties: create, query, edit
    Set or query the view option for this hyper graph editor.
The currently allowed views are "asIcons" and "asList".

---
visibility(vis): boolean
    properties: create, edit
    Set the visible state of the selected node(s).

---
zoom(zm): float
    properties: create, edit
    Specify the zoom factor for animating transitions

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hyperGraph.html 
    """


def hyperPanel(flagcontrol: boolean, flagcopy: string, flagcreateString: boolean, flagdefineTemplate: string, flagdocTag: string, flageditString: boolean, flagexists: boolean, flaghyperEditor: boolean, flaginit: boolean, flagisUnique: boolean, flaglabel: string, flagmenuBarRepeatLast: boolean, flagmenuBarVisible: boolean, flagneedsInit: boolean, flagparent: string, flagpopupMenuProcedure: script, flagreplacePanel: string, flagtearOff: boolean, flagtearOffCopy: string, flagtearOffRestore: boolean, flagunParent: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 hyperPanel(
[panelName]
    , [control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean], [hyperEditor=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hyperPanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.frameLayout( lv=False )
cmds.hyperPanel()
cmds.showWindow()

---
Return:
---


    string: The name of the panel

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
hyperEditor(he): boolean
    properties: query
    This flag returns the name of the hypergraph editor
contained by the panel.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hyperPanel.html 
    """


def hyperShade(flagassign: string, flagclearWorkArea: boolean, flagcollapse: string, flagcreateNode: string, flagdependGraphArea: boolean, flagdownStream: boolean, flagduplicate: boolean, flagfixRenderSize: boolean, flaggeometries: string, flagincremental: boolean, flaglistDownstreamNodes: name, flaglistDownstreamShaderNodes: name, flaglistGeometries: string, flaglistMaterialNodes: boolean, flaglistUpstreamNodes: name, flagname: string, flagnetworks: boolean, flagnoSGShapes: boolean, flagnoShapes: boolean, flagnoTransforms: boolean, flagobjects: string, flagrenderCreateAndDrop: string, flagreset: boolean, flagresetGraph: boolean, flagresetSwatch: boolean, flagsetAllowsRegraphing: boolean, flagsetWorkArea: string, flagshaderNetwork: string, flagshaderNetworks: boolean, flagshaderNetworksSelectMaterialNodes: boolean, flagsnapShot: boolean, flaguncollapse: string, flagupStream: boolean, flaguseMaterialTemplate: boolean, flaguserDefinedLayout: boolean, flagworkAreaAddCmd: string, flagworkAreaDeleteCmd: string, flagworkAreaSelectCmd: string) -> string:
    """Synopsis:
---
---
 hyperShade([assign=string], [clearWorkArea=boolean], [collapse=string], [createNode=string], [dependGraphArea=boolean], [downStream=boolean], [duplicate=boolean], [fixRenderSize=boolean], [geometries=string], [incremental=boolean], [listDownstreamNodes=name], [listDownstreamShaderNodes=name], [listGeometries=string], [listMaterialNodes=boolean], [listUpstreamNodes=name], [name=string], [networks=boolean], [noSGShapes=boolean], [noShapes=boolean], [noTransforms=boolean], [objects=string], [renderCreateAndDrop=string], [reset=boolean], [resetGraph=boolean], [resetSwatch=boolean], [setAllowsRegraphing=boolean], [setWorkArea=string], [shaderNetwork=string], [shaderNetworks=boolean], [shaderNetworksSelectMaterialNodes=boolean], [snapShot=boolean], [uncollapse=string], [upStream=boolean], [useMaterialTemplate=boolean], [userDefinedLayout=boolean], [workAreaAddCmd=string], [workAreaDeleteCmd=string], [workAreaSelectCmd=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

hyperShade is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.sphere()
cmds.cone()
myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.select( 'nurbsSphere1' )
cmds.hyperShade( assign=myBlinn )
cmds.select( cl=True )
cmds.hyperShade( objects=myBlinn )

blinn = cmds.createNode('blinn')
cmds.select( 'lambert1', blinn )
cmds.hyperShade( objects='' )

cmds.polySphere(sx=20,sy=20)
cmds.hyperShade( assign=myBlinn, geo=['pSphere1.f[300:359]', 'pSphere1.f[380:399]'])

---
Return:
---


    string: Command result

Flags:
---


---
assign(a): string
    properties: create
    Assign the specified shader node to renderable objects on the active list
or the geometries in the -geometries option when specified.
The node can either be a shading group or the shader node attached to the
shading group.

---
clearWorkArea(cwa): boolean
    properties: create
    Push the current work area on to the stack and create a clear work area

---
collapse(clp): string
    properties: create
    Hide the upstream nodes from the specified node.

---
createNode(rcn): string
    properties: create
    Create a node of the specified type.  This is called when a new rendering
node is created using drag and drop from the image browser or from the
RMB context sensitive menu on nodes in the Visor Create folders.

---
dependGraphArea(dg): boolean
    properties: create
    When setting a work area, and the work area doesn't already exist this
flag inicates a new graph should be created that is either a depend graph
or a folder view.

---
downStream(ds): boolean
    properties: create
    Show nodes downstream from the specified node

---
duplicate(dup): boolean
    properties: create
    Duplicate upstream nodes.  If the node is a shader make sure duplicate
include the shading group if there is one

---
fixRenderSize(fix): boolean
    properties: create
    If set to true dont rerender swatches when they change size as the user
zooms

---
geometries(geo): string
    properties: create, multiuse
    When used in conjunction with the -assign option the shaders will be assigned to geometries specified here.
When used in conjunction with the -listMaterialNodes option the material nodes used by the geometries specified here will be listed.

---
incremental(inc): boolean
    properties: create
    Enable or disable incremental layout when making new nodes or connections

---
listDownstreamNodes(ldn): name
    properties: create
    List all the downstream render nodes from the specified nodes.

---
listDownstreamShaderNodes(lds): name
    properties: create
    List all the downstream shader nodes from the specified nodes.

---
listGeometries(lgm): string
    properties: create
    List the geoemtries which are attached to the specified shader node.
The shader node can be either the shading group or the shader attached
to the shading group.  When this flag's argument is the empty string,
we will use the currently selected shader node as the input.

---
listMaterialNodes(lmn): boolean
    properties: create
    List all the materials nodes for the geometries in the -geometries option
or, if not specified, the currently selected objects.

---
listUpstreamNodes(lun): name
    properties: create
    List all the upstream render nodes from the specified nodes.

---
name(n): string
    properties: create
    Name for the work area created by this command

---
networks(net): boolean
    properties: create
    Do an incremental layout on all of the nodes in the current selection
list and that are in the current work area.

---
noSGShapes(nsg): boolean
    properties: create
    Display only shapes that are connected to nodes in the
network other than a shading group.

---
noShapes(ns): boolean
    properties: create
    Display no shapes when graphing networks.

---
noTransforms(nt): boolean
    properties: create
    Display no transforms when graphing networks.

---
objects(o): string
    properties: create
    Select the objects which are attached to the specified shader node.
The shader node can be either the shading group or the shader attached
to the shading group.  When this flag's argument is the empty string,
we will use the currently selected shder node as the input.

---
renderCreateAndDrop(rcd): string
    properties: create
    Create a render node of the specified type and put user into drag and
drop mode to place or connect it.

---
reset(rst): boolean
    properties: create
    Reset the Hypershade panel to its initial state.  In particular delete all
the work areas.

---
resetGraph(rsg): boolean
    properties: create
    Reset the current graph.  Typically called prior to rebuilding a folder in
a Hypershade view.

---
resetSwatch(rss): boolean
    properties: create
    For all selected nodes remove user defined swatches if the node has one

---
setAllowsRegraphing(sar): boolean
    properties: create
    For internal use only.

---
setWorkArea(swa): string
    properties: create
    Set the work area to the existing named work area

---
shaderNetwork(sn): string
    properties: create
    Show the shader network for the specified material node.  If the materials
shading group has a displacement or volume map these will be shown.  If not
then the shading group will not be shown.

---
shaderNetworks(sns): boolean
    properties: create
    Show the shader network for all the objects on the selection list that
have shaders.

---
shaderNetworksSelectMaterialNodes(smn): boolean
    properties: create
    Select the material nodes in the shader network for all the
objects on the selection list that have shaders.

---
snapShot(snp): boolean
    properties: create
    Put hypergraph in snapshot mode.  This is only for testing

---
uncollapse(ucl): string
    properties: create
    Unhide the upstream nodes from the specified node.

---
upStream(ups): boolean
    properties: create
    Show nodes upstream from the specified node

---
useMaterialTemplate(umt): boolean
    properties: create
    Specifies that a material will be assigned using the materialTemplate method.

---
userDefinedLayout(udl): boolean
    properties: create
    Enable or disable remembrance of user defined layouts.  Default is disabled
until this functionality is better tested.

---
workAreaAddCmd(waa): string
    properties: create
    Set the MEL procedure called when a new work area is added to HyperShade

---
workAreaDeleteCmd(wad): string
    properties: create
    Set the MEL procedure called when a work area is deleted in HyperShade

---
workAreaSelectCmd(was): string
    properties: create
    Set the MEL procedure called when a work area is selected in HyperShade

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/hyperShade.html 
    """
