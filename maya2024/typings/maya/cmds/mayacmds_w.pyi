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


def waitCursor(flagstate: boolean) -> boolean:
    """Synopsis:
---
---
 waitCursor([state=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

waitCursor is undoable, queryable, and NOT editable.waitCursor -state onwaitCursor -state offWarning: If a script fails that has turned
the wait cursor on, the wait cursor may be left on.
You need to turn it off manually from the command line by entering
and executing the command 'waitCursor -state off'.




Example:
---
import maya.cmds as cmds

cmds.waitCursor( state=True )
cmds.waitCursor( state=False )

---
Return:
---


    boolean: True if the wait cursor is on.

Flags:
---


---
state(st): boolean
    properties: create, query
    Set or reset the wait cursor for the entire Maya application.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/waitCursor.html 
    """


def walkCtx(flagalternateContext: boolean, flagcrouchCount: float, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagtoolName: string, flagwalkHeight: float, flagwalkSensitivity: float, flagwalkSpeed: float, flagwalkToolHud: boolean) -> string:
    """Synopsis:
---
---
 walkCtx([alternateContext=boolean], [crouchCount=float], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [toolName=string], [walkHeight=float], [walkSensitivity=float], [walkSpeed=float], [walkToolHud=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

walkCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.walkCtx( 'walkContext', ws=2.0 )

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
crouchCount(wcc): float
    properties: create, query, edit
    The camera crouch count.

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

---
walkHeight(wh): float
    properties: create, query, edit
    The camera initial height.

---
walkSensitivity(wsv): float
    properties: create, query, edit
    The camera rotate sensitivity.

---
walkSpeed(ws): float
    properties: create, query, edit
    The camera move speed.

---
walkToolHud(wth): boolean
    properties: create, query, edit
    Control whether show walk tool HUD.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/walkCtx.html 
    """


def warning(flagnoContext: boolean, flagshowLineNumber: boolean) -> None:
    """Synopsis:
---
---
 warning([noContext=boolean], [showLineNumber=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

warning is NOT undoable, NOT queryable, and NOT editable.
The warning command is provided so that the user can issue warning
messages from his/her scripts.
The string argument is displayed in the command window (or stdout if
running in batch mode) after being prefixed with a warning message heading
and surrounded by the appropriate language separators
(# for Python, // for Mel).




Example:
---
import maya.cmds as cmds


import maya.cmds as cmds
def lightWarning():
    l = cmds.ls( lights=True )
    if len(l) == 0:
        cmds.warning( "No Lights" )
lightWarning()

---

The above will produce the following output:
---

  Warning: No Lights ---

---

When the option to show line numbers in errors is enabled the output will
be the following:
---

  Warning: line 4 of 'lightWarning' in '<maya console'>: No Lights ---

---


---


Flags:
---


---
noContext(n): boolean
    properties: create
    Do not include the context information with the warning message.

---
showLineNumber(sl): boolean
    properties: create
    Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the
script editor that enables line number display instead.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/warning.html 
    """


def webBrowser(flagannotation: string, flagback: boolean, flagbackgroundColor: tuple[float, float, float], flagdefineTemplate: string, flagdocTag: string, flagdragCallback: script, flagdropCallback: script, flagenable: boolean, flagenableBackground: boolean, flagenableKeyboardFocus: boolean, flagexists: boolean, flagfind: string, flagforward: boolean, flagfullPathName: boolean, flagheight: int, flaghighlightColor: tuple[float, float, float], flaghome: boolean, flagisObscured: boolean, flagmanage: boolean, flagmatchCase: boolean, flagmatchWholeWorld: boolean, flagnoBackground: boolean, flagnumberOfPopupMenus: boolean, flagopenURL: string, flagparent: string, flagpopupMenuArray: boolean, flagpreventOverride: boolean, flagreload: boolean, flagsearchForward: boolean, flagstatusBarMessage: string, flagstop: boolean, flagurlChangedCb: string, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: int, flagwrap: boolean) -> string:
    """Synopsis:
---
---
 webBrowser(
[string]
    , [annotation=string], [back=boolean], [backgroundColor=[float, float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [find=string], [forward=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [home=boolean], [isObscured=boolean], [manage=boolean], [matchCase=boolean], [matchWholeWorld=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [openURL=string], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [reload=boolean], [searchForward=boolean], [statusBarMessage=string], [stop=boolean], [urlChangedCb=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int], [wrap=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

webBrowser is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
browser = cmds.webBrowser(width=800, height=600, url='www.alias.com')
cmds.showWindow()

---
Return:
---


    string: Full path name to the control

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
back(bk): boolean
    properties: create
    Go back a page

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
find(f): string
    properties: create
    Find text in a page

---
forward(fwd): boolean
    properties: create
    Go forward a page

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
home(hm): boolean
    properties: create
    Go to the home page

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
matchCase(mc): boolean
    properties: create
    True if the match should respect the case

---
matchWholeWorld(mww): boolean
    properties: create
    True if the match should check the whole world

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
openURL(url): string
    properties: create, query, edit
    Open the named URL

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
reload(rl): boolean
    properties: create
    Reload the current page

---
searchForward(sf): boolean
    properties: create
    True if search should be going forward from the current location

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
stop(st): boolean
    properties: create
    Stop loading a page

---
urlChangedCb(ucc): string
    properties: create
    Command to call when the URL changes

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

---
wrap(wr): boolean
    properties: create
    Set to true if the page should wrap

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/webBrowser.html 
    """


def weightsColor(flagcolorRamp: string, flagdeformer: string, flagfalseColor: boolean, flagoutOfRangeColor: tuple[float, float, float], flagrampMaxColor: tuple[float, float, float], flagrampMinColor: tuple[float, float, float], flaguseColorRamp: boolean, flaguseMaxMinColor: boolean) -> list[string]:
    """Synopsis:
---
---
 weightsColor(
[objects...]
    , [colorRamp=string], [deformer=string], [falseColor=boolean], [outOfRangeColor=[float, float, float]], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float, float]], [useColorRamp=boolean], [useMaxMinColor=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

weightsColor is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Turn on weight visualization for the cluster1 deformer on pSphere1
cmds.weightsColor('pSphere1', fc=True, dfm='cluster1')

Turn off weight visualization for pSphere1
cmds.weightsColor('pSphere1', fc=False)

Turn of the colorRamp
cmds.weightsColor(useColorRamp=False)

Use a purple min color and green max color
cmds.weightsColor(umc=True, rmc=(1.0,0.0,1.0), rxc=(0.0,1.0,0.0))

Set the outOfRange color for verts outside the deformers subset
cmds.weightsColor(orc=(0.0,1.0,1.0))

---
Return:
---


    list[string]: For query operation

Flags:
---


---
colorRamp(cr): string
    properties: query
    Allows a user defined color ramp to be used to map values to colors.

---
deformer(dfm): string
    properties: query
    Specify the deformer that needs to be visualized.

---
falseColor(fc): boolean
    properties: query
    Enable or disable false color display on the geometry.

---
outOfRangeColor(orc): [float, float, float]
    properties: query
    Defines a special color to be used for the areas outside the deformers subset.

---
rampMaxColor(rxc): [float, float, float]
    properties: query
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
rampMinColor(rmc): [float, float, float]
    properties: query
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
useColorRamp(ucr): boolean
    properties: query
    Specifies whether the user defined color ramp should be used to map values
from to colors. If this is turned off, the default greyscale feedback
will be used.

---
useMaxMinColor(umc): boolean
    properties: query
    Specifies whether the out of range colors should be used.  See rampMinColor
and rampMaxColor flags for further details.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/weightsColor.html 
    """


def whatsNewHighlight(flaghighlightColor: tuple[float, float, float], flaghighlightOn: boolean, flagshowStartupDialog: boolean) -> None:
    """Synopsis:
---
---
 whatsNewHighlight([highlightColor=[float, float, float]], [highlightOn=boolean], [showStartupDialog=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

whatsNewHighlight is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

   Turn on What's New highlighting if not already on.
---

if not cmds.whatsNewHighlight(query=True, highlightOn=True):
    cmds.whatsNewHighlight(highlightOn=True)

   Turn off What's New highlighting startup dialog if it is set to appear.
---

if cmds.whatsNewHighlight(query=True, showStartupDialog=True):
    cmds.whatsNewHighlight(showStartupDialog=False)

---


Flags:
---


---
highlightColor(hc): [float, float, float]
    properties: create, query
    Set the color of the What's New highlight. The arguments correspond to
the red, green, and blue color components. Each color component ranges
in value from 0.0 to 1.0.

---
highlightOn(ho): boolean
    properties: create, query
    Toggle the What's New highlighting feature. When turned on, menu items
and buttons introduced in the latest version will be highlighted.

---
showStartupDialog(ssd): boolean
    properties: create, query
    Set whether the settings dialog for this feature appears on startup.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/whatsNewHighlight.html 
    """


