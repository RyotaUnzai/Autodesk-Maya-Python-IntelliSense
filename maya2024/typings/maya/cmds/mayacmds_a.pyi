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


def aaf2fcp(deleteFile: boolean, dstPath: string, getFileName: int, progress: int, srcFile: string, terminate: int, waitCompletion: int) -> string:
    """Synopsis:
---
---
 aaf2fcp([deleteFile=boolean], [dstPath=string], [getFileName=int], [progress=int], [srcFile=string], [terminate=int], [waitCompletion=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

aaf2fcp is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


handle = cmds.aaf2fcp(srcFile='c:/tmp/test.aaf', dstPath='c:/tmp')
destinationFile = cmds.aff2fcp(getFileName=handle)
cmds.aaf2fcp(waitCompletion=handle)
cmds.aaf2fcp(terminate=handle,deleteFile=False)

---
Return:
---


    string: Command result

Flags:
---


---
deleteFile(df): boolean
    properties: create
    Delete temporary file. Can only be used with the terminate option

---
dstPath(dst): string
    properties: create
    Specifiy a destination path

---
getFileName(gfn): int
    properties: create
    Query output file name

---
progress(pr): int
    properties: create
    Request progress report

---
srcFile(src): string
    properties: create
    Specifiy a source file

---
terminate(t): int
    properties: create
    Complete the task

---
waitCompletion(wc): int
    properties: create
    Wait for the conversion process to complete

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/aaf2fcp.html 
    """


def about(apiVersion: boolean, application: boolean, arm64: boolean, batch: boolean, buildDirectory: boolean, buildVariant: boolean, codeset: boolean, compositingManager: boolean, connected: boolean, creativeVersion: boolean, ctime: boolean, currentDate: boolean, currentTime: boolean, customVersion: boolean, customVersionClient: boolean, customVersionMajor: boolean, customVersionMinor: boolean, customVersionString: boolean, cutIdentifier: boolean, date: boolean, environmentFile: boolean, evalVersion: boolean, file: boolean, fontInfo: boolean, helpDataDirectory: boolean, installedVersion: boolean, ioVersion: boolean, irix: boolean, is64: boolean, languageResources: boolean, linux: boolean, linux64: boolean, liveUpdate: boolean, localizedResourceLocation: boolean, ltVersion: boolean, macOS: boolean, macOSASi: boolean, macOSppc: boolean, macOSx86: boolean, majorVersion: boolean, minorVersion: boolean, ntOS: boolean, operatingSystem: boolean, operatingSystemVersion: boolean, patchVersion: boolean, preferences: boolean, product: boolean, qtVersion: boolean, tablet: boolean, tabletMode: boolean, uiLanguage: boolean, uiLanguageForStartup: boolean, uiLanguageIsLocalized: boolean, uiLocaleLanguage: boolean, version: boolean, win64: boolean, windowManager: boolean, windows: boolean) -> string:
    """Synopsis:
---
---
 about([apiVersion=boolean], [application=boolean], [arm64=boolean], [batch=boolean], [buildDirectory=boolean], [buildVariant=boolean], [codeset=boolean], [compositingManager=boolean], [connected=boolean], [creativeVersion=boolean], [ctime=boolean], [currentDate=boolean], [currentTime=boolean], [customVersion=boolean], [customVersionClient=boolean], [customVersionMajor=boolean], [customVersionMinor=boolean], [customVersionString=boolean], [cutIdentifier=boolean], [date=boolean], [environmentFile=boolean], [evalVersion=boolean], [file=boolean], [fontInfo=boolean], [helpDataDirectory=boolean], [installedVersion=boolean], [ioVersion=boolean], [irix=boolean], [is64=boolean], [languageResources=boolean], [linux=boolean], [linux64=boolean], [liveUpdate=boolean], [localizedResourceLocation=boolean], [ltVersion=boolean], [macOS=boolean], [macOSASi=boolean], [macOSppc=boolean], [macOSx86=boolean], [majorVersion=boolean], [minorVersion=boolean], [ntOS=boolean], [operatingSystem=boolean], [operatingSystemVersion=boolean], [patchVersion=boolean], [preferences=boolean], [product=boolean], [qtVersion=boolean], [tablet=boolean], [tabletMode=boolean], [uiLanguage=boolean], [uiLanguageForStartup=boolean], [uiLanguageIsLocalized=boolean], [uiLocaleLanguage=boolean], [version=boolean], [win64=boolean], [windowManager=boolean], [windows=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

about is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.about( )

version = cmds.about(v=True)

---
Return:
---


    string: The application's version information.

Flags:
---


---
apiVersion(api): boolean
    properties: create
    Returns the api version.

---
application(a): boolean
    properties: create
    Returns the application name string.

---
arm64(a64): boolean
    properties: create
    Returns true if the CPU is arm64 based.

---
batch(b): boolean
    properties: create
    Returns true if application is in batch mode.

---
buildDirectory(bd): boolean
    properties: create
    Returns the build directory string.

---
buildVariant(bv): boolean
    properties: create
    Returns the build variant string.

---
codeset(cs): boolean
    properties: create
    Returns a string identifying the codeset (codepage) of the
locale that Maya is running in.
Example return values include "UTF-8", "ISO-8859-1", "1252".
Note that the codeset values and naming conventions
are highly platform dependent.  They may differ in format
even if they have the same meaning (e.g. "utf8" vs. "UTF-8").

---
compositingManager(cm): boolean
    properties: create
    On Linux, returns true if there is a compositing manager running; on
all other platforms, it always returns true.

---
connected(cnt): boolean
    properties: create
    Return whether the user is connected or not to the Internet.

---
creativeVersion(cre): boolean
    properties: create
    Returns true if this is the Maya Creative version of the application.

---
ctime(cti): boolean
    properties: create
    Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0

---
currentDate(cd): boolean
    properties: create
    Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.

---
currentTime(ct): boolean
    properties: create
    Returns the current time in the format hh:mm:ss, e.g. 14:27:53.

---
customVersion(cv): boolean
    properties: create
    Returns true if this is a custom version of Maya.

---
customVersionClient(cvc): boolean
    properties: create
    Returns the custom client version string for Maya
or an empty string if this is not a custom version.

---
customVersionMajor(cvm): boolean
    properties: create
    Returns the custom major version of Maya
or 0 if this is not a custom version.

---
customVersionMinor(cvn): boolean
    properties: create
    Returns the custom minor version of Maya
or 0 if this is not a custom version.

---
customVersionString(cvs): boolean
    properties: create
    Returns the custom version string for Maya
or an empty string if this is not a custom version.

---
cutIdentifier(c): boolean
    properties: create
    Returns the cut string.

---
date(d): boolean
    properties: create
    Returns the build date string.

---
environmentFile(env): boolean
    properties: create
    Returns the location of the application defaults file.

---
evalVersion(ev): boolean
    properties: create
    This flag is now deprecated. Always returns false, as the eval version is no longer supported.

---
file(f): boolean
    properties: create
    Returns the file version string.

---
fontInfo(foi): boolean
    properties: create
    Returns a string of the specifications of the
fonts requested, and the specifications of the
fonts that are actually being used.

---
helpDataDirectory(hdd): boolean
    properties: create
    Returns the help data directory.

---
installedVersion(iv): boolean
    properties: create
    Returns the product version string.

---
ioVersion(io): boolean
    properties: create
    Returns true if this is the Maya IO version of the application.

---
irix(ir): boolean
    properties: create
    Returns true if the operating system is Irix.
Always false with support for Irix removed.

---
is64(x64): boolean
    properties: create
    Returns true if the application is 64 bit.

---
languageResources(lr): boolean
    properties: create
    Returns a string array of the currently installed language resources.
Each string entry consists of three elements delimited with a colon (':').
The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country code).  The second token is the language name in English.
This third token is the alpha-3 code (ISO 639-2).  For example English is
represented as "en_US:English:enu".

---
linux(li): boolean
    properties: create
    Returns true if the operating system is Linux.

---
linux64(l64): boolean
    properties: create
    Returns true if the operating system is Linux 64 bit.

---
liveUpdate(lu): boolean
    properties: create
    This flag is deprecated(2019) and may be removed in future releases of Maya.
Returns Autodesk formatted product information.

---
localizedResourceLocation(lrl): boolean
    properties: create
    Returns the path to the top level of the localized resource
directory, if we are running in an alternate language.
Returns an empty string if we are running in the default
language.

---
ltVersion(lt): boolean
    properties: create
    Deprecated.
Returns true if this is the Maya LT version of the application.

---
macOS(mac): boolean
    properties: create
    Returns true if the operating system is Macintosh.

---
macOSASi(asi): boolean
    properties: create
    Returns true if the operating system is an Apple Silicon Mac.

---
macOSppc(ppc): boolean
    properties: create
    Returns true if the operating system is a PowerPC Macintosh.

---
macOSx86(x86): boolean
    properties: create
    Returns true if the operating system is an Intel Macintosh.

---
majorVersion(mjv): boolean
    properties: create
    Returns the major version of Maya.

---
minorVersion(mnv): boolean
    properties: create
    Returns the minor version of Maya.

---
ntOS(nt): boolean
    properties: create
    Returns true if the operating system is Windows.

---
operatingSystem(os): boolean
    properties: create
    Returns the operating system type. Valid return types are
"nt", "win64", "mac", "linux" and "linux64"

---
operatingSystemVersion(osv): boolean
    properties: create
    Returns the operating system version.
on Linux this returns the equivalent of uname -srvm

---
patchVersion(pv): boolean
    properties: create
    Returns the patch version of Maya.

---
preferences(pd): boolean
    properties: create
    Returns the location of the preferences directory.

---
product(p): boolean
    properties: create
    Returns the license product name.

---
qtVersion(qt): boolean
    properties: create
    Returns Qt version string.

---
tablet(tab): boolean
    properties: create
    Windows only.  Returns true if the PC is a Tablet PC.

---
tabletMode(tm): boolean
    properties: create
    Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible
mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached).
See the tablet flag.

---
uiLanguage(uil): boolean
    properties: create
    Returns the language that Maya's running in.  Example return
values include "en_US" for English and "ja_JP" for Japanese.

---
uiLanguageForStartup(uis): boolean
    properties: create
    Returns the language that is used for Maya's next start up.
This is read from config file and is rewritten after setting
ui language in preference.

---
uiLanguageIsLocalized(uii): boolean
    properties: create
    Returns true if we are running in an alternate
language, not the default (English).

---
uiLocaleLanguage(ull): boolean
    properties: create
    Returns the language locale of the OS. English is default.

---
version(v): boolean
    properties: create
    Returns the version string.

---
win64(w64): boolean
    properties: create
    Returns true if the operating system is Windows x64 based.

---
windowManager(wm): boolean
    properties: create
    Returns the name of the Window Manager that is
assumed to be running.

---
windows(win): boolean
    properties: create
    Returns true if the operating system is Windows based.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/about.html 
    """


def addAttr(attributeType: string, binaryTag: string, cachedInternally: boolean, category: string, dataType: string, defaultValue: float, disconnectBehaviour: uint, enumName: string, exists: boolean, fromPlugin: boolean, hasMaxValue: boolean, hasMinValue: boolean, hasSoftMaxValue: boolean, hasSoftMinValue: boolean, hidden: boolean, indexMatters: boolean, internalSet: boolean, keyable: boolean, longName: string, maxValue: float, minValue: float, multi: boolean, niceName: string, numberOfChildren: uint, parent: string, proxy: string, readable: boolean, shortName: string, softMaxValue: float, softMinValue: float, storable: boolean, usedAsColor: boolean, usedAsFilename: boolean, usedAsProxy: boolean, worldSpace: boolean, writable: boolean) -> None:
    """Synopsis:
---
---
 addAttr([attributeType=string], [binaryTag=string], [cachedInternally=boolean], [category=string], [dataType=string], [defaultValue=float], [disconnectBehaviour=uint], [enumName=string], [exists=boolean], [fromPlugin=boolean], [hasMaxValue=boolean], [hasMinValue=boolean], [hasSoftMaxValue=boolean], [hasSoftMinValue=boolean], [hidden=boolean], [indexMatters=boolean], [internalSet=boolean], [keyable=boolean], [longName=string], [maxValue=float], [minValue=float], [multi=boolean], [niceName=string], [numberOfChildren=uint], [parent=string], [proxy=string], [readable=boolean], [shortName=string], [softMaxValue=float], [softMinValue=float], [storable=boolean], [usedAsColor=boolean], [usedAsFilename=boolean], [usedAsProxy=boolean], [worldSpace=boolean], [writable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

addAttr is undoable, queryable, and editable.
This command is used to add a dynamic attribute to a node or nodes.
Either the longName or the shortName or both must be specified.
If neither a dataType nor an attributeType is specified, a double
attribute will be added.  The dataType flag can be specified more than
once indicating that any of the supplied types will be accepted (logical-or).


To add a non-double attribute the following criteria
can be used to determine whether the dataType or the attributeType
flag is appropriate.  Some types, such as double3 can use either.
In these cases the -dt flag should be used when you only wish to
access the data as an atomic entity (eg. you never want to access the
three individual values that make up a double3).  In general it
is best to use the -at in these cases for maximum flexibility.
In most cases the -dt version will not display in the attribute
editor as it is an atomic type and you are not allowed to change
individual parts of it.


All attributes flagged as "(compound)" below or the compound attribute itself
are not actually added to the node until all of the children are defined
(using the "-p" flag to set their parent to the compound being created).  See
the EXAMPLES section for more details.



 Type of attribute               Flag and argument to use      
 boolean                                                 -at bool                      
 32 bit integer                                  -at long                      
 16 bit integer                                  -at short                     
 8 bit integer                                   -at byte                      
 char                                                    -at char                      
  enum                                                   -at enum (specify the enum names using the enumName flag)  
 float                                                   -at "float" (use quotes
                                                                        since float is a mel keyword)   
 double                                                  -at double            
 angle value                                     -at doubleAngle       
 linear value                                    -at doubleLinear      
 string                                                  -dt "string" (use quotes
                                                                        since string is a mel keyword)  
 array of strings                                -dt stringArray       
 compound                                                -at compound          
 message (no data)                               -at message           
 time                                                    -at time                      
 4x4 double matrix                               -dt "matrix" (use quotes
                                                                        since matrix is a mel keyword)  
 4x4 float matrix                                -at fltMatrix         
 reflectance                                     -dt reflectanceRGB
 reflectance (compound)                  -at reflectance       
 spectrum                                                -dt spectrumRGB       
 spectrum (compound)                     -at spectrum          
 2 floats                                                -dt float2            
 2 floats (compound)                     -at float2            
 3 floats                                                -dt float3            
 3 floats (compound)                     -at float3            
 2 doubles                                               -dt double2           
 2 doubles (compound)                    -at double2           
 3 doubles                                               -dt double3           
 3 doubles (compound)                    -at double3           
 2 32-bit integers                               -dt long2                     
 2 32-bit integers (compound)    -at long2                     
 3 32-bit integers                               -dt long3                     
 3 32-bit integers (compound)    -at long3                     
 2 16-bit integers                               -dt short2            
 2 16-bit integers (compound)    -at short2            
 3 16-bit integers                               -dt short3            
 3 16-bit integers (compound)    -at short3            
 array of doubles                                -dt doubleArray       
 array of floats                                 -dt floatArray        
 array of 32-bit ints                    -dt Int32Array        
 array of vectors                                -dt vectorArray       
 nurbs curve                                     -dt nurbsCurve        
 nurbs surface                                   -dt nurbsSurface      
 polygonal mesh                                  -dt mesh                      
 lattice                                                 -dt lattice           
 array of double 4D points               -dt pointArray        




Example:
---
import maya.cmds as cmds

cmds.sphere( name='earth' )
Add an attribute named ms/mass with a default value of 1 and a
minimum value of 0.001 and a maximum of 10000.
---

cmds.addAttr( shortName='ms', longName='mass', defaultValue=1.0, minValue=0.001, maxValue=10000 )

Add a multi attribute named ff/forcefield of type double3.
---

cmds.addAttr( shortName='ff', longName='forcefield', dataType='double3', multi=True )

Add a compound attribute named sampson with children home, midge,
damien, elizabeth, and sweetpea of varying types
---

cmds.addAttr( longName='sampson', numberOfChildren=5, attributeType='compound' )
cmds.addAttr( longName='home', attributeType='matrix', parent='sampson' )
cmds.addAttr( longName='midge', attributeType='message', parent='sampson' )
cmds.addAttr( longName='damien', attributeType='double', parent='sampson' )
cmds.addAttr( longName='elizabeth', attributeType='double', parent='sampson' )
cmds.addAttr( longName='sweetpea', attributeType='double', parent='sampson' )

To add an attribute that is to be interpreted as a color the
following attribute group must be used.
---

Note that the word "float" must be in quotations since it is a
MEL keyword.
---

cmds.addAttr( longName='rainbow', usedAsColor=True, attributeType='float3' )
cmds.addAttr( longName='redBow', attributeType='float', parent='rainbow' )
cmds.addAttr( longName='greenBow', attributeType='float', parent='rainbow' )
cmds.addAttr( longName='blueBow', attributeType='float', parent='rainbow' )

Other legal attribute types that can be interpreted as colors need
not specify the "-usedAsColor" flag as it will be assumed.  These
include "-attributeType spectrum", "-attributeType reflectance",
"-dataType spectrumRGB", and "-dataType reflectanceRGB".
---

cmds.addAttr( longName='implColor', dataType='spectrumRGB' )
cmds.addAttr( '.implColor', query=True, usedAsColor=True )
Result: 1 ---


Add a double3 attribute named sanders with children bess, les and wes
---

cmds.addAttr( longName='sanders', attributeType='double3' )
cmds.addAttr( longName='bess', attributeType='double', parent='sanders' )
cmds.addAttr( longName='les', attributeType='double', parent='sanders' )
cmds.addAttr( longName='wes', attributeType='double', parent='sanders' )

Create a proxy attribute
cmds.sphere( name='moon' )
cmds.select('earth');
cmds.addAttr(longName="someProxyAttr", proxy="moon.tx");

---


Flags:
---


---
attributeType(at): string
    properties: create, query
    Specifies the attribute type, see above table for more details.
Note that the attribute types "float", "matrix" and "string"
are also MEL keywords and must be enclosed in quotes.

---
binaryTag(bt): string
    properties: create, query
    This flag is obsolete and does not do anything any more

---
cachedInternally(ci): boolean
    properties: create, query
    Whether or not attribute data is cached internally in the node.
This flag defaults to true for writable attributes and false
for non-writable attributes. A warning will be issued if
users attempt to force a writable attribute to be uncached as
this will make it impossible to set keyframes.

---
category(ct): string
    properties: create, query, edit, multiuse
    An attribute category is a string associated with the attribute to identify it.
(e.g. the name of a plugin that created the attribute, version information, etc.)
Any attribute can be associated with an arbitrary number of categories however
categories can not be removed once associated.

---
dataType(dt): string
    properties: create, query, multiuse
    Specifies the data type.  See "setAttr" for
more information on data type names.

---
defaultValue(dv): float
    properties: create, query, edit
    Specifies the default value for the attribute
(can only be used for numeric attributes).

---
disconnectBehaviour(dcb): uint
    properties: create, query
    defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete

---
enumName(en): string
    properties: create, query, edit
    Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)

---
exists(ex): boolean
    properties: create, query
    Returns true if the attribute queried is a user-added, dynamic attribute; false if not.

---
fromPlugin(fp): boolean
    properties: create, query
    Was the attribute originally created by a plugin? Normally set
automatically when the API call is made - only added here to support
storing it in a file independently from the creating plugin.

---
hasMaxValue(hxv): boolean
    properties: create, query, edit
    Flag indicating whether an attribute has a maximum value.
(can only be used for numeric attributes).

---
hasMinValue(hnv): boolean
    properties: create, query, edit
    Flag indicating whether an attribute has a minimum value.
(can only be used for numeric attributes).

---
hasSoftMaxValue(hsx): boolean
    properties: create, query
    Flag indicating whether a numeric attribute has a soft maximum.

---
hasSoftMinValue(hsn): boolean
    properties: create, query
    Flag indicating whether a numeric attribute has a soft minimum.

---
hidden(h): boolean
    properties: create, query
    Will this attribute be hidden from the UI?

---
indexMatters(im): boolean
    properties: create, query
    Sets whether an index must be used when connecting
to this multi-attribute. Setting indexMatters to false forces the
attribute to non-readable.

---
internalSet(internalSet): boolean
    properties: create, query
    Whether or not the internal cached value is set when
this attribute value is changed.  This is an internal flag
used for updating UI elements.

---
keyable(k): boolean
    properties: create, query
    Is the attribute keyable by default?

---
longName(ln): string
    properties: create, query
    Sets the long name of the attribute.

---
maxValue(max): float
    properties: create, query, edit
    Specifies the maximum value for the attribute
(can only be used for numeric attributes).

---
minValue(min): float
    properties: create, query, edit
    Specifies the minimum value for the attribute
(can only be used for numeric attributes).

---
multi(m): boolean
    properties: create, query
    Makes the new attribute a multi-attribute.

---
niceName(nn): string
    properties: create, query, edit
    Sets the nice name of the attribute for display in the UI.  Setting the
attribute's nice name to a non-empty string overrides the default
behaviour of looking up the nice name from Maya's
string catalog.   (Use the MEL commands
"attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's
nice name in the catalog.)

---
numberOfChildren(nc): uint
    properties: create, query
    How many children will the new attribute have?

---
parent(p): string
    properties: create, query
    Attribute that is to be the new attribute's parent.

---
proxy(pxy): string
    properties: create, query
    Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.

---
readable(r): boolean
    properties: create, query
    Can outgoing connections be made from this attribute?

---
shortName(sn): string
    properties: create, query
    Sets the short name of the attribute.

---
softMaxValue(smx): float
    properties: create, query, edit
    Soft maximum, valid for numeric attributes only.  Specifies the
upper default limit used in sliders for this attribute.

---
softMinValue(smn): float
    properties: create, query, edit
    Soft minimum, valid for numeric attributes only.  Specifies the
lower default limit used in sliders for this attribute.

---
storable(s): boolean
    properties: create, query
    Can the attribute be stored out to a file?

---
usedAsColor(uac): boolean
    properties: create, query
    Is the attribute to be used as a color definition?
Must have 3 DOUBLE or 3 FLOAT children to use this
flag.  The attribute type "-at" should be "double3"
or "float3" as appropriate.  It can also be used to
less effect with data types "-dt" as "double3" or
"float3" as well but some parts of the code do not
support this alternative.  The special attribute
types/data "spectrum" and "reflectance" also support
the color flag and on them it is set by default.

---
usedAsFilename(uaf): boolean
    properties: create, query
    Is the attribute to be treated as a filename definition?
This flag is only supported on attributes with data type "-dt" of "string".

---
usedAsProxy(uap): boolean
    properties: create, query
    Set if the specified attribute should be treated as a proxy to another attributes.

---
worldSpace(ws): boolean
    properties: create, query
    Sets whether this attribute should be treated as worldspace.
Being worldspace indicates the attribute is dependent on the worldSpace
transformation of this node, and will be marked dirty by any attribute
changes in the hierarchy that affects the worldSpace transformation. The
attribute needs to be an array since during instancing there are
multiple worldSpace paths to the node and Maya requires one array element
per path for worldSpace attributes. Remarks:
1. Can only be used on array attributes.
2. This property is ignored on non-dag nodes.
3. The attribute should be affected by another attribute or have a connection.
   Otherwise, the attribute will not get computed and will not get dirty again.

---
writable(w): boolean
    properties: create, query
    Can incoming connections be made to this attribute?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/addAttr.html 
    """


def addDynamic() -> string:
    """Synopsis:
---
---
 addDynamic(
object object
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

addDynamic is undoable, NOT queryable, and NOT editable.
addDynamic makes the specified field or emitter a child of
the owner's transform (adding it to the model if it was not already
there), and makes the necessary attribute connections.

If either of the arguments is omitted, addDynamic searches the
selection list for objects to use instead. If more than one possible
owner or field/emitter is selected, addDynamic will do
nothing.

If the specified field/emitter already has a source, addDynamic will
remove the current source and replace it with the newly specified
source.

If a subset of the owner object's cvs/particles/vertices is selected,
addDynamic will add the field/emitter to that subset only.




Example:
---
import maya.cmds as cmds

Create an emitter
cmds.emitter( pos=(0, 0, 0), type='omni', r=100, sro=0, nuv=0, cye='none', cyi=1, spd=1, srn=0, nsp=1, tsp=0, mxd=0, mnd=0, dx=1, dy=0, dz=0, sp=0 )
Result: emitter1 ---


Get the emitter to emit particles
cmds.particle()
Result: particle2
cmds.connectDynamic( 'particle1', em='emitter1' )

Create a particle to use as the source of the emitter
cmds.particle( p=((6.0, 0, 7.0), (6.0, 0, 2.0)), c=1 )
Result: particle2

Use particle2 as a source of the emitter
cmds.addDynamic( 'emitter1', 'particle2' )

---
Return:
---


    string: The name of the source object and the field or emitter which was
attached to it.

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/addDynamic.html 
    """


def addExtension(attributeType: string, binaryTag: string, cachedInternally: boolean, category: string, dataType: string, defaultValue: float, disconnectBehaviour: uint, enumName: string, exists: boolean, fromPlugin: boolean, hasMaxValue: boolean, hasMinValue: boolean, hasSoftMaxValue: boolean, hasSoftMinValue: boolean, hidden: boolean, indexMatters: boolean, internalSet: boolean, keyable: boolean, longName: string, maxValue: float, minValue: float, multi: boolean, niceName: string, nodeType: string, numberOfChildren: uint, parent: string, proxy: string, readable: boolean, shortName: string, softMaxValue: float, softMinValue: float, storable: boolean, usedAsColor: boolean, usedAsFilename: boolean, usedAsProxy: boolean, worldSpace: boolean, writable: boolean) -> None:
    """Synopsis:
---
---
 addExtension([attributeType=string], [binaryTag=string], [cachedInternally=boolean], [category=string], [dataType=string], [defaultValue=float], [disconnectBehaviour=uint], [enumName=string], [exists=boolean], [fromPlugin=boolean], [hasMaxValue=boolean], [hasMinValue=boolean], [hasSoftMaxValue=boolean], [hasSoftMinValue=boolean], [hidden=boolean], [indexMatters=boolean], [internalSet=boolean], [keyable=boolean], [longName=string], [maxValue=float], [minValue=float], [multi=boolean], [niceName=string], [nodeType=string], [numberOfChildren=uint], [parent=string], [proxy=string], [readable=boolean], [shortName=string], [softMaxValue=float], [softMinValue=float], [storable=boolean], [usedAsColor=boolean], [usedAsFilename=boolean], [usedAsProxy=boolean], [worldSpace=boolean], [writable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

addExtension is NOT undoable, queryable, and editable.
This command is used to add an extension attribute to a node type.
Either the longName or the shortName or both must be specified.
If neither a dataType nor an attributeType is specified, a double
attribute will be added.  The dataType flag can be specified more than
once indicating that any of the supplied types will be accepted (logical-or).


To add a non-double attribute the following criteria
can be used to determine whether the dataType or the attributeType
flag is appropriate.  Some types, such as double3 can use either.
In these cases the -dt flag should be used when you only wish to
access the data as an atomic entity (eg. you never want to access the
three individual values that make up a double3).  In general it
is best to use the -at in these cases for maximum flexibility.
In most cases the -dt version will not display in the attribute
editor as it is an atomic type and you are not allowed to change
individual parts of it.


All attributes flagged as "(compound)" below or the compound attribute itself
are not actually added to the node until all of the children are defined
(using the "-p" flag to set their parent to the compound being created).  See
the EXAMPLES section for more details.



 Type of attribute               Flag and argument to use      
 boolean                                                 -at bool                      
 32 bit integer                                  -at long                      
 16 bit integer                                  -at short                     
 8 bit integer                                   -at byte                      
 char                                                    -at char                      
  enum                                                   -at enum (specify the enum names using the enumName flag)  
 float                                                   -at "float" (use quotes
                                                                        since float is a mel keyword)   
 double                                                  -at double            
 angle value                                     -at doubleAngle       
 linear value                                    -at doubleLinear      
 string                                                  -dt "string" (use quotes
                                                                        since string is a mel keyword)  
 array of strings                                -dt stringArray       
 compound                                                -at compound          
 message (no data)                               -at message           
 time                                                    -at time                      
 4x4 double matrix                               -dt "matrix" (use quotes
                                                                        since matrix is a mel keyword)  
 4x4 float matrix                                -at fltMatrix         
 reflectance                                     -dt reflectanceRGB
 reflectance (compound)                  -at reflectance       
 spectrum                                                -dt spectrumRGB       
 spectrum (compound)                     -at spectrum          
 2 floats                                                -dt float2            
 2 floats (compound)                     -at float2            
 3 floats                                                -dt float3            
 3 floats (compound)                     -at float3            
 2 doubles                                               -dt double2           
 2 doubles (compound)                    -at double2           
 3 doubles                                               -dt double3           
 3 doubles (compound)                    -at double3           
 2 32-bit integers                               -dt long2                     
 2 32-bit integers (compound)    -at long2                     
 3 32-bit integers                               -dt long3                     
 3 32-bit integers (compound)    -at long3                     
 2 16-bit integers                               -dt short2            
 2 16-bit integers (compound)    -at short2            
 3 16-bit integers                               -dt short3            
 3 16-bit integers (compound)    -at short3            
 array of doubles                                -dt doubleArray       
 array of floats                                 -dt floatArray        
 array of 32-bit ints                    -dt Int32Array        
 array of vectors                                -dt vectorArray       
 nurbs curve                                     -dt nurbsCurve        
 nurbs surface                                   -dt nurbsSurface      
 polygonal mesh                                  -dt mesh                      
 lattice                                                 -dt lattice           
 array of double 4D points               -dt pointArray        




Example:
---
import maya.cmds as cmds

Add an attribute named ms/mass with a default value of 1 and a
minimum value of 0.001 and a maximum of 10000 to all mesh shapes.
---

cmds.addExtension( nodeType='mesh', shortName='ms', longName='mass', defaultValue=1.0, minValue=0.001, maxValue=10000 )

Add a multi attribute named ff/forcefield of type double3 to all mesh shapes.
---

cmds.addExtension( nodeType='mesh', shortName='ff', longName='forcefield', dataType='double3', multi=True )

Add a compound attribute named sampson with children home, midge,
damien, elizabeth, and sweetpea of varying types to all choice nodes.
---

cmds.addExtension( nodeType='choice', longName='sampson', numberOfChildren=5, attributeType='compound' )
cmds.addExtension( nodeType='choice', longName='home', attributeType='matrix', parent='sampson' )
cmds.addExtension( nodeType='choice', longName='midge', attributeType='message', parent='sampson' )
cmds.addExtension( nodeType='choice', longName='damien', attributeType='double', parent='sampson' )
cmds.addExtension( nodeType='choice', longName='elizabeth', attributeType='double', parent='sampson' )
cmds.addExtension( nodeType='choice', longName='sweetpea', attributeType='double', parent='sampson' )

To add an attribute that is to be interpreted as a color the
following attribute group must be used.
---

Note that the word "float" must be in quotations since it is a
MEL keyword.
---

cmds.addExtension( nodeType='phong', longName='rainbow', usedAsColor=True, attributeType='float3' )
cmds.addExtension( nodeType='phong', longName='redBow', attributeType='float', parent='rainbow' )
cmds.addExtension( nodeType='phong', longName='greenBow', attributeType='float', parent='rainbow' )
cmds.addExtension( nodeType='phong', longName='blueBow', attributeType='float', parent='rainbow' )

Other legal attribute types that can be interpreted as colors need
not specify the "-usedAsColor" flag as it will be assumed.  These
include "-attributeType spectrum", "-attributeType reflectance",
"-dataType spectrumRGB", and "-dataType reflectanceRGB".
---

cmds.addExtension( nodeType='phong', longName='implColor', dataType='spectrumRGB' )

Add a double3 attribute named sanders with children bess, les and wes
to all dag nodes, including shapes, transforms, and joints.
---

cmds.addExtension( nodeType='dagNode', longName='sanders', attributeType='double3' )
cmds.addExtension( nodeType='dagNode', longName='bess', attributeType='double', parent='sanders' )
cmds.addExtension( nodeType='dagNode', longName='les', attributeType='double', parent='sanders' )
cmds.addExtension( nodeType='dagNode', longName='wes', attributeType='double', parent='sanders' )

---


Flags:
---


---
nodeType(nt): string
    properties: create, query, edit
    Specifies the type of node to which the attribute will be added.
See the nodeType command for the names of different node types.

---
attributeType(at): string
    properties: create, query
    Specifies the attribute type, see above table for more details.
Note that the attribute types "float", "matrix" and "string"
are also MEL keywords and must be enclosed in quotes.

---
binaryTag(bt): string
    properties: create, query
    This flag is obsolete and does not do anything any more

---
cachedInternally(ci): boolean
    properties: create, query
    Whether or not attribute data is cached internally in the node.
This flag defaults to true for writable attributes and false
for non-writable attributes. A warning will be issued if
users attempt to force a writable attribute to be uncached as
this will make it impossible to set keyframes.

---
category(ct): string
    properties: create, query, edit, multiuse
    An attribute category is a string associated with the attribute to identify it.
(e.g. the name of a plugin that created the attribute, version information, etc.)
Any attribute can be associated with an arbitrary number of categories however
categories can not be removed once associated.

---
dataType(dt): string
    properties: create, query, multiuse
    Specifies the data type.  See "setAttr" for
more information on data type names.

---
defaultValue(dv): float
    properties: create, query, edit
    Specifies the default value for the attribute
(can only be used for numeric attributes).

---
disconnectBehaviour(dcb): uint
    properties: create, query
    defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete

---
enumName(en): string
    properties: create, query, edit
    Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)

---
exists(ex): boolean
    properties: create, query
    Returns true if the attribute queried is a user-added, dynamic attribute; false if not.

---
fromPlugin(fp): boolean
    properties: create, query
    Was the attribute originally created by a plugin? Normally set
automatically when the API call is made - only added here to support
storing it in a file independently from the creating plugin.

---
hasMaxValue(hxv): boolean
    properties: create, query, edit
    Flag indicating whether an attribute has a maximum value.
(can only be used for numeric attributes).

---
hasMinValue(hnv): boolean
    properties: create, query, edit
    Flag indicating whether an attribute has a minimum value.
(can only be used for numeric attributes).

---
hasSoftMaxValue(hsx): boolean
    properties: create, query
    Flag indicating whether a numeric attribute has a soft maximum.

---
hasSoftMinValue(hsn): boolean
    properties: create, query
    Flag indicating whether a numeric attribute has a soft minimum.

---
hidden(h): boolean
    properties: create, query
    Will this attribute be hidden from the UI?

---
indexMatters(im): boolean
    properties: create, query
    Sets whether an index must be used when connecting
to this multi-attribute. Setting indexMatters to false forces the
attribute to non-readable.

---
internalSet(internalSet): boolean
    properties: create, query
    Whether or not the internal cached value is set when
this attribute value is changed.  This is an internal flag
used for updating UI elements.

---
keyable(k): boolean
    properties: create, query
    Is the attribute keyable by default?

---
longName(ln): string
    properties: create, query
    Sets the long name of the attribute.

---
maxValue(max): float
    properties: create, query, edit
    Specifies the maximum value for the attribute
(can only be used for numeric attributes).

---
minValue(min): float
    properties: create, query, edit
    Specifies the minimum value for the attribute
(can only be used for numeric attributes).

---
multi(m): boolean
    properties: create, query
    Makes the new attribute a multi-attribute.

---
niceName(nn): string
    properties: create, query, edit
    Sets the nice name of the attribute for display in the UI.  Setting the
attribute's nice name to a non-empty string overrides the default
behaviour of looking up the nice name from Maya's
string catalog.   (Use the MEL commands
"attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's
nice name in the catalog.)

---
numberOfChildren(nc): uint
    properties: create, query
    How many children will the new attribute have?

---
parent(p): string
    properties: create, query
    Attribute that is to be the new attribute's parent.

---
proxy(pxy): string
    properties: create, query
    Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.

---
readable(r): boolean
    properties: create, query
    Can outgoing connections be made from this attribute?

---
shortName(sn): string
    properties: create, query
    Sets the short name of the attribute.

---
softMaxValue(smx): float
    properties: create, query, edit
    Soft maximum, valid for numeric attributes only.  Specifies the
upper default limit used in sliders for this attribute.

---
softMinValue(smn): float
    properties: create, query, edit
    Soft minimum, valid for numeric attributes only.  Specifies the
lower default limit used in sliders for this attribute.

---
storable(s): boolean
    properties: create, query
    Can the attribute be stored out to a file?

---
usedAsColor(uac): boolean
    properties: create, query
    Is the attribute to be used as a color definition?
Must have 3 DOUBLE or 3 FLOAT children to use this
flag.  The attribute type "-at" should be "double3"
or "float3" as appropriate.  It can also be used to
less effect with data types "-dt" as "double3" or
"float3" as well but some parts of the code do not
support this alternative.  The special attribute
types/data "spectrum" and "reflectance" also support
the color flag and on them it is set by default.

---
usedAsFilename(uaf): boolean
    properties: create, query
    Is the attribute to be treated as a filename definition?
This flag is only supported on attributes with data type "-dt" of "string".

---
usedAsProxy(uap): boolean
    properties: create, query
    Set if the specified attribute should be treated as a proxy to another attributes.

---
worldSpace(ws): boolean
    properties: create, query
    Sets whether this attribute should be treated as worldspace.
Being worldspace indicates the attribute is dependent on the worldSpace
transformation of this node, and will be marked dirty by any attribute
changes in the hierarchy that affects the worldSpace transformation. The
attribute needs to be an array since during instancing there are
multiple worldSpace paths to the node and Maya requires one array element
per path for worldSpace attributes. Remarks:
1. Can only be used on array attributes.
2. This property is ignored on non-dag nodes.
3. The attribute should be affected by another attribute or have a connection.
   Otherwise, the attribute will not get computed and will not get dirty again.

---
writable(w): boolean
    properties: create, query
    Can incoming connections be made to this attribute?

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/addExtension.html 
    """


