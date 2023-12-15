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


def dagObjectCompare(flagattribute: boolean, flagbail: string, flagconnection: boolean, flagnamespace: string, flagrelative: boolean, flagshort: boolean, flagtype: boolean) -> None:
    """Synopsis:
---
---
 dagObjectCompare([attribute=boolean], [bail=string], [connection=boolean], [namespace=string], [relative=boolean], [short=boolean], [type=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dagObjectCompare is NOT undoable, NOT queryable, and NOT editable.
type -  Currently supports transform nodes and shape nodes
relatives - Compares DAG objects' children and parents
connections - Checks to make sure the two dags are connected to the same sources and destinations
attributes - Checks to make sure that the properties of active attributes are the same



Example:
---
import maya.cmds as cmds

Compare two objects based on type and their relatives where one is in the namespace "base":
cmds.dagObjectCompare( t=True, r=True, n="base" )

Compare two objects based on their connections and attributes where one is in the namespace "base" , break on first error:
cmds.dagObjectCompare( c=True, a=True, b="first")

Compare two objects based on their type, connections, attributes, relatives and break on error while finishing current category:
cmds.dagObjectCompare( t=True, r=True, c=True, a=True, b=True, category=True, n="base")

---


Flags:
---


---
attribute(a): boolean
    properties: create
    Compare dag object attributes

---
bail(b): string
    properties: create
    Bail on first error or bail on category. Legal values are
"never", "first", and "category".

---
connection(c): boolean
    properties: create
    Compare dag connections

---
namespace(n): string
    properties: create
    The baseline namespace

---
relative(r): boolean
    properties: create
    dag relatives

---
short(s): boolean
    properties: create
    Compress output to short form (not as verbose)

---
type(t): boolean
    properties: create
    Compare based on dag object type

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dagObjectCompare.html 
    """


def dagPose(flagaddToPose: boolean, flagatPose: boolean, flagbindPose: boolean, flagg: boolean, flagmembers: boolean, flagname: string, flagremove: boolean, flagreset: boolean, flagrestore: boolean, flagsave: boolean, flagselection: boolean, flagworldParent: boolean) -> string:
    """Synopsis:
---
---
 dagPose(
[objects]
    , [addToPose=boolean], [atPose=boolean], [bindPose=boolean], [g=boolean], [members=boolean], [name=string], [remove=boolean], [reset=boolean], [restore=boolean], [save=boolean], [selection=boolean], [worldParent=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dagPose is undoable, queryable, and editable.
This command can also be used to store a bindPose for an object.
When you skin an object, a dagPose is automatically created for the
skin.




Example:
---
import maya.cmds as cmds

To create a pose for all objects parented above and below
the selected items.
---

cmds.dagPose( save=True )

To create a dagPose named "mypose" for the selected items only and not
the dag objects parented below the selected items.
---

cmds.dagPose( save=True, selection=True, name='mypose' )

To restore the local (rather than global) mypose pose
---

cmds.dagPose( 'mypose', restore=True )

To restore the mypose pose in global mode.
---

cmds.dagPose( 'mypose', restore=True, global=True )

To query the members of the mypose pose.
---

cmds.dagPose( 'mypose', query=True, members=True )

To return the name (if any) of the bindPose attached to the
selected items.
---

cmds.dagPose( q=True, bindPose=True )

To reset the pose data on a joint named bigToe for "mypose"
---

cmds.dagPose( 'bigToe', reset=True, n='mypose' )

To remove a joint named pinky from "mypose"
---

cmds.dagPose( 'pinky', remove=True, n='mypose' )

To restore the skeleton to its bindPose
---

cmds.dagPose( restore=True, global=True, bindPose=True )

---
Return:
---


    string: Name of pose

Flags:
---


---
addToPose(a): boolean
    properties: create
    Allows adding the selected items to the dagPose.

---
atPose(ap): boolean
    properties: query
    Query whether the hierarchy is at same position as the pose.
Names of hierarchy members that are not at the pose position will
be returned. An empty return list indicates that the hierarchy is at the
pose.

---
bindPose(bp): boolean
    properties: create, query
    Used to specify the bindPose for the selected hierarchy.
Each hierarchy can have only
a single bindPose, which is saved automatically at the time of a skin
bind. The bindPose is used when adding influence objects,
binding new skins, or adding flexors. Take care when modifying
the bindPose with the -rs/-reset
or -rm/-remove flags, since if the bindPose is ill-defined it can
cause problems with subsequent skinning operations.

---
g(g): boolean
    properties: create
    This flag can be used in conjunction with the restore flag to
signal that the members of the pose should be restored to the
global pose. The global pose means not only is each object
locally oriented with respect to its parents, it is also in the
same global position that it was at when the pose was saved.
If a hierarchy's parenting has been changed since the time that
the pose was saved, you may have trouble reaching the global pose.

---
members(m): boolean
    properties: query
    Query the members of the specified pose. The pose should be
specified using the selection list, the -bp/-bindPose or the -n/-name flag.

---
name(n): string
    properties: create, query
    Specify the name of the pose. This can be used during create,
restore, reset, remove, and query operations to specify the pose
to be created or acted upon.

---
remove(rm): boolean
    properties: create
    Remove the selected joints from the specified pose.

---
reset(rs): boolean
    properties: create
    Reset the pose on the selected joints. If
you are resetting pose data for a bindPose, take care. It is appropriate
to use the -rs/-reset flag if a joint has been reparented and/or appears to
be exactly at the bindPose. However, a bindPose that is much different
from the exact bindPose can cause problems with subsequent skinning operations.

---
restore(r): boolean
    properties: create
    Restore the hierarchy to a saved pose. To specify the pose,
select the pose node, or use the -bp/-bindPose or -n/-name flag.

---
save(s): boolean
    properties: create
    Save a dagPose for the selected dag hierarchy. The name of the
new pose will be returned.

---
selection(sl): boolean
    properties: create, query
    Whether or not to store a pose for all items in the hierarchy,
or for only the selected items.

---
worldParent(wp): boolean
    properties: create
    Indicates that the selected pose member should be recalculated as if it is
parented to the world. This is typically used when you plan to reparent
the object to world as the next operation.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dagPose.html 
    """


def dataStructure(flagasFile: string, flagasString: string, flagdataType: boolean, flagformat: string, flaglistMemberNames: string, flagname: string, flagremove: boolean, flagremoveAll: boolean) -> list[string] | string:
    """Synopsis:
---
---
 dataStructure([asFile=string], [asString=string], [dataType=boolean], [format=string], [listMemberNames=string], [name=string], [remove=boolean], [removeAll=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dataStructure is undoable, queryable, and NOT editable.
Takes in a description of the structure and creates it, adding it to
the list of available data structures. The structure definition can
either be supplied in the asString flag or exist in a file that is
referenced by the asFile flag.


If the remove flag is specified with a name flag then the data
structure will be removed. This is to keep all structure operations
in a single command rather than create separate commands to create,
remove, and query the data structures. When you use the removeAll
flag then every existing metadata structure is removed. Use with care!
Note that removed structures may still be in use in metadata Streams after
removal, they are just no longer available for the creation of new Streams.


Both the creation modes and the remove mode are undoable.


Creation of an exact duplicate of an existing structure (including name)
will succeed silently without actually creating a new structure.
Attempting to create a new non-duplicate structure with the same name
as an existing structure will fail as there is no way to disambiguate
two structures with the same name.


Querying modes are defined to show information both on the created
structures and the structure serialization formats that have been
registered. The serialization formats preserve the structure
information as text (e.g. raw, XML, JSON). Since the raw structure
type is built in it will be assumed when none are specified.


General query with no flags will return the list of names of all
currently existing structures.


Querying the format flag will return the list of all registered structure
serialization formats.


Querying with the format supplied before the query flag will
show the detailed description of that particular structure
serialization format.


Querying the asString flag with a structure name and serialization
format supplied before the query flag will return a string
representing the named data structure in the serialization format
specified by the format flag. Even if the format is the same as
the one that created the structure the query return string may not
be identical since the queried value is formatted in a standard
way - original formatting is not preserved.


Querying the asFile flag with a structure name supplied before the
query flag will return the original file from which the structure
was generated. If the structure was created using the asString
flag or through the API then an empty string will be returned.


Querying the name flag returns the list of all structures created
so far.




Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.dataStructure( query=True, format=True )
Result: ['raw', 'debug'] ---


cmds.dataStructure( format='raw', asString='name=NameAndID:string=name:int32=ID' )
Result: 'NameAndID' ---


Note that this file doesn't exist, it's just an example of how to read
from the file after you've created it. The file contents should look
like this:
---
                name=FileBasedStructure
---
                string=fileInformation
cmds.dataStructure( asFile='someFile.raw' )

cmds.dataStructure( query=True )
Result: ['NameAndID', 'FileBasedStructure'] ---


cmds.dataStructure( name='NameAndID', format='raw', query=True, asString=True )
Result: 'name=NameAndID:string=name:int32=ID' ---


cmds.dataStructure( name='NameAndID', query=True, listMemberNames=True )
Result: [u'name', u'ID'] ---


cmds.dataStructure( name='NameAndID', query=True, listMemberNames=True, dataType=True )
Result: [u'name', u'string', u'ID', u'int32'] ---


cmds.dataStructure( remove=True, name='NameAndID' )
Result: 'NameAndID' ---


cmds.dataStructure( query=True )
Result: ['FileBasedStructure'] ---


cmds.dataStructure( removeAll=True )
Result: ['FileBasedStructure'] ---


---
Return:
---


    string: Name of the resulting structure, should match the name defined in the structure description
    list[string]: Name(s) of the removed structures.

Flags:
---


---
asFile(af): string
    properties: create, query
    Specify a file that contains the serialized data which describes the
structure.  The format of the data is specified by the 'format' flag.

---
asString(asString): string
    properties: create, query
    Specify the string containing the serialized data which describes the
structure. The format of the data is specified by the 'format' flag.

---
dataType(dt): boolean
    properties: create, query
    Used with the flag 'listMemberNames' to query the type of the member.
The type is appended after each relative member in the array.
For example, if the format is "name=idStructure:int32=id:string=name"
the returned array is "id int32 name string".

---
format(fmt): string
    properties: create, query
    Format of data to expect in the structure description. "raw" is supported
natively and will be assumed if the format type is omitted. Others are
available via plug-in. You can query the available formats by using this
flag in query mode.
                        In query mode, this flag can accept a value.

---
listMemberNames(lmn): string
    properties: create, query
    Query the member names in the dataStructure. The member names will be
returned in an array. The name of the data structure will not be returned.
To get the type of each member, use 'dataType' together. Then the type of
the member will be appended in the array after their relative member.
For example, if the format is "name=idStructure:int32=id:string=name"
the returned array is "id int32 name string".

---
name(n): string
    properties: query
    Query mode only.  Name of the data structure to be queried, or set to
list the available names.
                        In query mode, this flag can accept a value.

---
remove(rem): boolean
    properties: create
    Remove the named data structure. It's an error if it doesn't exist.

---
removeAll(ral): boolean
    properties: create
    Remove all metadata structures. This flag can not be used in conjunction with
any other flags.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dataStructure.html 
    """


def date(flagdate: boolean, flagformat: string, flagshortDate: boolean, flagshortTime: boolean, flagtime: boolean) -> string:
    """Synopsis:
---
---
 date([date=boolean], [format=string], [shortDate=boolean], [shortTime=boolean], [time=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

date is NOT undoable, NOT queryable, and NOT editable.-format


Example:
---
import maya.cmds as cmds

Get the current date and time
cmds.date()
Result:2006/03/09 16:50:24 ---


Get only the month and day
cmds.date( shortDate=True )
Result:03/09 ---


Get the date and time in a fancy format
cmds.date( format='Year is YY (or YYYY), month is MM, day is DD. And it is now hh:mm:ss' )
Result:Year is 06 (or 2006), month is 03, day is 09. And it is now 16:53:20 ---


---
Return:
---


    string: Command result

Flags:
---


---
date(d): boolean
    properties: create
    Returns the current date. Format is YYYY/MM/DD

---
format(f): string
    properties: create
    Specifies a string defining how the date and time should be represented. All
occurences of the keywords below will be replaced with the corresponding
values:

KeywordBecomes
YYYYCurrent year, using 4 digits
YYLast two digits of the current year
MMCurrent month, with leading 0 if necessary
DDCurrent day, with leading 0 if necessary
hhCurrent hour, with leading 0 if necessary
mmCurrent minute, with leading 0 if necessary
ssCurrent second, with leading 0 if necessary

---
shortDate(sd): boolean
    properties: create
    Returns the current date. Format is MM/DD

---
shortTime(st): boolean
    properties: create
    Returns the current time. Format is hh:mm

---
time(t): boolean
    properties: create
    Returns the current time. Format is hh:mm:ss

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/date.html 
    """


def dbcount(flagenabled: boolean, flagfile: string, flagkeyword: string, flaglist: boolean, flagmaxdepth: uint, flagquick: boolean, flagreset: boolean, flagspreadsheet: boolean) -> None:
    """Synopsis:
---
---
 dbcount([enabled=boolean], [file=string], [keyword=string], [list=boolean], [maxdepth=uint], [quick=boolean], [reset=boolean], [spreadsheet=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dbcount is NOT undoable, NOT queryable, and NOT editable.dbcount


Example:
---
import maya.cmds as cmds


cmds.dbcount( e='on' )              Enable counters
cmds.dbcount( )                     Print all available counters
cmds.dbcount( f='myCounts.txt' )    Print all available counters to the file "myCounts.txt"
cmds.dbcount( k='dirty' )           Print all counters with "dirty" in their name
cmds.dbcount( r=True, k='dirty' )   Reset counters with "dirty" in their name
cmds.dbcount( l=True )              List all counters
cmds.dbcount( l=True, k='dirty' )   List all counters with "dirty" in their name
cmds.dbcount( s=True, f='xls.txt' ) Print all counters in spreadsheet form to the file "xls.txt"

---


Flags:
---


---
enabled(e): boolean
    properties: create
    Set the enabled state of the counters ('on' to enable, 'off' to disable).
Returns the list of all counters affected.

---
file(f): string
    properties: create
    Destination file of the enabled count objects.  Use the special names
stdout and stderr to redirect to your command window.  As
well, the special name msdev is available on NT to direct your
output to the debug tab in the output window of Developer Studio.

---
keyword(k): string
    properties: create
    Print only the counters whose name matches this keyword (default is all).

---
list(l): boolean
    properties: create
    List all available counters and their current enabled status. (The only
thing you can do when counters are disabled.)

---
maxdepth(md): uint
    properties: create
    Maximum number of levels down to traverse and report. 0 is the default and
it means continue recursing as many times as are requested.

---
quick(q): boolean
    properties: create
    Display only a summary for each counter type instead of the full details.

---
reset(r): boolean
    properties: create
    Reset all counters back to 0 and remove all but the top level counters.
Returns the list of all counters affected.

---
spreadsheet(s): boolean
    properties: create
    Display in spreadsheet format instead of the usual nested braces.
This will include a header row that contains 'Count Level1 Level2 Level3...',
making the data suitable for opening directly in a spreadsheet table.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dbcount.html 
    """


def dbfootprint(flagallObjects: boolean, flagoutputFile: string, flagtype: string) -> list[string] | string:
    """Synopsis:
---
---
 dbfootprint([allObjects=boolean], [outputFile=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dbfootprint is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.dbfootprint( query=True )
Result: ['nodes'] ---


---
Return:
---


    string: JSON data representing the memory usage of the requested objects
    list[string]: List of types for which footprint measurements can be made (Query with no flags)
    string: Description of what a particular type will measure (Query with a 'type' flag)

Flags:
---


---
allObjects(all): boolean
    properties: create
    Ignore any specified or selected objects and measure all applicable
objects. The definition of "allObjects" will vary based on the type of
objects being measured - see the type documentation for details on
what it means for that type.
By default if no objects are selected or specified then it will behave
as though this flag were set.

---
outputFile(of): string
    properties: create
    Specify the location of a file to which the information is to be
dumped. Default will return the value from the command.  Use the
special names stdout, cout, stderr, or cerr to redirect
to the standard output or error locations.

---
type(t): string
    properties: create, query
    Specify the type of object footprint to measure. The various types are registered at
run time and can be listed by querying this flag without a value. If you query it
with a value then you get a description of what that particular type is going to
measure.
                        In query mode, this flag can accept a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dbfootprint.html 
    """


def dbmessage(flagfile: string, flaglist: boolean, flagmonitor: boolean, flagtype: string) -> None:
    """Synopsis:
---
---
 dbmessage([file=string], [list=boolean], [monitor=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dbmessage is NOT undoable, NOT queryable, and NOT editable.dbmessage


Example:
---
import maya.cmds as cmds


cmds.dbmessage( m='on' )                  Enable monitoring of all messages
cmds.dbmessage( l=True )                  Print all available messages and monitoring state
cmds.dbmessage( f='msgs.txt' )            Redirect all message output to the file "msgs.txt"
cmds.dbmessage( t='dgNodeAdded', m='on' ) Turn on monitoring for the "dgNodeAdded" message

---


Flags:
---


---
file(f): string
    properties: create
    Destination file of the message monitoring information.  Use the special names
stdout and stderr to redirect to your command window.  As
well, the special name msdev is available on NT to direct your
output to the debug tab in the output window of Developer Studio.
Default value is stdout.

---
list(l): boolean
    properties: create
    List all available message types and their current enabled status.

---
monitor(m): boolean
    properties: create
    Set the monitoring state of the message type ('on' to enable, 'off' to disable).
Returns the list of all message types being monitored after the change in state.

---
type(t): string
    properties: create
    Monitor only the messages whose name matches this keyword (default is all).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dbmessage.html 
    """


def dbpeek(flagallObjects: boolean, flagargument: string, flagcount: uint, flagevaluationGraph: boolean, flagoperation: string, flagoutputFile: string) -> int | list[string] | string:
    """Synopsis:
---
---
 dbpeek([allObjects=boolean], [argument=string], [count=uint], [evaluationGraph=boolean], [operation=string], [outputFile=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dbpeek is NOT undoable, queryable, and NOT editable.dbpeek


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
// Find the available peek operations
cmds.dbpeek( op=True, query=True )
Return: ['metadata', 'nodes', 'references', 'plugIterator'] ---


// Describe the detail of a single available operation
cmds.dbpeek( query=True, op='nodes' )
Return: '
Peek operation 'nodes':
    Normal display  will  show a count of nodes in the scene of each type.
Recognized 'argument' values:
    attributes
        Includes the attribute  count for each node as well, segregated by static, extension, and dynamic types.
    visible
        Filter the display  list to ignore any hidden or internal nodes. Default is to show all nodes.
'---


Describe the detail of a single available operation
cmds.dbpeek( query=True, op='plugIterator' )
Return: '
Peek operation 'plugIterator':
    This tests the performance of the class by iterating over all of the
    networked plugs in a plug tree.
    Suggested iteration count minimum is 1000000 for which the test machine
    measured a time of 19.234s.
This operation does not take any arguments.
'---


cmds.dbpeek( op='plugIterator', count=10000 )
Return: 'Run 10,000 loops of plug iteration over a tree of size 51, depth 4
Total time:   17.0s
Maximum time: 0.81s
Minimum time: 0.23s
Average time: 0.30s
'---

Run a performance test for 1000000 loops and store the results
cmds.dbpeek( op='plugIterator', count=1000000, outputFile='MyFile.txt' )
Return: 0 ---



cmds.loadPlugin( 'MetadataSample' )
cmds.polyPlane( name='planeLuck' )
cmds.dataStructure( asString='name=TestStructure:int32=ID )
cmds.importMetadata( asString='channel face\n stream\n TestStream\n TestStructure\n 0\n 99\n 1\n 999\n 2\n 9999\n endStream\n endChannel\n endAssociations" "planeLuckShape' )

Peek at the newly created metadata
---

cmds.dbpeek( op='metadata', argument='summary' )
Return: 'Node planeLuckShape : face( TestStream[3] )' ---


---
Return:
---


    list[string]: Query of operation yields a string array with available operations
    list[string]: Query of argument yields a string array with available argument definitions on the specified operation
    string: Query of specific operation without an output file returns a string with help information for that operation
    int: Query of specific operation with an output file dumps the help information for that operation to that file and returns the number of errors encountered

Flags:
---


---
allObjects(all): boolean
    properties: create, query
    Ignore any specified or selected objects and peek into all applicable
objects. The definition of "allObjects" will vary based on the peek
operation being performed - see the flag documentation for details on
what it means for a given operation.
By default if no objects are selected or specified then it will behave
as though this flag were set.

---
argument(a): string
    properties: create, query, multiuse
    Specify one or more arguments to be passed to the operation. The acceptable
values for the argument string are documented in the flag to which they will be
applied. If the argument itself takes a value then the value will be of the
form "argname=argvalue".
                        In query mode, this flag needs a value.

---
count(c): uint
    properties: create, query
    Specify a count to be used by the test. Different tests make different use of
the count, query the operation to find out how it interprets the value.
For example a performance test might use it as the number of iterations to run
in the test, an output operation might use it to limit the amount of output it
produces.

---
evaluationGraph(eg): boolean
    properties: create, query
    Ignore any nodes that are not explicitly part of the evaluation graph.
Usually this means nodes that are affected either directly or indirectly
by animation. May also tailor the operation to be EM-specific in the
areas where the structure of the DG differs from the structure of the
EM, for example, plug configurations.
This is a filter on the currently selected nodes, including the use of
the "allObjects" flag.

---
operation(op): string
    properties: create, query
    Specify the peeking operation to perform. The various operations are registered at
run time and can be listed by querying this flag without a value. If you
query it with a value then you get the detail values that peek operation accepts and
a description of what it does.
                        In query mode, this flag can accept a value.

---
outputFile(of): string
    properties: create, query
    Specify the location of a file to which the information is to be
dumped. Default will return the value from the command.  Use the
special names stdout and stderr to redirect to your
command window.
The special name msdev is available when debugging on Windows
to direct your output to the debug tab in the output window of Visual
Studio.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dbpeek.html 
    """


def dbtrace(flagfilter: string, flaginfo: boolean, flagkeyword: string, flagmark: boolean, flagoff: boolean, flagoutput: string, flagtimed: boolean, flagtitle: string, flagverbose: boolean) -> None:
    """Synopsis:
---
---
 dbtrace([filter=string], [info=boolean], [keyword=string], [mark=boolean], [off=boolean], [output=string], [timed=boolean], [title=string], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dbtrace is NOT undoable, queryable, and NOT editable.dbtrace
Trace Objects to affect (keyword KEY)
Optional filtering criteria (filter FILTER)
Function (off, output FILE, mark, title TITLE, timed : default operation is to enable traces)
offoutputfiltertimed


Example:
---
import maya.cmds as cmds

The default action is to turn the trace object on.  This action can be
changed using one of the -off, -output, -mark, -query, or -title.

cmds.dbtrace( off=True ) turns all active tracing off
cmds.dbtrace( k='key' )  turns on all tracing for keyword "key"
cmds.dbtrace( o='FRED' ) sends all active tracing output to the file "FRED"

Inserts a title line in all active trace destinations having keyword 'key'
cmds.dbtrace( k='key', t='This is a Title' )

Only turn on traces with keyword "key" in Transform nodes
cmds.dbtrace( k="key", f="transform" )

Show where output is going for all trace objects having keyword "fooTrace"
cmds.dbtrace( query=True, k="fooTrace", output=True )

---


Flags:
---


---
filter(f): string
    properties: create, query
    Set the filter object for these trace objects (see 'dgfilter')

---
info(i): boolean
    properties: query
    In query mode return a brief description of the trace object.

---
keyword(k): string
    properties: create, query, multiuse
    Keyword of the trace objects to affect
                        In query mode, this flag can accept a value.

---
mark(m): boolean
    properties: create
    Display a mark for all outputs of defined trace objects

---
off(): boolean
    properties: create
    Toggle the traces off.  If omitted it will turn them on.

---
output(o): string
    properties: create, query
    Destination file of the affected trace objects.  Use the special names
stdout and stderr to redirect to your command window.
The special name msdev is available on Windows to direct your
output to the debug tab in the output window of Visual Studio.

---
timed(tm): boolean
    properties: create, query
    Turn on/off timing information in the output of the specified trace objects.

---
title(t): string
    properties: create
    Display a title mark for all outputs of defined trace objects

---
verbose(v): boolean
    properties: create
    Include all traces in output and filter queries, not just those turned on.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dbtrace.html 
    """