def window(flagbackgroundColor: tuple[float, float, float], flagcloseCommand: script, flagdefineTemplate: string, flagdocTag: string, flagdockCorner: tuple[string, string], flagdockStation: boolean, flagdockingLayout: string, flagexists: boolean, flagfrontWindow: boolean, flagheight: int, flagiconName: string, flagiconify: boolean, flaginteractivePlacement: boolean, flagleftEdge: int, flagmainMenuBar: boolean, flagmainWindow: boolean, flagmaximizeButton: boolean, flagmenuArray: boolean, flagmenuBar: boolean, flagmenuBarCornerWidget: tuple[string, string], flagmenuBarResize: boolean, flagmenuBarVisible: boolean, flagmenuIndex: tuple[string, uint], flagminimizeButton: boolean, flagminimizeCommand: script, flagnestedDockingEnabled: boolean, flagnumberOfMenus: boolean, flagparent: string, flagresizeToFitChildren: boolean, flagrestoreCommand: script, flagretain: boolean, flagsizeable: boolean, flagstate: string, flagtitle: string, flagtitleBar: boolean, flagtitleBarMenu: boolean, flagtoolbox: boolean, flagtopEdge: int, flagtopLeftCorner: tuple[int, int], flaguseTemplate: string, flagvisible: boolean, flagwidth: int, flagwidthHeight: tuple[int, int]) -> string:
    """Synopsis:
---
---
 window(
[string]
    , [backgroundColor=[float, float, float]], [closeCommand=script], [defineTemplate=string], [docTag=string], [dockCorner=[string, string]], [dockStation=boolean], [dockingLayout=string], [exists=boolean], [frontWindow=boolean], [height=int], [iconName=string], [iconify=boolean], [interactivePlacement=boolean], [leftEdge=int], [mainMenuBar=boolean], [mainWindow=boolean], [maximizeButton=boolean], [menuArray=boolean], [menuBar=boolean], [menuBarCornerWidget=[string, string]], [menuBarResize=boolean], [menuBarVisible=boolean], [menuIndex=[string, uint]], [minimizeButton=boolean], [minimizeCommand=script], [nestedDockingEnabled=boolean], [numberOfMenus=boolean], [parent=string], [resizeToFitChildren=boolean], [restoreCommand=script], [retain=boolean], [sizeable=boolean], [state=string], [title=string], [titleBar=boolean], [titleBarMenu=boolean], [toolbox=boolean], [topEdge=int], [topLeftCorner=[int, int]], [useTemplate=string], [visible=boolean], [width=int], [widthHeight=[int, int]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

window is undoable, queryable, and editable.
Note: The window will require a control layout of some kind
to arrange the controls (buttons, sliders, fields, etc.).  Examples of
control layouts are columnLayout, formLayout, rowLayout, etc.

Note: This command will clear the uiTemplate stack.  Templates for
a window need to be set after the window cmd.




Example:
---
import maya.cmds as cmds

Make a new window
---

window = cmds.window( title="Long Name", iconName='Short Name', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Do Nothing' )
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.showWindow( window )

Resize the main window
---


This is a workaround to get MEL global variable value in Python
gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
cmds.window( gMainWindow, edit=True, widthHeight=(900, 777) )

Add a menu to the right of the main window's menu bar.
---

import maya.cmds as cmds;

cmds.setParent ( "" )
menuName = "menuTest"
cmds.optionMenu( menuName, label='test menu')
cmds.menuItem( label='item 1', parent = menuName )
cmds.menuItem( label='item 2', parent = menuName )
cmds.menuItem( label='item 3', parent = menuName )

cmds.window ("MayaWindow", edit=True, menuBarCornerWidget = (menuName, "topRight") )

---
Return:
---


    string: Name to the window.

Flags:
---


---
backgroundColor(bgc): [float, float, float]
    properties: create, edit
    The background color of the window. The arguments correspond
to the red, green, and blue color components. Each component ranges
in value from 0.0 to 1.0.

---
closeCommand(cc): script
    properties: create, edit
    Script executed after the window is closed.

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
    Attach a tag to the window.

---
dockCorner(dc): [string, string]
    properties: create, multiuse
    Specifies which docking areas occupied the four different corners of the window.
By default docking windows on the bottom or top will span the whole window.
Use multiple instances of this flag to allow the left and right docking areas to occupy the corners.
This method has two arguments: docking corner and docking area.
Possible values for docking corner are "topLeft", "topRight", bottomLeft", and "bottomRight".
Possible values for docking area are "left", "right", "top", and "bottom".

---
dockStation(ds): boolean
    properties: create
    When set this flag specifies that this window can contain other docked sub-windows.

---
dockingLayout(dl): string
    properties: create, query, edit
    When queried this flag will return a string holding the docking layout information.
This string can be set when creating or editing a docking station to restore the previous docking layout.
This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,
but can be saved and loaded using the optionVar command to restore layouts across sessions of Maya.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
frontWindow(fw): boolean
    properties: query
    Return the name of the front window.  Note: you must supply
the name of any window (the window does not need to exist).
Returns "unknown" if the front window cannot be determined.

---
height(h): int
    properties: create, query, edit
    Height of the window excluding any window frame in pixels.

---
iconName(iconName): string
    properties: create, query, edit
    The window's icon title.  By default it is the same as the
window's title.

---
iconify(i): boolean
    properties: create, query, edit
    Icon state of the window.

---
interactivePlacement(ip): boolean
    properties: create
    Deprecated flag. Recognized but not implemented.
This flag will be removed in a future version of Maya.

---
leftEdge(le): int
    properties: create, query, edit
    Position of the left edge of the window.

---
mainMenuBar(mm): boolean
    properties: create, query, edit
    If this flag is used then the main menu bar will be enabled.

---
mainWindow(mw): boolean
    properties: create, query, edit
    Main window for the application.  The main window
has an 'Exit' item in the Window Manager menu.  By default, the
first created window becomes the main window.

---
maximizeButton(mxb): boolean
    properties: create, query, edit
    Turns the window's maximize button on or off.

---
menuArray(ma): boolean
    properties: query
    Return a string array containing the names of the menus in
the window's menu bar.

---
menuBar(mb): boolean
    properties: create, query
    Adds an empty menu bar to the window.
The Qt name of the object will be m_menubar_nameOfTheWindow.

---
menuBarCornerWidget(mcw): [string, string]
    properties: query, edit
    This flag specifies a widget to add to a corner of the parent window.
The first argument corresponds to the widget name and the second to the position of the widget.
Possible values for widget position are "topLeft", "topRight", "bottomLeft", "bottomRight".
In query mode this flag returns all the corner widget names in the following order: topLeft, topRight, bottomLeft, bottomRight.
Add the -mbr/-menuBarResize flag to the changeCommand of widget passed (first argument) so that it will always have an
appropriate size.

---
menuBarResize(mbr): boolean
    properties: edit
    This flag should be used with the -mcw/-menuBarCornerWidget flag. This is used to resize the
menu bar so that the corner widgets are updated.

---
menuBarVisible(mbv): boolean
    properties: create, query, edit
    Visibility of the menu bar (if there is one).

---
menuIndex(mi): [string, uint]
    properties: edit
    Sets the index of a specified menu.

---
minimizeButton(mnb): boolean
    properties: create, query, edit
    Turns the window's minimize button on or off.

---
minimizeCommand(mnc): script
    properties: create, edit
    Script executed after the window is minimized (iconified).

---
nestedDockingEnabled(nde): boolean
    properties: create
    Controls whether nested docking is enabled or not.  Nested docking allows
for docking windows next to other docked windows for more possible arrangement styles.

---
numberOfMenus(nm): boolean
    properties: query
    Return the number of menus attached to the window's menu bar.

---
parent(p): string
    properties: create
    Specifies a parent window or layout which the created window is
always on top of. Note: If the parent is a window the created window
is not modal, so events are still propagated to the parent window.

---
resizeToFitChildren(rtf): boolean
    properties: create, query, edit
    The window will always grow/shrink to just fit
the controls it contains.

---
restoreCommand(rc): script
    properties: create, edit
    Script executed after the window is restored from
it's minimized (iconified) state.

---
retain(ret): boolean
    properties: create
    Retains the window after it has been closed.  The default is
to delete the window when it is closed.

---
sizeable(s): boolean
    properties: create, query, edit
    Whether or not the window may be interactively resized.

---
state(st): string
    properties: create, query, edit
    When queried this flag will return a string holding the window state information.
This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,
but can be saved and loaded using the optionVar command to restore window state across sessions of Maya.

---
title(t): string
    properties: create, query, edit
    The window's title.

---
titleBar(tb): boolean
    properties: create, query, edit
    Turns the window's title bar on or off.

---
titleBarMenu(tbm): boolean
    properties: create, query, edit
    Controls whether the title bar menu exists in the window
title bar. Only valid if -tb/titleBar is true. This Windows
only flag is true by default.

---
toolbox(tlb): boolean
    properties: create, query, edit
    Makes this a toolbox style window.  A Windows only
flag that makes the title bar smaller and uses a slightly
different display style.

---
topEdge(te): int
    properties: create, query, edit
    Position of the top edge of the window.

---
topLeftCorner(tlc): [int, int]
    properties: create, query, edit
    Position of the window's top left corner.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The window's visibility.

---
width(w): int
    properties: create, query, edit
    Width of the window excluding any window frame in pixels.

---
widthHeight(wh): [int, int]
    properties: create, query, edit
    Window's width and height excluding any window frame in pixels.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/window.html 
    """