def addMetadata(channelName: string, channelType: string, indexType: string, scene: boolean, streamName: string, structure: string) -> list[string]:
    """Synopsis:
---
---
 addMetadata([channelName=string], [channelType=string], [indexType=string], [scene=boolean], [streamName=string], [structure=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

addMetadata is undoable, queryable, and NOT editable.
Defines the attachment of a metadata structure to one or more selected
objects. This creates a placeholder with an empty metadata Stream for
later population through the editMetadata command. It's similar
in concept to the addAttr command for nodes - a data description
is added but no data is actually set.


When assigning a metadata structure you must specify these flags
- channelName is the metadata channel type (e.g. "vertex"),
streamName is the name of the metadata stream to be created,
and structure is the name of the structure type defining the
contents of the metadata. The indexType flag is optional.
If it is not present then the index will be presumed to be a standard
numerical value.


You can query metadata information at a variety of levels. See the
table below for a full list of the queryable arguments. In each case
the specification of any of the non-queried arguments filters the list
of metadata to be examined during the query. For all queries a single
object must be selected for querying.


For example querying the channelName flag with no other
arguments will return the list of all Channel types on the selected
object that contain any metadata. Querying the channelName flag
with the indexType flag specified will return only those
channel types containing metadata streams that use that particular
type of index.


Query the channelName flag to return the list of any channel types
that have metadata.
Specify the channelName and streamName flags and query the
structure flag to return the name of the structure assigned to the
given stream (if any).
Specify a channelName and query the streamName to return
the list of all streams assigned to that particular channel type.
If you query the streamName without a specific channelName
then it returns a list of pairs of (channelName, streamName) for all metadata
streams.


Flag Combinations:

ChannelName IndexType StreamName Structure   Create   Can Query
     0          0          0         0         X        ChannelName, StreamName, Structure
     0          0          0         1         X        ChannelName, StreamName, IndexType
     0          0          1         0         X        ChannelName, Structure, IndexType
     0          0          1         1         X        ChannelName, IndexType
     0          1          0         0         X        ChannelName, StreamName, Structure
     0          1          0         1         X        ChannelName, StreamName
     0          1          1         0         X        ChannelName, Structure
     0          1          1         1         X        ChannelName
     1          0          0         0         X        StreamName, Structure, IndexType
     1          0          0         1         X        StreamName, IndexType
     1          0          1         0         X        Structure, IndexType
     1          0          1         1        (a)       IndexType
     1          1          0         0         X        StreamName, Structure
     1          1          0         1         X        StreamName
     1          1          1         0         X        Structure
     1          1          1         1        (b)       X
    (a) Assign an empty metadata stream with default index type
    (b) Assign an empty metadata stream with the named index type




Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.polyPlane( name='p', ch=False )
cmds.select( 'pShape', replace=True )
cmds.dataStructure( format='raw', asString='name=IdStruct:int32=ID' )
cmds.dataStructure( format='raw', asString='name=OffStruct:float=Offset' )
cmds.dataStructure( format='raw', asString='name=OrgStruct:float[3]=Origin Point' )
Add three metadata streams
cmds.addMetadata( streamName='IdStream', channelName='vertex', structure='IdStruct' )
cmds.addMetadata( streamName='OffStream', channelName='vertex', structure='OffStruct' )
cmds.addMetadata( streamName='OrgStream', channelName='edge', structure='OrgStruct' )
cmds.addMetadata( streamName='VFStream', channelName='vertexFace', indexType='pair', structure='OrgStruct' )

Query for the list of all channel types possessing metadata
cmds.addMetadata( query=True, channelName=True )
Return: ['edge', 'vertex', 'vertexFace'] ---


Query for the structure assigned to a specific stream
cmds.addMetadata( channelName='vertex', streamName='OffStream', query=True, structure=True )
Return: 'OffStruct' ---


Query for the list of all streams on a specific channel type
cmds.addMetadata( channelName='vertex', query=True, streamName=True )
Return: ['IdStream', 'OffStream'] ---


Query for the list of all streams
cmds.addMetadata( query=True, streamName=True )
Return: ['IdStream', 'OffStream', 'OrgStream', 'VFStream'] ---


You can combine queries to answer more general questions about the
metadata on an object. For example suppose you wanted to know the
index type used by all Streams on the 'vertex' Channel.
First extract the list of Streams on the Channel
streams = cmds.addMetadata( channelName='vertex', query=True, streamName=True )
Loop through each Stream, querying the IndexType only for that Stream
for stream in streams:
        indexType = cmds.addMetadata( channelName='vertex', streamName=stream, query=True, indexType=True )[0]
        print 'Index type on %s is %s' % (stream, indexType)

---
Return:
---


    list[string]: List of nodes to which a new Stream was successfully added (create mode)
    list[string]: List of channel types containing metadata on an object when querying the channelName flag
    list[string]: List of stream names on an object when querying the streamName flag
    list[string]: List of structures used by an object's metadata Streams when querying the structure flag
    list[string]: List of index types used by an object when querying the indexType flag

Flags:
---


---
channelName(cn): string
    properties: create, query
    Name of the Channel type to which the structure is to be added (e.g. "vertex").
                        In query mode, this flag can accept a value.

---
channelType(cht): string
    properties: create, query
    Obsolete - use the 'channelName' flag instead.
                        In query mode, this flag can accept a value.

---
indexType(idt): string
    properties: create, query
    Name of the index type the new Channel should be using. If not specified this defaults
to a simple numeric index. Of the native types only a mesh "vertexFace" channel is
different, using a "pair" index type.
                        In query mode, this flag can accept a value.

---
scene(scn): boolean
    properties: create, query
    Use this flag when you want to add metadata to the scene as a whole rather than to
any individual nodes. If you use this flag and have nodes selected the nodes will
be ignored and a warning will be displayed.

---
streamName(stn): string
    properties: create, query
    Name of the empty stream being created. In query mode not specifying a value will
return a list of streams on the named channel type.
                        In query mode, this flag can accept a value.

---
structure(str): string
    properties: create, query
    Name of the structure which defines the metadata to be attached to the object.
In query mode this will return the name of the structure attached at a given
stream.
                        In query mode, this flag can accept a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/addMetadata.html 
    """


def addPP(attribute: string) -> list[string]:
    """Synopsis:
---
---
 addPP(
objects
    , [attribute=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

addPP is undoable, NOT queryable, and NOT editable.
The command adds any other necessary attributes wherever they are
needed, and makes all necessary connections.  If any of the attributes
already exist, the command simply connects to them.  The command also
toggles any relevant attributes in the emitter or field to indicate
that per-point capability is being used.

The command adds a separate per-point attribute to the owning object
for each emitter/field.  For example, for emission rate, there is a
separate ratePP for each emitter.  These attributes are named
according to the convention <emitter/field name><attr
name>PP.  For example, if a particle shape owned an emitter
"smoke", that shape would get attribute "smokeRatePP."

The name of the object must be the emitter or field for which
per-point capability is to be added (or the name of its parent
transform).  The addPP command adds the per-point capability for that
emitter or field but not for any others owned by the same object.  If
per-point capability is not supported for a named object, the command
will trigger a warning, but will continue executing for any other
objects which were valid.

If no objects are named, addPP uses any objects in the current
selection list for which the specified attribute is applicable.  (For
example, it would add per-point rate for all selected emitters.)

If addPP detects that the owner object has left-over attributes from a
deleted emitter, it will remove those attributes before adding the new
ones.  Thus, you can delete the emitter, make a new one, and run addPP
again, and addPP will clean up after the deleted emitter.  This is
most commonly used if you have a geometry emitter and then decide to
change the geometry.  Likewise, if addPP detects that some cvs or
vertices have been added to the geometry, then it will expand the
corresponding multi-attributes as necessary.  However, if it detects
that some cvs/vertices have been removed, it will not remove any
entries from the multi.  See the user manual for more discussion.




Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

cmds.emitter( n='myEmitter1' )
cmds.particle( n='myParticle1' )
cmds.connectDynamic( 'myParticle1', em='myEmitter1' )
cmds.select( 'myParticle1' )
cmds.emitter( n='myEmitter2' )
cmds.particle( n='myParticle2' )
cmds.connectDynamic( 'myParticle2', em='myEmitter2' )

cmds.addPP( 'myEmitter2', atr='rate' )

Suppose that myEmitter2 is owned by a particle shape, "myParticle1."
addPP will add an attribute "myEmitter2RatePP" to myParticle1, will connect
myParticle1.myEmitter2RatePP to myEmitter2.ratePP, and will set myEmitter2.useRatePP
to true.

---
Return:
---


    list[string]: Returns names of emitters/fields for which the per-point
capability was added for the specified attribute.

Flags:
---


---
attribute(atr): string
    properties: create
    Name of attribute to which you wish to add PP capability.
Currently the only attribute supported is rate (for emitters).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/addPP.html 
    """


def affectedNet(type: string) -> None:
    """Synopsis:
---
---
 affectedNet(
[node...]
    , [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

affectedNet is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a network of this transform node's attributes that affect
each other
cmds.affectedNet( 'transform1' )

Create a network all of the transform shared attributes that affect
each other
cmds.affectedNet( t='transform' )

Create a network of the revolve and shape node type attributes that
affect each other
cmds.affectedNet( t='revolve', t='shape' )

---


Flags:
---


---
type(t): string
    properties: create
    Get information from the given node type instead of one node

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/affectedNet.html 
    """


def affects(by: boolean, type: string) -> string:
    """Synopsis:
---
---
 affects(string, [by=boolean], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

affects is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

List the attributes on node "sphere" that affect the "tx" attribute
cmds.sphere( n='sphere' )
cmds.affects( 'tx', 'sphere' )

List the attributes on nodes of type "transform" that are affected by
the "ty" attribute
cmds.affects( 'ty', by=True, t='transform' )

List the attributes on nodes of type "revolve" that affect the
"outputSurface" attribute
cmds.affects( 'outputSurface', t='revolve' )

---
Return:
---


    string: List of affected/affecting attributes

Flags:
---


---
by(): boolean
    properties: create
    Show attributes that are affected by the given one rather than the
ones that affect it.

---
type(t): string
    properties: create
    static node type from which to get 'affects' information

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/affects.html 
    """


def aimConstraint(aimVector: tuple[float, float, float], layer: string, maintainOffset: boolean, name: string, offset: tuple[float, float, float], remove: boolean, skip: string, targetList: boolean, upVector: tuple[float, float, float], weight: float, weightAliasList: boolean, worldUpObject: name, worldUpType: string, worldUpVector: tuple[float, float, float]) -> list[string]:
    """Synopsis:
---
---
 aimConstraint(
[target...] object
    , [aimVector=[float, float, float]], [layer=string], [maintainOffset=boolean], [name=string], [offset=[float, float, float]], [remove=boolean], [skip=string], [targetList=boolean], [upVector=[float, float, float]], [weight=float], [weightAliasList=boolean], [worldUpObject=name], [worldUpType=string], [worldUpVector=[float, float, float]])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

aimConstraint is undoable, queryable, and editable.
An aimConstraint takes as input one or more "target" DAG transform
nodes at which to aim the single "constraint object" DAG transform
node.  The aimConstraint orients the constrained object such that
the aimVector (in the object's local coordinate system) points to
the in weighted average of the world space position target
objects.  The upVector (again the the object's local coordinate
system) is aligned in world space with the worldUpVector.




Example:
---
import maya.cmds as cmds

Orients the aim vector of cube1 in it's local coordinate space, to point at cone1.
cmds.aimConstraint( 'cone1', 'cube1' )

Aims cube2 at the average of the position of cone1 and surf2
cmds.aimConstraint( 'cone1', 'surf2', 'cube2', w=.1 )

Sets the weight for cone1's effect on cube2 to 10.
cmds.aimConstraint( 'cone1', 'cube2', e=True, w=10.0 )

Removes surf2 from cube2's aimConstraint.
cmds.aimConstraint( 'surf2', 'cube2', e=True, rm=True )

Adds surf3 to cube2's aimConstraint with the default weight.
cmds.aimConstraint( 'surf3', 'cube2' )

Aim constrain the z-axis only of sph2 to sph1
cmds.aimConstraint( 'sph1', 'sph2', skip=["x","y"] )

---
Return:
---


    list[string]: name of the created constraint node

Flags:
---


---
aimVector(aim): [float, float, float]
    properties: create, query, edit
    Set the aim vector.  This is the vector in local
coordinates that points at the target.  If not given at creation
time, the default value of (1.0, 0.0, 0.0) is used.

---
layer(l): string
    properties: create, edit
    Specify the name of the animation layer where the constraint should be added.

---
maintainOffset(mo): boolean
    properties: create
    The offset necessary to preserve the constrained
object's initial rotation will be calculated and used as the
offset.

---
name(n): string
    properties: create, query, edit
    Sets the name of the constraint node to the specified
name.  Default name is constrainedObjectName_constraintType

---
offset(o): [float, float, float]
    properties: create, query, edit
    Sets or queries the value of the offset. Default is 0,0,0.

---
remove(rm): boolean
    properties: edit
    removes the listed target(s) from the constraint.

---
skip(sk): string
    properties: create, edit, multiuse
    Specify the axis to be skipped. Valid values are "x", "y", "z" and
"none". During creation, "none" is the default.

---
targetList(tl): boolean
    properties: query
    Return the list of target objects.

---
upVector(u): [float, float, float]
    properties: create, query, edit
    Set local up vector.  This is the vector in local
coordinates that aligns with the world up vector.  If not given
at creation time, the default value of (0.0, 1.0, 0.0) is used.

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

---
worldUpObject(wuo): name
    properties: create, query, edit
    Set the DAG object use for worldUpType "object" and
"objectrotation". See worldUpType for greater detail.
The default value is no up object, which is interpreted
as world space.

---
worldUpType(wut): string
    properties: create, query, edit
    Set the type of the world up vector computation.
The worldUpType can have one of 5 values: "scene",
"object", "objectrotation", "vector", or "none".
If the value is "scene", the upVector is
aligned with the up axis of the scene and
worldUpVector and worldUpObject are ignored.
If the value is "object", the upVector is
aimed as closely as possible to the
origin of the space of the worldUpObject and
the worldUpVector is ignored.
If the value is "objectrotation" then the
worldUpVector is interpreted as being in
the coordinate space of the worldUpObject, transformed into
world space and the upVector is aligned as
closely as possible to the result.
If the value is "vector", the upVector
is aligned with worldUpVector as closely as
possible and worldUpMatrix is ignored.
Finally, if the value is "none" no twist calculation
is performed by the constraint, with the resulting "upVector"
orientation based previous orientation of the
constrained object, and the "great circle" rotation needed
to align the aim vector with its constraint.
The default worldUpType is "vector".

---
worldUpVector(wu): [float, float, float]
    properties: create, query, edit
    Set world up vector.  This is the vector in world
coordinates that up vector should align with.
See -wut/worldUpType (below)for greater detail.
If not given at creation time, the default
value of (0.0, 1.0, 0.0) is used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/aimConstraint.html 
    """


def air(attenuation: float, directionX: float, directionY: float, directionZ: float, enableSpread: boolean, fanSetup: boolean, inheritRotation: boolean, inheritVelocity: float, magnitude: float, maxDistance: linear, name: string, perVertex: boolean, position: tuple[linear, linear, linear], speed: float, spread: float, torusSectionRadius: linear, velocityComponentOnly: boolean, volumeExclusion: boolean, volumeOffset: tuple[linear, linear, linear], volumeShape: string, volumeSweep: angle, wakeSetup: boolean, windSetup: boolean) -> string:
    """Synopsis:
---
---
 air(
[objects]
    , [attenuation=float], [directionX=float], [directionY=float], [directionZ=float], [enableSpread=boolean], [fanSetup=boolean], [inheritRotation=boolean], [inheritVelocity=float], [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear, linear]], [speed=float], [spread=float], [torusSectionRadius=linear], [velocityComponentOnly=boolean], [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle], [wakeSetup=boolean], [windSetup=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

air is undoable, queryable, and editable.
If fields are created, this command returns the names of each
owning shape and of the field shapes themselves. If a field was queried,
the results of the query are returned. If a field was edited, the field
name is returned.

If no object names are provided but the active selection list is non-empty,
the command creates a field for every object in the list. If the
list is empty, the command defaults to -pos 0 0 0.
The air field simulates the effects of moving air. The affected objects
will be accelerated or decelerated so that their velocities match that
of the air.

With the '-vco true' flag thrown, only accelerations are applied.
By parenting an air field to a moving part of an object (ie. a foot of a
character) and using '-i 1 -m 0 -s .5 -vco true' flags, one can simulate
the movement of air around the
foot as it moves, since the TOTAL velocity vector of the field would be
only based on the
movement of the foot. This can be done while the character walks through
leaves or dust on the ground.


For each listed object, the command creates a new field.
The transform is the associated dependency node.
Use connectDynamic to cause the field to affect a dynamic object.

If fields are created,  this command returns the field names. If
a field was queried, the results of the query are returned. If a field
was edited, the field name is returned.

If the -pos flag is specified, a field is created at the position specified.
If not, if object names are provided or the active selection list is
non-empty, the command creates a field for every object in the list and
calls addDynamic to add it to the object; otherwise the command defaults
to -pos 0 0 0.

Setting the -pos flag with objects named on the command line is an error.




Example:
---
import maya.cmds as cmds

cmds.air( name='particle1', m=5.0, mxd=2.0 )
Creates an air field with magnitude 5.0 and maximum distance 2.0,
and adds it to the list
of fields particle1 owns.

cmds.air( wakeSetup=True )
Creates an air field with no no velocity in and of itself (magnitude = 0).
All of the air's
velocity is derived from the motion of the objects that own the field.

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
directionZ(dz): float
    properties: query, edit
    Direction that the air will try to match the affected
particles' velocity to. NOTE: This is not the velocity; this is only
the direction. Use the -s flag to set the speed.

---
enableSpread(es): boolean
    properties: query, edit
    This tells the system whether or not to use the spread
angle given by '-sp'. If this is 'false' then all connected objectswithin the maximum distance will
be affected. Also, if this is set to 'false', all affected objects are forced to match their velocities
along the direction vector. If this is set to 'true' and spread is used, then the direction of the force
is along the direction from the field to the object.

---
fanSetup(fs): boolean
    properties: edit
    Similar to 'windSetup' except that the effects of a fan or
a person blowing air are approximated. The user can pass the same
flags on the command line to adjust them from the defaults. These are
the values that get set to approximate a 'fan':
inheritVelocity 1.0
inheritRotation true
componentOnly false
enableSpread true
spread .5 (45 degrees from center )

---
inheritRotation(iro): boolean
    properties: query, edit
    If this is set to 'true', then the direction vector
described with -dx, -dy, and -dz will be considered local to the owning object. Therefore, if the
owning object's transform undergoes any rotation (by itself or one of its parents), the direction
vector of the air field will undergo that same rotation.

---
inheritVelocity(iv): float
    properties: query, edit
    Amount (from 0 to 1) of the field-owner's velocity added to the
vector determined by the direction and speed flags. The combination
of these two vectors makes
up the TOTAL velocity vector for the air field. This allows the air
to be determined directly by the motion of the owning object.

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
speed(s): float
    properties: query, edit
    How fast the affected objects' speed reaches the speed (based on the -mag, -dx, -dy, -dz flags) of the air field.
This value gets clamped internally to be between 0.0 and 1.0.  A value of 0.0 will make the air field have no effect.
A value of 1.0 will try to match the air field's speed much quicker, but not necessarily immediately.

---
spread(sp): float
    properties: query, edit
    This represents the angle from the direction vector within which
objects will be affected. The values are in the range of 0 to 1.
A value of 0 will result in an effect only
exactly in front of the air field along the direction vector. A
value of 1 will result in any object in front of the owning object, 90
degrees in all direction from the direction vector.

---
torusSectionRadius(tsr): linear
    properties: query, edit
    Section radius for a torus volume.  Applies only to torus.
Similar to the section radius in the torus modelling primitive.

---
velocityComponentOnly(vco): boolean
    properties: query, edit
    If this is 'false', the air will accelerate or decelerate
the affected objects so that their velocities will eventually match
the TOTAL velocity vector of the air field. If this is 'true',
only ACCELERTION is applied to the affected objects so that their
velocity component along the TOTAL velocity vector matches or is
greater in magnitude than the TOTAL velocity vector. This will not
slow objects down to match velocities, only speed them up
to match components. This is most useful when using the -iv flag
with a value >0.

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

---
wakeSetup(wks): boolean
    properties: edit
    Like the 'windSetup' and 'fanSetup', 'wakeSetup'
sets certain values in the field to approximate the movement of air
near a moving object, such as  a character's foot or hand.
The values that are set are:
inheritVelocity 1.0
inheritRotation false
componentOnly true
enableSpread false
speed 0.0

---
windSetup(wns): boolean
    properties: edit
    This will set some of the values above in a way that
approximates the effects of a basic wind. This allows the user to then change certain values as
he/she wishes on the same command line. First the preset values get set, and then any other flags
that were passed get taken into account. These are the values that get set to approximate 'wind':
inheritVelocity 0.0
inheritRotation true
componentOnly false
enableSpread false

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/air.html 
    """


def aliasAttr(remove: boolean) -> list[string]:
    """Synopsis:
---
---
 aliasAttr([remove=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

aliasAttr is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.createNode( 'blendShape', n='blender' )
---

Define intuitive names for the weights of a blendShape.
The blendShape command does this automatically to allow you
to refer to the weight corresponding to a target shape by the name
of that shape.
---

cmds.aliasAttr( 'smile', 'blender.w[0]', 'frown', 'blender.w[1]' )
Result: 2 ---

---

List all the attribute aliases for the node blendShape1
---

cmds.aliasAttr( 'blender', query=True )
Result: smile weight[0] frown weight[1] ---

---

Allow the X rotation on a joint to be called its "roll"
---

cmds.createNode( 'joint', n='elbow' )
cmds.aliasAttr( 'roll', 'elbow.rx' )
Result: 1 ---

cmds.aliasAttr( 'tuck', 'elbow.ry' )
Result: 1 ---

---

Remove the roll alias defined above.
---

cmds.aliasAttr( 'elbow.roll', rm=True )
---

Remove the tuck alias defined above.
---

cmds.aliasAttr( 'elbow.ry', rm=True )

---
Return:
---


    list[string]: in query mode.

Flags:
---


---
remove(rm): boolean
    properties: create
    Specifies that aliases listed should be removed (otherwise new aliases
are added).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/aliasAttr.html 
    """


def align(alignToLead: boolean, coordinateSystem: name, xAxis: string, yAxis: string, zAxis: string) -> boolean:
    """Synopsis:
---
---
 align([alignToLead=boolean], [coordinateSystem=name], [xAxis=string], [yAxis=string], [zAxis=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

align is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

align the selected objects to their average mid-point in x
cmds.align(x='mid')

align the selected objects to the mid-point in x of the first select object
cmds.align(x='mid', alignToLead=True)

---
Return:
---


    boolean: true/false

Flags:
---


---
alignToLead(atl): boolean
    properties: create
    When set, the min, center or max values are computed from the
lead object. Otherwise, the values are averaged for all objects.
Default is false

---
coordinateSystem(cs): name
    properties: create
    Defines the X, Y, and Z coordinates. Default is the world coordinates

---
xAxis(x): string
    properties: create
    Any of none, min, mid, max, dist, stack.
This defines the kind of alignment to perfom, default is none.

---
yAxis(y): string
    properties: create
    Any of none, min, mid, max, dist, stack.
This defines the kind of alignment to perfom, default is none.

---
zAxis(z): string
    properties: create
    Any of none, min, mid, max, dist, stack.
This defines the kind of alignment to perfom, default is none.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/align.html 
    """


def alignCtx(align: boolean, anchorFirstObject: boolean, distribute: boolean, exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string, showAlignTouch: boolean) -> string:
    """Synopsis:
---
---
 alignCtx(
[contextName]
    , [align=boolean], [anchorFirstObject=boolean], [distribute=boolean], [exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string], [showAlignTouch=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

alignCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a poly sphere and a poly cube, then move them apart
cmds.polySphere(r=3, n='pSphere1')
cmds.move(5, 0, 0)
cmds.polyCube(w=3, h=3, d=3, n='pCube1')
cmds.move(-5, 3, 0)
cmds.select('pSphere1', 'pCube1', r=True)

Create a new align context which is used to align objects, then switch to it
Now you can use this tool to align objects
cmds.alignCtx('alignCtx1',a=True)
cmds.setToolTo('alignCtx1')

---
Return:
---


    string: (name of the new context)

Flags:
---


---
align(a): boolean
    properties: create, query, edit
    Align objects

---
anchorFirstObject(afo): boolean
    properties: create, query, edit
    Anchor first or last selected object. Default false.
Only applicable when aligning objects.

---
distribute(d): boolean
    properties: create, query, edit
    Distribute objects

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
showAlignTouch(sat): boolean
    properties: create, query, edit
    Show or hide align touching handles. Default true.
Only applicable when aligning objects.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/alignCtx.html 
    """


def alignCurve(attach: boolean, caching: boolean, constructionHistory: boolean, curvatureContinuity: boolean, curvatureScale1: float, curvatureScale2: float, joinParameter: float, keepMultipleKnots: boolean, name: string, nodeState: int, object: boolean, positionalContinuity: boolean, positionalContinuityType: int, replaceOriginal: boolean, reverse1: boolean, reverse2: boolean, tangentContinuity: boolean, tangentContinuityType: int, tangentScale1: float, tangentScale2: float) -> list[string]:
    """Synopsis:
---
---
 alignCurve(
[curve] [curve]
    , [attach=boolean], [caching=boolean], [constructionHistory=boolean], [curvatureContinuity=boolean], [curvatureScale1=float], [curvatureScale2=float], [joinParameter=float], [keepMultipleKnots=boolean], [name=string], [nodeState=int], [object=boolean], [positionalContinuity=boolean], [positionalContinuityType=int], [replaceOriginal=boolean], [reverse1=boolean], [reverse2=boolean], [tangentContinuity=boolean], [tangentContinuityType=int], [tangentScale1=float], [tangentScale2=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

alignCurve is undoable, queryable, and editable.
Positional continuity means the curves (move) or the ends of the
curves (modify) are changed.

Tangent continuity means one of the curves is modified to be tangent
at the points where they meet.

Curvature continuity means one of the curves is modified to be
curvature continuous as well as tangent.

The default behaviour, when no curves or flags are passed, is to only
do positional and tangent continuity on the active list with the end
of the first curve and the start of the other curve used for alignment.




Example:
---
import maya.cmds as cmds

Do modify positional continuity on both curves with no history:
cmds.alignCurve( ch=False, pc=True, pct=6 )

Do positional and tangent continuity, with the second curve
tangent modified (by default move position continuity is done
on the first curve):
cmds.alignCurve( tc=True, tct=2 )

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
curvatureContinuity(cc): boolean
    properties: create, query, edit
    Curvature continuity is on if true and off otherwise.
Default: false

---
curvatureScale1(cs1): float
    properties: create, query, edit
    Curvature scale applied to curvature of first curve for curvature continuity.
Default: 0.0

---
curvatureScale2(cs2): float
    properties: create, query, edit
    Curvature scale applied to curvature of second curve for curvature continuity.
Default: 0.0

---
joinParameter(jnp): float
    properties: create, query, edit
    Parameter on reference curve where modified curve is to be aligned to.
Default: 123456.0

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
positionalContinuity(pc): boolean
    properties: create, query, edit
    Positional continuity is on if true and off otherwise.
Default: true

---
positionalContinuityType(pct): int
    properties: create, query, edit
    Positional continuity type legal values:
1 - move first curve,
2 - move second curve,
3 - move both curves,
4 - modify first curve,
5 - modify second curve,
6 - modify both curves
Default: 1

---
reverse1(rv1): boolean
    properties: create, query, edit
    If true, reverse the first input curve before doing align. Otherwise, do nothing to the first input curve before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
reverse2(rv2): boolean
    properties: create, query, edit
    If true, reverse the second input curve before doing align. Otherwise, do nothing to the second input curve before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
tangentContinuity(tc): boolean
    properties: create, query, edit
    Tangent continuity is on if true and off otherwise.
Default: true

---
tangentContinuityType(tct): int
    properties: create, query, edit
    Tangent continuity type legal values:
1 - do tangent continuity on first curve,
2 - do tangent continuity on second curve
Default: 1

---
tangentScale1(ts1): float
    properties: create, query, edit
    Tangent scale applied to tangent of first curve for tangent continuity.
Default: 1.0

---
tangentScale2(ts2): float
    properties: create, query, edit
    Tangent scale applied to tangent of second curve for tangent continuity.
Default: 1.0

---
attach(at): boolean
    properties: create
    True if the curve is to be attached

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
keepMultipleKnots(kmk): boolean
    properties: create
    True if multiple knots should be left as-is.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/alignCurve.html 
    """


def alignSurface(attach: boolean, caching: boolean, constructionHistory: boolean, curvatureContinuity: boolean, curvatureScale1: float, curvatureScale2: float, directionU: boolean, joinParameter: float, keepMultipleKnots: boolean, name: string, nodeState: int, object: boolean, positionalContinuity: boolean, positionalContinuityType: int, replaceOriginal: boolean, reverse1: boolean, reverse2: boolean, swap1: boolean, swap2: boolean, tangentContinuity: boolean, tangentContinuityType: int, tangentScale1: float, tangentScale2: float, twist: boolean) -> list[string]:
    """Synopsis:
---
---
 alignSurface(
[surface] [surface]
    , [attach=boolean], [caching=boolean], [constructionHistory=boolean], [curvatureContinuity=boolean], [curvatureScale1=float], [curvatureScale2=float], [directionU=boolean], [joinParameter=float], [keepMultipleKnots=boolean], [name=string], [nodeState=int], [object=boolean], [positionalContinuity=boolean], [positionalContinuityType=int], [replaceOriginal=boolean], [reverse1=boolean], [reverse2=boolean], [swap1=boolean], [swap2=boolean], [tangentContinuity=boolean], [tangentContinuityType=int], [tangentScale1=float], [tangentScale2=float], [twist=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

alignSurface is undoable, queryable, and editable.
NOTE: this tool is based on Studio's align tool.

Positional continuity means the surfaces (move) or the ends of the
surfaces (modify) are changed.

Tangent continuity means one of the surfaces is modified to be tangent
at the points where they meet.

Curvature continuity means one of the surfaces is modified to be
curvature continuous as well as tangent.

The default behaviour, when no surfaces or flags are passed, is to only
do positional and tangent continuity on the active list with the end
of the first surface and the start of the other surface used for
alignment.




Example:
---
import maya.cmds as cmds

Do modify positional continuity on both active surfaces with no history:
cmds.alignSurface( ch=False, pc=True, pct=6 )

Do positional and tangent continuity, with the second surface
tangent modified (by default move position continuity is done
on the first surface):
cmds.alignSurface( tc=True, tct=2 )

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
curvatureContinuity(cc): boolean
    properties: create, query, edit
    Curvature continuity is on if true and off otherwise.
Default: false

---
curvatureScale1(cs1): float
    properties: create, query, edit
    Curvature scale applied to curvature of first surface for curvature continuity.
Default: 0.0

---
curvatureScale2(cs2): float
    properties: create, query, edit
    Curvature scale applied to curvature of second surface for curvature continuity.
Default: 0.0

---
directionU(du): boolean
    properties: create, query, edit
    If true use U direction of surface and V direction otherwise.
Default: true

---
joinParameter(jnp): float
    properties: create, query, edit
    Parameter on reference surface where modified surface is to be aligned to.
Default: 123456.0

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
positionalContinuity(pc): boolean
    properties: create, query, edit
    Positional continuity is on if true and off otherwise.
Default: true

---
positionalContinuityType(pct): int
    properties: create, query, edit
    Positional continuity type legal values:
1 - move first surface,
2 - move second surface,
3 - move both surfaces,
4 - modify first surface,
5 - modify second surface,
6 - modify both surfaces
Default: 1

---
reverse1(rv1): boolean
    properties: create, query, edit
    If true, reverse the direction (specified by directionU) of the first input surface before doing align. Otherwise, do nothing to the first input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
reverse2(rv2): boolean
    properties: create, query, edit
    If true, reverse the direction (specified by directionU) of the second input surface before doing align. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
swap1(sw1): boolean
    properties: create, query, edit
    If true, swap the UV directions of the first input surface before doing align. Otherwise, do nothing to the first input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
swap2(sw2): boolean
    properties: create, query, edit
    If true, swap the UV directions of the second input surface before doing align. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
tangentContinuity(tc): boolean
    properties: create, query, edit
    Tangent continuity is on if true and off otherwise.
Default: true

---
tangentContinuityType(tct): int
    properties: create, query, edit
    Tangent continuity type legal values:
1 - do tangent continuity on first surface,
2 - do tangent continuity on second surface
Default: 1

---
tangentScale1(ts1): float
    properties: create, query, edit
    Tangent scale applied to tangent of first surface for tangent continuity.
Default: 1.0

---
tangentScale2(ts2): float
    properties: create, query, edit
    Tangent scale applied to tangent of second surface for tangent continuity.
Default: 1.0

---
twist(tw): boolean
    properties: create, query, edit
    If true, reverse the second surface in the opposite direction (specified by directionU) before doing align. This will avoid twists in the aligned surfaces. Otherwise, do nothing to the second input surface before aligning. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
attach(at): boolean
    properties: create
    Should surfaces be attached after alignment?

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
keepMultipleKnots(kmk): boolean
    properties: create
    Should multiple knots be kept?

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/alignSurface.html 
    """