def defaultLightListCheckBox(flagannotation: string, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagshadingGroup: name, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 defaultLightListCheckBox([annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [shadingGroup=name], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

defaultLightListCheckBox is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a window with a check box for at most 10 shading groups

cmds.window( wh=(200, 100) )
cmds.columnLayout( adj=True )
seList = cmds.ls(type='shadingEngine')
numLines = min(len(seList), 10)
for i in range(numLines):
    cmds.defaultLightListCheckBox( sg=seList[i], label=seList[i] )
cmds.showWindow()

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
shadingGroup(sg): name
    properties: create, edit
    The shading group that is to be connected/disconnected from the
defaultLightList.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/defaultLightListCheckBox.html 
    """


def defaultNavigation(flagconnectToExisting: boolean, flagcreateNew: boolean, flagdefaultAttribute: boolean, flagdefaultTraversal: boolean, flagdefaultWorkingNode: boolean, flagdelete: boolean, flagdestination: name, flagdisconnect: boolean, flagforce: boolean, flagignore: boolean, flagnavigatorDecisionString: string, flagquiet: boolean, flagrelatedNodes: boolean, flagsource: name, flagunignore: boolean) -> string:
    """Synopsis:
---
---
 defaultNavigation([connectToExisting=boolean], [createNew=boolean], [defaultAttribute=boolean], [defaultTraversal=boolean], [defaultWorkingNode=boolean], [delete=boolean], [destination=name], [disconnect=boolean], [force=boolean], [ignore=boolean], [navigatorDecisionString=string], [quiet=boolean], [relatedNodes=boolean], [source=name], [unignore=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

defaultNavigation is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Create a poly plane
cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')

This will open the Create Render Node window from which you can select a node that you want to connect to the existing lambert1.color attribute
cmds.defaultNavigation(createNew=True, destination='lambert1.color')

Select the Checker Node, you will find "checker1.outColor" is connected to "lambert1.color"

Break the connection between "checker1.outColor" and "lambert1.color" you have just established
cmds.disconnectAttr('checker1.outColor', 'lambert1.color')

Connect "checker1" to "lambert1". Only node is specified here, but the command will make a best guess.
So "checker1.outColor" and "lambert1.color" are connected
cmds.defaultNavigation(connectToExisting=True, source='checker1', destination='lambert1')

---
Return:
---


    string: or array of strings

Flags:
---


---
connectToExisting(ce): boolean
    properties: create
    Connect the destination (which is a node.attribute or simply
node) to an existing source. If the source is specified (as
node.attribute or simply as node), the command will proceed
immediately. If the source is not specified, the user will
be prompted to specify one. Once a source has been specified,
a best guess will be made about what the user is trying to
accomplish by connecting the two, based on the type of source and
type of destination. The command will connect the nodes/attributes
according to the best guess. The destination is specified using
the destination flag and the source specified using the
source flag.

---
createNew(cn): boolean
    properties: create
    Create a new node and connect it to the node.attribute specified
using the destination flag.

---
defaultAttribute(da): boolean
    properties: create
    Returns the name of the attribute to which a connectNodeToNode
would connect, given the source (attribute) and destination
(node) flags.
Returns a string.

---
defaultTraversal(dtv): boolean
    properties: create
    Returns the name of the node to which it would make the most
sense to navigate to from the destination node.attribute specified.
The destination is specified using the destination flag.
Returns a string.

---
defaultWorkingNode(dwn): boolean
    properties: create
    Returns the name of the node which the user is most likely to
want to work with if they are interested in the attributes of
the destination node.
The destination is specified using the destination flag.
Returns a string.

---
delete(delete): boolean
    properties: create
    Delete nodes with connections flowing into the node.attribute
specified by the destination flag.

---
destination(d): name
    properties: create
    Specifies an existing destination attribute for a createNew or connectToExisting.

---
disconnect(dis): boolean
    properties: create
    If used then disconnect the destination if it exists.

---
force(f): boolean
    properties: create
    If set to true, then an attempt to connect a source attribute to
a destination attribute which already has a source will cause the
existing source to be disconnected and the new source to be
connected in its place. Default value is true.

---
ignore(i): boolean
    properties: create
    Ignore any connections flowing into the node.attribute specified
by the destination flag.

---
navigatorDecisionString(nds): string
    properties: create
    This is your opportunity to pass the navigator a string that
can help it decide what behaviour to execute.

---
quiet(qt): boolean
    properties: create
    If set to true, then under no circumstances should the user be
prompted for more information. Default value is false.

---
relatedNodes(ren): boolean
    properties: create
    List nodes which are conceptually related to the node.attribute
specified by the destination. Related nodes may include,
but are not limited to, nodes which are directly or indirectly
connected to the destination.
The destination is specified using the destination flag.
Returns an array of strings.

---
source(s): name
    properties: create
    Specifies an existing source attribute for a connectToExisting.

---
unignore(u): boolean
    properties: create
    Stop ignoring any connections flowing into the node.attribute
specified by the destination flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/defaultNavigation.html 
    """


def defineDataServer(flagdevice: string, flagserver: string, flagundefine: boolean) -> None:
    """Synopsis:
---
---
 defineDataServer([device=string], [server=string], [undefine=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

defineDataServer is undoable, NOT queryable, and NOT editable.Connects to the specified data servername, creating a named device which
then can be attached to device handlers.

When the device is defined, it queries queries the server for data axis
information.  The "CapChannels" present are represented as axis in form
"channelName"."usage" for scalar channels and "channelName"."component"
for compound channels. See listInputDeviceAxes to list axis names.

Note that undoing 
defineDataServer -d "myDevice" -s "myServer"

does not break the connection with the data server until it cannot be
redone.  Executing any other command (sphere for example) will cause
this to occur.  Similarly, the command 
defineDataServer -d "myDevice" -u

does not break the connection with the data server until it cannot be
undone.  Either flushUndo, or the 'defineDataServer' command falling"
off the end of the undo queue causes this to occur, and the connection.
to be broken.

No return value.




Example:
---
import maya.cmds as cmds

cmds.defineDataServer( s='ultratrak_server', d='melvin' )

Connects to the ultratrak_server running on the localhost and gives it
the name "melvin"

cmds.defineDataServer( s='mocap_lab:5200', d='labFlock' )

Creates a device called "labFlock" which connects to the server running
on host "mocap_lab" at port "5200".

cmds.defineDataServer( undefine=True, d='labFlock' )

Delete the device "labFlock" closing the connection with the server
specified when it was created.

---


Flags:
---


---
device(d): string
    properties: create
    specified the device name to be given to the server connection.
device name must be unique or the command fails.

---
server(s): string
    properties: create
    specifies the name of the server with which the define
device connects, and can be specifiied in two ways


name -- the name of the server socket
Server names of the form name connect to the
server socket on the localhost corresponding to
name.  If name does not begin with "/",
then /tmp/name is used. This is the default behavior
of most servers. If name begins with "/",
name denotes the full path to the socket. 
host:service - a udp service
on the specified host.
The service can be any one of a "udp service name,"
a "port number," or a named service of "tcpmux," and they are
found in that order. If
host is omitted, the localhost is used. 

In any case, if the server cannot be found, the device is not
defined (created) and the command fails.

---
undefine(u): boolean
    properties: create
    undefines (destroys) the dataServer device, closing the connection
with the server.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/defineDataServer.html 
    """


def defineVirtualDevice(flagaxis: int, flagchannel: string, flagclear: boolean, flagcreate: boolean, flagdevice: string, flagparent: string, flagundefine: boolean, flagusage: string) -> None:
    """Synopsis:
---
---
 defineVirtualDevice([axis=int], [channel=string], [clear=boolean], [create=boolean], [device=string], [parent=string], [undefine=boolean], [usage=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

defineVirtualDevice is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

   Create a virtual clock and read in some data.
cmds.defineVirtualDevice( create=True )
cmds.defineVirtualDevice( channel='seconds', usage='rotZ', axis=2 )
cmds.defineVirtualDevice( channel='minutes', usage='rotZ', axis=1 )
cmds.defineVirtualDevice( channel='hours', usage='rotZ', axis=0 )
cmds.defineVirtualDevice( device='virtualClock' )
cmds.readTake( device='virtualClock', take='clock.mov' )

   Undefine the virtualClock
cmds.defineVirtualDevice( device='virtualClock', undefine=True )

   Create a body device.
cmds.defineVirtualDevice( create=True )
cmds.defineVirtualDevice( channel='pelvis', usage='posRot' )
cmds.defineVirtualDevice( channel='back', usage='posRot' )
cmds.defineVirtualDevice( channel='head', usage='posRot' )
cmds.defineVirtualDevice( device='body' )

   Explicitly order the axis of the device. The created device is
   the same as the above body device.
cmds.defineVirtualDevice( create=True )
cmds.defineVirtualDevice( channel='head', usage='posRot', axis=12 )
cmds.defineVirtualDevice( channel='back', usage='posRot', axis=6 )
cmds.defineVirtualDevice( channel='pelvis', usage='posRot', axis=0 )
cmds.defineVirtualDevice( device='body' )

---


Flags:
---


---
axis(ax): int
    properties: create
    Specifies the axis number of the channel. All children have their
axis number determined by their parent's axis number and the width
of the parent channel. If this flag is not used, the order of the
channel determines the axis number.

---
channel(c): string
    properties: create
    After a -create is started, channels may be added to the device
definition. The channel string wil be the name of the channel
being added to the device. The -channel flag must also be
accompanied by the -usage flag and optionally by the -axis flag.

---
clear(cl): boolean
    properties: create
    The -clear option will end a device definition and throw away
any defined channels.

---
create(cr): boolean
    properties: create
    Start defining a virtual device. If a device is currently being
defined, the -create flag will produce an error.

---
device(d): string
    properties: create
    The -device flag ends the device definition. All of the channels
between the -create flag and the -device flag are added to
the specified device. If that device already exists, the command
will fail and the device should be redefined with another device
name. To see the currently defined devices, use the listInputDevices
command. The -device flag is also used with -undefine to undefine a
virtual device.

---
parent(p): string
    properties: create
    Specified the parent channel of the channel being defined. If the
channel does not exist, or is an incompatible type, the command
will fail.

---
undefine(u): boolean
    properties: create
    Undefines the device specified with the -device flag.

---
usage(use): string
    properties: create
    The -usage option is required for every -channel flag. It
describes what usage type the defined channel is. The usage
types are:


unknownscalar

posrot
posRotquaternionposQuaternion

rotXYZrotYZXrotZXY
rotXZYrotYXZrotZYX

posRotXYZposRotYZXposRotZXY
posRotXZYposRotXZYposRotZYX

posXposYposZrotX
rotYrotZ

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/defineVirtualDevice.html 
    """


def deformableShape(flagchain: boolean, flagcreateOriginalGeometry: boolean, flagcreateTweakNode: boolean, flagcreateUpstreamTagInjectionNode: boolean, flagdeformShapeInAttr: boolean, flagdeformShapeOutAttr: boolean, flagfrontOfChain: boolean, flaglocalShapeInAttr: boolean, flaglocalShapeOutAttr: boolean, flagnodeChain: boolean, flagoriginalGeometry: boolean, flagoutputPlugChain: boolean, flagplugChain: boolean, flagsupportsComponentTags: boolean, flagtagInjectionList: boolean, flagtagInjectionNode: boolean, flagtweakNode: boolean, flagupstreamTagInjectionNode: boolean, flagworldShapeOutAttr: boolean) -> None:
    """Synopsis:
---
---
 deformableShape(
[objects...]
    , [chain=boolean], [createOriginalGeometry=boolean], [createTweakNode=boolean], [createUpstreamTagInjectionNode=boolean], [deformShapeInAttr=boolean], [deformShapeOutAttr=boolean], [frontOfChain=boolean], [localShapeInAttr=boolean], [localShapeOutAttr=boolean], [nodeChain=boolean], [originalGeometry=boolean], [outputPlugChain=boolean], [plugChain=boolean], [supportsComponentTags=boolean], [tagInjectionList=boolean], [tagInjectionNode=boolean], [tweakNode=boolean], [upstreamTagInjectionNode=boolean], [worldShapeOutAttr=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deformableShape is undoable, NOT queryable, and NOT editable.
If no shapes are specified on the command then the curently selected
shapes are used.




Example:
---
import maya.cmds as cmds

    Create an original geometry if it does not exist
    cmds.deformableShape('ball', cog=True)

    import maya.cmds as cmds

    cmds.polyCylinder(n="myGeo", r=1, h=6, sx=4, sy=5, sz=1)[0]
    cmds.select(['myGeo.vtx[12:23]', 'myGeo.vtx[25]'])

    clusterNode, clusterHandle = cmds.cluster()
    cmds.move(1.0, 0, 0, clusterHandle, absolute=True)

    Get the node chain leading up to the shape
    cmds.deformableShape('myGeoShape', nch=True)
    Result: [u'polyCylinder1', u'myGeoShapeOrig', u'groupParts2', u'tweak1', u'cluster1GroupParts', u'cluster1', u'myGeoShape'] ---


    Get the deformer chain leading up to the shape
    cmds.deformableShape('myGeoShape', ch=True)
    Result: [u'tweak1', u'cluster1'] ---


    Get the plug chain leading up to the shape
    cmds.deformableShape('myGeoShape', pch=True)
    Result: [u'polyCylinder1.output', u'myGeoShapeOrig.inMesh', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.inputGeometry', u'groupParts2.outputGeometry', u'tweak1.input[0].inputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.inputGeometry', u'cluster1GroupParts.outputGeometry', u'cluster1.input[0].inputGeometry', u'cluster1.outputGeometry[0]', u'myGeoShape.inMesh'] ---


    Get the output plug chain leading up to the shape
    cmds.deformableShape('myGeoShape', och=True)
    Result: [u'polyCylinder1.output', u'myGeoShapeOrig.worldMesh[0]', u'groupParts2.outputGeometry', u'tweak1.outputGeometry[0]', u'cluster1GroupParts.outputGeometry', u'cluster1.outputGeometry[0]'] ---


---


Flags:
---


---
chain(ch): boolean
    properties: create
    This flag will return the list of deformers that deformer the specified shapes

---
createOriginalGeometry(cog): boolean
    properties: create
    This creates an original geometry for the shape if it does not exist yet.

---
createTweakNode(ctw): boolean
    properties: create
    This creates a traditional tweak node if one did not exist yet.

---
createUpstreamTagInjectionNode(cti): boolean
    properties: create
    This creates an upstream component tag injection node if an editable one does not exist yet.

---
deformShapeInAttr(dsi): boolean
    properties: create
    Returns the name of deform shape in attribute

---
deformShapeOutAttr(dso): boolean
    properties: create
    Returns the name of deform shape out attribute

---
frontOfChain(foc): boolean
    properties: create
    This flag will return the name of the plug on a shape node at the front end of
the deformation chain. This can return an empty plug when none exists.

---
localShapeInAttr(lsi): boolean
    properties: create
    Returns the name of local shape in attribute

---
localShapeOutAttr(lso): boolean
    properties: create
    Returns the name of local shape out attribute

---
nodeChain(nch): boolean
    properties: create
    This flag will return the list of nodes through which the geometry passes to get to this shape

---
originalGeometry(og): boolean
    properties: create
    This flag will return the name of a plug on a node in the deformation chain
(likely at the front end) that is the best candidate to be used as the
originalGeometry. This can return an empty plug when none exists.

---
outputPlugChain(och): boolean
    properties: create
    This flag will return the list of output plugs leading to the shape

---
plugChain(pch): boolean
    properties: create
    This flag will return the list of plugs leading to the shape (both input and output plugs)

---
supportsComponentTags(sct): boolean
    properties: create
    Returns whether the shape supports component tags

---
tagInjectionList(til): boolean
    properties: create
    This flag will return the list of nodes which are non-procedural componentTag injection nodes

---
tagInjectionNode(ti): boolean
    properties: create
    This flag will return the name of the non-referenced component tag injection node as high
up in the deformation chain as possible. This can be the same as the input shape or an
empty string when none exists.

---
tweakNode(tw): boolean
    properties: create
    This flag will return the name of the tweak node in the deformation chain.
This can return an empty string when none exists.

---
upstreamTagInjectionNode(uti): boolean
    properties: create
    This flag will return the name of the non-referenced component tag injection node most
upstream from (but not including) the input shape.
This can be an empty string when none exists. If so, one can be created using the
cti/createUpstreamTagInjectionNode flag.

---
worldShapeOutAttr(wso): boolean
    properties: create
    Returns the name of world shape out attribute

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deformableShape.html 
    """


def deformer(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flagname: string, flagparallel: boolean, flagprune: boolean, flagremove: boolean, flagselectedComponents: boolean, flagsplit: boolean, flagtype: string, flaguseComponentTags: boolean) -> list[string]:
    """Synopsis:
---
---
 deformer(
selectionList
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [deformerTools=boolean], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string], [parallel=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean], [split=boolean], [type=string], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deformer is undoable, queryable, and editable.
This command creates a deformer node and connects it to a deformation chain.
If the deformer does not already exist, it is created. If the deformer already
exists, the command lets you modify parameters on the named deformer.
Unlike commands for specialized deformers, this command does not create or manage
deformer-specific setups. Using this command allows deformation chains to be
managed in a more general manner.




Example:
---
import maya.cmds as cmds

Select the geometries that you'd like to deform,
and use the deformer command as follows. For example, to deform a
cylinder with a deltaMush:
---

cmds.cylinder( ax=(0, 1, 0), r=1, hr=10, d=3, s=8, nsp=20, ch=1 )
cmds.select( 'nurbsCylinder1', r=True )
cmds.deformer( type="deltaMush" )

To query the membership of the deformer
---

cmds.deformer( 'deltaMush1',q=True, g=True )

To add additional geometries from your deformer, type:
---

cmds.select( 'nurbsCylinder1', r=True )
cmds.duplicate()
Result: nurbsCylinder2 ---

cmds.move( -2.749017, 0, 0, r=True )
cmds.deformer( 'deltaMush1', e=True, g='nurbsCylinder2' )

To remove a geometry from your deformer, type:
---

cmds.deformer( 'deltaMush1', e=True, rm=True, g='nurbsCylinder2' )

To query the components and the selected components used by the deformer
cmds.polyCylinder(r=1, h=6, sx=6, sy=1, sz=1)
cmds.select(['pCylinder1.vtx[6:11]', 'pCylinder1.vtx[13] '], r=True)
cmds.cluster()

cmds.select(['pCylinder1.vtx[4:5]', 'pCylinder1.vtx[10:11] '], r=True)
cmds.deformer('cluster1', q=True, cmp=True)
Result: ['pCylinder1.vtx[6:11]', 'pCylinder1.vtx[13]'] ---

cmds.deformer('cluster1', q=True, cms=True)
Result: ['pCylinder1.vtx[10:11]'] ---


---
Return:
---


    list[string]: Name of the algorithm node created/edited.

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
type(typ): string
    properties: create
    Specify the type of deformer to create. This flag is
required in create mode. Typically the type should specify a loaded
plugin deformer. This command should typically not be used to create
one of the standard deformers
such as sculpt, lattice, blendShape, wire and cluster, since they have
their own customized commands which perform useful specialized functionality.

---
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deformer.html 
    """


def deformerEvaluator(flagactive: boolean, flagallowDownloadRejections: boolean, flagallowDownloads: boolean, flagasNodeName: boolean, flagasText: boolean, flagdeformerChain: boolean, flagdeformers: boolean, flagdumpInfo: boolean, flagdumpOutliner: boolean, flaggpuBlockPolicy: string, flagisOpenCLValid: boolean, flaglimitMinimumVerts: boolean, flaglist: boolean, flagmembers: boolean, flagmeshes: boolean, flagmessage: boolean, flagminimumVerts: int, flagnodeInfo: boolean, flagnodeStatus: boolean, flagomitPassthroughs: boolean, flagoutlinerHash: boolean, flagpartition: boolean, flagpurge: boolean, flagreuseMode: tuple[string, string], flagverbose: boolean) -> list[string]:
    """Synopsis:
---
---
 deformerEvaluator([active=boolean], [allowDownloadRejections=boolean], [allowDownloads=boolean], [asNodeName=boolean], [asText=boolean], [deformerChain=boolean], [deformers=boolean], [dumpInfo=boolean], [dumpOutliner=boolean], [gpuBlockPolicy=string], [isOpenCLValid=boolean], [limitMinimumVerts=boolean], [list=boolean], [members=boolean], [meshes=boolean], [message=boolean], [minimumVerts=int], [nodeInfo=boolean], [nodeStatus=boolean], [omitPassthroughs=boolean], [outlinerHash=boolean], [partition=boolean], [purge=boolean], [reuseMode=[string, string]], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deformerEvaluator is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


Set the reuse mode for deformers and sinks
cmds.deformerEvaluator(ru=("always", "never"))

List all registered GPU deformers.
cmds.deformerEvaluator( deformers=True )

List all nodes that are on the GPU
cmds.deformerEvaluator( ls=True )

List all meshes that are on the GPU
cmds.deformerEvaluator( ls=True, m=True )

List information about selected nodes
cmds.deformerEvaluator( )

List information about selected meshes
cmds.deformerEvaluator( m=True )

List deformation chain information about selected meshes
cmds.deformerEvaluator( dch=True )

List all the deformation chains of all meshes that are active on the GPU
cmds.deformerEvaluator( dch=True, act=True )

List the names of the nodes that are in the same cluster(s) as the specified nodes.
cmds.deformerEvaluator( mbr=True )

List the messages associated with the selected nodes.
cmds.deformerEvaluator( msg=True )

Return all active clusters in JSON format.
cmds.deformerEvaluator(query=True, dumpInfo=True, opt=True);

---
Return:
---


    list[string]: the debug information when query mode is used.

Flags:
---


---
active(act): boolean
    properties: create, query
    Modifier to specify that instead of the current selection all active
        nodes on the GPU should be queried.

---
allowDownloadRejections(adr): boolean
    properties: create, query
    Specifies whether potentially rejecting parts of the graph that depend on GPU downloads is allowed.

---
allowDownloads(adl): boolean
    properties: create, query
    Specifies whether downloads from GPU to CPU are allowed.

---
asNodeName(nm): boolean
    properties: create, query
    Modifier to specify that when a certain node attribute is queried it should
        return the name of the node instead. This is useful when querying multiple
        nodes at a time and the results need to be lined up with the node names.

---
asText(txt): boolean
    properties: create, query
    Modifier to specify that when the node state is queried the state should
    be returned as text instead of a numeric code

---
deformerChain(dch): boolean
    properties: create, query
    Query the state of the nodes in the deformation chain of the specified meshes.

---
deformers(d): boolean
    properties: create, query
    Return a list of all currently registered GPU deformers.

---
dumpInfo(di): boolean
    properties: create, query
    List information about all supported deformation chains as JSON.

---
dumpOutliner(dol): boolean
    properties: create, query
    List information about all supported nodes as a python object.

---
gpuBlockPolicy(gbp): string
    properties: create, query
    Specifies the gpu blocking policy for a node.
    Currently, we support the following blocking modes:
    "off" "on" "group" "upstream" "upstreamExcl" "upstreamMesh" "downstream" "downstreamExcl" "groupDownload"
    Default is "off" which means the node causes no blocking of the GPU.

---
isOpenCLValid(clv): boolean
    properties: create, query
    Specifies whether OpenCL is valid/initialized.

---
limitMinimumVerts(lmv): boolean
    properties: create, query
    Specifies whether the limit on the minimum vert count of the geometry is used or not. The system configuration
determines a certain minimum size for geometries to be allowed on GPU.
When this flag is on this limit is obeyed. When this flag is off this limit is ignored.
This is only used for debugging purposes and is not saved to the file or any preferences.

---
list(ls): boolean
    properties: create, query
    Return a list of nodes that are currently active on the GPU.

---
members(mbr): boolean
    properties: create, query
    Return the names of the nodes that are in the same cluster as the specified nodes.

---
meshes(m): boolean
    properties: create, query
    Modifier to specify that only meshes need to be queried.

---
message(msg): boolean
    properties: create, query
    Return the messages associated with the specified nodes.

---
minimumVerts(mnv): int
    properties: create, query
    Set the minimum vert count under which the geometry will not be allowed on the GPU (unless in a network
with qualifying geometries).
This is only used for debugging purposes and is not saved to the file or any preferences.

---
nodeInfo(ni): boolean
    properties: create, query
    List all the information gathered during partitioning about the selected nodes

---
nodeStatus(ns): boolean
    properties: create, query
    Return the state of the node on the GPU. When queried it will return
        a numeric code unless the asText flag is used as well.

---
omitPassthroughs(opt): boolean
    properties: create, query
    Whether opassthrough nodes like groupParts nodes should be ommitted from the dumped info or not

---
outlinerHash(olh): boolean
    properties: create, query
    Return the unique hash value for the current outliner state.

---
partition(prt): boolean
    properties: create, query
    Flag to force a repartition (for debug purposes only)

---
purge(prg): boolean
    properties: create, query
    Purge the data of any unused gpu nodes

---
reuseMode(ru): [string, string]
    properties: create, query
    Specifies how the GPU nodes can be reused when repartitioning. A mode has to be specified for each of the three
node types (deformer and displayMesh). A mode for a node type is one of the following:

 Mode "never" means they will never be reused 
 Mode "immediate" means that nodes will remain in memory during repartitioning but the ones that are not in use immediatley after that will be purged 
 Mode "always" means that all nodes will remain in memory during and after repartitioning for later reuse

---
verbose(v): boolean
    properties: create, query
    Print more verbose information of other flags.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deformerEvaluator.html 
    """


def deformerWeights(flagattribute: string, flagdefaultValue: float, flagdeformer: string, flagexport: boolean, flagformat: string, flagignoreName: boolean, flagim: boolean, flagmethod: string, flagpath: string, flagpositionTolerance: float, flagremap: string, flagshape: string, flagskip: string, flagvertexConnections: boolean, flagweightPrecision: uint, flagweightTolerance: float, flagworldSpace: boolean) -> STRING:
    """Synopsis:
---
---
 deformerWeights([attribute=string], [defaultValue=float], [deformer=string], [export=boolean], [format=string], [ignoreName=boolean], [im=boolean], [method=string], [path=string], [positionTolerance=float], [remap=string], [shape=string], [skip=string], [vertexConnections=boolean], [weightPrecision=uint], [weightTolerance=float], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deformerWeights is undoable, queryable, and editable.










Example:
---
import maya.cmds as cmds


import maya.cmds as cmds

def createRig(nsp='nsp1', res=5):
    Create a plane with two clusters in a namespace.
    ---

    cmds.polyPlane( ch=1, w=10, h=10, sx=res, sy=res, ax=(0,1,0), name='%s:myShape'%nsp )
    cmds.cluster('%s:myShape'%nsp, name='%s:clusterA'%nsp)
    cmds.cluster('%s:myShape'%nsp, name='%s:clusterB'%nsp)

---
--------------------------------------------------------------------
Create the setup
---
--------------------------------------------------------------------

Clear file.
cmds.file( f=True,new=True )

Create plane and two clusters.
createRig(nsp='nsp1')

Modify some weights on clusterA.
cmds.select( ['nsp1:myShape.vtx[6:11]'])
cmds.percent( 'nsp1:clusterA', v=0.5 )

Modify some weights on clusterB.
---

cmds.select( ['nsp1:myShape.vtx[0:2]','nsp1:myShape.vtx[6:8]','nsp1:myShape.vtx[12:14]'])
cmds.percent( 'nsp1:clusterB', v=0.3 )


---
--------------------------------------------------------------------
Export the weights in a variety of different ways
---
--------------------------------------------------------------------

Write cluster A weights.
---

cmds.deformerWeights ('clusterA.xml', ex=True, deformer='nsp1:clusterA')

Write cluster B weights, but do not write values of 1.0.
---

cmds.deformerWeights ('clusterB.xml', ex=True, deformer='nsp1:clusterB', dv=1.0)

Write cluster A and B weights at the same time.
---

cmds.deformerWeights ('clusterAB.xml', ex=True, deformer=['nsp1:clusterA', 'nsp1:clusterB'])

Export weights for all deformers on the shape, including vertex connections.
---

cmds.deformerWeights ('shape_all.xml', ex=True, sh='nsp1:myShape', vc=True)

Same as above skipping deformers matching '*B'.
---

cmds.deformerWeights ('shape_NotB.xml', ex=True, sh='nsp1:myShape', vc=True, sk='*B')

Export weights and attributes.
---

attributes = ['envelope', 'percentResolution', 'usePartialResolution']
cmds.deformerWeights ('shape_all_attr.xml',ex=True, sh='nsp1:myShape', vc=True, at=attributes)

Export name space nsp1: in scene to nsp2: in xml.
cmds.deformerWeights ('shape_all_nsp2.xml', ex=True, sh='nsp1:myShape', vc=True, remap='nsp1:(.*);nsp2:$1')


---
--------------------------------------------------------------------
Import the weights
---
--------------------------------------------------------------------

Read both cluster's weight files separately.
cmds.deformerWeights('clusterA.xml', im=True, sh='nsp1:myShape', deformer='nsp1:clusterA')
cmds.deformerWeights('clusterB.xml', im=True, sh='nsp1:myShape', deformer='nsp1:clusterB')

Read both deformers from the single file.
cmds.deformerWeights('shape_all.xml', im=True, sh='nsp1:myShape', deformer=['nsp1:clusterA', 'nsp1:clusterB'])

Alternative way of reading both deformers.
cmds.deformerWeights('shape_all.xml', im=True, deformer=['nsp1:clusterA', 'nsp1:clusterB'])

Read clusterA from the file containing both clusters.
cmds.deformerWeights('shape_all.xml', im=True, deformer='nsp1:clusterA')

---

Create the same rig in a different namespace.
---

createRig(nsp='nsp2')

Import weights from file that remapped the namespace on export.
cmds.deformerWeights('shape_all_nsp2.xml', im=True, sh='nsp2:myShape', deformer=['nsp2:clusterA', 'nsp2:clusterB'])

Import weights from file containing a different namespace, and remap the namespace on import.
cmds.deformerWeights('shape_all.xml', im=True, sh='nsp2:myShape', deformer=['nsp2:clusterA', 'nsp2:clusterB'], remap='nsp1:(.*);nsp2:$1')

---

Create similar rig with different resolution (topology) in a different namespace.
---

createRig(nsp='nsp3', res=8)

Import weights from file, remap the namespace on import, and use the barycentric method to remap the weight values.
cmds.deformerWeights('shape_all.xml', im=True, sh='nsp3:myShape', deformer=['nsp3:clusterA', 'nsp3:clusterB'], remap='nsp1:(.*);nsp3:$1', method='barycentric')

---
Return:
---


    STRING: path to the file imported/exported, if successful

Flags:
---


---
attribute(at): string
    properties: create, query, edit, multiuse
    Specify the long name of deformer attribute that should be imported/exported along with the deformerWeights. i.e. -at "envelope" -at "skinningMethod" etc.. No warning or error is given if a specified attribute does not exist on a particular deformer, making it possible to use this command with multiple deformers without aborting or slowing down the import/export process.  Currently supports numeric attributes and matrix attributes

---
defaultValue(dv): float
    properties: create, query, edit
    Manually set the default value. Default values are values that are not written to file. For example, for blendShapes the default value is automatically set to 1.0 and these values are not written to disk. For skinClusters the value is 0.0. If all weights should be forced to be written to disk, set a defaultValue = -1.0.

---
deformer(df): string
    properties: create, query, edit, multiuse
    Specify the deformer whose weights should be exported or imported. If a pattern is supplied for the deformer
name (i.e: cluster*), only the first deformer that matches the pattern will be imported/exported unless used
in conjunction with the -skip option

---
export(ex): boolean
    properties: create, query, edit
    Export the given deformer

---
format(fm): string
    properties: create, query, edit
    Specify either "XML" or "JSON" as the file extension to save as.

---
ignoreName(ig): boolean
    properties: create, query, edit
    Ignore the names of the layers on import, just use the order of the layers instead. This can be used when
joint names have been changed. Leaving it on only name that match on import will be write to the deformer.

---
im(im): boolean
    properties: create, query, edit
    Import weights to the specified deformer. See the method flag for details
on how the weights will be mapped to the destination deformer.

---
method(m): string
    properties: create, query, edit
    Specify the method used to map the weight during import. Valid values are:
"index", "nearest", "barycentric", "bilinear" and "over". The "index" method
uses the vertex index to map the weights onto the object. This is most useful
when the destination object shares the same topology as the exported data.
The "nearest" method finds the nearest vertex in the imported data set and
sets the weight value to that value. This is best used when mapping a higher
resolution mesh to a lower resolution. The "barycentric" and "bilinear" methods
are only supported with polygon mesh exported with -vc/vertexConnections flag.
The "barycentric" method finds the nearest triangle of the input geometry and
rescales the weights at the triangle vertices according to the barycentric
weights to each vertex of the nearest triangle. The "bilinear" method finds the
nearest convex quad of the input geometry and rescales the weights at the quad
vertices according to the bilinear weights to each vertex of the nearest convex
quad. For non-quad polygon, the "bilinear" method will fall back to "barycentric"
method. The "over" method is similar to the "index" method but the weights on the
destination mesh are not cleared prior to mapping, so that unmatched indices
keep their weights intact.

---
path(p): string
    properties: create, query, edit
    The path to the given file. Default to the current project.

---
positionTolerance(pt): float
    properties: create, query, edit
    The position tolerance is used to determine the radius of search for the nearest method. This flag is only
used with import.
Defaults to a huge number.

---
remap(r): string
    properties: create, query, edit, multiuse
    Remap maps source regular expression to destination format. It maps any name that matches the regular expression (before the semi-colon) to the expression format (after the semi-colon).
For example, -remap "test:(.*);$1" will rename all items in the test namespace to the global namespace. Accepts $1, $2, .., $9 as pattern holders in the expression format.
Remap flag must be used together with import or export. When working with import, the name of the object from the xml file matching the regular expression is remapped to object in scene. When working with export, the name of the object from the scene matching the regular expression is remapped to object in xml file.

---
shape(sh): string
    properties: create, query, edit, multiuse
    Specify the source shape. Export will write out all the deformers on the shape node into one file.
If a pattern is supplied for the shape name (i.e: pCylinder*), only the first shape that matches the pattern will
be imported/exported unless used in conjunction with the -skip option.

---
skip(sk): string
    properties: create, query, edit, multiuse
    Skip any deformer, shape, or layer that whose name matches the given regular expression string

---
vertexConnections(vc): boolean
    properties: create, query, edit
    Export vertex connection information, which is required for -m/-method "barycentric" and "bilinear". The flag is only used with -ex/-export flag. The vertex connection information is automatically loaded during import if available in xml file.

---
weightPrecision(wp): uint
    properties: create, query, edit
    Sets the output decimal precision for exported weights. The default value is 3.

---
weightTolerance(wt): float
    properties: create, query, edit
    The weight tolerance is used to decide if a given weight value is close enough to the default value that it does not need to be included. This flag is only used with export. The default value is .001.

---
worldSpace(ws): boolean
    properties: create, query, edit
    For spatially based association methods (nearest), the position should be based on the world space position
rather then the local object space.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deformerWeights.html 
    """


def delete(flagall: boolean, flagattribute: string, flagchannels: boolean, flagconstraints: boolean, flagconstructionHistory: boolean, flagcontrolPoints: boolean, flagexpressions: boolean, flaghierarchy: string, flaginputConnectionsAndNodes: boolean, flagmotionPaths: boolean, flagshape: boolean, flagstaticChannels: boolean, flagtimeAnimationCurves: boolean, flagunitlessAnimationCurves: boolean) -> None:
    """Synopsis:
---
---
 delete(
objects
    , [all=boolean], [attribute=string], [channels=boolean], [constraints=boolean], [constructionHistory=boolean], [controlPoints=boolean], [expressions=boolean], [hierarchy=string], [inputConnectionsAndNodes=boolean], [motionPaths=boolean], [shape=boolean], [staticChannels=boolean], [timeAnimationCurves=boolean], [unitlessAnimationCurves=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

delete is undoable, NOT queryable, and NOT editable.
At times, more than just specified items will be deleted.  For
example, deleting two CVs in the same "row" on a NURBS surface
will delete the whole row.




Example:
---
import maya.cmds as cmds

To delete selected objects use:
cmds.delete()

To delete a few specific objects like surfaceShape1, surface1 and
paramCurve1 use:
cmds.delete( 'surfaceShape1', 'surface1', 'paramCurve1' )

To delete all channels in the scene:
cmds.delete( all=True, c=True )

To delete static channels connected to selected nodes:
cmds.delete( sc=True )

To delete motion path nodes connected to selected nodes:
cmds.delete( mp=True )

To delete all expressions in the scene:
cmds.delete( all=True, e=True )

To delete selected constraints and constraints attached to selected nodes:
cmds.delete( cn=True )

Notes:

The at, h, s and cp flags only apply when either c/channels
or sc/staticChannels or e/expressions options are specified.

---


Flags:
---


---
all(all): boolean
    properties: create
    Remove all objects of specified kind, in the scene. This flag
is to be used in conjunction with the following flags.

---
attribute(at): string
    properties: create, multiuse
    List of attributes to select
      In query mode, this flag needs a value.

---
channels(c): boolean
    properties: create
    Remove animation channels in the scene. Either all channels
can be removed, or the scope can be narrowed down by specifying
some of the above mentioned options.

---
constraints(cn): boolean
    properties: create
    Remove selected constraints and constraints attached to the
selected nodes, or remove all constraints in the scene.

---
constructionHistory(ch): boolean
    properties: create
    Remove the construction history on the objects specified or
selected.

---
controlPoints(cp): boolean
    properties: create
    This flag explicitly specifies whether or not to include the
control points of a shape (see "-s" flag) in the list of attributes.
Default: false.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
expressions(e): boolean
    properties: create
    Remove expressions in the scene. Either all expressions
can be removed, or the scope can be narrowed down by specifying
some of the above mentioned options.

---
hierarchy(hi): string
    properties: create
    Hierarchy expansion options.  Valid values are "above,"
"below," "both," and "none." (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
inputConnectionsAndNodes(icn): boolean
    properties: create
    Break input connection to specified attribute and delete all
unconnected nodes that are left behind. The graph will be
traversed until a node that cannot be deleted is encountered.

---
motionPaths(mp): boolean
    properties: create
    Remove motion paths in the scene. Either all
motion paths can be removed, or the scope can be narrowed down
by specifying some of the above mentioned options.

---
shape(s): boolean
    properties: create
    Consider attributes of shapes below transforms as well,
except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)
In query mode, this flag needs a value.

---
staticChannels(sc): boolean
    properties: create
    Remove static animation channels in the scene. Either all
static channels can be removed, or the scope can be narrowed down
by specifying some of the above mentioned options.

---
timeAnimationCurves(tac): boolean
    properties: create
    Modifies the -c/channels and -sc/staticChannels flags.
When true, only channels connected to time-input
animation curves (for instance, those created by
'setKeyframe' will be deleted.  When false, no
time-input animation curves will be deleted.
Default: true.

---
unitlessAnimationCurves(uac): boolean
    properties: create
    Modifies the -c/channels and -sc/staticChannels flags.
When true, only channels connected to
unitless-input animation curves (for instance,
those created by 'setDrivenKeyframe' will be
deleted.  When false, no unitless-input
animation curves will be deleted.  Default:
true.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/delete.html 
    """


def deleteAttr(flagattribute: string) -> None:
    """Synopsis:
---
---
 deleteAttr(
node...|attribute...
    , [attribute=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deleteAttr is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.createNode( 'planet', n='mars' )
cmds.addAttr( ln='martians', sn='mr', at='double' )
cmds.addAttr( ln='greenMen', sn='gm', at='double' )

Delete an attribute named mr/martians.
cmds.deleteAttr( 'mars', at='mr' )

Alternative syntax
cmds.deleteAttr( 'mars.greenMen' )

Query for the list of dynamic attributes.
cmds.deleteAttr( 'mars', q=True )

---


Flags:
---


---
attribute(at): string
    properties: create
    Specify either the long or short name of the attribute.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deleteAttr.html 
    """


def deleteAttrPattern(flagallPatterns: boolean, flagpatternName: string, flagpatternType: string) -> string:
    """Synopsis:
---
---
 deleteAttrPattern([allPatterns=boolean], [patternName=string], [patternType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deleteAttrPattern is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.deleteAttrPattern( patternType="xmlPattern" )
// Result: [myXMLPattern, myOtherXMLPattern] //

cmds.deleteAttrPattern( patternName="myJSONPattern" )
// Result: myJSONPattern //

---
Return:
---


    string: Name(s) of deleted pattern(s)

Flags:
---


---
allPatterns(all): boolean
    properties: create
    If specified it means delete all known attribute patterns.

---
patternName(pn): string
    properties: create
    The name of the pattern to be deleted.

---
patternType(pt): string
    properties: create
    Delete all patterns of the given type.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deleteAttrPattern.html 
    """


def deleteExtension(flagattribute: string, flagforceDelete: boolean, flagnodeType: string) -> int:
    """Synopsis:
---
---
 deleteExtension([attribute=string], [forceDelete=boolean], [nodeType=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deleteExtension is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
cmds.createNode( 'planet', name='jupiter' )
cmds.createNode( 'planet', name='mars' )
cmds.setAttr( 'mars.mr', 35 )

Delete an extension attribute named mr/martians.
Only returns 1 since the planet node 'jupiter'
does not have a non-default value on the extension.
cmds.deleteExtension( nodeType='planet', forceDelete=True, attribute='martians' )
Return: 1 //
The attribute is gone since it was forced out
cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
Return: 0 //

Re-add and delete the extension again, forcing the
attribute to remain if non-default values exist.
cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
cmds.setAttr( 'mars.mr', 35 )

cmds.deleteExtension( nodeType='planet', forceDelete=False, attribute='mr' )
Return: 0 //

The attribute still exists since it had some non-default values
cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
Return: 1 //
cmds.attributeQuery( name='jupiter', attribute='mr', query=True, exists=True )
Return: 1 //

---
Return:
---


    int: Number of nodes with altered data after the delete

Flags:
---


---
attribute(at): string
    properties: create
    Specify either the long or short name of the attribute.

---
forceDelete(fd): boolean
    properties: create
    If this flag is set and turned ON then data values for the extension
attributes are all deleted without confirmation. If it's set and turned
OFF then any extension attributes that have non-default values set on any
node will remain in place. If this flag is not set at all then the user
will be asked if they wish to preserve non-default values on this
attribute.

---
nodeType(nt): string
    properties: create
    The name of the node type.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deleteExtension.html 
    """


def deleteUI(flagcollection: boolean, flagcontrol: boolean, flageditor: boolean, flaglayout: boolean, flagmenu: boolean, flagmenuItem: boolean, flagpanel: boolean, flagpanelConfig: boolean, flagradioMenuItemCollection: boolean, flagtoolContext: boolean, flaguiTemplate: boolean, flagwindow: boolean) -> None:
    """Synopsis:
---
---
 deleteUI(
string [string...]
    , [collection=boolean], [control=boolean], [editor=boolean], [layout=boolean], [menu=boolean], [menuItem=boolean], [panel=boolean], [panelConfig=boolean], [radioMenuItemCollection=boolean], [toolContext=boolean], [uiTemplate=boolean], [window=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deleteUI is undoable, NOT queryable, and NOT editable.
NOTE: it is recommended that the type flags be used to disambiguate
different kinds of objects with the same name.




Example:
---
import maya.cmds as cmds

   Example 1.
---

   Create a simple window and then delete it and all of its children
   with one 'deleteUI -window' command.
---

window = cmds.window()
cmds.paneLayout()
cmds.button()
cmds.showWindow( window )

cmds.deleteUI( window, window=True )

   Example 2.
---

   Create a window with a number of buttons and delete a few of the
   buttons with the 'deleteUI -control' command.
---

window = cmds.window()
cmds.columnLayout()
cmds.button()
cmds.button()
cmds.button()
b1 = cmds.button()
b2 = cmds.button()
b3 = cmds.button()
cmds.showWindow( window )

cmds.deleteUI( b1, b2, b3, control=True )

---


Flags:
---


---
collection(cl): boolean
    properties: create
    Object names for deletion are all radio or tool collections.

---
control(ctl): boolean
    properties: create
    Object names for deletion are all controls.

---
editor(ed): boolean
    properties: create
    Object names for deletion are all editors.

---
layout(lay): boolean
    properties: create
    Object names for deletion are all layouts.

---
menu(m): boolean
    properties: create
    Object names for deletion are all menus.

---
menuItem(mi): boolean
    properties: create
    Object names for deletion are all menu items.

---
panel(pnl): boolean
    properties: create
    Object names for deletion are all panels.

---
panelConfig(pc): boolean
    properties: create
    Object names for deletion are panel configurations.

---
radioMenuItemCollection(ric): boolean
    properties: create
    Object names for deletion are all radio menu item collections.

---
toolContext(tc): boolean
    properties: create
    Object names for deletion are all tool contexts.

---
uiTemplate(uit): boolean
    properties: create
    Object names for deletion are all UI templates.

---
window(wnd): boolean
    properties: create
    Object names for deletion are all windows.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deleteUI.html 
    """


def deltaMush(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcomponents: boolean, flagdeformerTools: boolean, flagenvelope: float, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flaginwardConstraint: float, flagname: string, flagoutwardConstraint: float, flagparallel: boolean, flagpinBorderVertices: boolean, flagprune: boolean, flagremove: boolean, flagselectedComponents: boolean, flagsmoothingIterations: uint, flagsmoothingStep: float, flagsplit: boolean, flaguseComponentTags: boolean) -> string:
    """Synopsis:
---
---
 deltaMush(
selectionList
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [deformerTools=boolean], [envelope=float], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [inwardConstraint=float], [name=string], [outwardConstraint=float], [parallel=boolean], [pinBorderVertices=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean], [smoothingIterations=uint], [smoothingStep=float], [split=boolean], [useComponentTags=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deltaMush is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

Create a poly sphere
cmds.polySphere()

Attach a deltaMush deformer to the sphere performing
20 smoothing iterations with a step of 0.8
cmds.deltaMush( smoothingIterations=20, smoothingStep=0.8 )

---
Return:
---


    string: Delta mush deformer node name

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
deformerTools(dt): boolean
    properties: query
    Returns the name of the deformer tool objects (if any)
as string string ...

---
envelope(en): float
    properties: create, query, edit
    Envelope of the delta mush node. The envelope determines the percent of
deformation. Value is clamped to [0, 1] range.
Default is 1.

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
inwardConstraint(iwc): float
    properties: create, query, edit
    Constrains the movement of the vertex to not move inward from the input
deforming shape to preserve the contour. Value is in the [0,1] range.
Default is 0.0.

---
name(n): string
    properties: create
    Used to specify the name of the node being created.

---
outwardConstraint(owc): float
    properties: create, query, edit
    Constrains the movement of the vertex to not move outward from the input
deforming shape to preserve the contour. Value is in the [0,1] range.
Default is 0.0.

---
parallel(par): boolean
    properties: create, edit
    Inserts the new deformer in a parallel chain to any existing deformers in
the history of the object. A blendShape is inserted to blend the parallel
results together.
Works in create mode (and edit mode if the deformer has
no geometry added yet).

---
pinBorderVertices(pbv): boolean
    properties: create, query, edit
    If enabled, vertices on mesh borders will be pinned to their current
position during smoothing. Default is true.

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
smoothingIterations(si): uint
    properties: create, query, edit
    Number of smoothing iterations performed by the delta mush node.
Default is 10.

---
smoothingStep(ss): float
    properties: create, query, edit
    Step amount used per smoothing iteration. Value is clamped to [0, 1] range.
A higher value may lead to instabilities but converges faster compared
to a lower value. Default is 0.5.

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deltaMush.html 
    """


def detachCurve(flagcaching: boolean, flagconstructionHistory: boolean, flagcurveOnSurface: boolean, flagkeep: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagparameter: float, flagreplaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 detachCurve(
curve
    , [caching=boolean], [constructionHistory=boolean], [curveOnSurface=boolean], [keep=boolean], [name=string], [nodeState=int], [object=boolean], [parameter=float], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

detachCurve is undoable, queryable, and editable.  You can use this command to open a periodic curve at a particular
parameter value.  You would use this command with only one "-p" flag.
  If you are specifying "-k" flags, then you must specify one, none
or all "-k" flags.  If you are specifying all "-k" flags, there
must be one more "-k" flag than "-p" flags.




Example:
---
import maya.cmds as cmds

cmds.detachCurve( 'curve1', ch=True, p=0.2, replaceOriginal=False )
Detaches curve1 at parameter value 0.2.  The
result is two curves and a detachCurve dependency node.
The "-rpo" flag specifies that the original curve is not to be
replaced; as a result a new curve is created for each curve piece.
Note that if "k" flag is not used, then the default is that
all pieces are kept.

cmds.detachCurve( 'curve1.ep[1]', ch=True, replaceOriginal=False )
Detaches curve1 at its second edit point.

cmds.detachCurve( 'curve1.u[0.2]', ch=True, replaceOriginal=False )
Detaches curve1 at parameter value 0.2

cmds.detachCurve( 'curve1', ch=True, p=0.4, k=(1 , 0), rpo=False )
Detaches curve1 at parameter value 0.4 into two curves.  Because of
the "k" flags, two curves are created, but the second one is empty.
A detachCurve dependency node is also returned.

cmds.detachCurve( 'curve1', ch=True, p=(0.2, 0.4), rpo=True )
Detaches curve1 into three pieces.  Because the "rpo" flag is on,
the original curve is replaced with the first piece.  The names
of all curve pieces are returned.  If curve1 is a result of history,
then a dependency node is created and its output is connected as
the input to curve1.  If curve1 is not a result of construction
history, then a dependency node is not created (even though the
"ch" flag is on).

cmds.detachCurve( 'circle1', ch=True, p=(0.2, 0.4) )
Detaches a periodic curve, circle1, at two places.  Before
the detach, the circle is periodic, with a start parameter of 0.0,
and an end parameter of 8.0.
The first parameter, 0.2, is used to move the start point of the curve,
also called the "seam".  The second parameter, 0.4, is used to perform
a detach operation.  The result is TWO curves only.  The first curve
has a parameter range of 0.2 to 0.4.  The second curve has a parameter
range of 0.4 to 8.2.

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
keep(k): boolean
    properties: create, query, edit, multiuse
    Whether or not to keep a detached piece.  This multi attribute should be one element larger than the parameter multi attribute.
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
parameter(p): float
    properties: create, query, edit, multiuse
    Parameter values to detach at
Default: 0.0

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/detachCurve.html 
    """


def detachDeviceAttr(flagall: boolean, flagattribute: string, flagaxis: string, flagdevice: string, flagselection: boolean) -> None:
    """Synopsis:
---
---
 detachDeviceAttr([all=boolean], [attribute=string], [axis=string], [device=string], [selection=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

detachDeviceAttr is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.detachDeviceAttr( d='spaceball', ax='XAxis', at='translateX' )

---


Flags:
---


---
all(all): boolean
    properties: create
    Delete all attachments on every device.

---
attribute(at): string
    properties: create
    The attribute to detach. This flag must be used
with the -d/device flag.

---
axis(ax): string
    properties: create
    The axis to detach. This flag must be used with
the -d/device flag.

---
device(d): string
    properties: create
    Delete the attachment for this device. If the -ax/axis
flag is not used, all of the attachments connected to this
device are detached.

---
selection(sl): boolean
    properties: create
    Detaches selection attachments.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/detachDeviceAttr.html 
    """


def detachSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagdirection: int, flagkeep: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagparameter: float, flagreplaceOriginal: boolean) -> list[string]:
    """Synopsis:
---
---
 detachSurface(
surface
    , [caching=boolean], [constructionHistory=boolean], [direction=int], [keep=boolean], [name=string], [nodeState=int], [object=boolean], [parameter=float], [replaceOriginal=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

detachSurface is undoable, queryable, and editable.  You can only detach in either U or V (not both) with a single detachSurface operation.
    You can use this command to open a closed surface at a particular
parameter value.  You would use this command with only one "-p" flag.
  If you are specifying "-k" flags, then you must specify one, none
or all "-k" flags.  If you are specifying all "-k" flags, there
must be one more "-k" flag than "-p" flags.




Example:
---
import maya.cmds as cmds

cmds.detachSurface( 'surface1', ch=True, d=1, p=0.3, rpo=False )
cmds.detachSurface( 'surface1.u[0.3]', ch=True )
Detaches surface1 into two pieces at u = 0.3.
The results are two surface pieces, and a detachSurface dependency node.
Since no "-keep" flag is used, all pieces are kept.

cmds.detachSurface( 'surface1', ch=True, k=(1,0), rpo=False, p=0.34, d=0 )
cmds.detachSurface( 'surface1.v[0.34]', ch=True, k=(1,0), rpo=False )
Detaches surface1 at v = 0.34.  Because of the "k" flags, two
surfaces are created but the second surface is empty.  A
detachSurface dependency node is also returned.

cmds.detachSurface( 'surface1', ch=True, rpo=True, p=(0.2, 0.5), d=1 )
cmds.detachSurface( 'surface1.u[0.2]', 'surface1.u[0.5]', ch=True, rpo=True )
Detaches surface1 into three pieces.  Because of the "-rpo" flag,
the first surface piece is used to replace the original surface1.
The results are the three surfaces (including the original surface).
Even though the "ch" flag is on, a dependency node is not created
if surface1 is not a result of construction history.  If surface1
is the result of construction history, then a dependency node is
created and its name is returned.

cmds.detachSurface( 'cylinder1', ch=True, d=0, p=0.3, rpo=False )
Detaches cylinder1, which is periodic in V, where the V parameter
ranges between 0.0 and 8.0.  The parameter, 0.3, is used to move
the start point of the cylinder, also known as the "seam".
The resulting surface's V parameter range is 0.0 to 0.3.

cmds.detachSurface( 'cylinder1', ch=True, d=0, p=(0.3, 0.7), rpo=False )
Detaches cylinder1, which is periodic in V, where the V parameter
ranges between 0.0 and 8.0.  The 1st parameter, 0.3, is used to move
the start point of the cylinder, also known as the "seam".
The second parameter, 0.7, is used to detach the cylinder again.
The result is only TWO surfaces; the first surface's V parameter ranges
from 0.0 to 0.3. The second surface's V parameter ranges from 0.3 to 0.7.

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
direction(d): int
    properties: create, query, edit
    Direction in which to detach:
0 - V direction,
1 - U direction
Default: 1

---
keep(k): boolean
    properties: create, query, edit, multiuse
    Keep the detached pieces.
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
parameter(p): float
    properties: create, query, edit, multiuse
    Parameter at which to detach.
Default: 0.0

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/detachSurface.html 
    """


def deviceEditor(flagcontrol: boolean, flagdefineTemplate: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaghighlightConnection: string, flaglockMainConnection: boolean, flagmainListConnection: string, flagpanel: string, flagparent: string, flagselectionConnection: string, flagstateString: boolean, flagtakePath: string, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 deviceEditor([control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightConnection=string], [lockMainConnection=boolean], [mainListConnection=string], [panel=string], [parent=string], [selectionConnection=string], [stateString=boolean], [takePath=string], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deviceEditor is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

This example creates a new device editor in its own window
window = cmds.window()
cmds.paneLayout()
cmds.deviceEditor('myDeviceEditor')
cmds.showWindow( window )

---
Return:
---


    string: name of the editor

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
takePath(tp): string
    properties: query, edit
    The path used for writing/reading take data through the
editor.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deviceEditor.html 
    """


def deviceManager(flagattachment: boolean, flagaxisCoordChanges: boolean, flagaxisIndex: int, flagaxisName: boolean, flagaxisOffset: boolean, flagaxisScale: boolean, flagdeviceIndex: int, flagdeviceNameFromIndex: int, flagnumAxis: boolean, flagnumDevices: boolean) -> None:
    """Synopsis:
---
---
 deviceManager([attachment=boolean], [axisCoordChanges=boolean], [axisIndex=int], [axisName=boolean], [axisOffset=boolean], [axisScale=boolean], [deviceIndex=int], [deviceNameFromIndex=int], [numAxis=boolean], [numDevices=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

deviceManager is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


FIXME: get python sytax for above query.
cmds.deviceManager("layer1", root=True)

---


Flags:
---


---
attachment(att): boolean
    properties: query
    Returns the plugs that a device and axis are attached to.  Expects the -deviceIndex and
axisIndex to be used in conjunction.

---
axisCoordChanges(acc): boolean
    properties: query
    Returns whether the axis coordinate changes.  Expects the -deviceIndex and -axisIndex flags to be used
in conjunction.

---
axisIndex(axi): int
    properties: create, query, edit
    Used usually in conjunction with other flags, to indicate the index of the axis.

---
axisName(axn): boolean
    properties: query
    Returns the name of the axis.  Expects the -deviceIndex and -axisIndex flags to be used
in conjunction.

---
axisOffset(axo): boolean
    properties: query
    Returns the offset of the axis.  Expects the -deviceIndex and -axisIndex flags to be used
in conjunction.

---
axisScale(axs): boolean
    properties: query
    Returns the scale of the axis.  Expects the -deviceIndex and -axisIndex flags to be used
in conjunction.

---
deviceIndex(dvi): int
    properties: create, query, edit
    Used usually in conjunction with other flags, to indicate the index of the device.

---
deviceNameFromIndex(dni): int
    properties: query
    Returns the name of the device with the given index.

---
numAxis(nax): boolean
    properties: query
    Returns the number of axis this device has.  Expects the -deviceIndex flag to be used.

---
numDevices(ndv): boolean
    properties: query
    Returns the number of devices currently attached.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/deviceManager.html 
    """


def devicePanel(flagcontrol: boolean, flagcopy: string, flagcreateString: boolean, flagdefineTemplate: string, flagdocTag: string, flageditString: boolean, flagexists: boolean, flaginit: boolean, flagisUnique: boolean, flaglabel: string, flagmenuBarRepeatLast: boolean, flagmenuBarVisible: boolean, flagneedsInit: boolean, flagparent: string, flagpopupMenuProcedure: script, flagreplacePanel: string, flagtearOff: boolean, flagtearOffCopy: string, flagtearOffRestore: boolean, flagunParent: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 devicePanel([control=boolean], [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean], [parent=string], [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

devicePanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

This example creates a new device panel in its own window
window = cmds.window()
cmds.paneLayout()
cmds.devicePanel()
cmds.showWindow( window )

---
Return:
---


    string: name of panel

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/devicePanel.html 
    """


def dgInfo(flagallNodes: boolean, flagconnections: boolean, flagdirty: boolean, flagnodes: boolean, flagnonDeletable: boolean, flagoutputFile: string, flagpropagation: boolean, flagshort: boolean, flagsize: boolean, flagsubgraph: boolean, flagtype: string) -> None:
    """Synopsis:
---
---
 dgInfo([allNodes=boolean], [connections=boolean], [dirty=boolean], [nodes=boolean], [nonDeletable=boolean], [outputFile=string], [propagation=boolean], [short=boolean], [size=boolean], [subgraph=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dgInfo is NOT undoable, NOT queryable, and NOT editable.all
CLEAN means that evaluation of the plug's connection
succeeded and no dirty messages have come through it since then.
It also implies that the destination end of the connection has
received the value from the source end.

DIRTY means that a dirty message has passed through the
plug's connection since the last time an evaluation was made on the
destination side of that connection.


PROP means that the connection will allow dirty messages
to pass through and forwards them to all destinations.

BLOCK means that a dirty message will stop at this connection
and not continue on to any destinations. This is an optimization that
prevents excessive dirty flag propagation when many values are changing,
for example, a frame change in an animated sequece.

CLEAN BLOCKdgdirty -a
Simple A -> B : Plugs at both ends of the connection
share the same state information. The state information updates when an
evaluation request comes to A from B, or a dirty message is sent from
A to B.

Fan-Out A -> B, A -> C : Each of A, B, and
C have their own unique state information. B and C behave as described above.
A has its state information linked to B and C - it will have CLEAN
only when both B and C have CLEAN, it will have BLOCK only
when both B and C have BLOCK.

In-Out A -> B, C -> A : Each of A, B, and
C have their own unique state information. B and C behave as described above.
A has its state information linked to B and C. The CLEAN|DIRTY flag
looks backwards, then forwards:

if( C == CLEAN ) A = CLEAN
else if( B == CLEAN ) A = CLEAN

The BLOCK state is set when a dirty message passes through A, and
the PROP state is set either when A is set clean or an evaluation
passes through A.



All of this state change information only applies to dirty messages and
evaluations that use the normal context. Any changes in other contexts,
for example, through the getAttr -t TIME command, does not affect the
state in the connections.


Param curves and other passive inputs, for example blend nodes coming from
param curves, will not disable propagation. Doing so would make the keyframing
workflow impossible.


Certain messages can choose to completely ignore the connection state
information. For example when a node's state attribute changes a connection
may change to a blocking one so the message has to be propagated at least
one step further to all of its destinations. This way they can update their
information.


Certain operations can globally disable the use of the propagaton state
to reduce message flow.  The simplest example is when the evaluation
manager is building its graph. It has to visit all nodes so the propagation
cannot be blocked.


The messaging system has safeguards against cyclic messages flowing through
connections but sometimes a message bypasses the connection completely and
goes directly to the node. DAG parents do this to send messages to their
children. So despite connections into a node all having the BLOCK
state it could still receive dirty messages.




Example:
---
import maya.cmds as cmds

create a node
cmds.createNode('transform',name='NODE')
cmds.setKeyframe('NODE.translate')

Print all things connected to node NODE
cmds.dgInfo( 'NODE', c=True )

Print all connections currently in the graph
cmds.dgInfo( c=True, all=True )

Print the datablock size of all nodes currently in the graph
cmds.dgInfo( sz=True, all=True )
Return: [12, 12, 12314]

Print all connections to attribute tx on node NODE
cmds.dgInfo('NODE.tx',c=True)

Print all dirty connections in the entire graph
cmds.dgInfo( c=True, all=True, d=True )

---


Flags:
---


---
allNodes(all): boolean
    properties: create
    Use the entire graph as the context

---
connections(c): boolean
    properties: create
    Print the connection information

---
dirty(d): boolean
    properties: create
    Only print dirty/clean nodes/plugs/connections.  Default is both

---
nodes(n): boolean
    properties: create
    Print the specified nodes (or the entire graph if -all is used)

---
nonDeletable(nd): boolean
    properties: create
    Include non-deletable nodes as well (normally not of interest)

---
outputFile(of): string
    properties: create
    Send the output to the file FILE instead of STDERR

---
propagation(p): boolean
    properties: create
    Only print propagating/not propagating nodes/plugs/connections.
Default is both.

---
short(s): boolean
    properties: create
    Print using short format instead of long

---
size(sz): boolean
    properties: create
    Show datablock sizes for all specified nodes. Return value is tuple of
all selected nodes (NumberOfNodes, NumberOfDatablocks, TotalDatablockMemory)

---
subgraph(sub): boolean
    properties: create
    Print the subgraph affected by the node or plugs (or all nodes
in the graph grouped in subgraphs if -all is used)

---
type(nt): string
    properties: create
    Filter output to only show nodes of type NODETYPE

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dgInfo.html 
    """


def dgValidateCurve(flagallCurves: boolean, flagverbose: boolean) -> int:
    """Synopsis:
---
---
 dgValidateCurve([allCurves=boolean], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dgValidateCurve is NOT undoable, NOT queryable, and NOT editable.dgValidateCurve


Example:
---
import maya.cmds as cmds


Check all curves.
---

cmds.dgValidateCurve(allCurves=True);
Result: 123 ---


---
Return:
---


    int: Number of curves which changed their static status.

Flags:
---


---
allCurves(a): boolean
    properties: create
    Ignore the selected or specified objects and work on all curves.

---
verbose(v): boolean
    properties: create
    Prints out all of the curves set static or not.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dgValidateCurve.html 
    """


def dgdirty(flagallPlugs: boolean, flagclean: boolean, flagimplicit: boolean, flaglist: string, flagpropagation: boolean, flagshowTiming: boolean, flagverbose: boolean) -> int | list[string]:
    """Synopsis:
---
---
 dgdirty([allPlugs=boolean], [clean=boolean], [implicit=boolean], [list=string], [propagation=boolean], [showTiming=boolean], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dgdirty is NOT undoable, queryable, and NOT editable.dgdirtylistcleanall


Example:
---
import maya.cmds as cmds


Set everything in the entire scene dirty
---

cmds.dgdirty(allPlugs=True);
Result: 123 ---


Set all connected plugs dirty on "myNode"
5 plugs were set dirty
---

cmds.dgdirty( 'myNode' )
Result: 5 ---


Set all connected plugs dirty on "locator1"
0 plugs were connected so no dirty message was sent
---

cmds.dgdirty( 'locator1' )
Result: 0 ---



Set myNode.tx dirty
cmds.select( 'myNode.tx' )
cmds.dgdirty()
Result: 1 ---


Show the dirty elements in the node
cmds.dgdirty( list='data' )
Result: [myNode.tx] ---


Show plugs with dirty state, if any
cmds.dgdirty( list='plug' )
Result: [myNode.tx, myNode.ty] ---


Show plugs with dirty connections, if any
cmds.dgdirty( list='connection' )
Result: [myNode.ty] ---


Show the types of list parameters available
cmds.dgdirty( query=True, list=True )
Result: ['d/data', 'p/plug', 'c/connection']

Show the types of list parameters available with timing
cmds.dgdirty( query=True, list=True, showTiming=True )
Messages took 8 microseconds to process.
Result: ['d/data', 'p/plug', 'c/connection']

---
Return:
---


    list[string]: List of dirty/clean plugs in list plug mode.
    list[string]: List of plugs with dirty/clean data in list data mode.
    list[string]: Pairs of dirty/clean connected plugs in list connection mode.
    int: Number of dirty/clean messages sent out in normal mode.

Flags:
---


---
allPlugs(a): boolean
    properties: create, query
    Ignore the selected or specified objects and dirty (or clean)
all plugs.

---
clean(c): boolean
    properties: create, query
    If this flag is set then the attributes are cleaned.  Otherwise
they are set to dirty.

---
implicit(i): boolean
    properties: create, query
    If this flag is set then allow the implicit or default nodes to be
processed as well. Otherwise they will be skipped for efficiency.

---
list(l): string
    properties: create, query
    When this flag is specified then instead of sending out dirty/clean
messages the list of currently dirty/clean objects will be returned.
The allPlugs and clean flags are respected to narrow
guide the values to be returned.
The value of the flag tells what will be reported.

"data" or "d" = show plugs that have dirty/clean data
"plug" or "p" = show plugs that have dirty/clean states
"connection" or "c" = show plugs with connections that have dirty/clean states
Query this flag to find all legal values of the flag. Query this flag with
its value already set to get a description of what that value means.

Note that "p" and "c" modes are restricted to plugs that have connections
or non-standard state information. Other attributes will not have state
information to check, though they will have data.
In the case of array attributes only the children that have values
currently set will be considered. No attempt will be made to evaluate
them in order to update the available child lists.
e.g. if you have a DAG with transform T1 and shape S1 the instanced
attribute S1.wm[0] will be reported. If in a script you create a second
instance T2->S1 and immediately list the plugs again before evaluation
you will still only see S1.wm[0]. The new S1.wm[1] won't be reported
until it is created through an evaluation, usually caused by refresh,
a specific getAttr command, or an editor update.
Note that the list is only for selected nodes. Unlike when dirty
messages are sent this does not travel downstream.

---
propagation(p): boolean
    properties: create, query
    If this flag is set then the ability of dirty messages to flow through
the graph is left enabled.

---
showTiming(st): boolean
    properties: create, query
    If this flag is used then show how long the dirty messages took
to propagate.

---
verbose(v): boolean
    properties: create, query
    Prints out all of the plugs being set dirty on stdout.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dgdirty.html 
    """


def dgeval(flagsrc: boolean, flagverbose: boolean) -> None:
    """Synopsis:
---
---
 dgeval(
[objects]
    , [src=boolean], [verbose=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dgeval is undoable, NOT queryable, and NOT editable.dgeval
Normally the selection list is used to determine which objects to
evaluate, but you can add to the selection list by specifying which
objects you want on the command line.




Example:
---
import maya.cmds as cmds

Evaluate all (connected) plugs on "myNode"
cmds.dgeval( 'myNode' )
Result: 5
This means that 5 plugs were evaluated

Evaluate myNode.tx only
cmds.select( 'myNode.tx' )
cmds.dgeval()
Result: 1

---


Flags:
---


---
src(src): boolean
    properties: create
    This flag is obsolete. Do not use.

---
verbose(v): boolean
    properties: create
    If this flag is used then the results of the evaluation(s) is/are
printed on stdout.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dgeval.html 
    """


def dgfilter(flagattribute: string, flaglist: boolean, flaglogicalAnd: tuple[string, string], flaglogicalNot: string, flaglogicalOr: tuple[string, string], flagname: string, flagnode: string, flagnodeType: string, flagplug: string) -> boolean | list[string] | string:
    """Synopsis:
---
---
 dgfilter([attribute=string], [list=boolean], [logicalAnd=[string, string]], [logicalNot=string], [logicalOr=[string, string]], [name=string], [node=string], [nodeType=string], [plug=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dgfilter is NOT undoable, NOT queryable, and NOT editable.dgfilterdbtrace


Example:
---
import maya.cmds as cmds

Define attribute filter on translateX
cmds.dgfilter( atr='translateX', n='TX' )
Result: "TX"

Define plug filter on node.ty
cmds.dgfilter( plug='node.ty', n='TY' )
Result: "TY"

Define logical 'OR' filter.
cmds.dgfilter( logicalOr=('TX', 'TY'), n='OR' )
Result: "OR"

cmds.polyCube()
Result: [u'pCube1', u'polyCube1'] ---

cmds.polyCube()
Result: [u'pCube2', u'polyCube2'] ---


Filter passes since attribute matches
cmds.dgfilter( 'pCube1.tx', n='TX' )
Result: 1

Filter passes since TX portion succeeds
cmds.dgfilter( 'pCube1.tx', n='OR' )
Result: 1

Filter fails ; wrong attributes
cmds.dgfilter( 'pCube1.tz', n='OR' )
Result: 0

Filter fails ; wrong node
cmds.dgfilter( 'pCube2.ty', n='TY' )
Result: 0

Filter passes
cmds.dgfilter( 'pCube1.ty', n='TY' )
Result: 1

List filters available
cmds.dgfilter( list=True )
Result: [u'TX', u'TY', u'OR'] ---


Show filter information
cmds.dgfilter( list=True, n='OR' )
Result: LogicalOr( AttributeName(translateX), PlugName(node.ty) )

---
Return:
---


    string: if creating filter or getting filter info
    list[string]: if listing filters
    boolean: if applying filter

Flags:
---


---
attribute(atr): string
    properties: create
    Select objects whose attribute names match the pattern.

---
list(l): boolean
    properties: create
    List the available filters.  If used in conjunction with the -name
flag it will show a description of what the filter is.

---
logicalAnd(logicalAnd): [string, string]
    properties: create
    Logical AND of two filters.

---
logicalNot(logicalNot): string
    properties: create
    Logical inverse of filter.

---
logicalOr(logicalOr): [string, string]
    properties: create
    Logical OR of two filters.

---
name(n): string
    properties: create
    Use filter named FILTER (or create new filter with that name).
If no objects are specified then the name given to the filter
will be returned.

---
node(nd): string
    properties: create
    Select objects whose node names match the pattern.

---
nodeType(nt): string
    properties: create
    Select objects whose node type names match the pattern.

---
plug(p): string
    properties: create
    Select objects whose plug names match the pattern.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dgfilter.html 
    """


def dgmodified() -> list[string]:
    """Synopsis:
---
---
 dgmodified()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dgmodified is NOT undoable, NOT queryable, and NOT editable.dgmodified


Example:
---
import maya.cmds as cmds

list all modified nodes
cmds.dgmodified()

---
Return:
---


    list[string]: list of all nodes that have been modified

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dgmodified.html 
    """


def dgtimer(flagcombineType: boolean, flaghide: string, flaghierarchy: boolean, flagmaxDisplay: int, flagname: string, flagnoHeader: boolean, flagoutputFile: string, flagoverhead: boolean, flagrangeLower: float, flagrangeUpper: float, flagreset: boolean, flagreturnCode: string, flagreturnType: string, flagshow: string, flagsortMetric: string, flagsortType: string, flagthreshold: float, flagtimerOff: boolean, flagtimerOn: boolean, flagtrace: boolean, flagtype: string, flaguniqueName: boolean, flagupdateHeatMap: int) -> float:
    """Synopsis:
---
---
 dgtimer([combineType=boolean], [hide=string], [hierarchy=boolean], [maxDisplay=int], [name=string], [noHeader=boolean], [outputFile=string], [overhead=boolean], [rangeLower=float], [rangeUpper=float], [reset=boolean], [returnCode=string], [returnType=string], [show=string], [sortMetric=string], [sortType=string], [threshold=float], [timerOff=boolean], [timerOn=boolean], [trace=boolean], [type=string], [uniqueName=boolean], [updateHeatMap=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dgtimer is NOT undoable, queryable, and NOT editable.
The various operations we measure are called "metrics" and the types of
timers are called "timer types". The various metrics are always measured
when timing is on, but are only queried when specified via the -show and
-hide flags. The metrics currently supported are listed in detail under
the -show flag below. For each metric we support a standard set of timer
types. There are three of these:
"self" for self time (the time specific to the node and not its children),
"inclusive" (time including children of the node), and
"count" (number of operations of the given metric on the node).

The timing mechanism which is used by dgtimer is built into the DG
itself, thus ALL depend nodes can be timed and there is no need for
programmers writing plug-ins using the OpenMaya API to add any special
code in order for their nodes to be timed -- its all
handled transparently.

The dgtimer command allows node timers to be turned on, off, reset
to zero, and have their current value displayed, and these operations
can be performed globally on all nodes or on a specific set of nodes
defined by name, type or parentage. Note that all timer measurements are
computed in "real time" (the same time measurement you get from a
wristwatch) as opposed to "CPU time" (which only measures time when the
processor is executing your code). All times are displayed in seconds.

Use the -query flag to display the current timer values on a node,

use -on to turn on timing,

use -off to turn off timing,

and -reset to reset timers to zero.

To display the values measured during timing, there are two approaches.
The first method is to use the -query flag can be used to report the information which
has been measured. The second method is to use the query methods available on
the OpenMaya class MFnDependencyNode (see the OpenMaya documentation for details).

What follows is a description of what is generated via -query. The output
is broken out into several sections and these are described as follows:

SECTION 1:
Section 1 of the dgtimer output contains global information. This section
can be disabled via the -hoHeader flag.
These values are reset whenever a global timer reset
occurs (i.e. dgtimer -reset; is specified). The global values which are
reported are:


Total real time: the total wall-clock time since the
last global timer reset. This is the actual time which has been spent as you
might measure it measure it with your watch.
On a multi-processing system, this value will always remain true to to real
time (unlike user and sys time).
Total user time: the total time the CPU(s) spent
processing Maya not including any system time since the last global
timer reset.
Total sys time: the total time the CPU(s) spent in
operating system calls on behalf of Maya since the last global timer reset.

Summary of each metric for all nodes: a summary of self and count for each metric
that we measure:

Real time in callbacks reports the self time and count for the "callback" metric.
Real time in compute reports the self time and count for the "compute" metric.
Real time in dirty propagation reports the self time and count for the "dirty" metric.
Real time in drawing reports the self time and count for the "draw" metric.
Real time fetching data from plugs reports the self time and count for the "fetch" metric.

Breakdown of select metrics in greater detail: a reporting of certain combinations of
metrics that we measure:


Real time in compute invoked from callback reports the self time spent in compute
when invoked either directly or indirectly by a callback.
Real time in compute not invoked from callback reports the self time spent in compute
not invoked either directly or indirectly by a callback.

SECTION 2:
Section 2 of the dgtimer -query output contains per-node information. There is a header which
describes the meaning of each column, followed by the actual per-node data, and this is
ultimately followed by a footer which summarises the totals per column. Note that the data
contained in the footer is the global total for each metric and will include any nodes that
have been deleted since the last reset, so the value in the footer MAY exceed what you get when you total the
individual values in the column. To prevent the header
and footer from appearing, use the -noHeader flag to just display the per-node data.

The columns which are displayed are as follows:

Rank: The order of this node in the sorted list of all nodes, where the list
is sorted by -sortMetric and -sortType flag values (if these are omitted the default
is to sort by self compute time).
ON: Tells you if the timer for that node is currently on or off. (With
dgtimer, you have the ability to turn timing on and off on a per-node basis).
Per-metric information: various columns are reported for each metric. The
name of the metric is reported at in the header in capital letters (e.g. "DRAW"). The standard
columns for each metric are:

Self: The amount of real time (i.e. elapsed time as you might measure
it with a stopwatch) spent performing the operation (thus if the metric is "DRAW", then
this will be time spent drawing the node).
Inclusive: The amount of real time (i.e. elapsed time as you might measure
it with a stopwatch) spent performing the operation including any child operations
that were invoked on behalf of the operation (thus if the metric is "DRAW", then
this will be the total time taken to draw the node including any child operations).
Count: The number of operations that occued on this node (thus if the metric
is "DRAW", then the number of draw operations on the node will be reported).

Sort information if a column is the one being used to sort all the per-node
dgtimer information, then that column is followed by a Percent and Cumulative
column which describe a running total through the listing. Note that "-sortType none"
prevents these two columns from appearing and implicitely sorts on "self" time.

After the per-metric columns, the node name and type are reported:

Type The node type.
Name The name of the node. If the node is file referenced and you
are using namespaces, the namespace will be included. You can also force the
dagpath to be displayed by specifying the -uniqueName flag.
Plug-in name If the node was implemented in an OpenMaya plug-in, the
name of that plug-in is reported.


SECTION 3:
Section 3 of the dgtimer -query output describes time spent in callbacks. Note that
section 3 only appears when the CALLBACK metric is shown (see the -show flag).

The first part is SECTION 3.1 lists the time per callback with each entry comprising:

The name of the callback, such as "attributeChangedMsg". These names are internal
Maya names, and in the cases where the callback is available through the OpenMaya API,
the API access to the callback is similarly named.
The name is followed by a breakdown per callbackId. The callbackId is an identifying
number which is unique to each client that is registered to a callback and can
be deduced by the user, such as through the OpenMaya API. You can cross-reference by finding
the same callbackId value listed in SECTIONs 3.1 and 3.3.

Self time (i.e. real time spent within that callbackId type not including any child
operations which occur while processing the callback).
Percent (see the -sortType flag). Note that the percent values are listed to sum up to
100% for that callback. This is not a global percent.
Cumulative (see the -sortType flag).
Inclusive time (i.e. real time spent within that callbackId including any child operations).
Count (number of times the callbackId was invoked).
API lists "Y" if the callbackId was defined through the OpenMaya API, and "N" if the
callbackId was defined internally within Maya.
Node lists the name of the node this callbackId was associated with. If the callbackId was
associated with more than one node, the string "*multiple*" is printed. If there was no node
associated with the callbackId (or its a callback type in which the node is hard to deduce),
the entry is blank.

After the callbackId entries are listed, a dashed line is printed followed by a single
line listing the self, inclusive and count values for the callback. Note that the percent
is relative to the global callback time.

At the bottom of SECTION 3.1 is the per-column total. The values printed match the summation at
the bottom of the listing in section 2. Note that the values from SECTION 3.1
include any nodes that have been deleted since the last reset. The thresholding parameters
(-threshold, -rangeLower, -rangeUpper and -maxDisplay) are honoured when generating the listing.
The sorting of the
rows and display of the Percent and Cumulative columns obeys the -sortType flag. As the listing
can be long, zero entries are not displayed.

The second part is SECTION 3.2 which lists the data per callbackId. As noted earlier, the
callbackId is an identifying
number which is unique to each client that is registered to a callback and can
be deduced by the user, such as through the OpenMaya API. The entries in SECTION 3.2 appear
as follows:

CallbackId the numeric identifier for the callback. You can cross reference by
finding the same callbackId value listed in SECTIONs 3.1 and 3.3.
For each callbackId, the data is broken down per-callback:

Callback the name of the callback, e.g. "attributeChangedMsg".
Percent, Cumulative, Inclusive, Count, API and Node entries as described in SECTION 3.1.

After the callback entries are listed for the callbackId, a dashed followed by a summary line is
printed. The summary line lists the self, inclusive and count values for the callback. Note that
the percent is relative to the global callback time.


The third part is SECTION 3.3 which lists data per-callback per-node. The
nodes are sorted based on the -sortType flag, and for each node, the
callbacks are listed, also sorted based on the -sortType flag. As this
listing can be long, zero entries are not displayed. An important note for SECTION 3.3 is
that only nodes which still exist are displayed. If a node has been deleted, no infromation
is listed.




Example:
---
import maya.cmds as cmds

Turns on node timing and resets the timers.
cmds.dgtimer( on=True )

Turns off node timing. Note that this does not reset the
timers.
cmds.dgtimer( off=True )

Prints the current timer values to the default (stdout).
cmds.dgtimer( query=True )

To reset the timers:
cmds.dgtimer( reset=True )

Turn on node timing and reset the timer values to zero.
Then, playback the scene, turn off timing and dump to a file.
Turn on timing without resetting the timers, and repeat.
cmds.dgtimer( on=True, reset=True )
cmds.play( wait=True )
cmds.dgtimer( off=True )
cmds.dgtimer( outputFile='/home/virginia/timing/dgtrace_once.txt', query=True )
cmds.dgtimer( on=True )
cmds.play( wait=True )
cmds.dgtimer( off=True )
cmds.dgtimer( outputFile='/home/virginia/timing/dgtrace_twice.txt', query=True )

---
Return:
---


    float: By default, the total of self-compute time for all nodes. Can be modified via the -returnType, -sortMetric and -sortType flags.

Flags:
---


---
combineType(ct): boolean
    properties: query
    Causes all nodes of the same type (e.g. animCurveTA) to be combined in the
output display.

---
hide(hi): string
    properties: create, query, multiuse
    This flag is the converse of -show. As with -show, it is a query-only
flag which can be specified multiple times. If you do specify -hide, we display
all columns except those listed by the -hide flags.

---
hierarchy(h): boolean
    properties: create, query
    Used to specify that a hierarchy of the dependency graph be affected,
thus "-reset -hierarchy -name ball" will reset the timers on the node
named "ball" and all of its descendents in the dependency graph.

---
maxDisplay(m): int
    properties: query
    Truncates the display so that only the most expenive "n" entries are
printed in the output display.

---
name(n): string
    properties: create, query
    Used in conjunction with -reset or -query to specify the name of the node
to reset or print timer values for. When querying a single timer, only a
single line of output is generated (i.e. the global timers and header
information is omitted). Note that one can force output to the script editor
window via the "-outputFile MEL" option to make it easy to grab the values
in a MEL script. Note: the -name and -type flag cannot be used together.

---
noHeader(nh): boolean
    properties: create, query
    Used in conjunction with -query to prevent any header or footer information
from being printed. All that will be output is the per-node timing data.
This option makes it easier to parse the output such as when you output the
query to a file on disk using the -outputFile option.

---
outputFile(o): string
    properties: query
    Specifies where the output of timing or tracing is displayed. The flag takes a string
argument which accepts three possible values:


The name of a file on disk.
Or the keyword "stdout", which causes output to be displayed on the terminal window (Linux and Macintosh), and the status window on Windows.
Or the keyword "MEL", which causes output to be displayed in the Maya Script Editor (only supported with -query).

The "stdout" setting is the default behaviour.

This flag can be used with the -query flag as well as the -trace flag.

When used with the -trace flag, any tracing output will be displayed on the destination
specified by the -outputFile (or stdout if -outputFile is omitted). Tracing operations
will continue to output to the destination until you specify the -trace and -outputFile
flags again.

When used with the -query flag, timing output will be displayed to the destination
specified by the -outputFile (or "stdout" if -outputFile is omitted).

Here are some examples of how to use the -query, -trace and -outputFile flags:

Example: output the timing information to a single file on disk:


dgtimer -on;                                       // Turn on timing
create some animated scene content;
play -wait;                                        // Play the scene through
dgtimer -query -outputFile "/tmp/timing.txt"       // Output node timing information to a file on disk


Example: output the tracing information to a single file on disk:


dgtimer -on;                                       // Turn on timing
create some animated scene content;
dgtimer -trace on -outputFile "/tmp/trace.txt"     // Turn on tracing and output the results to file
play -wait;                                        // Play the scene through; trace info goes to /tmp/trace.txt
dgtimer -query;                                    // But the timing info goes to the terminal window
play -wait;                                        // Play the scene again, trace info still goes to /tmp/trace.txt


Example: two runs, outputting the trace information and timing information to separate files:


dgtimer -on;                                       // Turn on timing
create some animated scene content;
dgtimer -trace on -outputFile "/tmp/trace1.txt"    // Turn on tracing and output the results to file
play -wait;                                        // Play the scene through
dgtimer -query -outputFile "/tmp/query1.txt"       // Output node timing information to another file
dgtimer -reset;
dgtimer -trace on -outputFile "/tmp/trace2.txt"    // Output tracing results to different file
play -wait;                                        // Play the scene through
dgtimer -query -outputFile "/tmp/query2.txt"       // Output node timing information to another file


Tips and tricks:


Outputting the timing results to the script editor makes it easy to
use the results in MEL e.g. string $timing[] = `dgtimer -query -outputFile MEL`.
It is important to note that the -outputFile you specify with -trace is
totally independent from the one you specify with -query.
If the file you specify already exists, Maya will empty the file first
before outputting data to it (and if the file is not writable, an error is
generated instead).

In query mode, this flag needs a value.

---
overhead(oh): boolean
    properties: create, query
    Turns on and off the measurement of timing overhead. Under ordinary circumstances the
amount of timing overhead is minimal compared with the events being measured, but in
complex scenes, one might find the overhead to be measurable. By default this option
is turned off. To enable it, specify "dgtimer -overhead true" prior to starting timing.
When querying timing, the overhead is reported in SECTION 1.2 of the dgtimer output and
is not factored out of each individual operation.

---
rangeLower(rgl): float
    properties: create
    This flag can be specified to limit the range of nodes which are displayed
in a query, or the limits of the heat map with -updateHeatMap. The value
is the lower percentage cutoff for the nodes which are processed. There is also
a -rangeLower flag which sets the lower range limit. The default value is 0,
meaning that all nodes with timing value below the upper range limit are considered.

---
rangeUpper(rgu): float
    properties: create
    This flag can be specified to limit the range of nodes which are displayed
in a query, or the limits of the heat map with -updateHeatMap. The value
is the upper percentage cutoff for the nodes which are processed. There is also
a -rangeLower flag which sets the lower range limit. The default value is 100,
meaning that all nodes with timing value above the lower range limit are considered.

---
reset(r): boolean
    properties: create
    Resets the node timers to zero. By default, the timers on all nodes as
well as the global timers are reset, but if specified with the -name or
-type flags, only the timers on specified nodes are reset.

---
returnCode(rc): string
    properties: create, query
    This flag has been replaced by the more general -returnType flag.
The -returnCode flag was unfortunately specific to the compute metric only.
It exists only for backwards compatability purposes.
It will be removed altogether in a future release.

Here are some handy equivalences:

To get the total number of nodes:
OLD WAY: dgtimer -rc nodecount -q;
// Result:325//

NEW WAY: dgtimer -returnType total -sortType none -q;
// Result:325//

OLD WAY: dgtimer -rc count -q;
// Result:1270//

To get the sum of the compute count column:
NEW WAY: dgtimer -returnType total -sortMetric compute -sortType count -q;
// Result:1270//

OLD WAY: dgtimer -rc selftime -q;
// Result:0.112898//

To get the sum of the compute self column:
NEW WAY: dgtimer -returnType total -sortMetric compute -sortType self -q;
// Result:0.112898//

---
returnType(rt): string
    properties: query
    This flag specifies what the double value returned by the dgtimer command represents.
By default, the value returned is the global total as displayed in SECTION 1 for the
column we are sorting on in the per-node output (the sort column can be specified
via the -sortMetric and -sortType flags). However, instead of the
total being returned, the user can instead request the individual entries for
the column. This flag is useful mainly for querying without forcing any output.
The flag accepts the values "total", to just display the column total, or
"all" to display all entries individually.

For example, if you want to get the total of draw self time without any other
output simply specify the following:

dgtimer -returnType total -sortMetric draw -sortType self -threshold 100 -noHeader -query;
// Result: 7718.01 //

To instead get each individual entry, change the above query to:

dgtimer -returnType all -sortMetric draw -sortType self -threshold 100 -noHeader -query;
// Result: 6576.01 21.91 11.17 1108.92 //

To get the inclusive dirty time for a specific node, use -name as well as -returnType all:

dgtimer -name "virginia" -returnType all -sortMetric dirty -sortType inclusive -threshold 100 -noHeader -query;

Note: to get the total number of nodes, use "-sortType none -returnType total".  To get
the on/off status for each node, use "-sortType none -returnType all".

---
show(sh): string
    properties: create, query, multiuse
    Used in conjunction with -query to specify which columns are to be displayed
in the per-node section of the output. -show takes an argument, which can
be
"all" (to display all columns),
"callback" (to display the time spent during any callback processing on the node not due to evaluation),
"compute" (to display the time spent in the node's compute methods),
"dirty" (to display time spent propagating dirtiness on behalf of the node),
"draw" (to display time spent drawing the node),
"compcb" (to display time spent during callback processing on node due to compute),
and
"compncb" (to display time spent during callback processing on node NOT due to compute).
The -show flag can be used multiple
times, but cannot be specified with -hide. By default, if neither -show,
-hide, or -sort are given, the effective display mode is:
"dgtimer -show compute -query".

---
sortMetric(sm): string
    properties: create, query
    Used in conjunction with -query to specify which metric is to be sorted on
when the per-node section of the output is generated, for example "draw" time.
Note that the -sortType flag can also be specified to define which timer is
sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will
sort the output by the number of times each node was drawn. Both -sortMetric and
-sortType are optional and you can specify one without the other. The -sortMetric
flag can only be specified at most once. The flag takes the following arguments:
"callback" (to sort on time spent during any callback processing on the node),
"compute" (to sort on the time spent in the node's compute methods),
"dirty" (to sort on the time spent propagating dirtiness on behalf of the node),
"draw" (to sort on time spent drawing the node),
"fetch" (to sort on time spent copying data from the datablock),
The default, if -sortMetric is omitted, is to sort on the first displayed column.
Note that the sortMetric is
independent of which columns are displayed via -show and -hide. Sort on a hidden
column is allowed.
The column selected by -sortMetric and -sortType specifies which total is returned
by the dgtimer command on the MEL command line.
This flag is also used with -updateHeatMap to specify which metric to build the heat map for.

---
sortType(st): string
    properties: create, query
    Used in conjunction with -query to specify which timer is to be sorted on
when the per-node section of the output is generated, for example "self" time.
Note that the -sortMetric flag can also be specified to define which metric is
sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will
sort the output by the number of times each node was drawn. Both -sortMetric and
-sortType are optional and you can specify one without the other. The -sortType
flag can be specified at most once. The flag takes the following arguments:
"self" (to sort on self time, which is the time specific to the node and not its children),
"inclusive" (to sort on the time including children of the node),
"count" (to sort on the number of times the node was invoked).
and
"none" (to sort on self time, but do not display the Percent and Cumulative columns
in the per-node display, as well as cause the total number of nodes in Maya to be
returned on the command line).
The default, if -sortType is omitted, is to sort on self time.
The column selected by -sortMetric and -sortType specifies which total is returned
by the dgtimer command on the MEL command line. The global total as displayed in
SECTION 1 of the listing is returned. The special case of "-sortType none"
causes the number of nodes in Maya to instead be returned.
This flag is also used with -updateHeatMap to specify which metric to build the heat map for.

---
threshold(th): float
    properties: query
    Truncates the display once the value falls below the threshold value. The
threshold applies to whatever timer is being used for sorting. For example, if
our sort key is self compute time (i.e. -sortMetric is "compute" and -sortType
is "self") and the threshold parameter is 20.0, then only nodes with a compute
self-time of 20.0 or higher will be displayed. (Note that -threshold uses
absolute time. There are the similar -rangeUpper and -rangeLower parameters
which specify a range using percentage).

---
timerOff(off): boolean
    properties: create, query
    Turns off node timing. By default, the timers on all nodes are turned off,
but if specified with the -name or
-type flags, only the timers on specified nodes are turned off.
If the timers on all nodes become turned off, then global timing is also
turned off as well.

---
timerOn(on): boolean
    properties: create, query
    Turns on node timing. By default, the timers on all nodes are turned on,
but if specified with the -name or
-type flags, only the timers on specified nodes are turned on.
The global timers are also turned on by this command.
Note that turning on timing does NOT reset the timers to zero. Use the -reset
flag to reset the timers. The idea for NOT resetting the timers is to allow the
user to arbitrarily turn timing on and off and continue to add to the
existing timer values.

---
trace(tr): boolean
    properties: create
    Turns on or off detailed execution tracing.
By default, tracing is off. If enabled, each timeable operation is logged when it starts and
again when it ends. This flag can be used in conjunction with -outputFile to specify where the
output is generated to. The following example shows how the output is formatted:

dgtimer:begin: compute 3 particleShape1Deformed particleShape1Deformed.lastPosition

The above is an example of the output when -trace is true that marks the start
of an operation. For specific details on each field: the "dgtimer:begin:" string
is an identifying marker to flag that this is a begin operation record. The
second argument, "compute" in our example, is the operation metric. You can view
the output of each given metric via "dgtimer -q" by specifying the -show flag.
The integer which follows (3 in this case) is the depth in the operation stack,
and the third argument is the name of the node (particleShape1Deformed). The
fourth argument is specific to the metric. For "compute", it gives the name of
the plug being computed. For "callback", its the internal Maya name of the callback.
For "dirty", its the name of the plug that dirtiness is being propagated from.

dgtimer:end: compute 3 particleShape1Deformed 0.000305685 0.000305685

The above is the end operation record. The "compute", "3" and "particleShapeDeformed"
arguments were described in the "dgtimer:begin" overview earlier. The two floating-point
arguments are self time and inclusive time for the operation measured in seconds.
The inclusive measure lists the total time since the matching "dgtimer:begin:" entry
for this operation, while the self measure lists the inclusive time minus any time
consumed by child operations which may have occurred during execution of the current operation.
As noted elsewhere in this document, these two times are "wall clock times", measuring
elapsed time including any time in which Maya was idle or performing system calls.

Since dgtimer can measure some non-node qualities in Maya, such as global message
callbacks, a "-" is displayed where the node name would ordinarily be displayed.
The "-" means "not applicable".

---
type(t): string
    properties: create, query
    Used in conjunction with -reset or -query to specify the type of the node(s)
(e.g. animCurveTA) to reset or print timer values for.
When querying, use of the -combineType flag will cause all nodes of the
same type to be combined into one entry, and only one line of output is
generated (i.e. the global timers and header information is omitted).
Note: the -name and -type flag cannot be used together.

---
uniqueName(un): boolean
    properties: create, query
    Used to specify that the DAG nodes listed in the output should be
listed by their unique names.  The full DAG path to the object
will be printed out instead of just the node name.

---
updateHeatMap(uhm): int
    properties: create
    Forces Maya's heat map to rebuild based on the specified parameters.
The heat map is an internal dgtimer structure used in mapping
intensity values to colourmap entries during display by the HyperGraph
Editor. There is one heat map shared by all editors that are using heat
map display mode. Updating the heat map causes the timer values on all
nodes to be analysed to compose the distribution of entries in the heat map.
The parameter is the integer number of divisions in the map and should equal
the number of available colours for displaying the heat map. This flag can
be specified with the -rangeLower and -rangeUpper flags
to limit the range of displayable to lie between the percentile range.
The dgtimer command returns the maximum timing value for all nodes in Maya
for the specified metric and type.
Note: when the display range includes 0, the special zeroth (exactly zero)
slot in the heat map is avilable.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dgtimer.html 
    """


def dimWhen(flagclear: boolean, flagfalse: boolean, flagtrue: boolean) -> None:
    """Synopsis:
---
---
 dimWhen(
string string
    , [clear=boolean], [false=boolean], [true=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dimWhen is undoable, NOT queryable, and NOT editable.
This command will fail if the object does not exist. If the condition
does not exist (yet), that's okay --- a placeholder will be used until
such a condition comes into existence.

The UI object should be one of two things, either a control or a menu
item.




Example:
---
import maya.cmds as cmds

   Create a window with a menu item and button that will dim if
   there are no objects selected in the scene.
---

window = cmds.window(menuBar=True, title='dimWhen Example')
cmds.menu( label='Edit' )
menuItem = cmds.menuItem(label='Delete Selection', command='cmds.delete()')
cmds.columnLayout(adjustableColumn=True)
button = cmds.button(label='Delete Selection', command='cmds.delete()')

   Create a few buttons to create some objects, select all the objects in
   the scene, and clear the selection.
---

cmds.button(label='Create Objects', command='cmds.sphere(); cmds.cone(); cmds.cylinder();')
cmds.button(label='Select All', command='cmds.select(all=True)')
cmds.button(label='Select Nothing', command='cmds.select(clear=True)')

   Add the dim conditions.
---

cmds.dimWhen( 'SomethingSelected', button, false=True )
cmds.dimWhen( 'SomethingSelected', menuItem, false=True )

cmds.showWindow( window )

---


Flags:
---


---
clear(c): boolean
    properties: create
    Remove the condition on the specified dimmable.

---
false(f): boolean
    properties: create
    Dim the object when the condition is false.

---
true(t): boolean
    properties: create
    Dim the object when the condition is true. (default)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dimWhen.html 
    """


def directKeyCtx(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagoption: string, flagselectedOnly: boolean) -> string:
    """Synopsis:
---
---
 directKeyCtx(
contextName
    , [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [option=string], [selectedOnly=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

directKeyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a directKeyCtx which works in insert mode
---

cmds.directKeyCtx( 'specialDirectKeyContext', option='insert' )

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
selectedOnly(so): boolean
    properties: create, query, edit
    Controls whether only selected curves/keys can be moved, or
all.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/directKeyCtx.html 
    """


def directionalLight(flagdecayRate: int, flagdiscRadius: linear, flagexclusive: boolean, flagintensity: float, flagname: string, flagposition: tuple[linear, linear, linear], flagrgb: tuple[float, float, float], flagrotation: tuple[angle, angle, angle], flagshadowColor: tuple[float, float, float], flagshadowDither: float, flagshadowSamples: int, flagsoftShadow: boolean, flaguseRayTraceShadows: boolean) -> double[] | int | string:
    """Synopsis:
---
---
 directionalLight([decayRate=int], [discRadius=linear], [exclusive=boolean], [intensity=float], [name=string], [position=[linear, linear, linear]], [rgb=[float, float, float]], [rotation=[angle, angle, angle]], [shadowColor=[float, float, float]], [shadowDither=float], [shadowSamples=int], [softShadow=boolean], [useRayTraceShadows=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

directionalLight is undoable, queryable, and editable.
This is the commmand that instantiates an directionalLight
or edits the parameters of an existing one.
TdirectionalLightCmd inherits from TnonExtendedLightCmd
which defines softShadow flags.
See TlightCmd for a global picture of the light commands.

TdirectionalLightCmd behaves like any other command, it
has flags, saves undo information etc. the only slightly
different behaviour is that it calls up to
TnonExtendedLightCmd to complete the functionality of
the command.




Example:
---
import maya.cmds as cmds

Create a directional light
light = cmds.directionalLight(rotation=(45, 30, 15))

Change the light intensity
cmds.directionalLight( light, e=True, intensity=0.5 )

Query it
cmds.directionalLight( light, q=True, intensity=True )
Result:0.5---


---
Return:
---


    double[]: when querying the rgb or shadowColor flags
double when querying the intensity flag
boolean when querying the useRayTraceShadows or exclusive flags
linear[] when querying the position flag
angle[] when querying the rotation flag
string when querying the name flag
    int: rate of light decay, when querying the decayRate flag
    int: Number of shadow samples, when querying the shadowSamples flag
boolean True if soft shadows are enabled, when querying the softShadow flag
float Shadow dithering value, when querying the shadowDither flag
float Disc radius value, when querying the discRadius flag
    string: Light shape name

Flags:
---


---
decayRate(d): int
    properties: create
    Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)

---
discRadius(drs): linear
    properties: create, query
    Radius of shadow disc.

---
exclusive(exc): boolean
    properties: create, query
    True if the light is exclusively assigned

---
intensity(i): float
    properties: create, query
    Intensity of the light

---
name(n): string
    properties: create, query
    Name of the light

---
position(pos): [linear, linear, linear]
    properties: create, query
    Position of the light

---
rgb(rgb): [float, float, float]
    properties: create, query
    RGB colour of the light

---
rotation(rot): [angle, angle, angle]
    properties: create, query
    Rotation of the light for orientation, where applicable

---
shadowColor(sc): [float, float, float]
    properties: create, query
    Color of the light's shadow

---
shadowDither(sd): float
    properties: create, query
    Shadow dithering value.

---
shadowSamples(sh): int
    properties: create, query
    Numbr of shadow samples to use

---
softShadow(ss): boolean
    properties: create, query
    True if soft shadowing is to be enabled

---
useRayTraceShadows(rs): boolean
    properties: create, query
    True if ray trace shadows are to be used

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/directionalLight.html 
    """


def dirmap(flagconvertDirectory: string, flagenable: boolean, flaggetAllMappings: boolean, flaggetMappedDirectory: string, flagmapDirectory: tuple[string, string], flagunmapDirectory: string) -> string:
    """Synopsis:
---
---
 dirmap(
string string
    , [convertDirectory=string], [enable=boolean], [getAllMappings=boolean], [getMappedDirectory=string], [mapDirectory=[string, string]], [unmapDirectory=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dirmap is undoable, queryable, and NOT editable.
Directories
must both be absolute paths, and should be separated with forward
slashes ('/'). The mapping is case-sensitive on all platforms.
This command can be useful when moving projects to
another machine where some textures may not be contained in the Maya
project, or when a texture archive moves to a new location. This
command is not necessary when moving a (self-contained) project from
one machine to another - instead copy the entire project over and set
the Maya project to the new location. 
For one-time directory moves, if the command is enabled and the mapping
configured correctly, when a scene is opened and saved the mapped
locations will be reflected in the filenames saved with the file.
To set up a permanent mapping the command should
be enabled and the mappings set up in a script which is executed every
time you launch Maya (userSetup.mel is sourced on startup).
The directory mappings and enabled state are not preserved between
Maya sessions.
This command requires one "main" flag that specifies the action to take.
Flags are:
-[m|um|gmd|gam|cd|en]





Example:
---
import maya.cmds as cmds

cmds.dirmap( en=True )
cmds.dirmap( m=('/usr/maya/textures', '/share/store/textures') )
cmds.dirmap( cd='/usr/maya/textures/characters/skin1.iff' )
Result: /share/store/textures/characters/skin1.iff"
cmds.dirmap( m=('D:/mySoundfiles', '/usr/me/sounds') )
cmds.dirmap( cd='D:/mySoundfiles/' )
Result: /usr/me/sounds/

---
Return:
---


    string: when convertDirectory is used

Flags:
---


---
convertDirectory(cd): string
    properties: create
    Convert a file or directory.
Returns the name of the mapped file or directory, if the command is
enabled. If the given string
contains one of the mapped directories, the return value will have that
substring replaced with the mapped one. Otherwise the given argument
string will be returned. If the command is disabled the given argument
is always returned. Checks are not
made for whether the file or directory exists. If the given string
is a directory it should have a trailing '/'.

---
enable(en): boolean
    properties: create, query
    Enable directory mapping.
Directory mapping is off when you start Maya. If enabled, when opening
Maya scenes, file texture paths (and other file paths) will be converted
when the scene is opened. The -cd flag only returns mapped directories
when -enable is true.
Query returns whether mapping has been enabled.

---
getAllMappings(gam): boolean
    properties: create
    Get all current mappings.
Returns string array of current mappings in format:
[redirect1, replacement1, ... redirectN, replacementN]

---
getMappedDirectory(gmd): string
    properties: create
    Get the mapped redirected directory. The given argument must
exactly match the first string used with the -mapDirectory flag.

---
mapDirectory(m): [string, string]
    properties: create
    Map a directory - the first argument is mapped to the second.
Neither directory needs to exist on the local machine at the time
of invocation.

---
unmapDirectory(um): string
    properties: create
    Unmap a directory. The given argument must exactly match the
argument used with the -mapDirectory flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dirmap.html 
    """


def disable(flagvalue: boolean) -> None:
    """Synopsis:
---
---
 disable(
[string]
    , [value=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

disable is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.window()
cmds.formLayout()
cmds.button( 'fred' )
cmds.showWindow()
cmds.disable( 'fred' ) dims the button
cmds.disable( 'fred', v=False ) un-dims it

---


Flags:
---


---
value(v): boolean
    properties: create
    If true, this command disables the control.
If false, this command enables the control.
Default value is true (disable)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/disable.html 
    """


def disableIncorrectNameWarning() -> None:
    """Synopsis:
---
---
 disableIncorrectNameWarning()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

disableIncorrectNameWarning is NOT undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.disableIncorrectNameWarning()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/disableIncorrectNameWarning.html 
    """


def disconnectAttr(flagnextAvailable: boolean) -> string:
    """Synopsis:
---
---
 disconnectAttr(
attribute attribute
    , [nextAvailable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

disconnectAttr is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

   Create a sphere and cone and connect their rotate attribute.
---

sph = cmds.sphere()
con = cmds.cone()
sphereR = '%s.r' % sph[0]
coneR = '%s.r' % con[0]
cmds.connectAttr(sphereR, coneR)

   Break the connection between the rotate attributes.
---

cmds.disconnectAttr(sphereR, coneR)

---
Return:
---


    string: A phrase containing the names of the disconnected attributes.

Flags:
---


---
nextAvailable(na): boolean
    properties: create
    If the destination multi-attribute has set the indexMatters
to be false, the command will disconnect the first matching
connection.  No index needs to be specified.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/disconnectAttr.html 
    """


def disconnectJoint(flagattachHandleMode: boolean, flagdeleteHandleMode: boolean) -> string:
    """Synopsis:
---
---
 disconnectJoint([attachHandleMode=boolean], [deleteHandleMode=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

disconnectJoint is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.joint( p=(0, 0, 0), name='jointA' )
cmds.joint( p=(0, 1, 0), name='jointB' )
cmds.joint( p=(0, 2, 0), name='jointC' )
cmds.disconnectJoint( 'jointB' )

---
Return:
---


    string: After the joint is disconnected, a new joint will be created. The return value is the name of the newly created joint and its ancestor.

Flags:
---


---
attachHandleMode(ahm): boolean
    properties: create
    This flag is obsolete and no longer supported.

---
deleteHandleMode(dhm): boolean
    properties: create
    Delete the handle on the associated joint.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/disconnectJoint.html 
    """


def diskCache(flagappend: boolean, flagcacheType: string, flagclose: string, flagcloseAll: boolean, flagdelete: string, flagdeleteAll: boolean, flagempty: string, flagemptyAll: boolean, flagenabledCachesOnly: boolean, flagendTime: time, flagframeRangeType: string, flagoverSample: boolean, flagsamplingRate: int, flagstartTime: time, flagtempDir: boolean) -> None:
    """Synopsis:
---
---
 diskCache([append=boolean], [cacheType=string], [close=string], [closeAll=boolean], [delete=string], [deleteAll=boolean], [empty=string], [emptyAll=boolean], [enabledCachesOnly=boolean], [endTime=time], [frameRangeType=string], [overSample=boolean], [samplingRate=int], [startTime=time], [tempDir=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

diskCache is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Explicitly specify the settings for disk cache
creation: the start time to 3 and the end time to 10.
cmds.diskCache( startTime=3, endTime=10 )

Specify to use over sampling and with sampling
rate set to 2, sampling twice for each frame.
cmds.diskCache( overSample=True, samplingRate=2 )

Delete all caches
cmds.diskCache( deleteAll=True )

Clear the cache content for diskCache3's cache.
cmds.diskCache( empty='diskCache3' )

Close all the disk caches.
cmds.diskCache( emptyAll=True )

---


Flags:
---


---
append(a): boolean
    properties: create, query
    Append at the end and not to flush the existing cache

---
cacheType(ct): string
    properties: create, query
    Specifies the type of cache to overwrite.  "mcfp" for particle playback
cache, "mcfi" for particle initial cache. "mcj" for jiggle cache. This
option is only activated during the cache creation.

---
close(c): string
    properties: create, query
    Close the cache given the disk cache node name.  If -eco/enabledCachesOnly
is "true" only enabled disk cache nodes are affected.

---
closeAll(ca): boolean
    properties: create, query
    Close all disk cache files. If -eco/enabledCachesOnly
is "true" only enabled disk cache nodes are affected.

---
delete(d): string
    properties: create, query
    Delete the cache given the disk cache node name.  If -eco/enabledCachesOnly
is "true" only enabled disk cache nodes are affected.

---
deleteAll(da): boolean
    properties: create, query
    Delete all disk cache files.  If -eco/enabledCachesOnly
is "true" only enabled disk cache nodes are affected.

---
empty(e): string
    properties: create, query
    Clear the content of the disk cache with the given
disk cache node name.  If -eco/enabledCachesOnly
is "true" only enabled disk cache nodes are affected.

---
emptyAll(ea): boolean
    properties: create, query
    Clear the content of all disk caches.  If -eco/enabledCachesOnly
is "true" only enabled disk cache nodes are affected.

---
enabledCachesOnly(eco): boolean
    properties: create, query
    When present, this flag restricts the -ea/emptyAll,
so that only "enabled" disk caches (i.e., disk cache nodes
with the ".enable" attribute set to "true") are affected.

---
endTime(et): time
    properties: create, query
    Specifies the end frame of the cache range.

---
frameRangeType(frt): string
    properties: create, query
    Specifies the type of frame range to use, namely "Render Globals",
"Time Slider", and "Start/End".  In the case of "Time Slider", startFrame
and endFrame need to be specified.  (This flag is now obsolete.  Please
use the -startTime and -endTime flags to specify the frame range explicitly.)

---
overSample(os): boolean
    properties: create, query
    Over sample if true. Otherwise, under sample.

---
samplingRate(sr): int
    properties: create, query
    Specifies how frequently to sample relative to each frame.
When over-sampling (-overSample has been specified),
this parameter determines how many times per frame the runup will be evaluated.
When under-sampling (the default, when -overSample has not been specified), the runup will evaluate only once per sr frames, where sr is the value specified to this flag.

---
startTime(st): time
    properties: create, query
    Specifies the start frame of the cache range.

---
tempDir(tmp): boolean
    properties: create, query
    Query-only flag for the location of temporary diskCache files.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/diskCache.html 
    """


def displacementToPoly(flagfindBboxOnly: boolean) -> boolean:
    """Synopsis:
---
---
 displacementToPoly([findBboxOnly=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displacementToPoly is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To bake the rendered geometry and create a new meshShape, for the
selected geometry shape use:
cmds.displacementToPoly()

---
Return:
---


    boolean: Success or Failure.

Flags:
---


---
findBboxOnly(fbb): boolean
    properties: create, query, edit
    When used, only the bounding box scale for the displaced object is found.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displacementToPoly.html 
    """


def displayAffected() -> int:
    """Synopsis:
---
---
 displayAffected()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displayAffected is undoable, queryable, and NOT editable.
If one of the curves in a loft were selected and this feature were
turned on, then the lofted surface would be highlighted because it
is affected by the loft curve.




Example:
---
import maya.cmds as cmds

Turn on the display of affected objects
cmds.displayAffected( True )

Query whether the display of affected objects is turned on:
cmds.displayAffected( query=True )

---
Return:
---


    int: Affected display count

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displayAffected.html 
    """


def displayColor(flagactive: boolean, flagcreate: boolean, flagdormant: boolean, flaglist: boolean, flagqueryIndex: int, flagresetToFactory: boolean, flagresetToSaved: boolean) -> None:
    """Synopsis:
---
---
 displayColor(
string
    , [active=boolean], [create=boolean], [dormant=boolean], [list=boolean], [queryIndex=int], [resetToFactory=boolean], [resetToSaved=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displayColor is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.displayColor( 'grid', 15, dormant=True )
cmds.displayColor( 'grid', q=True, dormant=True )
cmds.displayColor( list=True )
cmds.displayColor( resetToFactory=True )
cmds.displayColor( queryIndex=15 )

---


Flags:
---


---
active(a): boolean
    properties: create
    Specifies the color index applies to active color palette.
name
Specifies the name of color to change.
index
The color index for the color.

---
create(c): boolean
    properties: create
    Creates a new display color which can be queried or set.
If is used only when saving color preferences.

---
dormant(d): boolean
    properties: create
    Specifies the color index applies to dormant color palette.
If neither of the dormant or active flags is specified, dormant
is the default.

---
list(l): boolean
    properties: create
    Writes out a list of all color names and their value.

---
queryIndex(qi): int
    properties: create
    Allows you to obtain a list of color names with the given color indices.

---
resetToFactory(rf): boolean
    properties: create
    Resets all display colors to their factory defaults.

---
resetToSaved(rs): boolean
    properties: create
    Resets all display colors to their saved values.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displayColor.html 
    """


def displayCull(flagbackFaceCulling: boolean) -> None:
    """Synopsis:
---
---
 displayCull(
[objects]
    , [backFaceCulling=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displayCull is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.displayCull( bfc=True )
cmds.displayCull( bfc=False )
cmds.displayCull( q=True, bfc=True )
Returns 0 if the back-face-culling on the selected object is false.
Returns 1 if the back-face-culling on the selected object is true.

---


Flags:
---


---
backFaceCulling(bfc): boolean
    properties: create, query
    Enable/disable culling of back faces.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displayCull.html 
    """


def displayLevelOfDetail(flaglevelOfDetail: boolean) -> None:
    """Synopsis:
---
---
 displayLevelOfDetail([levelOfDetail=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displayLevelOfDetail is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.displayLevelOfDetail( lod=True )
cmds.displayLevelOfDetail( lod=False )
cmds.displayLevelOfDetail( q=True, lod=True )
Returns 0 if the level-of-detail display is false.
Returns 1 if the level-of-detail display is true.

---


Flags:
---


---
levelOfDetail(lod): boolean
    properties: 
    Enable/disable level of detail.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displayLevelOfDetail.html 
    """


def displayPref(flagactiveObjectPivots: boolean, flagdisplayAffected: boolean, flagdisplayGradient: boolean, flagghostFrames: tuple[int, int, int], flagmaterialLoadingMode: string, flagmaxHardwareTextureResolution: boolean, flagmaxTextureResolution: int, flagpurgeExistingTextures: boolean, flagregionOfEffect: boolean, flagshadeTemplates: boolean, flagtextureDrawPixel: boolean, flagwireframeOnShadedActive: string) -> None:
    """Synopsis:
---
---
 displayPref([activeObjectPivots=boolean], [displayAffected=boolean], [displayGradient=boolean], [ghostFrames=[int, int, int]], [materialLoadingMode=string], [maxHardwareTextureResolution=boolean], [maxTextureResolution=int], [purgeExistingTextures=boolean], [regionOfEffect=boolean], [shadeTemplates=boolean], [textureDrawPixel=boolean], [wireframeOnShadedActive=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displayPref is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Turn on the display of affected objects
cmds.displayPref( displayAffected=True )

Query whether affected objects will be displayed
in a special color or not.
cmds.displayPref( q=True, displayAffected=True )
Result: 1 ---


Turn on full wireframes on active shaded objects
cmds.displayPref( wireframeOnShadedActive='full' )

---


Flags:
---


---
activeObjectPivots(aop): boolean
    properties: create, query
    Sets the display state for drawing pivots for active objects.

---
displayAffected(da): boolean
    properties: create, query
    Turns on/off the special coloring of objects that are affected
by the objects that are currently in the selection list.
If one of the curves in a loft were selected and this feature were
turned on, then the lofted surface would be highlighted because it
is affected by the loft curve.

---
displayGradient(dgr): boolean
    properties: create, query
    Set whether to display the background using a colored gradient as opposed
to a constant background color.

---
ghostFrames(gf): [int, int, int]
    properties: create, query
    Obsolete - use the "ghosting" command to set these values.

---
materialLoadingMode(mld): string
    properties: create, query
    Sets the material loading mode when loading the scene.  Possible
values for the string argument are
"immediate", "deferred" and "parallel".

---
maxHardwareTextureResolution(mhr): boolean
    properties: query
    Query the maximum allowable hardware texture resolution
available on the current video card. This maximum can vary
between different video cards and different operating systems.

---
maxTextureResolution(mtr): int
    properties: create, query
    Sets the maximum hardware texture resolution to be
used when creating hardware textures for display. The maximum
will be clamped to the maximum allowable texture determined
for the hardware at the time this command is invoked. Use
the -maxHardwareTextureResolution to retrieve this maximum value.
Existing hardware textures are not affected. Only newly created
textures will be clamped to this maximum.

---
purgeExistingTextures(pet): boolean
    properties: create
    Purge any existing hardware textures. This will force
a re-evaluation of hardware textures used for display, and
thus may take some time to evaluate.

---
regionOfEffect(roe): boolean
    properties: create, query
    Turns on/off the display of the region of curves/surfaces
that is affected by changes to selected CVs and edit points.

---
shadeTemplates(st): boolean
    properties: create, query
    Turns on/off the display of templated surfaces as shaded
in shaded display mode. If its off, templated surfaces appear
in wireframe.

---
textureDrawPixel(tdp): boolean
    properties: create, query
    Sets the display mode for drawing image planes. True for
use of gltexture calls for perspective views. This flag should
not normally be needed. Image Planes may display faster on
Windows but can result in some display artifacts.

---
wireframeOnShadedActive(wsa): string
    properties: create, query
    Sets the display state for drawing the wireframe on active
shaded objects.  Possible values for the string argument are
"full", "reduced" and "none".

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displayPref.html 
    """


def displayRGBColor(flagalpha: boolean, flagcreate: boolean, flaghueSaturationValue: boolean, flaglist: boolean, flagresetToFactory: boolean, flagresetToSaved: boolean) -> string:
    """Synopsis:
---
---
 displayRGBColor(
string
    , [alpha=boolean], [create=boolean], [hueSaturationValue=boolean], [list=boolean], [resetToFactory=boolean], [resetToSaved=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displayRGBColor is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Set the background colour to red
cmds.displayRGBColor( 'background', 1, 0, 0 )

List the current RGB color settings
cmds.displayRGBColor( list=True )

Query a RGB color by name
cmds.displayRGBColor("object", query=True)

Query the HSVA values of a color
cmds.displayRGBColor("object", query=True, hsv=True, alpha=True)

---
Return:
---


    string: when the list flag is used, none otherwise

Flags:
---


---
alpha(a): boolean
    properties: query
    Indicates that we want to query the alpha value of the color.
Upon query, returns RGBA or HSVA as an array of 4 floats.

---
create(c): boolean
    properties: create
    Creates a new RGB display color which can be queried or set.
If is used only when saving color preferences.
name
Specifies the name of color to change.

---
hueSaturationValue(hsv): boolean
    properties: create, query
    Indicates that rgb values are really hsv values.
Upon query, returns the HSV values as an array of 3 floats.
h s v
The HSV values for the color.  (Between 0-1)

---
list(l): boolean
    properties: create
    Writes out a list of all RGB color names and their value.

---
resetToFactory(rf): boolean
    properties: create
    Resets all the RGB display colors to their factory defaults.

---
resetToSaved(rs): boolean
    properties: create
    Resets all the RGB display colors to their saved values.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displayRGBColor.html 
    """


def displaySmoothness(flagall: boolean, flagboundary: boolean, flagdefaultCreation: boolean, flagdivisionsU: int, flagdivisionsV: int, flagfull: boolean, flaghull: boolean, flagpointsShaded: int, flagpointsWire: int, flagpolygonObject: int, flagrenderTessellation: boolean, flagsimplifyU: int, flagsimplifyV: int) -> None:
    """Synopsis:
---
---
 displaySmoothness(
[objects]
    , [all=boolean], [boundary=boolean], [defaultCreation=boolean], [divisionsU=int], [divisionsV=int], [full=boolean], [hull=boolean], [pointsShaded=int], [pointsWire=int], [polygonObject=int], [renderTessellation=boolean], [simplifyU=int], [simplifyV=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displaySmoothness is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

create a surface
cmds.sphere()

set rough smoothness settings
cmds.displaySmoothness( du=0, dv=0, pw=4, ps=1 )

set medium smoothness settings
cmds.displaySmoothness( du=1, dv=1, pw=8, ps=2 )

set fine smoothness settings
cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 )

Display surface as a hull
cmds.displaySmoothness( hull=True )

Display with reduced number of points
cmds.displaySmoothness( hull=True, su=2, sv=2 )

Display rendering tesselation
cmds.displaySmoothness( rt=1 )

Set default value for pointsShaded.
Subsequent surfaces created will have pointsShaded as 2.
cmds.displaySmoothness( dc=True, ps=2 )

displaySmoothness queries
---

query hull display, returns boolean
cmds.displaySmoothness( q=True, hull=True )

query default pointsShaded value
cmds.displaySmoothness( q=True, dc=True, ps=True )

query surface divisionsU value
cmds.displaySmoothness( q=True, du=True )

Only the -pointsWire flag works on curves.
cmds.circle()

change the number of points displayed per curve span.
cmds.displaySmoothness( pw=3 )
query default pointsWire value for curves.
cmds.displaySmoothness( q=True, dc=True, pw=True )

cmds.polyCube()

Query the display resolution
cmds.displaySmoothness( q=True, polygonObject=True )
Result: 0

Change the display resolution
cmds.displaySmoothness( polygonObject=2 )

---


Flags:
---


---
all(all): boolean
    properties: create, query
    Change smoothness for all curves and surfaces

---
boundary(bn): boolean
    properties: create, query
    Display wireframe surfaces using only the boundaries of the surface
Not fully implemented yet

---
defaultCreation(dc): boolean
    properties: create, query
    The default values at creation (applies only -du, -dv, -pw, -ps)

---
divisionsU(du): int
    properties: create, query
    Number of isoparm divisions per span in the U direction.
The valid range of values is [0,64].

---
divisionsV(dv): int
    properties: create, query
    Number of isoparm divisions per span in the V direction.
The valid range of values is [0,64].

---
full(f): boolean
    properties: create, query
    Display surface at full resolution - the default.

---
hull(hl): boolean
    properties: create, query
    Display surface using the hull (control points are drawn rather
than surface knot points). This mode is a useful display performance
improvement when modifying a surface since it doesn't require
evaluating points on the surface.

---
pointsShaded(ps): int
    properties: create, query
    Number of points per surface span in shaded mode. The
valid range of values is [1,64].

---
pointsWire(pw): int
    properties: create, query
    Number of points per surface isoparm span
or the number of points per curve span in wireframe mode.
The valid range of values is [1,128].
Note: This is the only flag that also applies to nurbs curves.

---
polygonObject(po): int
    properties: create, query
    Display the polygon objects with the given resolution

---
renderTessellation(rt): boolean
    properties: create, query
    Display using render tesselation parameters when in shaded mode.

---
simplifyU(su): int
    properties: create, query
    Number of spans to skip in the U direction when in
hull display mode.

---
simplifyV(sv): int
    properties: create, query
    Number of spans to skip in the V direction when in
hull display mode.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displaySmoothness.html 
    """


def displayString(flagdelete: boolean, flagexists: boolean, flagkeys: boolean, flagreplace: boolean, flagvalue: string) -> None:
    """Synopsis:
---
---
 displayString([string][string][string][string], [delete=boolean], [exists=boolean], [keys=boolean], [replace=boolean], [value=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displayString is NOT undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

   Associate a string with an identifier.
---

cmds.displayString( 'kExampleHelloWorld', value='Hello world' )

   Query string associated with an identifer.
---

cmds.displayString( 'kExampleHelloWorld', query=True, value=True )

   Define a simple formatted string to append ellipses.
---

cmds.displayString( 'kExampleEllipsesFormat', value='^1s...' )
cmds.displayString( 'kExampleEllipsesFormat', 'kExampleHelloWorld', query=True, value=True )

   Define a formatted string using all the available
   embedded characters.
---

cmds.displayString( 'kExampleAnotherFormat', value='These ^1s are ^2s me ^3s' )
cmds.displayString( 'kExamplePretzels', value='pretzels' )
cmds.displayString( 'kExampleAnotherFormat', 'kExamplePretzels', 'making', 'thirsty', query=True, value=True )

Obtain a list of matching displayString keys.
In the first example  a list of  all keys containing the substring
"niceName".
In the second example a list of all keys in the string set
m_testStrings
cmds.displayString( 'niceName', query=True, keys=True )
cmds.displayString( 'm_testStrings.', query=True, keys=True )

   If you do not specify the -v/value flag on creating then
   the value will be the same as the identifier.
---

cmds.displayString( 'kExampleMissingValue' )
cmds.displayString( 'kExampleMissingValue', query=True, value=True )

---


Flags:
---


---
delete(d): boolean
    properties: create
    This flag is used to remove an identifer string.
The command will fail if the identifier does not exist.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the specified identifier exists.

---
keys(k): boolean
    properties: create, query
    List all displayString keys that match the identifier string.
The identifier string may be a whole or partial key string.
The command will return a list of all identifier keys that contain this
identifier string as a substring.

---
replace(r): boolean
    properties: create, query
    Since a displayString command will fail if it tries to assign a new value
to an existing identifer, this flag is required to allow updates
to the value of an already-existing identifier.  If the identifier does
not already exist, a new identifier is added as if the -replace flag were
not present.

---
value(v): string
    properties: create, query
    The display string\'s value. If you do not specify this flag when
creating a display string then the value will be the same as the
identifier.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displayString.html 
    """


def displaySurface(flagflipNormals: boolean, flagtwoSidedLighting: boolean, flagxRay: boolean) -> boolean:
    """Synopsis:
---
---
 displaySurface(
[objects...]
    , [flipNormals=boolean], [twoSidedLighting=boolean], [xRay=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

displaySurface is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.sphere(n='mySphere1')
cmds.sphere(n='mySphere2')
cmds.displaySurface( ['mySphere1', 'mySphere2'], two=False )
cmds.displaySurface( xRay=True )

---
Return:
---


    boolean: when in the query mode.

Flags:
---


---
flipNormals(flp): boolean
    properties: query
    flip normal direction on the surface

---
twoSidedLighting(two): boolean
    properties: query
    toggle if the surface should be considered
two-sided.  If it's single-sided, drawing and rendering
may use single sided lighting and back face cull
to improve performance.

---
xRay(x): boolean
    properties: query
    toggle X ray mode (make surface transparent)

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/displaySurface.html 
    """


def distanceDimContext(flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string) -> string:
    """Synopsis:
---
---
 distanceDimContext([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

distanceDimContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.distanceDimContext()

---
Return:
---


    string: - name of the context created

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/distanceDimContext.html 
    """


def distanceDimension(flagendPoint: tuple[linear, linear, linear], flagstartPoint: tuple[linear, linear, linear]) -> string:
    """Synopsis:
---
---
 distanceDimension([endPoint=[linear, linear, linear]], [startPoint=[linear, linear, linear]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

distanceDimension is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

To measure ths distance between [0,2,2] and [1,5,6]:
cmds.distanceDimension( sp=(0, 2, 2), ep=(1, 5, 6) )
 Result: distanceDimensionShape1  ---


---
Return:
---


    string: - the shape name of the DAG node created.

Flags:
---


---
endPoint(ep): [linear, linear, linear]
    properties: create
    Specifies the point to measure distance to, from the startPoint.

---
startPoint(sp): [linear, linear, linear]
    properties: create
    Specifies the point to start measuring distance from.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/distanceDimension.html 
    """


def doBlur(flagcolorFile: string, flaglength: float, flagmemCapSize: float, flagsharpness: float, flagsmooth: float, flagsmoothColor: boolean, flagvectorFile: string) -> string:
    """Synopsis:
---
---
 doBlur([colorFile=string], [length=float], [memCapSize=float], [sharpness=float], [smooth=float], [smoothColor=boolean], [vectorFile=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

doBlur is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.doBlur( l=2, s=1, m=2, c='testimage', v='testimage.motion' )

---
Return:
---


    string: Command result

Flags:
---


---
colorFile(c): string
    properties: create
    Name of the input color image to be blurred.

---
length(l): float
    properties: create
    Scale applied on the motion vector. Ranges from 0 to infinity.

---
memCapSize(o): float
    properties: create
    Size of the memory cap, in bytes

---
sharpness(s): float
    properties: create
    Determines  the shape of the blur filter. The higher the value,
the narrower the filter, the sharper the blur. The lower the value,
the wider the filter, the more spread out the blur.
Ranges from 0 to infinity.

---
smooth(m): float
    properties: create
    Filter size to smooth the blurred image. The higher the value,
the more anti-aliased the alpha channel. Ranges from 1.0 to 5.0.

---
smoothColor(r): boolean
    properties: create
    Whether to smooth the color or not.

---
vectorFile(v): string
    properties: create
    Name of the input motion vector file.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/doBlur.html 
    """


def dockControl(flagallowedArea: string, flagannotation: string, flagarea: string, flagbackgroundColor: tuple[float, float, float], flagcloseCommand: script, flagcontent: string, flagdefineTemplate: string, flagdocTag: string, flagdockStation: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagenablePopupOption: boolean, flagexists: boolean, flagfixedHeight: boolean, flagfixedWidth: boolean, flagfloatChangeCommand: script, flagfloating: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flagisObscured: boolean, flaglabel: string, flagmanage: boolean, flagmoveable: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagr: boolean, flagretain: boolean, flagsizeable: boolean, flagsplitLayout: string, flagstate: string, flagstatusBarMessage: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int) -> string:
    """Synopsis:
---
---
 dockControl(
[name]
    , [allowedArea=string], [annotation=string], [area=string], [backgroundColor=[float, float, float]], [closeCommand=script], [content=string], [defineTemplate=string], [docTag=string], [dockStation=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enablePopupOption=boolean], [exists=boolean], [fixedHeight=boolean], [fixedWidth=boolean], [floatChangeCommand=script], [floating=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [moveable=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [r=boolean], [retain=boolean], [sizeable=boolean], [splitLayout=string], [state=string], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dockControl is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

myWindow = cmds.window()
buttonForm = cmds.formLayout( parent = myWindow )
cmds.button( parent = buttonForm )
allowedAreas = ['right', 'left']
cmds.dockControl( area='left', content=myWindow, allowedArea=allowedAreas )

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
allowedArea(aa): string
    properties: create, query, edit, multiuse
    Areas where the dock control may be placed. Valid values are "top", "left", "bottom", "right" and "all".  The default is "all".

---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
area(a): string
    properties: create, query, edit
    The initial dock area for this dock control. This is a required flag.

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
closeCommand(cc): script
    properties: create, edit
    Script executed after the dock control is closed.

---
content(con): string
    properties: create, query
    The name of the control that is the content of this dock control.  This is a required flag.

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
dockStation(ds): string
    properties: create
    The name of the control the window can be docked into.
If this is not set it is assumed to be the main window.

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
enablePopupOption(epo): boolean
    properties: create, query, edit
    Whether or not the menu option for the dock control in the UI Elements popup menu is enabled.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fixedHeight(fh): boolean
    properties: create, query, edit
    Whether or not the dockControl height may be interactively resized.

---
fixedWidth(fw): boolean
    properties: create, query, edit
    Whether or not the dockControl width may be interactively resized.

---
floatChangeCommand(fcc): script
    properties: create, edit
    The script executed when the floating state of the dock widget changes.

---
floating(fl): boolean
    properties: create, query, edit
    Whether the dock widget is floating.
A floating dock widget is presented to the user as an independent window "on top" of main window, instead of being docked in the main window.

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
    The label text.  The default label is the name of the control.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
moveable(mov): boolean
    properties: create, query, edit
    Control over whether or not the dockControl may be undocked/redocked.

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
r(r): boolean
    properties: query, edit
    Whether the dock widget is visible and either floating or at the top of its dock widget area.

---
retain(ret): boolean
    properties: create, query, edit
    Control over whether or not the window and its contents are deleted when closed.
The default is true.  The window and its contents are retained when closed unless this is set to false.

---
sizeable(s): boolean
    properties: create, query, edit
    Whether or not the dockControl width may be interactively resized.
Deprecated!!  Use the fixedWidth flag instead.

---
splitLayout(sl): string
    properties: create
    When two windows are added to a single docking area they are by default tabbed together.
Setting a value for splitLayout will allow it to be placed next to another control in the same area.
The flag's argument controls the orientation of the split.
Valid values are "horizontal" or "vertical".

---
state(st): string
    properties: create, query, edit
    When queried this flag will return a string holding the dock control state information.
This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,
but can be saved and loaded using the optionVar command to restore a dock control's state across sessions of Maya.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dockControl.html 
    """


def dolly(flagabsolute: boolean, flagdistance: linear, flagdollyTowardsCenter: boolean, flagorthoScale: float, flagrelative: boolean) -> None:
    """Synopsis:
---
---
 dolly(
[camera]
    , [absolute=boolean], [distance=linear], [dollyTowardsCenter=boolean], [orthoScale=float], [relative=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dolly is undoable, NOT queryable, and NOT editable.

Relative mode: for a perspective camera, the camera is moved along
its viewing direction, and the distance of travel is computed with
respect to the current position of the camera in the world
space. In relative mode, when the camera is moved, its COI is
moved along with it, and is kept at the same distance, in front of
the camera, as before applying the dolly operation. For
orthographic camera, the viewing width of the camera is changed by
scaling its ortho width by the new value specified on the command
line. 

Absolute mode: for a perspective camera, the camera is moved along
its viewing direction, to the distance that is computed with
respect to the current position of the world center of interest
(COI) of the camera. In the absolute mode, when the camera is
moved, the COI of the camera is not moved with the camera, but it
is fixed at its current location in space. For orthographic
camera, the viewing width of the camera is changed by replacing
its ortho width with the new value specified on the command
line. This command may be applied to more than one cameras;
objects that are not cameras are ignored. When no camera name
supplied on the command line, this command is applied to all
currently active cameras. 

The dolly command can be applied to either a perspective or an
orthographic camera. 




Example:
---
import maya.cmds as cmds

cmds.camera()

Moves the persp camera forward through its center of interest
cmds.dolly( 'persp', abs=True, d=-3 )

Move the persp camera and its center of interest.
cmds.dolly( 'persp', d=-3 )

Changes the ortho-width of the top camera to 7.5
cmds.dolly( 'top', abs=True, os=7.5 )

Scale the ortho-width of the top camera by a quarter from its current value.
cmds.dolly( 'top', os=0.25 )

---


Flags:
---


---
absolute(abs): boolean
    properties: create
    This flag modifies the behavior of the distance and orthoScale
flags. When used in conjunction with the distance flag, the distance
argument specifies how far the camera's eye point should be set from
the camera's center of interest. When used with the orthoScale flag,
the orthoScale argument specifies the camera's new ortho width.

---
distance(d): linear
    properties: create
    Unit distance to dolly a perspective camera.

---
dollyTowardsCenter(dtc): boolean
    properties: create
    This flag controls whether the dolly is performed towards the
center of the view (if true), or towards the point where the user
clicks (if false). By default, dollyTowardsCenter is on.

---
orthoScale(os): float
    properties: create
    Scale to change the ortho width of an orthographic camera.

---
relative(rel): boolean
    properties: create
    This flag modifies the behavior of the distance and orthoScale
flags. When used in conjunction with the distance flag, the camera
eye and center of interest are both moved by the amount specified
by the distance flag's argument. When used with the orthoScale flag,
the orthoScale argument is used multiply the camera's ortho width.By
default the relative flag is always on.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dolly.html 
    """


def dollyCtx(flagalternateContext: boolean, flagboxDollyType: string, flagcenterOfInterestDolly: boolean, flagdollyTowardsCenter: boolean, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglocalDolly: boolean, flagname: string, flagorthoZoom: boolean, flagscale: float, flagtoolName: string) -> string:
    """Synopsis:
---
---
 dollyCtx(
object
    , [alternateContext=boolean], [boxDollyType=string], [centerOfInterestDolly=boolean], [dollyTowardsCenter=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [localDolly=boolean], [name=string], [orthoZoom=boolean], [scale=float], [toolName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dollyCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.dollyCtx( 'dollyContext', s=1.0, ac=False, ld=False, cd=False )

cmds.dollyCtx( 'dollyContext', e=True, bdt='surface' )

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
boxDollyType(bdt): string
    properties: create, query, edit
    Set the behavior of where the camera's center of interest is
set to after the box dolly. In surface mode, the center
of interest will be snapped to the surface point at the center
of the marquee. In bbox mode, the closest bounding box
to the camera will be used. Bounding box mode will use the
selection mask to determine which objects to include into the
calculation.

---
centerOfInterestDolly(cd): boolean
    properties: create, query, edit
    Set the translate the camera's center of interest. Left and
right drag movements with the mouse will translate the center
of interest towards or away respectively from the camera. The
center of interest can be snapped to objects by using the left
mouse button for selection. The default select mask will be
used.

---
dollyTowardsCenter(dtc): boolean
    properties: create, query, edit
    Dolly towards center (if true), else dolly towards point where
user clicks in the view.

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
localDolly(ld): boolean
    properties: create, query, edit
    Dolly with respect to the camera's center of interest. The
camera will not pass through the center of interest. Local
dolly only applies to perspective cameras.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
orthoZoom(oz): boolean
    properties: create, query, edit
    Zoom orthographic view (if true), else dolly orthographic camera.
Default value is true.

---
scale(s): float
    properties: create, query, edit
    The sensitivity for dollying the camera.

---
toolName(tn): string
    properties: create, query
    Name of the specific tool to which this command refers.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dollyCtx.html 
    """


def dopeSheetEditor(flagautoFit: string, flagautoFitTime: string, flagcontrol: boolean, flagdefineTemplate: string, flagdisplayActiveKeyTangents: string, flagdisplayActiveKeys: string, flagdisplayInfinities: string, flagdisplayKeys: string, flagdisplayTangents: string, flagdisplayValues: string, flagdocTag: string, flagexists: boolean, flagfilter: string, flagforceMainConnection: string, flaghierarchyBelow: boolean, flaghighlightConnection: string, flaglockMainConnection: boolean, flaglookAt: string, flagmainListConnection: string, flagoutliner: string, flagpanel: string, flagparent: string, flagselectionConnection: string, flagselectionWindow: tuple[float, float, float, float], flagshowScene: boolean, flagshowSummary: boolean, flagshowTicks: boolean, flagsnapTime: string, flagsnapValue: string, flagstateString: boolean, flagunParent: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 dopeSheetEditor(
editorName
    , [autoFit=string], [autoFitTime=string], [control=boolean], [defineTemplate=string], [displayActiveKeyTangents=string], [displayActiveKeys=string], [displayInfinities=string], [displayKeys=string], [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [hierarchyBelow=boolean], [highlightConnection=string], [lockMainConnection=boolean], [lookAt=string], [mainListConnection=string], [outliner=string], [panel=string], [parent=string], [selectionConnection=string], [selectionWindow=[float, float, float, float]], [showScene=boolean], [showSummary=boolean], [showTicks=boolean], [snapTime=string], [snapValue=string], [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dopeSheetEditor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.dopeSheetEditor( 'dopeSheetEditor' )

---
Return:
---


    string: Editor name

Flags:
---


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
hierarchyBelow(hb): boolean
    properties: query, edit
    display animation for objects hierarchically

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
outliner(o): string
    properties: query, edit
    the name of the outliner which is associated with the dope sheet

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
selectionWindow(sel): [float, float, float, float]
    properties: query, edit
    The selection area specified as left, right, bottom, top respectively.

---
showScene(sc): boolean
    properties: query, edit
    display the scene summary object

---
showSummary(ss): boolean
    properties: query, edit
    display the summary object

---
showTicks(stk): boolean
    properties: query, edit
    display per animation tick divider in channel

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dopeSheetEditor.html 
    """


def doubleProfileBirailSurface(flagblendFactor: float, flagcaching: boolean, flagconstructionHistory: boolean, flagname: string, flagnodeState: int, flagobject: boolean, flagpolygon: int, flagtangentContinuityProfile1: boolean, flagtangentContinuityProfile2: boolean, flagtransformMode: int) -> list[string]:
    """Synopsis:
---
---
 doubleProfileBirailSurface(
curve curve curve curve
    , [blendFactor=float], [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean], [polygon=int], [tangentContinuityProfile1=boolean], [tangentContinuityProfile2=boolean], [transformMode=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

doubleProfileBirailSurface is undoable, queryable, and editable.
This command builds a railed surface by sweeping profile "profile1"
along the two given rail curves "rail1", "rail2" until "profile2" is
reached. By using the -blend control, the railed surface creation
could be biased more towards one of the two profile curves. The curves
( both profiles and rails ) could also be surface curves ( isoparams,
curve on surfaces ). If the profile curves are surface curves the
surface constructed could be made tangent continuous to the surfaces
underlying the profiles using the flags -tp1, -tp2 respectively.
Current Limitation: Its necessary that the two profile curves
intersect the rail curves for successful surface creation.




Example:
---
import maya.cmds as cmds

cmds.doubleProfileBirailSurface( 'curve1', 'curve2', 'curve3', 'curve4', bl=0.5 )

Tangent continuous birail surface across the two profiles.
cmds.doubleProfileBirailSurface( 'surface1.u[0.5]', 'surface2.v[0.2]', 'curve1', 'curve2', bl=1.0, tp1=True, tp2=True )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
blendFactor(bl): float
    properties: create, query, edit
    A blend factor applied in between the two profiles.
The amount of influence 'inputProfile1' has in the surface creation.
Default: 0.5

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
    Need tangent continuity across the input profile at inputProfile1.
Default: false

---
tangentContinuityProfile2(tp2): boolean
    properties: create, query, edit
    Need tangent continuity across the input curve at inputProfile2.
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/doubleProfileBirailSurface.html 
    """


def drag(flagattenuation: float, flagdirectionX: float, flagdirectionY: float, flagdirectionZ: float, flagmagnitude: float, flagmaxDistance: linear, flagname: string, flagperVertex: boolean, flagposition: tuple[linear, linear, linear], flagtorusSectionRadius: linear, flaguseDirection: boolean, flagvolumeExclusion: boolean, flagvolumeOffset: tuple[linear, linear, linear], flagvolumeShape: string, flagvolumeSweep: angle) -> string:
    """Synopsis:
---
---
 drag(
[objects]
    , [attenuation=float], [directionX=float], [directionY=float], [directionZ=float], [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear], [useDirection=boolean], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

drag is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
Drag exerts a friction, or braking force proportional to the speed of
a moving object. If direction is not enabled, the drag acts opposite
to the current velocity of the object. If direction is enabled, it acts
opposite to the component of the velocity in the specified direction.
The force is independent of the position of the affected object.

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

Creates a drag field resisting in direction (0,1,0.5).
cmds.drag( name='myDrag', dx=0, dy=1.0, dz=0.5, useDirection=1 )

Edits the acceleration value of the field myDrag
cmds.drag( 'myDrag', e=True, m=0.75 )

Queries myDrag for its magnitude
cmds.drag( 'myDrag', q=True, m=True )

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
useDirection(ud): boolean
    properties: query, edit
    Enable/disable direction. Drag will use -dx/-dy/-dz arguments if
and only if this flag is set true.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/drag.html 
    """


def dragAttrContext(flagconnectTo: name, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagreset: boolean) -> string:
    """Synopsis:
---
---
 dragAttrContext(
[name]
    , [connectTo=name], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [reset=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dragAttrContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )

cmds.dragAttrContext( 'myDragAttrContext' )

Example 1: Move along X direction and rotate around X at the same time.
cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
cmds.setToolTo( 'myDragAttrContext' )

Example 2: Extrude a face and then modify the distance that it is extruded by.
cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
cmds.setToolTo( 'myDragAttrContext' )

Example 3: Do a wedge face and modify both the number of divisions and the
angle at the same time.
cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
cmds.setToolTo( 'myDragAttrContext' )

---
Return:
---


    string: The name of the context created

Flags:
---


---
connectTo(ct): name
    properties: create, query, edit, multiuse
    Specifies an attribute to which to connect the context. This is a multi-use
flag, but all attributes used must be from one object.

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
reset(r): boolean
    properties: create, edit
    Resets the list of attributes to which the context is connected.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dragAttrContext.html 
    """


def draggerContext(flaganchorPoint: tuple[float, float, float], flagbutton: int, flagcurrentStep: int, flagcursor: string, flagdragCommand: script, flagdragPoint: tuple[float, float, float], flagdrawString: string, flagexists: boolean, flagfinalize: script, flaghelpString: string, flaghistory: boolean, flagholdCommand: script, flagimage1: string, flagimage2: string, flagimage3: string, flaginitialize: script, flagmodifier: string, flagname: string, flagplane: tuple[float, float, float], flagprePressCommand: script, flagpressCommand: script, flagprojection: string, flagreleaseCommand: script, flagsnapping: boolean, flagspace: string, flagstepsCount: int, flagundoMode: string) -> string:
    """Synopsis:
---
---
 draggerContext(
[name]
    , [anchorPoint=[float, float, float]], [button=int], [currentStep=int], [cursor=string], [dragCommand=script], [dragPoint=[float, float, float]], [drawString=string], [exists=boolean], [finalize=script], [helpString=string], [history=boolean], [holdCommand=script], [image1=string], [image2=string], [image3=string], [initialize=script], [modifier=string], [name=string], [plane=[float, float, float]], [prePressCommand=script], [pressCommand=script], [projection=string], [releaseCommand=script], [snapping=boolean], [space=string], [stepsCount=int], [undoMode=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

draggerContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Procedure called on press
def SampleContextPress():
        pressPosition = cmds.draggerContext( 'sampleContext', query=True, anchorPoint=True)
        print ("Press: " + str(pressPosition))

Procedure called on drag
def SampleContextDrag():
        dragPosition = cmds.draggerContext( 'sampleContext', query=True, dragPoint=True)
        button = cmds.draggerContext( 'sampleContext', query=True, button=True)
        modifier = cmds.draggerContext( 'sampleContext', query=True, modifier=True)
        print ("Drag: " + str(dragPosition) + "  Button is " + str(button) + "  Modifier is " + modifier + "\n")
        message = str(dragPosition[0]) + ", " + str(dragPosition[1])
        cmds.draggerContext( 'sampleContext', edit=True, drawString=message)

Define draggerContext with press and drag procedures
cmds.draggerContext( 'sampleContext', pressCommand='SampleContextPress()', dragCommand='SampleContextDrag()', cursor='hand' );

Set the tool to the sample context created
Results can be observed by dragging mouse around main window
cmds.setToolTo('sampleContext')

---
Return:
---


    string: The name of the context.

Flags:
---


---
anchorPoint(ap): [float, float, float]
    properties: query
    Anchor point (double array) where dragger was initially pressed.

---
button(bu): int
    properties: query
    Returns the current mouse button (1,2,3).

---
currentStep(cs): int
    properties: query
    Current step (press-drag-release sequence) for dragger context.
When queried before first press event happened, returns 0.

---
cursor(cur): string
    properties: create, query, edit
    Cursor displayed while context is active.  Valid values are:
"default", "hand", "crossHair", "dolly", "track", and "tumble".

---
dragCommand(dc): script
    properties: create, query, edit
    Command called when mouse dragger is dragged.

---
dragPoint(dp): [float, float, float]
    properties: query
    Drag point (double array) current position of dragger during drag.

---
drawString(ds): string
    properties: create, edit
    A string to be drawn at the current position of the pointer.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
finalize(fnz): script
    properties: create, query, edit
    Command called when the tool is exited.

---
helpString(hs): string
    properties: query
    Help string for context

---
history(ch): boolean
    properties: create
    If this is a tool command, turn the construction history on
for the tool in question.

---
holdCommand(hc): script
    properties: create, query, edit
    Command called when mouse dragger is held.

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
initialize(inz): script
    properties: create, query, edit
    Command called when the tool is entered.

---
modifier(mo): string
    properties: query
    Returns the current modifier type:  ctrl, alt or none.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
plane(pl): [float, float, float]
    properties: create, edit
    Provide normal of projection plane (see -projection flag for details).

---
prePressCommand(ppc): script
    properties: create, query, edit
    Command called when mouse dragger is pressed. It is called before
pressCommand, so it can be used for initialization of context.

---
pressCommand(pc): script
    properties: create, query, edit
    Command called when mouse dragger is pressed.

---
projection(pr): string
    properties: create, query, edit
    Sets current projection of drag point. Valid types are:


viewPlane
project to view plane


objectViewPlane
project to object plane (parallel to view plane)


objectPlane
project to specified plane defined by object location and normal (default) 0,1,0


plane
project to specified plane defined by origin and normal (default) 0,1,0


sketchPlane
project to sketch plane


xAxis
project to closest point on X axis


yAxis
project to closest point on Y axis


zAxis
project to closest point on Z axis


boundingSphere
project to closest point on object sphere bounds


boundingBox
project to closest point on object bounding box

---
releaseCommand(rc): script
    properties: create, query, edit
    Command called when mouse dragger is released.

---
snapping(snp): boolean
    properties: create, query, edit
    Enable/disable snapping for dragger context.

---
space(sp): string
    properties: create, query, edit
    Sets current space that coordinates are reported in. Types are:


world
world space (global)


object
object space (local)


screen
screen space

---
stepsCount(sc): int
    properties: create, query, edit
    Number of steps (press-drag-release sequences) for dragger context.
When combined with undoMode flag, several steps might be recorded as
single undo action.

---
undoMode(um): string
    properties: create, query, edit
    Undo queue mode for the context actions.
Acceptable values are:

"all" default behaviour when every action that happens during
dragger context activity is recorded as an individual undo chunk.
"step" - all the actions that happen between each press and
release are combined into one undo chunk.
"sequence" - all the actions that happen between very first press
and very last release are combined into single undo chunk. This works
exactly the same as "step" for a single step dragger context.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/draggerContext.html 
    """


def dropoffLocator() -> list[string]:
    """Synopsis:
---
---
 dropoffLocator(
float float string selectionList
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dropoffLocator is undoable, NOT queryable, and NOT editable.
The arguments are two floats, the envelope and percentage, followed by
the wire node name and then by the curve point(s).




Example:
---
import maya.cmds as cmds

create a wire deformer
---

cmds.polyPlane(w=24,h=24,sx=20,sy=20)
cmds.curve(d=3,p=[(-10, 0, 0),(-6, 0, 10),(-3, 0, -10),(10, 0, 0)],k=[0, 0, 0, 1, 1, 1])
cmds.select('pPlane1')
cmds.wire(w='curve1')

add a locator at curve point 0.5, with envelope 2 and percent 1
---

cmds.select( 'curve1.u[0.5]', r=True )
cmds.dropoffLocator( 2.0, 1.0, 'wire1' )

---
Return:
---


    list[string]: Locator name(s)

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dropoffLocator.html 
    """


def duplicate(flagfullPath: boolean, flaginputConnections: boolean, flaginstanceLeaf: boolean, flagname: string, flagparentOnly: boolean, flagrenameChildren: boolean, flagreturnRootsOnly: boolean, flagsmartTransform: boolean, flagtransformsOnly: boolean, flagupstreamNodes: boolean) -> list[string]:
    """Synopsis:
---
---
 duplicate(
[objects...]
    , [fullPath=boolean], [inputConnections=boolean], [instanceLeaf=boolean], [name=string], [parentOnly=boolean], [renameChildren=boolean], [returnRootsOnly=boolean], [smartTransform=boolean], [transformsOnly=boolean], [upstreamNodes=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

duplicate is undoable, NOT queryable, and NOT editable.
The smart transform feature allows duplicate to transform
newly duplicated objects based on previous transformations
between duplications.

Example: Duplicate an object and move it to a new
location. Duplicate it again with the smart duplicate
flag. It should have moved once again the distance you had
previously moved it.

Note: changing the selected list between smart duplications
will cause the transform information to be deleted

The upstream Nodes option forces duplication of all
upstream nodes leading upto the selected objects.. Upstream nodes
are defined as all nodes feeding into selected nodes. During traversal
of Dependency graph, if another dagObject is encountered, then that
node and all it's parent transforms are also duplicated.

The inputConnections option forces the duplication of input connections
to the nodes that are to be duplicated. This is very useful especially
in cases where two nodes that are connected to each other are
specified as nodes to be duplicated. In that situation, the connection
between the nodes is also duplicated.

See also: instance




Example:
---
import maya.cmds as cmds

Create a hierarchy of two spheres;
cmds.sphere( n='sphere1' )
cmds.move( 3, 0, 0 )
cmds.sphere( n='sphere2' )
cmds.move( -3, 0, 0 )
cmds.group( 'sphere1', 'sphere2', n='group1' )
cmds.circle( n='circle1' )

Create a duplicate of the group
cmds.duplicate( 'group1' )
Result: group2 sphere1 sphere2 ---


cmds.undo()
cmds.duplicate( 'group1', rr=True )
Result: group2 ---


Create a row of 4 circles equally spaced using
the -smartTransform flag.
cmds.duplicate( 'circle1' )
cmds.move( 3, 0, 0 )
cmds.duplicate( st=True )
cmds.duplicate( st=True )

Duplicate a sphere along with its input connections.
If animCurves were feeding into original transforms of the
sphere, they will feed into the duplicated ones also.
If the sphere has history (in this case it does),
then the history is connected to the duplicate. Note that
changing the radius for the makeNurbSphere for the sphere1
affects the duplicated sphere.
---

cmds.duplicate( 'group1|sphere1', ic=True )
cmds.move( 0, 0, 0 )
cmds.setAttr( 'makeNurbSphere1.radius', 2 )

Duplicate selected objects along with their upstream nodes
and connections. This will duplicate the history.
cmds.select( 'group1|sphere2' )
cmds.duplicate( un=True )

---
Return:
---


    list[string]: : names of the objects created

Flags:
---


---
fullPath(f): boolean
    properties: create
    ADDED 2023
Return full pathnames instead of object names.

---
inputConnections(ic): boolean
    properties: create
    Input connections to the node to be duplicated, are
also duplicated. This would result in a fan-out
scenario as the nodes at the input side are not
duplicated (unlike the -un option).

---
instanceLeaf(ilf): boolean
    properties: create
    instead of duplicating leaf DAG nodes, instance them.

---
name(n): string
    properties: create
    name to give duplicated object(s)

---
parentOnly(po): boolean
    properties: create
    Duplicate only the specified DAG node and not any of its
children.

---
renameChildren(rc): boolean
    properties: create
    rename the child nodes of the hierarchy, to make them
unique.

---
returnRootsOnly(rr): boolean
    properties: create
    return only the root nodes of the new hierarchy.
When used with upstreamNodes flag, the upstream nodes
will be omitted in the result.  This flag controls only
what is returned in the output string[], and it does
NOT change the behaviour of the duplicate command.

---
smartTransform(st): boolean
    properties: create
    remembers last transformation and applies
it to duplicated object(s)

---
transformsOnly(to): boolean
    properties: create
    Duplicate only transform nodes and not any shapes.

---
upstreamNodes(un): boolean
    properties: create
    the upstream nodes leading upto the selected nodes
(along with their connections) are also duplicated.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/duplicate.html 
    """


def duplicateCurve(flagcaching: boolean, flagconstructionHistory: boolean, flaglocal: boolean, flagmaxValue: float, flagmergeItems: boolean, flagminValue: float, flagname: string, flagnodeState: int, flagrange: boolean, flagrelative: boolean) -> list[string]:
    """Synopsis:
---
---
 duplicateCurve([caching=boolean], [constructionHistory=boolean], [local=boolean], [maxValue=float], [mergeItems=boolean], [minValue=float], [name=string], [nodeState=int], [range=boolean], [relative=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

duplicateCurve is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.cone( ch=True, o=True, po=0, ax=(0, 1, 0), r=3, hr=4 )
Result: [u'nurbsCone1', u'makeNurbCone1'] ---


duplicate isoparm at v param 0.5 with history
cmds.duplicateCurve( 'nurbsCone1.v[0.5]', ch= True, o=True )

duplicate isoparm at normalized u param 0.1, no history
cmds.duplicateCurve( 'nurbsCone1.un[0.1]', ch=False )

cmds.nurbsPlane( ch=True, o=True, po=0, ax=(0, 1, 0), w=10, lr=1 ) ;
cmds.circle( ch=True, o=True, nr=(0, 1, 0), r=4 ) ;
cmds.projectCurve( 'nurbsCircle1', 'nurbsPlane1', ch=False, rn=False, un=False, tol=0.01 )
duplicate curve on surface
cmds.duplicateCurve( 'nurbsPlaneShape1->projectionCurve1_1', ch=True, o=False )

cmds.trim( 'nurbsPlaneShape1', 'projectionCurve1_Shape1', ch=True, o=True, rpo=True, lu=0.2, lv=0.3 )
duplicate trim edge
cmds.duplicateCurve( 'nurbsPlane1.edge[1][1][1]', ch=True, o=False);

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
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
local(l): boolean
    properties: create
    Copy the transform of the surface and connect to the local
space version instead.

---
maxValue(max): float
    properties: create, query, edit
    Maximum parameter value for the curve segment.  Must be greater
than or equal to the minValue attribute.
If relative is true, then this attribute has maximum value of 1.0.
Default: -1.0

---
mergeItems(mi): boolean
    properties: create
    Merge component results where possible. For example, instead of returning a[1] and a[2], return a[1:2].

---
minValue(min): float
    properties: create, query, edit
    Minimum parameter value for the curve segment
If relative is true, then this attribute has minimum value of 0.0.
Default: 1.0

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
range(rn): boolean
    properties: create
    Force a curve range on complete input curve.

---
relative(r): boolean
    properties: create, query, edit
    True means use a relative parameter range, from 0.0 to 1.0.
Otherwise, the parameter values are absolute values.
Default: false

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/duplicateCurve.html 
    """


def duplicateSurface(flagcaching: boolean, flagconstructionHistory: boolean, flagfaceCountU: int, flagfaceCountV: int, flagfirstFaceU: int, flagfirstFaceV: int, flaglocal: boolean, flagmergeItems: boolean, flagname: string, flagnodeState: int) -> list[string]:
    """Synopsis:
---
---
 duplicateSurface([caching=boolean], [constructionHistory=boolean], [faceCountU=int], [faceCountV=int], [firstFaceU=int], [firstFaceV=int], [local=boolean], [mergeItems=boolean], [name=string], [nodeState=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

duplicateSurface is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.nurbsPlane( u=4, v=3 )
cmds.duplicateSurface( 'nurbsPlane1.sf[1:2][0:1]', ch=True, o=True )

Duplicates 4 faces of a nurbs plane.

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
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
faceCountU(fcu): int
    properties: create, query, edit
    Number of faces in U direction
Default: 1

---
faceCountV(fcv): int
    properties: create, query, edit
    Number of faces in V direction
Default: 1

---
firstFaceU(ffu): int
    properties: create, query, edit
    First face (U direction index)
Default: 0

---
firstFaceV(ffv): int
    properties: create, query, edit
    First face (V direction index)
Default: 0

---
local(l): boolean
    properties: create
    Copy the transform of the surface and connect to the local
space version instead.

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

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/duplicateSurface.html 
    """


def dynCache() -> None:
    """Synopsis:
---
---
 dynCache()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynCache is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Create an emitter and connect it to a particle shape
cmds.emitter(typ='omni', pos=(1, 1, 1), n='myEmitter')
cmds.particle(n='myParticles')
cmds.connectDynamic('myParticles', em='myEmitter')

Cache all attributes of the particle shape at time 50
cmds.playbackOptions(min=0, max=50, ast=0, aet=100)
cmds.currentTime('0');
cmds.play(w=True)
cmds.dynCache()

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynCache.html 
    """


def dynExport(flagallObjects: boolean, flagattribute: string, flagformat: string, flagmaxFrame: time, flagminFrame: time, flagonlyUpdateParticles: boolean, flagoverSampling: int, flagpath: string) -> string:
    """Synopsis:
---
---
 dynExport(
[objects]
    , [allObjects=boolean], [attribute=string], [format=string], [maxFrame=time], [minFrame=time], [onlyUpdateParticles=boolean], [overSampling=int], [path=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynExport is undoable, NOT queryable, and NOT editable.
For cache export (-format cache), dynExport also sets three attributes
of the current dynGlobals node.  It sets the useParticleRenderCache
attribute to true, and the min/maxFrameOfLastParticleRenderCache
attributes to correspond to the min and max frames.

Exported .pda or .pdb files are assigned a name of form object
name.frame.extension, where extension is "pda" or "pdb."

The naming convention for .pdc files is similar but does not use frame
numbers, it uses a more precise representation of the time instead.

By default, the pda and pdb formats export all per-particle
attributes, and all integer or float type attributes except those
which are hidden or not storable. (Exception: level of detail is not
exported, by default) The pdc format exports all attributes which the
particle object needs for its state cache.

To specify only selected attributes, use the -atr flag (which is
multi-use).  In general, it is recommended not to use this flag with
pdc type, since you need all the attributes in order for the cache to
be useful.

dynExport exports data for the current frame, or for a range of frames
specified with -mnf and -mxf. If you are not already at the start
frame, dynExport will run up the scene for you.  VERY VERY
IMPORTANT NOTE: If you use dynExport in -prompt mode, it does NOT
automatically force evaluation of your objects.  You must do this
yourself from your script.  The easiest way is to request each
particle object's "count" attribute each frame.  You must request the
count attribute for each object you want to export, because their
solvers run independently of one another.  In interactive mode,
objects WILL get evaluated automatically and you don't have to worry
about any of this.

When exporting a particle object whose particles are created from
collisions involving particles in another particle object(s), you must
make sure you simultaneously export all the particle objects involved
in the dependency chain otherwise you will get an empty cache file.

For non-per-particle attributes, pda and pdb formats write the
identical value once for each particle.  The following types of
non-per-particle attributes can be exported: float, double,
doubleLinear, doubleAngle, byte, short, long, enum.  The first four
are exported as "Real" (in PDB parlance), and the last four as
"Integer."

In the pda and pdb formats, "particleId" and "particleId0" are
exported as Integer, and are exported under the names "id" and "id0"
respectively.  All other attributes are exported under their long
names.




Example:
---
import maya.cmds as cmds

cmds.dynExport( 'particle1', mnf=5, mxf=10, os=2, atr=('position', 'velocity'), p='PDB' )

Export position and velocity attributes for particle1
for frames 5 through 10 at every half frame interval,
to files in subdirectory "PDB" of the workspace root
directory. The default format (binary) will be used.

---
Return:
---


    string: Path to the exported files

Flags:
---


---
allObjects(all): boolean
    properties: create
    Ignore the selection list and export all particle objects.
If you also specify an object name, the -all flag will be ignored.

---
attribute(atr): string
    properties: create, multiuse
    Name of attribute to be exported. If any specified object
does not have one of the specified attributes, dynExport will issue
an error and not do the export.

---
format(f): string
    properties: create
    Desired format: "binary" ("pdb"), "ascii" ("pda"), or "cache" ("pdc").
The pdc format is for use by the Maya particle system to
cache particle data.  The pda and pdb format options
are intended for pipelines involving other software (for example,
sending the data to some program written in-house);
Maya cannot read pda or pdb files.
There is no formal description of the PDB format, but the
ExploreMe/particles/readpdb directory contains the source
and Makefile for a small, simple C program called "readpdb"
which reads it. Note that you must compile and run readpdb on the
platform which you exported the files on.

---
maxFrame(mxf): time
    properties: create
    Ending frame to be exported.

---
minFrame(mnf): time
    properties: create
    Starting frame to be exported. The export operation will play the
scene through from min frame to max frame as it exports.

---
onlyUpdateParticles(oup): boolean
    properties: create
    Specify to only update the particles before exporting.

---
overSampling(os): int
    properties: create
    OverSampling to be used during export.

---
path(p): string
    properties: create
    This option allows you to specify a subdirectory of the workspace
"particles" directory where you want the exported files to be stored.
By default, files are stored in the workspace particles directory,
i.e., -path is relative to that directory.
( Please Read This:  This is a change from previous versions of Maya
in which the path was relative to the workspace root directory.)
You can set the "particles" directory anywhere you want using the
project window or workspace -fr command. (In this way, you can use
an absolute path for export).
The -path flag cannot handle strings which include "/" or "\",
in other words, it lets you go down only one level in the directory hierarchy.
If you specify a path which doesn't exist, the action will create it
if possible; if it can't create the path it will warn you and fail.
If you are using a project for which a particle data directory is
not defined, dynExport will create a default one called "particles"
and add it to your workspace.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynExport.html 
    """


def dynExpression(flagcreation: boolean, flagruntime: boolean, flagruntimeAfterDynamics: boolean, flagruntimeBeforeDynamics: boolean, flagstring: string) -> string:
    """Synopsis:
---
---
 dynExpression(
selectionItem
    , [creation=boolean], [runtime=boolean], [runtimeAfterDynamics=boolean], [runtimeBeforeDynamics=boolean], [string=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynExpression is undoable, queryable, and editable.expressionpositionvelocity
If this command is being sent by the command line or in a script, then
the user should be sure to embed escaped newlines (\n), tabs (\t) for
clarity when reading them in the expression editor.  Also, quotes in
an expression must be escaped (\") so that they are not confused by
the system as the end of your string.  When using the expression
editor, these characters are escaped for you unless they are already
within quotes.

This type of expression is executed during the evaluation of the
dynamics.  If an output of the expression is requested before that,
then the dynamics will be force to compute at that time.  If dynamics
is disabled, then these expressions will have no effect.




Example:
---
import maya.cmds as cmds

cmds.dynExpression( 'particleShape1', s='rgbPP = << 1, 0, 0 >>', c=1 )

This expression tells particleShape1 that whenever new particles are
created for this object, then their color should start out as << 1, 0, 0 >>,
which is red.

cmds.dynExpression( 'particleShape1', s='rgbPP = rgbPP * .9;', rbd=1 )

This sets the runtime before dynamics expression for rgbPP.  When a particle is
first "born", its color will be red from the previous example.  Every other frame after
that, its color is reduced by 10 percent each time the expression is executed.

cmds.dynExpression( 'particleShape1', s='rgbPP = rgbPP * .9;', rad=1 )

This sets the runtime after dynamics expression for rgbPP.  When a particle is
first "born", its color will be red from the previous example.  Every other frame after
that, its color is reduced by 10 percent each time the expression is executed.

---
Return:
---


    string: The particle shape which this expression belongs to

Flags:
---


---
creation(c): boolean
    properties: create, query, edit
    Tells the command that the string passed will be a
creation expression for the particle shape.  This means that
this expression will be executed when a particle is emitted
or at the beginning of the scene for existing particles.

---
runtime(r): boolean
    properties: create, query, edit
    Tells the command that the string passed will be a
runtime expression for the particle shape.  This expression
will be executed at the beginning of runtime.

---
runtimeAfterDynamics(rad): boolean
    properties: create, query, edit
    Tells the command that the string passed will be a
runtime expression for the particle shape.  This expression
will be executed after dynamics whenever a particle's age
is greater then zero (0).

---
runtimeBeforeDynamics(rbd): boolean
    properties: create, query, edit
    Tells the command that the string passed will be a
runtime expression for the particle shape.  This expression
will be executed before dynamics whenever a particle's age
is greater then zero (0).

---
string(s): string
    properties: create, edit
    Set the expression string. This is queriable with the -q/query flag and the -rbd/runtimeBeforeDynamics,
the -rab/runtimeAfterDynamics or the -c/creation flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynExpression.html 
    """


def dynGlobals(flagactive: boolean, flaglistAll: boolean, flagoverSampling: int) -> int | string:
    """Synopsis:
---
---
 dynGlobals([active=boolean], [listAll=boolean], [overSampling=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynGlobals is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.dynGlobals( e=True, os=5 )
or
cmds.dynGlobals( os=5 )

Both of these commands will edit the overSampling attribute of
the active dynGlobals node.

---
Return:
---


    string: For edit commands
    int: or string
For query commands, depending on the flag queried.

Flags:
---


---
active(a): boolean
    properties: query
    This flag returns the name of the active dynGlobals node in the
the scene.  Only one dynGlobals node is active. It is the first on
created.  Any additional dynGlobals nodes will be ignored.

---
listAll(la): boolean
    properties: query
    This flag will list all of the dynGlobals nodes in the scene.

---
overSampling(os): int
    properties: query, edit
    This flag will set the current overSampling value for all of
the particle in the scene.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynGlobals.html 
    """


def dynPaintEditor(flagactiveOnly: boolean, flagautoSave: boolean, flagcamera: string, flagcanvasMode: boolean, flagcanvasUndo: boolean, flagchangeCommand: tuple[string, string, string, string], flagclear: tuple[float, float, float], flagcontrol: boolean, flagcurrentCanvasSize: boolean, flagdefineTemplate: string, flagdisplayAppearance: string, flagdisplayFog: boolean, flagdisplayImage: int, flagdisplayLights: string, flagdisplayStyle: string, flagdisplayTextures: boolean, flagdocTag: string, flagdoubleBuffer: boolean, flagdrawAxis: boolean, flagdrawContext: boolean, flagexists: boolean, flagfastUpdate: int, flagfileName: string, flagfilter: string, flagforceMainConnection: string, flaghighlightConnection: string, flagiconGrab: boolean, flagloadImage: string, flaglockMainConnection: boolean, flagmainListConnection: string, flagmenu: string, flagnbImages: boolean, flagnewImage: tuple[int, int, float, float, float], flagpaintAll: float, flagpanel: string, flagparent: string, flagredrawLast: boolean, flagrefresh: boolean, flagrefreshMode: int, flagremoveAllImages: boolean, flagremoveImage: boolean, flagrollImage: tuple[float, float], flagsaveAlpha: boolean, flagsaveBumpmap: string, flagsaveImage: boolean, flagscaleBlue: float, flagscaleGreen: float, flagscaleRed: float, flagselectionConnection: string, flagsingleBuffer: boolean, flagsnapShot: boolean, flagstateString: boolean, flagswap: int, flagtileSize: int, flagunParent: boolean, flagundoCache: boolean, flagunlockMainConnection: boolean, flagupdateMainConnection: boolean, flaguseTemplate: string, flagwrap: tuple[boolean, boolean], flagwriteImage: string, flagzoom: float) -> string:
    """Synopsis:
---
---
 dynPaintEditor(
editorName
    , [activeOnly=boolean], [autoSave=boolean], [camera=string], [canvasMode=boolean], [canvasUndo=boolean], [changeCommand=[string, string, string, string]], [clear=[float, float, float]], [control=boolean], [currentCanvasSize=boolean], [defineTemplate=string], [displayAppearance=string], [displayFog=boolean], [displayImage=int], [displayLights=string], [displayStyle=string], [displayTextures=boolean], [docTag=string], [doubleBuffer=boolean], [drawAxis=boolean], [drawContext=boolean], [exists=boolean], [fastUpdate=int], [fileName=string], [filter=string], [forceMainConnection=string], [highlightConnection=string], [iconGrab=boolean], [loadImage=string], [lockMainConnection=boolean], [mainListConnection=string], [menu=string], [nbImages=boolean], [newImage=[int, int, float, float, float]], [paintAll=float], [panel=string], [parent=string], [redrawLast=boolean], [refresh=boolean], [refreshMode=int], [removeAllImages=boolean], [removeImage=boolean], [rollImage=[float, float]], [saveAlpha=boolean], [saveBumpmap=string], [saveImage=boolean], [scaleBlue=float], [scaleGreen=float], [scaleRed=float], [selectionConnection=string], [singleBuffer=boolean], [snapShot=boolean], [stateString=boolean], [swap=int], [tileSize=int], [unParent=boolean], [undoCache=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string], [wrap=[boolean, boolean]], [writeImage=string], [zoom=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynPaintEditor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.dynPaintEditor( 'editor' )

cmds.dynPaintEditor( 'editor', e=True, ni=(640, 480, 1.0, 0.5, 0.2) )

---
Return:
---


    string: Editor name

Flags:
---


---
activeOnly(ao): boolean
    properties: query, edit
    For Scene mode, this determines if only the active strokes will
be refreshed.

---
autoSave(autoSave): boolean
    properties: query, edit
    For Canvas mode, this determines if the buffer will be saved
to a disk file after every stroke. Good for painting textures and
viewing the results in shaded display in the model view.

---
camera(cam): string
    properties: query, edit
    Sets the name of the camera which the Paint Effects panel
looks through.

---
canvasMode(cm): boolean
    properties: query, edit
    Sets the Paint Effects panel into Canvas mode if true.

---
canvasUndo(cu): boolean
    properties: edit
    Does a fast undo in Canvas mode. This is a special undo because
we are not using any history when we paint in Canvas mode so we
provide a single level undo for the Canvas.

---
changeCommand(cc): [string, string, string, string]
    properties: create, query, edit
    Parameters:

First string: command
Second string: editorName
Third string: editorCmd
Fourth string: updateFunc


Call the command when something changes in the editor The command
should have this prototype :

command(string $editor, string $editorCmd, string $updateFunc, int $reason)

The possible reasons could be :

0: no particular reason
1: scale color
2: buffer (single/double)
3: axis 
4: image displayed
5: image saved in memory

---
clear(cl): [float, float, float]
    properties: edit
    Clears the buffer (if in Canvas mode) to the floating point
values (R,G,B).

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
currentCanvasSize(ccs): boolean
    properties: query
    In Query mode, this returns the (X,Y) resolution of the
current canvas.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
displayAppearance(dsa): string
    properties: query, edit
    Sets the display appearance of the model panel.  Possible
values are "wireframe", "points", "boundingBox", "smoothShaded",
"flatShaded".  This flag may be used with the -interactive
and -default flags.  Note that only "wireframe", "points", and
"boundingBox" are valid for the interactive mode.

---
displayFog(dfg): boolean
    properties: query, edit
    For Scene mode, this determines if fog will be displayed in
the Paint Effects panel when refreshing the scene. If fog is on,
but this is off, fog will only be drawn on the strokes, not the
rest of the scene.

---
displayImage(di): int
    properties: query, edit
    Set a particular image in the Editor Image Stack as the current Editor Image.
Images are added to the Editor Image Stack using the "si/saveImage" flag.

---
displayLights(dsl): string
    properties: query, edit
    Sets the lighting for shaded mode.  Possible values are "selected",
"active", "all", "default".

---
displayStyle(dst): string
    properties: create, query, edit
    Set the mode to display the image. Valid values are:

"color" to display the basic RGB image
"mask" to display the mask channel
"lum" to display the luminance of the image

---
displayTextures(dtx): boolean
    properties: query, edit
    Turns on or off display of textures in shaded mode

---
docTag(dtg): string
    properties: create, query, edit
    Attaches a tag to the editor.

---
doubleBuffer(dbf): boolean
    properties: create, query, edit
    Set the display in double buffer mode

---
drawAxis(da): boolean
    properties: create, query, edit
    Set or query whether the axis will be drawn.

---
drawContext(drc): boolean
    properties: query
    Returns the name of the context.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
fastUpdate(fu): int
    properties: 
    Obsolete - do not use

---
fileName(fil): string
    properties: query, edit
    This sets the file to which the canvas will be saved.

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
iconGrab(ig): boolean
    properties: edit
    This puts the Paint Effects panel into Grab Icon mode where the
user is expected to drag out a section of the screen to be made into
an icon.

---
loadImage(li): string
    properties: edit
    load an image from disk and set it as the current Editor Image

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
menu(mn): string
    properties: create
    Sets the name of the script used to build a menu in the editor. The script
takes the editor name as an argument.

---
nbImages(nim): boolean
    properties: query
    returns the number of images

---
newImage(ni): [int, int, float, float, float]
    properties: query, edit
    Starts a new image in edit mode, setting the resolution to
the integer values (X,Y) and clearing the buffer to the floating point
values (R,G,B). In Query mode, this returns the (X,Y) resolution of the
current Image.

---
paintAll(pa): float
    properties: edit
    Redraws the buffer in current refresh mode.

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
redrawLast(rl): boolean
    properties: edit
    Redraws the last stroke again. Useful when it's brush has just
changed. This feature does a fast undo and redraws the stroke again.

---
refresh(ref): boolean
    properties: edit
    requests a refresh of the current Editor Image.

---
refreshMode(rmd): int
    properties: query, edit
    Sets the refresh mode to the specified value. 0 - Do not draw
strokes on refresh, 1 - Redraw strokes in wireframe mode, 2 -
Redraw strokes in final rendered mode.

---
removeAllImages(ra): boolean
    properties: edit
    remove all the Editor Images from the Editor Image Stack

---
removeImage(ri): boolean
    properties: edit
    remove the current Editor Image from the Editor Image Stack

---
rollImage(rig): [float, float]
    properties: edit
    In Canvas mode, this rolls the image by the floating point
values (X,Y). X and Y are between 0 (no roll) and 1 (full roll). A
value of .5 rolls the image 50% (ie. the border moves to the center of the screen.

---
saveAlpha(sa): boolean
    properties: query, edit
    For Canvas mode, this determines if the alpha will be saved when
storing the canvas to a disk file.

---
saveBumpmap(sbm): string
    properties: query, edit
    Saves the current buffer as a bump map to the specified file.

---
saveImage(si): boolean
    properties: edit
    save the current Editor Image to memory. Saved Editor Images are
stored in an Editor Image Stack. The most recently saved image is stored in
position 0, the second most recently saved image in position 1,
and so on... To set the current Editor Image to a previously saved
image use the "di/displayImage" flag.

---
scaleBlue(sb): float
    properties: create, query, edit
    Define the scaling factor for the blue component
in the View. The default value is 1 and can be
between -1000 to +1000

---
scaleGreen(sg): float
    properties: create, query, edit
    Define the scaling factor for the green component
in the View. The default value is 1 and can be
between -1000 to +1000

---
scaleRed(sr): float
    properties: create, query, edit
    Define the scaling factor for the red component
in the View. The default value is 1 and can be
between -1000 to +1000

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
singleBuffer(sbf): boolean
    properties: create, query, edit
    Set the display in single buffer mode

---
snapShot(snp): boolean
    properties: edit
    Takes a snapshot of the current camera view.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
swap(swp): int
    properties: 
    Obsolete - do not use

---
tileSize(ts): int
    properties: edit
    Sets the size of the tile for the hardware texture redraw of the display buffer.

---
unParent(up): boolean
    properties: create, edit
    Specifies that the editor should be removed from its layout.
This cannot be used in query mode.

---
undoCache(uc): boolean
    properties: edit
    By default the last image is cached for undo. If this is set false, then
undoing will be disabled in canvas mode and undo in scene mode will force a full
refresh. Less memory will be used if this is set false before the first clear or
refresh of the current scene.

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
wrap(wr): [boolean, boolean]
    properties: query, edit
    For Canvas mode, should the buffer wrap in U, and V
(respectively) when painting.

---
writeImage(wi): string
    properties: edit
    write the current Editor Image to disk

---
zoom(zm): float
    properties: query, edit
    Zooms the Canvas image by the specified value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynPaintEditor.html 
    """


def dynParticleCtx(flagconserve: float, flagcursorPlacement: boolean, flagexists: boolean, flaggrid: boolean, flaggridSpacing: float, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagjitterRadius: float, flaglowerLeftX: float, flaglowerLeftY: float, flaglowerLeftZ: float, flagname: string, flagnucleus: boolean, flagnumJitters: int, flagparticleName: string, flagsketch: boolean, flagsketchInterval: int, flagtextPlacement: boolean, flagupperRightX: float, flagupperRightY: float, flagupperZ: float) -> None:
    """Synopsis:
---
---
 dynParticleCtx(
string
    , [conserve=float], [cursorPlacement=boolean], [exists=boolean], [grid=boolean], [gridSpacing=float], [history=boolean], [image1=string], [image2=string], [image3=string], [jitterRadius=float], [lowerLeftX=float], [lowerLeftY=float], [lowerLeftZ=float], [name=string], [nucleus=boolean], [numJitters=int], [particleName=string], [sketch=boolean], [sketchInterval=int], [textPlacement=boolean], [upperRightX=float], [upperRightY=float], [upperZ=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynParticleCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.dynParticleCtx( 'dynParticleContext', e=True, nj=5, jr=1.5 )
Set the option values for number of jitters to 5 and jitter
radius to 1.5 in the particle context, which will result in
creating 5 particles for each mouse click in the viewport,
randomly placed, but all within 1.5 units of the mouse click.

---


Flags:
---


---
conserve(c): float
    properties: query, edit
    Conservation of momentum control (between 0 and 1). For smaller
values, the field will tend to erase any existing velocity the object
has (in other words, will not conserve momentum from frame to frame).
A value of 1 (the default) corresponds to the true physical law
of conservation of momentum.

---
cursorPlacement(cp): boolean
    properties: query, edit
    Use the cursor to place the lower left and upper right of the grid.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
grid(gr): boolean
    properties: query, edit
    Create a particle grid.

---
gridSpacing(grs): float
    properties: query, edit
    Spacing between particles in the grid.

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
jitterRadius(jr): float
    properties: query, edit
    Max radius from the center to place the particle instances.

---
lowerLeftX(llx): float
    properties: query, edit
    Lower left X position of the particle grid.

---
lowerLeftY(lly): float
    properties: query, edit
    Lower left Y position of the particle grid.

---
lowerLeftZ(llz): float
    properties: query, edit
    Lower left Z position of the particle grid.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
nucleus(nc): boolean
    properties: query, edit
    If set true then an nParticle is generated with a nucleus node connection.
Otherwise a standard particle is created.

---
numJitters(nj): int
    properties: query, edit
    Number of jitters (instances) per particle.

---
particleName(pn): string
    properties: query, edit
    Particle name.

---
sketch(sk): boolean
    properties: query, edit
    Create particles in sketch mode.

---
sketchInterval(ski): int
    properties: query, edit
    Interval between particles, when in sketch mode.

---
textPlacement(tp): boolean
    properties: query, edit
    Use the textfields to specify the lower left and upper right of/
the grid.

---
upperRightX(urx): float
    properties: query, edit
    Upper right X position of the particle grid.

---
upperRightY(ury): float
    properties: query, edit
    Upper right Y position of the particle grid.

---
upperZ(urz): float
    properties: query, edit
    Upper right Z position of the particle grid.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynParticleCtx.html 
    """


def dynPref(flagautoCreate: boolean, flagechoCollision: boolean, flagrunupFrom: int, flagrunupToCurrentTime: boolean, flagsaveOnQuit: boolean, flagsaveRuntimeState: boolean) -> None:
    """Synopsis:
---
---
 dynPref([autoCreate=boolean], [echoCollision=boolean], [runupFrom=int], [runupToCurrentTime=boolean], [saveOnQuit=boolean], [saveRuntimeState=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynPref is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Sets autoCreate rigid bodies to "on"
cmds.dynPref( autoCreate=1 )

---


Flags:
---


---
autoCreate(ac): boolean
    properties: create, query
    If on, autoCreate rigid bodies.

---
echoCollision(ec): boolean
    properties: create, query
    If on, will cause particle systems to echo to the Script Editor the
command that they are running for each particle collision event.
If off, only the output of the command will be echoed.

---
runupFrom(rf): int
    properties: create, query
    If on, run up from previous time; if 2, run up from start time

---
runupToCurrentTime(rt): boolean
    properties: create, query
    If on, run up the scene to current time

---
saveOnQuit(sq): boolean
    properties: create, query
    If on, save the current values of preferences to userPrefs file.

---
saveRuntimeState(sr): boolean
    properties: create, query
    If on, runtime state as well as initial state of all particle objects
will be saved to file. If off, only initial state will be saved.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynPref.html 
    """


def dynamicLoad() -> None:
    """Synopsis:
---
---
 dynamicLoad(
string
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

dynamicLoad is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.dynamicLoad( 'libDynSlice.dll' )

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/dynamicLoad.html 
    """