def windowPref(flagenableAll: boolean, flagexists: boolean, flagheight: int, flagleftEdge: int, flagloadAll: boolean, flagmaximized: boolean, flagparentMain: boolean, flagremove: boolean, flagremoveAll: boolean, flagrestoreMainWindowState: string, flagsaveAll: boolean, flagsaveMainWindowState: string, flagtopEdge: int, flagtopLeftCorner: tuple[int, int], flagwidth: int, flagwidthHeight: tuple[int, int]) -> None:
    """Synopsis:
---
---
 windowPref(
string
    , [enableAll=boolean], [exists=boolean], [height=int], [leftEdge=int], [loadAll=boolean], [maximized=boolean], [parentMain=boolean], [remove=boolean], [removeAll=boolean], [restoreMainWindowState=string], [saveAll=boolean], [saveMainWindowState=string], [topEdge=int], [topLeftCorner=[int, int]], [width=int], [widthHeight=[int, int]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

windowPref is undoable, queryable, and editable.
Note that window preferences are not applied to the main Maya window
nor the Command window.




Example:
---
import maya.cmds as cmds

   Check if the window exists.
---

if cmds.window('ExampleWindow', exists=True):
        cmds.deleteUI('ExampleWindow', window=True)

   Create a window.
---

cmds.window( 'ExampleWindow' )
cmds.columnLayout()
cmds.text( label='Size and position the window before closing it.' )
cmds.button( label='Close', command='cmds.deleteUI("ExampleWindow", window=True)' )
cmds.showWindow( 'ExampleWindow' )

   When the window is closed a window preference object is
   created for the window. It has the same name as the window
   object.
---

cmds.windowPref( 'ExampleWindow', exists=True )

   Query the window preference size and position.
---

cmds.windowPref( 'ExampleWindow', query=True, topLeftCorner=True )
cmds.windowPref( 'ExampleWindow', query=True, widthHeight=True )

   Create a window with the same name. When it is shown
   it will be sized and positioned according to the
   window preference.
---

if cmds.window('ExampleWindow', exists=True):
        cmds.deleteUI('ExampleWindow', window=True)

cmds.window( 'ExampleWindow' )
cmds.columnLayout()
cmds.text( label='Size and position the window before closing it.' )
cmds.button( label='Close', command='cmds.deleteUI("ExampleWindow", window=True)' )
cmds.showWindow( 'ExampleWindow' )

   Delete the window preference and the window will have a
   default size and position.
---

cmds.windowPref( 'ExampleWindow', remove=True )

   Create the window one last time.
---

if cmds.window('ExampleWindow', exists=True):
        cmds.deleteUI('ExampleWindow', window=True)

cmds.window( 'ExampleWindow' )
cmds.columnLayout()
cmds.text( label='Size and position the window before closing it.' )
cmds.button( label='Close', command='cmds.deleteUI("ExampleWindow", window=True)' )
cmds.showWindow( 'ExampleWindow' )

---


Flags:
---


---
enableAll(ea): boolean
    properties: create, query
    Enable/disable all window preferences.  Preferences are enabled
by default.  Set this flag to false and window's will ignore all
preference values.

---
exists(ex): boolean
    properties: create
    Returns true|false depending upon whether the specified object
exists. Other flags are ignored.

---
height(h): int
    properties: create, query, edit
    Height of the window.

---
leftEdge(le): int
    properties: create, query, edit
    Left edge position of the window.

---
loadAll(la): boolean
    properties: create
    Reads in file with window attributes from disk.

---
maximized(max): boolean
    properties: create, query, edit
    Maximize the window.

---
parentMain(pm): boolean
    properties: create, query
    Set whether window is parented to main application window. Windows only.

---
remove(r): boolean
    properties: create
    Remove a window preference.

---
removeAll(ra): boolean
    properties: create
    Remove all window preferences.

---
restoreMainWindowState(rms): string
    properties: create
    Reads in file with main window state (positions of toolbars and dock controls).

---
saveAll(sa): boolean
    properties: create
    Writes out file with window attributes.

---
saveMainWindowState(sms): string
    properties: create
    Writes out file with main window state (positions of toolbars and dock controls).

---
topEdge(te): int
    properties: create, query, edit
    Top edge position of the window.

---
topLeftCorner(tlc): [int, int]
    properties: create, query, edit
    Top and left edge position of the window.

---
width(w): int
    properties: create, query, edit
    Width of the window.

---
widthHeight(wh): [int, int]
    properties: create, query, edit
    Width and height of the window.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/windowPref.html 
    """


def wire(flagafter: boolean, flagafterReference: boolean, flagbefore: boolean, flagcomponents: boolean, flagcrossingEffect: float, flagdeformerTools: boolean, flagdropoffDistance: tuple[uint, linear], flagenvelope: float, flagexclusive: string, flagfrontOfChain: boolean, flaggeometry: string, flaggeometryIndices: boolean, flaggroupWithBase: boolean, flagholder: tuple[uint, string], flagignoreSelected: boolean, flagincludeHiddenSelections: boolean, flaglocalInfluence: float, flagname: string, flagparallel: boolean, flagprune: boolean, flagremove: boolean, flagselectedComponents: boolean, flagsplit: boolean, flaguseComponentTags: boolean, flagwire: string, flagwireCount: uint) -> list[string]:
    """Synopsis:
---
---
 wire(
[objects]
    , [after=boolean], [afterReference=boolean], [before=boolean], [components=boolean], [crossingEffect=float], [deformerTools=boolean], [dropoffDistance=[uint, linear]], [envelope=float], [exclusive=string], [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean], [groupWithBase=boolean], [holder=[uint, string]], [ignoreSelected=boolean], [includeHiddenSelections=boolean], [localInfluence=float], [name=string], [parallel=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean], [split=boolean], [useComponentTags=boolean], [wire=string], [wireCount=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

wire is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

select a surface and a curve that you want to be a wire, then enter
cmds.wire()

create a wire deformer on surface1 using curve1 and curve2
cmds.wire( 'surface1', 'curve1', 'curve2' )

modify the dropoff distance and envelope on wire1
cmds.wire( 'wire1', edit=True, en=0.8, dds=[(0, 6),(1, 3.2)] )

---
Return:
---


    list[string]: The wire node name and the wire curve name

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
crossingEffect(ce): float
    properties: create, query, edit
    Set the amount of convolution effect. Varies from fully
convolved at 0 to a simple additive effect at 1 (which
is what you get with the filter off).
Default is 0.
 This filter should make its way into all
blend nodes that deal with combining effects from
multiple sources.

---
deformerTools(dt): boolean
    properties: query
    Returns the name of the deformer tool objects (if any)
as string string ...

---
dropoffDistance(dds): [uint, linear]
    properties: create, query, edit, multiuse
    Set the dropoff distance (second parameter) for the wire at index (first parameter).

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
groupWithBase(gw): boolean
    properties: create
    Groups the wire with the base wire so that they can easily be moved
together to create a ripple effect.
Default is false.

---
holder(ho): [uint, string]
    properties: create, query, edit, multiuse
    Set the specified curve or surface (second parameter  as a holder for the wire at index (first parameter).

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
localInfluence(li): float
    properties: create, query, edit
    Set the local control a wire has with respect to other
wires irrespective of whether it is deforming the surface.
Varies from no local effect at 0 to full local control
at 1.
Default is 0.

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
useComponentTags(uct): boolean
    properties: create
    When this flag is specified a setup using componentTags will be created.
This means no groupId, groupParts, tweak or objectSet nodes will be
created and connected to the new deformer.

---
wire(w): string
    properties: create, query, edit, multiuse
    Specify or query the wire curve name.

---
wireCount(wc): uint
    properties: create, query, edit
    Set the number of wires.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/wire.html 
    """