def allNodeTypes(includeAbstract: boolean) -> list[string]:
    """Synopsis:
---
---
 allNodeTypes([includeAbstract=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

allNodeTypes is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


cmds.allNodeTypes()
Result: [u'list', u'of', u'node', u'types']  ---


cmds.allNodeTypes(includeAbstract=True)
Result: [u'very (abstract)', u'long (abstract)', u'list', u'of', u'all (abstract)', u'node', u'types']  ---


Trickier example using Python capabilities to get node types starting with 'l'
[item for item in cmds.allNodeTypes(includeAbstract=True) if item[0].lower() == 'l']
Result: [u'long (abstract)', u'list']  ---


---
Return:
---


    list[string]: List of node types

Flags:
---


---
includeAbstract(ia): boolean
    properties: create
    Show every node type, even the abstract ones which cannot be created
via the 'createNode' command. These will have the suffix "(abstract)" appended
to them in the list.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/allNodeTypes.html 
    """


def ambientLight(ambientShade: float, discRadius: linear, exclusive: boolean, intensity: float, name: string, position: tuple[linear, linear, linear], rgb: tuple[float, float, float], rotation: tuple[angle, angle, angle], shadowColor: tuple[float, float, float], shadowDither: float, shadowSamples: int, softShadow: boolean, useRayTraceShadows: boolean) -> double[] | string:
    """Synopsis:
---
---
 ambientLight([ambientShade=float], [discRadius=linear], [exclusive=boolean], [intensity=float], [name=string], [position=[linear, linear, linear]], [rgb=[float, float, float]], [rotation=[angle, angle, angle]], [shadowColor=[float, float, float]], [shadowDither=float], [shadowSamples=int], [softShadow=boolean], [useRayTraceShadows=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

ambientLight is undoable, queryable, and editable.
This is the commmand that instantiates an ambientLight
or edits the parameters of an existing one.
TambientLightCmd inherits from TlightCmd which defines
common flags like intensity, colour etc.
See TlightCmd for a global picture of the light commands.
Note that the flag fAmbientLightUsed indicates whether
the command uses any ambient specific flags.
That is, if a command doesn't use flags
defined here, the boolean fAmbientLightUsed is set to
false and thus the undo/redo information is not saved
at this level.

TambientLightCmd behaves like any other command, it
has flags, saves undo information etc. the only slightly
different behaviour is that it calls up to TlightCmd to
complete the functionality of the command.
Example	parseArgs:  TambientLightCmd defines
ambientLight specific parameters like -ambientShade
however, several other parameters are available in
TlightCmd such as -intensity etc.  So when parsing
the arguments, a call is made to TlightCmd::parseArgs
to parse common parameters (like Intensity).




Example:
---
import maya.cmds as cmds

Create an ambientLight light
light = cmds.ambientLight(intensity=0.8)

Change the light intensity
cmds.ambientLight( light, e=True, intensity=0.5 )

Query it
cmds.ambientLight( light, q=True, intensity=True )
Result:0.5 ---


---
Return:
---


    double[]: when querying the rgb or shadowColor flags
double when querying the intensity flag
boolean when querying the useRayTraceShadows or exclusive flags
linear[] when querying the position flag
angle[] when querying the rotation flag
string when querying the name flag
    string: Light shape name

Flags:
---


---
ambientShade(ambientShade): float
    properties: create, query, edit
    ambientShade

---
discRadius(drs): linear
    properties: create, query, edit
    radius of the disc around the light

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
    properties: create, query, edit
    dither the shadow

---
shadowSamples(sh): int
    properties: create, query, edit
    number of shadow samples.

---
softShadow(ss): boolean
    properties: create, query, edit
    soft shadow

---
useRayTraceShadows(rs): boolean
    properties: create, query
    True if ray trace shadows are to be used

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/ambientLight.html 
    """


def angleBetween(caching: boolean, constructionHistory: boolean, euler: boolean, nodeState: int, vector1: tuple[linear, linear, linear], vector1X: linear, vector1Y: linear, vector1Z: linear, vector2: tuple[linear, linear, linear], vector2X: linear, vector2Y: linear, vector2Z: linear) -> float[] | string:
    """Synopsis:
---
---
 angleBetween([caching=boolean], [constructionHistory=boolean], [euler=boolean], [nodeState=int], [vector1=[linear, linear, linear]], [vector1X=linear], [vector1Y=linear], [vector1Z=linear], [vector2=[linear, linear, linear]], [vector2X=linear], [vector2Y=linear], [vector2Z=linear])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

angleBetween is undoable, NOT queryable, and NOT editable.ch



Example:
---
import maya.cmds as cmds

To find the euler angle between these two vectors. The result is three
angles in the current angular unit. In this example, the first vector
must be rotated -63.434949 degrees about the X axis, 16.60155 degrees
about the Y axis and -26.565051 degrees about the Z axis to achieve
the second vector.

cmds.angleBetween( euler=True, v1=(0.0, 1.0, 2.0), v2=(1.0, 2.0, 0.0) )
Result: -63.434949 16.60155 -26.565051 ---


To find the angle between these two vectors.  The result is an axis and
an angle (in the current angular unit).  In this example, the first
vector must be rotated 66.421822 degrees about the axis
(-0.8728716, 0.4364358, -0.2182179) to achieve the second vector.

cmds.angleBetween( v1=(0.0, 1.0, 2.0), v2=(1.0, 2.0, 0.0) )
Result: -0.8728716 0.4364358 -0.2182179 66.421822 ---


How to create a dependency node that calculates the angle between two
vectors. This example shows how the (x,z) position of a sphere
can be used to control the rotate factors (about y) of a cone shape.

angleBtwnNode = cmds.angleBetween(v1=(1, 0, 0), v2=(1, 0, 0), ch=True)
sphere = cmds.sphere()
cmds.move( 5, 0, 5, sphere[0] )
cmds.connectAttr( sphere[0]+'.translateX', angleBtwnNode+'.vector2X' )
cmds.connectAttr( sphere[0]+'.translateZ', angleBtwnNode+'.vector2Z' )

cone = cmds.cone( ch=False )
convert = cmds.createNode( 'unitConversion' )
cmds.connectAttr( angleBtwnNode+'.eulerY', convert+'.input' )
cmds.connectAttr( convert+'.output', cone[0]+'.rotateY' )

---
Return:
---


    float[]: 3 Euler angles or axis and angle
    string: When constructionHistory flag is used.

Flags:
---


---
caching(cch): boolean
    properties: create
    Toggle caching for all attributes so that no recomputation is needed

---
constructionHistory(ch): boolean
    properties: create
    Turn the construction history on or off.

---
euler(er): boolean
    properties: create
    return the rotation as 3 Euler angles instead of axis + angle

---
nodeState(nds): int
    properties: create
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
vector1(v1): [linear, linear, linear]
    properties: create
    vector from which to compute the rotation

---
vector1X(v1x): linear
    properties: create
    X coordinate of the vector from which to compute the rotation

---
vector1Y(v1y): linear
    properties: create
    Y coordinate of the vector from which to compute the rotation

---
vector1Z(v1z): linear
    properties: create
    Z coordinate of the vector from which to compute the rotation

---
vector2(v2): [linear, linear, linear]
    properties: create
    vector to which to compute the rotation

---
vector2X(v2x): linear
    properties: create
    X coordinate of the vector to which to compute the rotation

---
vector2Y(v2y): linear
    properties: create
    Y coordinate of the vector to which to compute the rotation

---
vector2Z(v2z): linear
    properties: create
    Z coordinate of the vector to which to compute the rotation

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/angleBetween.html 
    """


def animCurveEditor(areCurvesSelected: boolean, autoFit: string, autoFitTime: string, classicMode: boolean, clipTime: string, constrainDrag: uint, control: boolean, curvesShown: boolean, curvesShownForceUpdate: boolean, defineTemplate: string, denormalizeCurvesCommand: string, displayActiveKeyTangents: string, displayActiveKeys: string, displayInfinities: string, displayKeys: string, displayNormalized: boolean, displayTangents: string, displayValues: string, docTag: string, exists: boolean, filter: string, forceMainConnection: string, highlightAffectedCurves: boolean, highlightConnection: string, keyMinScale: float, keyScale: float, keyingTime: string, limitToSelectedCurves: boolean, lockMainConnection: boolean, lockPlayRangeShades: string, lookAt: string, mainListConnection: string, menu: script, normalizeCurvesCommand: string, outliner: string, panel: string, parent: string, preSelectionHighlight: boolean, renormalizeCurves: boolean, resultSamples: time, resultScreenSamples: int, resultUpdate: string, selectionConnection: string, showActiveCurveNames: boolean, showBufferCurves: string, showCurveNames: boolean, showPlayRangeShades: string, showResults: string, showUpstreamCurves: boolean, simpleKeyView: boolean, smoothness: string, snapTime: string, snapValue: string, stackedCurves: boolean, stackedCurvesMax: float, stackedCurvesMin: float, stackedCurvesSpace: float, stateString: boolean, timelinePositionTop: boolean, unParent: boolean, unlockMainConnection: boolean, updateMainConnection: boolean, useTemplate: string, valueLinesToggle: string) -> string:
    """Synopsis:
---
---
 animCurveEditor(
editorName
    , [areCurvesSelected=boolean], [autoFit=string], [autoFitTime=string], [classicMode=boolean], [clipTime=string], [constrainDrag=uint], [control=boolean], [curvesShown=boolean], [curvesShownForceUpdate=boolean], [defineTemplate=string], [denormalizeCurvesCommand=string], [displayActiveKeyTangents=string], [displayActiveKeys=string], [displayInfinities=string], [displayKeys=string], [displayNormalized=boolean], [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean], [filter=string], [forceMainConnection=string], [highlightAffectedCurves=boolean], [highlightConnection=string], [keyMinScale=float], [keyScale=float], [keyingTime=string], [limitToSelectedCurves=boolean], [lockMainConnection=boolean], [lockPlayRangeShades=string], [lookAt=string], [mainListConnection=string], [menu=script], [normalizeCurvesCommand=string], [outliner=string], [panel=string], [parent=string], [preSelectionHighlight=boolean], [renormalizeCurves=boolean], [resultSamples=time], [resultScreenSamples=int], [resultUpdate=string], [selectionConnection=string], [showActiveCurveNames=boolean], [showBufferCurves=string], [showCurveNames=boolean], [showPlayRangeShades=string], [showResults=string], [showUpstreamCurves=boolean], [simpleKeyView=boolean], [smoothness=string], [snapTime=string], [snapValue=string], [stackedCurves=boolean], [stackedCurvesMax=float], [stackedCurvesMin=float], [stackedCurvesSpace=float], [stateString=boolean], [timelinePositionTop=boolean], [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string], [valueLinesToggle=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

animCurveEditor is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Check to see if the "default" graph editor has been created
---

cmds.animCurveEditor( 'graphEditor1GraphEd', exists=True )
Show result curves
---

cmds.animCurveEditor( 'graphEditor1GraphEd', edit=True, showResults='on' )
Show Play Range Shades
---

cmds.animCurveEditor( 'graphEditor1GraphEd', edit=True, showPlayRangeShades='on' )
Lock Play Range Shades
---

cmds.animCurveEditor( 'graphEditor1GraphEd', edit=True, lockPlayRangeShades='on' )
Decrease the sampling rate for the result curves
---

cmds.animCurveEditor( 'graphEditor1GraphEd', edit=True, resultSamples=5 )

Constrain all Graph Editor animation curve traversals to the X-axis
---

cmds.animCurveEditor( 'graphEditor1GraphEd', edit=True, constrainDrag=1 )

---
Return:
---


    string: Editor name

Flags:
---


---
areCurvesSelected(acs): boolean
    properties: query
    Returns a boolean to know if at least one curve is selected in the graph editor.

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
classicMode(cm): boolean
    properties: query, edit
    When on, the graph editor is displayed in "Classic Mode", otherwise "Suites Mode" is used.

---
clipTime(ct): string
    properties: query, edit
    Valid values: "on" "off"
Display the clips with their offset and scale
applied to the anim curves in the clip.

---
constrainDrag(cd): uint
    properties: create, query, edit
    Constrains all Graph Editor animation curve drag operations
to either the X-axis, the Y-axis, or to neither of those axes.
Values to supply are: 0 for not constraining any axis,
1 for constraing the X-axis, or 2 for constraining the Y-axis.
When used in queries, this flag returns the latter values and
these values have the same interpretation as above.
Note: when the shift key is pressed before dragging the animation
curve, the first mouse movement will instead determine (and override)
any prior set constrained axis.

---
control(ctl): boolean
    properties: query
    Query only. Returns the top level control for this editor.
Usually used for getting a parent to attach popup menus.
Caution: It is possible for an editor to exist without a
control. The query will return "NONE" if no control is present.

---
curvesShown(cs): boolean
    properties: query
    Returns a string array containing the names of the animCurve nodes
currently displayed in the graph editor.

---
curvesShownForceUpdate(csf): boolean
    properties: query
    Returns a string array containing the names of the animCurve nodes
currently displayed in the graph editor. Unlike the curvesShown flag,
this will force an update of the graph editor for the case where
the mainListConnection has been modified since the last refresh.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
denormalizeCurvesCommand(dcc): string
    properties: create, edit
    Sets the script that is run to denormalize curves in the graph editor.
This is intended for internal use only.

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
displayNormalized(dn): boolean
    properties: query, edit
    When on, display all curves normalized to the range -1 to +1.

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
highlightAffectedCurves(hac): boolean
    properties: query, edit
    When on, highlights the curve segment affected by the selected key/tangent

---
highlightConnection(hlc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that
the editor will synchronize with its highlight list. Not all
editors have a highlight list. For those that do, it is a secondary
selection list.

---
keyMinScale(kms): float
    properties: query, edit
    The minimum key selection size in the graph editor.
A value of 0.0 means there is no minimum size.
A value of 1.0 means the minimum size is the size of a key with keyScale set to 1.0

---
keyScale(ksc): float
    properties: query, edit
    Scales the key size in the graph editor

---
keyingTime(kt): string
    properties: query
    The current time in the given curve to be keyed in the graph editor.

---
limitToSelectedCurves(lsc) 2024: boolean
    properties: query, edit
    When on, marquee selection refines the current selection and only
affects curves with active keys or tangents.  When off (or when
there are no curves, keys, or tangents selected), performs a
normal marquee selection and replaces the current selection with
everything that is selectable inside the marquee.

---
lockMainConnection(lck): boolean
    properties: create, edit
    Locks the current list of objects within the mainConnection,
so that only those objects are displayed within the editor.
Further changes to the original mainConnection are ignored.

---
lockPlayRangeShades(lpr): string
    properties: query, edit
    Valid values: "on" "off" "tgl"
Lock Play Range Shades.

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
menu(m): script
    properties: create
    Specify a script to be run when the editor
is created.  The function will be passed one string
argument which is the new editor's name.

---
normalizeCurvesCommand(ncc): string
    properties: create, edit
    Sets the script that is run to normalize curves in the graph editor.
This is intended for internal use only.

---
outliner(o): string
    properties: query, edit
    The name of the outliner that is associated with the graph editor.

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
preSelectionHighlight(psh): boolean
    properties: query, edit
    When on, the curve/key/tangent under the mouse pointer is highlighted
to ease selection.

---
renormalizeCurves(rnc): boolean
    properties: edit
    This flag causes the curve normalization factors to be recalculated.

---
resultSamples(rs): time
    properties: query, edit
    Specify the sampling for result curves
Note: the smaller this number is, the longer it will
take to update the display.

---
resultScreenSamples(rss): int
    properties: query, edit
    Specify the screen base result sampling for result curves.
If 0, then results are sampled in time.

---
resultUpdate(ru): string
    properties: query, edit
    Valid values: "interactive" "delayed"
Controls how changes to animCurves are reflected in the
result curves (if results are being shown).  If resultUpdate
is "interactive", then as interactive changes are being made
to the animCurve, the result curves will be updated.  If
modelUpdate is delayed (which is the default setting), then
result curves are updated once the final change to an
animCurve has been made.

---
selectionConnection(slc): string
    properties: create, query, edit
    Specifies the name of a selectionConnection object that the
editor will synchronize with its own selection list. As the user
selects things in this editor, they will be selected in the
selectionConnection object. If the object undergoes changes, the
editor updates to show the changes.

---
showActiveCurveNames(acn): boolean
    properties: query, edit
    Display the active curve(s)'s name.

---
showBufferCurves(sb): string
    properties: query, edit
    Valid values: "on" "off" "tgl"
Display buffer curves.

---
showCurveNames(scn): boolean
    properties: query, edit
    Display the curves's name.

---
showPlayRangeShades(spr): string
    properties: query, edit
    Valid values: "on" "off" "tgl"
Display Play Range Shades.

---
showResults(sr): string
    properties: query, edit
    Valid values: "on" "off" "tgl"
Display result curves from expression or other non-keyed
action.

---
showUpstreamCurves(suc): boolean
    properties: query, edit
    If true, the dependency graph is searched upstream for all curves
that drive the selected plugs (showing multiple curves for example
in a typical driven key setup, where first the driven key curve is
encountered, followed by the actual animation curve that drives the
source object). If false, only the first curves encountered
will be shown. Note that, even if false, multiple curves can be shown
if e.g. a blendWeighted node is being used to combine multiple curves.

---
simpleKeyView(skv): boolean
    properties: query, edit
    on | off
Display simpler and smaller key.

---
smoothness(s): string
    properties: query, edit
    Valid values: "coarse" "rough" "medium" "fine"
Specify the display smoothness of animation curves.

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
stackedCurves(sc): boolean
    properties: query, edit
    Switches the display mode between normal (all curves sharing one set of axes)
to stacked (each curve on its own value axis, stacked vertically).

---
stackedCurvesMax(scx): float
    properties: query, edit
    Sets the maximum value on the per-curve value axis when in stacked mode.

---
stackedCurvesMin(scm): float
    properties: query, edit
    Sets the minimum value on the per-curve value axis when in stacked mode.

---
stackedCurvesSpace(scs): float
    properties: query, edit
    Sets the spacing between curves when in stacked mode.

---
stateString(sts): boolean
    properties: query
    Query only flag. Returns the MEL command that will create an
editor to match the current editor state. The returned command string
uses the string variable $editorName in place of a specific name.

---
timelinePositionTop(tlp): boolean
    properties: query, edit
    on | off | tgl
Display timeline either at the top or bottom.

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
valueLinesToggle(vlt): string
    properties: edit
    on | off | tgl
Display the value lines for high/low/zero of selected curves in the editor

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/animCurveEditor.html 
    """


def animDisplay(modelUpdate: string, refAnimCurvesEditable: boolean, timeCode: string, timeCodeOffset: string) -> None:
    """Synopsis:
---
---
 animDisplay([modelUpdate=string], [refAnimCurvesEditable=boolean], [timeCode=string], [timeCodeOffset=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

animDisplay is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

If the current time unit were ntsc (30 frames per
second) frame 50 would be displayed as "00:00:01:20".
---

cmds.animDisplay( timeCode=True )


Set the display option so that interactive operations
in the graph editor or dope sheet will cause the
model views to be updated simultaneously
---

cmds.animDisplay( modelUpdate="interactive" )

---


Flags:
---


---
modelUpdate(upd): string
    properties: create, query, edit
    Controls how changes to animCurves are propagated through the
dependency graph. Valid modes are "none", "interactive" or
"delayed". If modelUpdate is "none" then changing an
animCurve will not cause the model to be updated (change currentTime
in order to update the model).  If modelUpdate is "interactive" (which
is the default setting), then as interactive changes are being made
to the animCurve, the model will be updated.  If modelUpdate is
delayed, then the model is updated once the final change to an
animCurve has been made.  With modelUpdate set to
either "interactive" or "delayed", changes
to animCurves made via commands will also cause the
model to be updated.

---
refAnimCurvesEditable(rae): boolean
    properties: create, query, edit
    Specify if animation curves from referenced files are
editable.

---
timeCode(tc): string
    properties: create, query, edit
    Controls how time value are display. Valid values are "frame", "timecode", "fulltimecode".
If the value is "frame" maya will display time in frame everywhere.
If the value is "timecode" maya will display time in timecode in time
slider, graph editor and dope sheet.
If the value is "fulltimecode" maya will display time in timecode everywhere.

---
timeCodeOffset(tco): string
    properties: create, query, edit
    This flag has now been deprecated.  It still exists to not break
legacy scripts, but it will now do nothing.  See the new timeCode
command to set and query timeCodes.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/animDisplay.html 
    """


def animLayer(addRelatedKG: boolean, addSelectedObjects: boolean, affectedLayers: boolean, animCurves: boolean, attribute: string, baseAnimCurves: boolean, bestAnimLayer: boolean, bestLayer: boolean, blendNodes: boolean, children: string, collapse: boolean, copy: string, copyAnimation: string, copyNoAnimation: string, excludeBoolean: boolean, excludeDynamic: boolean, excludeEnum: boolean, excludeProxy: boolean, excludeRotate: boolean, excludeScale: boolean, excludeTranslate: boolean, excludeVisibility: boolean, exists: boolean, extractAnimation: string, findCurveForPlug: string, forceUIRebuild: boolean, forceUIRefresh: boolean, layeredPlug: string, lock: boolean, maxLayers: boolean, moveLayerAfter: string, moveLayerBefore: string, mute: boolean, override: boolean, parent: string, passthrough: boolean, preferred: boolean, removeAllAttributes: boolean, removeAttribute: string, removeSelectedObjects: boolean, root: string, selected: boolean, solo: boolean, weight: float, writeBlendnodeDestinations: boolean) -> string:
    """Synopsis:
---
---
 animLayer([addRelatedKG=boolean], [addSelectedObjects=boolean], [affectedLayers=boolean], [animCurves=boolean], [attribute=string], [baseAnimCurves=boolean], [bestAnimLayer=boolean], [bestLayer=boolean], [blendNodes=boolean], [children=string], [collapse=boolean], [copy=string], [copyAnimation=string], [copyNoAnimation=string], [excludeBoolean=boolean], [excludeDynamic=boolean], [excludeEnum=boolean], [excludeProxy=boolean], [excludeRotate=boolean], [excludeScale=boolean], [excludeTranslate=boolean], [excludeVisibility=boolean], [exists=boolean], [extractAnimation=string], [findCurveForPlug=string], [forceUIRebuild=boolean], [forceUIRefresh=boolean], [layeredPlug=string], [lock=boolean], [maxLayers=boolean], [moveLayerAfter=string], [moveLayerBefore=string], [mute=boolean], [override=boolean], [parent=string], [passthrough=boolean], [preferred=boolean], [removeAllAttributes=boolean], [removeAttribute=string], [removeSelectedObjects=boolean], [root=string], [selected=boolean], [solo=boolean], [weight=float], [writeBlendnodeDestinations=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

animLayer is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


cmds.animLayer("layer1", mute=True, solo=True, override=True, passthrough=False, lock=True)

cmds.animLayer("layer1", query=True, mute=True)
Result: 1 ---


cmds.animLayer("layer1", query=True, solo=True)
Result: 1 ---


cmds.animLayer("layer1", query=True, override=True)
Result: 1 ---


cmds.animLayer("layer1", query=True, passthrough=True)
Result: 0 ---


cmds.animLayer("layer1", query=True, lock=True)
Result: 1 ---


cmds.animLayer("layer1", query=True, parent=True)
Result: BaseAnimation ---


---
Return:
---


    string: Return values currently not documented.

Flags:
---


---
addRelatedKG(akg): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, adds associated keying group(s)
to the object(s).

---
addSelectedObjects(aso): boolean
    properties: create, query, edit
    Adds selected object(s) to the layer.

---
affectedLayers(afl): boolean
    properties: query
    Return the layers that the currently selected object(s) are members of

---
animCurves(anc): boolean
    properties: create, query, edit
    In query mode returns the anim curves associated with this layer

---
attribute(at): string
    properties: create, query, edit, multiuse
    Adds a specific attribute on a object to the layer.

---
baseAnimCurves(bac): boolean
    properties: create, query, edit
    In query mode returns the base layer anim curves associated with this layer, if any.

---
bestAnimLayer(blr): boolean
    properties: create, query, edit
    In query mode returns the best anim layers for keying for the selected
objects. If used in conjunction with -at, will return the best anim layers
for keying for the specific plugs (attributes) specified.

---
bestLayer(bl): boolean
    properties: query
    Return the layer that will be keyed for specified attribute.

---
blendNodes(bld): boolean
    properties: create, query, edit
    In query mode returns the blend nodes associated with this layer

---
children(c): string
    properties: query
    Get the list of children layers. Return value is a string array.

---
collapse(col): boolean
    properties: create, query, edit
    Determine if a layer is collapse in the layer editor.

---
copy(cp): string
    properties: edit
    Copy from the layer.

---
copyAnimation(ca): string
    properties: create, edit
    Copy animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.

---
copyNoAnimation(cna): string
    properties: edit
    Copy from layer without the animation curves.

---
excludeBoolean(ebl): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes any boolean attributes.

---
excludeDynamic(edn): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes any dynamic attributes.

---
excludeEnum(een): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes any enum attributes.

---
excludeProxy(epr): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes any proxy attributes.

---
excludeRotate(ert): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes the rotate attribute.

---
excludeScale(esc): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes the scale attribute.

---
excludeTranslate(etr): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes the translate attribute.

---
excludeVisibility(evs): boolean
    properties: create, query, edit
    When adding or removing selected object(s) from the layer, excludes the visibility attribute.

---
exists(ex): boolean
    properties: query
    Determine if a layer exists.

---
extractAnimation(ea): string
    properties: create, edit
    Transfer animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.

---
findCurveForPlug(fcv): string
    properties: query, edit
    Finds the parameter curve containing the animation data for the specified plug on the given layer.
                        In query mode, this flag needs a value.

---
forceUIRebuild(fur): boolean
    properties: create
    Rebuilds the animation layers user interface.

---
forceUIRefresh(uir): boolean
    properties: create
    Refreshes the animation layers user interface.

---
layeredPlug(lp): string
    properties: query
    Returns the plug on the blend node corresponding to the specified layer
                        In query mode, this flag needs a value.

---
lock(l): boolean
    properties: create, query, edit
    Set the lock state of the specified layer. A locked layer cannot receive key. Default is false.

---
maxLayers(ml): boolean
    properties: query
    Returns the maximum number of anim layers supported by this product.

---
moveLayerAfter(mva): string
    properties: edit
    Move layer after the specified layer

---
moveLayerBefore(mvb): string
    properties: edit
    Move layer before the specified layer

---
mute(m): boolean
    properties: create, query, edit
    Set the mute state of the specified layer. Default is false.

---
override(o): boolean
    properties: create, query, edit
    Set the overide state of the specified layer. Default is false.

---
parent(p): string
    properties: create, query, edit
    Set the parent of the specified layer. Default is the animation layer root.

---
passthrough(pth): boolean
    properties: create, query, edit
    Set the passthrough state of the specified layer. Default is true.

---
preferred(prf): boolean
    properties: create, query, edit
    Determine if a layer is a preferred layer, the best layer algorithm will try to set keyframe in preferred layer first.

---
removeAllAttributes(raa): boolean
    properties: edit
    Remove all objects from the layer.

---
removeAttribute(ra): string
    properties: edit, multiuse
    Remove object from the layer.

---
removeSelectedObjects(rso) 2024: boolean
    properties: edit
    Removes selected object(s) from the layer.

---
root(r): string
    properties: query
    Return the base layer if it exist

---
selected(sel): boolean
    properties: create, query, edit
    Determine if a layer is selected, a selected layer will be show in the timecontrol, graph editor.

---
solo(s): boolean
    properties: create, query, edit
    Set the solo state of the specified layer. Default is false.

---
weight(w): float
    properties: create, query, edit
    Set the weight of the specified layer between 0.0 and 1.0. Default is 1.

---
writeBlendnodeDestinations(wbd): boolean
    properties: edit
    In edit mode writes the destination plugs of the blend nodes that belong to the layer
into the blend node. This is used for layer import/export purposes and is not for
general use.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/animLayer.html 
    """


def animView(endTime: time, maxValue: float, minValue: float, nextView: boolean, previousView: boolean, startTime: time) -> None:
    """Synopsis:
---
---
 animView(
string[]
    , [endTime=time], [maxValue=float], [minValue=float], [nextView=boolean], [previousView=boolean], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

animView is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Look at the area between 0 and 5 seconds, and the range 0 - 100
cmds.animView( 'graphView', startTime='0sec', endTime='5sec', minValue=0, maxValue=100 )

---


Flags:
---


---
endTime(et): time
    properties: 
    End time to display within the editor

---
maxValue(max): float
    properties: 
    Upper value to display within the editor

---
minValue(min): float
    properties: 
    Lower value to display within the editor

---
nextView(nv): boolean
    properties: edit
    Switches to the next view.

---
previousView(pv): boolean
    properties: edit
    Switches to the previous view.

---
startTime(st): time
    properties: 
    Start time to display within the editor

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/animView.html 
    """


def annotate(point: tuple[linear, linear, linear], text: string) -> string:
    """Synopsis:
---
---
 annotate(
[objects]
    , [point=[linear, linear, linear]], [text=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

annotate is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

The following specifies an annotation with text "my annotation text" on
object mySphere, with the text being centered at point [5,6,3].
cmds.sphere( name='mySphere' )
cmds.annotate( 'mySphere', tx='my annotation text', p=(5, 6, 5) )

---
Return:
---


    string: Annotation added

Flags:
---


---
point(p): [linear, linear, linear]
    properties: create
    Specifies the point about which the annotation text is to be
centered.

---
text(tx): string
    properties: create
    Specifies the annotation text.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/annotate.html 
    """


def appHome(iconVisible: boolean, instrument: string, setTab: string, toggleVisibility: boolean, updateRecentFiles: boolean, visible: boolean) -> None:
    """Synopsis:
---
---
 appHome([iconVisible=boolean], [instrument=string], [setTab=string], [toggleVisibility=boolean], [updateRecentFiles=boolean], [visible=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

appHome is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Hide app home
cmds.appHome(edit=True, visibility=False)

Show app home
cmds.appHome(edit=True, visibility=True)

Show app home on GettingStarted tab
cmds.appHome(visibility=True, setTab='GettingStarted')

Update app home recent file data
cmds.appHome(updateRecentFiles=True)

Query app home visilibity
visible = cmds.appHome(query=True, visibility=True)

Toggle app home visibility
cmds.appHome(edit=True, toggleVisibility=True)

---


Flags:
---


---
iconVisible(iv): boolean
    properties: create, query, edit
    Query or set application home icon visibility preference.

Note: Icon visibility cannot be modified if the MAYA_NO_HOME_ICON
environment variable is defined.

---
instrument(i): string
    properties: create
    Instrument the app home command with the given string.

---
setTab(t): string
    properties: create, edit
    Navigate app home to the specified tab.

Available tabs are:
Recent
GettingStarted
Learning
WhatsNew
Community

---
toggleVisibility(tv): boolean
    properties: create, edit
    Toggle application home widget visibility.

---
updateRecentFiles(urf): boolean
    properties: create, edit
    Update the recent file list data.

---
visible(v): boolean
    properties: create, query, edit
    Query or set application home widget visibility.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/appHome.html 
    """


def applyAttrPattern(nodeType: string, patternName: string) -> int:
    """Synopsis:
---
---
 applyAttrPattern([nodeType=string], [patternName=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

applyAttrPattern is undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds

cmds.polySphere( name="sphere1" )
cmds.applyAttrPattern( patternName="myXMLPattern" )
// Result: 1 //

name2 = cmds.polySphere( name="sphere2" )
name3 = cmds.polySphere( name="sphere3" )
cmds.select( [name2, name3] )
cmds.applyAttrPattern( patternName="myXMLPattern" )
// Result: 2 //

cmds.applyAttrPattern( patternName="myXMLPattern", nodeType="transform" )
// Result: 1 //

---
Return:
---


    int: Number of nodes or node types to which the attribute were added

Flags:
---


---
nodeType(nt): string
    properties: create
    Name of the node type to which the attribute pattern is to be applied. This flag
will cause a new extension attribute tree to be created, making the new attributes
available on all nodes of the given type. If it is not specified then either a node
name must be specified or a node must be selected for application of dynamic
attributes.

---
patternName(pn): string
    properties: create
    The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/applyAttrPattern.html 
    """


