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


def querySubdiv(flagaction: int, flaglevel: int, flagrelative: boolean) -> boolean:
    """Synopsis:
---
---
 querySubdiv([action=int], [level=int], [relative=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

querySubdiv is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

find all tweaked verticies at current level
cmds.querySubdiv( a=1 )

find all tweaked verticies one level finer than current level
cmds.querySubdiv( a=1, l=1, r=True )

find all creased verticies at current level
cmds.querySubdiv( a=2 )

find all creased edges at current level
cmds.querySubdiv( a=3 )

find all faces at current level.
You should work with the subdivision surface shape.
---

cmds.querySubdiv( 'subdivShape1', a=4 )

find all faces at level 1.
---

cmds.querySubdiv( 'subdivShape1', a=4, level=1, relative=False )

find all faces at the next finest level from the current one.
---

cmds.querySubdiv( 'subdivShape1', a=4, level=1, relative=True )

---
Return:
---


    boolean: Command result

Flags:
---


---
action(a): int
    properties: create
    Specifies the query parameter:
        1 = find all tweaked verticies at level
        2 = find all sharpened vertices at level
        3 = find all sharpened edges at level
        4 = find all faces at level
If the attribute "level" is not specified then the query is applied to
the current component display level. If the attribute level is
specified then the query is applied to that level, either absolute or
relative to the current level based on the "relative" flag state.

---
level(l): int
    properties: create
    Specify the level of the subdivision surface on which to perform the operation.

---
relative(r): boolean
    properties: create
    If set, level flag refers to the level relative to the current component display level.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/querySubdiv.html 
    """


def quit(flagabort: boolean, flagexitCode: uint, flagforce: boolean) -> None:
    """Synopsis:
---
---
 quit([abort=boolean], [exitCode=uint], [force=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

quit is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.quit()
cmds.quit(force=True)

---


Flags:
---


---
abort(a): boolean
    properties: create
    Will quit without saving like -force, but will also prevent
preferences/hotkeys/colors from being saved.  Use at
your own risk.

---
exitCode(ec): uint
    properties: create
    Specifies the exit code to be returned once the application
exits.  The default exit code is 0.

---
force(f): boolean
    properties: create
    If specified, this flag will force a quit without saving
or prompting for saving changes. Use at
your own risk.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/quit.html 
    """