def wireContext(flagcrossingEffect: linear, flagdeformationOrder: string, flagdropoffDistance: linear, flagenvelope: linear, flagexclusive: boolean, flagexclusivePartition: string, flagexists: boolean, flaggroupWithBase: boolean, flaghistory: boolean, flagholder: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flaglocalInfluence: linear, flagname: string) -> string:
    """Synopsis:
---
---
 wireContext(
string
    , [crossingEffect=linear], [deformationOrder=string], [dropoffDistance=linear], [envelope=linear], [exclusive=boolean], [exclusivePartition=string], [exists=boolean], [groupWithBase=boolean], [history=boolean], [holder=boolean], [image1=string], [image2=string], [image3=string], [localInfluence=linear], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

wireContext is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.wireContext( 'wireCtx' )

---
Return:
---


    string: The name of the context created

Flags:
---


---
crossingEffect(ce): linear
    properties: create, query, edit
    Set the amount of convolution filter effect. Varies from fully
convolved at 0 to a simple additive effect at 1.
Default is 0.

---
deformationOrder(do): string
    properties: create, query, edit
    Set the appropriate flag that determines the position in
in the deformation hierarchy.

---
dropoffDistance(dds): linear
    properties: create, query, edit
    Set the dropoff Distance for the wires.

---
envelope(en): linear
    properties: create, query, edit
    Set the envelope value for the deformer. Default is 1.0

---
exclusive(exc): boolean
    properties: create, query, edit
    Set exclusive mode on or off.

---
exclusivePartition(ep): string
    properties: create, query, edit
    Set the name of an exclusive partition.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
groupWithBase(gw): boolean
    properties: create, query, edit
    Groups the wire with the base wire so that they can easily be moved
together to create a ripple effect.
Default is false.

---
history(ch): boolean
    properties: create
    If this is a tool command, turn the construction history on
for the tool in question.

---
holder(ho): boolean
    properties: create, edit
    Controls whether the user can specify holders for the wires
from the wire context. A holder is a curve that you can use to limit
the wire's deformation region. Default is false.

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
localInfluence(li): linear
    properties: create, query, edit
    Set the amount of local influence a wire has with respect
to other wires.
Default is 0.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/wireContext.html 
    """