def applyMetadata(format: string, scene: boolean, value: string) -> Boolean:
    """Synopsis:
---
---
 applyMetadata([format=string], [scene=boolean], [value=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

applyMetadata is undoable, NOT queryable, and NOT editable.
Define the values of a particular set of metadata on selected objects.
This command is used in preservation of metadata through Maya file formats
(.ma/.mb). If any metadata already exists it will be kept and merged with
the new metadata, overwriting duplicate entries. (i.e. if this command
specifies data at index N and you already have a value at index N then
the one this command specifies will be the new value and the old one
will cease to exist.)


Unlike the editMetadata command it is not necessary to first use
the addMetadata command or API equivalent to attach a metadata
stream to the object, this command will do both assignment of structure
and of metadata values. You do have to use the dataStructure
command or API equivalent to create the structure being assigned first
though.


The formatted input will be in a form expected by the data
associations serializer (see adsk::Data::AssociationsSerializer for
more information). The specific serialization type will be the default
'raw' if the format flag is not used.


For example the "raw" format input string
"channel face\n[STREAMDATA]\nendChannels\nendAssociations"
with no flags is equivalent to the input "[STREAMDATA]\nendChannels" with
the channel flag set to 'face'




Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
pNode = cmds.polyPlane( name='p' )
Create a sample structure
cmds.dataStructure( format='raw', asString='name=IdStruct:int32=ID' )
Apply some metadata based on the defined structure to the created mesh
Normally you'll only see these in Maya files but it can be used from the
command line.
cmds.applyMetadata( pNode, value='channel\nname face\nstream\nname IdStream\nstructure IdStruct\n0\n99\n1\n999\n2\n9999\nendStream\nendChannel\nendAssociations' )
Return: 1 ---


---
Return:
---


    Boolean: True if the application succeeded

Flags:
---


---
format(fmt): string
    properties: create
    Name of the data association format type to use in the value flag parsing.
Default value is "raw".

---
scene(scn): boolean
    properties: create
    Use this flag when you want to apply metadata to the scene as a whole
rather than to any individual nodes. If you use this flag and have
nodes selected the nodes will be ignored and a warning will be displayed.
Scene metadata is incompatible with referenced scenes. Node associated
metadata from referenced files will still be readable from master scenes
but scene specific metadata of referenced files will not be accessible
from a any master scene. This will ensure that referenced files metadata
will not end up corrupting the master file scene-metadata.

---
value(v): string
    properties: create
    String containing all of the metadata to be assigned to the selected
object.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/applyMetadata.html 
    """


def applyTake(channel: string, device: string, filter: string, preview: boolean, recurseChannel: boolean, reset: boolean, specifyChannel: boolean, startTime: time) -> None:
    """Synopsis:
---
---
 applyTake([channel=string], [device=string], [filter=string], [preview=boolean], [recurseChannel=boolean], [reset=boolean], [specifyChannel=boolean], [startTime=time])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

applyTake is undoable, NOT queryable, and NOT editable.
The command looks for animation curves attached to the target attributes
of a device attachment. If animation curves exist, the take is
pasted over the existing curves. If the curves do not exist, new
animation curves are created.

If devices are not specified, all of the devices with take data and that
are enabled for applyTake, will have their data applied.

See also: recordDevice, enableDevice, readTake, writeTake




Example:
---
import maya.cmds as cmds

   Apply all of the recorded data to param curves.
cmds.applyTake()

   Applies the takes from clock and ultra devices and starts the
   data at anim time 100.
cmds.applyTake( d=('clock', 'ultra'), st=100 )

   Applies the take from the ultra device and uses the euler and
   simplify filters.
cmds.applyTake( d='ultra', f=('euler', 'simplify') )

   Applies only the shoulder channel and all of its children.
cmds.applyTake( d='ultra', c='shoulder', sc=True, rc=True )

---


Flags:
---


---
channel(c): string
    properties: create, multiuse
    This flag overrides the set channel enable value.
If a channel is specified, it will be enabled. 
C: The default is all applyTake enabled channels for the device(s).

---
device(d): string
    properties: create, multiuse
    Specifies which device contains the take. 
C: The default is all applyTake enabled devices.

---
filter(f): string
    properties: create, multiuse
    This flag specifies the filters to use during the
applyTake. If this flag is used multiple times, the ordering
of the filters is from left to right. 
C: The default is no filters.

---
preview(p): boolean
    properties: create
    Applies the take to blendDevice nodes attached to the target
attributes connected to the device attachments. Animation curves
attached to the attributes will not be altered, but for the time
that preview data is defined, the preview data will be the data
used during playback. 
C: The default is to not preview.

---
recurseChannel(rc): boolean
    properties: create
    When this flag is used, the children of the channel(s)
specified by -c/channel are also applied.
C: The default is all of the enabled channels.

---
reset(r): boolean
    properties: create
    Resets the blendDevice nodes affected by -preview. The preview data
is removed and if animation curves exist, they are used during
playback.

---
specifyChannel(sc): boolean
    properties: create
    This flag is used with -c/channel flag. When used, applyTake
will only work on the channels listed with the -c/channel flag. 
C: The default is all of the enabled channels.

---
startTime(st): time
    properties: create
    The default start time for a take is determined at record time.
The startTime option sets the starting time of the take in the
current animation units. 
C: The default is the first time stamp of the take. If a time
stamp does not exist for the take, 0 is used.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/applyTake.html 
    """


def arcLenDimContext(exists: boolean, history: boolean, image1: string, image2: string, image3: string, name: string) -> string:
    """Synopsis:
---
---
 arcLenDimContext([exists=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

arcLenDimContext is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.arcLenDimContext()

---
Return:
---


    string: : name of the context created

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/arcLenDimContext.html 
    """


def arcLengthDimension() -> string:
    """Synopsis:
---
---
 arcLengthDimension(
[curve|surface]
    )  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

arcLengthDimension is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

Measure the arcLength of curve curveShape1 at u = 0.5
cmds.curve( d=3, p=((-9.3, 0, 3.2), (-4.2, 0, 5.0), (6.0, 0, 8.6), (2.1, 0, -1.9)), k=(0, 0, 0, 1, 2, 2));
cmds.arcLengthDimension( 'curveShape1.u[0.5]' )

Measure the arcLength of sphere nurbsSphere1 at u = 0.5 and v = 0.5
cmds.sphere();
cmds.arcLengthDimension( 'nurbsSphere1.uv[0.5][0.5]' );

---
Return:
---


    string: Name of the arcLengthDimension node created

Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/arcLengthDimension.html 
    """


def arclen(caching: boolean, constructionHistory: boolean, nodeState: int) -> float | string:
    """Synopsis:
---
---
 arclen(
curve
    , [caching=boolean], [constructionHistory=boolean], [nodeState=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

arclen is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

cmds.arclen( 'curve1' )
This command returns a float value that is the length of curve1 in
the current linear units.

curveInfoNode = cmds.arclen('curve1', ch=True)
cmds.expression( s= 'surface1.sx = %s.arcLength' %  curveInfoNode )
The first command produces a curve info node for curve1 and returns
the name of the curve info node.  The second command shows how the
arc length attribute of the curve info node can be used to set up
an expression, ie. it drives one of the scale factors of surface1.
---

Note the expression command still only creates MEL expressions, although they can
be called from Python.

---
Return:
---


    float: Length in non history mode.
    string: Node name, in history mode.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/arclen.html 
    """


def arrayMapper(destAttr: string, inputU: string, inputV: string, mapTo: string, target: string, type: string) -> list[string]:
    """Synopsis:
---
---
 arrayMapper([destAttr=string], [inputU=string], [inputV=string], [mapTo=string], [target=string], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

arrayMapper is undoable, NOT queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.arrayMapper( target='particle1', destAttr='rgbPP', inputV='ageNormalized', type='ramp' )

---
Return:
---


    list[string]: Names of created arrayMapper nodes.

Flags:
---


---
destAttr(da): string
    properties: create
    Specifies the attribute which will be the downstream
connection for the output data from the mapper node. The
attribute type will be used to determine which output attribute
to use: float array gets outValuePP, vector array gets outColorPP.
If the flag is omitted, no output connection is made.

---
inputU(iu): string
    properties: create
    Specifies the upstream attribute to connect to the mapper's
uCoordPP attribute. If the flag is omitted, no input connection
is made.

---
inputV(iv): string
    properties: create
    Specifies the upstream attribute to connect to the mapper's
vCoordPP attribute. If the flag is omitted, no input connection
is made.

---
mapTo(mt): string
    properties: create
    Specifies an existing node to be used to compute the output values.
This node must be of the appropriate type. Currently, only ramp nodes
may be used.

---
target(t): string
    properties: create, multiuse
    Specifies the target object to be connected to.

---
type(ty): string
    properties: create
    Specifies the node type to create which will be used to compute
the output values. Currently, only ramp is valid. If the flag is
omitted, no connection is made and the external node is not created.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/arrayMapper.html 
    """


def art3dPaintCtx(accopacity: boolean, afterStrokeCmd: string, alphablendmode: string, assigntxt: boolean, attrnames: string, beforeStrokeCmd: string, brushalignment: boolean, brushdepth: float, brushfeedback: boolean, brushtype: string, clear: boolean, commonattr: string, dragSlider: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, extendFillColor: boolean, fileformat: string, filetxtaspectratio: float, filetxtsizex: int, filetxtsizey: int, floodOpacity: float, floodall: boolean, floodselect: boolean, history: boolean, image1: string, image2: string, image3: string, keepaspectratio: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, name: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintmode: string, paintoperationtype: string, painttxtattr: string, painttxtattrname: string, pfxScale: float, pfxWidth: float, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, pressureMapping1: int, pressureMapping2: int, pressureMapping3: int, pressureMax1: float, pressureMax2: float, pressureMax3: float, pressureMin1: float, pressureMin2: float, pressureMin3: float, profileShapeFile: string, projective: boolean, radius: float, record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, reloadtexfile: boolean, resizeratio: float, resizetxt: boolean, rgbcolor: tuple[float, float, float], rgbflood: tuple[float, float, float], saveTextureOnStroke: boolean, saveonstroke: boolean, savetexture: boolean, screenRadius: float, selectclonesource: boolean, shadernames: string, shapeattr: boolean, shapenames: string, showactive: boolean, soloAsDiffuse: boolean, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, textureFilenames: boolean, updateEraseTex: boolean, usepressure: boolean, worldRadius: float) -> None:
    """Synopsis:
---
---
 art3dPaintCtx([accopacity=boolean], [afterStrokeCmd=string], [alphablendmode=string], [assigntxt=boolean], [attrnames=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushdepth=float], [brushfeedback=boolean], [brushtype=string], [clear=boolean], [commonattr=string], [dragSlider=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [extendFillColor=boolean], [fileformat=string], [filetxtaspectratio=float], [filetxtsizex=int], [filetxtsizey=int], [floodOpacity=float], [floodall=boolean], [floodselect=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [keepaspectratio=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [name=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintmode=string], [paintoperationtype=string], [painttxtattr=string], [painttxtattrname=string], [pfxScale=float], [pfxWidth=float], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [pressureMapping1=int], [pressureMapping2=int], [pressureMapping3=int], [pressureMax1=float], [pressureMax2=float], [pressureMax3=float], [pressureMin1=float], [pressureMin2=float], [pressureMin3=float], [profileShapeFile=string], [projective=boolean], [radius=float], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [reloadtexfile=boolean], [resizeratio=float], [resizetxt=boolean], [rgbcolor=[float, float, float]], [rgbflood=[float, float, float]], [saveTextureOnStroke=boolean], [saveonstroke=boolean], [savetexture=boolean], [screenRadius=float], [selectclonesource=boolean], [shadernames=string], [shapeattr=boolean], [shapenames=string], [showactive=boolean], [soloAsDiffuse=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [textureFilenames=boolean], [updateEraseTex=boolean], [usepressure=boolean], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

art3dPaintCtx is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

Create a new 3d paint context, then switch to it
cmds.art3dPaintCtx('art3dPaintCtx1')
cmds.setToolTo('art3dPaintCtx1')

Set art3dPaintCtx1's radius to 2.0, lowerradius to 0.5
cmds.art3dPaintCtx('art3dPaintCtx1', edit=True, r=2.0, lr=0.5)

---


Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
alphablendmode(abm): string
    properties: create, query, edit
    Specifies the blend mode used while painting
RGB channel. Currently, we support the following blend modes:
"Default" "Lighten" "Darken" "Difference" "Exclusion"
"Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant"
Default is "Default".

---
assigntxt(ast): boolean
    properties: edit
    Sends a request to the tool to allocate and assign
file textures to the specified attibute on the selected
shaders.

---
attrnames(atn): string
    properties: create, query, edit
    Name of attributes

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushdepth(bd): float
    properties: create, query, edit
    Depth of the brush

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
brushtype(brt): string
    properties: create, query, edit
    Name of the brush type

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
commonattr(cat): string
    properties: query
    Returns a string with the names of all common to
all the shaders paintable attributes and supported by the
Paint Texture Tool.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
extendFillColor(efc): boolean
    properties: create, query, edit
    States if the painted textures will be automatically
postprocessed on each stroke to fill in the background color.
Default is true.

---
fileformat(eff): string
    properties: create, query, edit
    Name of the file format

---
filetxtaspectratio(far): float
    properties: create, query, edit
    Specifies the aspect ration of the texture
width and height.
Default is 1.

---
filetxtsizex(ftx): int
    properties: create, query, edit
    Specifies the width of the texture.
Default is 256.

---
filetxtsizey(fty): int
    properties: create, query, edit
    Specifies the height of the texture.
Default is 256.

---
floodOpacity(fop): float
    properties: create, query, edit
    Value of the flood opacity

---
floodall(fal): boolean
    properties: create, query, edit
    Turn on to flood everything

---
floodselect(fsl): boolean
    properties: create, query, edit
    Should the selected area be flooded?

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
keepaspectratio(kar): boolean
    properties: create, query, edit
    States if the aspect ratio of the file texture
sizes should remain constant.
Default is true.
boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
painttxtattr(pta): string
    properties: create, query, edit
    Specifies the attribute on the shader which
the user wants to paint. Currently, we support the following
attributes: "Color", "Transparency", "Ambient", "Incandescence",
"BumpMap", "Diffuse", "Translucence" "Eccentricity"
"SpecularColor", "Reflectivity", "ReflectedColor", and
user-defined float, float3, double, and double3 attributes.
Default is "Color".

---
painttxtattrname(ptn): string
    properties: query, edit
    Returns a string with the names of all paintable
attributes supported by the Paint Texture Tool.

---
pfxScale(psc): float
    properties: query, edit
    Specifies the scale for Paint Effect brushes.

---
pfxWidth(pwd): float
    properties: query, edit
    Specifies the width for Paint Effect brushes.

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
pressureMapping1(pm1): int
    properties: create, query, edit
    First pressure mapping value

---
pressureMapping2(pm2): int
    properties: create, query, edit
    Second pressure mapping value

---
pressureMapping3(pm3): int
    properties: create, query, edit
    Third pressure mapping value

---
pressureMax1(px1): float
    properties: create, query, edit
    First pressure maximum value

---
pressureMax2(px2): float
    properties: create, query, edit
    Second pressure maximum value

---
pressureMax3(px3): float
    properties: create, query, edit
    Third pressure maximum value

---
pressureMin1(ps1): float
    properties: create, query, edit
    First pressure minimum value

---
pressureMin2(ps2): float
    properties: create, query, edit
    Second pressure minimum value

---
pressureMin3(ps3): float
    properties: create, query, edit
    Third pressure minimum value

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
reloadtexfile(rtf): boolean
    properties: edit
    Sends a request to the tool to reload the texture
from the disc.

---
resizeratio(rr): float
    properties: query, edit
    Specifies the scale by which to resize the
current textures.

---
resizetxt(rft): boolean
    properties: edit
    Sends a request to the tool to resize all the
currently in use textures.

---
rgbcolor(rgb): [float, float, float]
    properties: create, query, edit
    Colour value

---
rgbflood(fc): [float, float, float]
    properties: create, query, edit
    Color of the flood

---
saveTextureOnStroke(sts): boolean
    properties: create, query, edit
    States if the original texture will be automatically saved
on each stroke.
Default is false.

---
saveonstroke(sos): boolean
    properties: create, query, edit
    States if the temporary texture will be automatically saved
on each stroke.
Default is false.

---
savetexture(stx): boolean
    properties: edit
    Sends a request to the tool to save the texture
to the disc.

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
shadernames(hnm): string
    properties: query
    Returns a string with the names of all shaders assigned
to selected surfaces.

---
shapeattr(spa): boolean
    properties: query, edit
    States if the attribute to paint is an attribute of the shape and not the shader.
Default is false.

---
shapenames(shn): string
    properties: query
    Returns a string with the names of all surfaces
which are being painted on.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
soloAsDiffuse(sod): boolean
    properties: query, edit
    States if the currently paintable texture will be rendered as
as diffuse texture in the viewport.
Default is false.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
textureFilenames(tfn): boolean
    properties: query
    Returns a string array with the names of all the painted
file textures.

---
updateEraseTex(uet): boolean
    properties: create, query, edit
    Should the erase texture update?

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/art3dPaintCtx.html 
    """


def artAttrCtx(accopacity: boolean, activeListChangedProc: string, afterStrokeCmd: string, alphaclamp: string, alphaclamplower: float, alphaclampupper: float, attrSelected: string, beforeStrokeCmd: string, brushalignment: boolean, brushfeedback: boolean, clamp: string, clamplower: float, clampupper: float, clear: boolean, colorAlphaValue: float, colorRGBAValue: tuple[float, float, float, float], colorRGBValue: tuple[float, float, float], colorRamp: string, colorfeedback: boolean, colorfeedbackOverride: boolean, colorrangelower: float, colorrangeupper: float, dataTypeIndex: int, disablelighting: boolean, dragSlider: string, duringStrokeCmd: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, filterNodes: boolean, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, interactiveUpdate: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, maxvalue: float, minvalue: float, name: string, numericColorRamp: string, numericDisplayColor: tuple[float, float, float], numericDisplayPrecision: uint, numericMaxColor: tuple[float, float, float], numericMinColor: tuple[float, float, float], objattrArray: string, objattrArrayNoMenu: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintNodeArray: string, paintattrselected: string, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, radius: float, rampMaxColor: tuple[float, float, float], rampMinColor: tuple[float, float, float], record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, screenRadius: float, selectclonesource: boolean, selectedattroper: string, showactive: boolean, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, toolOffProc: string, toolOnProc: string, useColorRamp: boolean, useMaxMinColor: boolean, useNumericColorRamp: boolean, useNumericDisplay: boolean, usepressure: boolean, value: float, whichTool: string, worldRadius: float) -> string:
    """Synopsis:
---
---
 artAttrCtx([accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float], [attrSelected=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean], [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean], [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [interactiveUpdate=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxvalue=float], [minvalue=float], [name=string], [numericColorRamp=string], [numericDisplayColor=[float, float, float]], [numericDisplayPrecision=uint], [numericMaxColor=[float, float, float]], [numericMinColor=[float, float, float]], [objattrArray=string], [objattrArrayNoMenu=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string], [paintattrselected=string], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string], [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string], [useColorRamp=boolean], [useMaxMinColor=boolean], [useNumericColorRamp=boolean], [useNumericDisplay=boolean], [usepressure=boolean], [value=float], [whichTool=string], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artAttrCtx is undoable, queryable, and editable.
This is a context command to set the flags on the
Attribute Paint Tool context.




Example:
---
import maya.cmds as cmds

Create a new Attribute Paint Tool context, then switch to it
cmds.artAttrCtx('artAttrCtx1')
cmds.setToolTo('artAttrCtx1')

Set brush's radius to 2.0, lower radius to 0.5
cmds.artAttrCtx('artAttrCtx1', edit=True, r=2.0, lr=0.5)

---
Return:
---


    string: The name of the context created.

Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
activeListChangedProc(alp): string
    properties: create, query, edit
    Accepts a string that contains a MEL command that is
invoked whenever the active list changes. There may be some
situations where the UI, for example, needs to be updated,
when objects are selected/deselected in the scene. In query
mode, the name of the currently registered MEL command is
returned and this will be an empty string if none is defined.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
alphaclamp(alc): string
    properties: create, query, edit
    Specifies if the weight value should be alpha clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
alphaclamplower(acl): float
    properties: create, query, edit
    Specifies the lower bound for the alpha values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
alphaclampupper(acu): float
    properties: create, query, edit
    Specifies the upper bound for the alpha values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
attrSelected(asl): string
    properties: query
    Returns a name of the currently selected attribute.
Q: When queried, it returns a string.

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
clamp(cl): string
    properties: create, query, edit
    Specifies if the weight value should be clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
clamplower(cll): float
    properties: create, query, edit
    Specifies the lower bound for the values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
clampupper(clu): float
    properties: create, query, edit
    Specifies the upper bound for the values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
colorAlphaValue(cl1): float
    properties: create, query, edit
    The Alpha value of the color.

---
colorRGBAValue(cl4): [float, float, float, float]
    properties: create, query, edit
    The RGBA value of the color.

---
colorRGBValue(cl3): [float, float, float]
    properties: create, query, edit
    The RGB value of the color.

---
colorRamp(cr): string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors.

---
colorfeedback(cf): boolean
    properties: create, query, edit
    Sets on/off the color feedback display.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorfeedbackOverride(cfo): boolean
    properties: create, query, edit
    Sets on/off the color feedback override.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorrangelower(crl): float
    properties: create, query, edit
    Specifies the value that maps to black when
color feedback mode is on.
C: Default is 0.0.  Q: When queried, it returns a float.

---
colorrangeupper(cru): float
    properties: create, query, edit
    Specifies the value that maps to the maximum
color when color feedback mode is on.
C: Default is 1.0.  Q: When queried, it returns a float.

---
dataTypeIndex(dti): int
    properties: query, edit
    When the selected paintable attribute is a vectorArray,
it specifies which field to paint on.

---
disablelighting(dl): boolean
    properties: create, query, edit
    If color feedback is on, this flag determines whether
lighting is disabled or not for the surfaces that are
affected.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
duringStrokeCmd(dsk): string
    properties: create, query, edit
    The passed string is executed as a MEL command
during the stroke, each time the mouse is dragged.
C: Default is no command. Q: When queried, it returns
the current command

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

---
filterNodes(fon): boolean
    properties: edit
    Sets the node filter.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
interactiveUpdate(iu): boolean
    properties: create, query, edit
    Specifies how often to transfer the painted values
into the attribute.
TRUE: transfer them "continuously" (many times per stroke)
FALSE: transfer them only at the end of a stroke (on mouse
button release).
C: Default is TRUE. Q: When queried, it returns a boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
maxvalue(mxv): float
    properties: create, query, edit
    Specifies the maximum value for each attribute.
C: Default is 1.0.  Q: When queried, it returns a float.

---
minvalue(miv): float
    properties: create, query, edit
    Specifies the minimum value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
numericColorRamp(ncr) 2024: string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors for the
numeric display.

---
numericDisplayColor(ndc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a color to be used when displaying numeric values.

---
numericDisplayPrecision(ndp) 2024: uint
    properties: create, query, edit
    Specifies how many decimal points of precision should be used for the
numeric display.

---
numericMaxColor(nxc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
numericMinColor(nmc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
objattrArray(oaa): string
    properties: query
    An array of all paintable attributes. Each element of
the array is a string with the following information:
NodeType.NodeName.AttributeName.MenuType
*MenuType: type (level) of the item in the Menu (UI).
Q: When queried, it returns a string.

---
objattrArrayNoMenu(oan) 2024: string
    properties: query
    Returns an array of all paintable attributes in their original order.
Each element of the array is a string with the following information:
NodeType.NodeName.AttributeName

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintNodeArray(pna): string
    properties: query
    An array of paintable nodes.
Q: When queried, it returns a string.

---
paintattrselected(pas): string
    properties: edit
    An array of selected paintable attributes.
Each element of the array is a string with the
following information:
NodeType.NodeName.AttributeName.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
rampMaxColor(rxc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
rampMinColor(rmc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
selectedattroper(sao): string
    properties: create, query, edit
    Sets the edit weight operation. Four edit weights
operations are provided : "absolute" - the value of the weight
is replaced by the current one, "additive" - the value of the
weight is added to the current one, "scale" - the value of the
weight is multiplied by the current one, "smooth" - the value
of the weight is divided by the current one.
C: Default is "absolute".  Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
toolOffProc(tfp): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned off.
For example, cloth invokes "clothPaintToolOff" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is deactivated.
It is typical that if you implement a toolOffProc you will
want to implement a toolOnProc as well (see the -toolOnProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
toolOnProc(top): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned on.
For example, cloth invokes "clothPaintToolOn" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is activated.
It is typical that if you implement a toolOnProc you will
want to implement a toolOffProc as well (see the -toolOffProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
useColorRamp(ucr): boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors.  If this is turned off, the default greyscale feedback
will be used.

---
useMaxMinColor(umc): boolean
    properties: create, query, edit
    Specifies whether the out of range colors should be used.  See rampMinColor
and rampMaxColor flags for further details.

---
useNumericColorRamp(unr) 2024: boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors on the numeric display. If this is turned off, the set single
numeric color will be used.

---
useNumericDisplay(und) 2024: boolean
    properties: create, query, edit
    Specifies whether numerical weight values should be displayed next to
their associated control points.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
value(val): float
    properties: create, query, edit
    Specifies the value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
whichTool(wst): string
    properties: create, query, edit
    The string defines the name of the tool to be
used for the Artisan context. An example is "artClothPaint".
In query mode, the tool name for the given context is returned.
Note: due to the way MEL works, always specify the -query flag
last when specifying a flag that takes arguments.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artAttrCtx.html 
    """


def artAttrPaintVertexCtx(accopacity: boolean, activeListChangedProc: string, afterStrokeCmd: string, alphaclamp: string, alphaclamplower: float, alphaclampupper: float, attrSelected: string, beforeStrokeCmd: string, brushalignment: boolean, brushfeedback: boolean, clamp: string, clamplower: float, clampupper: float, clear: boolean, colorAlphaValue: float, colorRGBAValue: tuple[float, float, float, float], colorRGBValue: tuple[float, float, float], colorRamp: string, colorfeedback: boolean, colorfeedbackOverride: boolean, colorrangelower: float, colorrangeupper: float, dataTypeIndex: int, disablelighting: boolean, dragSlider: string, duringStrokeCmd: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, filterNodes: boolean, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, interactiveUpdate: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, maxvalue: float, minvalue: float, name: string, numericColorRamp: string, numericDisplayColor: tuple[float, float, float], numericDisplayPrecision: uint, numericMaxColor: tuple[float, float, float], numericMinColor: tuple[float, float, float], objattrArray: string, objattrArrayNoMenu: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintChannel: string, paintComponent: int, paintNodeArray: string, paintNumChannels: int, paintRGBA: boolean, paintVertexFace: boolean, paintattrselected: string, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, radius: float, rampMaxColor: tuple[float, float, float], rampMinColor: tuple[float, float, float], record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, screenRadius: float, selectclonesource: boolean, selectedattroper: string, showactive: boolean, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, toolOffProc: string, toolOnProc: string, useColorRamp: boolean, useMaxMinColor: boolean, useNumericColorRamp: boolean, useNumericDisplay: boolean, usepressure: boolean, value: float, vertexColorRange: boolean, vertexColorRangeLower: float, vertexColorRangeUpper: float, whichTool: string, worldRadius: float) -> None:
    """Synopsis:
---
---
 artAttrPaintVertexCtx(
[context]
    , [accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float], [attrSelected=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean], [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean], [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [interactiveUpdate=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxvalue=float], [minvalue=float], [name=string], [numericColorRamp=string], [numericDisplayColor=[float, float, float]], [numericDisplayPrecision=uint], [numericMaxColor=[float, float, float]], [numericMinColor=[float, float, float]], [objattrArray=string], [objattrArrayNoMenu=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintChannel=string], [paintComponent=int], [paintNodeArray=string], [paintNumChannels=int], [paintRGBA=boolean], [paintVertexFace=boolean], [paintattrselected=string], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string], [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string], [useColorRamp=boolean], [useMaxMinColor=boolean], [useNumericColorRamp=boolean], [useNumericDisplay=boolean], [usepressure=boolean], [value=float], [vertexColorRange=boolean], [vertexColorRangeLower=float], [vertexColorRangeUpper=float], [whichTool=string], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artAttrPaintVertexCtx is undoable, queryable, and editable.
This is a context command to set the flags on the
Paint color on vertex Tool context.




Example:
---
import maya.cmds as cmds

Create a new vertexAttr paint context, then switch to it
cmds.artAttrPaintVertexCtx('artAttrPaintVertexCtx1')
cmds.setToolTo('artAttrPaintVertexCtx1')

---


Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
activeListChangedProc(alp): string
    properties: create, query, edit
    Accepts a string that contains a MEL command that is
invoked whenever the active list changes. There may be some
situations where the UI, for example, needs to be updated,
when objects are selected/deselected in the scene. In query
mode, the name of the currently registered MEL command is
returned and this will be an empty string if none is defined.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
alphaclamp(alc): string
    properties: create, query, edit
    Specifies if the weight value should be alpha clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
alphaclamplower(acl): float
    properties: create, query, edit
    Specifies the lower bound for the alpha values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
alphaclampupper(acu): float
    properties: create, query, edit
    Specifies the upper bound for the alpha values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
attrSelected(asl): string
    properties: query
    Returns a name of the currently selected attribute.
Q: When queried, it returns a string.

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
clamp(cl): string
    properties: create, query, edit
    Specifies if the weight value should be clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
clamplower(cll): float
    properties: create, query, edit
    Specifies the lower bound for the values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
clampupper(clu): float
    properties: create, query, edit
    Specifies the upper bound for the values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
colorAlphaValue(cl1): float
    properties: create, query, edit
    The Alpha value of the color.

---
colorRGBAValue(cl4): [float, float, float, float]
    properties: create, query, edit
    The RGBA value of the color.

---
colorRGBValue(cl3): [float, float, float]
    properties: create, query, edit
    The RGB value of the color.

---
colorRamp(cr): string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors.

---
colorfeedback(cf): boolean
    properties: create, query, edit
    Sets on/off the color feedback display.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorfeedbackOverride(cfo): boolean
    properties: create, query, edit
    Sets on/off the color feedback override.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorrangelower(crl): float
    properties: create, query, edit
    Specifies the value that maps to black when
color feedback mode is on.
C: Default is 0.0.  Q: When queried, it returns a float.

---
colorrangeupper(cru): float
    properties: create, query, edit
    Specifies the value that maps to the maximum
color when color feedback mode is on.
C: Default is 1.0.  Q: When queried, it returns a float.

---
dataTypeIndex(dti): int
    properties: query, edit
    When the selected paintable attribute is a vectorArray,
it specifies which field to paint on.

---
disablelighting(dl): boolean
    properties: create, query, edit
    If color feedback is on, this flag determines whether
lighting is disabled or not for the surfaces that are
affected.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
duringStrokeCmd(dsk): string
    properties: create, query, edit
    The passed string is executed as a MEL command
during the stroke, each time the mouse is dragged.
C: Default is no command. Q: When queried, it returns
the current command

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

---
filterNodes(fon): boolean
    properties: edit
    Sets the node filter.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
interactiveUpdate(iu): boolean
    properties: create, query, edit
    Specifies how often to transfer the painted values
into the attribute.
TRUE: transfer them "continuously" (many times per stroke)
FALSE: transfer them only at the end of a stroke (on mouse
button release).
C: Default is TRUE. Q: When queried, it returns a boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
maxvalue(mxv): float
    properties: create, query, edit
    Specifies the maximum value for each attribute.
C: Default is 1.0.  Q: When queried, it returns a float.

---
minvalue(miv): float
    properties: create, query, edit
    Specifies the minimum value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
numericColorRamp(ncr) 2024: string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors for the
numeric display.

---
numericDisplayColor(ndc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a color to be used when displaying numeric values.

---
numericDisplayPrecision(ndp) 2024: uint
    properties: create, query, edit
    Specifies how many decimal points of precision should be used for the
numeric display.

---
numericMaxColor(nxc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
numericMinColor(nmc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
objattrArray(oaa): string
    properties: query
    An array of all paintable attributes. Each element of
the array is a string with the following information:
NodeType.NodeName.AttributeName.MenuType
*MenuType: type (level) of the item in the Menu (UI).
Q: When queried, it returns a string.

---
objattrArrayNoMenu(oan) 2024: string
    properties: query
    Returns an array of all paintable attributes in their original order.
Each element of the array is a string with the following information:
NodeType.NodeName.AttributeName

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintChannel(pch) 2024: string
    properties: create, query, edit
    Channel to paint - RGB, RGBA, R, G, B, A

---
paintComponent(pc): int
    properties: create, query, edit
    Specifies whether face or vertex or vertex face is being painted.
1 - Vertex
2 - VertexFace
3 - Face
C: Default is Vertex.  Q: When queried, it returns a int.

---
paintNodeArray(pna): string
    properties: query
    An array of paintable nodes.
Q: When queried, it returns a string.

---
paintNumChannels(pnc): int
    properties: create, query, edit
    Number of channels to paint - 1 (alpha), 3 (RGB), or 4 (RGBA)

---
paintRGBA(pc4): boolean
    properties: create, query, edit
    Specifies whether RGB or RGBA channels are being painted.
TRUE: RGBA channels.
FALSE: RGB channels. Alpha channel remains unaffected.
C: Default is FALSE (Painting RGB channels).
Q: When queried, it returns a int.

---
paintVertexFace(pvf): boolean
    properties: create, query, edit
    Specifies whether vertex face is being painted.
TRUE: Vertex face being painted. (Allows each face connected to the vertex
to be painted)
FALSE: Vertex being painted.(affects all connected faces)
C: Default is FALSE.  Q: When queried, it returns a int.

---
paintattrselected(pas): string
    properties: edit
    An array of selected paintable attributes.
Each element of the array is a string with the
following information:
NodeType.NodeName.AttributeName.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
rampMaxColor(rxc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
rampMinColor(rmc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
selectedattroper(sao): string
    properties: create, query, edit
    Sets the edit weight operation. Four edit weights
operations are provided : "absolute" - the value of the weight
is replaced by the current one, "additive" - the value of the
weight is added to the current one, "scale" - the value of the
weight is multiplied by the current one, "smooth" - the value
of the weight is divided by the current one.
C: Default is "absolute".  Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
toolOffProc(tfp): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned off.
For example, cloth invokes "clothPaintToolOff" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is deactivated.
It is typical that if you implement a toolOffProc you will
want to implement a toolOnProc as well (see the -toolOnProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
toolOnProc(top): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned on.
For example, cloth invokes "clothPaintToolOn" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is activated.
It is typical that if you implement a toolOnProc you will
want to implement a toolOffProc as well (see the -toolOffProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
useColorRamp(ucr): boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors.  If this is turned off, the default greyscale feedback
will be used.

---
useMaxMinColor(umc): boolean
    properties: create, query, edit
    Specifies whether the out of range colors should be used.  See rampMinColor
and rampMaxColor flags for further details.

---
useNumericColorRamp(unr) 2024: boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors on the numeric display. If this is turned off, the set single
numeric color will be used.

---
useNumericDisplay(und) 2024: boolean
    properties: create, query, edit
    Specifies whether numerical weight values should be displayed next to
their associated control points.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
value(val): float
    properties: create, query, edit
    Specifies the value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
vertexColorRange(vcr): boolean
    properties: create, query, edit
    Specifies whether the vertex color range should be applied
to the currently selected object.
C: Default is false  Q: When queried, it returns a boolean.

---
vertexColorRangeLower(vcl): float
    properties: create, query, edit
    Specifies the min value of the vertex color range.
C: Default is 0.0.  Q: When queried, it returns a float.

---
vertexColorRangeUpper(vcu): float
    properties: create, query, edit
    Specifies the max value of the vertex color range.
C: Default is 1.0.  Q: When queried, it returns a float.

---
whichTool(wst): string
    properties: create, query, edit
    The string defines the name of the tool to be
used for the Artisan context. An example is "artClothPaint".
In query mode, the tool name for the given context is returned.
Note: due to the way MEL works, always specify the -query flag
last when specifying a flag that takes arguments.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artAttrPaintVertexCtx.html 
    """