def workspace(flagactive: boolean, flagbaseWorkspace: string, flagcreate: string, flagdirectory: string, flagexpandName: string, flagfileRule: tuple[string, string], flagfileRuleEntry: string, flagfileRuleList: boolean, flagfilter: boolean, flagfullName: boolean, flaglist: boolean, flaglistFullWorkspaces: boolean, flaglistWorkspaces: boolean, flagnewWorkspace: boolean, flagobjectType: tuple[string, string], flagobjectTypeEntry: string, flagobjectTypeList: boolean, flagopenWorkspace: boolean, flagprojectPath: string, flagremoveFileRuleEntry: string, flagremoveVariableEntry: string, flagrenderType: tuple[string, string], flagrenderTypeEntry: string, flagrenderTypeList: boolean, flagrootDirectory: boolean, flagsaveWorkspace: boolean, flagshortName: boolean, flagupdate: boolean, flagupdateAll: boolean, flagvariable: tuple[string, string], flagvariableEntry: string, flagvariableList: boolean) -> list[string] | string:
    """Synopsis:
---
---
 workspace(
[string]
    , [active=boolean], [baseWorkspace=string], [create=string], [directory=string], [expandName=string], [fileRule=[string, string]], [fileRuleEntry=string], [fileRuleList=boolean], [filter=boolean], [fullName=boolean], [list=boolean], [listFullWorkspaces=boolean], [listWorkspaces=boolean], [newWorkspace=boolean], [objectType=[string, string]], [objectTypeEntry=string], [objectTypeList=boolean], [openWorkspace=boolean], [projectPath=string], [removeFileRuleEntry=string], [removeVariableEntry=string], [renderType=[string, string]], [renderTypeEntry=string], [renderTypeList=boolean], [rootDirectory=boolean], [saveWorkspace=boolean], [shortName=boolean], [update=boolean], [updateAll=boolean], [variable=[string, string]], [variableEntry=string], [variableList=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

workspace is undoable, queryable, and NOT editable.
The string argument represents the workspace. If no workspace is
specified then the current workspace is assumed.

A workspace provides the underlying definition of a Maya Project.
Each project has an associated workspace file, named workspace.mel, which is stored in the project root directory.
The workspace file defines a set of rules that map file types to their storage, either relative to the
project root or as an absolute location.  These rules are used when resolving file paths at runtime.

The workspace command operates directly on the low-level definition of the workspace to read, change and store
the definition to the underlying file.  Use of this command is not generally required, for most purposes
it is recommended that project definition changes be done via the Project Window in the User Interface. Multiple
actions go under the assumption that given paths exist.




Example:
---
import maya.cmds as cmds

Set the current workspace to "alphabet".
cmds.workspace( 'alphabet', openWorkspace=True )

Save the current workspace settings (for "alphabet").
cmds.workspace( saveWorkspace=True )

Change current directory to project directory
cmds.workspace( directory="/h/userName/maya/projects/" )

Create a directory for a new workspace
cmds.workspace( create="newWorkspace" )

Create a new workspace named "newWorkspace".
cmds.workspace( 'newWorkspace', newWorkspace=True )

The file rules and variables of "newWorkspace" are based on "default" workspace
cmds.workspace( baseWorkspace='default' )

Return the list of existing workspaces
cmds.workspace( listWorkspaces=True )
Result: default   newWorkspace

Add a scriptJob to run on workspaceChanged events
def workspaceChangedCallback():
print 'My workspaceChangedCallback was called'

workspaceChangedID = cmds.scriptJob( event = ["workspaceChanged", workspaceChangedCallback] )

add a file rule to the current workspace
cmds.workspace(fileRule = ['newFileRuleName', 'newFileRuleValue'])
My workspaceChangedCallback was called            ---
workspaceChangedCallback was called

look up the value of the file rule entry
cmds.workspace(fileRuleEntry = 'newFileRuleName')
Result: newFileRuleValue

remove specified file rule entry
cmds.workspace(removeFileRuleEntry = 'newFileRuleName')
My workspaceChangedCallback was called            ---
workspaceChangedCallback is called

kill the scriptJob with the number
cmds.scriptJob(kill = workspaceChangedID)

The following example shows how to expand environment and workspace variables

expand a path value to be a full path relative to the project directory
relative path example
cmds.workspace( expandName = 'relativePathName')
Result: /h/userName/maya/projects/newWorkspace/relativePathName
full path example
cmds.workspace( expandName = '/h/userName/maya/projects/default/')
Result: /h/userName/maya/projects/default/

The following examples show various formats for expanding workspace and
environment variables.

add a variable to the current workspace
cmds.workspace(variable = ['newVariableName', 'newVariableValue'])
cmds.workspace( expandName = '%newVariableName%')
Result: /h/userName/maya/projects/newWorkspace/newVariableValue

add an environment variable
os.environ['newEnvVariableName'] = "newEnvVariableValue"
cmds.workspace( expandName = os.environ['newEnvVariableName'])
Result: /h/userName/maya/projects/newWorkspace/newEnvVariableValue

When a tilde is used, maya will only consider the environment variable
not the workspace variable.
cmds.workspace( expandName = '~%newVariableName%')
Result: /h/userName/maya/projects/newWorkspace/~newEnvVariableValue

The following example shows how to set multiple paths into a fileRule value
cmds.workspace(fileRule = ['newMultiPathFileRuleName', '/h/userName/maya/projects/default;newFileRuleValue'])
multipath = cmds.workspace(fileRuleEntry = 'newMultiPathFileRuleName')
Result : /h/userName/maya/projects/default;newFileRuleValue

Note that white space at the beginning or end of each path is significant.
Add a file rule that uses multiple paths with the white space at the beginning and end of each path
cmds.workspace(fileRule = ['newMultiPathFileRuleName', ' /h/userName/maya/projects/default ; newFileRuleValue '])
Querying and expanding the path value shows that the white space is still included.
multipath = cmds.workspace(fileRuleEntry = 'newMultiPathFileRuleName')
Result :  /h/userName/maya/projects/default ; newFileRuleValue

Find the current workspace area.
cmds.workspace( q=True, directory=True )
Result : /h/userName/maya/projects/

Note that the "current working directory" as defined by the
'pwd' and 'chdir' commands is unrelated to the directories
used by the workspace command
---

os.getcwd()
Result : /usr/tmp

os.chdir( '/tmp' )
os.getcwd()
Result : /tmp
cmds.workspace( q=True, directory=True )
Result : /h/userName/maya/projects/

cmds.workspace( directory='/h/userName/maya/projects/commercial' )
os.getcwd()
Result : /tmp

---
Return:
---


    string: Project short name when querying the 'shortName' flag.
    string: Project full name when querying the 'fullName' flag.
    string: Current workspace name when querying the 'openWorkspace' flag and there is a current one.
    string: Working space directory when querying the 'directory' flag.
    string: File rule on the current workspace when querying one of the 'renderTypeEntry', 'fileRuleEntry', or 'objectTypeEntry' flags.
    string: File rule on the current workspace when querying the 'variableEntry' flag.
    string: Resolved full name of the given file name, or the current root directory if no name given when querying the 'expandName' flag.
    string: Path to the current project workspace when querying the 'projectPath' flag.
    string: Current workspace's base workspace name when querying the 'baseWorkspace' flag.
    string: Current workspace's root directory when querying the 'rootDirectory' flag.
    list[string]: List of file rules when querying the 'fileRule' flag.
    list[string]: List of variables when querying the 'variableList' flag.
    list[string]: List of all workspaces when querying the 'listWorkspaces' flag.
    list[string]: List of full names of all workspaces when querying the 'listFullWorkspaces' flag.
    list[string]: List of path names for all workspace in the directory named when querying the 'list' flag or the current workspace if no directory is named.
    list[string]: List of alternating (file rule, rule location) strings corresponding to the current workspace's file rules.
    list[string]: List of alternating (variable, value) strings corresponding to the current workspace's variables.

Flags:
---


---
active(act): boolean
    properties: create, query
    This flag is a synonym for -o/openWorkspace.

---
baseWorkspace(bw): string
    properties: query
    A workspace may be based on another workspace.  This means
that all the file rules and variables in the base workspace
apply to this workspace unless they are explicitly overridden.
By default, a new workspace has the workspace "default" as
it's base workspace. Note that "duplicated" file rules
containing relative paths are not verified nor created when
creating a new workspace or when changing the base workspace.

---
create(cr): string
    properties: create
    Create a new directory.  If the directory name is not
a full path name, it will be created as a subdirectory of
the "current" directory set with the -dir flag. Note that this
flag does not create a workspace.

---
directory(dir): string
    properties: create, query
    This option will set the current workspace directory to the
path specified. When queried it will return the current workspace
directory. This directory is used as an initial directory for the
fileBrowser and is part of the search path used for locating
files. It should not be confused with the current working
directory as used by the pwd and chdir commands.
When the file browser is used, it will set this value to the last
location navigated to.

---
expandName(en): string
    properties: create, query
    Query for the full path location of a filename using the current workspace definition.
The path may be a project relative file name, a full path name or a variable name.
The return value is always a full path name.
If the path is an empty string, the return value will be the project root directory.
Variable expansion is supported, and will consider both variables defined in the workspace
as well as environment variables.
There are three formats supported for expanding variable names:
%variableName%, $variableName, ${variableName}.
Maya will first attempt to find matching variables defined in the current workspace,
then search for a matching environment variable.
The tilde character ('~') is also supported.
If a tilde is located at the beginning of a variable, Maya
will only consider and expand environment variables, and will leave the tilde in the
expanded result.
On linux and mac platforms, a tilde can be used to expand a user's home directory,
using the form ~username, ~, or ~/.  When specified as ~username, it will be replaced
with the corresponding user's home directory.  When specified as ~ or ~/, it will
be replaced with the value of the HOME environment variable.

---
fileRule(fr): [string, string]
    properties: create, query
    Set the default location for a file. The first parameter is
the fileRule name(scenes, images, etc) and the second is the location. When
queried, it returns a list of strings.  The elements of the
returned list alternate between fileRule names and the corresponding
location.  There is typically one file rule for each available
translator. Environment variables are supported.
You can set multiple path for the file rule by separating them with
semicolons (;) on Windows and colons(:) on MacOSX and Linux.
Note that whitespace at the beginning and end of each item in the
separated sequence is significant and will be included as part of the
path name (which is not usually desired unless the pathname does
actually start or end with spaces).
A valid filerule name cannot contain multiple byte characters. Note that
creating a filerule does not create any directories. It is the user's
responsibility to ensure that all paths are valid.

---
fileRuleEntry(fre): string
    properties: create, query
    Return the location for the given fileRule.

---
fileRuleList(frl): boolean
    properties: create, query
    Returns a list of the currently defined file rules.

---
filter(f): boolean
    properties: 
    This flag is obsolete.

---
fullName(fn): boolean
    properties: create, query
    Return the full name of the workspace.

---
list(l): boolean
    properties: create, query
    This option will list the current workspace directory. If a
path is specified for the "workspaceFile" then the contents of that
directory will be listed.  Otherwise, the contents of the directory
set with the -dir flag will be listed.

---
listFullWorkspaces(lfw): boolean
    properties: create, query
    Returns a list of the full path names of all the currently
defined workspaces.

---
listWorkspaces(lw): boolean
    properties: create, query
    Returns a list of all the currently defined workspace
names.

---
newWorkspace(n): boolean
    properties: create
    This specifies that a new workspace is being created with a given
path (full path or relative to "current" directory). If a
workspace with this path already exists, the command will fail.
Note that the application is creating a virtual workspace without creating
any new directories. If given a relative path, it will map the
new workspace to the "current" directory set with the -dir flag
concatenated with the given path. If the path does not exist, it
will default the workspace root directory -rd to the system's root
path (e.g. C:\ or '/'). It is the user's responsibility to ensure
that all paths exist.

---
objectType(ot): [string, string]
    properties: create, query
    This flag is obsolete. All default locations will be added to the
fileRules going forward.

---
objectTypeEntry(ote): string
    properties: create, query
    This flag is obsolete. This will now return the same as fileRuleEntry.

---
objectTypeList(otl): boolean
    properties: create, query
    This flag is obsolete. This will now return the same results as
fileRuleList going forward.

---
openWorkspace(o): boolean
    properties: create, query
    Open the workspace.  The workspace becomes the current
workspace.

---
projectPath(pp): string
    properties: create, query
    Convert filePath passed as argument to a filename that is relative to the
project root directory (if possible) and return it.  If the
filePath is not under the project root directory, a full path
name will be returned.

---
removeFileRuleEntry(rfr): string
    properties: create
    Remove the given file rule from the specified workspace. If the
workspace name is not specified, the given file rule will be removed from
the current workspace.

---
removeVariableEntry(rve): string
    properties: create
    Remove the given variable from the specified workspace. If the
workspace name is not specified, the given variable will be removed from
the current workspace.

---
renderType(rt): [string, string]
    properties: create, query
    This flag is obsolete. All default render types will be added to
fileRules going forward.

---
renderTypeEntry(rte): string
    properties: create, query
    This flag is obsolete, use fileRuleEntry going forward

---
renderTypeList(rtl): boolean
    properties: create, query
    This flag is obsolete, use fileRuleList going forward.

---
rootDirectory(rd): boolean
    properties: query
    Returns the root directory of the workspace.

---
saveWorkspace(s): boolean
    properties: create
    Save the workspace.  Workspaces are normally saved when
Maya exits but this flag will make sure that the data is
flushed to disk.

---
shortName(sn): boolean
    properties: create, query
    Query the short name of the workspace.

---
update(u): boolean
    properties: create
    This flag reads all the workspace definitions from the project
directory.  It is used by Maya at startup time to find the available
workspaces.

---
updateAll(ua): boolean
    properties: create
    This flag is a synonym for -u/update.

---
variable(v): [string, string]
    properties: create, query
    Set or query the value of a project variable. Project variables
are used when expanding names. See the -en/expandName flag below.

---
variableEntry(ve): string
    properties: create, query
    Given a variable name, will return its value.

---
variableList(vl): boolean
    properties: create, query
    Return a list of all variables in the workspace.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/workspace.html 
    """


def workspaceControl(flagactLikeMayaUIElement: boolean, flagchecksPlugins: boolean, flagclose: boolean, flagcloseCommand: script, flagcollapse: boolean, flagdefineTemplate: string, flagdockToControl: tuple[string, string], flagdockToMainWindow: tuple[string, boolean], flagdockToPanel: tuple[string, string, boolean], flagduplicatable: boolean, flagexists: boolean, flagfloating: boolean, flagheight: boolean, flagheightProperty: string, flaghorizontal: boolean, flaginitCallback: string, flaginitialHeight: int, flaginitialWidth: int, flaglabel: string, flaglayoutDirectionCallback: string, flagloadImmediately: boolean, flagminimumHeight: int, flagminimumWidth: int, flagr: boolean, flagrequiredControl: string, flagrequiredPlugin: string, flagresizeHeight: int, flagresizeWidth: int, flagrestore: boolean, flagretain: boolean, flagstateString: string, flagtabPosition: tuple[string, boolean], flagtabToControl: tuple[string, int], flaguiScript: script, flaguseTemplate: string, flagvisible: boolean, flagvisibleChangeCommand: script, flagwidth: boolean, flagwidthProperty: string) -> string:
    """Synopsis:
---
---
 workspaceControl(
[name]
    , [actLikeMayaUIElement=boolean], [checksPlugins=boolean], [close=boolean], [closeCommand=script], [collapse=boolean], [defineTemplate=string], [dockToControl=[string, string]], [dockToMainWindow=[string, boolean]], [dockToPanel=[string, string, boolean]], [duplicatable=boolean], [exists=boolean], [floating=boolean], [height=boolean], [heightProperty=string], [horizontal=boolean], [initCallback=string], [initialHeight=int], [initialWidth=int], [label=string], [layoutDirectionCallback=string], [loadImmediately=boolean], [minimumHeight=int], [minimumWidth=int], [r=boolean], [requiredControl=string], [requiredPlugin=string], [resizeHeight=int], [resizeWidth=int], [restore=boolean], [retain=boolean], [stateString=string], [tabPosition=[string, boolean]], [tabToControl=[string, int]], [uiScript=script], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=boolean], [widthProperty=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

workspaceControl is undoable, queryable, and editable.




Example:
---
import maya.cmds as cmds

def createCustomWorkspaceControlUI(*args):
  cmds.columnLayout()
  cmds.button()
  cmds.button()
  cmds.button()

cmds.workspaceControl("myCustomWorkspaceControl", retain=False, floating=True, uiScript="createCustomWorkspaceControlUI()");

---
Return:
---


    string: Full path name to the control.

Flags:
---


---
actLikeMayaUIElement(alm): boolean
    properties: create, query, edit
    Controls whether or not this workspace control acts like Maya UI Elements such as the Shelf
and the Tool Box.

For example, this hides the tab bar and shows a toolbar grip on the end of the control to
allow undocking.

---
checksPlugins(cp): boolean
    properties: create, edit
    Sets whether the UI (as defined by the uiScript) checks the loaded state of one or more plug-ins in its code.
The UI will not be loaded until the auto-loading of plug-ins is complete. Default value is false.

---
close(cl): boolean
    properties: edit
    Closes the workspace control.

---
closeCommand(cc): script
    properties: create, edit
    Command that gets executed when the workspace control is closed.

---
collapse(clp): boolean
    properties: create, query, edit
    Collapse or expand the tab widget parent of the workspace control.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
dockToControl(dtc): [string, string]
    properties: create, edit
    Dock this workspace control next to the given control. The first argument is the control name,
the second is dock position relative to the control (valid values are: "left", "right", "top", "bottom").

---
dockToMainWindow(dtm): [string, boolean]
    properties: create, edit
    Dock this workspace control into the main window. The first argument is the dock position along the sides of
the main window (valid values are: "left", "right", "top", "bottom"), the second specifies whether the
control should be tabbed into the first control found at the dock position.

---
dockToPanel(dtp): [string, string, boolean]
    properties: create, edit
    Dock this workspace control into the workspace docking panel that the given workspace control is in. The first argument
is the control name, the second is dock position along the sides of the panel (valid values are: "left", "right", "top",
"bottom"), the third specifies whether the control should be tabbed into the first control found at the dock position.

---
duplicatable(dup): boolean
    properties: create, query, edit
    Controls whether or not this workspace control can be duplicated.

The default duplicate state is controlled by whether or not the panel is unique. Unique panels cannot be
duplicated or copied. Workspace controls without a panel also cannot be duplicated, unless specifically
set as such using this flag.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
floating(fl): boolean
    properties: create, query, edit
    Whether the workspace control is floating.

---
height(h): boolean
    properties: query
    Query only flag returning the current height of the control.

---
heightProperty(hp): string
    properties: create, query, edit
    Set height property of the workspace control.
Valid values are:

fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing
preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing
free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing

Default: free 
In query mode returns the current height property of the workspace control.

---
horizontal(hr): boolean
    properties: create, query, edit
    Orientation of the control. This flag is true by default, which corresponds to a horizontally oriented widget.

Note: currently only "Toolbox" and "Shelf" support a vertical orientation.

---
initCallback(ic): string
    properties: create, query, edit
    Adds a mel command to be executed when the control is added to the layout.
The command should be a mel proc and it will be called with the workspaceControl name as parameter.
The mel command should take the form:

global proc callbackName(string $workspaceControlName)

If "save" is appended to the command name, it will be called during the layout save.

global proc callbackNameSave(string $workspaceControlName)

---
initialHeight(ih): int
    properties: create, edit
    The initial height of the workspace control when first shown.

---
initialWidth(iw): int
    properties: create, edit
    The initial width of the workspace control when first shown.

---
label(l): string
    properties: create, query, edit
    The label text. The default label is the name of the workspace control.

---
layoutDirectionCallback(ldc): string
    properties: create, query, edit
    Set a mel procedure to be called when the control changes orientation. The procedure is
called with argument 1 for horizontal and 0 for vertical.

---
loadImmediately(li): boolean
    properties: create, edit
    Sets whether the UI (as defined by the uiScript) will be built immediately on workspace control
creation (true) or delayed until the control is actually shown (false). Default value is false.

---
minimumHeight(mh): int
    properties: create, query, edit
    Sets the minimum height of control to the given value.

If given value is 0 (False), minimum height is set to 0.
If given value is 1 (True), minimum height is set to initial height.
If given value is greater than 1, minimum height is set to the given value.

In query mode returns current minimum height of the control.

---
minimumWidth(mw): int
    properties: create, query, edit
    Sets the minimum width of control to the given value.
This flag parameter was changed from bool to int in 2018 and old settings are still respected according to the following.

If given value is 0 (False), minimum width is set to 0.
If given value is 1 (True), minimum width is set to initial width.
If given value is greater than 1, minimum width is set to the given value.

In query mode returns current minimum width of the control.

---
r(r): boolean
    properties: query, edit
    Raises a workspace control to the top and makes it active.
In Query mode, this flag will return whether the workspace control is active or not.
Note that this flag won't raise a control if is minimized or collapsed. Use the flag -rs/restore instead.

---
requiredControl(rc): string
    properties: create, edit, multiuse
    The name of a workspace control that needs to be open in order for this workspace control to properly function.
This workspace control will not be created if the required control is not open, and will be closed when the
required control is closed.

---
requiredPlugin(rp): string
    properties: create, edit, multiuse
    The name of a plug-in that needs to be loaded in order to build the workspace control UI.

---
resizeHeight(rsh): int
    properties: edit
    Resizes a floating workspace control's height to the given value.

---
resizeWidth(rsw): int
    properties: edit
    Resizes a floating workspace control's width to the given value.

---
restore(rs): boolean
    properties: create, edit
    Restores the control according to the following rules:

If collapsed then the control will be expanded
If hidden then the control will be shown
If minimized then the control will be restored
If the control is an inactive tab into a tab group then it will become the active tab

---
retain(rt): boolean
    properties: create
    Sets whether the workspace control is retained (i.e. only hidden) or deleted when closed. Default value is true.

---
stateString(ss): string
    properties: create, query, edit
    String containing the state of the control.
Can be used with the initCallback flag.

---
tabPosition(tp): [string, boolean]
    properties: create, query, edit
    Changes the tab position. The possible values are: "north", "east" and "west".
The boolean value, if set to true, changes the tab positions of all the controls in the parent widget.
If it is not set, only the current control will get its position changed.
A control can have a different orientation than the tab widget.
If the control tab position is different from the tab widget's one, the tab position will be changed when the control becomes the only control in the tab widget.
On query, only the control's tab position will be returned, not the tab widget's position. They may differ.

---
tabToControl(ttc): [string, int]
    properties: create, edit
    Tab this workspace control into the given control. The first argument is the control name,
the second is the index position within the containing tab widget (invalid values mean append).

---
uiScript(ui): script
    properties: create, edit
    The specified script will be invoked to build the UI of the workspaceControl.  This is a required flag.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
visible(vis): boolean
    properties: create, query, edit
    The visible state of the workspace control. A control is created visible by default.
If the control is created as not visible, the control will be created in a closed state.
To make it appear, edit the control to set the flags floating or the flag visible to true.
Use -r/raise flag to get the active status of a control as this flag will return true when the control
is minimized or collapsed.

---
visibleChangeCommand(vcc): script
    properties: create, edit
    Command that gets executed when visible state of the workspace control changes.

---
width(w): boolean
    properties: query
    Query only flag returning the current width of the control.

---
widthProperty(wp): string
    properties: create, query, edit
    Set width property of the workspace control.
Valid values are:

fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing
preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing
free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing

Default: free 
In query mode returns the current width property of the workspace control.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/workspaceControl.html 
    """