def artAttrSkinPaintCtx(accopacity: boolean, activeListChangedProc: string, afterStrokeCmd: string, alphaclamp: string, alphaclamplower: float, alphaclampupper: float, attrSelected: string, beforeStrokeCmd: string, brushalignment: boolean, brushfeedback: boolean, clamp: string, clamplower: float, clampupper: float, clear: boolean, colorAlphaValue: float, colorRGBAValue: tuple[float, float, float, float], colorRGBValue: tuple[float, float, float], colorRamp: string, colorfeedback: boolean, colorfeedbackOverride: boolean, colorrangelower: float, colorrangeupper: float, dataTypeIndex: int, disablelighting: boolean, dragSlider: string, duringStrokeCmd: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, filterNodes: boolean, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, influence: string, interactiveUpdate: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, maxvalue: float, minvalue: float, name: string, numericColorRamp: string, numericDisplayColor: tuple[float, float, float], numericDisplayPrecision: uint, numericMaxColor: tuple[float, float, float], numericMinColor: tuple[float, float, float], objattrArray: string, objattrArrayNoMenu: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintNodeArray: string, paintSelectMode: int, paintattrselected: string, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, radius: float, rampMaxColor: tuple[float, float, float], rampMinColor: tuple[float, float, float], record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, screenRadius: float, selectclonesource: boolean, selectedattroper: string, showactive: boolean, skinPaintMode: int, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, toolOffProc: string, toolOnProc: string, useColorRamp: boolean, useMaxMinColor: boolean, useNumericColorRamp: boolean, useNumericDisplay: boolean, usepressure: boolean, value: float, whichTool: string, worldRadius: float, xrayJoints: boolean) -> None:
    """Synopsis:
---
---
 artAttrSkinPaintCtx(
[context]
    , [accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float], [attrSelected=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean], [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean], [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [influence=string], [interactiveUpdate=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxvalue=float], [minvalue=float], [name=string], [numericColorRamp=string], [numericDisplayColor=[float, float, float]], [numericDisplayPrecision=uint], [numericMaxColor=[float, float, float]], [numericMinColor=[float, float, float]], [objattrArray=string], [objattrArrayNoMenu=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string], [paintSelectMode=int], [paintattrselected=string], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string], [showactive=boolean], [skinPaintMode=int], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string], [useColorRamp=boolean], [useMaxMinColor=boolean], [useNumericColorRamp=boolean], [useNumericDisplay=boolean], [usepressure=boolean], [value=float], [whichTool=string], [worldRadius=float], [xrayJoints=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artAttrSkinPaintCtx is undoable, queryable, and editable.
This is a context command to set the flags on the
Paint skin weights tool context.




Example:
---
import maya.cmds as cmds

Create a new skinAttr paint context, then switch to it
cmds.artAttrSkinPaintCtx('artAttrSkinPaintCtx1')
cmds.setToolTo('artAttrSkinPaintCtx1')

Set the edit weight operation to "smooth"
cmds.artAttrSkinPaintCtx('artAttrSkinPaintCtx1', edit=True, sao='smooth')

---


Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
activeListChangedProc(alp): string
    properties: create, query, edit
    Accepts a string that contains a MEL command that is
invoked whenever the active list changes. There may be some
situations where the UI, for example, needs to be updated,
when objects are selected/deselected in the scene. In query
mode, the name of the currently registered MEL command is
returned and this will be an empty string if none is defined.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
alphaclamp(alc): string
    properties: create, query, edit
    Specifies if the weight value should be alpha clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
alphaclamplower(acl): float
    properties: create, query, edit
    Specifies the lower bound for the alpha values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
alphaclampupper(acu): float
    properties: create, query, edit
    Specifies the upper bound for the alpha values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
attrSelected(asl): string
    properties: query
    Returns a name of the currently selected attribute.
Q: When queried, it returns a string.

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
clamp(cl): string
    properties: create, query, edit
    Specifies if the weight value should be clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
clamplower(cll): float
    properties: create, query, edit
    Specifies the lower bound for the values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
clampupper(clu): float
    properties: create, query, edit
    Specifies the upper bound for the values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
colorAlphaValue(cl1): float
    properties: create, query, edit
    The Alpha value of the color.

---
colorRGBAValue(cl4): [float, float, float, float]
    properties: create, query, edit
    The RGBA value of the color.

---
colorRGBValue(cl3): [float, float, float]
    properties: create, query, edit
    The RGB value of the color.

---
colorRamp(cr): string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors.

---
colorfeedback(cf): boolean
    properties: create, query, edit
    Sets on/off the color feedback display.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorfeedbackOverride(cfo): boolean
    properties: create, query, edit
    Sets on/off the color feedback override.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorrangelower(crl): float
    properties: create, query, edit
    Specifies the value that maps to black when
color feedback mode is on.
C: Default is 0.0.  Q: When queried, it returns a float.

---
colorrangeupper(cru): float
    properties: create, query, edit
    Specifies the value that maps to the maximum
color when color feedback mode is on.
C: Default is 1.0.  Q: When queried, it returns a float.

---
dataTypeIndex(dti): int
    properties: query, edit
    When the selected paintable attribute is a vectorArray,
it specifies which field to paint on.

---
disablelighting(dl): boolean
    properties: create, query, edit
    If color feedback is on, this flag determines whether
lighting is disabled or not for the surfaces that are
affected.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
duringStrokeCmd(dsk): string
    properties: create, query, edit
    The passed string is executed as a MEL command
during the stroke, each time the mouse is dragged.
C: Default is no command. Q: When queried, it returns
the current command

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

---
filterNodes(fon): boolean
    properties: edit
    Sets the node filter.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
influence(inf): string
    properties: query, edit
    Specifies which joint has been selected by the user for painting.
Q: When queried, it returns a string.

---
interactiveUpdate(iu): boolean
    properties: create, query, edit
    Specifies how often to transfer the painted values
into the attribute.
TRUE: transfer them "continuously" (many times per stroke)
FALSE: transfer them only at the end of a stroke (on mouse
button release).
C: Default is TRUE. Q: When queried, it returns a boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
maxvalue(mxv): float
    properties: create, query, edit
    Specifies the maximum value for each attribute.
C: Default is 1.0.  Q: When queried, it returns a float.

---
minvalue(miv): float
    properties: create, query, edit
    Specifies the minimum value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
numericColorRamp(ncr) 2024: string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors for the
numeric display.

---
numericDisplayColor(ndc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a color to be used when displaying numeric values.

---
numericDisplayPrecision(ndp) 2024: uint
    properties: create, query, edit
    Specifies how many decimal points of precision should be used for the
numeric display.

---
numericMaxColor(nxc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
numericMinColor(nmc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
objattrArray(oaa): string
    properties: query
    An array of all paintable attributes. Each element of
the array is a string with the following information:
NodeType.NodeName.AttributeName.MenuType
*MenuType: type (level) of the item in the Menu (UI).
Q: When queried, it returns a string.

---
objattrArrayNoMenu(oan) 2024: string
    properties: query
    Returns an array of all paintable attributes in their original order.
Each element of the array is a string with the following information:
NodeType.NodeName.AttributeName

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintNodeArray(pna): string
    properties: query
    An array of paintable nodes.
Q: When queried, it returns a string.

---
paintSelectMode(psm): int
    properties: query, edit
    Specifies whether the paint select tool: adds to selection (1)
removes from selection (2), toggles selection (3)
Q: When queried, it returns an int as defined above.

---
paintattrselected(pas): string
    properties: edit
    An array of selected paintable attributes.
Each element of the array is a string with the
following information:
NodeType.NodeName.AttributeName.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
rampMaxColor(rxc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
rampMinColor(rmc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
selectedattroper(sao): string
    properties: create, query, edit
    Sets the edit weight operation. Four edit weights
operations are provided : "absolute" - the value of the weight
is replaced by the current one, "additive" - the value of the
weight is added to the current one, "scale" - the value of the
weight is multiplied by the current one, "smooth" - the value
of the weight is divided by the current one.
C: Default is "absolute".  Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
skinPaintMode(spm): int
    properties: query, edit
    Specifies whether the skin paint tool is in paint skin weights mode (1)
Marquee select mode (0), or paint select mode (2)
Q: When queried, it returns an int as defined above.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
toolOffProc(tfp): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned off.
For example, cloth invokes "clothPaintToolOff" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is deactivated.
It is typical that if you implement a toolOffProc you will
want to implement a toolOnProc as well (see the -toolOnProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
toolOnProc(top): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned on.
For example, cloth invokes "clothPaintToolOn" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is activated.
It is typical that if you implement a toolOnProc you will
want to implement a toolOffProc as well (see the -toolOffProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
useColorRamp(ucr): boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors.  If this is turned off, the default greyscale feedback
will be used.

---
useMaxMinColor(umc): boolean
    properties: create, query, edit
    Specifies whether the out of range colors should be used.  See rampMinColor
and rampMaxColor flags for further details.

---
useNumericColorRamp(unr) 2024: boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors on the numeric display. If this is turned off, the set single
numeric color will be used.

---
useNumericDisplay(und) 2024: boolean
    properties: create, query, edit
    Specifies whether numerical weight values should be displayed next to
their associated control points.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
value(val): float
    properties: create, query, edit
    Specifies the value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
whichTool(wst): string
    properties: create, query, edit
    The string defines the name of the tool to be
used for the Artisan context. An example is "artClothPaint".
In query mode, the tool name for the given context is returned.
Note: due to the way MEL works, always specify the -query flag
last when specifying a flag that takes arguments.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

---
xrayJoints(xry): boolean
    properties: query, edit
    Specifies whether joints should be displayed in xray mode while painting
Q: When queried, it returns a boolean.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artAttrSkinPaintCtx.html 
    """


def artAttrTool(add: string, exists: string, remove: string) -> None:
    """Synopsis:
---
---
 artAttrTool([add=string], [exists=string], [remove=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artAttrTool is NOT undoable, queryable, and NOT editable.     The artAttrTool command manages the list of tool types which are
        used for attribute painting. This command supports querying the
        list contents as well as adding new tools to the list. Note that
        there is a set of built-in tools. The list of built-ins can
        be queried by starting Maya and doing an "artAttrTool -q".

        The tools which are managed by this command are all intended for
        attribute painting via Artisan: when you create a new context via
        artAttrCtx you specify the tool name via artAttrCtx's -whichTool
        flag. Typically the user may wish to simply use one of the built-in
        tools. However, if you need to have custom Properties and Values sheets
        asscociated with your tool, you will need to define a custom tool
        via artAttrTool -add "toolName". For an example of a custom
        attribute painting tool, see the devkit example customtoolPaint.mel.




Example:
---
import maya.cmds as cmds

Add a tool named "customtoolPaint" to the list of
attribute painting tools, then creates a new context called
"customtoolPaintContext" which utilises the "customtoolPaint" tool.
---

cmds.artAttrTool( add='customtoolPaint' )
cmds.artAttrCtx( 'customtoolPaintContext', whichTool='customtoolPaint' )

List all tools currently defined.
---

cmds.artAttrTool( query=True )

---


Flags:
---


---
add(): string
    properties: create
    Adds the named tool to the internal list of tools.

---
exists(ex): string
    properties: create, query
    Checks if the named tool exists, returning true if found, and false otherwise.

---
remove(rm): string
    properties: create
    Removes the named tool from the internal list of tools.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artAttrTool.html 
    """


def artBuildPaintMenu() -> None:
    """Synopsis:
---
---
 artBuildPaintMenu()  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artBuildPaintMenu is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds


build a list of paintable attributes for the selected item(s)
---

cmds.artBuildPaintMenu();

---


Flags:
---


URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artBuildPaintMenu.html 
    """


def artFluidAttrCtx(accopacity: boolean, activeListChangedProc: string, afterStrokeCmd: string, alphaclamp: string, alphaclamplower: float, alphaclampupper: float, attrSelected: string, autoSave: string, beforeStrokeCmd: string, brushalignment: boolean, brushfeedback: boolean, clamp: string, clamplower: float, clampupper: float, clear: boolean, colorAlphaValue: float, colorRGBAValue: tuple[float, float, float, float], colorRGBValue: tuple[float, float, float], colorRamp: string, colorfeedback: boolean, colorfeedbackOverride: boolean, colorrangelower: float, colorrangeupper: float, currentPaintableFluid: string, dataTypeIndex: int, delaySelectionChanged: boolean, disablelighting: boolean, displayAsRender: boolean, displayVelocity: boolean, doAutoSave: boolean, dragSlider: string, duringStrokeCmd: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, filterNodes: boolean, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, interactiveUpdate: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, maxvalue: float, minvalue: float, name: string, numericColorRamp: string, numericDisplayColor: tuple[float, float, float], numericDisplayPrecision: uint, numericMaxColor: tuple[float, float, float], numericMinColor: tuple[float, float, float], objattrArray: string, objattrArrayNoMenu: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintNodeArray: string, paintattrselected: string, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, property: string, radius: float, rampMaxColor: tuple[float, float, float], rampMinColor: tuple[float, float, float], record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, rgbValue: tuple[float, float, float], screenRadius: float, selectclonesource: boolean, selectedattroper: string, showactive: boolean, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, toolOffProc: string, toolOnProc: string, useColorRamp: boolean, useMaxMinColor: boolean, useNumericColorRamp: boolean, useNumericDisplay: boolean, useStrokeDirection: boolean, usepressure: boolean, value: float, velocity: tuple[float, float, float], whichTool: string, worldRadius: float) -> None:
    """Synopsis:
---
---
 artFluidAttrCtx([accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float], [attrSelected=string], [autoSave=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean], [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float], [currentPaintableFluid=string], [dataTypeIndex=int], [delaySelectionChanged=boolean], [disablelighting=boolean], [displayAsRender=boolean], [displayVelocity=boolean], [doAutoSave=boolean], [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [interactiveUpdate=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxvalue=float], [minvalue=float], [name=string], [numericColorRamp=string], [numericDisplayColor=[float, float, float]], [numericDisplayPrecision=uint], [numericMaxColor=[float, float, float]], [numericMinColor=[float, float, float]], [objattrArray=string], [objattrArrayNoMenu=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string], [paintattrselected=string], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [property=string], [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [rgbValue=[float, float, float]], [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string], [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string], [useColorRamp=boolean], [useMaxMinColor=boolean], [useNumericColorRamp=boolean], [useNumericDisplay=boolean], [useStrokeDirection=boolean], [usepressure=boolean], [value=float], [velocity=[float, float, float]], [whichTool=string], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artFluidAttrCtx is undoable, queryable, and editable.
This command is used to paint properties
(such as density) of selected fluid volumes.




Example:
---
import maya.cmds as cmds

Create a new fluidAttr paint context, then switch to it
cmds.artFluidAttrCtx('artFluidAttrCtx1')
cmds.setToolTo('artFluidAttrCtx1')

Set to paint the color property on the fluid
cmds.artFluidAttrCtx('artFluidAttrCtx1', edit=True, property='color')

---


Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
activeListChangedProc(alp): string
    properties: create, query, edit
    Accepts a string that contains a MEL command that is
invoked whenever the active list changes. There may be some
situations where the UI, for example, needs to be updated,
when objects are selected/deselected in the scene. In query
mode, the name of the currently registered MEL command is
returned and this will be an empty string if none is defined.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
alphaclamp(alc): string
    properties: create, query, edit
    Specifies if the weight value should be alpha clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
alphaclamplower(acl): float
    properties: create, query, edit
    Specifies the lower bound for the alpha values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
alphaclampupper(acu): float
    properties: create, query, edit
    Specifies the upper bound for the alpha values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
attrSelected(asl): string
    properties: query
    Returns a name of the currently selected attribute.
Q: When queried, it returns a string.

---
autoSave(autoSave): string
    properties: create, query, edit
    A MEL command to save the fluid state.  Called
before an event which could overwrite unsaved values of
painted fluid properties.  Such events include: changing
current time, changing the current paintable property, and
exiting the paint tool.  (To turn auto-save off, pass in
an empty-valued string argument: e.g., "".)

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
clamp(cl): string
    properties: create, query, edit
    Specifies if the weight value should be clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
clamplower(cll): float
    properties: create, query, edit
    Specifies the lower bound for the values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
clampupper(clu): float
    properties: create, query, edit
    Specifies the upper bound for the values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
colorAlphaValue(cl1): float
    properties: create, query, edit
    The Alpha value of the color.

---
colorRGBAValue(cl4): [float, float, float, float]
    properties: create, query, edit
    The RGBA value of the color.

---
colorRGBValue(cl3): [float, float, float]
    properties: create, query, edit
    The RGB value of the color.

---
colorRamp(cr): string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors.

---
colorfeedback(cf): boolean
    properties: create, query, edit
    Sets on/off the color feedback display.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorfeedbackOverride(cfo): boolean
    properties: create, query, edit
    Sets on/off the color feedback override.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorrangelower(crl): float
    properties: create, query, edit
    Specifies the value that maps to black when
color feedback mode is on.
C: Default is 0.0.  Q: When queried, it returns a float.

---
colorrangeupper(cru): float
    properties: create, query, edit
    Specifies the value that maps to the maximum
color when color feedback mode is on.
C: Default is 1.0.  Q: When queried, it returns a float.

---
currentPaintableFluid(cpf): string
    properties: query
    Query the name of the fluid on which this context is
currently painting.  Returns string.

---
dataTypeIndex(dti): int
    properties: query, edit
    When the selected paintable attribute is a vectorArray,
it specifies which field to paint on.

---
delaySelectionChanged(dsc): boolean
    properties: create, query, edit
    Internal use only.  Under normal conditions,
the tool responds to changes to the selection list so it
can update its list of paintable geometry.  When
-dsl true is used, the tool will not update its paintable
list until a corresponding -dsl false is called.

---
disablelighting(dl): boolean
    properties: create, query, edit
    If color feedback is on, this flag determines whether
lighting is disabled or not for the surfaces that are
affected.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
displayAsRender(dar): boolean
    properties: create, query, edit
    When true, sets the "Shaded Display" attribute
of the fluid to "AsRender": all fluid properties displayed
as hardware rendered.  When false, displays only the
currently selected paintable attribute of the fluid.

---
displayVelocity(dv): boolean
    properties: create, query, edit
    Turns on/off velocity display, independently of the
above "dar/displayAsRender" setting.  Use this flag
to enable velocity display while only displaying density, for
example.

---
doAutoSave(das): boolean
    properties: edit
    Execute the -autoSave command if there are
unsaved painted fluid properties.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
duringStrokeCmd(dsk): string
    properties: create, query, edit
    The passed string is executed as a MEL command
during the stroke, each time the mouse is dragged.
C: Default is no command. Q: When queried, it returns
the current command

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

---
filterNodes(fon): boolean
    properties: edit
    Sets the node filter.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
interactiveUpdate(iu): boolean
    properties: create, query, edit
    Specifies how often to transfer the painted values
into the attribute.
TRUE: transfer them "continuously" (many times per stroke)
FALSE: transfer them only at the end of a stroke (on mouse
button release).
C: Default is TRUE. Q: When queried, it returns a boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
maxvalue(mxv): float
    properties: create, query, edit
    Specifies the maximum value for each attribute.
C: Default is 1.0.  Q: When queried, it returns a float.

---
minvalue(miv): float
    properties: create, query, edit
    Specifies the minimum value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
numericColorRamp(ncr) 2024: string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors for the
numeric display.

---
numericDisplayColor(ndc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a color to be used when displaying numeric values.

---
numericDisplayPrecision(ndp) 2024: uint
    properties: create, query, edit
    Specifies how many decimal points of precision should be used for the
numeric display.

---
numericMaxColor(nxc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
numericMinColor(nmc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
objattrArray(oaa): string
    properties: query
    An array of all paintable attributes. Each element of
the array is a string with the following information:
NodeType.NodeName.AttributeName.MenuType
*MenuType: type (level) of the item in the Menu (UI).
Q: When queried, it returns a string.

---
objattrArrayNoMenu(oan) 2024: string
    properties: query
    Returns an array of all paintable attributes in their original order.
Each element of the array is a string with the following information:
NodeType.NodeName.AttributeName

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintNodeArray(pna): string
    properties: query
    An array of paintable nodes.
Q: When queried, it returns a string.

---
paintattrselected(pas): string
    properties: edit
    An array of selected paintable attributes.
Each element of the array is a string with the
following information:
NodeType.NodeName.AttributeName.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
property(p): string
    properties: create, query, edit
    Specifies a property to paint on the fluid.
Valid values are "color", "density", "densityAndColor,"
"densityAndFuel," "temperature," "fuel", "velocity".

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
rampMaxColor(rxc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
rampMinColor(rmc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
rgbValue(rgb): [float, float, float]
    properties: create, query, edit
    Specifies the values of the red, green, and
blue components of the color to
use when painting the property "color."

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
selectedattroper(sao): string
    properties: create, query, edit
    Sets the edit weight operation. Four edit weights
operations are provided : "absolute" - the value of the weight
is replaced by the current one, "additive" - the value of the
weight is added to the current one, "scale" - the value of the
weight is multiplied by the current one, "smooth" - the value
of the weight is divided by the current one.
C: Default is "absolute".  Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
toolOffProc(tfp): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned off.
For example, cloth invokes "clothPaintToolOff" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is deactivated.
It is typical that if you implement a toolOffProc you will
want to implement a toolOnProc as well (see the -toolOnProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
toolOnProc(top): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned on.
For example, cloth invokes "clothPaintToolOn" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is activated.
It is typical that if you implement a toolOnProc you will
want to implement a toolOffProc as well (see the -toolOffProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
useColorRamp(ucr): boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors.  If this is turned off, the default greyscale feedback
will be used.

---
useMaxMinColor(umc): boolean
    properties: create, query, edit
    Specifies whether the out of range colors should be used.  See rampMinColor
and rampMaxColor flags for further details.

---
useNumericColorRamp(unr) 2024: boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors on the numeric display. If this is turned off, the set single
numeric color will be used.

---
useNumericDisplay(und) 2024: boolean
    properties: create, query, edit
    Specifies whether numerical weight values should be displayed next to
their associated control points.

---
useStrokeDirection(usd): boolean
    properties: create, query, edit
    Applicable only during "velocity"
painting.  Specifies whether the value of the
painted velocity should come from the direction
of the brush stroke, overriding the value specified
by the -v/-velocity flag.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
value(val): float
    properties: create, query, edit
    Specifies the value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
velocity(v): [float, float, float]
    properties: create, query, edit
    Specifies the values of the x, y, and z
components of the velocity to use when painting the property
"velocity".

---
whichTool(wst): string
    properties: create, query, edit
    The string defines the name of the tool to be
used for the Artisan context. An example is "artClothPaint".
In query mode, the tool name for the given context is returned.
Note: due to the way MEL works, always specify the -query flag
last when specifying a flag that takes arguments.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artFluidAttrCtx.html 
    """


def artPuttyCtx(accopacity: boolean, activeListChangedProc: string, afterStrokeCmd: string, alphaclamp: string, alphaclamplower: float, alphaclampupper: float, attrSelected: string, autosmooth: boolean, beforeStrokeCmd: string, brushStrength: float, brushalignment: boolean, brushfeedback: boolean, clamp: string, clamplower: float, clampupper: float, clear: boolean, collapsecvtol: float, colorAlphaValue: float, colorRGBAValue: tuple[float, float, float, float], colorRGBValue: tuple[float, float, float], colorRamp: string, colorfeedback: boolean, colorfeedbackOverride: boolean, colorrangelower: float, colorrangeupper: float, dataTypeIndex: int, disablelighting: boolean, dispdecr: boolean, dispincr: boolean, dragSlider: string, duringStrokeCmd: string, dynclonemode: boolean, erasesrfupd: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, filterNodes: boolean, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, interactiveUpdate: boolean, invertrefvector: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, maxdisp: float, maxvalue: float, minvalue: float, mouldtypehead: string, mouldtypemouse: string, mouldtypetail: string, name: string, numericColorRamp: string, numericDisplayColor: tuple[float, float, float], numericDisplayPrecision: uint, numericMaxColor: tuple[float, float, float], numericMinColor: tuple[float, float, float], objattrArray: string, objattrArrayNoMenu: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintNodeArray: string, paintattrselected: string, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, polecv: boolean, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, radius: float, rampMaxColor: tuple[float, float, float], rampMinColor: tuple[float, float, float], record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, refsurface: boolean, refvector: string, refvectoru: float, refvectorv: float, screenRadius: float, selectclonesource: boolean, selectedattroper: string, showactive: boolean, smoothiters: int, stampDepth: float, stampProfile: string, stampSpacing: float, stitchcorner: boolean, stitchedgeflood: boolean, stitchtype: string, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, toolOffProc: string, toolOnProc: string, updateerasesrf: boolean, updaterefsrf: boolean, useColorRamp: boolean, useMaxMinColor: boolean, useNumericColorRamp: boolean, useNumericDisplay: boolean, usepressure: boolean, value: float, whichTool: string, worldRadius: float) -> None:
    """Synopsis:
---
---
 artPuttyCtx([accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float], [attrSelected=string], [autosmooth=boolean], [beforeStrokeCmd=string], [brushStrength=float], [brushalignment=boolean], [brushfeedback=boolean], [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean], [collapsecvtol=float], [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean], [dispdecr=boolean], [dispincr=boolean], [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean], [erasesrfupd=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [interactiveUpdate=boolean], [invertrefvector=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxdisp=float], [maxvalue=float], [minvalue=float], [mouldtypehead=string], [mouldtypemouse=string], [mouldtypetail=string], [name=string], [numericColorRamp=string], [numericDisplayColor=[float, float, float]], [numericDisplayPrecision=uint], [numericMaxColor=[float, float, float]], [numericMinColor=[float, float, float]], [objattrArray=string], [objattrArrayNoMenu=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string], [paintattrselected=string], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [polecv=boolean], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [refsurface=boolean], [refvector=string], [refvectoru=float], [refvectorv=float], [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string], [showactive=boolean], [smoothiters=int], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [stitchcorner=boolean], [stitchedgeflood=boolean], [stitchtype=string], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string], [updateerasesrf=boolean], [updaterefsrf=boolean], [useColorRamp=boolean], [useMaxMinColor=boolean], [useNumericColorRamp=boolean], [useNumericDisplay=boolean], [usepressure=boolean], [value=float], [whichTool=string], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artPuttyCtx is undoable, queryable, and editable.
This command is used to modify NURBS surfaces using a brush based
interface (Maya Artisan). This is accomplished by moving the control
vertices (CVs) under the brush in the specified direction.




Example:
---
import maya.cmds as cmds

Set the brush radius to 20.0
cmds.artPuttyCtx( 'artPuttyContext', e=True, radius=20.00  )

Set the display of additional brush feedback
cmds.artPuttyCtx( 'artPuttyContext', e=True, brushfeedback=True )

---


Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
activeListChangedProc(alp): string
    properties: create, query, edit
    Accepts a string that contains a MEL command that is
invoked whenever the active list changes. There may be some
situations where the UI, for example, needs to be updated,
when objects are selected/deselected in the scene. In query
mode, the name of the currently registered MEL command is
returned and this will be an empty string if none is defined.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
alphaclamp(alc): string
    properties: create, query, edit
    Specifies if the weight value should be alpha clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
alphaclamplower(acl): float
    properties: create, query, edit
    Specifies the lower bound for the alpha values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
alphaclampupper(acu): float
    properties: create, query, edit
    Specifies the upper bound for the alpha values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
attrSelected(asl): string
    properties: query
    Returns a name of the currently selected attribute.
Q: When queried, it returns a string.

---
autosmooth(asm): boolean
    properties: create, query, edit
    Sets up the auto smoothing option. When the brush
is in the smooth mode, adjusting the strength will adjust how
fast the surfaces is smoothed out.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushStrength(bs): float
    properties: create, query, edit
    Sets the strength of the brush. Brush strength is supported
by the pinch and slide brushes. In pinch mode, adjusting the strength
will adjust how quickly the surface converges on the brush
center. In slide mode, the strength scales the motion of the brush.
C: Default is 1.0.  Q: When queried, it returns a float.

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
clamp(cl): string
    properties: create, query, edit
    Specifies if the weight value should be clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
clamplower(cll): float
    properties: create, query, edit
    Specifies the lower bound for the values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
clampupper(clu): float
    properties: create, query, edit
    Specifies the upper bound for the values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
collapsecvtol(clc): float
    properties: create, query, edit
    Specifies the tolerance for the collapse cv detection.
C: Default is 0.005 cm.  Q: When queried, it returns a float.

---
colorAlphaValue(cl1): float
    properties: create, query, edit
    The Alpha value of the color.

---
colorRGBAValue(cl4): [float, float, float, float]
    properties: create, query, edit
    The RGBA value of the color.

---
colorRGBValue(cl3): [float, float, float]
    properties: create, query, edit
    The RGB value of the color.

---
colorRamp(cr): string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors.

---
colorfeedback(cf): boolean
    properties: create, query, edit
    Sets on/off the color feedback display.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorfeedbackOverride(cfo): boolean
    properties: create, query, edit
    Sets on/off the color feedback override.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorrangelower(crl): float
    properties: create, query, edit
    Specifies the value that maps to black when
color feedback mode is on.
C: Default is 0.0.  Q: When queried, it returns a float.

---
colorrangeupper(cru): float
    properties: create, query, edit
    Specifies the value that maps to the maximum
color when color feedback mode is on.
C: Default is 1.0.  Q: When queried, it returns a float.

---
dataTypeIndex(dti): int
    properties: query, edit
    When the selected paintable attribute is a vectorArray,
it specifies which field to paint on.

---
disablelighting(dl): boolean
    properties: create, query, edit
    If color feedback is on, this flag determines whether
lighting is disabled or not for the surfaces that are
affected.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
dispdecr(dde): boolean
    properties: create, edit
    Decreases a maximum displacement by 10%.

---
dispincr(din): boolean
    properties: create, edit
    Increases a maximum displacement by 10%.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
duringStrokeCmd(dsk): string
    properties: create, query, edit
    The passed string is executed as a MEL command
during the stroke, each time the mouse is dragged.
C: Default is no command. Q: When queried, it returns
the current command

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
erasesrfupd(eut): boolean
    properties: create, query, edit
    Toggles the update for the erase surface

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

---
filterNodes(fon): boolean
    properties: edit
    Sets the node filter.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
interactiveUpdate(iu): boolean
    properties: create, query, edit
    Specifies how often to transfer the painted values
into the attribute.
TRUE: transfer them "continuously" (many times per stroke)
FALSE: transfer them only at the end of a stroke (on mouse
button release).
C: Default is TRUE. Q: When queried, it returns a boolean.

---
invertrefvector(irv): boolean
    properties: create, query, edit
    Sets the invert of the reference vector option when
the reflection is ON. If it is true, the reference vector
for the reflected stroke is negated with respect to the original
one.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
maxdisp(md): float
    properties: create, query, edit
    Defines a maximum displacement
( maxDisp in [0.0..5.0] ).
C: Default is 1.0.  Q: When queried, it returns a float.

---
maxvalue(mxv): float
    properties: create, query, edit
    Specifies the maximum value for each attribute.
C: Default is 1.0.  Q: When queried, it returns a float.

---
minvalue(miv): float
    properties: create, query, edit
    Specifies the minimum value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
mouldtypehead(mth): string
    properties: create, query, edit
    Type of type mould to use

---
mouldtypemouse(mtm): string
    properties: create, query, edit
    Specifies the putty operations/mode ("push" - pushes CVs
along the given direction (see refvector flag), "pull" - pulls
CVs along the specified direction, "smooth" - smooths the sculpt,
"erase" - erases the paint).
C: Default is "push".  Q: When queried, it returns a string.

---
mouldtypetail(mtt): string
    properties: create, query, edit
    Type of eraser mould to use

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
numericColorRamp(ncr) 2024: string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors for the
numeric display.

---
numericDisplayColor(ndc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a color to be used when displaying numeric values.

---
numericDisplayPrecision(ndp) 2024: uint
    properties: create, query, edit
    Specifies how many decimal points of precision should be used for the
numeric display.

---
numericMaxColor(nxc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
numericMinColor(nmc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
objattrArray(oaa): string
    properties: query
    An array of all paintable attributes. Each element of
the array is a string with the following information:
NodeType.NodeName.AttributeName.MenuType
*MenuType: type (level) of the item in the Menu (UI).
Q: When queried, it returns a string.

---
objattrArrayNoMenu(oan) 2024: string
    properties: query
    Returns an array of all paintable attributes in their original order.
Each element of the array is a string with the following information:
NodeType.NodeName.AttributeName

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintNodeArray(pna): string
    properties: query
    An array of paintable nodes.
Q: When queried, it returns a string.

---
paintattrselected(pas): string
    properties: edit
    An array of selected paintable attributes.
Each element of the array is a string with the
following information:
NodeType.NodeName.AttributeName.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
polecv(pcv): boolean
    properties: create, query, edit
    Pull all the pole CVs to the same position.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
rampMaxColor(rxc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
rampMinColor(rmc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
refsurface(rs): boolean
    properties: create, query, edit
    Sets on/off the update of the reference surface.
If it is true the reference surface is automatically updated
on the per stroke bases. If it is false, the user has to update
the reference surface explicitly by pressing the update button
(see updaterefsrf).
C: Default is TRUE.  Q: When queried, it returns a boolean.

---
refvector(rv): string
    properties: create, query, edit
    Specifies the direction of the push/pull operation
("normal" - sculpt along normals, "firstnormal" - sculpt along
the first normal of the stroke, "view" - sculpt along the view
direction, "xaxis", "yaxis", "zaxis" - sculpt along a given
axis directions, "uisoparm", "visoparm" - sculpt along U or V
isoparametric lines), "uvvector" - sculpt along an arbitrary
vector in UV space.
C: Default is "normal".  Q: When queried, it returns a string.

---
refvectoru(rvu): float
    properties: create, query, edit
    Specifies the U component of the UV vector to be used
when -refVector is set to "uvvector".

---
refvectorv(rvv): float
    properties: create, query, edit
    Specifies the V component of the UV vector to be used
when -refVector is set to "uvvector".

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
selectedattroper(sao): string
    properties: create, query, edit
    Sets the edit weight operation. Four edit weights
operations are provided : "absolute" - the value of the weight
is replaced by the current one, "additive" - the value of the
weight is added to the current one, "scale" - the value of the
weight is multiplied by the current one, "smooth" - the value
of the weight is divided by the current one.
C: Default is "absolute".  Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
smoothiters(si): int
    properties: create, query, edit
    Sets the quality of the smoothing operation (number of
iterations).
C: Default is 3.  Q: When queried, it returns an int.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
stitchcorner(stc): boolean
    properties: create, query, edit
    Sets on/off the stitching corner mode
C: Default is "off".  Q: When queried, it returns a boolean.

---
stitchedgeflood(sef): boolean
    properties: edit
    Triggers postprocessing stitching edge procedure.

---
stitchtype(stt): string
    properties: create, query, edit
    Sets on/off the stitching mode ( "off" - stitching
is turned off, "position" - position stitching is done without
taking care about the tangent continuity C0, "tan" - C1
continuity is preserved).
C: Default is "position".  Q: When queried, it returns a string.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
toolOffProc(tfp): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned off.
For example, cloth invokes "clothPaintToolOff" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is deactivated.
It is typical that if you implement a toolOffProc you will
want to implement a toolOnProc as well (see the -toolOnProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
toolOnProc(top): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned on.
For example, cloth invokes "clothPaintToolOn" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is activated.
It is typical that if you implement a toolOnProc you will
want to implement a toolOffProc as well (see the -toolOffProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
updateerasesrf(ues): boolean
    properties: create, edit
    Updates the erase surface.

---
updaterefsrf(urs): boolean
    properties: create, edit
    Updates the reference surface.

---
useColorRamp(ucr): boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors.  If this is turned off, the default greyscale feedback
will be used.

---
useMaxMinColor(umc): boolean
    properties: create, query, edit
    Specifies whether the out of range colors should be used.  See rampMinColor
and rampMaxColor flags for further details.

---
useNumericColorRamp(unr) 2024: boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors on the numeric display. If this is turned off, the set single
numeric color will be used.

---
useNumericDisplay(und) 2024: boolean
    properties: create, query, edit
    Specifies whether numerical weight values should be displayed next to
their associated control points.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
value(val): float
    properties: create, query, edit
    Specifies the value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
whichTool(wst): string
    properties: create, query, edit
    The string defines the name of the tool to be
used for the Artisan context. An example is "artClothPaint".
In query mode, the tool name for the given context is returned.
Note: due to the way MEL works, always specify the -query flag
last when specifying a flag that takes arguments.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artPuttyCtx.html 
    """