def workspaceControlState(flagdefaultTopLeftCorner: tuple[int, int], flagdefaultWidthHeight: tuple[int, int], flagexists: boolean, flagheight: int, flagleftEdge: int, flagmaximized: boolean, flagremove: boolean, flagtopEdge: int, flagtopLeftCorner: tuple[int, int], flagwidth: int, flagwidthHeight: tuple[int, int]) -> None:
    """Synopsis:
---
---
 workspaceControlState(
string
    , [defaultTopLeftCorner=[int, int]], [defaultWidthHeight=[int, int]], [exists=boolean], [height=int], [leftEdge=int], [maximized=boolean], [remove=boolean], [topEdge=int], [topLeftCorner=[int, int]], [width=int], [widthHeight=[int, int]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

workspaceControlState is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

   Check if the window exists.
---

if cmds.window('ExampleWindow', exists=True):
        cmds.deleteUI('ExampleWindow', window=True)

   Create a window.
---

cmds.window( 'ExampleWindow' )
cmds.columnLayout()
cmds.text( label='Size and position the window before closing it.' )
cmds.button( label='Close', command='cmds.deleteUI("ExampleWindow", window=True)' )
cmds.showWindow( 'ExampleWindow' )

   When the window is closed a window preference object is
   created for the window. It has the same name as the window
   object.
---

cmds.workspaceControlState( 'ExampleWindow', exists=True )

   Query the window preference size and position.
---

cmds.workspaceControlState( 'ExampleWindow', query=True, topLeftCorner=True )
cmds.workspaceControlState( 'ExampleWindow', query=True, widthHeight=True )

   Create a window with the same name. When it is shown
   it will be sized and positioned according to the
   window preference.
---

if cmds.window('ExampleWindow', exists=True):
        cmds.deleteUI('ExampleWindow', window=True)

cmds.window( 'ExampleWindow' )
cmds.columnLayout()
cmds.text( label='Size and position the window before closing it.' )
cmds.button( label='Close', command='cmds.deleteUI("ExampleWindow", window=True)' )
cmds.showWindow( 'ExampleWindow' )

   Delete the window preference and the window will have a
   default size and position.
---

cmds.workspaceControlState( 'ExampleWindow', remove=True )

   Create the window one last time.
---

if cmds.window('ExampleWindow', exists=True):
        cmds.deleteUI('ExampleWindow', window=True)

cmds.window( 'ExampleWindow' )
cmds.columnLayout()
cmds.text( label='Size and position the window before closing it.' )
cmds.button( label='Close', command='cmds.deleteUI("ExampleWindow", window=True)' )
cmds.showWindow( 'ExampleWindow' )

---


Flags:
---


---
defaultTopLeftCorner(dc): [int, int]
    properties: create, query, edit
    Top and left edge position that the window will have when "Remember size and position" is off and when the panel is first opened.
The values will be DPI scaled on edit and the value in query is returned unscaled.
This value will only be used if the default width and height are also valid.

---
defaultWidthHeight(dwh): [int, int]
    properties: create, query, edit
    Width and height that the window will have when "Remember size and position" is off and when the panel is first opened.
The values will be DPI scaled on edit and the value in query is returned unscaled.
The position used in that case is defaultTopLeftCorner.

---
exists(ex): boolean
    properties: create
    Returns true|false depending upon whether the specified object
exists. Other flags are ignored.

---
height(h): int
    properties: create, query, edit
    Height of the window.

---
leftEdge(le): int
    properties: create, query, edit
    Left edge position of the window.

---
maximized(max): boolean
    properties: create, query, edit
    Maximize the window.

---
remove(r): boolean
    properties: create
    Remove a window preference.

---
topEdge(te): int
    properties: create, query, edit
    Top edge position of the window.

---
topLeftCorner(tlc): [int, int]
    properties: create, query, edit
    Top and left edge position of the window.

---
width(w): int
    properties: create, query, edit
    Width of the window.

---
widthHeight(wh): [int, int]
    properties: create, query, edit
    Width and height of the window.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/workspaceControlState.html 
    """


def workspaceLayoutManager(flagcollapseMainWindowControls: tuple[string, boolean], flagcurrent: boolean, flagdelete: string, flagi: string, flaglistLayouts: boolean, flaglistModuleLayouts: boolean, flaglistUserLayouts: boolean, flagmodified: string, flagparentWorkspaceControl: string, flagreset: boolean, flagrestoreMainWindowControls: boolean, flagsave: boolean, flagsaveAs: string, flagsetCurrent: string, flagsetCurrentCallback: string, flagsetModifiedCallback: string, flagtype: string) -> list[string]:
    """Synopsis:
---
---
 workspaceLayoutManager(
[name]
    , [collapseMainWindowControls=[string, boolean]], [current=boolean], [delete=string], [i=string], [listLayouts=boolean], [listModuleLayouts=boolean], [listUserLayouts=boolean], [modified=string], [parentWorkspaceControl=string], [reset=boolean], [restoreMainWindowControls=boolean], [save=boolean], [saveAs=string], [setCurrent=string], [setCurrentCallback=string], [setModifiedCallback=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

workspaceLayoutManager is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.workspaceLayoutManager( listLayouts=True )

---
Return:
---


    list[string]: depending on arguments

Flags:
---


---
collapseMainWindowControls(cmw): [string, boolean]
    properties: create
    Saves main window layout and collapses all other controls in main window except the given one (first parameter)
if it does not have any size constraint. Second parameter specifies if main window UI elements should be hidden or not.

---
current(cu): boolean
    properties: create, query
    Get the name of the current layout.

---
delete(d): string
    properties: create
    Delete the given workspace. The string is the name of the layout, not the file name.

---
i(i): string
    properties: create
    Import the given workspace file to the workspaces directory. The string is an absolute path.

---
listLayouts(ll): boolean
    properties: create
    List the names of all registered layouts.

---
listModuleLayouts(lml): boolean
    properties: create
    List the names of module layouts.

---
listUserLayouts(lul): boolean
    properties: create
    List the names of user layouts.

---
modified(m): string
    properties: create
    Check whether or not the specified layout has been modified.

---
parentWorkspaceControl(pwc): string
    properties: create
    Returns the parent workspace control of the given UI (panel) or an empty string if it does not exist.

---
reset(rs): boolean
    properties: create
    Reset the current workspace to its original layout. Factory layouts will be reverted to default while user layouts will be reloaded from disk.

---
restoreMainWindowControls(rmw): boolean
    properties: create
    Restores the main window layout to the one saved with the -cmw/-collapseMainWindowControls flag.
The loaded workspace file will be deleted once it is restored.

---
save(s): boolean
    properties: create
    Save the current layout.

---
saveAs(sa): string
    properties: create
    Save the current layout under the specified name.

---
setCurrent(sc): string
    properties: create
    Load the given workspace.  The string is the name of the layout, not the file name.

---
setCurrentCallback(scc): string
    properties: create
    MEL only.  The string is interpreted as a MEL callback, which is called
each time a layout is set as current (with -setCurrent flag).
The callback is of the form:

global proc MySetCurrentCallback(string $layoutName)

---
setModifiedCallback(smc): string
    properties: create
    MEL only.  The string is interpreted as a MEL callback, which is called
each time a layout is modified or restored, that is, each time the -modified flag value changes.
The callback is of the form:

global proc MySetModifiedCallback()

---
type(t): string
    properties: create
    Get the type of the specified layout: FACTORY, FACTORY_OVERRIDE, MODULE, MODULE_OVERRIDE or USER.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/workspaceLayoutManager.html 
    """