def artSelectCtx(accopacity: boolean, addselection: boolean, afterStrokeCmd: string, beforeStrokeCmd: string, brushalignment: boolean, brushfeedback: boolean, clear: boolean, dragSlider: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, importthreshold: float, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, name: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, radius: float, record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, screenRadius: float, selectall: boolean, selectclonesource: boolean, selectop: string, showactive: boolean, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, toggleall: boolean, unselectall: boolean, usepressure: boolean, worldRadius: float) -> None:
    """Synopsis:
---
---
 artSelectCtx([accopacity=boolean], [addselection=boolean], [afterStrokeCmd=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean], [clear=boolean], [dragSlider=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [importthreshold=float], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [name=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [radius=float], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float], [selectall=boolean], [selectclonesource=boolean], [selectop=string], [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [toggleall=boolean], [unselectall=boolean], [usepressure=boolean], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artSelectCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a new select context, then switch to it
cmds.artSelectCtx('artSelectCtx1')
cmds.setToolTo('artSelectCtx1')

Set brush's radius to 2.0, lower radius to 0.5
cmds.artSelectCtx('artSelectCtx1', edit=True, r=2.0, lr=0.5)

---


Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
addselection(ads): boolean
    properties: create, query, edit
    If true, each new stroke adds cvs to the active
list. If false, each stroke replaces the previous selection.
C: Default is true. Q: When queried, it returns a boole

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
importthreshold(ift): float
    properties: create, query, edit
    Specifies the threshold for the import of
the attribute maps.
C: Default is 0.5.  Q: When queried, it returns a float.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectall(sal): boolean
    properties: create, edit
    Selects all vertices/egdes/faces/uvs.

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
selectop(sop): string
    properties: create, query, edit
    Specifies the selection operation
("select", "unselect", "toggle").
C: Default is "select". Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
toggleall(tal): boolean
    properties: create, edit
    Toggle all vertices/egdes/faces/uvs.

---
unselectall(ual): boolean
    properties: create, edit
    Unselects all vertices/egdes/faces/uvs.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artSelectCtx.html 
    """


def artSetPaintCtx(accopacity: boolean, afterStrokeCmd: string, beforeStrokeCmd: string, brushalignment: boolean, brushfeedback: boolean, clear: boolean, dragSlider: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, name: string, objectsetnames: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, radius: float, record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, screenRadius: float, selectclonesource: boolean, setcolorfeedback: boolean, setdisplaycvs: boolean, setopertype: string, settomodify: string, showactive: boolean, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, usepressure: boolean, worldRadius: float) -> None:
    """Synopsis:
---
---
 artSetPaintCtx([accopacity=boolean], [afterStrokeCmd=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean], [clear=boolean], [dragSlider=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [name=string], [objectsetnames=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [radius=float], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean], [setcolorfeedback=boolean], [setdisplaycvs=boolean], [setopertype=string], [settomodify=string], [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [usepressure=boolean], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artSetPaintCtx is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

Create a new set membership paint context, then switch to it
cmds.artSetPaintCtx('artSetPaintCtx1')
cmds.setToolTo('artSetPaintCtx1')

Set brush's radius to 2.0, lower radius to 0.5
cmds.artSetPaintCtx('artSetPaintCtx1', edit=True, r=2.0, lr=0.5)

---


Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
objectsetnames(osn): string
    properties: create, query, edit
    Default name of object sets

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
setcolorfeedback(scf): boolean
    properties: create, query, edit
    Specifies if the color feedback is on or off.
C: Default is ON.  Q: When queried, it returns a boolean.

---
setdisplaycvs(dcv): boolean
    properties: create, query, edit
    Specifies if the active cvs are displayed.
C: Default is ON. Q: When queried, it returns a boolean.

---
setopertype(sot): string
    properties: create, query, edit
    Specifies the setEdit operation
("add", "transfer", "remove").
C: Default is "add". Q: When queried, it returns a string.

---
settomodify(stm): string
    properties: create, query, edit
    Specifies the name of the set to modify.
Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artSetPaintCtx.html 
    """


def artUserPaintCtx(accopacity: boolean, activeListChangedProc: string, afterStrokeCmd: string, alphaclamp: string, alphaclamplower: float, alphaclampupper: float, attrSelected: string, beforeStrokeCmd: string, brushalignment: boolean, brushfeedback: boolean, chunkCommand: string, clamp: string, clamplower: float, clampupper: float, clear: boolean, colorAlphaValue: float, colorRGBAValue: tuple[float, float, float, float], colorRGBValue: tuple[float, float, float], colorRamp: string, colorfeedback: boolean, colorfeedbackOverride: boolean, colorrangelower: float, colorrangeupper: float, dataTypeIndex: int, disablelighting: boolean, dragSlider: string, duringStrokeCmd: string, dynclonemode: boolean, exists: boolean, expandfilename: boolean, exportaspectratio: float, exportfilemode: string, exportfilesave: string, exportfilesizex: int, exportfilesizey: int, exportfiletype: string, filterNodes: boolean, finalizeCmd: string, fullpaths: boolean, getArrayAttrCommand: string, getSurfaceCommand: string, getValueCommand: string, history: boolean, image1: string, image2: string, image3: string, importfileload: string, importfilemode: string, importreassign: boolean, initializeCmd: string, interactiveUpdate: boolean, lastRecorderCmd: string, lastStampName: string, lowerradius: float, makeStroke: uint, mappressure: string, maxvalue: float, minvalue: float, name: string, numericColorRamp: string, numericDisplayColor: tuple[float, float, float], numericDisplayPrecision: uint, numericMaxColor: tuple[float, float, float], numericMinColor: tuple[float, float, float], objattrArray: string, objattrArrayNoMenu: string, opacity: float, outline: boolean, outwhilepaint: boolean, paintNodeArray: string, paintattrselected: string, paintmode: string, paintoperationtype: string, pickColor: boolean, pickValue: boolean, playbackCursor: tuple[float, float], playbackPressure: float, preserveclonesource: boolean, profileShapeFile: string, projective: boolean, radius: float, rampMaxColor: tuple[float, float, float], rampMinColor: tuple[float, float, float], record: boolean, reflection: boolean, reflectionaboutorigin: boolean, reflectionaxis: string, screenRadius: float, selectclonesource: boolean, selectedattroper: string, setArrayValueCommand: string, setValueCommand: string, showactive: boolean, stampDepth: float, stampProfile: string, stampSpacing: float, strokesmooth: string, surfaceConformedBrushVertices: boolean, tablet: boolean, tangentOutline: boolean, toolCleanupCmd: string, toolOffProc: string, toolOnProc: string, toolSetupCmd: string, useColorRamp: boolean, useMaxMinColor: boolean, useNumericColorRamp: boolean, useNumericDisplay: boolean, usepressure: boolean, value: float, whichTool: string, worldRadius: float) -> string:
    """Synopsis:
---
---
 artUserPaintCtx([accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float], [attrSelected=string], [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean], [chunkCommand=string], [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean], [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean], [finalizeCmd=string], [fullpaths=boolean], [getArrayAttrCommand=string], [getSurfaceCommand=string], [getValueCommand=string], [history=boolean], [image1=string], [image2=string], [image3=string], [importfileload=string], [importfilemode=string], [importreassign=boolean], [initializeCmd=string], [interactiveUpdate=boolean], [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxvalue=float], [minvalue=float], [name=string], [numericColorRamp=string], [numericDisplayColor=[float, float, float]], [numericDisplayPrecision=uint], [numericMaxColor=[float, float, float]], [numericMinColor=[float, float, float]], [objattrArray=string], [objattrArrayNoMenu=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string], [paintattrselected=string], [paintmode=string], [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean], [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string], [setArrayValueCommand=string], [setValueCommand=string], [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean], [toolCleanupCmd=string], [toolOffProc=string], [toolOnProc=string], [toolSetupCmd=string], [useColorRamp=boolean], [useMaxMinColor=boolean], [useNumericColorRamp=boolean], [useNumericDisplay=boolean], [usepressure=boolean], [value=float], [whichTool=string], [worldRadius=float])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

artUserPaintCtx is undoable, queryable, and editable.
This command executes a scriptable paint (Maya Artisan). It
allows the user to apply Mel commands/scripts to modify cvs'
attributes for all cvs under the paint brush.




Example:
---
import maya.cmds as cmds

create the context
cmds.artUserPaintCtx('artUserPaintCtx')

set the init Mel script
cmds.artUserPaintCtx( 'artUserPaintCtx', e=True, ic='spherePaint' )

---
Return:
---


    string: The name of the context created.

Flags:
---


---
accopacity(aco): boolean
    properties: create, query, edit
    Sets opacity accumulation on/off.
C: Default is false (Except for sculpt tool for which it is true by default).
Q: When queried, it returns a boolean.

---
activeListChangedProc(alp): string
    properties: create, query, edit
    Accepts a string that contains a MEL command that is
invoked whenever the active list changes. There may be some
situations where the UI, for example, needs to be updated,
when objects are selected/deselected in the scene. In query
mode, the name of the currently registered MEL command is
returned and this will be an empty string if none is defined.

---
afterStrokeCmd(asc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately after the end of a stroke.
C: Default is no command. Q: When queried, it returns
the current command

---
alphaclamp(alc): string
    properties: create, query, edit
    Specifies if the weight value should be alpha clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
alphaclamplower(acl): float
    properties: create, query, edit
    Specifies the lower bound for the alpha values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
alphaclampupper(acu): float
    properties: create, query, edit
    Specifies the upper bound for the alpha values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
attrSelected(asl): string
    properties: query
    Returns a name of the currently selected attribute.
Q: When queried, it returns a string.

---
beforeStrokeCmd(bsc): string
    properties: create, query, edit
    The passed string is executed as a MEL command
immediately before the start of a stroke.
C: Default is no command. Q: When queried, it returns the
current command

---
brushalignment(bra): boolean
    properties: create, query, edit
    Specifies the path brush alignemnt. If true,
the brush will align to stroke path, otherwise it will
align to up vector.
C: Default is true. Q: When queried, it returns a boolean.

---
brushfeedback(brf): boolean
    properties: create, query, edit
    Specifies if the brush additional feedback should
be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
chunkCommand(cc): string
    properties: create, query, edit
    Specifies th name of the Mel script/procedure that is
called once for every selected surface when a chunk is
received on that surface.
Q: When queried, it returns a string.

---
clamp(cl): string
    properties: create, query, edit
    Specifies if the weight value should be clamped to
the lower and upper bounds. There are four options here:
"none" - no clamping is performed, "lower" - clamps only to
the lower bound, "upper" - clamps only to the upper bounds,
"both" - clamps to the lower and upper bounds.
C: Default is "none".  Q: When queried, it returns a string.

---
clamplower(cll): float
    properties: create, query, edit
    Specifies the lower bound for the values.
C: Default is 0.0.  Q: When queried, it returns a float.

---
clampupper(clu): float
    properties: create, query, edit
    Specifies the upper bound for the values.
C: Default is 1.0.  Q: When queried, it returns a float.

---
clear(clr): boolean
    properties: create, edit
    Floods all cvs/vertices to the current value.

---
colorAlphaValue(cl1): float
    properties: create, query, edit
    The Alpha value of the color.

---
colorRGBAValue(cl4): [float, float, float, float]
    properties: create, query, edit
    The RGBA value of the color.

---
colorRGBValue(cl3): [float, float, float]
    properties: create, query, edit
    The RGB value of the color.

---
colorRamp(cr): string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors.

---
colorfeedback(cf): boolean
    properties: create, query, edit
    Sets on/off the color feedback display.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorfeedbackOverride(cfo): boolean
    properties: create, query, edit
    Sets on/off the color feedback override.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
colorrangelower(crl): float
    properties: create, query, edit
    Specifies the value that maps to black when
color feedback mode is on.
C: Default is 0.0.  Q: When queried, it returns a float.

---
colorrangeupper(cru): float
    properties: create, query, edit
    Specifies the value that maps to the maximum
color when color feedback mode is on.
C: Default is 1.0.  Q: When queried, it returns a float.

---
dataTypeIndex(dti): int
    properties: query, edit
    When the selected paintable attribute is a vectorArray,
it specifies which field to paint on.

---
disablelighting(dl): boolean
    properties: create, query, edit
    If color feedback is on, this flag determines whether
lighting is disabled or not for the surfaces that are
affected.
C: Default is FALSE.  Q: When queried, it returns a boolean.

---
dragSlider(dsl): string
    properties: create, edit
    Sets the current brush drag state for resizing or
offsetting the brush (like the 'b' and 'm' default hotkeys).
The string argument is one of: "radius", "lowradius",
"opacity", "value", "depth", "displacement", "uvvector"
or "none".
C: Default is "none".

---
duringStrokeCmd(dsk): string
    properties: create, query, edit
    The passed string is executed as a MEL command
during the stroke, each time the mouse is dragged.
C: Default is no command. Q: When queried, it returns
the current command

---
dynclonemode(dcm): boolean
    properties: create, query, edit
    Enable or disable dynamic clone mode.

---
exists(ex): boolean
    properties: create
    Returns true or false depending upon whether the
specified object exists. Other flags are ignored.

---
expandfilename(eef): boolean
    properties: create, edit
    If true, it will expand the name of the export file
and concatenate it with the surface name. Otherwise it
will take the name as it is.
C: Default is true.

---
exportaspectratio(ear): float
    properties: create, query, edit
    Value of aspect ratio for export

---
exportfilemode(efm): string
    properties: create, query, edit
    Specifies the export channel.The valid
entries here are: "alpha", "luminance", "rgb", "rgba".
C: Default is "luminance/rgb".
Q: When queried, it returns a string.

---
exportfilesave(esf): string
    properties: edit
    Exports the attribute map and saves to a specified file.

---
exportfilesizex(fsx): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfilesizey(fsy): int
    properties: create, query, edit
    Specifies the width of the attribute map to export.
C: Default width is 256. Q: When queried, it returns an integer.

---
exportfiletype(eft): string
    properties: create, query, edit
    Specifies the image file format. It can be one of
the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"
"postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".
C: default is tiff. Q: When queried, it returns a string.

---
filterNodes(fon): boolean
    properties: edit
    Sets the node filter.

---
finalizeCmd(fc): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called at the end of each stroke.
Q: When queried, it returns a string.

---
fullpaths(fp): boolean
    properties: create, query, edit
    Specifies whether full path names should
be used when surface names are passed to scripts. If
false, just the surface name is passed.
C: Default is false  Q: When queried, it returns a boolean.

---
getArrayAttrCommand(gac): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called once for every surface that is selected for painting.
This procedure returns a string, which is interpreted
as a list of names referring to double array attributes on some
dependency node.
Q: When queried, it returns a string.

---
getSurfaceCommand(gsc): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called once for every dependency node on the selection list,
whenever Artisan processes the selection list.
It returns the name of the surface to paint on.
Q: When queried, it returns a string.

---
getValueCommand(gvc): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called every time a value on the surface is needed
by the scriptable paint tool.
Q: When queried, it returns a string.

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
importfileload(ifl): string
    properties: edit
    Load the attribute map a specified file.

---
importfilemode(ifm): string
    properties: create, query, edit
    Specifies the channel to import. The valid
entries here are: "alpha", "luminance", "red", "green",
"blue", and "rgb"
C: Default is "alpha". Q: When queried, it returns a string.

---
importreassign(irm): boolean
    properties: create, query, edit
    Specifies if the multiply atrribute maps are to be
reassigned while importing. Only maps previously exported from
within Artisan can be reassigned.
C: Default is FALSE. Q: When queried, it returns a  boolean.

---
initializeCmd(ic): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called in the beginning of each stroke.
Q: When queried, it returns a string.

---
interactiveUpdate(iu): boolean
    properties: create, query, edit
    Specifies how often to transfer the painted values
into the attribute.
TRUE: transfer them "continuously" (many times per stroke)
FALSE: transfer them only at the end of a stroke (on mouse
button release).
C: Default is TRUE. Q: When queried, it returns a boolean.

---
lastRecorderCmd(lrc): string
    properties: create, query, edit
    Value of last recorded command.

---
lastStampName(lsn): string
    properties: create, query, edit
    Value of the last stamp name.

---
lowerradius(lr): float
    properties: create, query, edit
    Sets the lower size of the brush (only apply on tablet).

---
makeStroke(mst): uint
    properties: create, query, edit, multiuse
    Stroke point values.

---
mappressure(mp): string
    properties: create, query, edit
    Sets the tablet pressure mapping when the table
is used. There are three options:
"Opacity" - the pressure is mapped to the opacity,
"Radius" - the is mapped to modify the radius of the brush,
"Both" - the pressure modifies both the opacity and the radius.
C: Default is "Opacity". Q: When queried, it returns a string.

---
maxvalue(mxv): float
    properties: create, query, edit
    Specifies the maximum value for each attribute.
C: Default is 1.0.  Q: When queried, it returns a float.

---
minvalue(miv): float
    properties: create, query, edit
    Specifies the minimum value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
name(n): string
    properties: create
    If this is a tool command, name the tool appropriately.

---
numericColorRamp(ncr) 2024: string
    properties: create, query, edit
    Allows a user defined color ramp to be used to map values to colors for the
numeric display.

---
numericDisplayColor(ndc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a color to be used when displaying numeric values.

---
numericDisplayPrecision(ndp) 2024: uint
    properties: create, query, edit
    Specifies how many decimal points of precision should be used for the
numeric display.

---
numericMaxColor(nxc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
numericMinColor(nmc) 2024: [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
objattrArray(oaa): string
    properties: query
    An array of all paintable attributes. Each element of
the array is a string with the following information:
NodeType.NodeName.AttributeName.MenuType
*MenuType: type (level) of the item in the Menu (UI).
Q: When queried, it returns a string.

---
objattrArrayNoMenu(oan) 2024: string
    properties: query
    Returns an array of all paintable attributes in their original order.
Each element of the array is a string with the following information:
NodeType.NodeName.AttributeName

---
opacity(op): float
    properties: create, query, edit
    Sets the brush opacity.
C: Default is 1.0. Q: When queried, it returns a float.

---
outline(o): boolean
    properties: create, query, edit
    Specifies if the brush should be drawn.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
outwhilepaint(owp): boolean
    properties: create, query, edit
    Specifies if the brush outline should be drawn
while painting.
C: Default is FALSE. Q: When queried, it returns a boolean.

---
paintNodeArray(pna): string
    properties: query
    An array of paintable nodes.
Q: When queried, it returns a string.

---
paintattrselected(pas): string
    properties: edit
    An array of selected paintable attributes.
Each element of the array is a string with the
following information:
NodeType.NodeName.AttributeName.

---
paintmode(pm): string
    properties: create, query, edit
    Specifies the paint mode. There are two
possibilities: "screen" and "tangent".
C: Default is "screen". Q: When queried, it returns a string.

---
paintoperationtype(pot): string
    properties: create, query, edit
    Specifies the operation type used by the
Paint Tool.  Currently, we support the following
paint modes: "Paint", "Smear", "Blur", "Erase"
and "Clone".
Default is "Paint".

---
pickColor(pcm): boolean
    properties: create, query, edit
    Set pick color mode on or off

---
pickValue(pv): boolean
    properties: create, query, edit
    Toggle for picking

---
playbackCursor(plc): [float, float]
    properties: create, query, edit, multiuse
    Values for the playback cursor.

---
playbackPressure(plp): float
    properties: create, query, edit, multiuse
    Valus for the playback pressure.

---
preserveclonesource(pcs): boolean
    properties: create, query, edit
    Whether or not to preserve a clone source.

---
profileShapeFile(psf): string
    properties: query, edit
    Passes a name of the image file for the stamp shape
profile.

---
projective(prm): boolean
    properties: create, query, edit
    Specifies the projective paint mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
radius(r): float
    properties: create, query, edit
    Sets the size of the brush.
C: Default is 1.0 cm. Q: When queried, it returns a float.

---
rampMaxColor(rxc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is greater than or equal to
the maximum value.

---
rampMinColor(rmc): [float, float, float]
    properties: create, query, edit
    Defines a special color to be used when the value is less than or equal to the
minimum value.

---
record(rec): boolean
    properties: create, query, edit
    Toggle on for recording.

---
reflection(rn): boolean
    properties: create, query, edit
    Specifies the reflection mode.
C: Default is 'false'. Q: When queried, it returns a boolean.

---
reflectionaboutorigin(rno): boolean
    properties: create, query, edit
    Toggle on to reflect about the origin

---
reflectionaxis(ra): string
    properties: create, query, edit
    Specifies the reflection axis. There are three
possibilities: "x", "y" and "z".
C: Default is "x". Q: When queried, it returns a string.

---
screenRadius(scR): float
    properties: create, query, edit
    Brush radius on the screen

---
selectclonesource(scs): boolean
    properties: create, query, edit
    Toggle on to select the clone source

---
selectedattroper(sao): string
    properties: create, query, edit
    Sets the edit weight operation. Four edit weights
operations are provided : "absolute" - the value of the weight
is replaced by the current one, "additive" - the value of the
weight is added to the current one, "scale" - the value of the
weight is multiplied by the current one, "smooth" - the value
of the weight is divided by the current one.
C: Default is "absolute".  Q: When queried, it returns a string.

---
setArrayValueCommand(sac): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called for each paint stamp. A stamp may affect
one or more values on the surface. This call rolls up
all the calls that would be made to setValueCommand
for the stamp into one call with array arguments.
Q: When queried, it returns a string.

---
setValueCommand(svc): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called every time a value on the surface is changed.
Q: When queried, it returns a string.

---
showactive(sa): boolean
    properties: create, query, edit
    Sets on/off the display of the surface isoparms.
C: Default is TRUE. Q: When queried, it returns a boolean.

---
stampDepth(stD): float
    properties: create, query, edit
    Depth of the stamps

---
stampProfile(stP): string
    properties: create, query, edit
    Sets the brush profile of the current stamp.
Currently, the following profiles are supported:
"gaussian", "poly", "solid" and "square".
C: Default is gaussian. Q: When queried, it returns a string.

---
stampSpacing(stS): float
    properties: create, query, edit
    Specifies the stamp spacing. Default is 1.0.

---
strokesmooth(ssm): string
    properties: create, query, edit
    Stroke smoothing type name

---
surfaceConformedBrushVertices(scv): boolean
    properties: create, query, edit
    Enables/disables the the display of the effective brush area
as affected vertices.

---
tablet(tab): boolean
    properties: query
    Returns true if the tablet device is present, false if it is absent

---
tangentOutline(to): boolean
    properties: create, query, edit
    Enables/disables the display of the brush circle tangent to
the surface.

---
toolCleanupCmd(tcc): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called when this tool is exited.
Q: When queried, it returns a string.

---
toolOffProc(tfp): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned off.
For example, cloth invokes "clothPaintToolOff" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is deactivated.
It is typical that if you implement a toolOffProc you will
want to implement a toolOnProc as well (see the -toolOnProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
toolOnProc(top): string
    properties: create, query, edit
    Accepts a strings describing the name of a MEL
procedure that is invoked whenever the tool is turned on.
For example, cloth invokes "clothPaintToolOn" when the cloth
paint tool is turned on. Define this callback if your tool
requires special functionality when your tool is activated.
It is typical that if you implement a toolOnProc you will
want to implement a toolOffProc as well (see the -toolOffProc
flag. In query mode, the name of the currently registered MEL
command is returned and this will be an empty string if none
is defined.

---
toolSetupCmd(tsc): string
    properties: create, query, edit
    Specifies the name of the Mel script/procedure
that is called once for every selected surface when an
initial click is received on that surface.
Q: When queried, it returns a string.

---
useColorRamp(ucr): boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors.  If this is turned off, the default greyscale feedback
will be used.

---
useMaxMinColor(umc): boolean
    properties: create, query, edit
    Specifies whether the out of range colors should be used.  See rampMinColor
and rampMaxColor flags for further details.

---
useNumericColorRamp(unr) 2024: boolean
    properties: create, query, edit
    Specifies whether the user defined color ramp should be used to map values
from to colors on the numeric display. If this is turned off, the set single
numeric color will be used.

---
useNumericDisplay(und) 2024: boolean
    properties: create, query, edit
    Specifies whether numerical weight values should be displayed next to
their associated control points.

---
usepressure(up): boolean
    properties: create, query, edit
    Sets the tablet pressure on/off.
C: Default is false. Q: When queried, it returns a boolean.

---
value(val): float
    properties: create, query, edit
    Specifies the value for each attribute.
C: Default is 0.0.  Q: When queried, it returns a float.

---
whichTool(wst): string
    properties: create, query, edit
    The string defines the name of the tool to be
used for the Artisan context. An example is "artClothPaint".
In query mode, the tool name for the given context is returned.
Note: due to the way MEL works, always specify the -query flag
last when specifying a flag that takes arguments.

---
worldRadius(wlR): float
    properties: create, query, edit
    Radius in worldspace

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/artUserPaintCtx.html 
    """


def arubaNurbsToPoly(caching: boolean, constructionHistory: boolean, localSpace: boolean, name: string, nodeState: int, object: boolean, worldSpace: boolean) -> list[string]:
    """Synopsis:
---
---
 arubaNurbsToPoly(
[surface]
    , [caching=boolean], [constructionHistory=boolean], [localSpace=boolean], [name=string], [nodeState=int], [object=boolean], [worldSpace=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

arubaNurbsToPoly is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

To create a new polygonal surface from a NURBS surface:
cmds.arubaNurbsToPoly( 'nurbsSphere1' )

To create a new polygonal surface from a NURBS surface with
history so that the tesselation can be edited afterwards:
cmds.arubaNurbsToPoly( 'nurbsSphere1', ch=True )

---
Return:
---


    list[string]: The polygon and optionally the dependency node name

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
localSpace(ls): boolean
    properties: create
    Tesselate in local space

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
object(o): boolean
    properties: create
    Create the result, or just the dependency node.

---
worldSpace(ws): boolean
    properties: create
    Tesselate in world space

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/arubaNurbsToPoly.html 
    """


def assembly(active: string, activeLabel: string, canCreate: string, createOptionBoxProc: script, createRepresentation: string, defaultType: string, deleteRepresentation: string, deregister: string, input: string, isAType: string, isTrackingMemberEdits: string, label: string, listRepTypes: boolean, listRepTypesProc: script, listRepresentations: boolean, listTypes: boolean, name: string, newRepLabel: string, postCreateUIProc: script, proc: script, renameRepresentation: string, repLabel: string, repName: string, repNamespace: string, repPostCreateUIProc: string, repPreCreateUIProc: string, repType: string, repTypeLabel: string, repTypeLabelProc: script, type: string) -> None:
    """Synopsis:
---
---
 assembly([active=string], [activeLabel=string], [canCreate=string], [createOptionBoxProc=script], [createRepresentation=string], [defaultType=string], [deleteRepresentation=string], [deregister=string], [input=string], [isAType=string], [isTrackingMemberEdits=string], [label=string], [listRepTypes=boolean], [listRepTypesProc=script], [listRepresentations=boolean], [listTypes=boolean], [name=string], [newRepLabel=string], [postCreateUIProc=script], [proc=script], [renameRepresentation=string], [repLabel=string], [repName=string], [repNamespace=string], [repPostCreateUIProc=string], [repPreCreateUIProc=string], [repType=string], [repTypeLabel=string], [repTypeLabelProc=script], [type=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

assembly is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds


---
Create a default type of assembly and name it MyAssembly.
---
The assembly name is optional.
---

cmds.assembly(name='MyAssembly')

---
Create an assembly of type MyAssemblyType and name it MyAssembly.
---

cmds.assembly(name='MyAssembly', type='MyAssemblyType')

---
Set the default type to be MyAssemblyType.
---

cmds.assembly(edit=True, defaultType='MyAssemblyType')

---
Create a representation of type "MyRepType", on assembly myAssembly, and
---
name it "MyRepName"
---

cmds.assembly(myAssembly, edit=True, createRepresentation='MyRepType',
              repName='MyRepName')

---
Rename representation "MyRepName" to "MyNewRepName" on assembly myAssembly.
---

cmds.assembly(myAssembly, edit=True, renameRepresentation='MyRepName',
                      repName='MyNewRepName')

---
Create a representation of type "Locator", on assembly myAssembly, name it
---
"myLocator", and add an annotation using the input flag.
---

cmds.assembly(myAssembly, edit=True, createRepresentation='Locator',
                          repName="myLocator", input="An Annotation")

---
Create a representation of type "Scene", on assembly myAssembly,
---
using file "/path/to/mayafile.mb"
---

cmds.assembly(myAssembly, edit=True, createRepresentation='Scene',
                          input="/path/to/mayafile.mb")


---
Delete scene representation from assembly myAssembly
cmds.assembly(myAssembly, edit=True, deleteRepresentation="mayafile.mb")

---
Delete locator representation from assembly myAssembly
cmds.assembly(myAssembly, edit=True, deleteRepresentation="myLocator")

---
Set the procedure that provides the representation type label for
---
an assembly type.
---

cmds.assembly(edit=True, repTypeLabelProc='MyRepTypeLabelQuery', type='MyAssembly')

---
Set the label for the default assembly type.
---

cmds.assembly(edit=True, label='My Assembly Type')

---
Set the procedure that provides the representation type list which the
---
default assembly supports.
---

cmds.assembly(edit=True, listRepTypesProc='MyRepTypesProc')

---
Set the pre-create UI procedure for a representation type, for a
---
specific type of assembly.
---

cmds.assembly(edit=True, repPreCreateUIProc='MyRepresentation', proc='MyPreCreateProcedure', type='MyAssembly')

---
Set the post-create UI procedure for a representation type, for the
---
default assembly type.
---

cmds.assembly(edit=True, repPostCreateUIProc='MyRepresentation', proc='MyPostCreateProcedure' )

---


Flags:
---


---
active(a): string
    properties: query, edit
    Set the active representation by name, or query the name of the active representation.
Edit mode can be applied to more than one assembly.
Query mode will return a single string when only a single assembly is specified,
and will return an array of strings when multiple assemblies are specified.
Using an empty string as name means to inactivate the currently active representation.

---
activeLabel(al): string
    properties: query, edit
    Set the active representation by label, or query the label of the active representation.
Edit mode can be applied to more than one assembly.
Query mode will return a single string when only a single assembly is specified,
and will return an array of strings when multiple assemblies are specified.

---
canCreate(cc): string
    properties: query
    Query the representation types the specific assembly can create.

---
createOptionBoxProc(cob): script
    properties: query, edit
    Set or query the option box menu procedure for a specific assembly type.
The assembly type will be the default type, unless
the -type flag is used to specify an explicit assembly type.

---
createRepresentation(cr): string
    properties: edit
    Create and add a specific type of representation for an assembly.
If the representation type needs additional parameters, they
must be specified using the "input" flag. For example, the Maya
scene assembly reference implementation Cache and Scene
representations need an input file.

---
defaultType(dt): string
    properties: query, edit
    Set or query the default type of assembly.  When the assembly
command is used to perform an operation on an assembly type rather
than on an assembly object, it will be performed on the default
type, unless the -type flag is used to specify an explicit assembly type.

---
deleteRepresentation(dr): string
    properties: edit
    Delete a specific representation from an assembly.

---
deregister(d): string
    properties: edit
    Deregister a registered assembly type.
If the deregistered type is the default type,
the default type will be set to the empty string.

---
input(input): string
    properties: edit
    Specify the additional parameters of representation creation procedure
when creating a representation.
This flag must be used with createRepresentation flag.

---
isAType(isa): string
    properties: query
    Query whether the given object is of an assembly type.

---
isTrackingMemberEdits(ite): string
    properties: query
    Query whether the given object is tracking member edits.

---
label(lbl): string
    properties: query, edit
    Set or query the label for an assembly type. Assembly type is specified
with flag "type". If no type specified, the default type is used.

---
listRepTypes(lrt): boolean
    properties: query
    Query the supported representation types for a given assembly type.  The
assembly type will be the default type, unless the -type flag is used to
specify an explicit assembly type.

---
listRepTypesProc(lrp): script
    properties: query, edit
    Set or query the procedure that provides the representation type list which
an assembly type supports.  This procedure takes no argument, and
returns a string array of representation types that represents the full set
of representation types this assembly type can create.  The assembly type
for which this procedure applies will be the default type, unless the type
flag is used to specify an explicit assembly type.

---
listRepresentations(lr): boolean
    properties: query
    Query the created representations list for a specific assembly.  The -repType
flag can be used to filter the list and return representations for a
single representation type.  If the -repType flag is not used, all created
representations will be returned.

---
listTypes(lt): boolean
    properties: query
    Query the supported assembly types.

---
name(n): string
    properties: create
    Specify the name of the assembly when creating it.

---
newRepLabel(nrl): string
    properties: edit
    Specify the representation label to set on representation label edit.

---
postCreateUIProc(aoc): script
    properties: query, edit
    Set or query the UI post-creation procedure for a given assembly type.
This procedure will be invoked by Maya immediately after an assembly of the
specified type is created from the UI, but not through scripting.  It can be
used to invoke a dialog, to obtain and set initial parameters on a
newly-created assembly.  The assembly type will be the default type, unless
the -type flag is used to specify an explicit assembly type.

---
proc(prc): script
    properties: edit
    Specify the procedure when setting the representation UI post- or
pre-creation procedure, for a given assembly type.  The assembly
type will be the default type, unless the -type flag is used to specify
an explicit assembly type.

---
renameRepresentation(rnr): string
    properties: edit
    Renames the representation that is the argument to this flag.  The
repName flag must be used to provide the new name.

---
repLabel(rl): string
    properties: query, edit
    Query or edit the label of the representation that is the argument to this
flag, for a given assembly.  In both query and edit modes, the -repLabel flag
specifies the name of the representation.  In edit mode, the -newRepLabel flag
must be used to specify the new representation label.
                        In query mode, this flag needs a value.

---
repName(rnm): string
    properties: edit
    Specify the representation name to set on representation creation or rename.
This flag is optional with the createRepresentation flag: if omitted, the
assembly will name the representation.  It is mandatory with the
renameRepresentation flag.

---
repNamespace(rns): string
    properties: query
    Query the representation namespace of this assembly node.
The value returned is used by Maya for creating the namespace where nodes created
by the activation of a representation will be added. If a name clash occurs when the
namespace is added to its parent namespace, Maya will update repNamespace with the new
name.
Two namespaces are involved when dealing with an assembly node: the namespace of the
assembly node itself (which this flag does not affect or query), and the namespace
of its representations. The representation namespace is a child of its assembly node's
namespace. The assembly node's namespace is set by its containing assembly, if it
is nested, or by the top-level file. Either the assembly node's namespace, or the
representation namespace, or both, can be the empty string.
It should be noted that if the assembly node is nested, the assembly
node's namespace will be (by virtue of its nesting) the
representation namespace of its containing assembly.

---
repPostCreateUIProc(poc): string
    properties: query, edit
    Set or query the UI post-creation procedure for a specific representation type,
and for a specific assembly type.  This procedure takes two arguments, the
first the DAG path to the assembly, and the second the name of the
representation.  It returns no value.  It will be invoked by Maya
immediately after a representation of the specified type is created
from the UI, but not through scripting.  It can be used to invoke a
dialog, to obtain and set initial parameters on a newly-created
representation.  The representation type is the argument of this flag.
The -proc flag must be used to specify the procedure name.  The
assembly type will be the default type, unless the -type flag is used
to specify an explicit assembly type.
                        In query mode, this flag needs a value.

---
repPreCreateUIProc(pec): string
    properties: query, edit
    Set or query the UI pre-creation procedure for a specific representation type,
and for a specific assembly type.  This procedure takes no argument, and
returns a string that is passed as an argument to the -input flag
when Maya invokes the assembly command with the -createRepresentation flag.
The representation pre-creation procedure is invoked by Maya
immediately before creating a representation of the specified type from the
UI, but not through scripting.  It can be used to invoke a dialog, to obtain
the creation argument for a new representation.  The representation type is
the argument of this flag.  The -proc flag must be used to specify the
procedure name.  The assembly type will be the default type, unless the
-type flag is used to specify an explicit assembly type.
                        In query mode, this flag needs a value.

---
repType(rt): string
    properties: query
    Specify a representation type to use as a filter for the -listRepresentations
query.  The representation type is the argument to this flag.
                        In query mode, this flag needs a value.

---
repTypeLabel(rtl): string
    properties: query
    Query the label of the specific representation type.
                        In query mode, this flag needs a value.

---
repTypeLabelProc(rtp): script
    properties: query, edit
    Set or query the procedure that provides the representation type label,
for a given assembly type.  The procedure takes the representation type as
its sole argument, and returns a localized representation type label.
The assembly type for which this procedure applies will be the
default type, unless the -type flag is used to specify an explicit
assembly type.

---
type(typ): string
    properties: create, query, edit
    Set or query properties for the specified registered assembly type.
                        In query mode, this flag needs a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/assembly.html 
    """


def assignCommand(addDivider: string, altModifier: boolean, annotation: string, command: script, commandModifier: boolean, ctrlModifier: boolean, data1: string, data2: string, data3: string, delete: int, dividerString: string, enableCommandRepeat: boolean, factorySettings: boolean, index: int, keyArray: boolean, keyString: string, keyUp: boolean, name: boolean, numDividersPreceding: int, numElements: boolean, optionModifier: boolean, sortByKey: boolean, sourceUserCommands: boolean) -> None:
    """Synopsis:
---
---
 assignCommand(
int
    , [addDivider=string], [altModifier=boolean], [annotation=string], [command=script], [commandModifier=boolean], [ctrlModifier=boolean], [data1=string], [data2=string], [data3=string], [delete=int], [dividerString=string], [enableCommandRepeat=boolean], [factorySettings=boolean], [index=int], [keyArray=boolean], [keyString=string], [keyUp=boolean], [name=boolean], [numDividersPreceding=int], [numElements=boolean], [optionModifier=boolean], [sortByKey=boolean], [sourceUserCommands=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

assignCommand is undoable, queryable, and editable.
This command is obsolete for setting new hotkeys, instead please use the "hotkey" command.




Example:
---
import maya.cmds as cmds

Print out all the names of the named command objects and the
hotkeys attached to them.
---

count = cmds.assignCommand(query=True, numElements=True)
print ('There are ' + str(count) + ' named command objects.')

for index in range(1, count+1):
    keyString = cmds.assignCommand(index, query=True, keyString=True)

    if  0 < len(keyString) and keyString[0] != "NONE":
        displayString = '('

        if "1" == keyString[2]: displayString += 'Ctrl+'
        if "1" == keyString[1]: displayString += 'Alt+'
        if "1" == keyString[5]: displayString += 'Command+'
        if "1" == keyString[6]: displayString += 'Shift+'

        displayString += keyString[0]

        if "1" == keyString[3]: displayString += ' Release'
        if "1" == keyString[4]: displayString += ' KeyRepeat'

        displayString += ')'

        print cmds.assignCommand(index, query=True, name=True), displayString

---


Flags:
---


---
addDivider(ad): string
    properties: edit
    Appends an "annotated divider" item to the end of the list of
commands.

---
altModifier(alt): boolean
    properties: edit
    This flag specifies if an alt modifier is used for the key.

---
annotation(ann): string
    properties: query, edit
    The string is the english name describing the command.

---
command(c): script
    properties: query, edit
    This is the command that is executed when this object is
mapped to a key or menuItem.

---
commandModifier(cmd): boolean
    properties: edit
    This flag specifies if a command modifier is used for the key.
This is only available on systems which support a separate command key.

---
ctrlModifier(ctl): boolean
    properties: edit
    This flag specifies if a ctrl modifier is used for the key.

---
data1(da1): string
    properties: query, edit
    Optional, user-defined data strings may be attached to
the nameCommand objects.

---
data2(da2): string
    properties: query, edit
    Optional, user-defined data strings may be attached to
the nameCommand objects.

---
data3(da3): string
    properties: query, edit
    Optional, user-defined data strings may be attached to
the nameCommand objects.

---
delete(d): int
    properties: edit
    This tells the Manager to delete the object at position index.

---
dividerString(ds): string
    properties: query
    If the passed index corresponds to a "divider" item, then the
divider's annotation is returned.  Otherwise, a null string is
returned.

---
enableCommandRepeat(ecr): boolean
    properties: edit
    This flag specifies whether command repeat is enabled.

---
factorySettings(fs): boolean
    properties: edit
    This flag sets the manager back to factory settings.

---
index(i): int
    properties: edit
    The index of the object to operate on. The index value
ranges from 1 to the number of name command objects.

---
keyArray(ka): boolean
    properties: query
    This flag returns all of the hotkeys on the command.

---
keyString(k): string
    properties: query, edit
    This specifies a key to assign a command to in edit mode.
In query mode this flag returns the key string, modifiers and
indicates if the command is mapped to keyUp or keyDown.

---
keyUp(kup): boolean
    properties: edit
    This flag specifies if the command is executed on keyUp
or keyDown.

---
name(n): boolean
    properties: query
    The name of the command object.

---
numDividersPreceding(ndp): int
    properties: query
    If the index of a namedCommand object C is passed in,
then this flag returns the number of "divider" items preceding
C when the namedCommands are sorted by category.

---
numElements(num): boolean
    properties: query
    This command returns the number of namedCommands in the system.
This flag doesn't require the index to be specified.

---
optionModifier(opt): boolean
    properties: edit
    This flag specifies if an option modifier is used for the key.

---
sortByKey(sbk): boolean
    properties: query, edit
    This key tells the manager to sort by key or by order of
creation.

---
sourceUserCommands(suc): boolean
    properties: edit
    This command sources the user named command file.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/assignCommand.html 
    """


def assignInputDevice(clutch: string, continuous: boolean, device: string, immediate: boolean, multiple: boolean) -> string:
    """Synopsis:
---
---
 assignInputDevice([clutch=string], [continuous=boolean], [device=string], [immediate=boolean], [multiple=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

assignInputDevice is undoable, queryable, and NOT editable.
This command is most useful for associating buttons on a device
with commands.  For using a device to capture continous movements
it is much more efficient to attach the device directly into
the dependency graph.




Example:
---
import maya.cmds as cmds

cmds.assignInputDevice( 'setKeyframe', d='spaceball', c='Button1' )

This command will assign button1 on the spaceball with
the setKeyframe command.  This is very much like using
the spaceball buttons as hotkeys.

cmds.assignInputDevice( '"currentTime -e Axis0"', d='midi', ct=True, m=True )

This command will execute the command to set the time
to the value of the first midi slider.  As the slider
moves this command will be executed.  So the slider
will control time.

---
Return:
---


    string: Command result

Flags:
---


---
clutch(c): string
    properties: create
    specify a clutch button.  This button must be down
for the command string to be executed.
If no clutch is specified the command string is
executed everytime the device state changes

---
continuous(ct): boolean
    properties: create
    if this flag is set the command string is continously
(once for everytime the device changes state).  By
default if a clutch button is specified the command
string is only executed once when the button is
pressed.

---
device(d): string
    properties: create
    specify which device to assign the command string.

---
immediate(im): boolean
    properties: create
    Immediately executes the command, without using the queue.

---
multiple(m): boolean
    properties: create
    if this flag is set the other command strings
associated with this device are not deleted.
By default, when a new command string is attached
to the device, all other command strings are deleted.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/assignInputDevice.html 
    """


def assignViewportFactories(materialFactory: string, nodeType: string, textureFactory: string) -> None:
    """Synopsis:
---
---
 assignViewportFactories([string], [materialFactory=string], [nodeType=string], [textureFactory=string])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

assignViewportFactories is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

To set the viewport factories for all my_material nodes.
---

cmds.assignViewportFactories( materialFactory='solidMaterialInfo', textureFactory='solidTextureInfo', nodeType='my_material' )

---


Flags:
---


---
materialFactory(mf): string
    properties: create, query, edit
    Set or query the materialFactory for the node type.

---
nodeType(nt): string
    properties: create, query, edit
    The node type.

---
textureFactory(tf): string
    properties: create, query, edit
    Set or query the textureFactory for the node type.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/assignViewportFactories.html 
    """


def attachCurve(blendBias: float, blendKnotInsertion: boolean, caching: boolean, constructionHistory: boolean, keepMultipleKnots: boolean, method: int, name: string, nodeState: int, object: boolean, parameter: float, replaceOriginal: boolean, reverse1: boolean, reverse2: boolean) -> list[string]:
    """Synopsis:
---
---
 attachCurve(
curve curve [curve...]
    , [blendBias=float], [blendKnotInsertion=boolean], [caching=boolean], [constructionHistory=boolean], [keepMultipleKnots=boolean], [method=int], [name=string], [nodeState=int], [object=boolean], [parameter=float], [replaceOriginal=boolean], [reverse1=boolean], [reverse2=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attachCurve is undoable, queryable, and editable.
If there are two curves, the end of the first curve is attached to the
start of the second curve. If there are more than two curves, closest
endpoints are joined.

Note: if the command is done with Keep Original off, the first curve
is replaced by the attached curve. All other curves will remain, the
command does not delete them.




Example:
---
import maya.cmds as cmds

Attach the curves and remove the multiple knots:
cmds.attachCurve( 'curve1', 'curve2', kmk=False )

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
on the blend factory being smaller or larger than 0.5.
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
keepMultipleKnots(kmk): boolean
    properties: create, query, edit
    If true, keep multiple knots at the join parameter.
Otherwise remove them.
Default: true

---
method(m): int
    properties: create, query, edit
    Attach method (connect-0, blend-1)
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
reverse1(rv1): boolean
    properties: create, query, edit
    If true, reverse the first input curve before doing attach.
Otherwise, do nothing to the first input curve before attaching.
NOTE: setting this attribute to random values will cause
unpredictable results and is not supported.
Default: false

---
reverse2(rv2): boolean
    properties: create, query, edit
    If true, reverse the second input curve before doing attach.
Otherwise, do nothing to the second input curve before
attaching. NOTE: setting this attribute to random values will
cause unpredictable results and is not supported.
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
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attachCurve.html 
    """


def attachDeviceAttr(attribute: string, axis: string, camera: boolean, cameraRotate: boolean, cameraTranslate: boolean, clutch: string, device: string, selection: boolean) -> None:
    """Synopsis:
---
---
 attachDeviceAttr([attribute=string], [axis=string], [camera=boolean], [cameraRotate=boolean], [cameraTranslate=boolean], [clutch=string], [device=string], [selection=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attachDeviceAttr is undoable, queryable, and NOT editable.



Example:
---
import maya.cmds as cmds

cmds.attachDeviceAttr( 'surface1.translateX', d='spaceball', ax='XAxis' )

This command will assign the XAxis of the spaceball to
the translateX attribute of surface1.  This
assignment is independent of the selection list (i.e.
if surface1 was selected when the command is executed,
surface1 will be translated by the spaceball regardless
of the current selection.)

cmds.attachDeviceAttr( d='spaceball', ax='XAxis', at='translateX' )

This command will assign the XAxis of the spaceball to
the translateX attribute of the selected objects.

cmds.attachDeviceAttr( d='wacom', ax='puck:X', c='puckButton1', at='translateX', sl=True )
cmds.attachDeviceAttr( d='wacom', ax='puck:Y', c='puckButton1', at='translateY', sl=True )

This command will attach the wacom puck X and Y axes to the
X and Y translate attributes of the selected items.
When the selection changes so does the attachment.
The -c option means you can only move the selected items
with the puck when button1 on the puck is down.

---


Flags:
---


---
attribute(at): string
    properties: create, multiuse
    specify the attribute to attach to

---
axis(ax): string
    properties: create
    specify the axis to attach from.

---
camera(cam): boolean
    properties: create
    This flag attaches the device/axis to the current camera.
The mapping between device axes and camera controls is
uses a heuristic based on the device descripton.
The interaction is a copy of the mouse camera navigation
controls.

---
cameraRotate(cr): boolean
    properties: create
    This flag attaches the device/axis to the current cameras
rotation controls.

---
cameraTranslate(ct): boolean
    properties: create
    This flag attaches the device/axis to the current cameras
translate controls.

---
clutch(c): string
    properties: create
    specify a clutch button.  This button must be down
for the command string to be executed.
If no clutch is specified the command string is
executed everytime the device state changes

---
device(d): string
    properties: create
    specify which device to assign the command string.

---
selection(sl): boolean
    properties: create
    This flag attaches to the nodes in the selection list.
This is different from the default arguments of the command
since changing the selection will change the attachments.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attachDeviceAttr.html 
    """


def attachSurface(blendBias: float, blendKnotInsertion: boolean, caching: boolean, constructionHistory: boolean, directionU: boolean, keepMultipleKnots: boolean, method: int, name: string, nodeState: int, object: boolean, parameter: float, replaceOriginal: boolean, reverse1: boolean, reverse2: boolean, swap1: boolean, swap2: boolean, twist: boolean) -> list[string]:
    """Synopsis:
---
---
 attachSurface(
[surface] [surface]
    , [blendBias=float], [blendKnotInsertion=boolean], [caching=boolean], [constructionHistory=boolean], [directionU=boolean], [keepMultipleKnots=boolean], [method=int], [name=string], [nodeState=int], [object=boolean], [parameter=float], [replaceOriginal=boolean], [reverse1=boolean], [reverse2=boolean], [swap1=boolean], [swap2=boolean], [twist=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attachSurface is undoable, queryable, and editable.
The end of the first surface is attached to the start of the second
surface in the specified direction.

Note: if the command is done with Keep Original off there will be an
extra surface in the model (the second surface). The command does not
delete it. The first surface is replaced by the attached surface.




Example:
---
import maya.cmds as cmds

Attach the nurbs planes (in the default U direction) and remove the
multiple knots:
cmds.attachSurface( 'nurbsPlane1', 'nurbsPlane2', kmk=False )

Attach the two active surfaces along the v direction (keeps multiple
knots by default):
cmds.attachSurface( du=False )

---
Return:
---


    list[string]: Object name and node name

Flags:
---


---
blendBias(bb): float
    properties: create, query, edit
    Skew the result toward the first or the second curve depending on the blend factory being smaller or larger than 0.5.
Default: 0.5

---
blendKnotInsertion(bki): boolean
    properties: create, query, edit
    If set to true, insert a knot in one of the original curves (relative position given by the parameter attribute below) in order to produce a slightly different effect.
Default: false

---
caching(cch): boolean
    properties: create, query, edit
    Toggle caching for all attributes so that no recomputation is needed

---
directionU(du): boolean
    properties: create, query, edit
    If true attach in U direction of surface and V direction otherwise.
Default: true

---
keepMultipleKnots(kmk): boolean
    properties: create, query, edit
    If true, keep multiple knots at the join parameter. Otherwise remove them.
Default: true

---
method(m): int
    properties: create, query, edit
    Attach method (connect-0, blend-1)
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
reverse1(rv1): boolean
    properties: create, query, edit
    If true, reverse the direction (specified by directionU) of the first input surface before doing attach. Otherwise, do nothing to the first input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
reverse2(rv2): boolean
    properties: create, query, edit
    If true, reverse the direction (specified by directionU) of the second input surface before doing attach. Otherwise, do nothing to the second input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
swap1(sw1): boolean
    properties: create, query, edit
    If true, swap the UV directions of the first input surface before doing attach. Otherwise, do nothing to the first input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
swap2(sw2): boolean
    properties: create, query, edit
    If true, swap the UV directions of the second input surface before doing attach. Otherwise, do nothing to the second input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
Default: false

---
twist(tw): boolean
    properties: create, query, edit
    If true, reverse the second surface in the opposite direction (specified by directionU) before doing attach. This will avoid twists in the attached surfaces. Otherwise, do nothing to the second input surface before attaching. NOTE: setting this attribute to random values will cause unpredictable results and is not supported.
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
replaceOriginal(rpo): boolean
    properties: create
    Create "in place" (i.e., replace).

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attachSurface.html 
    """


def attrColorSliderGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, alphaValue: float, annotation: string, attrNavDecision: tuple[name, string], attribute: string, backgroundColor: tuple[float, float, float], columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], hsvValue: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, rgbValue: tuple[float, float, float], rowAttach: tuple[int, string, int], showButton: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 attrColorSliderGrp(
groupName
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [alphaValue=float], [annotation=string], [attrNavDecision=[name, string]], [attribute=string], [backgroundColor=[float, float, float]], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [hsvValue=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rgbValue=[float, float, float]], [rowAttach=[int, string, int]], [showButton=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attrColorSliderGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

Create a color slider group consisting of a label, a color canvas,
a slider and a button.  Clicking on the canvas will bring up the
color editor.  If the button is visible, it will allow you to map
a texture to the attribute.




Example:
---
import maya.cmds as cmds

cmds.window( title='Attr Field Slider Groups' )
objName = cmds.shadingNode('phong', asShader=True)
cmds.columnLayout()
cmds.attrColorSliderGrp( at='%s.color' % objName )
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
attrNavDecision(attrNavDecision): [name, string]
    properties: create, query, edit
    The first argument is the name of an attribute.
The button will be attached to the attribute so the button
can be kept in synch with the attribute.  The second
argument is the navigatorDecisionString that can guide the
behaviour that the navigator implements.

---
attribute(at): string
    properties: create, query, edit
    The name of a unique attribute of type 3double.  This newly
created field will be attached to the attribute, so that
modifications to one will change the other.

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
hsvValue(hsv): [float, float, float]
    properties: create, query, edit
    Specifies the color in hsv style.

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
    By default, the label of this field will be the name of the
attribute.  This flag can be used to override that name with
whatever the user wants.

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
    Specifies the color in rgb style.

---
rowAttach(rat): [int, string, int]
    properties: create, edit, multiuse
    Arguments are : column, attachment type, offset.
Possible attachments are: top | bottom | both.
Specifies attachment types and offsets for the entire row.

---
showButton(sb): boolean
    properties: create, query, edit
    Control the display of the texture link button.
True by default (show it).

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attrColorSliderGrp.html 
    """


def attrControlGrp(annotation: string, attribute: name, changeCommand: script, enable: boolean, exists: boolean, handlesAttribute: name, hideMapButton: boolean, label: string, preventOverride: boolean) -> string:
    """Synopsis:
---
---
 attrControlGrp([annotation=string], [attribute=name], [changeCommand=script], [enable=boolean], [exists=boolean], [handlesAttribute=name], [hideMapButton=boolean], [label=string], [preventOverride=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attrControlGrp is NOT undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.attrControlGrp( attribute='defaultResolution.width' )
cmds.showWindow()

---
Return:
---


    string: The control name.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Sets or queries the annotation value of the control group.

---
attribute(a): name
    properties: create, query, edit
    Sets or queries the attribute the control represents. The name of the attribute
must be fully specified, including the name of the node. Some types of
attributes are not supported, but most commonly used attribute types are.

---
changeCommand(cc): script
    properties: create, query, edit
    Sets or queries the change command of the control group. The change
command will be executed when the control is used to change the value
of the attribute.

---
enable(en): boolean
    properties: create, query, edit
    Sets or queries the enable state of the control group. The control is dimmed if
the enable state is set to false.

---
exists(ex): boolean
    properties: create, query, edit
    Returns whether the
specified object exists or not. Other flags are ignored.

---
handlesAttribute(ha): name
    properties: query, edit
    Returns true or false as to whether this command can create a control for the
specified attribute.
                        In query mode, this flag needs a value.

---
hideMapButton(hmb): boolean
    properties: create, query, edit
    Force the map button to remain hidden for this control.

---
label(l): string
    properties: create, query, edit
    Sets or queries the label of the control group.

---
preventOverride(po): boolean
    properties: create, query, edit
    Sets or queries the prevent adjustment state of the control group. If true,
the RMB menu for the control will not allow adjustments to be made.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attrControlGrp.html 
    """


def attrEnumOptionMenu(annotation: string, attribute: name, backgroundColor: tuple[float, float, float], changeCommand: script, defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, enumeratedItem: tuple[int, string], exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 attrEnumOptionMenu(
[string]
    , [annotation=string], [attribute=name], [backgroundColor=[float, float, float]], [changeCommand=script], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enumeratedItem=[int, string]], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attrEnumOptionMenu is undoable, queryable, and editable.



Example:
---
import maya.cmds as cmds

window = cmds.window()
cmds.columnLayout()
node = cmds.createNode('opticalFX')
attrib = node + '.glowType'
cmds.attrEnumOptionMenu( label='Glow Type', attribute=attrib );
cmds.showWindow( window )

---
Return:
---


    string: The full name of the control.

Flags:
---


---
annotation(ann): string
    properties: create, query, edit
    Annotate the control with an extra string value.

---
attribute(at): name
    properties: create, edit
    Attribute that the menu controls.

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
    The command string is executed when the value of the
option menu changes.

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
enumeratedItem(ei): [int, string]
    properties: create, multiuse
    Enumerated item and the corresponding string.  If this flag is
not supplied when the control is created, then the command will
try to read the values from the attribute.

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
    The label text.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attrEnumOptionMenu.html 
    """


def attrEnumOptionMenuGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, attribute: name, backgroundColor: tuple[float, float, float], columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, enumeratedItem: tuple[int, string], exists: boolean, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, rowAttach: tuple[int, string, int], statusBarMessage: string, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 attrEnumOptionMenuGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [attribute=name], [backgroundColor=[float, float, float]], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [enumeratedItem=[int, string]], [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attrEnumOptionMenuGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label and option
menu button associated with an attribute of a node. The attribute
should be an integer, and this control allows a UI association of
strings to the integers of the attribute. When a new menu item is
choosen the corresponding integer will be assigned to the
attribute. 

This control will automatically read the enumeration values from
the attribute if none are provided.




Example:
---
import maya.cmds as cmds

cmds.window()
cmds.columnLayout()
cmds.attrEnumOptionMenuGrp( l='Output Format',
                            at='defaultRenderGlobals.imageFormat',
                            ei=[(0, 'GIF'),(1, 'SoftImage'), (2, 'RLA'),
                                (3, 'TIFF'), (4, 'TIFF16'), (5, 'SGI'),
                                (6, 'Alias PIX'), (7, 'Maya IFF'), (8, 'JPEG'),
                                (9, 'EPS'), (10, 'Maya16 IFF'), (11, 'Cineon'),
                                (12, 'Quantel'), (13, 'SGI16'), (19, 'Targa'),
                                (20, 'BMP') ] )
cmds.showWindow()

---
Return:
---


    string: The full name of the control on creation.

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
attribute(at): name
    properties: create, edit
    The name of an attribute.  The button will be attached
to the attribute so the button can be kept in synch
with the attribute.

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
enumeratedItem(ei): [int, string]
    properties: create, multiuse
    Enumerated item and the corresponding string. If this flag is
not supplied when the control is created, then the command will
try to read the values from the attribute.

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
    Text for the control.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attrEnumOptionMenuGrp.html 
    """


def attrFieldGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, attribute: string, backgroundColor: tuple[float, float, float], changeCommand: script, columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, extraButton: boolean, extraButtonCommand: script, extraButtonIcon: string, extraLabel: string, forceAddMapButton: boolean, fullPathName: boolean, height: int, hideMapButton: boolean, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, maxValue: float, minValue: float, noBackground: boolean, numberOfFields: int, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, precision: int, preventOverride: boolean, rowAttach: tuple[int, string, int], statusBarMessage: string, step: float, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 attrFieldGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [attribute=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraButton=boolean], [extraButtonCommand=script], [extraButtonIcon=string], [extraLabel=string], [forceAddMapButton=boolean], [fullPathName=boolean], [height=int], [hideMapButton=boolean], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean], [numberOfFields=int], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string], [step=float], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attrFieldGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label text, plus two to
four float fields.  These fields will be attached to the
specified vector attribute, so that changes in either will be reflected
in the other.

The fields created here are expression fields -- while normally operating
as a float field, the user can type in any expression starting with
the character "-".

The field also has an automatic menu brought up by the right mouse
button.  The contents of this menu change depending on the state of
the attribute being watched by the field.




Example:
---
import maya.cmds as cmds

   Create an object and a window containing an 'attrFieldGrp' that will
   manipulate the position of that object.
---

object = cmds.sphere()
window = cmds.window(title='attrFieldGrp Example')
cmds.columnLayout()
cmds.attrFieldGrp( attribute='%s.translate' % object[0] )
cmds.showWindow()

---
Return:
---


    string: The full name of the control.

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
attribute(at): string
    properties: create, query, edit
    The name of a unique attribute of type vector.  This newly
created field will be attached to the attribute, so that modifications
to one will change the other.  A "vector" attribute is any
compound attribute whose children consist of two to four double-valued
attributes.

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
    The command string is executed when the value of any of the
floatFields change.

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
extraButton(eb): boolean
    properties: create
    Add an extra icon button to the end of this control (before extra label).

---
extraButtonCommand(ebc): script
    properties: create, edit
    The command string is executed when the extra button is clicked.

---
extraButtonIcon(ebi): string
    properties: create, query, edit
    The icon file name of the extra button.

---
extraLabel(el): string
    properties: create, query, edit
    set an optional string that will be positioned to the right of all the fields.

---
forceAddMapButton(fmb): boolean
    properties: create
    Force adding a map button to this control. If this option is true,
option hideMapButton is suppressed.

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
hideMapButton(hmb): boolean
    properties: create
    Force the map button to remain hidden for this control.

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
    By default, the label of this field will be the name of the
attribute.  This flag can be used to override that name with
whatever the user wants.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxValue(max): float
    properties: create, query, edit
    Sets the maximum value for all fields.

---
minValue(min): float
    properties: create, query, edit
    Sets the minimum value for all fields.

---
noBackground(nbg): boolean
    properties: create, edit
    Clear/reset the control's background.
Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.

---
numberOfFields(nf): int
    properties: create
    sets the number of fields.  Only allowed values are 2 to 4.  If not
specified, defaults to 3.  NOTE: if the -at flag is used when this
widget is created, the number of children in the attribute will determine
the number of fields.  Also note:  after creation, the number of fields cannot
be changed with the -e flag.

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
    properties: create, edit
    Sets the precision for all fields

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
step(s): float
    properties: create, query, edit
    Sets the increment for all fields

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attrFieldGrp.html 
    """


def attrFieldSliderGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, attribute: string, backgroundColor: tuple[float, float, float], changeCommand: script, columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], defineTemplate: string, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, extraButton: boolean, extraButtonCommand: script, extraButtonIcon: string, fieldMaxValue: float, fieldMinValue: float, fieldStep: float, forceAddMapButton: boolean, fullPathName: boolean, height: int, hideMapButton: boolean, highlightColor: tuple[float, float, float], isObscured: boolean, label: string, manage: boolean, maxValue: float, minValue: float, noBackground: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, precision: int, preventOverride: boolean, rowAttach: tuple[int, string, int], sliderMaxValue: float, sliderMinValue: float, sliderStep: float, statusBarMessage: string, step: float, useTemplate: string, vertical: boolean, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 attrFieldSliderGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [attribute=string], [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraButton=boolean], [extraButtonCommand=script], [extraButtonIcon=string], [fieldMaxValue=float], [fieldMinValue=float], [fieldStep=float], [forceAddMapButton=boolean], [fullPathName=boolean], [height=int], [hideMapButton=boolean], [highlightColor=[float, float, float]], [isObscured=boolean], [label=string], [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]], [sliderMaxValue=float], [sliderMinValue=float], [sliderStep=float], [statusBarMessage=string], [step=float], [useTemplate=string], [vertical=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attrFieldSliderGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged collection of label text, float
field and float slider (for values with a min or max specified)
The group
also supports the notion of a larger secondary range of possible
field values.

If an attribute is specified for this object, then it will use any
min and max values defined in the attribute.  The user-specified
values can reduce the min and max, but cannot expand them.

The field created here
is an expression field -- while normally operating
as a float field, the user can type in any expression starting with
the character "=".  This will expand the field to occupy the space
previously taken by the slider.

The field also has
an automatic menu brought up by the right mouse button.
The contents of this menu change depending on the state of
the attribute being watched by the field.





Example:
---
import maya.cmds as cmds

cmds.window( title='Attr Field Slider Groups' )
objName = cmds.sphere()
cmds.columnLayout()
cmds.attrFieldSliderGrp( min=-10.0, max=10.0, at='%s.tx' % objName[0] )
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
attribute(at): string
    properties: create, query, edit
    The name of a unique attribute of type double or int.
This newly created field will be attached to the attribute, so
that modifications to one will change the other.

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
    The command string is executed when the value of the slider
or floatField changes.  It will be executed only once after a
drag of the slider.

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
extraButton(eb): boolean
    properties: create
    Add an extra icon button to the end of this control.

---
extraButtonCommand(ebc): script
    properties: create, edit
    The command string is executed when the extra button is clicked.

---
extraButtonIcon(ebi): string
    properties: create, query, edit
    The icon file name of the extra button.

---
fieldMaxValue(fmx): float
    properties: create, query, edit
    Set the maximum value for the field.  This flag allows you
to specify a maximum bound for the field higher than that
of the slider.   (See note above
about max and min values.)

---
fieldMinValue(fmn): float
    properties: create, query, edit
    Set the minimum value for the field.  This flag allows you
to specify a minimum bound for the field lower than that of
the slider.  (See note above
about max and min values.)

---
fieldStep(fs): float
    properties: create, query, edit
    Sets the increment for the float field.

---
forceAddMapButton(fmb): boolean
    properties: create
    Force adding a map button to this control. If this option is true,
option hideMapButton is suppressed.

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
hideMapButton(hmb): boolean
    properties: create
    Force the map button to remain hidden for this control.

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
    By default, the label of this field will be the name of the
attribute.  This flag can be used to override that name with
whatever string you want.

---
manage(m): boolean
    properties: create, query, edit
    Manage state of the control.  An unmanaged control is
not visible, nor does it take up any screen real estate.  All
controls are created managed by default.

---
maxValue(max): float
    properties: create, query, edit
    Sets the maximum value for both the slider and the field.
(See note above about min and max values)

---
minValue(min): float
    properties: create, query, edit
    Sets the minimum value for both the slider and the field.
(by default max and min are set according to what is in the
attribute, if anything.  If no max and min are specified,
or if only one of the two are specified, then no slider
is created.)

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
    properties: create, edit
    Sets the number of digits to the right of the decimal.
(If attached to an int attribute, this is automatically
set to 0 and cannot be overridden.)

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
sliderMaxValue(smx): float
    properties: create, query, edit
    Set the maximum value for the slider.  The slider
max will be clipped to the field max.

---
sliderMinValue(smn): float
    properties: create, query, edit
    Set the minimum value for the slider.  The slider min
will be clipped to the field min.

---
sliderStep(ss): float
    properties: create, query, edit
    On Linux the slider step value represents the
amount the value will increase or decrease when
you click either side of the slider.

---
statusBarMessage(sbm): string
    properties: create, edit
    Extra string to display in the status bar when the mouse is over the control.

---
step(s): float
    properties: create, query, edit
    Sets the increment for both the slider and float field.

---
useTemplate(ut): string
    properties: create
    Forces the command to use a command template other than
the current one.

---
vertical(vr): boolean
    properties: create, query
    Whether the orientation of the controls in this group
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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attrFieldSliderGrp.html 
    """


def attrNavigationControlGrp(adjustableColumn: int, adjustableColumn2: int, adjustableColumn3: int, adjustableColumn4: int, adjustableColumn5: int, adjustableColumn6: int, annotation: string, attrNavDecision: tuple[name, string], attribute: name, backgroundColor: tuple[float, float, float], columnAlign: tuple[int, string], columnAlign2: tuple[string, string], columnAlign3: tuple[string, string, string], columnAlign4: tuple[string, string, string, string], columnAlign5: tuple[string, string, string, string, string], columnAlign6: tuple[string, string, string, string, string, string], columnAttach: tuple[int, string, int], columnAttach2: tuple[string, string], columnAttach3: tuple[string, string, string], columnAttach4: tuple[string, string, string, string], columnAttach5: tuple[string, string, string, string, string], columnAttach6: tuple[string, string, string, string, string, string], columnOffset2: tuple[int, int], columnOffset3: tuple[int, int, int], columnOffset4: tuple[int, int, int, int], columnOffset5: tuple[int, int, int, int, int], columnOffset6: tuple[int, int, int, int, int, int], columnWidth: tuple[int, int], columnWidth1: int, columnWidth2: tuple[int, int], columnWidth3: tuple[int, int, int], columnWidth4: tuple[int, int, int, int], columnWidth5: tuple[int, int, int, int, int], columnWidth6: tuple[int, int, int, int, int, int], connectAttrToDropped: script, connectNodeToDropped: script, connectToExisting: script, createNew: script, defaultTraversal: script, defineTemplate: string, delete: string, disconnect: script, docTag: string, dragCallback: script, dropCallback: script, enable: boolean, enableBackground: boolean, enableKeyboardFocus: boolean, exists: boolean, extraButton: boolean, extraButtonCommand: script, extraButtonIcon: string, fullPathName: boolean, height: int, highlightColor: tuple[float, float, float], ignore: script, ignoreNotSupported: boolean, isObscured: boolean, label: string, manage: boolean, noBackground: boolean, noIgnorableMenu: boolean, noKeyableMenu: boolean, numberOfPopupMenus: boolean, parent: string, popupMenuArray: boolean, preventOverride: boolean, relatedNodes: script, rowAttach: tuple[int, string, int], statusBarMessage: string, unignore: script, useTemplate: string, visible: boolean, visibleChangeCommand: script, width: int) -> string:
    """Synopsis:
---
---
 attrNavigationControlGrp(
[groupName]
    , [adjustableColumn=int], [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string], [attrNavDecision=[name, string]], [attribute=name], [backgroundColor=[float, float, float]], [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string, string, string, string]], [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int, int]], [connectAttrToDropped=script], [connectNodeToDropped=script], [connectToExisting=script], [createNew=script], [defaultTraversal=script], [defineTemplate=string], [delete=string], [disconnect=script], [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean], [extraButton=boolean], [extraButtonCommand=script], [extraButtonIcon=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]], [ignore=script], [ignoreNotSupported=boolean], [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean], [noIgnorableMenu=boolean], [noKeyableMenu=boolean], [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [relatedNodes=script], [rowAttach=[int, string, int]], [statusBarMessage=string], [unignore=script], [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attrNavigationControlGrp is undoable, queryable, and editable.
All of the group commands position their individual controls in columns
starting at column 1.  The layout of each control (ie. column) can be
customized using the -cw/columnWidth, -co/columnOffset,
-cat/columnAttach, -cal/columnAlign, and
-adj/adjustableColumn flags.  By default, columns are left aligned
with no offset and are 100 pixels wide.  Only one column in any group can
be adjustable.

This command creates a pre-packaged label
navigation button.

The group is used to help the user manage connections to
a particular attribute.

When creating the control you have the opportunity to attach
scripts to the control that are executed on various
UI events.  You can define what happens when the navigation
button is pressed, and when a node is dragged and dropped
onto this attribute.

The navigation button can traverse to the connected node
or can bring up UI to create new connections to the attribute.
The button also can show you state information: if there
already exists a connection/if the connection is ignored.




Example:
---
import maya.cmds as cmds

newNode = cmds.shadingNode( 'blinn', asShader=True )
newNodeAttr = newNode + '.normalCamera'
cmds.window()
cmds.columnLayout()
cmds.attrNavigationControlGrp( l='bump mapping', at=newNodeAttr )
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
attrNavDecision(attrNavDecision): [name, string]
    properties: create, query, edit
    The first argument is the name of an attribute.
The button will be attached to the attribute so the button
can be kept in synch with the attribute.  The second
argument is the navigatorDecisionString that can guide the
behaviour that the navigator implements.

---
attribute(at): name
    properties: create, query, edit
    The name of an attribute. The button will be attached
to the attribute so the button can be kept in synch
with the attribute.

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
connectAttrToDropped(cad): script
    properties: create, query, edit
    The script to execute when a node is dragged and dropped
onto an attribute (multilister dnd attribute editor).
Your script should take in two arguments: the source node
and destination attribute respectively.

---
connectNodeToDropped(cnd): script
    properties: create, query, edit
    The script to execute when a node is dragged and dropped
onto a node (the multilister issues this).  Your script
should take in two arguments: the source node and
destination node respectively.

---
connectToExisting(ce): script
    properties: create, query, edit
    The script to execute when a connection should be
made to an existing node.

---
createNew(cn): script
    properties: create, query, edit
    The script to execute when a new "connection" is
requested.

---
defaultTraversal(dtv): script
    properties: create, query, edit
    The script to execute to find out the name of the default
traversal node.  The script you attach should be able to
take in one argument (the attribute) and return the name
of the node that is the default traversal node.

---
defineTemplate(dt): string
    properties: create
    Puts the command in a mode where any other flags and arguments are
parsed and added to the command template specified in the argument.
They will be used as default arguments in any subsequent
invocations of the command when templateName is set as the
current template.

---
delete(delete): string
    properties: create, query, edit
    The script to execute when the connection (and the node
connected to) should be deleted.

---
disconnect(d): script
    properties: create, query, edit
    The script to execute when a "disconnection" is
requested.

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
extraButton(eb): boolean
    properties: create
    Add an extra icon button to the last of this control.

---
extraButtonCommand(ebc): script
    properties: create, edit
    The command string is executed when the extra button is clicked.

---
extraButtonIcon(ebi): string
    properties: create, query, edit
    The icon file name of the extra button.

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
ignore(i): script
    properties: create, query, edit
    The script to execute when the connection should be
ignored.

---
ignoreNotSupported(ins): boolean
    properties: 
    Obsolete flag; has no effect.

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
    Text for the control.

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
noIgnorableMenu(nim): boolean
    properties: create, edit
    Not show ignorable related popup menu when right click the label.

---
noKeyableMenu(nkm): boolean
    properties: create, edit
    Not show keyable related popup menu when right click the label.

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
relatedNodes(ren): script
    properties: create, query, edit
    The script to execute to find out what the related
nodes are.  The script you attach should be able to
take in one argument (the attribute) and return a list
of strings that are the name of the nodes that are
related.

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
unignore(u): script
    properties: create, query, edit
    The script to execute when the connection should be
unignored.

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
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attrNavigationControlGrp.html 
    """


def attributeInfo(allAttributes: boolean, bool: boolean, enumerated: boolean, hidden: boolean, inherited: boolean, internal: boolean, leaf: boolean, logicalAnd: boolean, multi: boolean, short: boolean, type: string, userInterface: boolean, writable: boolean) -> list[string]:
    """Synopsis:
---
---
 attributeInfo([allAttributes=boolean], [bool=boolean], [enumerated=boolean], [hidden=boolean], [inherited=boolean], [internal=boolean], [leaf=boolean], [logicalAnd=boolean], [multi=boolean], [short=boolean], [type=string], [userInterface=boolean], [writable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attributeInfo is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.createNode( 'choice' )

Get the list of only hidden choice node attributes
---

cmds.attributeInfo( h=True, t='choice' )
Result: [u'message', u'isHistoricallyInteresting', u'binMembership'] ---


Get the list of all attributes on choice nodes
cmds.attributeInfo( all=True, t='choice' )
Result: [u'message', u'caching', u'isHistoricallyInteresting', u'nodeState', u'binMembership', u'selector', u'input', u'output'] ---


Get the list of boolean or enumerated transform node attributes
---

cmds.attributeInfo( b=True, e=True, t='transform' )
Result: [u'caching', u'nodeState', u'visibility', u'intermediateObject', u'template', u'ghosting', u'useObjectColor', u'overrideDisplayType', u'overrideLevelOfDetail', u'overrideShading', u'overrideTexturing', u'overridePlayback', u'overrideEnabled', u'overrideVisibility', u'lodVisibility', u'layerRenderable', u'renderLayerRenderable', u'ghostingMode', u'rotateOrder', u'minTransXLimitEnable', u'minTransYLimitEnable', u'minTransZLimitEnable', u'maxTransXLimitEnable', u'maxTransYLimitEnable', u'maxTransZLimitEnable', u'minRotXLimitEnable', u'minRotYLimitEnable', u'minRotZLimitEnable', u'maxRotXLimitEnable', u'maxRotYLimitEnable', u'maxRotZLimitEnable', u'minScaleXLimitEnable', u'minScaleYLimitEnable', u'minScaleZLimitEnable', u'maxScaleXLimitEnable', u'maxScaleYLimitEnable', u'maxScaleZLimitEnable', u'inheritsTransform', u'displayHandle', u'displayScalePivot', u'displayRotatePivot', u'displayLocalAxis', u'dynamics', u'showManipDefault', u'rotationInterpolation', u'miDeriveFromMaya', u'miHide', u'miVisible', u'miTrace', u'miShadow', u'miCaustic', u'miGlobillum', u'miExportGeoShader'] ---


Get the list of short names of enumerated attributes on a particular choice
node.
---

cmds.attributeInfo( 'choice1', s=True, e=True )
Result: message input output selector

Get the list of hidden or internal attributes on one particular choice node
using the UI name for the attributes (that is the one that will show up
in the attribute editor).
---

cmds.attributeInfo( 'choice1', ui=True, h=True, i=True )
Result: [u'Message', u'Caching', u'Is Historically Interesting', u'Node State', u'Bin Membership'] ---


---
Return:
---


    list[string]: List of attributes matching criteria

Flags:
---


---
allAttributes(all): boolean
    properties: create
    Show all attributes associated with the node regardless of type.
Use of this flag overrides any other attribute type flags and logical operation
that may be specified on the command.

---
bool(b): boolean
    properties: create
    Show the attributes that are of type boolean.
Use the 'on' state to get only boolean attributes; the 'off' state
to ignore boolean attributes.

---
enumerated(e): boolean
    properties: create
    Show the attributes that are of type enumerated.
Use the 'on' state to get only enumerated attributes; the 'off' state
to ignore enumerated attributes.

---
hidden(h): boolean
    properties: create
    Show the attributes that are marked as hidden.
Use the 'on' state to get hidden attributes; the 'off' state
to get non-hidden attributes.

---
inherited(inherited): boolean
    properties: create
    Filter the attributes based on whether they belong to the node type directly
or have been inherited from a root type (e.g. meshShape/direct or
dagObject/inherited).
Use the 'on' state to get only inherited attributes, the 'off' state
to get only directly owned attributes, and leave the flag unspecified to
get both.

---
internal(i): boolean
    properties: create
    Show the attributes that are marked as internal to the node.
Use the 'on' state to get internal attributes; the 'off' state
to get non-internal attributes.

---
leaf(l): boolean
    properties: create
    Show the attributes that are complex leaves (ie. that have parent attributes
and have no children themselves).
Use the 'on' state to get leaf attributes; the 'off' state
to get non-leaf attributes.

---
logicalAnd(logicalAnd): boolean
    properties: create
    The default is to take the logical 'or' of the above conditions.
Specifying this flag switches to the logical 'and' instead.

---
multi(m): boolean
    properties: create
    Show the attributes that are multis.
Use the 'on' state to get multi attributes; the 'off' state
to get non-multi attributes.

---
short(s): boolean
    properties: create
    Show the short attribute names instead of the long names.

---
userInterface(ui): boolean
    properties: create
    Show the UI-friendly attribute names instead of the Maya ASCII names.
Takes precedence over the -s/-short flag if both are specified.

---
writable(w): boolean
    properties: create
    Show the attributes that are writable (ie. can have input connections).
Use the 'on' state to get writable attributes; the 'off' state
to get non-writable attributes.

---
type(t): string
    properties: create
    static node type from which to get 'affects' information

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attributeInfo.html 
    """


def attributeMenu(beginMenu: boolean, editor: string, finishMenu: boolean, inputs: boolean, plug: name, regPulldownMenuCommand: string, unregPulldownMenuCommand: int) -> string:
    """Synopsis:
---
---
 attributeMenu([beginMenu=boolean], [editor=string], [finishMenu=boolean], [inputs=boolean], [plug=name], [regPulldownMenuCommand=string], [unregPulldownMenuCommand=int])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attributeMenu is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

cmds.attributeMenu( 'nodeName', inputs=1, beginMenu=True, editor='editor' )
cmds.attributeMenu( 'nodeName', inputs=0, beginMenu=True, editor='editor' )

---
Return:
---


    string: Command result

Flags:
---


---
beginMenu(beg): boolean
    properties: create
    If true the menu will be used to start a connection edit so it will list all
available attributes for either inputs or outputs.  If false the menu will
be used to complete a connection so it will list only the attributes
compatible with the attribute at the other end of the connection.  A
plug must be supplied in this case.

---
editor(edt): string
    properties: create
    Name of the Hypergraph, Hypershade or Visor editor for which this menu
is being built.  This argument is no longer mandatory. If it is omitted,
the inputs flag and the node must be used to specify the search targets.
This allows attributeMenu to be used in the absence of a hypershade editor.

---
finishMenu(fsh): boolean
    properties: create
    finishes the menu

---
inputs(inp): boolean
    properties: create
    If true only attributes which can be used as inputs will be listed.  If
false only attributes which can be used as outputs will be listed

---
plug(p): name
    properties: create
    If inputs is false then we are completing a connection and the name
of the plug at the other end of the connection must be supplied.

---
regPulldownMenuCommand(rpm): string
    properties: create
    This flag will register a callback that allows the user to define their own popup menu
for a specific node type for use in the Hypershade and Hypergraph editor.
The command signature should look like this:

global proc int proc_name>(string $editorName, string $nodeName, string $plug, string $mode, string $menuType)

The method should return 0 if it does not recognize the node type
and the default attributeMenu popup menu will be displayed.
If the callback returns one then the menu is considered built and no other menuItems will be
added to the popup. The return value from this flag will be the ID to use for the -unregPulldownMenuCommand flag.

---
unregPulldownMenuCommand(upm): int
    properties: create
    This flag will unregister a callback procedure that was registered with the -regPulldownMenuCommand flag.
The argument should be the integer identifier returned from the -regPulldownMenuCommand flag.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attributeMenu.html 
    """


def attributeName(leaf: boolean, long: boolean, nice: boolean, short: boolean) -> string:
    """Synopsis:
---
---
 attributeName([leaf=boolean], [long=boolean], [nice=boolean], [short=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attributeName is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

import maya.cmds as cmds
cmds.attributeName( "persp.tx" )
Result: Translate X ---


cmds.attributeName( "persp.translateX", s=True )
Result: tx ---


cmds.attributeName( "persp.tx", l=True )
Result: translateX ---


cmds.attributeName( "nurbsSphere1.controlPoints[50].xv", leaf=True )
// Result: xValue //

cmds.attributeName( "nurbsSphere1.controlPoints[50].xv", leaf=False )
// Result: Control Points[50].X Value //

---
Return:
---


    string: Command result

Flags:
---


---
leaf(lf): boolean
    properties: create
    When false, shows parent multi attributes (like
"controlPoints[2].xValue").  When true, shows only the
leaf-level attribute name (like "xValue").  Default is true.
Note that for incomplete attribute strings, like a missing
multi-parent index ("controlPoints.xValue") or an
incorrectly named compound (cntrlPnts[2].xValue), this
flag defaults to true and provides a result as long as the
named leaf-level attribute is defined for the node.

---
long(l): boolean
    properties: create
    Returns names in "long name" format like "translateX"

---
nice(n): boolean
    properties: create
    Returns names in "nice name" format like "Translate X"

---
short(s): boolean
    properties: create
    Returns names in "short name" format like "tx"

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attributeName.html 
    """


def attributeQuery(affectsAppearance: boolean, affectsWorldspace: boolean, attributeType: boolean, cachedInternally: boolean, categories: boolean, channelBox: boolean, connectable: boolean, enum: boolean, exists: boolean, hidden: boolean, indeterminant: boolean, indexMatters: boolean, internal: boolean, internalGet: boolean, internalSet: boolean, keyable: boolean, listChildren: boolean, listDefault: boolean, listEnum: boolean, listParent: boolean, listSiblings: boolean, localizedListEnum: boolean, longName: boolean, maxExists: boolean, maximum: boolean, message: boolean, minExists: boolean, minimum: boolean, multi: boolean, niceName: boolean, node: name, numberOfChildren: boolean, range: boolean, rangeExists: boolean, readable: boolean, renderSource: boolean, shortName: boolean, softMax: boolean, softMaxExists: boolean, softMin: boolean, softMinExists: boolean, softRange: boolean, softRangeExists: boolean, storable: boolean, type: string, typeExact: string, usedAsColor: boolean, usedAsFilename: boolean, usesMultiBuilder: boolean, worldspace: boolean, writable: boolean) -> boolean | float[]:
    """Synopsis:
---
---
 attributeQuery([affectsAppearance=boolean], [affectsWorldspace=boolean], [attributeType=boolean], [cachedInternally=boolean], [categories=boolean], [channelBox=boolean], [connectable=boolean], [enum=boolean], [exists=boolean], [hidden=boolean], [indeterminant=boolean], [indexMatters=boolean], [internal=boolean], [internalGet=boolean], [internalSet=boolean], [keyable=boolean], [listChildren=boolean], [listDefault=boolean], [listEnum=boolean], [listParent=boolean], [listSiblings=boolean], [localizedListEnum=boolean], [longName=boolean], [maxExists=boolean], [maximum=boolean], [message=boolean], [minExists=boolean], [minimum=boolean], [multi=boolean], [niceName=boolean], [node=name], [numberOfChildren=boolean], [range=boolean], [rangeExists=boolean], [readable=boolean], [renderSource=boolean], [shortName=boolean], [softMax=boolean], [softMaxExists=boolean], [softMin=boolean], [softMinExists=boolean], [softRange=boolean], [softRangeExists=boolean], [storable=boolean], [type=string], [typeExact=string], [usedAsColor=boolean], [usedAsFilename=boolean], [usesMultiBuilder=boolean], [worldspace=boolean], [writable=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

attributeQuery is NOT undoable, NOT queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

Determine the hidden status of the "selector" attribute on choice nodes.
---

cmds.attributeQuery( 'selector', typ='choice', h=True )
Result: 0

Determine the hidden status of the "selector" attribute on this choice node.
(Usually the same but you can do this for dynamic attributes too.)
---

cmds.createNode( 'choice', n='whoIsIt' )
Result: choice1
cmds.attributeQuery( 'selector', n='whoIsIt', h=True )
Result: 0

Determine the range of the selector value on choice nodes.
In this case there is no range.
Note, if there is only a minimum or only a maximum range will not set.
---

cmds.attributeQuery( 'selector', typ='choice', range=True )

For the next several examples create a poly cube and add extra attributes.
cmds.polyCube( cuv=4, ch=1, w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0, 1, 0) )
cmds.addAttr( '|pCube1', ln='egRange', at='long', min=0, max=5, dv=2 )
cmds.setAttr( '|pCube1.egRange', e=True, keyable=False )

Determine if an attribute is keyable
---

cmds.attributeQuery( 'egRange', node='pCube1', k=True )
Result: 0

Determine the minimum and maximum values of the added attribute egRange
---

cmds.attributeQuery( 'egRange', node='pCube1', range=True )
Result: [0.0, 5.0]

Determine if there is a minimum for the attribute.
Note, having a minimum or maximum value does not imply the attribute has a range.
cmds.addAttr( '|pCube1', ln='egMin', at='long', min=2 )
cmds.attributeQuery( 'egMin', node='pCube1', minExists=True )
Result: 1
cmds.attributeQuery( 'egMin', node='pCube1', maxExists=True )
Result: 0
cmds.attributeQuery( 'egMin', node='pCube1', min=True )
Result: [2.0]

Determine if an attribute is an enum
List the enum strings. This will use ':' as a separator like the attr is written in
an .ma file.
cmds.addAttr( '|pCube1', ln='myEnum', at='enum', en='chicken:turkey:duck:', ct='fowl' )
cmds.attributeQuery( 'myEnum', node='pCube1', listEnum=True )
Result: [u'chicken:turkey:duck'] ---


Secondary way to find an attribute's type directly
cmds.attributeQuery( 'myEnum', node='pCube1', attributeType=True )
Result: ['enum'] ---


See to which categories and attribute belongs
cmds.attributeQuery( 'myEnum', node='pCube1', categories=True )
Result: ['fowl'] ---


---
Return:
---


    float[]: when querying ranges or default values
    boolean: when querying attribute flags

Flags:
---


---
affectsAppearance(aa): boolean
    properties: create
    Return true if the attribute affects the appearance of the node

---
affectsWorldspace(aws): boolean
    properties: create
    Return the status of the attribute flag marking attributes affecting worldspace

---
attributeType(at): boolean
    properties: create
    Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).

---
cachedInternally(ci): boolean
    properties: create
    Return whether the attribute is cached within the node as well as in the datablock

---
categories(ct): boolean
    properties: create
    Return the categories to which the attribute belongs or an empty list if it does not belong to any.

---
channelBox(ch): boolean
    properties: create
    Return whether the attribute should show up in the channelBox or not

---
connectable(c): boolean
    properties: create
    Return the connectable status of the attribute

---
enum(e): boolean
    properties: create
    Return true if the attribute is a enum attribute

---
exists(ex): boolean
    properties: create
    Return true if the attribute exists

---
hidden(h): boolean
    properties: create
    Return the hidden status of the attribute

---
indeterminant(idt): boolean
    properties: create
    Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time

---
indexMatters(im): boolean
    properties: create
    Return the indexMatters status of the attribute

---
internal(i): boolean
    properties: create
    Return true if the attribute is either internalSet or internalGet

---
internalGet(ig): boolean
    properties: create
    Return true if the attribute come from getCachedValue

---
internalSet(internalSet): boolean
    properties: create
    Return true if the attribute must be set through setCachedValue

---
keyable(k): boolean
    properties: create
    Return the keyable status of the attribute

---
listChildren(lc): boolean
    properties: create
    Return the list of children attributes of the given attribute.

---
listDefault(ld): boolean
    properties: create
    Return the default values of numeric and compound numeric attributes.

---
listEnum(le): boolean
    properties: create
    Return the list of enum strings for the given attribute.

---
listParent(lp): boolean
    properties: create
    Return the parent of the given attribute.

---
listSiblings(ls): boolean
    properties: create
    Return the list of sibling attributes of the given attribute.

---
localizedListEnum(lz): boolean
    properties: create
    Return the list of localized enum strings for the given attribute.

---
longName(ln): boolean
    properties: create
    Return the long name of the attribute.

---
maxExists(mxe): boolean
    properties: create
    Return true if the attribute has a hard maximum. A min does not have to be present.

---
maximum(max): boolean
    properties: create
    Return the hard maximum of the attribute's value

---
message(msg): boolean
    properties: create
    Return true if the attribute is a message attribute

---
minExists(mne): boolean
    properties: create
    Return true if the attribute has a hard minimum. A max does not have to be present.

---
minimum(min): boolean
    properties: create
    Return the hard minimum of the attribute's value

---
multi(m): boolean
    properties: create
    Return true if the attribute is a multi-attribute

---
niceName(nn): boolean
    properties: create
    Return the nice name (or "UI name") of the attribute.

---
node(n): name
    properties: create
    Use all attributes from node named NAME

---
numberOfChildren(nc): boolean
    properties: create
    Return the number of children the attribute has

---
range(r): boolean
    properties: create
    Return the hard range of the attribute's value

---
rangeExists(re): boolean
    properties: create
    Return true if the attribute has a hard range. Both min and max must be present.

---
readable(rd): boolean
    properties: create
    Return the readable status of the attribute

---
renderSource(rs): boolean
    properties: create
    Return whether this attribute is marked as a render source or not

---
shortName(sn): boolean
    properties: create
    Return the short name of the attribute.

---
softMax(smx): boolean
    properties: create
    Return the soft max (slider range) of the attribute's value

---
softMaxExists(sxe): boolean
    properties: create
    Return true if the attribute has a soft maximum. A min does not have to be present.

---
softMin(smn): boolean
    properties: create
    Return the soft min (slider range) of the attribute's value

---
softMinExists(sme): boolean
    properties: create
    Return true if the attribute has a soft minimum. A max does not have to be present.

---
softRange(s): boolean
    properties: create
    Return the soft range (slider range) of the attribute's value

---
softRangeExists(se): boolean
    properties: create
    Return true if the attribute has a soft range. Both min and max must be present.

---
storable(st): boolean
    properties: create
    Return true if the attribute is storable

---
type(typ): string
    properties: create
    Use static attributes from nodes of type TYPE.  Includes attributes inherited from parent class nodes.

---
typeExact(tex): string
    properties: create
    Use static attributes only from nodes of type TYPE.  Does not included inherited attributes.

---
usedAsColor(uac): boolean
    properties: create
    Return true if the attribute should bring up a color picker

---
usedAsFilename(uaf): boolean
    properties: create
    Return true if the attribute should bring up a file browser

---
usesMultiBuilder(umb): boolean
    properties: create
    Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data

---
worldspace(ws): boolean
    properties: create
    Return the status of the attribute flag marking worldspace attribute

---
writable(w): boolean
    properties: create
    Return the writable status of the attribute

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/attributeQuery.html 
    """


def audioTrack(insertTrack: uint, lock: boolean, mute: boolean, numTracks: uint, removeEmptyTracks: boolean, removeTrack: uint, solo: boolean, swapTracks: tuple[uint, uint], title: string, track: uint) -> None:
    """Synopsis:
---
---
 audioTrack([insertTrack=uint], [lock=boolean], [mute=boolean], [numTracks=uint], [removeEmptyTracks=boolean], [removeTrack=uint], [solo=boolean], [swapTracks=[uint, uint]], [title=string], [track=uint])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

audioTrack is undoable, queryable, and editable.


Example:
---
import maya.cmds as cmds

 Move the audio clip named "audio2" to track 3
---

cmds.audioTrack( 'audio2', track=3 )

Lock the track containing the audio clip named "audio1"
---

cmds.audioTrack( 'audio1', lock=True )

Remove any empty tracks
---

cmds.audioTrack(removeEmptyTracks=True)

audioTrack -q -track audio1;
---

cmds.audioTrack( 'audio1', q=True, track=True )

---


Flags:
---


---
insertTrack(it): uint
    properties: create
    This flag is used to insert a new empty track at the track index specified. Indices are 1-based.

---
lock(l): boolean
    properties: create, query, edit
    This flag specifies whether all audio clips on the same track as the specified audio node are to be locked at their current location and track.

---
mute(m): boolean
    properties: create, query, edit
    This flag specifies whether all audio clips on the same track as the specified audio node are to be muted or not.

---
numTracks(nt): uint
    properties: query
    To query the number of audio tracks

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
    This flag specifies whether all audio clips on the same track as the specified audio node are to be soloed or not.

---
swapTracks(st): [uint, uint]
    properties: create
    This flag is used to swap the contents of two specified tracks. Indices are 1-based.

---
title(t): string
    properties: create, query, edit
    This flag specifies the title for the track.

---
track(tr): uint
    properties: create, query, edit
    Specify the track on which to operate by using the track's trackNumber.
                        In query mode, this flag needs a value.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/audioTrack.html 
    """


def autoKeyframe(addAttr: name, characterOption: string, listAttr: boolean, noReset: boolean, state: boolean) -> int:
    """Synopsis:
---
---
 autoKeyframe([addAttr=name], [characterOption=string], [listAttr=boolean], [noReset=boolean], [state=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

autoKeyframe is undoable, queryable, and editable.
autoKeyframe does not create new animation curves.  An attribute
must have already been keyframed (with the setKeyframe command)
for autoKeyframe to  add new keyframes for modified attributes.

You can also query the current state of autoKeyframing
with "autoKeyframe -query -state".




Example:
---
import maya.cmds as cmds

Start remembering attributes that have changed
---

cmds.autoKeyframe( state=True )

Set a keyframe for all attributes that have changed
since the last "autoKeyframe( state=True )
---

cmds.autoKeyframe()

Stop remembering attributes that have changed.
Note that Subsequent "autoKeyframe" commands
(with no flags) will have no effect until an
autoKeyframe( state=True ) command is executed.
---

cmds.autoKeyframe( state=False )

List the plugs that will be considered to add a key on completion of the
next set attribute.
cmds.autoKeyframe(query=True, listAttr=True)

Add to the list the plugs that will be considered to add a key on
completion of the next set attribute.
cmds.autoKeyframe(edit=True, addAttr='myNode.myAttr')

When auto-keying, key all character attributes, not just
those that have changed.
---

cmds.autoKeyframe( characterOption="all" )

---
Return:
---


    int: Number of keyframes set.

Flags:
---


---
addAttr(aa): name
    properties: edit
    Add to the list of plugs (node.attribute) that autoKeyframe is currently
considering for auto keying.  This list is transient and short-lived, and
is reset as soon as autoKeyframe sets the keyframe or decides that no
keyframe is to be set, on completion of the next set attribute.

---
characterOption(co): string
    properties: create, query, edit
    Valid options are: "standard", "all". Dictates whether
when auto-keying characters the auto-key works as usual or whether
it keys all of the character attributes. Default is "standard".

---
listAttr(lsa): boolean
    properties: query
    Returns the list of plugs (node.attribute) that autoKeyframe is currently
considering for auto keying.  This list is transient and short-lived, and
is reset as soon as autoKeyframe sets the keyframe or decides that no
keyframe is to be set, on completion of the next set attribute.

---
noReset(nr): boolean
    properties: create, edit
    Must be used in conjunction with the state/st flag.
When noReset/nr is specified, the list of plugs to be autokeyed
is not cleared when the state changes

---
state(st): boolean
    properties: create, query, edit
    turns on/off remembering of modified attributes

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/autoKeyframe.html 
    """


def autoPlace(useMouse: boolean) -> float[]:
    """Synopsis:
---
---
 autoPlace([useMouse=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

autoPlace is undoable, NOT queryable, and NOT editable.um/useMouse



Example:
---
import maya.cmds as cmds

   Move the scene around a bit so the grid is no longer
   centered in the view.
---

cmds.track( right=10 )
cmds.track( down=10 )

   Create a sphere.
---

sphere = cmds.sphere()

   Reposition the sphere so that it is in the center of the
   view.
---

position = cmds.autoPlace()
cmds.move( position[0], position[1], position[2], sphere[0], relative=True )

---
Return:
---


    float[]: Placement location in 3D space

Flags:
---


---
useMouse(um): boolean
    properties: create
    Use the current mouse position rather than the centre of the
active view.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/autoPlace.html 
    """


def autoSave(destination: int, destinationFolder: boolean, enable: boolean, folder: string, interval: float, limitBackups: boolean, maxBackups: int, perform: boolean, prompt: boolean) -> None:
    """Synopsis:
---
---
 autoSave([destination=int], [destinationFolder=boolean], [enable=boolean], [folder=string], [interval=float], [limitBackups=boolean], [maxBackups=int], [perform=boolean], [prompt=boolean])  
Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis.

autoSave is undoable, queryable, and NOT editable.


Example:
---
import maya.cmds as cmds

set the interval between auto-saves to 5 minutes
---

cmds.autoSave( int=300 )

query the auto-save interval
---

cmds.autoSave( q=True, int=True )
Result: 300.0 ---


---


Flags:
---


---
destination(dst): int
    properties: create, query
    Sets the option for where auto-save files go.
0 - auto-saves go into the workspace autosave folder
1 - auto-saves go into the named folder (set with the -folder flag)
2 - auto-saves go into a folder set by an environment variable (MAYA_AUTOSAVE_FOLDER)

---
destinationFolder(df): boolean
    properties: query
    Queries the actual destination folder for auto-saves, based on the current
setting of the -destination flag, workspace rules and environment variables.
Resolves environment variables etc. and makes any relative path
absolute (resolved relative to the workspace root).
The returned string will end with a trailing separator ('/').

---
enable(en): boolean
    properties: create, query
    Enables or disables auto-saves.

---
folder(fol): string
    properties: create, query
    Sets the folder for auto-saves used if the destination option is 1.

---
interval(int): float
    properties: create, query
    Sets the interval between auto-saves (in seconds).
The default interval is 600 seconds (10 minutes).

---
limitBackups(lim): boolean
    properties: create, query
    Sets whether the number of auto-save files is limited.

---
maxBackups(max): int
    properties: create, query
    Sets the maximum number of auto-save files, if limiting is in effect.

---
perform(p): boolean
    properties: create
    Invokes the auto-save process.

---
prompt(prm): boolean
    properties: create, query
    Sets whether the auto-save prompts the user before auto-saving.

URL:
---
https://help.autodesk.com/cloudhelp/2024/ENU/Maya-Tech-Docs/CommandsPython/autoSave.html 
    """