def workspacePanel(flagdefineTemplate: string, flagexists: boolean, flagmainWindow: boolean, flaguseTemplate: string) -> string:
    """Synopsis:
---
---
 workspacePanel([defineTemplate=string], [exists=boolean], [mainWindow=boolean], [useTemplate=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

workspacePanel is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.workspacePanel(mainWindow=True)

---
Return:
---


    string: Full path name to the workspace panel.

Flags:
---


---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
exists(ex): boolean
    properties: create
    Returns whether the
specified object exists or not. Other flags are ignored.

---
mainWindow(mw): boolean
    properties: create, query, edit
    Main window for the application.  The main window
has an 'Exit' item in the Window Manager menu.  By default, the
first created window becomes the main window.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/workspacePanel.html 
    """


def wrinkle(flagaxis: tuple[linear, linear, linear], flagbranchCount: uint, flagbranchDepth: uint, flagcenter: tuple[linear, linear, linear], flagcrease: string, flagdropoffDistance: linear, flagenvelope: linear, flagrandomness: linear, flagstyle: string, flagthickness: linear, flaguvSpace: tuple[linear, linear, linear, linear, linear], flagwrinkleCount: uint, flagwrinkleIntensity: linear) -> list[string]:
    """Synopsis:
---
---
 wrinkle(
objects
    , [axis=[linear, linear, linear]], [branchCount=uint], [branchDepth=uint], [center=[linear, linear, linear]], [crease=string], [dropoffDistance=linear], [envelope=linear], [randomness=linear], [style=string], [thickness=linear], [uvSpace=[linear, linear, linear, linear, linear]], [wrinkleCount=uint], [wrinkleIntensity=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

wrinkle is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Apply radial wrinkles to a sphere:

mySph = cmds.sphere()
cmds.wrinkle( mySph, st='radial', wc=3, brc=2, bd=0, th=1, rnd=0.2, wi=0.5, uv=(2.0, 4.0, 0.0, 2.0, 4.0) )

Apply a 5-line tangential wrinkle to a plane:

myPlane = cmds.nurbsPlane( w=50, u=20, v=20 )
cmds.wrinkle( myPlane, st='lines', wc=5, th=1.0, rnd=0.2, wi=0.5, uv=(1.0, 1.0, 0.0, 0.5, 0.5) )

---
Return:
---


    list[string]: List of clusters created followed by list of wire deformers created.

Flags:
---


---
axis(ax): [linear, linear, linear]
    properties: create
    Specifies the plane of the wrinkle.

---
branchCount(brc): uint
    properties: create
    Specifies the number of branches per wrinkle. Default is 2.

---
branchDepth(bd): uint
    properties: create
    Specifies the depth of the branching. Default is 0.

---
center(ct): [linear, linear, linear]
    properties: create
    Specifies the center of the wrinkle.

---
crease(cr): string
    properties: create, multiuse
    Specifies an existing curve to serve as the wrinkle.

---
dropoffDistance(dds): linear
    properties: create
    Specifies the dropoff distance around the center.

---
envelope(en): linear
    properties: create
    The envelope globally attenuates the amount of deformation. Default is 1.0.

---
randomness(rnd): linear
    properties: create
    Amount of randomness. Default is 0.2.

---
style(st): string
    properties: create
    Specifies the wrinkle style. Valid values are "radial" or "tangential"

---
thickness(th): linear
    properties: create
    Wrinkle thickness. Default is 1.0.

---
uvSpace(uv): [linear, linear, linear, linear, linear]
    properties: create
    1/2 length, 1/2 breadth, rotation angle, center u, v
definition of a patch in uv space where the wrinkle is
to be constructed.

---
wrinkleCount(wc): uint
    properties: create
    Specifies the number of wrinkle lines to be generated.
Default is 3.

---
wrinkleIntensity(wi): linear
    properties: create
    Increasing the intensity makes it more wrinkly. Default is 0.5.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/wrinkle.html 
    """


def wrinkleContext(flagbranchCount: uint, flagbranchDepth: uint, flagexists: boolean, flaghistory: boolean, flagimage1: string, flagimage2: string, flagimage3: string, flagname: string, flagrandomness: linear, flagstyle: string, flagthickness: linear, flagwrinkleCount: uint, flagwrinkleIntensity: linear) -> string:
    """Synopsis:
---
---
 wrinkleContext(
string
    , [branchCount=uint], [branchDepth=uint], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [randomness=linear], [style=string], [thickness=linear], [wrinkleCount=uint], [wrinkleIntensity=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

wrinkleContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.wrinkleContext( 'wrinkleCtx' )

---
Return:
---


    string: The name of the context created

Flags:
---


---
branchCount(brc): uint
    properties: create, query, edit
    Set the number of branches spawned from a crease for radial wrinkles.
Default is 2.

---
branchDepth(bd): uint
    properties: create, query, edit
    Set the depth of branching for radial wrinkles.
Defaults to 0.

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
randomness(rnd): linear
    properties: create, query, edit
    Set the deviation of the wrinkle creases from straight lines and
other elements of the wrinkle structure.
Defaults to 0.2.

---
style(st): string
    properties: create, query, edit
    Set the wrinkle characteristic shape."lines"|"radial"|"custom.
Default is "radial".

---
thickness(th): linear
    properties: create, query, edit
    Set the thickness of wrinkle creases by setting the dropoff
distance on the underlying wires.

---
wrinkleCount(wc): uint
    properties: create, query, edit
    Set the number of wrinkle creases.
Default is 3.

---
wrinkleIntensity(wi): linear
    properties: create, query, edit
    Set the depth intensity of the wrinkle furrows.
Defaults to 0.5.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/wrinkleContext.html 
    """


def writeTake(flagangle: string, flagdevice: string, flaglinear: string, flagnoTime: boolean, flagprecision: int, flagtake: string, flagvirtualDevice: string) -> None:
    """Synopsis:
---
---
 writeTake([angle=string], [device=string], [linear=string], [noTime=boolean], [precision=int], [take=string], [virtualDevice=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

writeTake is undoable, NOT queryable, and NOT editable.
See also: recordDevice, readTake, defineVirtualDevice




Example:
---
import maya.cmds as cmds

   Record data from the clock device and write out the virtual
   device definition and take file.
cmds.recordDevice( device='clock' )
cmds.recordDevice( device='clock', stop=True )
cmds.writeTake( device='clock', take='clock.mov', virtualDevice='virtualClock.mel' )

   Read the virtualClock and virtualClock take data.
maya.mel.eval("virtualClock")
cmds.readTake( device='virtualClock', take='clock.mov' )

---


Flags:
---


---
angle(a): string
    properties: create
    Sets the angular unit used in the take.
Valid strings are [deg|degree|rad|radian]. 
C: The default is the current user angular unit.

---
device(d): string
    properties: create
    Specifies the device that contains the take. This is a required
argument. If the device does not contain a take, the action will
fail.

---
linear(l): string
    properties: create
    Sets the linear unit used in the take. Valid strings are
[mm|millimeter|cm|centimeter|m|meter|km|kilometer|in|inch|ft|foot|yd|yard|mi|mile] 
C: The default is the current user linear unit.

---
noTime(nt): boolean
    properties: create
    The take (.mov) file will not contain time stamps. 
C: The default is to put time stamps in the take file.

---
precision(pre): int
    properties: create
    Sets the number of digits to the right of the decimal place in
the take file.
C: The default is 6.

---
take(t): string
    properties: create
    Write out the take to a file with the specified name.

---
virtualDevice(vd): string
    properties: create
    Writes out the virtual device definition to a mel script with the
specified file name.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/writeTake.html 
    """
